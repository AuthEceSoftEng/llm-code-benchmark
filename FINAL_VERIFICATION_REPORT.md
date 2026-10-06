# Final verification report

Status: local archival package prepared; no commit, push, tag, GitHub Release,
or model/API call was made.

## Commands run

All commands below were run from this package directory and used only packaged
or previously supplied local artifacts:

```text
python3 scripts/reproduce_all.py
```

Result: `PASS`; 164 HumanEval records, 246 ExtendedEval records, 57 AppliedEval
records, 15 models, 147 verified pairs, 17 explicit absences, and 2,205 paired
rows. Published ExtendedEval totals, paired statistics, saturation summaries,
and HumanEval retained/excluded accounting all matched the release gates.

The reference-suite audits were run offline before packaging:

```text
python3 audit_extendedeval.py --dataset datasets/ExtendedEval.jsonl --out <local-audit-output>
python3 audit_appliedeval.py datasets/AppliedEval.jsonl
```

The ExtendedEval audit reported 246/246 canonical solutions passing. The
AppliedEval audit reported 57/57 canonical solutions passing with no structural
failures. Temporary audit outputs were not copied into the package except for
the sanitized JSON audit records under `provenance/`.

The figure source was converted locally into `figures/overall_accuracy.svg`,
`figures/overall_accuracy.png`, and `figures/overall_accuracy.pdf`.

## Generated and checked artifacts

- `datasets/`: exact 164/246/57 evaluated snapshots.
- `provenance/humaneval_extendedeval_mapping.csv`: 164 rows, 147 verified
  mappings, 17 explicit absences.
- `results/extendedeval/`: 15 authoritative task-level matrices reproducing
  the published 246-task totals.
- `results/appliedeval/`: 15 authoritative task-level matrices.
- `results/humaneval/task_outcomes.jsonl`: 2,460 task-level outcomes.
- `results/paired/paired_task_outcomes.csv`: exactly 2,205 rows.
- `results/paired/`: paired counts, exact McNemar tests, Holm correction,
  bootstrap intervals, Spearman, and Kendall tau-b outputs.
- `results/saturation/`: paired-subset saturation and 0/105 contrast summary.
- `results/universal/`: universal-failure evidence and dossier.
- `results/aggregates/`: overall/category/error/hardest-task tables and
  statistical summaries.
- `figures/source/` and `figures/`: figure source data and generated figures.
- `release_manifest.json`: counts, models, result-file hashes, and parameters.
- `SHA256SUMS`: SHA-256 checksums for every release file except the checksum
  file itself.

The authoritative validation output is
`reproduced/validation_report.json`.

## Reproduction gates confirmed

- ExtendedEval published totals: exact match for all 15 models.
- Paired subset: 147 × 15 = 2,205 rows.
- HumanEval excluded tasks: 248/255; retained tasks: 2,119/2,205.
- Paired score ranges: 6.12 and 10.20 percentage points.
- Universal passes: 118 and 79; non-universal tasks: 28 and 63.
- Between-model Holm-significant contrasts: 0/105 in both paired subsets.
- Paired correlations: Spearman 0.2109; Kendall tau-b 0.1641.

## Deviations and release notes

- This folder is intentionally unreleased: no commit, tag, GitHub Release, or
  DOI was created.
- No original manuscript PDF/PNG figures were available in the source
  workspace; the included figures are generated archival derivatives from the
  packaged source CSV.
- No authoritative design-operation coding artifact was supplied. No such
  labels were invented; the limitation is documented in
  `results/aggregates/DESIGN_OPERATION_CODING.md`.
- AppliedEval JSONL files omit a model field; the package records the exact
  filename-to-model mapping in the release manifest.
- The 17 explicit absences have no contemporaneous exclusion explanation in
  the supplied mapping. The package says this explicitly and does not infer a
  reason from entry-point similarity.
