"""Ish joyi tayyorligini tekshirish. Hech narsa o‘rnatmaydi va o‘zgartirmaydi."""
import importlib
import importlib.metadata
import sqlite3
import sys

print("Buyruq: python3")
print("Interpretator:", sys.executable)
print("Versiya:", sys.version.split()[0])
errors = []
for name in ("fastmcp", "pytest"):
    try:
        importlib.import_module(name)
        print(name + ":", importlib.metadata.version(name))
    except Exception as exc:
        errors.append(name + ": " + str(exc))
try:
    from fastmcp import Client, FastMCP
    from fastmcp.client.transports import StdioTransport
    from pydantic import Field
    with sqlite3.connect(":memory:") as con:
        con.execute("SELECT 1").fetchone()
except Exception as exc:
    errors.append("Imkoniyatlarni tekshirish: " + str(exc))
if errors:
    print("Muhit tayyor emas. Bu chiqishni xodimlarga bering:")
    print("\n".join(errors))
    raise SystemExit(1)
print("Kerakli modullar mavjud. python3 client.py demo ni ishga tushiring.")

