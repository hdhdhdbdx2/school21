# The Shop Rules and Tools

## Data

| Identifier | Product | Price | Limit per participant | Stock |
| --- | --- | --- | --- | --- |
| hoodie | Hoodie | 500 | 1 | S 3, M 5, L 2, XL 1 |
| tshirt | T-shirt | 250 | 2 | S 10, M 8, L 6, XL 4 |
| stickers | Stickers | 50 | 5 | one_size 50 |
| bottle | Bottle | 150 | 2 | one_size 12 |
| tote | Tote bag | 100 | 3 | one_size 20 |

The users are entered into the database in advance: `student_01` — 1000 coins, `student_02` — 300, `student_poor` — 20. Reading the balance doesn’t create a new user. For an unknown user, `USER_NOT_FOUND` is returned.

The price and quantity are integers. One order contains one product of one size. The default quantity is 1. The limit is counted as the sum of units of this product in all of the user’s orders with the `created` and `picked_up` statuses, across all sizes. Cancellation frees up the limit.

When an order is created, the server writes the cost into the order. When an order is cancelled, the saved cost is used, not the current catalog price. In the basic version, the full amount is refunded.

## Responses

Success: `{"ok": true, "data": {...}}`.

A refusal under a Shop rule: `{"ok": false, "error": {"code": "OUT_OF_STOCK", "message": "Not enough stock"}}`. Phrase the message text clearly; the check compares the code, not the exact phrase.

A wrong argument type or a quantity less than 1 is rejected at the MCP input before the handler is called. Such a protocol response has `isError` set; the client shows it as a request error. This is a separate case, not one of the Shop codes. The string "2", the fraction 1.5, and true aren’t an integer quantity.

## Contracts

All arguments are mandatory except `quantity`. Identifiers and the size are non-empty strings. The names of the fields in data are given below; the full schemas are in `contracts/tools_schemas_eng.json`.

| Tool | Arguments | Fields in data |
| --- | --- | --- |
| list_products | None | products — a list of products |
| get_product | product_id | id, name, price_coins, user_limit, stock |
| get_coin_balance | user_id | user_id, balance |
| create_order | user_id, product_id, size, quantity = 1 | order_id, status, total_price |
| get_order_status | order_id | order_id, status |
| cancel_order | order_id | order_id, status |
| confirm_pickup | order_id | order_id, status |

`stock` is a dictionary of sizes and stock; an element of `products` has the same fields as `get_product`. The catalog is returned in the order of identifiers. `order_id` is a new non-empty string assigned by the server.

## Purchase

The checks are performed in this order:

1. The user exists — otherwise `USER_NOT_FOUND`.
2. The product exists — otherwise `PRODUCT_NOT_FOUND`.
3. The size exists and there’s enough stock — otherwise `OUT_OF_STOCK`.
4. The new order doesn’t exceed the limit, taking previous ones into account — otherwise `USER_LIMIT_EXCEEDED`.
5. There are enough coins for the full cost — otherwise `INSUFFICIENT_COINS`.

After all the checks, the server creates the order and reduces the balance and the stock. These three changes are made in one transaction: either all of them are saved, or none.

A repeated purchase call is considered a new order and goes through all the checks again. Protection against repeats using a special key isn’t part of the mandatory part.

## Order states

From `created`, you can go to `cancelled` or `picked_up`. There are no transitions from `cancelled` and `picked_up`.

An unknown order — `ORDER_NOT_FOUND`. A repeated cancellation, a repeated pickup, picking up a cancelled order, and cancelling a picked-up order — `ORDER_STATUS_ERROR`.

Cancellation returns the stock and the coins exactly once. Pickup changes only the status: the product and the coins were already charged at creation.

With any refusal, the products, stock, users, and orders tables keep their previous values. Reading doesn’t change them either.

## Boundaries of the training service

The project has no real payments and no real orders. The users are training ones; sign-in and identity verification aren’t implemented. The client can pass any of the training identifiers. This must be written down explicitly in the datasheet so that the next developer doesn’t mistake the service for a system with access control.

The server runs locally, and the calls in the checks go one after another. Simultaneous purchases by several clients, delivery, changing the catalog via MCP, and personal accounts aren’t part of the mandatory part.

An envelope changes one rule. Tool names and the structures of their responses stay the same. The new rule and the check profile must be stated in the datasheet.

