# Data schema

All datasets are UTF-8 JSON Lines.

- HumanEval: `task_id`, `prompt`, `entry_point`, `canonical_solution`, `test`.
- ExtendedEval: the same core fields plus release provenance/category metadata where present; 246 unique task IDs.
- AppliedEval: `task_id`, `prompt`, `entry_point`, `canonical_solution`, structured `test`, and category metadata; 57 unique task IDs.
- HumanEval–ExtendedEval mapping: one row per HumanEval task. `primary_extended_task_id` is populated for 147 verified one-to-one pairs and empty for the 17 explicit absences. `release_exclusion_reason` is added in the packaged copy for every absent row.

Task-level result JSONL files contain one record per model/task and preserve the stored evaluator fields, including `passed`, status, runner output, and error type where available.
