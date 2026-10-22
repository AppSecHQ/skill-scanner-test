# Scan: ai-automation-workflows

- **Verdict:** ISSUES FOUND
- **Max severity:** HIGH
- **Findings:** 3
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:35:35.123249+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| INFO | policy_violation | Skill does not specify a license | SKILL.md |
| MEDIUM | command_injection | Python code block executes shell commands | SKILL.md:294 |
| HIGH | command_injection | Active instruction invokes dynamic code or process execution | SKILL.md:301 |
