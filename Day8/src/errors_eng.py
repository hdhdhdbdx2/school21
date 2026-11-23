"""The Shop responses. Protocol errors are handled by FastMCP."""
def success(data):
    return {"ok": True, "data": data}

def failure(code, message):
    return {"ok": False, "error": {"code": code, "message": message}}

