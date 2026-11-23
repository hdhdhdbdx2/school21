# How to Divide the Work in the Team

At the start of the project, set aside 15 minutes for the assignment. Run the demo together, read the four areas below, and choose who takes each one. The lead is one of the four participants; they have code too.

| Area | Main files | What to do | What to hand over to the team |
| --- | --- | --- | --- |
| Lead and read tools | `read_handlers_eng.py`, `contracts/tools_schemas_eng.json` | Finish the catalog, balance, and status; put together the tool descriptions; merge changes | Four working read tools and a common runnable branch |
| Rules and tests | `domain_eng.py`, `testing/test_rules_eng.py` | Calculate the cost and the refund; check the purchase, cancellation, and pickup; write rule tests | Rule functions with examples of inputs and expected answers |
| Data | `storage_eng.py` | Implement SQL queries, writing an order, charging and refunding in one transaction | Storage methods with ready-made signatures; an explanation of the table changes |
| Order actions | `order_handlers_eng.py`, `testing/test_orders_eng.py` | Connect the checks and the writing; finish creation, cancellation, and pickup | Three working actions and refusal tests |

The method names and data shapes are already set in the template. If you want to change an internal method, first agree with whoever calls it. Don’t edit someone else’s main file at the same time as them.

## The first half hour after the assignment

The lead finishes the descriptions and starts reading the catalog. The participant with the rules checks the cost calculation on simple numbers and writes the first test. The participant with the data starts with reading users and orders. The participant with the actions studies the ready-made handler and works out the order of checks for the purchase.

While writing an order isn’t ready, the rules can be checked separately. To work on the handler, agree with the author of the storage on an example of the returned dictionary; use a temporary substitute only in a test, don’t submit it instead of SQL.

## When to meet

1. After the demo — the assignment and an agreement on the signatures.
2. When reading and the rules appear — the first common purchase call.
3. At the end of day 08 — a launch from the common branch and a list of unfinished work.
4. After the basic checks of day 09 — the envelope and distributing the change.
5. Before submission — a launch following the instructions and a short rehearsal of the explanation.

For Git, a common `develop` branch and separate working branches are enough. Merge changes into the common branch one at a time. Before merging, the author shows which command they ran and what it checked. The lead makes sure that accepted changes don’t remain only on someone’s computer.

If for 15 minutes you can’t continue because of someone else’s part, tell the team: which method you need, what result you expect, and what can already be checked. In a dispute, first formulate the rule and an example. If you couldn’t agree, the lead chooses the solution and writes down the reason.

## If the team has changed

Four people is a recommendation. With a smaller team, combine the areas as follows and update `docs/team_eng.md`:

| Team | Areas |
| --- | --- |
| Three | 1) Lead, read tools, and contracts; 2) Rules and tests; 3) Data and order actions — `storage_eng.py` and `order_handlers_eng.py` are linked by one transaction, it’s more convenient for one person to handle them |
| Two | 1) Lead, read tools, contracts, rules, and their tests; 2) Data and order actions, refusal tests |

Divide the documents in `docs/` and `RUN_eng.md` equally. With a larger team, work in pairs on the same areas. The scope of the mandatory part doesn’t increase. If the lead has left, the team chooses a new one; a change in the team on the platform is arranged through the staff.

The assignment document helps organize the work. It isn’t used to count personal contribution or to give individual grades.

