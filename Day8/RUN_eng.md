# Launching the Shop

Fill in and check these instructions before submission.

Rules profile: base

## Check the environment

~~~bash
python3 check_environment_eng.py
~~~

## Run the demo

~~~bash
python3 client_eng.py demo
~~~

## Go through the full scenario

~~~bash
python3 client_eng.py scenario
~~~

## Start the server for another client

~~~bash
python3 -m src.server_eng
~~~

The transport is stdio. The server itself waits for client messages; the visible scenario is started via client_eng.py.

## Check the project

~~~bash
python3 -m pytest -c pytest_eng.ini -q
python3 checks/acceptance_eng.py --project . --profile base
~~~

If you’re submitting an envelope, change the profile in the last command and at the beginning of this file.

## State

Manual requests `client_eng.py call` and starting the server directly use data/shop_eng.db. A restart keeps this database.

The demo and scenario commands without --db create a temporary database each time and delete it after finishing. To keep the result of a scenario, set --db, as in the example below.
Client log: logs/client_eng.jsonl.

To run a separate clean training database, specify a new file name:

~~~bash
python3 client_eng.py --db data/trial_01_eng.db scenario
~~~

If the file already exists, the state will continue. Don’t delete other people’s data for the sake of a demo.

## Our request example

Add the command and an explanation of the received response.

