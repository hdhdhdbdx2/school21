# Envelope E2 No More Than Two at a Time

A message from the Shop:

«A queue has formed at the pickup point. For now, let’s limit one order to two units of a product».

## The new condition

One order may contain no more than two units. An order with a quantity of 3 or more gets `USER_LIMIT_EXCEEDED`, even if the personal limit of the product is higher.

For example, you can’t buy three sticker packs at a time, but you can buy two. Through several separate orders, a participant can still get up to five sticker packs: the overall product limit is kept.

The new cap is checked together with the personal limit, after the stock availability and before the balance. The price, the refund, the tool schemas, and the minimum quantity of 1 don’t change.

## Your work

Before the change, write down the expected files in `docs/change_eng.md`. Implement the rule and add tests for quantities 2 and 3. The first attempt is 45 minutes. AI and a search engine are available.

~~~bash
python3 -m pytest -c pytest_eng.ini -q
python3 checks/acceptance_eng.py --project . --profile E2
~~~

The submission profile with the change completed is E2.

