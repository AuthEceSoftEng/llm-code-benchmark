# AuthEceSoftEng/llm-code-benchmark

Archival reproduction package for the manuscript’s three evaluated benchmarks.
This directory is prepared locally and has not been committed or pushed.

## Authority rules

- `results/extendedeval/` is the authoritative 15-model, 246-task ExtendedEval matrix.
- `results/appliedeval/` is the authoritative 15-model, 57-task AppliedEval matrix.
- `results/humaneval/task_outcomes.jsonl` is the authoritative 15-model, 164-task HumanEval matrix.
- `provenance/humaneval_extendedeval_mapping.csv` contains 164 HumanEval rows: 147 verified pairs and 17 explicit absences. No entry-point inference is used for the absences.
- Provisional matrices and completion files are not included. See `quarantine/README.md`.

## Layout

`datasets/` contains the exact evaluated JSONL snapshots. `provenance/` contains the mapping and schema/checksum metadata. `results/` contains task-level outcomes, paired outcomes, aggregate tables, universal-failure evidence, and manuscript reports. `scripts/` contains the deterministic validation/reproduction command. `figures/` contains derived figure source data and release figures.

## Environment and reproduction

Tested with Python 3.12 and the standard library only. From this directory:

```bash
python3 scripts/reproduce_all.py
```

The command fails loudly on record-count, hash, model, mapping, aggregate, paired-statistic, or saturation-summary mismatches. It writes regenerated tables and validation output under `reproduced/`.

No API key is required. The reproduction command never calls a model provider.

To generate new model completions, see `REPRODUCE_EXPERIMENTS.md` and run
`scripts/run_experiments.py`. This requires a user-owned OpenRouter API key.
New reruns must be stored separately from the authoritative `results/` files.

## Release status

This is an unreleased local archival package. No Git commit, tag, GitHub Release, URL, or DOI has been created. After independent review, publish the repository and record its release URL/DOI in this file and in the manuscript data-availability statement.
