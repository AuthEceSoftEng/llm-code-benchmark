# AppliedEval final evaluation report

AppliedEval contains 57 corrected, executable tasks. Every model was evaluated with the same task set and denominator. A task is correct only when the complete test suite passes.

## Overall performance

| Model | Correct | Accuracy |
|---|---:|---:|
| GPT-5.6 Luna | 53/57 | 92.98% |
| DeepSeek V4 Pro | 53/57 | 92.98% |
| GPT-5.6 Sol | 52/57 | 91.23% |
| Kimi K2.6 | 52/57 | 91.23% |
| Gemini 3.5 Flash | 52/57 | 91.23% |
| DeepSeek V4 Flash | 52/57 | 91.23% |
| Qwen 3.7 Max | 51/57 | 89.47% |
| Kimi K3 | 51/57 | 89.47% |
| Claude Sonnet 5 | 51/57 | 89.47% |
| Claude Opus 4.8 | 51/57 | 89.47% |
| Qwen 3.7 Plus | 50/57 | 87.72% |
| GPT-5.6 Terra | 50/57 | 87.72% |
| GLM 5.2 | 49/57 | 85.96% |
| MiMo v2.5 Pro | 49/57 | 85.96% |
| MiniMax M3 | 47/57 | 82.46% |

## Category summary

| Category | Tasks | Mean model accuracy | Best accuracy | Worst accuracy |
|---|---:|---:|---:|---:|
| Bit Manipulation & Mathematical Computing | 8 | 99.17% | 100.00% | 87.50% |
| Graph, Tree & Dynamic Programming | 6 | 95.56% | 100.00% | 66.67% |
| Array, Sequence & Data Structures | 13 | 91.28% | 100.00% | 84.62% |
| String Processing & Validation | 22 | 88.18% | 100.00% | 77.27% |
| System Processing & Complex Validation | 8 | 74.17% | 75.00% | 62.50% |

## String Processing & Validation (22 tasks)

| Rank | Model | Correct | Accuracy |
|---:|---|---:|---:|
| 1 | DeepSeek V4 Pro | 22/22 | 100.00% |
| 2 | GPT-5.6 Luna | 21/22 | 95.45% |
| 3 | Qwen 3.7 Plus | 20/22 | 90.91% |
| 4 | GPT-5.6 Sol | 20/22 | 90.91% |
| 5 | Kimi K3 | 20/22 | 90.91% |
| 6 | DeepSeek V4 Flash | 20/22 | 90.91% |
| 7 | Claude Sonnet 5 | 20/22 | 90.91% |
| 8 | Claude Opus 4.8 | 20/22 | 90.91% |
| 9 | Qwen 3.7 Max | 19/22 | 86.36% |
| 10 | GPT-5.6 Terra | 19/22 | 86.36% |
| 11 | Kimi K2.6 | 19/22 | 86.36% |
| 12 | Gemini 3.5 Flash | 19/22 | 86.36% |
| 13 | GLM 5.2 | 18/22 | 81.82% |
| 14 | MiMo v2.5 Pro | 17/22 | 77.27% |
| 15 | MiniMax M3 | 17/22 | 77.27% |

**Hardest tasks by cross-model pass rate**

| Task | Models passing | Pass rate |
|---|---:|---:|
| `pretty_print_matrix` | 2/15 | 13.33% |
| `format_duration` | 5/15 | 33.33% |
| `clean_and_split_sentences` | 8/15 | 53.33% |
| `max_repeated_substring` | 11/15 | 73.33% |
| `normalize_filename` | 13/15 | 86.67% |

## Array, Sequence & Data Structures (13 tasks)

| Rank | Model | Correct | Accuracy |
|---:|---|---:|---:|
| 1 | Kimi K2.6 | 13/13 | 100.00% |
| 2 | Gemini 3.5 Flash | 13/13 | 100.00% |
| 3 | DeepSeek V4 Flash | 13/13 | 100.00% |
| 4 | MiMo v2.5 Pro | 12/13 | 92.31% |
| 5 | Qwen 3.7 Plus | 12/13 | 92.31% |
| 6 | Qwen 3.7 Max | 12/13 | 92.31% |
| 7 | GPT-5.6 Sol | 12/13 | 92.31% |
| 8 | GPT-5.6 Luna | 12/13 | 92.31% |
| 9 | DeepSeek V4 Pro | 12/13 | 92.31% |
| 10 | Claude Sonnet 5 | 12/13 | 92.31% |
| 11 | GLM 5.2 | 11/13 | 84.62% |
| 12 | GPT-5.6 Terra | 11/13 | 84.62% |
| 13 | Kimi K3 | 11/13 | 84.62% |
| 14 | MiniMax M3 | 11/13 | 84.62% |
| 15 | Claude Opus 4.8 | 11/13 | 84.62% |

**Hardest tasks by cross-model pass rate**

| Task | Models passing | Pass rate |
|---|---:|---:|
| `summarize_category_totals` | 8/15 | 53.33% |
| `rotate_matrix` | 9/15 | 60.00% |
| `MinStack` | 13/15 | 86.67% |
| `find_balanced_sublist` | 14/15 | 93.33% |
| `find_peak_index` | 14/15 | 93.33% |

## Graph, Tree & Dynamic Programming (6 tasks)

| Rank | Model | Correct | Accuracy |
|---:|---|---:|---:|
| 1 | GLM 5.2 | 6/6 | 100.00% |
| 2 | MiMo v2.5 Pro | 6/6 | 100.00% |
| 3 | Qwen 3.7 Max | 6/6 | 100.00% |
| 4 | GPT-5.6 Terra | 6/6 | 100.00% |
| 5 | GPT-5.6 Sol | 6/6 | 100.00% |
| 6 | GPT-5.6 Luna | 6/6 | 100.00% |
| 7 | Kimi K3 | 6/6 | 100.00% |
| 8 | Kimi K2.6 | 6/6 | 100.00% |
| 9 | Gemini 3.5 Flash | 6/6 | 100.00% |
| 10 | DeepSeek V4 Flash | 6/6 | 100.00% |
| 11 | Claude Sonnet 5 | 6/6 | 100.00% |
| 12 | Claude Opus 4.8 | 6/6 | 100.00% |
| 13 | MiniMax M3 | 5/6 | 83.33% |
| 14 | DeepSeek V4 Pro | 5/6 | 83.33% |
| 15 | Qwen 3.7 Plus | 4/6 | 66.67% |

**Hardest tasks by cross-model pass rate**

| Task | Models passing | Pass rate |
|---|---:|---:|
| `resolve_dependencies` | 12/15 | 80.00% |
| `can_form_expression` | 14/15 | 93.33% |
| `can_finish_prereqs` | 15/15 | 100.00% |
| `binary_tree_paths` | 15/15 | 100.00% |
| `bfs_order` | 15/15 | 100.00% |

## Bit Manipulation & Mathematical Computing (8 tasks)

| Rank | Model | Correct | Accuracy |
|---:|---|---:|---:|
| 1 | GLM 5.2 | 8/8 | 100.00% |
| 2 | MiMo v2.5 Pro | 8/8 | 100.00% |
| 3 | Qwen 3.7 Plus | 8/8 | 100.00% |
| 4 | Qwen 3.7 Max | 8/8 | 100.00% |
| 5 | GPT-5.6 Terra | 8/8 | 100.00% |
| 6 | GPT-5.6 Sol | 8/8 | 100.00% |
| 7 | GPT-5.6 Luna | 8/8 | 100.00% |
| 8 | Kimi K3 | 8/8 | 100.00% |
| 9 | Kimi K2.6 | 8/8 | 100.00% |
| 10 | MiniMax M3 | 8/8 | 100.00% |
| 11 | Gemini 3.5 Flash | 8/8 | 100.00% |
| 12 | DeepSeek V4 Pro | 8/8 | 100.00% |
| 13 | DeepSeek V4 Flash | 8/8 | 100.00% |
| 14 | Claude Opus 4.8 | 8/8 | 100.00% |
| 15 | Claude Sonnet 5 | 7/8 | 87.50% |

**Hardest tasks by cross-model pass rate**

| Task | Models passing | Pass rate |
|---|---:|---:|
| `unique_permutations` | 14/15 | 93.33% |
| `minimal_partition_difference` | 15/15 | 100.00% |
| `has_balanced_bits` | 15/15 | 100.00% |
| `longest_prime_gap` | 15/15 | 100.00% |
| `single_number_triplicates` | 15/15 | 100.00% |

## System Processing & Complex Validation (8 tasks)

| Rank | Model | Correct | Accuracy |
|---:|---|---:|---:|
| 1 | GLM 5.2 | 6/8 | 75.00% |
| 2 | MiMo v2.5 Pro | 6/8 | 75.00% |
| 3 | Qwen 3.7 Plus | 6/8 | 75.00% |
| 4 | Qwen 3.7 Max | 6/8 | 75.00% |
| 5 | GPT-5.6 Terra | 6/8 | 75.00% |
| 6 | GPT-5.6 Sol | 6/8 | 75.00% |
| 7 | GPT-5.6 Luna | 6/8 | 75.00% |
| 8 | Kimi K3 | 6/8 | 75.00% |
| 9 | Kimi K2.6 | 6/8 | 75.00% |
| 10 | MiniMax M3 | 6/8 | 75.00% |
| 11 | Gemini 3.5 Flash | 6/8 | 75.00% |
| 12 | DeepSeek V4 Pro | 6/8 | 75.00% |
| 13 | Claude Sonnet 5 | 6/8 | 75.00% |
| 14 | Claude Opus 4.8 | 6/8 | 75.00% |
| 15 | DeepSeek V4 Flash | 5/8 | 62.50% |

**Hardest tasks by cross-model pass rate**

| Task | Models passing | Pass rate |
|---|---:|---:|
| `rank_projects_by_score` | 0/15 | 0.00% |
| `filter_map_validate` | 0/15 | 0.00% |
| `classify_severity` | 14/15 | 93.33% |
| `normalize_user_roles` | 15/15 | 100.00% |
| `safe_deep_get` | 15/15 | 100.00% |

## Interpretation

AppliedEval is more demanding than a collection of isolated algorithmic exercises because correctness depends on applying an algorithm under explicit contracts, heterogeneous inputs, validation rules, ordering constraints, and realistic data transformations.

The strongest results are obtained by DeepSeek V4 Pro and GPT-5.6 Luna at 53/57 (92.98%), followed by DeepSeek V4 Flash, Gemini 3.5 Flash, Kimi K2.6, and GPT-5.6 Sol at 52/57 (91.23%). The weakest result is MiniMax M3 at 47/57 (82.46%). The overall spread is 10.52 percentage points, demonstrating useful but not extreme separation across the remaining 15 models.

Bit Manipulation/Mathematical Computing has the highest mean accuracy (99.17%), and Graph/Tree/Dynamic Programming is also close to saturation at 95.56%. System Processing/Complex Validation is the main difficulty at 74.17%. String Processing/Validation and Array/Sequence/Data Structures expose errors in exact contracts, state transitions, and invalid-input handling. The 10.52-point overall range is descriptive rather than evidence of a definitive ranking.

The benchmark should therefore be reported with category scores rather than a single aggregate number. No pairwise comparison remains significant after Holm correction, so the overall ordering should not be treated as definitive.

The dominant interpretation of failures is semantic rather than syntactic: the generated programs generally execute, but fail one or more assertions involving exact output shape, ordering, boundary cases, malformed input, or interacting constraints.
