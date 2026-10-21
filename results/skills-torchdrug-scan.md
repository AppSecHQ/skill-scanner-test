# Scan: torchdrug

- **Verdict:** ISSUES FOUND
- **Max severity:** HIGH
- **Findings:** 4
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-21T21:36:34.275321+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| HIGH | command_injection | Python code block uses eval/exec | references/molecular_generation.md:74 |
| HIGH | command_injection | Python code block uses eval/exec | references/molecular_generation.md:201 |
| HIGH | command_injection | Python code block uses eval/exec | references/molecular_property_prediction.md:118 |
| HIGH | command_injection | Python code block uses eval/exec | references/retrosynthesis.md:193 |
