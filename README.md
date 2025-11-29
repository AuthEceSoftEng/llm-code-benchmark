# 🧪 LLM Code Benchmark

A comprehensive toolkit for evaluating Large Language Models (LLMs) on programming tasks using structured benchmarks. Test multiple providers (OpenAI, Claude, Gemini, AWS Bedrock, Grok) with a unified interface.
---

## ✨ Features

- 🎯 **Multi-Provider Support** - Test OpenAI, Claude, Gemini, Bedrock, and Grok models
- 📊 **Comprehensive Benchmarks** - HumanEval, ExtendedEval, and NewCodeBench datasets
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
- **`evaluate_results_of_NewCodeBench.py`** - Evaluate LLM outputs for NewCodeBench.jsonl
- **`evaluate_results_of_ExtendedEval.py`** - Evaluate LLM outputs for ExtendedEval.jsonl
- **`DifficultyLevel.py`** - Analyze and classify problem difficulty
- **`TestCoverage.py`** - Analyze test coverage and edge case handling

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

### 3. Run Evaluation

```bash
# Configure which models to test in example_usage_multiple_models.py
# Then run:
python3 example_usage_multiple_models.py \
    --dataset NewCodeBench.jsonl \
    --field prompt \
    --out results.jsonl

# Evaluate the results
python evaluate_results_of_NewCodeBench.py \
    --results results.jsonl \
    --out evaluation_report.jsonl \
    --verbose
```

---

## 📖 Usage

### Configuring Models

Edit `example_usage_multiple_models.py` to enable the models you want to test:

```python
OPENAI_MODELS = [
    "gpt-5-2025-08-07",
]

GOOGLE_MODELS = [
    "gemini-2.5-pro",
    "gemini-2.0-flash",
]

BEDROCK_MODELS = [
    "us.anthropic.claude-sonnet-4-20250514-v1:0",
]
```

### Running on Different Datasets

```bash
python3 example_usage_multiple_models.py \
    --dataset NewCodeBench.jsonl \
    --field prompt \
    --out results.jsonl
```

### Evaluating Results

#### For NewCodeBench.jsonl or MyOwnBench.jsonl

```bash
# Basic evaluation
#### For NewCodeBench.jsonl

```bash
python evaluate_results_of_NewCodeBench.py \
    --results results.jsonl \
    --out evaluation_report.jsonl \
    --verbose
```

#### For ExtendedEval.jsonl

```bash
python evaluate_results_of_ExtendedEval.py \
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

### Analyzing Difficulty Levels

Classify problems by complexity using multiple metrics:

```bash
python DifficultyLevel.py \
    --input NewCodeBench.jsonl \
    --out difficulty_analysis.csv
```

**Metrics Analyzed:**
- Code complexity (branching, loops, nesting depth)
- Recursion usage
- Exception handling
- Test case characteristics
- Prompt complexity and constraints

### Analyzing Test Coverage

Assess edge case coverage in test suites:

```bash
python TestCoverage.py \
    --input NewCodeBench.jsonl \
    --out coverage_report.csv \
    --markdown coverage_summary.md \
    --summary
```

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


## Examples

### Real-World Workflow Examples

#### Example 1: Single Model Evaluation with Google Gemini

```bash
# Activate environment
source venv/bin/activate

# Set API key
export GOOGLE_API_KEY="your-google-api-key"

# Run evaluation
python3 example_usage_multiple_models.py \
    --dataset MyOwnBench.jsonl \
    --field prompt \
    --out results.jsonl

# Evaluate results
python evaluate_results_of_NewCodeBench.py \
    --results results.jsonl \
    --out evaluation_report.jsonl \
    --verbose
```

#### Example 2: AWS Bedrock with Region Configuration

```bash

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

