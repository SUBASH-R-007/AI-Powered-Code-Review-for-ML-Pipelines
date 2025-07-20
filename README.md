# 🤖 AI-Powered Code Review for ML Pipelines

An **AI-driven** tool that automates code reviews specifically tailored for **Machine Learning (ML) pipelines**. It analyzes code for best practices, identifies performance bottlenecks, detects potential bugs, and ensures adherence to industry standards—all to boost the reliability, maintainability, and performance of your ML projects.

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)

---

## 🔍 Features

- **Best-Practice Enforcement**: Checks for coding standards, naming conventions, and project structure.
- **Performance Profiling**: Detects expensive operations, memory leaks, and suggests optimizations.
- **Bug Detection**: Flags potential runtime errors, data leaks, and security vulnerabilities.
- **ML-Specific Insights**: Validates data loading, feature transformation, model training loops, and serialization.
- **Customizable Rules**: Extend or override default review rules via a plugin architecture.
- **Automated Reports**: Generates detailed review reports in HTML or Markdown.

---

## 🛠 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Prasanna-Nadrajan/AI-Powered-Code-Review-for-ML-Pipelines.git
   cd AI-Powered-Code-Review-for-ML-Pipelines.git


2. **Create a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

1. **Run a review** on your ML project folder:

   ```bash
   ai-review --path /path/to/your/ml/project --output report.md
   ```
2. **View the report**:

   ```bash
   open report.md
   ```
3. **Customize rules** by editing `config/rules.yaml`.

---

## ⚙️ Configuration

* **`config/rules.yaml`**: Defines which checks are active and their severity levels.
* **`config/plugins/`**: Drop custom Python modules to extend review capabilities.
* **CLI Options**:

  * `--path`: Path to the target project.
  * `--output`: File path for the generated report.
  * `--format`: Report format (`md`, `html`, `json`).

---

## 🏗️ Architecture

1. **Parser Layer**: Builds an AST of your code and ML pipeline definitions.
2. **Rule Engine**: Applies a suite of linting and profiling rules.
3. **Report Generator**: Compiles findings into user-friendly formats.
4. **Plugin Loader**: Dynamically loads custom rule sets.

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---
