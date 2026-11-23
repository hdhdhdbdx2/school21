# Envelope E3 A Cancellation Fee

A message from the Shop:

«We’ve already packed the order, and then it gets cancelled. From now on, when an order is cancelled, we refund 90 percent of the coins charged».

## The new condition

When a created order is cancelled, refund 90% of its saved cost, rounding the refund amount down to a whole coin. Formula: `total_price * 9 // 10`.

For a bottle costing 150, 135 coins will be refunded. If 151 was charged from the participant, 135 will be refunded too. The product is returned in full. The limit is freed up, as before.

A repeated cancellation refunds nothing. An order that has been picked up can’t be cancelled. A change in the current product price doesn’t affect the refund for an already created order.

The schemas don’t change: `cancel_order` still returns only `order_id` and `status` inside data. Show the refund amount by the change in the balance via `get_coin_balance`.

## Your work

Write down the forecast of the files, make the change, and add a test of the rounding or of the one-time refund. The first 45 minutes are the team’s attempt; AI and a search engine are available.

~~~bash
python3 -m pytest -c pytest_eng.ini -q
python3 checks/acceptance_eng.py --project . --profile E3
~~~

If your old test expected a full refund, update this expectation and explain the reason in `docs/change_eng.md`. The submission profile is E3.

