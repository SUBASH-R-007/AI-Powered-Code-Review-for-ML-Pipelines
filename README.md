# ML Code Reviewer: Core Engine

This project provides a powerful, static analysis engine designed to automatically review Python machine learning code. It acts as an intelligent assistant, identifying common pitfalls, promoting best practices, and flagging potential issues ranging from critical data leakage to subtle performance optimizations.

This version is a command-line tool that houses the core analysis logic, perfect for integration into larger CI/CD pipelines or for local development use.

## How It Works

The reviewer employs a multi-layered analysis strategy to inspect code:

1.  **Regex-Based Pattern Matching:** It uses a comprehensive set of regular expressions to quickly find common anti-patterns and good practices (e.g., detecting `fit_transform` on a test set or the use of `pickle.load`).
2.  **Abstract Syntax Tree (AST) Analysis:** The code is parsed into an AST, allowing the reviewer to understand its structure and detect syntax errors without actually executing it.
3.  **Rule-Based Heuristics:** A modular rules engine checks for more complex, context-dependent issues, such as suggesting hyperparameter tuning for sophisticated models or recommending feature scaling for scale-sensitive algorithms.

The results are then compiled into a prioritized, human-readable report.

## Project Structure

The project is organized into a clean, modular structure:

```text
ml_code_reviewer_project/
├── reviewer/
│   ├── __init__.py          # Makes 'reviewer' a Python package
│   ├── analyzer.py          # The core MLCodeReviewer class and analysis logic
│   └── rules.py             # A comprehensive, easily-extendable dictionary of rules
├── tests/
│   ├── __init__.py          # Makes 'tests' a Python package
│   └── test_analyzer.py     # Unit tests for the reviewer's logic
├── main.py                  # A demonstration script to run the reviewer with examples
├── requirements.txt         # Python dependencies for the project
└── README.md                # This file
```

## Getting Started

Follow these steps to get the reviewer up and running on your local machine.

### 1. Installation

Ensure you have Python 3.x installed. It's recommended to work within a virtual environment.

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install the necessary dependencies
pip install -r requirements.txt
```

### 2. Running the Demonstration

To see the reviewer in action, execute the `main.py` script. It will run an analysis on several pre-defined code snippets and print a detailed report for each.

```bash
python main.py
```

## Running Tests

To verify that the analysis logic is working as expected, you can run the suite of unit tests using Python's built-in `unittest` module.

```bash
python -m unittest discover
```

## Extending the Reviewer

The reviewer is designed to be easily extensible. To add a new check:

1.  **Open `reviewer/rules.py`**.
2.  Add your new pattern or logic to the appropriate category (e.g., `data_leakage`, `code_quality`).
3.  The `analyzer` will automatically pick up and apply the new rule during its next run.

## Future Work

The core logic in this project is self-contained and can be readily integrated into a larger application. Future plans include:

* **Web Interface:** Building a Flask/FastAPI backend and a React/HTML frontend for an interactive user experience.
* **CI/CD Integration:** Creating a GitHub Action or GitLab CI template to automatically review code in pull requests.
