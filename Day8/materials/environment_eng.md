# Python and Running in Linux

The project commands are executed in the terminal from the repository root — the folder with `README_eng.md`. The specified set of dependencies requires Python 3.12 or newer. The campus preparation profile uses Python 3.12.14; with a different version, first run the check below. The Bash activation commands are the same in Linux and macOS.

## If the campus environment is already prepared

The `campus_preflight.py --prepare` script creates a separate environment and installs the Python packages. In the preparation kit, the path is set with the `--venv` parameter; the standard launch path is `$HOME/.venvs/bassein-12-10`. If technical support gave you a different path, use it.

```bash
source "$HOME/.venvs/bassein-12-10/bin/activate"
python3 -c "import sys; print(sys.executable); print(sys.version)"
python3 check_environment_eng.py
python3 client_eng.py demo
```

The first command only activates the existing environment. If the `bin/activate` file isn’t found, the preparation for this path hasn’t been done yet. Check the path with technical support or create a personal environment following the steps below. In a new terminal, the activation has to be repeated. To exit the environment, run `deactivate`.

## If you need to create a personal environment

Run from the project root:

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r materials/requirements_eng.txt -c materials/requirements-campus.lock_eng.txt
python3 -m pip check
python3 check_environment_eng.py
python3 client_eng.py demo
```

`materials/requirements_eng.txt` lists the project packages, and `materials/requirements-campus.lock_eng.txt` limits the versions of their dependencies. The command installs only the package tree needed for this project. Installation requires access to an allowed package repository; with a restricted network, use the prepared campus environment or contact technical support.

If there’s no `python3`, the version is lower than 3.12, or creating the environment reports that `venv`/`ensurepip` is missing, system components are needed. Their names and the installation method depend on the Linux distribution — contact technical support with the full text of the error. Python packages are installed inside the environment; `sudo pip`, `--user`, and bypassing the protection of the system Python aren’t needed.

Don’t add the `.venv/` folder to Git. Git, an editor, and a browser are separate programs: `pip` doesn’t install them.

## The first result

The demo should show the `hoodie` product (price 500, M stock — 5) and the expected `PRODUCT_NOT_FOUND` refusal for `missing`. This is a real local MCP call. Model access, an API key, and the internet aren’t needed for the call itself.

`python3 -m pytest -c pytest_eng.ini testing/test_example_eng.py -q` checks the provided example. The full check `python3 checks/acceptance_eng.py --project . --profile base` doesn’t pass on the starting template: the descriptions and the functions with `TODO` are yet to be implemented in the tasks.
