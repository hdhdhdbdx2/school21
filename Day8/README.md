# Days 08–09. The «School 21» Shop

RETURN CHANNEL · INCOMING PACKET

sent 2030 recipient you

> ***Hi! Remember the claim that human language will become the main programming language. Now imagine that you send a request to a machine: «Order this thing for me». And you close your computer.\
What should happen while you’re busy with your own things?***

> ***In your time, a person often finishes the work for the AI themselves: moves text from the chat, opens another program, clicks the right button.\
In 2030, we’re used to entrusting a machine with a whole task. You speak, it acts. Convenient — until it turns out that you and it understood the word «order» differently.***
> ***Today your role is an AI integration engineer. You’ll have to give an AI agent tools with which it can do something outside the conversation. And figure out which actions it can be trusted with and under what conditions it must stop. An AI chat has only a voice. You’ll give it hands too.\
An AI can write very politely: «All done». But for a person standing empty-handed at the pickup counter, this politeness is of little use. The order is already expected at the counter. And there’s no order.\
So I’ll pass on a habit from the future to you: behind every «done», look for what has actually changed. Did the order appear in the system? Did the product stock change? Or do you only have a message saying so? The more tasks you entrust to AI, the more important this habit becomes. Even if you don’t end up becoming an AI integration engineer.\
And here’s what worries me most. When you give a machine a tool, you let it affect someone’s life. In this project at the Pool, it’s just merch for coins. In another system, it’s a doctor’s appointment, a money transfer, access to documents. You choose what it will be able to reach.***

«School 21» has a Shop that sells merch: goods with the School logo. Merch is bought with coins. To find out the stock, the balance, and what happened to an order, participants go to the administrator, and the queue grows. Soon a software AI agent will be connected to the Shop. It’s polite and fast, but it may mix up a size, repeat a request, or try to cancel an order that has already been picked up. It needs tools — and a server that won’t let it break the Shop rules.

Today is a group project in which you’ll build the Shop’s MCP server. 

*An MCP server is a thing that every business has in my time. A special server for connecting AI agents. In your time, such access for agents is still rare for businesses, but this will change very soon. And today you’ll learn to develop such servers — one of the most in-demand skills in the near future.\
You work as a team. The recommended team size is 4 people. Today and tomorrow, the team is counting on you. Remember how you put together the exam? Back then, everyone wrote their own parts, and a person went through one common program. It will be the same here. By the end of the second day, you’ll have to build a server that works according to clear rules, withstands erroneous requests, and can be handed over to the next developer.*

**What an AI integration engineer does.** Connects an AI agent with the operations of a real system: for example, viewing stock, creating an order, or canceling a booking. To do this, they describe the available tools and the data format, implement rule checks on the server, check the data changes, and prepare the launch for another team. Behind the message «order cancelled» there must be a verifiable action: the status changed, the refund happened once.

During these two days, you build the server side of such an integration and test it with a ready-made software client. After the Pool, this experience will come in handy when connecting an agent to an ordering or appointment booking service. The same skills are needed in an ordinary application: a button, a script, and an AI agent can call the same operation, and its rules must be enforced by the server.

Tasks 1–4 are day 08, Tasks 5–8 are day 09.\
Future readiness practices are included in the tasks: team agreements — Task 2, the final reflection — Task 8. Write down the results of both practices in `docs/team_eng.md`.\
Open the materials when you need them: they contain the Shop rules, how the server is structured, and command examples. How to divide the work and in what order to put it together is up to the team.

[Getting Started](#getting-started)

Day 08
- [Task 1. First Launch and the Path of a Request](#task-1-first-launch-and-the-path-of-a-request)
- [Task 2. Team Agreements](#task-2-team-agreements)
- [Task 3. Tool Contracts](#task-3-tool-contracts)
- [Task 4. A Purchase and the First Order](#task-4-a-purchase-and-the-first-order)

Day 09
- [Task 5. Cancellation, Pickup, and Your Own Tests](#task-5-cancellation-pickup-and-your-own-tests)
- [Task 6. The Envelope](#task-6-the-envelope)
- [Task 7. Handing Over the Server](#task-7-handing-over-the-server)
- [Task 8. What We Take to the Next Teamwork](#task-8-what-we-take-to-the-next-teamwork)

[Checkpoint](#checkpoint)

## Getting Started

<details>
<summary>How to learn at «School 21»</summary>

- A unique educational experience with a lot of freedom awaits you here. You get a task and look for ways to solve it on your own.
- Peer learning (Peer-to-Peer, P2P) is the exchange of knowledge and experience with other peers, where everyone acts as both a teacher and a learner. This approach lets you understand the material more deeply by learning from each other.
- Feel free to ask for help. The people around you are also taking this path for the first time. Share your experience and ideas with others.
- Learning won’t make any sense if you copy other people’s solutions. If you use help from others, always get to the bottom of why, how, and what for. Don’t be afraid to make mistakes.
- Does the task seem impossible? Take a break, get some fresh air, reset your mind — this has helped many people. Perhaps the solution will come to you afterward.
- Keep track of your time while working on the project. We recommend overcoming at least one challenge a day.

</details>

<details>
<summary>How to work with the project</summary>

- The «Access open» mode: search engines and AI assistants are allowed. Check the suggested code on the Shop data: if a model claims that a repeated cancellation is safe, show it with a request and the state of the database.
- This is a group project. The recommended team size is 4 people. The team works in one repository, submits one version, and gets one grade for everyone.
- Tasks 1–4 are day 08, Tasks 5–8 are day 09. All tasks are mandatory. A completed envelope in Task 6 gives an extra point. The project is reviewed by the lead of another team after day 09.
- Open the materials when you need them: they contain the Shop rules, how the server is structured, and command examples. How to divide the work and in what order to put it together is up to the team.
- The mandatory part works locally. Paid services, model keys, and a connection to an AI aren’t needed to complete or review it.
- The team works in one team repository. Each participant clones it from GitLab and goes to the root — the folder that contains the README.
- The common branch is `develop`: it’s what is submitted for review. Work in your own working branches and merge changes into `develop` one at a time. The team writes down who merges and how in `docs/team_eng.md`.
- **All run commands are executed from the repository root.** A mention of a file path is not a command.
- Write code in `src/`, your own tests in `testing/`. Don’t change the provided checks `checks/` and the source data `data/seed_eng.sql`. In the mandatory part, you don’t need to change the wrapper `src/server_eng.py` and `src/mcp_adapter_eng.py`.
- Don’t add the local databases `data/\*.db` and the virtual environment to the repository.
- The environment at the workstation is already prepared, use `python3`.

**Teamwork**

The work is divided into 4 areas. An area isn’t necessarily one person: in a smaller team, areas are combined; in a larger one, people work in pairs on one area.

| **Area** | **Main files** | **What to hand over to the team** |
| --- | --- | --- |
| Lead and read tools | `src/read_handlers_eng.py`, `contracts/tools_schemas_eng.json` | 4 working read tools, tool descriptions, a common runnable `develop` branch |
| Rules and tests | `src/domain_eng.py`, `testing/test_rules_eng.py` | Rule functions with examples of inputs and expected answers |
| Data | `src/storage_eng.py` | Storage methods: SQL queries, writing an order, charging and refunding in one transaction |
| Order actions | `src/order_handlers_eng.py`, `testing/test_orders_eng.py` | Creating, cancelling, and picking up an order, refusal tests |

If the team has fewer than 4 people:

| **Team** | **Areas** |
| --- | --- |
| Three | 1) Lead, read tools, and contracts; 2) Rules and tests; 3) Data and order actions: `storage_eng.py` and `order_handlers_eng.py` are linked by one transaction, it’s more convenient for one person to handle them |
| Two | 1) Lead, read tools, contracts, rules, and their tests; 2) Data and order actions, refusal tests |

Divide the documents in `docs/` and `RUN_eng.md` equally.

The **lead** combines coordination with one of the development areas. The lead merges changes into `develop`, makes sure that accepted work doesn’t remain only on someone’s computer, and defends the project at the review.

**When to meet:**

1.  After the demo — assigning the areas and agreeing on function signatures. After Task 1, discuss the team agreements; if necessary, postpone forming them to the end of day 08.
2.  When reading and the rules are ready — the first common purchase call.
3.  At the end of day 08 — a launch from `develop` and a list of unfinished work. Add to `docs/team_eng.md` an example of using strengths together, or formulate the agreements if you postponed the discussion.
4.  After the basic checks of day 09 — the envelope (received via the link in Task 6) and distributing the change.
5.  Before submission — a launch following the instructions and a short rehearsal of the explanation. After Task 7, discuss the experience of the two days and write down the common and personal conclusions for the next teamwork.

If for 15 minutes you can’t continue because of someone else’s part, tell the team: which method you need, what result you expect, and what can already be checked. More details are in `materials/team_eng.md`.\
If you get stuck, tell your team. I know you want to figure it out first and come with good news. While you’re silent, the others make plans as if everything is working out for you. Don’t let your team down by staying silent. You can find a bug in the code together. Guessing that you need help is much harder. Even in the future, we still can’t read each other’s minds.

</details>

<details>
<summary>Materials</summary>

| **What you need** | **Where to find it** |
| --- | --- |
| The Shop rules: products, users, responses, contracts, the order of purchase checks, order states | `materials/shop_rules_eng.md` |
| Teamwork | `materials/team_eng.md` |
| How the server works: handlers, rules, storage, transaction | `materials/architecture_eng.md` |
| How to write tests and run the common check | `materials/testing_eng.md` |
| Project review | `materials/acceptance_eng.md`, `check-list_eng.yml` |
| Python and dependencies | `materials/environment_eng.md`, `materials/requirements_eng.txt`, `materials/requirements-campus.lock_eng.txt` |

**Provided files.** You don’t need to create them again.

| **File** | **What it is** |
| --- | --- |
| `src/` | The server: the ready-made `get_product` tool, the database connection, and function stubs marked `TODO` |
| `client_eng.py` | The client: a demo, a scenario, and manual tool calls. Each call is written to `logs/client_eng.jsonl` |
| `check_environment_eng.py` | Checking the workstation |
| `data/seed_eng.sql` | Training products, users, and tables. Must not be changed |
| `contracts/tools_schemas_eng.json` | Tool schemas. The descriptions need to be filled in |
| `checks/` | Common acceptance checks. You can run them, but not change them |
| `testing/test_example_eng.py` | An example test. It doesn’t count toward your own tests |
| `docs/team_eng.md`, `docs/system_eng.md`, `docs/change_eng.md` | Templates of the team documents |
| `RUN_eng.md` | A template of the launch instructions |

</details>

## Task 1. First Launch and the Path of a Request

_Day 08, the whole team._

1\.  All participants clone the team repository. The lead creates the `develop` branch and pushes it, the others switch to it.

2\.  Activate the environment according to `materials/environment_eng.md`, then check the workstation and run the demo:

- `python3 check_environment_eng.py`
- `python3 client_eng.py demo`
- The demo starts the server by itself and requests 2 products. For `hoodie`, the server will return the price 500 and the stock by size, for `missing` — the `PRODUCT_NOT_FOUND` refusal. The whole team should see both responses.

3\.  Together, trace the path of `get_product` through the code: `src/mcp_adapter_eng.py` → `src/read_handlers_eng.py` → `src/storage_eng.py`. Find the function that receives the request, the SQL query that reads from the database, and the place where the response or refusal is formed. A short reference is in `materials/architecture_eng.md`.

4\.  Write down this path in one line with the function names in `docs/system_eng.md`, the «Request path» section.

5\.  Assign the areas (15 minutes for this) and fill in `docs/team_eng.md`: the lead, who takes which area, how you merge changes.

You don’t need to read the whole project before the first launch.

**Result:** the whole team has experience of launching the server and analyzing its real response; `docs/team_eng.md` records the assignment, `docs/system_eng.md` — the path of `get_product`.  

**Check:** `python3 client_eng.py demo` shows the price and stock of the hoodie and the `PRODUCT_NOT_FOUND` refusal. The lead shows the path of `get_product` through 3 files, names the SQL query, and explains how the `PRODUCT_NOT_FOUND` refusal differs from an unexpected Python exception. `docs/team_eng.md` lists the lead, 4 areas, and the way of merging changes.  
**Why:** right now, the path of the ready-made `get_product` will help you finish the other 6 tools and understand where to look for a bug: in receiving the request, in the handler, or in reading the data. After the Pool, such an analysis will come in handy when an agent reports wrong product stock: an AI integration engineer traces a specific call down to the database and the response to find the cause.

## Task 2. Team Agreements

In the previous individual projects, you learned to recognize your state and manage your reaction to difficulties — you developed Emotional intelligence — and you also learned to turn a failure into a specific lesson and a next step. In the analytical projects, you used the «Iceberg» to develop Systems thinking and breaking a problem down into measurable components to develop Analytical thinking.

Now you have to build the Shop server together. We suggest approaching the organization of teamwork through one more Future readiness practice and practicing the skill of Collaboration and partnership: coordinating actions, sharing responsibility, and using each other’s complementary strengths.

To do this, use the «Team working agreements» tool. It helps to explicitly discuss the rules of interaction instead of assuming that everyone works the same way.

You’ve already launched the server and assigned the areas. Remember the previous team project: what helped you work together, and what led to delays or confusion? Take this experience into account in the discussion. 

Add three short blocks to `docs/team_eng.md`:
1. How we work together. Agree on the result of day 08, the communication channel, response times, and the decision-making procedure. Based on the assignment from Task 1, agree on how the team checks the common result. You don’t need to repeat information already written down. 
2. How we handle disagreements and delays. Agree on how to discuss disagreements directly, by which objective criteria to choose a solution, and whom to turn to for help. Specify who makes the final decision and how, and what to do in case of a delay or being blocked by someone else’s part.
3. How we use strengths. Name the participants’ strengths and how they’re applied in the work or in helping each other. 
Write briefly: a few points in each block are enough. The agreements should be clear to all participants and applicable in the current project.

At the end of day 08, add one specific example of how a combination of strengths helped the common result. If it hasn’t helped yet, state what is worth changing in the organization of work.

**Result:** `docs/team_eng.md` records the agreed rules of interaction, the procedure for handling disagreements, and the use of the team’s strengths.

**Check:** the lead shows the three blocks in `docs/team_eng.md`, explains how the team makes decisions and acts in case of delays, and gives the recorded example of using strengths together or explains the proposed change.
You can postpone forming the agreements to the end of day 08, when you’ll have gained experience of working together and better understand each other’s strengths. Then rely on specific situations of the past day and formulate rules for continuing the project on day 09.

## Task 3. Tool Contracts

_Day 08, the lead’s area; checking the descriptions — the whole team._

MCP is a protocol by which a program finds out which tools a server provides and calls them with the right arguments. A tool is one operation, for example `get_product`. A contract is an agreement about what a tool accepts and what it returns.

The server has seven tools:

| **Tool** | **What it does** |
| --- | --- |
| `list_products` | Shows the catalog and stock |
| `get_product` | Shows one product |
| `get_coin_balance` | Shows a participant’s balance |
| `create_order` | Creates an order, charges coins, and reserves the product |
| `get_order_status` | Shows the state of an order |
| `cancel_order` | Cancels an order and returns the product and coins |
| `confirm_pickup` | Marks that an order has been picked up |

The contract skeleton is already in `contracts/tools_schemas_eng.json`. The server takes the tool descriptions from this file and shows them to the client.

1.  For 6 tools, replace the `TODO` mark with your own description. In the description, state when the tool is needed, what it changes, and in which case it will refuse. For example, the description of cancellation warns that an order that has been picked up can’t be cancelled.
2.  Don’t change tool names, arguments, and response schemas: the next developer’s client will access the server by them.
3.  Check the descriptions within the team: split into two groups. One names a situation, the other chooses a tool based only on the description. If the choice turned out to be ambiguous, clarify the text. To see what the client sees: `python3 client_eng.py list`.
4.  In `docs/system_eng.md`, fill in the «What the server does» and «Boundaries» sections: which actions the system performs and what can’t be promised to the client. A hint is the «Boundaries of the training service» section in `materials/shop_rules_eng.md`.

**Result:** `contracts/tools_schemas_eng.json` has 7 descriptions without `TODO`; `docs/system_eng.md` describes the capabilities and boundaries of the server.  

**Check:** for the situation «a created bottle order hasn’t been picked up yet, the participant wants to cancel it», the lead uses the descriptions to choose `cancel_order` and names the required argument. The lead explains why a description doesn’t replace a check in the code and why a public tool can’t be renamed arbitrarily. `docs/system_eng.md` names at least one action that can’t be promised to the client.  
**Why:** right now, precise descriptions help choose the right operation and arguments, and common schemas let the team connect their parts. In the work of an AI integration engineer, such a contract is needed to connect another client or agent to an ordering service without guessing the data format. A description helps choose an action; the server checks whether the arguments and the action itself are allowed.

## Task 4. A Purchase and the First Order

_The most difficult task._

_Day 08, all areas in parallel._

Today the 4 read tools and the purchase will start working. The functions that need to be finished are marked `TODO` and for now raise `NotImplementedError`.

| **Area** | **What to finish in Task 4** |
| --- | --- |
| Lead and read tools | `src/read_handlers_eng.py`: `list_products`, `get_coin_balance`, `get_order_status` |
| Rules and tests | `src/domain_eng.py`: `calculate_total`, `purchase_error`; the first rule tests |
| Data | `src/storage_eng.py`: `list_products`, `get_user`, `get_order`, `count_owned`, `create_order` |
| Order actions | `src/order_handlers_eng.py`: `create_order`; the first refusal tests |

1\.  Go to your areas from `docs/team_eng.md`. The areas won’t be ready at the same time, and that’s normal:

- the rules in `src/domain_eng.py` don’t access the database: they can be finished and covered with tests while storage isn’t ready;
- the purchase handler can be written against a temporary storage stub — a dictionary with the same fields you agreed on. The stub lives only in a test: you can’t submit it instead of SQL.

2\.  A purchase checks the conditions strictly in this order: the user exists → the product exists → the size is available and there’s enough stock → the limit isn’t exceeded → there are enough coins. The refusal codes are in `materials/shop_rules_eng.md`, the «Purchase» section.

3\.  Writing the order, charging the coins, and reducing the stock are done in one transaction: either all 3 changes are saved, or none. How to do this is in `materials/architecture_eng.md`, the «Transaction» section.

4\.  Do the first common check on a new training database:

- `python3 client_eng.py --db data/day08_eng.db call create_order '{"user_id":"student_01","product_id":"bottle","size":"one_size","quantity":1}'`
- `python3 client_eng.py --db data/day08_eng.db call get_coin_balance '{"user_id":"student_01"}'`
- `python3 client_eng.py --db data/day08_eng.db call get_product '{"product_id":"bottle"}'`
- `python3 client_eng.py --db data/day08_eng.db call create_order '{"user_id":"student_poor","product_id":"hoodie","size":"M","quantity":1}'`
- Expected: a bottle order with the `created` status and a cost of 150, the balance of `student_01` — 850, the bottle stock — 11. Buying a hoodie for `student_poor` — the `INSUFFICIENT_COINS` refusal, the balance stays 20, the hoodie M stock — 5.

5\.  Add your own tests of the calculation and a refusal to `testing/`. How a test is structured is in `materials/testing_eng.md` and `testing/test_example_eng.py`.

6\.  Before leaving, merge the work into `develop`. Everyone shows the team their area on one request. If the first order still doesn’t go through, write down the specific reason in `docs/team_eng.md`, the «What’s left at the end of day 08» section, and start day 09 with it.

**Result:** the 4 read tools and `create_order` work; the order is visible in the database, the balance and stock changed correctly; `testing/` has your own tests of the calculation and a refusal.  

**Check:** on a new database, buying a bottle and the refusal for `student_poor` give the expected responses. The lead shows the purchase checks in the right order and explains why `USER_NOT_FOUND` will be returned when both the user and the product are unknown. The lead shows that the refusal happens before writing and shows the common transaction. Using the purchase as an example, the lead shows where the handler is, where the rule without SQL is, and where the SQL is.  

**Why:** right now, the transaction links the order, charging the coins, and reducing the stock: in case of an error, you can’t save only part of these changes. After the Pool, the same approach will be needed, for example, when booking a seat: the booking record and the number of free seats must stay consistent. An AI integration engineer checks that a tool call leads to a consistent change in the data.

>***So, did you manage to place the first order?\
If so, pause for a second: now your code takes part in an action after which a person’s balance changes. Do you feel the difference? If it hasn’t worked out yet — before leaving, agree on what you’ll start with in the morning. Be sure to come tomorrow, even if your part already works. On the second day, you’ll see what you may not notice at all today, sitting in your own file. And the others are counting on you to be there.***

RETURN CHANNEL · INCOMING PACKET

sent 2030 recipient you

> ***Hi.\
Imagine: an AI agent asked the server to cancel an order. The server cancelled it, returned the coins, and sent a response. The response got lost.\
The AI agent received nothing. It’s trying to help the person and asks to cancel the order again.\
The buyer changed their mind once. The request came twice. Nobody wanted to break anything. But if the system can’t deal with such cases, the money can be refunded twice.\
And yet, each of them separately may think that everything was done right…***

>***Now you have to look at the whole system: who talks to whom, who knows what, who depends on whom, and what will happen when the usual order of things is disrupted.\
In 2030, parts of one project can be created by different people and different AIs. Each model saw its own task and confidently reported that it had coped. An architect has to understand what each part believes has happened and what has actually happened. As in the story with the cancellation: the server has already returned the coins, but the AI agent doesn’t know about it yet. What will it do next?\
Your Shop is the same. But try to look at it through the eyes of a person who will have to change it a year from now. This person doesn’t know about your conversations. Will they manage to understand why everything is arranged exactly this way?\
Maybe that person will be you. Our memory is wonderful, of course. But it’s still better to leave an explanation. Heh-heh.***

## Task 5. Cancellation, Pickup, and Your Own Tests

_Day 09, all areas._

An order has 3 states: `created`, `cancelled`, `picked_up`. Only an order in the `created` state can be cancelled or picked up.

| **Area** | **What to finish in Task 5** |
| --- | --- |
| Rules and tests | `src/domain_eng.py`: `refund_amount`, `can_cancel`, `can_pickup` |
| Data | `src/storage_eng.py`: `cancel_order`, `confirm_pickup` |
| Order actions | `src/order_handlers_eng.py`: `cancel_order`, `confirm_pickup` |
| Lead | Merging into `develop`, a common run of the checks |

1\.  Finish cancellation and pickup:

- cancellation returns the product and coins exactly 1 time; the refund amount is taken from the saved order cost, not from the current price;
- pickup changes only the status: the product and coins were already charged at creation;
- a repeated cancellation, a repeated pickup, picking up a cancelled order, and cancelling a picked-up order — the `ORDER_STATUS_ERROR` refusal; an unknown order — `ORDER_NOT_FOUND`.

2\.  Go through the full path: create an order, find out its state, cancel it; create another one, pick it up, try to cancel the picked-up one. The scenario with a repeated cancellation is already built into the client: `python3 client_eng.py scenario`.

3\.  Bring your own tests up to at least 3 cases:

- calculating the cost;
- a refusal after which the data didn’t change: compare the contents of the products, stock, users, orders tables before and after;
- a repeated action with an order.

- The ready-made example doesn’t count. Tests without checks and `assert True` aren’t counted.

4\.  Run the tests and the common check:

- `python3 -m pytest -c pytest_eng.ini -q`
- `python3 checks/acceptance_eng.py --project . --profile base`
- If the check fails, start with the first error message. Fix the server’s behavior: the ready-made checks and the source products can’t be changed.

**Result:** all 7 tools work; the common check finishes with `PASS` for the `base` profile; `testing/` has at least 3 of your own tests, and they pass.  

**Check:** at the review, the reviewer runs their own original copy of the checks and `pytest`. The lead walks through one of your own tests: the input data, the expected result, and the bug the test will catch. The lead shows the status check before cancellation and pickup and explains why a repeated cancellation won’t return the coins again.  

**Why:** right now, the state check and the repeated cancellation test help make sure that the server returns the coins once. After the Pool, this will come in handy when an agent resends a request or a button in an app is clicked twice. An AI integration engineer needs to check both the response and the state of the data: a repeated request must not repeat a refund that has already been made.

## Task 6. The Envelope

_Day 09, the whole team._

💡 When the common `base` check passes without errors, [**click and get the envelope**](http://21-school-programs.ru/page301377209.html)

Study the new condition from the Shop: one changed rule and its own check profile (`E1`–`E5`).

1\.  Before changing the code, write down in `docs/change_eng.md` the number and the condition of the envelope and which files, in your opinion, you’ll have to touch.

2\.  Make the change. Tool names, arguments, and response fields stay the same.

3\.  Add a test that distinguishes the new behavior from the old one.

4\.  Run the tests and the common check with your envelope’s profile:

- `python3 -m pytest -c pytest_eng.ini -q`
- `python3 checks/acceptance_eng.py --project . --profile E1`
- Replace `E1` with your envelope number.

5\.  Write down in `docs/change_eng.md` what you actually changed, which test distinguishes the rules, and how the check ended.

6\.  Specify the submitted profile in the same way in `RUN_eng.md`, `docs/system_eng.md`, and `docs/change_eng.md`.

The first attempt gets 45 minutes. If it didn’t work out, write down where you stopped. You can continue until submission or go back to the basic rules and submit `base`. The number of the received envelope stays in the report.

**Result:** `docs/change_eng.md` records the condition, the assumption about the files, the actual change, and the check result; the profile matches in 3 documents.  

**Check:** the lead retells the new rule, gives an example on which the old and the new behavior differ, and shows the place in the code where the rule was changed or was going to be changed. A full analysis when submitting `base` corresponds to 4 for this task. A 5 requires the submitted profile of the received envelope, `PASS` of the official check, and your own passing test of the new rule. An unfinished envelope doesn’t zero out the grades of other tasks.  

**Why:** right now, the envelope shows how easy it is to find and change one rule in a working server. After the Pool, this skill will be needed for a new discount or a change in the order limit: an AI integration engineer changes the behavior of a service while keeping the agreed call format. A test of the new condition shows the difference in behavior, and rerunning the other checks helps notice side-effect errors.

## Task 7. Handing Over the Server

_Day 09, the whole team._

An AI agent is going to be connected to the server. To hand this work over to another person, everything necessary must be in the repository.

1.  Fill in `RUN_eng.md`:
    - commands to launch and check;
    - an example of a request and the received response;
    - how to start with a new training database via `--db` without losing the working data;
    - which files keep the state: manual calls `client_eng.py call` without `--db` work with `data/shop_eng.db`, `demo` and `scenario` without `--db` create a temporary database, the log is written to `logs/client_eng.jsonl`;
    - the submitted profile.
2.  Complete `docs/system_eng.md`: the request path, the system boundaries, one example of a refusal with an explanation of where it’s checked, the submitted profile, and the «Connecting another client» section: the server launch command `python3 -m src.server_eng`, the `stdio` transport.
3.  Attach the `logs/client_eng.jsonl` log created by the client during a real run. The log isn’t written or edited by hand.
4.  Swap within the team: the instructions are carried out by another part of the team: they start with a clean copy of the repository and check the text without its authors. Fix the places where verbal hints were needed.

**Result:** another person launches the server following `RUN_eng.md` and understands its capabilities from `docs/system_eng.md`.  

**Check:** the reviewer runs the `RUN_eng.md` commands from a clean copy and gets a server response without hints from the team. After a request made in the reviewer’s presence, a new entry appears in `logs/client_eng.jsonl`. The lead shows the server code, the contracts, the datasheet, `RUN_eng.md`, and the log and explains the purpose of each; explains the difference between the database and the log.  

**Why:** right now, a launch by another part of the team reveals the steps missing from the instructions. After the Pool, an AI integration engineer will need to hand over a service to those who connect an agent or maintain an application: they need launch commands, the call format, the service boundaries, and a way to check the result. Clear instructions let the work continue without constant verbal hints from the authors.

## Task 8. What We Take to the Next Teamwork

On day 08, you formed team agreements: you discussed how to communicate, make decisions, handle disagreements, and use each other’s strengths. Now your joint work is coming to an end. We suggest reflecting on the experience you’ve gained and determining what will be useful to you in future teams.

We continue the Future readiness practices and practice the skill of Intrapreneurship — the ability to notice opportunities to improve the common work and propose useful changes.

First, everyone recalls a situation from these two days and briefly tells the team: what helped or hindered the work, how the agreements of day 08 worked, and what will be useful in the future. A separate written answer isn’t needed.

Then discuss the experience together. Choose one situation from which a useful lesson can be learned. Add the «What we take to the next teamwork» section to `docs/team_eng.md`:
1. Situation and conclusion. What happened, how did it affect the work, and what did it teach you? What in the agreements of day 08 helped or needs clarification?
2. An approach for the future. Propose one rule, technique, or simple template. State when it will come in handy and how it will help.
3. Everyone’s personal conclusion. Write down one sentence from each participant: what specifically they’ll take to the next teamwork.
If there were no difficulties, analyze a successful episode: what ensured a good result and how to keep this approach in another team. You don’t need to make up a problem or a change.

**Result:** one common section in `docs/team_eng.md` with a specific situation, a conclusion for future teamwork, and a short personal conclusion of each participant. You aren’t required to implement the change in the project that’s ending or to prove its effect. 

**Check:** the lead shows the «What we take to the next teamwork» section in `docs/team_eng.md` and presents the participants’ team and personal conclusions for future teamwork.

## Checkpoint

The `develop` branch of the team repository in GitLab is submitted for review.

Before finishing your work:

- Make sure that the work of all areas is merged into `develop` and pushed.
- Check `git status`: the files you were going to submit must not remain outside commits. There are no local databases `data/\*.db` and no virtual environment in the commits.
- The submitted profile is the same in `RUN_eng.md`, `docs/system_eng.md`, and `docs/change_eng.md`.
- Clone `develop` into a separate folder and launch the project following `RUN_eng.md`.
- Check that `docs/team_eng.md` contains the three blocks of team agreements and an example of using strengths together or a proposal to change the work, as well as the «What we take to the next teamwork» section with each participant’s personal conclusion.
- Open the repository in GitLab, select `develop`, and check that the latest changes are on the server.
- Finish the project on the platform. A push by itself doesn’t finish the project.

**How the review goes.** The lead of one team reviews the lead of another, the other participants can be present and ask questions. The review takes up to 45 minutes. The reviewer runs the submitted version on a clean copy and uses their own original copy of the checks, not the `checks/` folder from your repository. You don’t need to write new code against the clock. The grade is common for the team: personal contribution, the number of commits, and lines of code aren’t measured. If part of the project doesn’t work, the other tasks are still reviewed. The acceptance procedure is in `materials/acceptance_eng.md`.

Before the review, think about:

- what will happen to the balance if there was enough product but not enough coins;
- why you can’t return coins on every repeated cancellation;
- where to change the purchase rule so as not to rewrite the client;
- how a tool description differs from checking its arguments;
- how to prove that nothing changed in the database after a refusal;
- what the next day’s developer should get to connect an assistant.

Final result

Everything listed must be on the `develop` branch in GitLab.

| **Task** | **What is submitted** | **How it’s checked** |
| --- | --- | --- |
| 1   | `docs/team_eng.md`, the request path in `docs/system_eng.md` | The demo works; the lead shows the path of `get_product` |
| 2   | Three blocks in `docs/team_eng.md` and an example of using strengths together or a proposal to change the work | The lead explains the rules of interaction, the procedure in case of disagreements and delays, and the combination of strengths |
| 3   | `contracts/tools_schemas_eng.json`, the boundaries in `docs/system_eng.md` | 7 descriptions without `TODO`; the lead chooses a tool by its description |
| 4   | Reading and purchase code in `src/`, tests in `testing/` | A purchase and a refusal on a new database; the order of checks and the transaction |
| 5   | Cancellation and pickup code, at least 3 of your own tests | The common check `PASS`, `pytest` passes; the lead walks through a test |
| 6   | `docs/change_eng.md`, the envelope change, if submitted | The condition and an example; 4 for a full analysis with `base`, 5 for a confirmed envelope |
| 7   | `RUN_eng.md`, `docs/system_eng.md`, `logs/client_eng.jsonl` | The reviewer launches the server following `RUN_eng.md`; a new entry in the log |
| 8   | The «What we take to the next teamwork» section in `docs/team_eng.md` | A specific situation, an applicable approach for the future, and the participants’ personal conclusions |

The provided files `checks/` and `data/seed_eng.sql` stay unchanged. Local databases and the virtual environment aren’t part of the submission.

> ***What can already be handed over to another person without verbal hints? Start checking whether the server is ready with this. If the rules withstand the checks and the instructions work, you can try connecting an AI agent.***

> ***It’s me again. What fascinated you more: making the AI agent able to fulfill a request, or figuring out how everything is connected and what will happen when the rules change?***

> ***Don’t rush to answer that you liked what turned out to be easier. Maybe it wasn’t clear at all how to approach the terminal. Now you have experience on which you can base further choices.\
I still won’t tell you who we’ve become. Maybe you’ll choose differently now. Then I, here in the future, will have something to reconsider…***

> ***Now imagine: the server works, the AI agent carries out requests and gives the person an answer. Everything sounds reasonable. Even too pleasant to read. At what point will you suspect that something is wrong?\
Tomorrow there will be a separate set — you don’t need to carry over today’s server. You’ll try the profession of an AI engineer: you’ll build an AI agent and figure out how a model’s proposal turns into a completed action. And here’s a request from the future: check especially carefully the answer that you like. When a machine says exactly what we want to hear, you and I stop asking questions surprisingly quickly. See you tomorrow.***

💡 [**Click here**](http://opros.so/BQbV3) to leave feedback on this project. It’s anonymous and helps us make learning better.

![img1](misc/images/д8.png)