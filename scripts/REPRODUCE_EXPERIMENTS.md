# Re-running the model experiments

The package contains the public runner needed to generate new completions. It
does not contain credentials. New calls require an OpenRouter account and may
incur cost; they are not needed to reproduce the released tables.

## Setup

Use Python 3.12 or newer. The runner uses only the Python standard library:

```bash
export OPENROUTER_API_KEY='your-key'
cd llm-code-benchmark
```

The 15 exact model IDs and default protocol are in
`configs/models.json`. The default protocol is temperature 0, top-p 1,
16,384 output tokens, two transport retries, and 300 seconds per request.

## Smoke test

```bash
python3 scripts/run_experiments.py \
  --dataset datasets/ExtendedEval.jsonl \
  --model qwen/qwen3.7-max \
  --limit 2 --workers 2 \
  --output /tmp/smoke_qwen.jsonl
```

## Full run for one model

```bash
python3 scripts/run_experiments.py \
  --dataset datasets/ExtendedEval.jsonl \
  --model qwen/qwen3.7-max \
  --workers 50 --timeout 300 --retries 2 \
  --output results/reruns/qwen3_7_max_ExtendedEval.jsonl
```

Repeat the command for each model in `configs/models.json`. Use `--resume` to
reuse successful records after an interrupted run.

## Reasoning protocol

The default `--reasoning none` sends `{"effort":"none","exclude":true}`.
If a provider rejects that setting, the run must be recorded as unsupported;
do not silently switch protocols. `--reasoning minimal` is an explicit
deviation and uses low effort. `--reasoning allow` omits the reasoning field.

## Important reproducibility note

Provider model versions, routing, availability, and pricing can change. New
completions therefore do not replace the authoritative outcomes in `results/`.
Save reruns separately and record the date, model metadata, generation body,
provider response, retries, and evaluator version.

After generation, use the existing stored-result analysis workflow for formal
comparisons. The release validator remains:

```bash
python3 scripts/reproduce_all.py
```
