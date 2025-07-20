# Contributing to AI-Powered Code Review for ML Pipelines

Thank you for considering contributing to this project! Your help makes it better for everyone.

## 📝 How to Contribute

1. **Fork the repository** and create your branch from `main`:
   ```bash
   git checkout -b feature/YourFeatureName

2. **Install dependencies** and set up your environment as described in the README.
3. **Write clear, descriptive commit messages** and follow the [Conventional Commits](https://www.conventionalcommits.org/) format.
4. **Add tests** for any new feature or bug fix.
5. **Run all tests** and ensure they pass:

   ```bash
   pytest --maxfail=1 --disable-warnings -q
   ```
6. **Submit a Pull Request**:

   * Base branch: `main`
   * Provide a summary of changes and link to any related issues.

## 🎨 Code Style

* **Follow PEP 8** for Python code.
* Use **flake8** for linting:

  ```bash
  flake8 .
  ```
* Document public functions and classes with **docstrings**.

## 📑 Issue Guidelines

* Search for existing issues before opening a new one.
* When reporting a bug, include:

  * Steps to reproduce
  * Expected behavior
  * Actual behavior
  * Environment details (OS, Python version, dependencies)

## 🧪 Testing

* Place new tests in the `tests/` directory.
* Use **pytest** fixtures and assertions.

## 🚧 Development Workflow

* Keep your branch up to date by rebasing on `main` regularly:

  ```bash
  git fetch origin
  git rebase origin/main
  ```
* Squash minor fixup commits into meaningful commits before merging.

## 🙌 Code of Conduct

This project follows the [Contributor Covenant](https://www.contributor-covenant.org/) Code of Conduct. By participating, you agree to abide by its terms.

---

*Thank you for improving AI-Powered Code Review for ML Pipelines!*
