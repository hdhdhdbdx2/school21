# The Shop Datasheet

Rules profile: base

## What the server does

List the available actions and the data that changes.

## Boundaries

Which users exist? Is there identity verification? Which actions can’t be promised to the client?

## Request path

Client → tool name → handler function → rule, if needed → storage method → response.

## Refusal check

Request example:
Expected refusal:
Where it’s checked:
How we showed that the data didn’t change:

## Connecting another client

Server launch command:
Transport:
Contracts: contracts/tools_schemas_eng.json
Instructions: RUN_eng.md
Log: logs/client_eng.jsonl
Known limitations:

