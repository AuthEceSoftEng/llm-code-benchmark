# Recomputed HumanEval–ExtendedEval paired results

Authority: `final_evaluations_v2_release`; 147 verified pairs; 15 models.

Direction: ExtendedEval minus HumanEval. Bootstrap: 2,000 task-level resamples, seed 7.

| Model | HumanEval | ExtendedEval | E-H | H pass/E fail | H fail/E pass | Discordant | Raw p | Holm p | Bootstrap CI |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| moonshotai/kimi-k3 | 97.28% | 91.84% | -5.44% | 12 | 4 | 16 | 0.0768127 | 0.153625 | [-10.88%, 0.00%] |
| anthropic/claude-opus-4.8 | 97.28% | 89.80% | -7.48% | 14 | 3 | 17 | 0.0127258 | 0.0561318 | [-12.93%, -2.72%] |
| google/gemini-3.5-flash | 97.28% | 87.76% | -9.52% | 18 | 4 | 22 | 0.00434351 | 0.0304046 | [-15.65%, -3.40%] |
| openai/gpt-5.6-terra | 92.52% | 87.76% | -4.76% | 15 | 8 | 23 | 0.21004 | 0.21004 | [-11.56%, 1.36%] |
| moonshotai/kimi-k2.6 | 97.28% | 87.07% | -10.20% | 18 | 3 | 21 | 0.00148964 | 0.016386 | [-16.33%, -4.76%] |
| minimax/minimax-m3 | 95.92% | 87.07% | -8.84% | 18 | 5 | 23 | 0.010622 | 0.0561318 | [-14.97%, -2.72%] |
| openai/gpt-5.6-luna | 94.56% | 86.39% | -8.16% | 19 | 7 | 26 | 0.0289593 | 0.0868778 | [-14.97%, -1.36%] |
| qwen/qwen3.7-plus | 97.96% | 86.39% | -11.56% | 20 | 3 | 23 | 0.000488281 | 0.00634766 | [-18.37%, -5.44%] |
| z-ai/glm-5.2 | 95.24% | 85.71% | -9.52% | 20 | 6 | 26 | 0.00935531 | 0.0561318 | [-16.33%, -3.40%] |
| anthropic/claude-sonnet-5 | 98.64% | 85.03% | -13.61% | 21 | 1 | 22 | 1.09673e-05 | 0.000164509 | [-19.73%, -8.16%] |
| openai/gpt-5.6-sol | 95.24% | 85.03% | -10.20% | 19 | 4 | 23 | 0.00259948 | 0.0259948 | [-16.33%, -4.08%] |
| qwen/qwen3.7-max | 97.96% | 85.03% | -12.93% | 22 | 3 | 25 | 0.000156522 | 0.00219131 | [-19.73%, -6.80%] |
| deepseek/deepseek-v4-pro | 96.60% | 83.67% | -12.93% | 24 | 5 | 29 | 0.000546113 | 0.00655335 | [-20.41%, -6.12%] |
| xiaomi/mimo-v2.5-pro | 94.56% | 82.99% | -11.56% | 24 | 7 | 31 | 0.00332689 | 0.029942 | [-19.05%, -4.08%] |
| deepseek/deepseek-v4-flash | 93.20% | 81.63% | -11.56% | 24 | 7 | 31 | 0.00332689 | 0.029942 | [-19.05%, -4.76%] |

Spearman correlation: 0.210912.
Kendall tau-b: 0.164122.

The previous paired aggregate used the provisional matrix and is not used here.
