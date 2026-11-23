# How the Server Works

The client starts the server as a separate process and communicates with it through the standard streams — this connection method is called stdio. A separate port and a browser aren’t needed. FastMCP already handles the message exchange.

## Three parts of your code

**Handlers** receive a tool call, get the necessary data, apply the rules, and choose an action. For reading, it’s `read_handlers_eng.py`, for changing an order — `order_handlers_eng.py`. No SQL is written here.

**Rules** in `domain_eng.py` work with numbers and dictionaries. They calculate the amount and decide whether an action is allowed. These functions can be tested without the database and without MCP.

**Storage** in `storage_eng.py` reads and writes SQLite. SQL uses query parameters. Related writes are done in one transaction. It isn’t decided here who is entitled to a discount or whether an order can be cancelled.

The ready-made wrapper is `server_eng.py` and `mcp_adapter_eng.py`. It starts the server, registers the tools, and checks the input types. You don’t need to change it in the mandatory part.

## The path of the ready-made call

In `mcp_adapter_eng.py`, find `get_product`. It calls `read_handlers_eng.get_product`, and the handler calls `Storage.get_product`. The storage method executes a SELECT. The handler turns the result into a successful response or an error.

See the difference for yourself:

~~~bash
python3 client_eng.py call get_product '{"product_id":"hoodie"}'
python3 client_eng.py call get_product '{"product_id":"missing"}'
~~~

The `logs/client_eng.jsonl` log contains the tool name, the arguments, and the received response for each client call. It’s a trace of a real run. It doesn’t prove that all the other requests are correct.

## Transaction

Inside `with connection:`, you can execute several SQL commands. If it finishes normally, they’re committed; in case of an exception, they’re rolled back. Don’t put a separate commit between charging the coins and writing the order.

Initialization adds the source data only to a new database. A regular restart must not restore the spent coins and stock.

