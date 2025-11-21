# LLM Programming Evaluation Toolkit

This toolkit provides files for evaluating Large Language Models (LLMs) on programming tasks using structured benchmarks like NewCodeBench, ExtendedEval, and similar datasets.


##  Overview

This toolkit consists of four main components:

1. **Model Execution** - Run multiple LLM providers on programming benchmarks
2. **Result Evaluation** - Automatically test LLM-generated code against test cases
3. **Difficulty Analysis** - Classify problems by complexity metrics
4. **Coverage Analysis** - Assess test case comprehensiveness

##  Files Description

### Core Scripts

- **`example_usage_multiple_models.py`** - Execute multiple LLM models on benchmark datasets
- **`evaluate_results_of_NewCodeBench.py`** - Evaluate LLM outputs for NewCodeBench.jsonl
- **`evaluate_results_of_ExtendedEval.py`** - Evaluate LLM outputs for ExtendedEval.jsonl
- **`DifficultyLevel.py`** - Analyze and classify problem difficulty
- **`TestCoverage.py`** - Analyze test coverage and edge case handling

## 🔧 Prerequisites

### Python Requirements

```bash
python >= 3.8
```

## 🛠️ Installation & Setup

### Step 1: Create Virtual Environment

```bash
# Create a Python virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

### Step 2: Install Dependencies

**Step 1: Install**
```bash
pip install -e ".[dev]"
```

**step 2: Install from requirements.txt**
```bash
pip install -r requirements.txt
````

### Step 3: Configure API Keys

#### For OpenAI
```bash
export OPENAI_API_KEY="your-openai-key-here"
```

#### For Anthropic (Claude)
```bash
export ANTHROPIC_API_KEY="your-anthropic-key-here"
```

#### For Google (Gemini)
```bash
export GOOGLE_API_KEY="your-google-api-key-here"
```

#### For xAI (Grok)
```bash
export XAI_API_KEY="your-xai-api-key-here"
```

#### For AWS Bedrock

**Option 1: Using AWS Configure (Recommended)**
```bash
aws configure
# Enter your AWS Access Key ID
# Enter your AWS Secret Access Key
# Enter default region: us-east-1 (or eu-central-1)
# Enter default output format: json
```

**Option 2: Using Environment Variables**
```bash
export AWS_ACCESS_KEY_ID="your-aws-access-key"
export AWS_SECRET_ACCESS_KEY="your-aws-secret-key"
export AWS_REGION="us-east-1"  # or eu-central-1
```

**Note:** AWS Bedrock availability varies by region. Common regions:
- `us-east-1` (US East - N. Virginia)
- `eu-central-1` (Europe - Frankfurt)

**To change AWS region:**
```bash
export AWS_REGION="eu-central-1"
```

##  Usage

### Quick Start

Here's a complete workflow from setup to evaluation:

```bash
# 1. Activate virtual environment
source venv/bin/activate

# 2. Set up API keys (example with Google)
export GOOGLE_API_KEY="your-key-here"

# 3. Run model evaluation
python3 example_usage_multiple_models.py \
    --dataset NewCodeBench.jsonl \
    --field prompt \
    --out results.jsonl

# 4. Evaluate the results
python evaluate_results_of_NewCodeBench.py \
    --results results.jsonl \
    --out evaluation_report.jsonl
```

### Running Model Evaluations

Execute multiple LLM models on your benchmark dataset:

**Basic usage:**
```bash
python3 example_usage_multiple_models.py
```

**With custom dataset:**
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
# Configure AWS credentials
aws configure
# (Enter your credentials when prompted)

# Set region to US East
export AWS_REGION="us-east-1"

# Run evaluation with Bedrock models
python3 example_usage_multiple_models.py

# If you need to change region
export AWS_REGION="eu-central-1"
python3 example_usage_multiple_models.py
```


## 🔍 Troubleshooting

### Environment Setup Issues

**Issue: Virtual environment not activated**
```bash
# Solution: Activate the virtual environment
source venv/bin/activate

# Verify activation (should show venv in prompt)
which python
```

**Issue: AWS credentials not configured**
```bash
# Solution 1: Use aws configure
aws configure

# Solution 2: Set environment variables
export AWS_ACCESS_KEY_ID="your-key"
export AWS_SECRET_ACCESS_KEY="your-secret"
export AWS_REGION="us-east-1"
```

**Issue: Wrong AWS region for Bedrock**
```bash
# Check current region
echo $AWS_REGION

# Set correct region
export AWS_REGION="us-east-1"  # or eu-central-1
```
