# pylearn

A sandbox for learning Python. Managed with [uv](https://docs.astral.sh/uv/).

## Layout

```
src/pylearn/   the package — your code goes here
tests/         pytest tests, one test_*.py file per topic
pyproject.toml project metadata, dependencies and tool settings
uv.lock        exact resolved versions (commit it, don't edit it)
```

## Everyday commands

```sh
uv sync                 # create .venv and install everything from uv.lock
uv run pylearn          # run the app (the `main` function)
uv run pytest           # run the tests
uv run ruff check .     # lint
uv run ruff format .    # auto-format
uv add <package>        # add a dependency
uv add --dev <package>  # add a dev-only dependency
```

`uv run` always uses the project's `.venv`, so there is no need to activate it.
