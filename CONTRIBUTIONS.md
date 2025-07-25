# Contributing to the ML Code Reviewer

First off, thank you for considering contributing! This project thrives on community involvement, and every contribution is appreciated.

This document provides a set of guidelines for contributing to the ML Code Reviewer. These are mostly guidelines, not strict rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## How Can I Contribute?

There are many ways to contribute, from writing code and tests to improving the documentation and submitting bug reports.

### Reporting Bugs

If you find a bug, please ensure the bug was not already reported by searching on GitHub under [Issues](https://github.com/Prasanna-Nadrajan/AI-Powered-Code-Review-for-ML-Pipelines/issues).

If you're unable to find an open issue addressing the problem, [open a new one](https://github.com/Prasanna-Nadrajan/AI-Powered-Code-Review-for-ML-Pipelines/issues/new). Be sure to include a **title and clear description**, as much relevant information as possible, and a **code sample** or an executable test case demonstrating the expected behavior that is not occurring.

### Suggesting Enhancements

If you have an idea for an enhancement, feel free to open an issue to discuss it. This allows us to coordinate efforts and ensure the proposed change aligns with the project's goals.

Suggestions for new rules are particularly welcome! When suggesting a new rule, please provide:
* A clear description of the problem the rule solves.
* Examples of code that should trigger the rule.
* Examples of good code that should *not* trigger the rule.

### Submitting Changes (Pull Requests)

Ready to contribute code? Here’s how to set up your fork and submit a pull request.

1.  **Fork the repository** on GitHub.
2.  **Clone your fork** locally:
    ```bash
    git clone https://github.com/Prasanna-Nadrajan/AI-Powered-Code-Review-for-ML-Pipelines
    ```
3.  **Create a new branch** for your changes:
    ```bash
    git checkout -b name-of-your-feature-or-fix
    ```
4.  **Set up the development environment** as described in the `README.md`.
5.  **Make your changes.**
6.  **Add or update tests** for your changes in the `tests/` directory.
7.  **Run the test suite** to ensure everything is still working correctly:
    ```bash
    python -m unittest discover
    ```
8.  **Commit your changes** with a clear and descriptive commit message.
9.  **Push your branch** to your fork on GitHub:
    ```bash
    git push origin name-of-your-feature-or-fix
    ```
10. **Open a pull request** to the `main` branch of the original repository. Provide a clear title and description for your pull request, explaining the changes you've made.

## Coding Style

* This project follows the **PEP 8** style guide for Python code.
* Use clear and descriptive variable and function names.
* Add comments to explain complex logic.
* Ensure any new user-facing text is clear and easy to understand.

Thank you again for your interest in contributing!
