"""Workstation readiness check. Does not install or change anything."""
import importlib
import importlib.metadata
import sqlite3
import sys

print("Command: python3")
print("Interpreter:", sys.executable)
print("Version:", sys.version.split()[0])
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
    errors.append("Capability check: " + str(exc))
if errors:
    print("The environment is not ready. Give this output to the staff:")
    print("\n".join(errors))
    raise SystemExit(1)
print("The required modules are available. Run python3 client_eng.py demo.")

