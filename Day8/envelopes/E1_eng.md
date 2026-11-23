# Envelope E1 A Protected Minimum Balance

A message from the Shop:

«Participants spend everything on merch and then find out that they still need coins for other activities. After a new purchase, at least 50 coins must remain on the balance».

## The new condition

A purchase can be made if 50 coins or more remain after the charge. Exactly 50 is acceptable. If less remains, return `INSUFFICIENT_COINS`. Nothing can be changed before the charge.

A participant with a balance of 180 can’t buy a bottle for 150. With a balance of 200, they can.

The previous checks of the user, product, size, and limit are kept and come before the balance check. Cancellation refunds the full cost. Tool names, arguments, and response fields don’t change.

## Your work

Before the change, write down the expected files in `docs/change_eng.md`. Implement the condition, add a test of the refusal and of the boundary case. The first attempt is 45 minutes. AI and a search engine are available.

~~~bash
python3 -m pytest -c pytest_eng.ini -q
python3 checks/acceptance_eng.py --project . --profile E1
~~~

If you’re submitting this change, specify E1 in the instructions, the datasheet, and the envelope report.

