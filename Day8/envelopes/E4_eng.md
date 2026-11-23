# Envelope E4 A Quantity Discount

A message from the Shop:

«Let’s test a small promotion: when buying three or more units of one product, we’ll give a ten percent discount».

## The new condition

For a quantity of 3 or more, the total cost is `price * quantity * 9 // 10`. The total cost of the whole order is rounded down. For quantities 1 and 2, the price stays the same.

Three sticker packs at 50 cost 135. If the price of one unit is 51, three cost 137. The personal limits and stock are kept: the promotion doesn’t allow buying three hoodies with a limit of 1.

The balance check, the charge, and the recorded cost use the discounted amount. On cancellation, exactly the charged amount is refunded. The tool schemas and response fields don’t change.

## Your work

Write down the forecast of the files, change the calculation, and add a test that distinguishes the old price from the discount. The first attempt is 45 minutes; AI and a search engine are available.

~~~bash
python3 -m pytest -c pytest_eng.ini -q
python3 checks/acceptance_eng.py --project . --profile E4
~~~

The submission profile is E4.

