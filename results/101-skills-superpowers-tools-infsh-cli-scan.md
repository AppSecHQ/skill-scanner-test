# Scan: infsh-cli

- **Verdict:** ISSUES FOUND
- **Max severity:** HIGH
- **Findings:** 5
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:35:34.050589+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| INFO | policy_violation | Skill does not specify a license | SKILL.md |
| HIGH | data_exfiltration | Dangerous data flow in command pipeline | SKILL.md:1 |
| MEDIUM | command_injection | Network-derived content reaches code execution | SKILL.md:18 |
| LOW | data_exfiltration | Dangerous data flow in command pipeline | references/authentication.md:1 |
| LOW | data_exfiltration | Dangerous data flow in command pipeline | references/cli-reference.md:1 |
