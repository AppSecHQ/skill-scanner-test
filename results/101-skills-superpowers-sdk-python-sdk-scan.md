# Scan: python-sdk

- **Verdict:** ISSUES FOUND
- **Max severity:** HIGH
- **Findings:** 3
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:35:34.627555+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| INFO | policy_violation | Skill does not specify a license | SKILL.md |
| HIGH | command_injection | Python code block uses eval/exec | references/tool-builder.md:254 |
| HIGH | command_injection | Python code block uses eval/exec | references/tool-builder.md:364 |
