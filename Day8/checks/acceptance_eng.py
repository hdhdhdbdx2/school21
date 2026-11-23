"""The original check. Run the unmodified copy kept by the reviewer."""
import argparse
import asyncio
import json
import sqlite3
import sys
import tempfile
from pathlib import Path
from fastmcp import Client
from fastmcp.client.transports import StdioTransport
from jsonschema import validate

HERE = Path(__file__).resolve().parent
REFERENCE = json.loads((HERE / "tools_reference_eng.json").read_text(encoding="utf-8"))
SPECS = {t["name"]: t for t in REFERENCE["tools"]}
SEED = HERE / "fixture_eng.sql"
TABLES = ("products", "stock", "users", "orders")

def normalized(value):
    if isinstance(value, dict):
        return {k: normalized(v) for k,v in value.items()
                if k not in ("title", "$schema") and not (k == "required" and v == [])}
    if isinstance(value, list):
        return [normalized(v) for v in value]
    return value

def snapshot(db):
    with sqlite3.connect(db) as con:
        return {t: sorted(con.execute("SELECT * FROM " + t).fetchall()) for t in TABLES}

def reset(db):
    with sqlite3.connect(db) as con:
        con.executescript(
            "DELETE FROM orders; DELETE FROM stock; DELETE FROM users; DELETE FROM products;"
        )
        con.executescript(SEED.read_text(encoding="utf-8"))

def sql(db, command, args=()):
    with sqlite3.connect(db) as con:
        return con.execute(command, args).fetchall()

async def check(project, profile):
    contract = json.loads((project / "contracts/tools_schemas_eng.json").read_text(encoding="utf-8"))
    submitted = {t["name"]:t for t in contract["tools"]}
    assert len(contract["tools"]) == 7 and set(submitted) == set(SPECS), "Seven unique tools are needed"
    for name, spec in SPECS.items():
        text = submitted[name]["description"]
        assert isinstance(text,str) and text.strip() and "TODO" not in text, name + ": fill in the description"
        for field in ("inputSchema", "outputSchema"):
            assert normalized(submitted[name][field]) == normalized(spec[field]), name + ": the contract has been changed"

    calls = 0
    with tempfile.TemporaryDirectory(prefix="shop-check-") as temp:
        db = Path(temp) / "check_eng.db"
        server_log = Path(temp) / "server_eng.log"
        def connection():
            return Client(StdioTransport(
                command=sys.executable, args=["-m", "src.server_eng", "--db", str(db), "--seed", str(SEED)],
                cwd=str(project), log_file=server_log), timeout=15)

        try:
            async with connection() as client:
                remote = {t.name:t for t in await client.list_tools()}
                assert set(remote) == set(SPECS), "The server must have exactly seven mandatory tools"
                for name, tool in remote.items():
                    assert normalized(tool.inputSchema) == normalized(SPECS[name]["inputSchema"]), name + ": server input schema"
                    assert normalized(tool.outputSchema) == normalized(SPECS[name]["outputSchema"]), name + ": server response schema"
                    assert tool.description == submitted[name]["description"], name + ": the description did not reach the client"
                print("OK — seven contracts are published by the server")

                async def call(name, args=None):
                    nonlocal calls
                    calls += 1
                    result = await client.call_tool(name,args or {},raise_on_error=False)
                    assert not result.is_error, name + ": " + str(result.content)
                    data = result.structured_content
                    validate(data, SPECS[name]["outputSchema"])
                    return data

                async def ok(name, args=None):
                    answer = await call(name,args)
                    assert answer["ok"], name + ": " + str(answer)
                    return answer["data"]

                async def refused(name, args, code):
                    before = snapshot(db)
                    answer = await call(name,args)
                    assert answer["ok"] is False and answer["error"]["code"] == code, name + ": expected " + code + ", got " + str(answer)
                    assert snapshot(db) == before, name + ": the data changed after a refusal"

                def purchase(user="student_01", product="bottle", size="one_size", quantity=1):
                    return {"user_id":user,"product_id":product,"size":size,"quantity":quantity}

                before = snapshot(db)
                products = (await ok("list_products"))["products"]
                assert [x["id"] for x in products] == ["bottle","hoodie","stickers","tote","tshirt"], 'The catalog is incomplete or the product order is broken'
                hoodie = await ok("get_product",{"product_id":"hoodie"})
                assert hoodie["price_coins"] == 500 and hoodie["stock"]["M"] == 5, 'The initial hoodie price or stock is wrong'
                assert (await ok("get_coin_balance",{"user_id":"student_01"}))["balance"] == 1000, 'The initial balance of student_01 must be 1000'
                assert snapshot(db) == before, "Reading changed the data"
                await refused("get_product",{"product_id":"missing"},"PRODUCT_NOT_FOUND")
                await refused("get_coin_balance",{"user_id":"missing"},"USER_NOT_FOUND")
                for name in ("get_order_status","cancel_order","confirm_pickup"):
                    await refused(name,{"order_id":"missing"},"ORDER_NOT_FOUND")
                print("OK — reading and unknown identifiers")

                order = await ok("create_order", {"user_id":"student_01","product_id":"bottle","size":"one_size"})
                assert order["status"] == "created" and order["total_price"] == 150, 'A bottle must create a created order costing 150'
                oid = order["order_id"]
                assert sql(db,"SELECT coins FROM users WHERE id='student_01'")[0][0] == 850, 'After buying a bottle, the balance must be 850'
                assert sql(db,"SELECT quantity FROM stock WHERE product_id='bottle'")[0][0] == 11, 'After buying one bottle, the stock must be 11'
                assert sql(db,"SELECT total_price,status FROM orders WHERE id=?",(oid,))[0] == (150,"created"), 'The order is not recorded with the cost 150 and the created status'
                assert (await ok("get_order_status",{"order_id":oid}))["status"] == "created", 'A new order must have the created status'
                await ok("cancel_order",{"order_id":oid})
                refund = 135 if profile == "E3" else 150
                assert sql(db,"SELECT coins FROM users WHERE id='student_01'")[0][0] == 850+refund, 'Wrong balance after cancellation for the selected profile'
                assert sql(db,"SELECT quantity FROM stock WHERE product_id='bottle'")[0][0] == 12, 'Cancellation must fully return the bottle stock to 12'
                await refused("cancel_order",{"order_id":oid},"ORDER_STATUS_ERROR")
                await refused("confirm_pickup",{"order_id":oid},"ORDER_STATUS_ERROR")
                print("OK — purchase, cancellation, and a one-time refund")

                reset(db)
                oid = (await ok("create_order",purchase()))["order_id"]
                before_money = sql(db,"SELECT coins FROM users ORDER BY id")
                before_stock = sql(db,"SELECT * FROM stock ORDER BY product_id,size")
                await ok("confirm_pickup",{"order_id":oid})
                assert (await ok("get_order_status",{"order_id":oid}))["status"] == "picked_up", 'After pickup, the status must be picked_up'
                assert sql(db,"SELECT coins FROM users ORDER BY id") == before_money, 'Pickup changed the balance again'
                assert sql(db,"SELECT * FROM stock ORDER BY product_id,size") == before_stock, 'Pickup changed the stock again'
                await refused("confirm_pickup",{"order_id":oid},"ORDER_STATUS_ERROR")
                await refused("cancel_order",{"order_id":oid},"ORDER_STATUS_ERROR")
                print("OK — pickup without a repeated charge")

                reset(db)
                for args, code in [
                    (purchase(user="missing"),"USER_NOT_FOUND"),
                    (purchase(product="missing"),"PRODUCT_NOT_FOUND"),
                    (purchase(product="hoodie",size="XXL"),"OUT_OF_STOCK"),
                    (purchase(quantity=100),"OUT_OF_STOCK"),
                    (purchase(user="student_poor"),"INSUFFICIENT_COINS"),
                    (purchase(product="hoodie",size="M",quantity=2),"USER_LIMIT_EXCEEDED"),
                ]:
                    await refused("create_order",args,code)
                oid = (await ok("create_order",purchase(product="hoodie",size="S")))["order_id"]
                await ok("confirm_pickup",{"order_id":oid})
                await refused("create_order",purchase(product="hoodie",size="M"),"USER_LIMIT_EXCEEDED")
                reset(db)
                await ok("create_order",purchase(product="hoodie",size="XL"))
                await refused("create_order",purchase(user="student_02",product="hoodie",size="XL"),"OUT_OF_STOCK")
                print("OK — balance, stock, and the limit across all sizes")

                reset(db)
                invalid = [purchase(quantity=q) for q in (0,-1,1.5,"2",True)]
                invalid += [{"product_id":"bottle","size":"one_size"},
                            {**purchase(),"extra":"unknown"},purchase(user=""),
                            {**purchase(),"product_id":12}]
                for args in invalid:
                    before = snapshot(db)
                    calls += 1
                    result = await client.call_tool("create_order",args,raise_on_error=False)
                    assert result.is_error, "Invalid input accepted: " + str(args)
                    assert snapshot(db) == before, "Invalid input changed the data"
                print("OK — wrong types, quantity, and request fields")

                # Cancellation uses the saved cost and returns the product in full.
                reset(db)
                sql(db,"UPDATE products SET price_coins=151 WHERE id='bottle'")
                oid = (await ok("create_order",purchase()))["order_id"]
                sql(db,"UPDATE products SET price_coins=9999 WHERE id='bottle'")
                await ok("cancel_order",{"order_id":oid})
                expected = 1000-151+(151*9//10 if profile == "E3" else 151)
                assert sql(db,"SELECT coins FROM users WHERE id='student_01'")[0][0] == expected, 'Wrong refund: use the saved cost and the profile rule'
                assert sql(db,"SELECT quantity FROM stock WHERE product_id='bottle'")[0][0] == 12, 'Cancellation must fully return the bottle stock to 12'

                reset(db)
                sql(db,"UPDATE users SET coins=180 WHERE id='student_01'")
                if profile == "E1":
                    await refused("create_order",purchase(),"INSUFFICIENT_COINS")
                else:
                    await ok("create_order",purchase())
                reset(db)
                sql(db,"UPDATE users SET coins=200 WHERE id='student_01'")
                await ok("create_order",purchase())
                assert sql(db,"SELECT coins FROM users WHERE id='student_01'")[0][0] == 50, 'A purchase at the 50-coin balance boundary is calculated incorrectly'

                reset(db)
                if profile == "E2":
                    await refused("create_order",purchase(product="stickers",quantity=3),"USER_LIMIT_EXCEEDED")
                else:
                    order = await ok("create_order",purchase(product="stickers",quantity=3))
                    assert order["total_price"] == (135 if profile == "E4" else 150), 'The price of three sticker packs does not match the profile'
                reset(db)
                order = await ok("create_order",purchase(product="stickers",quantity=2))
                assert order["total_price"] == 100, 'Two sticker packs must cost 100'
                if profile == "E4":
                    reset(db)
                    sql(db,"UPDATE products SET price_coins=51 WHERE id='stickers'")
                    order = await ok("create_order",purchase(product="stickers",quantity=3))
                    assert order["total_price"] == 137, 'E4: the cost of 3 units at 51 must round down to 137'
                    assert sql(db,"SELECT coins FROM users WHERE id='student_01'")[0][0] == 863, 'E4: the charge does not match the discounted price'
                reset(db)
                oid = (await ok("create_order",purchase(product="hoodie",size="M")))["order_id"]
                if profile == "E5":
                    await refused("cancel_order",{"order_id":oid},"ORDER_STATUS_ERROR")
                else:
                    await ok("cancel_order",{"order_id":oid})
                    # Cancellation frees up the limit, including another size.
                    await ok("create_order",purchase(product="hoodie",size="S"))
                print("OK — profile rules " + profile)

                # An artificial write failure checks the rollback of an already started transaction.
                reset(db)
                sql(db,"CREATE TRIGGER check_fail BEFORE INSERT ON orders BEGIN SELECT RAISE(ABORT,'test rollback'); END")
                before = snapshot(db)
                calls += 1
                failed = await client.call_tool("create_order",purchase(),raise_on_error=False)
                assert failed.is_error, "An artificial write failure must be visible to the client"
                assert snapshot(db) == before, "A partially written purchase after the failure"
                sql(db,"DROP TRIGGER check_fail")
                print("OK — rollback of an incomplete write")

                reset(db)
                saved_order = (await ok("create_order",purchase()))["order_id"]
                before_restart = snapshot(db)
            async with connection() as restarted:
                result = await restarted.call_tool("get_order_status",{"order_id":saved_order})
                calls += 1
                assert result.structured_content["data"]["status"] == "created", 'After a restart, the new order is not found in the created state'
                assert snapshot(db) == before_restart, "The restart reset the state"
            print("OK — the state survives a restart")
        except Exception:
            print("Check the first failed scenario and the selected profile.",file=sys.stderr)
            raise
    print("PASS — profile " + profile + ", tool calls: " + str(calls))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project",required=True,type=Path)
    parser.add_argument("--profile",choices=["base","E1","E2","E3","E4","E5"],default="base")
    args = parser.parse_args()
    try:
        asyncio.run(check(args.project.resolve(),args.profile))
    except Exception as exc:
        print("FAIL — " + str(exc),file=sys.stderr)
        raise SystemExit(1)

if __name__ == "__main__":
    main()

