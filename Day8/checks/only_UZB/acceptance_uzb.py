"""Boshlang‘ich tekshiruv. Tekshiruvchining o‘zgartirilmagan nusxasini ishga tushiring."""
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
REFERENCE = json.loads((HERE / "tools_reference.json").read_text(encoding="utf-8"))
SPECS = {t["name"]: t for t in REFERENCE["tools"]}
SEED = HERE / "fixture.sql"
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
    contract = json.loads((project / "contracts/tools_schemas.json").read_text(encoding="utf-8"))
    submitted = {t["name"]:t for t in contract["tools"]}
    assert len(contract["tools"]) == 7 and set(submitted) == set(SPECS), "Yettita takrorlanmas vosita kerak"
    for name, spec in SPECS.items():
        text = submitted[name]["description"]
        assert isinstance(text,str) and text.strip() and "TODO" not in text, name + ": tavsifni to‘ldiring"
        for field in ("inputSchema", "outputSchema"):
            assert normalized(submitted[name][field]) == normalized(spec[field]), name + ": kontrakt o‘zgartirilgan"

    calls = 0
    with tempfile.TemporaryDirectory(prefix="lavka-check-") as temp:
        db = Path(temp) / "check.db"
        server_log = Path(temp) / "server.log"
        def connection():
            return Client(StdioTransport(
                command=sys.executable, args=["-m", "src.server", "--db", str(db), "--seed", str(SEED)],
                cwd=str(project), log_file=server_log), timeout=15)

        try:
            async with connection() as client:
                remote = {t.name:t for t in await client.list_tools()}
                assert set(remote) == set(SPECS), "Serverda aynan yettita majburiy vosita bo‘lishi kerak"
                for name, tool in remote.items():
                    assert normalized(tool.inputSchema) == normalized(SPECS[name]["inputSchema"]), name + ": server kirish sxemasi"
                    assert normalized(tool.outputSchema) == normalized(SPECS[name]["outputSchema"]), name + ": server javob sxemasi"
                    assert tool.description == submitted[name]["description"], name + ": tavsif mijozga yetib bormadi"
                print("OK — yettita kontrakt serverda e’lon qilingan")

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
                    assert answer["ok"] is False and answer["error"]["code"] == code, name + ": kutilgan " + code + ", olingan " + str(answer)
                    assert snapshot(db) == before, name + ": rad etishdan keyin ma’lumotlar o‘zgardi"

                def purchase(user="student_01", product="bottle", size="one_size", quantity=1):
                    return {"user_id":user,"product_id":product,"size":size,"quantity":quantity}

                before = snapshot(db)
                products = (await ok("list_products"))["products"]
                assert [x["id"] for x in products] == ["bottle","hoodie","stickers","tote","tshirt"], 'Katalog to‘liq emas yoki tovarlar tartibi buzilgan'
                hoodie = await ok("get_product",{"product_id":"hoodie"})
                assert hoodie["price_coins"] == 500 and hoodie["stock"]["M"] == 5, 'Xudining boshlang‘ich narxi yoki qoldig‘i noto‘g‘ri'
                assert (await ok("get_coin_balance",{"user_id":"student_01"}))["balance"] == 1000, 'student_01 ning boshlang‘ich balansi 1000 bo‘lishi kerak'
                assert snapshot(db) == before, "O‘qish ma’lumotlarni o‘zgartirdi"
                await refused("get_product",{"product_id":"missing"},"PRODUCT_NOT_FOUND")
                await refused("get_coin_balance",{"user_id":"missing"},"USER_NOT_FOUND")
                for name in ("get_order_status","cancel_order","confirm_pickup"):
                    await refused(name,{"order_id":"missing"},"ORDER_NOT_FOUND")
                print("OK — o‘qish va noma’lum identifikatorlar")

                order = await ok("create_order", {"user_id":"student_01","product_id":"bottle","size":"one_size"})
                assert order["status"] == "created" and order["total_price"] == 150, 'Butilka created holatida qiymati 150 bo‘lgan buyurtma yaratishi kerak'
                oid = order["order_id"]
                assert sql(db,"SELECT coins FROM users WHERE id='student_01'")[0][0] == 850, 'Butilka xarididan keyin balans 850 bo‘lishi kerak'
                assert sql(db,"SELECT quantity FROM stock WHERE product_id='bottle'")[0][0] == 11, 'Bitta butilka xarididan keyin qoldiq 11 bo‘lishi kerak'
                assert sql(db,"SELECT total_price,status FROM orders WHERE id=?",(oid,))[0] == (150,"created"), 'Buyurtma 150 qiymati va created holati bilan yozilmagan'
                assert (await ok("get_order_status",{"order_id":oid}))["status"] == "created", 'Yangi buyurtma created holatida bo‘lishi kerak'
                await ok("cancel_order",{"order_id":oid})
                refund = 135 if profile == "E3" else 150
                assert sql(db,"SELECT coins FROM users WHERE id='student_01'")[0][0] == 850+refund, 'Tanlangan profil uchun bekor qilishdan keyingi balans noto‘g‘ri'
                assert sql(db,"SELECT quantity FROM stock WHERE product_id='bottle'")[0][0] == 12, 'Bekor qilish butilkalar qoldig‘ini to‘liq 12 ga qaytarishi kerak'
                await refused("cancel_order",{"order_id":oid},"ORDER_STATUS_ERROR")
                await refused("confirm_pickup",{"order_id":oid},"ORDER_STATUS_ERROR")
                print("OK — xarid, bekor qilish va bir martalik qaytarish")

                reset(db)
                oid = (await ok("create_order",purchase()))["order_id"]
                before_money = sql(db,"SELECT coins FROM users ORDER BY id")
                before_stock = sql(db,"SELECT * FROM stock ORDER BY product_id,size")
                await ok("confirm_pickup",{"order_id":oid})
                assert (await ok("get_order_status",{"order_id":oid}))["status"] == "picked_up", 'Berilgandan keyin holat picked_up bo‘lishi kerak'
                assert sql(db,"SELECT coins FROM users ORDER BY id") == before_money, 'Berish balansni qayta o‘zgartirdi'
                assert sql(db,"SELECT * FROM stock ORDER BY product_id,size") == before_stock, 'Berish qoldiqlarni qayta o‘zgartirdi'
                await refused("confirm_pickup",{"order_id":oid},"ORDER_STATUS_ERROR")
                await refused("cancel_order",{"order_id":oid},"ORDER_STATUS_ERROR")
                print("OK — qayta yechishsiz berish")

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
                print("OK — balans, ombor va barcha o‘lchamlar bo‘yicha limit")

                reset(db)
                invalid = [purchase(quantity=q) for q in (0,-1,1.5,"2",True)]
                invalid += [{"product_id":"bottle","size":"one_size"},
                            {**purchase(),"extra":"unknown"},purchase(user=""),
                            {**purchase(),"product_id":12}]
                for args in invalid:
                    before = snapshot(db)
                    calls += 1
                    result = await client.call_tool("create_order",args,raise_on_error=False)
                    assert result.is_error, "Noto‘g‘ri kirish qabul qilindi: " + str(args)
                    assert snapshot(db) == before, "Noto‘g‘ri kirish ma’lumotlarni o‘zgartirdi"
                print("OK — noto‘g‘ri turlar, miqdor va so‘rov maydonlari")

                # Bekor qilish saqlangan qiymatdan foydalanadi va tovarni to‘liq qaytaradi.
                reset(db)
                sql(db,"UPDATE products SET price_coins=151 WHERE id='bottle'")
                oid = (await ok("create_order",purchase()))["order_id"]
                sql(db,"UPDATE products SET price_coins=9999 WHERE id='bottle'")
                await ok("cancel_order",{"order_id":oid})
                expected = 1000-151+(151*9//10 if profile == "E3" else 151)
                assert sql(db,"SELECT coins FROM users WHERE id='student_01'")[0][0] == expected, 'Qaytarish noto‘g‘ri: saqlangan qiymat va profil qoidasidan foydalaning'
                assert sql(db,"SELECT quantity FROM stock WHERE product_id='bottle'")[0][0] == 12, 'Bekor qilish butilkalar qoldig‘ini to‘liq 12 ga qaytarishi kerak'

                reset(db)
                sql(db,"UPDATE users SET coins=180 WHERE id='student_01'")
                if profile == "E1":
                    await refused("create_order",purchase(),"INSUFFICIENT_COINS")
                else:
                    await ok("create_order",purchase())
                reset(db)
                sql(db,"UPDATE users SET coins=200 WHERE id='student_01'")
                await ok("create_order",purchase())
                assert sql(db,"SELECT coins FROM users WHERE id='student_01'")[0][0] == 50, '50 koin qoldig‘i chegarasidagi xarid noto‘g‘ri hisoblangan'

                reset(db)
                if profile == "E2":
                    await refused("create_order",purchase(product="stickers",quantity=3),"USER_LIMIT_EXCEEDED")
                else:
                    order = await ok("create_order",purchase(product="stickers",quantity=3))
                    assert order["total_price"] == (135 if profile == "E4" else 150), 'Uchta stiker to‘plamining narxi profilga mos emas'
                reset(db)
                order = await ok("create_order",purchase(product="stickers",quantity=2))
                assert order["total_price"] == 100, 'Ikkita stiker to‘plami 100 turishi kerak'
                if profile == "E4":
                    reset(db)
                    sql(db,"UPDATE products SET price_coins=51 WHERE id='stickers'")
                    order = await ok("create_order",purchase(product="stickers",quantity=3))
                    assert order["total_price"] == 137, 'E4: har biri 51 dan 3 birlik qiymati 137 gacha pastga yaxlitlanishi kerak'
                    assert sql(db,"SELECT coins FROM users WHERE id='student_01'")[0][0] == 863, 'E4: yechilgan summa chegirmali narxga mos emas'
                reset(db)
                oid = (await ok("create_order",purchase(product="hoodie",size="M")))["order_id"]
                if profile == "E5":
                    await refused("cancel_order",{"order_id":oid},"ORDER_STATUS_ERROR")
                else:
                    await ok("cancel_order",{"order_id":oid})
                    # Bekor qilish limitni, jumladan, boshqa o‘lcham uchun ham bo‘shatadi.
                    await ok("create_order",purchase(product="hoodie",size="S"))
                print("OK — profil qoidalari " + profile)

                # Sun’iy yozish nosozligi boshlangan tranzaksiyaning ortga qaytarilishini tekshiradi.
                reset(db)
                sql(db,"CREATE TRIGGER check_fail BEFORE INSERT ON orders BEGIN SELECT RAISE(ABORT,'test rollback'); END")
                before = snapshot(db)
                calls += 1
                failed = await client.call_tool("create_order",purchase(),raise_on_error=False)
                assert failed.is_error, "Sun’iy yozish nosozligi mijozga ko‘rinishi kerak"
                assert snapshot(db) == before, "Nosozlikdan keyin qisman yozilgan xarid"
                sql(db,"DROP TRIGGER check_fail")
                print("OK — to‘liq bo‘lmagan yozuvni ortga qaytarish")

                reset(db)
                saved_order = (await ok("create_order",purchase()))["order_id"]
                before_restart = snapshot(db)
            async with connection() as restarted:
                result = await restarted.call_tool("get_order_status",{"order_id":saved_order})
                calls += 1
                assert result.structured_content["data"]["status"] == "created", 'Qayta ishga tushirgandan keyin yangi buyurtma created holatida topilmadi'
                assert snapshot(db) == before_restart, "Qayta ishga tushirish holatni boshlang‘ich holatga qaytardi"
            print("OK — holat qayta ishga tushirilganda saqlanadi")
        except Exception:
            print("Birinchi o‘tmagan ssenariy va tanlangan profilni tekshiring.",file=sys.stderr)
            raise
    print("PASS — profil " + profile + ", vosita chaqiruvlari: " + str(calls))

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

