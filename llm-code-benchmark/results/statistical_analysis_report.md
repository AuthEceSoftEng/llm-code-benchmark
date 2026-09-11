# Statistical analysis of the final benchmark results

The primary metric is empirical pass@1: one completion per task, counted as correct only when every test passes. Wilson intervals are 95% confidence intervals for the binomial proportion. Pairwise tests use exact McNemar tests on paired task outcomes. Holm correction is applied separately to the 105 pairwise comparisons within each dataset. Paired bootstrap intervals use 2,000 task-level resamples, random seed 7, percentile 95% intervals, and estimate accuracy(Model A) minus accuracy(Model B).

## ExtendedEval

Tasks: 246; models: 15

| Model | Correct | Accuracy | 95% Wilson CI |
|---|---:|---:|---:|
| Kimi K3 | 226/246 | 91.87% | [87.78%, 94.68%] |
| Claude Opus 4.8 | 224/246 | 91.06% | [86.83%, 94.02%] |
| GPT-5.6 Terra | 218/246 | 88.62% | [84.04%, 92.01%] |
| GPT-5.6 Luna | 217/246 | 88.21% | [83.58%, 91.67%] |
| Kimi K2.6 | 217/246 | 88.21% | [83.58%, 91.67%] |
| Gemini 3.5 Flash | 216/246 | 87.80% | [83.12%, 91.32%] |
| Qwen 3.7 Max | 216/246 | 87.80% | [83.12%, 91.32%] |
| Claude Sonnet 5 | 215/246 | 87.40% | [82.67%, 90.98%] |
| GLM 5.2 | 214/246 | 86.99% | [82.21%, 90.63%] |
| GPT-5.6 Sol | 214/246 | 86.99% | [82.21%, 90.63%] |
| Qwen 3.7 Plus | 214/246 | 86.99% | [82.21%, 90.63%] |
| DeepSeek V4 Pro | 210/246 | 85.37% | [80.41%, 89.24%] |
| MiniMax M3 | 210/246 | 85.37% | [80.41%, 89.24%] |
| MiMo v2.5 Pro | 208/246 | 84.55% | [79.51%, 88.53%] |
| DeepSeek V4 Flash | 205/246 | 83.33% | [78.17%, 87.47%] |

### Hardest tasks

| Models passing | Task |
|---:|---|
| 0/15 | `ExtendedEval/7_regex` |
| 0/15 | `ExtendedEval/14` |
| 0/15 | `ExtendedEval/15` |
| 0/15 | `ExtendedEval/21_variant2` |
| 0/15 | `ExtendedEval/81` |
| 0/15 | `ExtendedEval/148` |
| 0/15 | `ExtendedEval/149` |
| 0/15 | `ExtendedEval/recursion_2` |
| 1/15 | `ExtendedEval/1_variant2` |
| 1/15 | `ExtendedEval/20` |

### Error-type counts

| Error type | Count |
|---|---:|
| assertion/test failure | 426 |
| syntax error | 39 |
| timeout | 1 |

### Pairwise significance

2 pairwise comparisons remain significant after Holm correction at alpha=0.05.

| Model A | Model B | Holm-adjusted p | Bootstrap difference CI |
|---|---|---:|---:|
| DeepSeek V4 Flash | Kimi K3 | 0.0052 | [-12.60%, -4.47%] |
| Kimi K3 | MiMo v2.5 Pro | 0.0126 | [3.66%, 10.98%] |
## AppliedEval

Tasks: 57; models: 15

| Model | Correct | Accuracy | 95% Wilson CI |
|---|---:|---:|---:|
| DeepSeek V4 Pro | 53/57 | 92.98% | [83.30%, 97.24%] |
| GPT-5.6 Luna | 53/57 | 92.98% | [83.30%, 97.24%] |
| DeepSeek V4 Flash | 52/57 | 91.23% | [81.06%, 96.19%] |
| Gemini 3.5 Flash | 52/57 | 91.23% | [81.06%, 96.19%] |
| Kimi K2.6 | 52/57 | 91.23% | [81.06%, 96.19%] |
| GPT-5.6 Sol | 52/57 | 91.23% | [81.06%, 96.19%] |
| Claude Opus 4.8 | 51/57 | 89.47% | [78.88%, 95.09%] |
| Claude Sonnet 5 | 51/57 | 89.47% | [78.88%, 95.09%] |
| Kimi K3 | 51/57 | 89.47% | [78.88%, 95.09%] |
| Qwen 3.7 Max | 51/57 | 89.47% | [78.88%, 95.09%] |
| GPT-5.6 Terra | 50/57 | 87.72% | [76.75%, 93.92%] |
| Qwen 3.7 Plus | 50/57 | 87.72% | [76.75%, 93.92%] |
| MiMo v2.5 Pro | 49/57 | 85.96% | [74.68%, 92.71%] |
| GLM 5.2 | 49/57 | 85.96% | [74.68%, 92.71%] |
| MiniMax M3 | 47/57 | 82.46% | [70.63%, 90.18%] |

### Hardest tasks

| Models passing | Task |
|---:|---|
| 0/15 | `custom_rank_projects_by_score` |
| 0/15 | `se_filter_map_validate_nested` |
| 2/15 | `custom_pretty_print_matrix` |
| 5/15 | `custom_format_duration` |
| 8/15 | `custom_summarize_category_totals` |
| 8/15 | `str_clean_and_split_sentences` |
| 9/15 | `custom_rotate_matrix` |
| 11/15 | `custom_max_repeated_substring` |
| 12/15 | `custom_resolve_dependencies` |
| 13/15 | `custom_normalize_filename` |

### Error-type counts

| Error type | Count |
|---|---:|
| assertion/test failure | 92 |

### Pairwise significance

0 pairwise comparisons remain significant after Holm correction at alpha=0.05.
The available task counts are small enough that close rankings should be described as ties or near-ties rather than definitive superiority.
