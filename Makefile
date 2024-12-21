install:
    uv venv # python3 -m venv .venv
    uv sync --dev # pip install -e .[dev]
run:
    uv run main.py # replace python ./my_lib/my_script.py
test:
    uv run coverage run -m pytest # pytest with coverage
