# AI Pytest Test Case Generator

An AI-powered Python tool that automatically generates structured **Pytest** test cases from a given Python function using a **locally hosted language model**.

This project is designed to reduce the manual effort involved in writing unit tests by leveraging an LLM to analyze function logic, edge cases, and expected behavior.

---

## Features

- Generates ready-to-run **Pytest** test cases
- Works with a **local LLM** (no API calls required)
- Handles:
  - Basic cases
  - Edge cases
  - Invalid input scenarios
- CLI-based workflow
- Optimized for lightweight models and low memory usage
- Fallback logic for safer generation

---

## Project Structure
├── ai_module.py # Core AI + prompt logic
├── generate_from_prompt.py # LLM interaction and response handling
├── test_gen.py # CLI entry point
├── examples/ # Sample input functions
├── tests/ # Generated pytest files
├── output/ # Generated outputs
├── .gitignore
└── README.md


---

## How It Works

1. The user provides a Python function.
2. The function is converted into a structured prompt.
3. A local language model analyzes the function.
4. Pytest-compatible test cases are generated.
5. Output is saved as a runnable test file.

---

## Usage

Run the test generator using:

```bash
python test_gen.py

```

Requirements
Python 3.10+
Pytest
PyTorch
Local LLM (e.g. DeepSeek-Coder-1.3B-Instruct)
