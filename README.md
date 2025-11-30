# 🧪 A Framework for Evaluating the Programming Proficiency of Large Language Models

A comprehensive toolkit for evaluating Large Language Models (LLMs) on programming tasks using structured benchmarks. Test multiple providers (OpenAI, Claude, Gemini, AWS Bedrock, Grok) with a unified interface.

## ✨ Features

- 🎯 **Multi-Provider Support** - Test OpenAI, Claude, Gemini, Bedrock, and Grok models
- 📊 **Comprehensive Benchmarks** - HumanEval, ExtendedEval, and AppliedEval datasets
- 🔍 **Automated Evaluation** - Test LLM-generated code against structured test cases
- 📈 **Difficulty Analysis** - Classify problems by complexity metrics
- 🧪 **Coverage Analysis** - Assess edge case coverage in test suites

---

## 📋 Overview

This toolkit consists of four main components:

1. **Model Execution** - Run multiple LLM providers on programming benchmarks
2. **Result Evaluation** - Automatically test LLM-generated code against test cases
3. **Difficulty Analysis** - Classify problems by complexity metrics
4. **Coverage Analysis** - Assess test case comprehensiveness

### Core Scripts

- **`example_usage_multiple_models.py`** - Execute multiple LLM models on benchmark datasets
- **`E1_evaluate_results_of_AppliedEval.py`** - Evaluate LLM outputs for AppliedEval.jsonl
- **`E2_evaluate_results_of_ExtendedEval.py`** - Evaluate LLM outputs for ExtendedEval.jsonl
- **`M5_DifficultyLevel.py`** - Analyze and classify problem difficulty
- **`M4_TestCoverage.py`** - Analyze test coverage and edge case handling

---

##  Quick Start

### 1. Clone and Install

```bash
git clone https://github.com/AuthEceSoftEng/llm-code-benchmark.git
cd llm-code-benchmark

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (includes Multi-LLM SDK)
pip install -r requirements.txt
```

> **Note:** This project uses the [Multi-LLM SDK](https://github.com/dimitrisna/MultiLLM-SDK) for unified LLM provider access.

### 2. Configure API Keys

The easiest way is to use a `.env` file:

```bash
# Copy the example env file
cp .env.example .env

# Edit .env and add your API keys
nano .env  # or use your preferred editor
```

Your `.env` file should look like:
```bash
OPENAI_API_KEY=sk-...
GOOGLE_API_KEY=...
# Add other keys as needed
```

The script will **automatically load** these keys when it runs!

## 3. Analyzing Difficulty Levels

Classify problems by complexity using multiple metrics:

```bash
python M5_DifficultyLevel.py \
    --input AppliedEval.jsonl \
    --out difficulty_analysis.csv
```
This script computes a difficulty score and difficulty category (Easy / Medium / Hard / Challenging) for each task in a HumanEval-style dataset. 
It analyzes:

- The canonical solution using AST (branching, loops, recursion, depth…)
- The prompt (length + constraint words)
- The tests (assert count + pattern features)

What it produces:

- A CSV file where each row includes:
- code features
- prompt features
- test features
- difficulty score
- difficulty bucket

**Metrics Analyzed:**
- Code complexity (branching, loops, nesting depth)
- Recursion usage
- Exception handling
- Test case characteristics
- Prompt complexity and constraints

### 4. Analyzing Test Coverage

Assess edge case coverage in test suites:

```bash
python M4_TestCoverage.py \
    --input AppliedEval.jsonl \
    --out coverage_report.csv \
    --markdown coverage_summary.md \
    --summary

```
This script analyzes a HumanEval-style JSONL dataset and produces coverage metrics for the test cases. 
It checks patterns such as negatives, zeros, floats, large integers, Unicode, exceptions, empty lists/strings, and more.

What it produces:

- A CSV file summarizing per-task test coverage
- An optional Markdown report
- A command-line summary with coverage statistics

**Coverage Categories:**
- Negative numbers
- Zero values
- Large integers (5+ digits)
- Floating-point numbers
- Empty collections (lists, strings)
- None/null values
- Unicode characters
- Exception handling
- Whitespace/escape sequences


## 📖 Usage

### Running on Different Datasets

```bash
python3 example_usage_multiple_models.py \
    --dataset AppliedEval.jsonl \
    --field prompt \
    --out results.jsonl
```


###  Run Evaluation

```bash
# Configure which models to test in example_usage_multiple_models.py
# Then run:
python3 example_usage_multiple_models.py \
    --dataset AppliedEval.jsonl \
    --field prompt \
    --out results.jsonl

# Evaluate the results
python E1_evaluate_results_of_AppliedEval.py \
    --results results.jsonl \
    --out evaluation_report.jsonl \
    --verbose
```

---


#### For AppliedEval.jsonl 

```bash
# Basic evaluation
#### For AppliedEval.jsonl

```bash
python evaluate_results_of_AppliedEval.py \
    --results results.jsonl \
    --out evaluation_report.jsonl \
    --verbose
```

#### For ExtendedEval.jsonl

```bash
python E2_evaluate_results_of_ExtendedEval.py \
    --results results.jsonl \
    --out evaluation_report.jsonl \
    --verbose
```

**Output:**
The evaluation script will:
- Extract Python code from LLM responses
- Run code against structured test cases
- Handle both function-based and class-based tasks
- Generate a detailed report with pass/fail status
- Display final accuracy metrics


## 🔍 Troubleshooting

### ModuleNotFoundError: multi_llm_sdk

```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### API Key Not Found

```bash
# Make sure .env file exists and has your keys
cp .env.example .env
# Edit .env with your actual API keys
```

