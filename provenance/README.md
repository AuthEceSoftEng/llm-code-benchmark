# Provenance

`humaneval_extendedeval_mapping.csv` is the verified HumanEval-to-ExtendedEval
provenance manifest. It contains all 164 HumanEval tasks: 147 verified
one-to-one inherited mappings and 17 rows explicitly marked
`not_present_in_extended_dataset`. The absent-task rows include an explicit
`release_exclusion_reason`; where the construction record supplied no reason,
the field says so rather than inferring one from entry-point similarity.

Entry-point names are not used as proof of identity. The manifest is the only
mapping used by the paired analysis.
