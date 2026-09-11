# Final benchmark validation report

## Dataset validation status

### ExtendedEval

- Release file: `ExtendedEval_final.jsonl`
- Records: 246
- Unique task IDs: 246
- Canonical solutions passing the complete validation harness: 246/246
- Repeated deterministic audit: identical result on the second run
- Duplicate records: none in the scored release

### AppliedEval

- Release file: `AppliedEval_cleaned.jsonl`
- Records: 57
- Unique task IDs: 57
- Canonical solutions passing the complete validation harness: 57/57
- Repeated deterministic audit: identical result on the second run
- Duplicate records: none
- Category counts: 22 String, 13 Array/Sequence, 6 Graph/Tree/DP, 8 Bit/Math, 8 System/Validation

## Evaluation status

Stored model completions were re-evaluated against the repaired ExtendedEval tests for the 15-model reporting set after excluding Claude Fable 5. The corrected `words_in_sentence` prompt was rerun once per remaining model; all 15 corrected completions were present and passed the corresponding executable tests.

The final ExtendedEval statistical release is complete. The two missing GLM records were rerun successfully. One corrected GLM completion passes and the other fails the executable tests, so the remaining GLM failure is a genuine model-evaluation outcome rather than a missing-response artifact.

AppliedEval has complete stored completions for all 15 remaining models and is included in the regenerated final statistical reports.

## Repaired task scope

The final ExtendedEval release includes specification-based repairs for the six requested tasks and additional objectively inconsistent expected outputs discovered during complete canonical validation. No new algorithmic requirements were introduced.

## Completion condition

The final matrices and statistical reports were regenerated after the corrected-prompt rerun. The manuscript tables may now be labelled final, subject to the stated statistical methods and model-run protocol.
