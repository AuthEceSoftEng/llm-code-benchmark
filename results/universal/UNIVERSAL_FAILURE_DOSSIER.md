# UNIVERSAL_FAILURE_DOSSIER

Source: stored release task-level outcomes only. No model/API calls were made. A 0/15 result is an empirical observation, not proof of benchmark quality.

The stored artifacts confirm that all 246 ExtendedEval reference solutions and all 57 AppliedEval reference solutions pass their complete suites. The repository does not contain a reviewer record proving that two experienced software engineers independently reviewed every prompt, reference implementation, and test. Therefore that review is recorded as **not evidenced**, not claimed as completed.

## ExtendedEval/7_regex — `filter_by_pattern`

Contract summary: Filter strings by literal or regex pattern, with case-insensitive and inverted matching options.

Release pass rate: **0/15 (0.00%)**.
Reference implementation: **passes the complete stored suite**.
Independent engineering review: **not evidenced in stored artifacts**; no claim of completed dual review is made.

Requirement-to-test trace: Literal-match tests, regex tests, case-insensitive tests, inversion tests, and malformed-pattern handling are exercised.

Failure-category counts:
- `invalid_input_or_validation`: 15/15

Representative first failing assertions:
- `assert candidate(['test[abc', 'normal'], 'test[', use_regex=True) == ['test[abc']`

Dominant interpretation: malformed-regex behavior or regex error handling was not implemented as required. This may reflect genuine contract difficulty, specification sensitivity, or both; zero-pass alone cannot distinguish them.
Release decision: **revise**.

## ExtendedEval/14 — `all_prefixes`

Contract summary: Return prefixes subject to minimum/maximum length, step, and optional reverse ordering.

Release pass rate: **0/15 (0.00%)**.
Reference implementation: **passes the complete stored suite**.
Independent engineering review: **not evidenced in stored artifacts**; no claim of completed dual review is made.

Requirement-to-test trace: Empty input, default prefixes, min/max bounds, step=2/3, and reverse ordering are tested.

Failure-category counts:
- `boundary_or_threshold`: 15/15

Representative first failing assertions:
- `assert candidate('abcdef', step=2) == ['ab', 'abcd', 'abcdef']`
- `assert candidate('') == []`

Dominant interpretation: prefix step/bounds semantics were miscomputed. This may reflect genuine contract difficulty, specification sensitivity, or both; zero-pass alone cannot distinguish them.
Release decision: **retain**.

## ExtendedEval/15 — `string_sequence`

Contract summary: Generate an inclusive space-delimited integer sequence with direction checks and step-zero validation.

Release pass rate: **0/15 (0.00%)**.
Reference implementation: **passes the complete stored suite**.
Independent engineering review: **not evidenced in stored artifacts**; no claim of completed dual review is made.

Requirement-to-test trace: Default sequence, custom start, positive/negative steps, incompatible directions, and step=0 ValueError are tested.

Failure-category counts:
- `boundary_or_threshold`: 15/15

Representative first failing assertions:
- `assert candidate(3, start=5) == ''`
- `assert candidate(-3) == '0 -1 -2 -3'`

Dominant interpretation: inclusive sequence direction or negative-end handling was miscomputed. This may reflect genuine contract difficulty, specification sensitivity, or both; zero-pass alone cannot distinguish them.
Release decision: **retain**.

## ExtendedEval/21_variant2 — `rescale_to_unit`

Contract summary: Scale finite numeric values to [0,1], preserve invalid entries, support duplicates and equal-value inputs.

Release pass rate: **0/15 (0.00%)**.
Reference implementation: **passes the complete stored suite**.
Independent engineering review: **not evidenced in stored artifacts**; no claim of completed dual review is made.

Requirement-to-test trace: Normal scaling, equal values, None/NaN/infinity, duplicate-aware scaling, and all-invalid inputs are tested.

Failure-category counts:
- `invalid_input_or_validation`: 15/15

Representative first failing assertions:
- `assert candidate([1.0, None, 3.0, float('nan')]) == [0.0, None, 1.0, None]`
- `assert candidate([float('nan'), float('inf'), -float('inf')]) == [None, None, None]`

Dominant interpretation: None/non-finite values or scaling edge cases were mishandled. This may reflect genuine contract difficulty, specification sensitivity, or both; zero-pass alone cannot distinguish them.
Release decision: **retain**.

## ExtendedEval/81 — `grade_calculator`

Contract summary: Grade GPAs with invalid/absent handling, custom scale, rounding modes, and optional statistics.

Release pass rate: **0/15 (0.00%)**.
Reference implementation: **passes the complete stored suite**.
Independent engineering review: **not evidenced in stored artifacts**; no claim of completed dual review is made.

Requirement-to-test trace: Basic GPA bands, invalid/absent values, rounding modes, custom scales, and statistics are tested.

Failure-category counts:
- `boundary_or_threshold`: 13/15
- `syntax_error`: 2/15

Representative first failing assertions:
- `assert candidate([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B+', 'C', 'C+', 'A-']`
- `stored runner output did not expose an assertion line`
- `assert candidate([0.5]) == ['D-']`

Dominant interpretation: grade thresholds or rounding/invalid-value semantics were mishandled. This may reflect genuine contract difficulty, specification sensitivity, or both; zero-pass alone cannot distinguish them.
Release decision: **revise**.

## ExtendedEval/148 — `bf`

Contract summary: Return planets strictly between two valid planets, handle case-insensitivity, invalid names, and close pairs.

Release pass rate: **0/15 (0.00%)**.
Reference implementation: **passes the complete stored suite**.
Independent engineering review: **not evidenced in stored artifacts**; no claim of completed dual review is made.

Requirement-to-test trace: Named planet intervals, reversed intervals, invalid names, case-insensitivity, and distance<2 tuple behavior are tested.

Failure-category counts:
- `output_shape_or_format`: 15/15

Representative first failing assertions:
- `assert candidate('Earth', 'Earth') == ()`
- `assert candidate('Jupiter', 'Neptune') == ('Saturn', 'Uranus'), 'First test error: ' + str(candidate('Jupiter', 'Neptune'))`

Dominant interpretation: planet interval/close-pair return contract was mishandled. This may reflect genuine contract difficulty, specification sensitivity, or both; zero-pass alone cannot distinguish them.
Release decision: **retain**.

## ExtendedEval/149 — `sorted_list_sum`

Contract summary: Lowercase, remove odd-length/digit/special-character strings, and sort valid strings by length then alphabetically.

Release pass rate: **0/15 (0.00%)**.
Reference implementation: **passes the complete stored suite**.
Independent engineering review: **not evidenced in stored artifacts**; no claim of completed dual review is made.

Requirement-to-test trace: Odd lengths, normalization, digits/special characters, duplicates, length sorting, and alphabetical ties are tested.

Failure-category counts:
- `specification_misinterpretation`: 15/15

Representative first failing assertions:
- `assert candidate(["AI", "ai", "au"]) == ["ai", "au"]`

Dominant interpretation: normalization, filtering, or secondary sort semantics were missed. This may reflect genuine contract difficulty, specification sensitivity, or both; zero-pass alone cannot distinguish them.
Release decision: **revise**.

## ExtendedEval/recursion_2 — `nested_sum`

Contract summary: Recursively sum arbitrarily nested integer lists, including scalar and empty-list base cases.

Release pass rate: **0/15 (0.00%)**.
Reference implementation: **passes the complete stored suite**.
Independent engineering review: **not evidenced in stored artifacts**; no claim of completed dual review is made.

Requirement-to-test trace: Nested lists, empty list, negative values, deep nesting, and scalar base case are tested.

Failure-category counts:
- `state_or_dependency_logic`: 15/15

Representative first failing assertions:
- `assert candidate(42) == 42`

Dominant interpretation: recursive base-case handling was incomplete. This may reflect genuine contract difficulty, specification sensitivity, or both; zero-pass alone cannot distinguish them.
Release decision: **retain**.

## custom_rank_projects_by_score — `rank_projects_by_score`

Contract summary: Rank project records by a score formula, descending score and alphabetical tie-break.

Release pass rate: **0/15 (0.00%)**.
Reference implementation: **passes the complete stored suite**.
Independent engineering review: **not evidenced in stored artifacts**; no claim of completed dual review is made.

Requirement-to-test trace: Five AppliedEval cases cover score ordering, alphabetical ties, zeros, empty input, and lower-scoring projects.

Failure-category counts:
- `invalid_input_or_validation`: 15/15

Representative first failing assertions:
- `AssertionError: Case 0 failed with exception: list indices must be integers or slices, not str`
- `AssertionError: Case 0 failed with exception: 'list' object has no attribute 'get'`

Dominant interpretation: the tested project-record representation was misread or not validated. This may reflect genuine contract difficulty, specification sensitivity, or both; zero-pass alone cannot distinguish them.
Release decision: **revise**.

## se_filter_map_validate_nested — `filter_map_validate`

Contract summary: Normalize, validate, filter, and sort heterogeneous product records under multiple conditional rules.

Release pass rate: **0/15 (0.00%)**.
Reference implementation: **passes the complete stored suite**.
Independent engineering review: **not evidenced in stored artifacts**; no claim of completed dual review is made.

Requirement-to-test trace: Five cases cover currency/price parsing, type/stock/size rules, flags, refurb condition, weight, and final ordering.

Failure-category counts:
- `invalid_input_or_validation`: 15/15

Representative first failing assertions:
- `AssertionError: Case 0 failed: result=[] expected=['A-1', 'B-2']`
- `AssertionError: Case 0 failed: result=['B-2', 'c-3', 'd-4', 'e-5'] expected=['A-1', 'B-2']`

Dominant interpretation: one or more nested normalization/validation gates were missed. This may reflect genuine contract difficulty, specification sensitivity, or both; zero-pass alone cannot distinguish them.
Release decision: **revise**.
