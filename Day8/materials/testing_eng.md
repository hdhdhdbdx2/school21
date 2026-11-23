# How to Check the Server

A test is code with input data and a check of the expected result. `testing/test_example_eng.py` has an example on the ready-made tool: it creates a temporary database and checks the returned product. To run:

~~~bash
python3 -m pytest -c pytest_eng.ini -q
~~~

An example of a check of the cost rule after it’s implemented:

~~~python
from src.domain_eng import calculate_total

def test_two_bottles_cost_300():
    assert calculate_total(150, 2) == 300
~~~

If the function returned a different number, assert will stop the test, and pytest will show which expectation was violated. Save such code in a file whose name starts with test_ and ends with _eng.py.

Add your own tests. Choose at least three meaningful cases: a correct cost calculation; a purchase refusal with an unchanged state; a repeated action with an order. This is minimal help in development, not a guarantee of completeness. A separate test of the new condition will be needed for the envelope.

For a refusal, first save the state of the tables, execute the request, and compare the state after it. One correct error code isn’t enough: the server might have already charged the coins.

## The common check

~~~bash
python3 checks/acceptance_eng.py --project . --profile base
~~~

It starts a real MCP server as a separate process, uses its own training data in a temporary folder, and checks the list of tools, the schemas, purchases, cancellations, pickup, errors, and the state of the database after refusals and a restart. Your working database isn’t involved.

For an envelope, replace `base` with `E1`, `E2`, `E3`, `E4`, or `E5`. The profile changes the expected result only where the condition has changed. The number in the command doesn’t change the server’s behavior by itself.

The checks are open: you can read them. You can’t fix the ready-made checks so that they accept wrong behavior. At the acceptance, the reviewer’s original copy is used.

If the run with the envelope profile doesn’t pass, finish the change or return the code to the basic rules and submit `base`. Reflect this in `docs/change_eng.md`.

The checks aren’t protection against deliberately hostile Python code. They help find errors, and the team’s explanation helps understand its solution.

