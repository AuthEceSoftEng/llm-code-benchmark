# ExtendedEval: detailed category analysis

This report analyses the fixed 246-task evaluation set. Missing model outputs are counted as failures; category labels are descriptive taxonomy labels based on the task entry points.

## Category summary

| Category | Tasks | Mean model accuracy | Best accuracy | Worst accuracy |
|---|---:|---:|---:|
| Algorithms & data structures | 33 | 93.94% | 100.00% | 84.85% |
| Collections & sequence logic | 78 | 87.86% | 92.31% | 84.62% |
| Numeric & mathematical | 69 | 85.70% | 92.75% | 79.71% |
| Parsing, formats & validation | 28 | 92.38% | 96.43% | 85.71% |
| Text & strings | 38 | 80.00% | 84.21% | 71.05% |

## Algorithms & data structures (33 tasks)

| Rank | Model | Correct | Accuracy |
|---:|---|---:|---:|
| 1 | Qwen 3.7 Max | 33/33 | 100.00% |
| 2 | Claude Opus 4.8 | 32/33 | 96.97% |
| 3 | Claude Sonnet 5 | 32/33 | 96.97% |
| 4 | GPT-5.6 Sol | 32/33 | 96.97% |
| 5 | GPT-5.6 Terra | 32/33 | 96.97% |
| 6 | Kimi K3 | 32/33 | 96.97% |
| 7 | Gemini 3.5 Flash | 31/33 | 93.94% |
| 8 | GPT-5.6 Luna | 31/33 | 93.94% |
| 9 | Kimi K2.6 | 31/33 | 93.94% |
| 10 | MiMo v2.5 Pro | 31/33 | 93.94% |
| 11 | DeepSeek V4 Flash | 30/33 | 90.91% |
| 12 | DeepSeek V4 Pro | 30/33 | 90.91% |
| 13 | GLM 5.2 | 30/33 | 90.91% |
| 14 | Qwen 3.7 Plus | 30/33 | 90.91% |
| 15 | MiniMax M3 | 28/33 | 84.85% |

**Most difficult tasks**

| Task ID | Entry point | Models passing | Pass rate |
|---|---|---:|---:|
| `ExtendedEval/176` | `serialize_deserialize_tree` | 2/15 | 13.33% |
| `ExtendedEval/graph_4` | `topo_sort` | 10/15 | 66.67% |
| `ExtendedEval/so_normalize_path` | `normalize_path` | 11/15 | 73.33% |
| `ExtendedEval/178` | `n_queens` | 13/15 | 86.67% |
| `ExtendedEval/recursion_3` | `unique_permutations` | 14/15 | 93.33% |

**Most consistently solved tasks**

| Task ID | Entry point | Models passing | Pass rate |
|---|---|---:|---:|
| `ExtendedEval/177` | `word_break` | 15/15 | 100.00% |
| `ExtendedEval/174_variant2` | `find_median_sorted_arrays` | 15/15 | 100.00% |
| `ExtendedEval/173_variant2` | `longest_increasing_subsequence` | 15/15 | 100.00% |
| `ExtendedEval/172_variant2` | `sliding_window_maximum` | 15/15 | 100.00% |
| `ExtendedEval/171_variant2` | `merge_k_sorted_lists` | 15/15 | 100.00% |

## Collections & sequence logic (78 tasks)

| Rank | Model | Correct | Accuracy |
|---:|---|---:|---:|
| 1 | Kimi K3 | 72/78 | 92.31% |
| 2 | Claude Opus 4.8 | 71/78 | 91.03% |
| 3 | Gemini 3.5 Flash | 70/78 | 89.74% |
| 4 | GPT-5.6 Terra | 70/78 | 89.74% |
| 5 | MiniMax M3 | 70/78 | 89.74% |
| 6 | GPT-5.6 Luna | 69/78 | 88.46% |
| 7 | Kimi K2.6 | 69/78 | 88.46% |
| 8 | Qwen 3.7 Plus | 69/78 | 88.46% |
| 9 | Claude Sonnet 5 | 68/78 | 87.18% |
| 10 | DeepSeek V4 Pro | 68/78 | 87.18% |
| 11 | GPT-5.6 Sol | 67/78 | 85.90% |
| 12 | Qwen 3.7 Max | 67/78 | 85.90% |
| 13 | DeepSeek V4 Flash | 66/78 | 84.62% |
| 14 | GLM 5.2 | 66/78 | 84.62% |
| 15 | MiMo v2.5 Pro | 66/78 | 84.62% |

**Most difficult tasks**

| Task ID | Entry point | Models passing | Pass rate |
|---|---|---:|---:|
| `ExtendedEval/81` | `grade_calculator` | 0/15 | 0.00% |
| `ExtendedEval/148` | `bf` | 0/15 | 0.00% |
| `ExtendedEval/137` | `compare_one` | 1/15 | 6.67% |
| `ExtendedEval/106` | `f` | 2/15 | 13.33% |
| `ExtendedEval/110` | `exchange` | 2/15 | 13.33% |

**Most consistently solved tasks**

| Task ID | Entry point | Models passing | Pass rate |
|---|---|---:|---:|
| `ExtendedEval/175_variant2` | `regular_expression_match` | 15/15 | 100.00% |
| `ExtendedEval/175` | `regular_expression_match` | 15/15 | 100.00% |
| `ExtendedEval/gh_gitignore_match` | `is_ignored` | 15/15 | 100.00% |
| `ExtendedEval/gh_markdown_toc` | `extract_headings` | 15/15 | 100.00% |
| `ExtendedEval/so_datetime_diff` | `days_diff` | 15/15 | 100.00% |

## Numeric & mathematical (69 tasks)

| Rank | Model | Correct | Accuracy |
|---:|---|---:|---:|
| 1 | Kimi K3 | 64/69 | 92.75% |
| 2 | Claude Opus 4.8 | 62/69 | 89.86% |
| 3 | Gemini 3.5 Flash | 61/69 | 88.41% |
| 4 | GLM 5.2 | 60/69 | 86.96% |
| 5 | GPT-5.6 Sol | 60/69 | 86.96% |
| 6 | GPT-5.6 Terra | 60/69 | 86.96% |
| 7 | Kimi K2.6 | 60/69 | 86.96% |
| 8 | Claude Sonnet 5 | 59/69 | 85.51% |
| 9 | GPT-5.6 Luna | 59/69 | 85.51% |
| 10 | Qwen 3.7 Max | 59/69 | 85.51% |
| 11 | Qwen 3.7 Plus | 59/69 | 85.51% |
| 12 | DeepSeek V4 Pro | 57/69 | 82.61% |
| 13 | MiMo v2.5 Pro | 56/69 | 81.16% |
| 14 | MiniMax M3 | 56/69 | 81.16% |
| 15 | DeepSeek V4 Flash | 55/69 | 79.71% |

**Most difficult tasks**

| Task ID | Entry point | Models passing | Pass rate |
|---|---|---:|---:|
| `ExtendedEval/21_variant2` | `rescale_to_unit` | 0/15 | 0.00% |
| `ExtendedEval/149` | `sorted_list_sum` | 0/15 | 0.00% |
| `ExtendedEval/recursion_2` | `nested_sum` | 0/15 | 0.00% |
| `ExtendedEval/20` | `find_closest_elements` | 1/15 | 6.67% |
| `ExtendedEval/163` | `generate_integers` | 2/15 | 13.33% |

**Most consistently solved tasks**

| Task ID | Entry point | Models passing | Pass rate |
|---|---|---:|---:|
| `ExtendedEval/so_prime_sieve` | `sieve_primes` | 15/15 | 100.00% |
| `ExtendedEval/so_pascal_triangle` | `pascal_triangle` | 15/15 | 100.00% |
| `ExtendedEval/dict_3` | `merge_sum` | 15/15 | 100.00% |
| `ExtendedEval/157` | `right_angle_triangle` | 15/15 | 100.00% |
| `ExtendedEval/bitwise_4` | `count_bits` | 15/15 | 100.00% |

## Parsing, formats & validation (28 tasks)

| Rank | Model | Correct | Accuracy |
|---:|---|---:|---:|
| 1 | Claude Opus 4.8 | 27/28 | 96.43% |
| 2 | DeepSeek V4 Flash | 27/28 | 96.43% |
| 3 | GPT-5.6 Luna | 27/28 | 96.43% |
| 4 | GPT-5.6 Terra | 27/28 | 96.43% |
| 5 | Qwen 3.7 Max | 27/28 | 96.43% |
| 6 | GLM 5.2 | 26/28 | 92.86% |
| 7 | Kimi K2.6 | 26/28 | 92.86% |
| 8 | Kimi K3 | 26/28 | 92.86% |
| 9 | MiniMax M3 | 26/28 | 92.86% |
| 10 | Qwen 3.7 Plus | 26/28 | 92.86% |
| 11 | Claude Sonnet 5 | 25/28 | 89.29% |
| 12 | DeepSeek V4 Pro | 25/28 | 89.29% |
| 13 | MiMo v2.5 Pro | 25/28 | 89.29% |
| 14 | Gemini 3.5 Flash | 24/28 | 85.71% |
| 15 | GPT-5.6 Sol | 24/28 | 85.71% |

**Most difficult tasks**

| Task ID | Entry point | Models passing | Pass rate |
|---|---|---:|---:|
| `ExtendedEval/gh_parse_github_slug` | `parse_github_url` | 1/15 | 6.67% |
| `ExtendedEval/gh_json_minify` | `json_minify` | 6/15 | 40.00% |
| `ExtendedEval/so_split_csv` | `split_csv` | 12/15 | 80.00% |
| `ExtendedEval/6` | `parse_nested_parens` | 14/15 | 93.33% |
| `ExtendedEval/38` | `decode_cyclic` | 14/15 | 93.33% |

**Most consistently solved tasks**

| Task ID | Entry point | Models passing | Pass rate |
|---|---|---:|---:|
| `ExtendedEval/169` | `valid_parentheses_stack` | 15/15 | 100.00% |
| `ExtendedEval/164_variant2` | `is_valid_ipv4` | 15/15 | 100.00% |
| `ExtendedEval/164` | `is_valid_ipv4` | 15/15 | 100.00% |
| `ExtendedEval/gh_changelog_latest` | `latest_changelog_version` | 15/15 | 100.00% |
| `ExtendedEval/gh_license_detect_simple` | `detect_license` | 15/15 | 100.00% |

## Text & strings (38 tasks)

| Rank | Model | Correct | Accuracy |
|---:|---|---:|---:|
| 1 | Claude Opus 4.8 | 32/38 | 84.21% |
| 2 | GLM 5.2 | 32/38 | 84.21% |
| 3 | Kimi K3 | 32/38 | 84.21% |
| 4 | Claude Sonnet 5 | 31/38 | 81.58% |
| 5 | GPT-5.6 Luna | 31/38 | 81.58% |
| 6 | GPT-5.6 Sol | 31/38 | 81.58% |
| 7 | Kimi K2.6 | 31/38 | 81.58% |
| 8 | DeepSeek V4 Pro | 30/38 | 78.95% |
| 9 | Gemini 3.5 Flash | 30/38 | 78.95% |
| 10 | MiMo v2.5 Pro | 30/38 | 78.95% |
| 11 | MiniMax M3 | 30/38 | 78.95% |
| 12 | Qwen 3.7 Max | 30/38 | 78.95% |
| 13 | Qwen 3.7 Plus | 30/38 | 78.95% |
| 14 | GPT-5.6 Terra | 29/38 | 76.32% |
| 15 | DeepSeek V4 Flash | 27/38 | 71.05% |

**Most difficult tasks**

| Task ID | Entry point | Models passing | Pass rate |
|---|---|---:|---:|
| `ExtendedEval/7_regex` | `filter_by_pattern` | 0/15 | 0.00% |
| `ExtendedEval/14` | `all_prefixes` | 0/15 | 0.00% |
| `ExtendedEval/15` | `string_sequence` | 0/15 | 0.00% |
| `ExtendedEval/1_variant2` | `separate_paren_groups` | 1/15 | 6.67% |
| `ExtendedEval/so_word_wrap` | `word_wrap` | 1/15 | 6.67% |

**Most consistently solved tasks**

| Task ID | Entry point | Models passing | Pass rate |
|---|---|---:|---:|
| `ExtendedEval/dict_1` | `char_count` | 15/15 | 100.00% |
| `ExtendedEval/154` | `cycpattern_check` | 15/15 | 100.00% |
| `ExtendedEval/143` | `words_in_sentence` | 15/15 | 100.00% |
| `ExtendedEval/125` | `split_words` | 15/15 | 100.00% |
| `ExtendedEval/119` | `match_parens` | 15/15 | 100.00% |

## Cross-category interpretation

- Algorithms and data structures have the highest mean accuracy (93.94%), while parsing, formats, and validation follow at 92.38%.
- Algorithms have the largest best-to-worst observed spread (15.15 percentage points), followed by text/strings (13.16), numeric/mathematical (13.04), and parsing/validation (10.72).
- Collections/sequence logic has the narrowest observed spread (7.69 percentage points), so it is comparatively less discriminative across these models.
- Text/string tasks have the lowest mean accuracy (80.00%) and are the clearest common weakness.
- Numeric tasks average 85.70%; Kimi K3 has the highest observed numeric score, so the category does not support attributing the advantage to the GPT-5.6 family.

The category results should be reported together with the overall score: the benchmark is heterogeneous, and a single aggregate accuracy hides meaningful differences in failure profiles.
