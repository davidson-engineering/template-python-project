install:
    uv sync # pip install -r 
    uv pip install .[test] # pip install -e .
run_main:
    uv run main.py # replace python ./my_lib/my_script.py
test:
    uv run pytest -n auto --cov-report=xml # replace uv run pytest -n auto --cov-report=xml
