# Acceptance in 45 Minutes

The lead reviews the lead of another team. The other participants can be present and ask questions. Only the reviewing lead fills in the platform. The result is common for the team, personal contribution isn’t assessed.

## Before the launch

The submitted version of the repository is reviewed. At the workstation of the team being reviewed, its lead opens a separate clean copy of the submitted commit under their own access. The reviewer compares the commit identifier with the platform and looks at `git status --short`: the source files must not contain local edits. There’s no need to share someone else’s password or clone a private repository under someone else’s account.

The environment at the workstation is already prepared. The reviewer runs their own original copy of `checks/acceptance_eng.py`, passing the path to the clean copy of the project and the declared profile. How the organizer provides this copy is described in its regulations.

An example of the command, if the original checks are in the neighboring folder `official_checks`:

~~~bash
python3 ../official_checks/acceptance_eng.py --project . --profile base
~~~

## The course of the review

| Time | What happens |
| --- | --- |
| 0–5 minutes | Check the repository, the commit, and the profile, and run the environment check |
| 5–13 minutes | The lead shows a request, a purchase, and a refusal via the client |
| 13–23 minutes | Run the common checks and the team’s tests; read the result |
| 23–35 minutes | Analyze the call path, the place of the rule, the transaction, and the envelope result |
| 35–40 minutes | Clarifying questions, including from the participants present |
| 40–45 minutes | The reviewing lead fills in the platform and explains the marks |

The questions are limited to the presented project. The reviewer doesn’t ask to write a new function and doesn’t quiz on all of Python.

## The main part

For each item, the reviewer marks «yes» or «no» and, in case of «no», states the observed reason.

1. **Launch.** The submitted version launches following `RUN_eng.md` in the prepared environment; a real MCP call has been demonstrated.
2. **Behavior.** The common check of the chosen profile finishes without errors; the seven mandatory tools are available.
3. **Code separation.** Using one example, the team shows the handler, the rule, and the SQL in the corresponding parts; the rule calculation can be called without the database.
4. **Own checks.** There are three meaningful tests, and they pass: a calculation, a refusal without a state change, a repeated action. The ready-made example doesn’t replace them.
5. **Explanation.** The lead explains the path of one request and shows the code that prevents the chosen error. A general phrase «this is checked» isn’t enough.
6. **Handover.** The contracts, `RUN_eng.md`, and the datasheet match the behavior; the profile, the access boundaries, and the log path are stated; the log was created by a real run.
7. **The envelope result.** `docs/change_eng.md` has the condition, the assumption about the affected files, the actual result, and the submission profile. An unfinished attempt is acceptable.

The main part is counted when all seven items are met. The distribution of roles, the number of commits, and the amount of personal code aren’t assessment criteria.

## Extra item for the envelope

It’s counted if the new rule is implemented, the common checks of the corresponding profile pass, and the team presents its own test that distinguishes the old and the new behavior. The lead explains why the change was made exactly in this area.

If the team submits `base`, the extra item isn’t counted. A correctly implemented envelope is checked by its own profile: the old expectation of a full refund, for example, mustn’t interfere with checking the new fee.

## If something doesn’t work

A project error is marked in the corresponding item. At an acceptance that has already started, there’s no made-up action «send back for revision»: the result is recorded by the means of the platform.

If the prepared environment doesn’t start or the submitted version is unavailable due to a site failure, call the staff. A technical failure is recorded separately and isn’t passed off as a business rule error.

