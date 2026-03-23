# Lab 7: Bubble Sort

This project contains a simple Bubble Sort implementation in Python and a basic pytest test suite.

## Project Structure

- main.py: Bubble Sort function and a small runnable example.
- tests/test_main.py: 5 pytest tests for sorting behavior and edge cases.
- requirements-dev.txt: Development dependency list (pytest).

## Requirements

- Python 3.11+ recommended

## Run the Program

From the project root:

```bash
python main.py
```

Expected output:

```text
[1, 2, 4, 5, 8]
```

## Set Up Testing

1. Create and activate a virtual environment (optional but recommended).

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install test dependencies:

```bash
pip install -r requirements-dev.txt
```

3. Run tests:

```bash
pytest -q
```

You should see all 5 tests passing.

## What Is Tested

The test suite checks:

1. Sorting an unsorted list
2. Handling an already sorted list
3. Handling duplicates and negative numbers
4. Handling an empty list
5. In-place behavior (same list object is returned)

## Notes

- The current function name is bbs.
- The algorithm mutates the input list in place.
