# Envelope E5 Hoodies on Pre-order

A message from the Shop:

«We pass hoodies on for packing right after the order. We’re temporarily closing hoodie cancellation. The rest of the merch follows the previous rules».

## The new condition

An order of the product with `product_id = "hoodie"` can’t be cancelled even in the `created` state. The response is `ORDER_STATUS_ERROR`; the balance, stock, and status are kept.

A created hoodie order can be picked up. Cancellation of other products works as before. For a non-existent order, `ORDER_NOT_FOUND` is still returned.

The rule is determined by the product identifier, not by its display name in the catalog. The tool schemas don’t change.

## Your work

Write down the forecast of the files. Add the new condition and two tests: a hoodie cancellation is rejected, a bottle cancellation remains available. The first attempt is 45 minutes; AI and a search engine are available.

~~~bash
python3 -m pytest -c pytest_eng.ini -q
python3 checks/acceptance_eng.py --project . --profile E5
~~~

The submission profile is E5.

