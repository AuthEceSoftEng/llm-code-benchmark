# ExtendedEval final experimental results

All scores below use the fixed 246-task evaluation set and deterministic execution. A task is correct only when its generated implementation passes the complete executable test suite.

## Overall performance

| Model | Correct | Accuracy |
|---|---:|---:|
| Kimi K3 | 226/246 | 91.87% |
| Claude Opus 4.8 | 224/246 | 91.06% |
| GPT-5.6 Terra | 218/246 | 88.62% |
| GPT-5.6 Luna | 217/246 | 88.21% |
| Kimi K2.6 | 217/246 | 88.21% |
| Gemini 3.5 Flash | 216/246 | 87.80% |
| Qwen 3.7 Max | 216/246 | 87.80% |
| Claude Sonnet 5 | 215/246 | 87.40% |
| GLM 5.2 | 214/246 | 86.99% |
| GPT-5.6 Sol | 214/246 | 86.99% |
| Qwen 3.7 Plus | 214/246 | 86.99% |
| DeepSeek V4 Pro | 210/246 | 85.37% |
| MiniMax M3 | 210/246 | 85.37% |
| MiMo v2.5 Pro | 208/246 | 84.55% |
| DeepSeek V4 Flash | 205/246 | 83.33% |

## Performance by task category

| Model | Algorithms/DS | Collections | Numeric | Parsing/validation | Text/strings |
|---|---:|---:|---:|---:|---:|
| Kimi K3 | 32/33 (97.0%) | 72/78 (92.3%) | 64/69 (92.8%) | 26/28 (92.9%) | 32/38 (84.2%) |
| Claude Opus 4.8 | 32/33 (97.0%) | 71/78 (91.0%) | 62/69 (89.9%) | 27/28 (96.4%) | 32/38 (84.2%) |
| GPT-5.6 Terra | 32/33 (97.0%) | 70/78 (89.7%) | 60/69 (87.0%) | 27/28 (96.4%) | 29/38 (76.3%) |
| GPT-5.6 Luna | 31/33 (93.9%) | 69/78 (88.5%) | 59/69 (85.5%) | 27/28 (96.4%) | 31/38 (81.6%) |
| Kimi K2.6 | 31/33 (93.9%) | 69/78 (88.5%) | 60/69 (87.0%) | 26/28 (92.9%) | 31/38 (81.6%) |
| Gemini 3.5 Flash | 31/33 (93.9%) | 70/78 (89.7%) | 61/69 (88.4%) | 24/28 (85.7%) | 30/38 (78.9%) |
| Qwen 3.7 Max | 33/33 (100.0%) | 67/78 (85.9%) | 59/69 (85.5%) | 27/28 (96.4%) | 30/38 (78.9%) |
| Claude Sonnet 5 | 32/33 (97.0%) | 68/78 (87.2%) | 59/69 (85.5%) | 25/28 (89.3%) | 31/38 (81.6%) |
| GLM 5.2 | 30/33 (90.9%) | 66/78 (84.6%) | 60/69 (87.0%) | 26/28 (92.9%) | 32/38 (84.2%) |
| GPT-5.6 Sol | 32/33 (97.0%) | 67/78 (85.9%) | 60/69 (87.0%) | 24/28 (85.7%) | 31/38 (81.6%) |
| Qwen 3.7 Plus | 30/33 (90.9%) | 69/78 (88.5%) | 59/69 (85.5%) | 26/28 (92.9%) | 30/38 (78.9%) |
| DeepSeek V4 Pro | 30/33 (90.9%) | 68/78 (87.2%) | 57/69 (82.6%) | 25/28 (89.3%) | 30/38 (78.9%) |
| MiniMax M3 | 28/33 (84.8%) | 70/78 (89.7%) | 56/69 (81.2%) | 26/28 (92.9%) | 30/38 (78.9%) |
| MiMo v2.5 Pro | 31/33 (93.9%) | 66/78 (84.6%) | 56/69 (81.2%) | 25/28 (89.3%) | 30/38 (78.9%) |
| DeepSeek V4 Flash | 30/33 (90.9%) | 66/78 (84.6%) | 55/69 (79.7%) | 27/28 (96.4%) | 27/38 (71.1%) |

## Interpretation

The leading ExtendedEval endpoints form a close observed cluster rather than a statistically complete ranking. Kimi K3 obtains the highest observed accuracy at 226/246 tasks (91.87%), followed by Claude Opus 4.8 at 224/246 (91.06%). Only two of the 105 pairwise comparisons remain significant after Holm correction, primarily contrasting the highest-performing endpoints with models lower in the observed ranking.

Algorithms and data structures have the highest mean model accuracy (93.94%), followed by parsing, formats, and validation (92.38%). Collections and sequence logic reach 87.86%, numeric and mathematical tasks 85.70%, and text and string tasks have the lowest mean accuracy (80.00%). Algorithms show the largest best-to-worst observed spread (15.15 percentage points), followed by text/strings (13.16), numeric/mathematical (13.04), and parsing/validation (10.72); collections have the narrowest spread (7.69 points).

Category-level rankings reveal complementary profiles. Qwen 3.7 Max achieves 33/33 on algorithms and data structures, Kimi K3 obtains the highest numeric and collections scores, and Claude Opus 4.8 is among the strongest endpoints in parsing/validation and text processing. These results support reporting category-level performance alongside aggregate empirical pass@1.

The error pattern is primarily semantic: 426 failures are assertion/test failures, 39 are syntax errors, and 1 is a timeout. Most failed submissions are therefore syntactically valid but implement a subtly different interpretation of the specification.
