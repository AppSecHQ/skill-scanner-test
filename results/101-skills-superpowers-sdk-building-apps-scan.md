# Scan: building-inferencesh-apps

- **Verdict:** ISSUES FOUND
- **Max severity:** HIGH
- **Findings:** 8
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:35:34.700351+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| INFO | policy_violation | Skill does not specify a license | SKILL.md |
| HIGH | data_exfiltration | Dangerous data flow in command pipeline | SKILL.md:1 |
| MEDIUM | command_injection | Network-derived content reaches code execution | SKILL.md:24 |
| LOW | data_exfiltration | Dangerous data flow in command pipeline | references/cli.md:1 |
| HIGH | data_exfiltration | Dangerous data flow in command pipeline | references/cli.md:2 |
| LOW | data_exfiltration | Dangerous data flow in command pipeline | references/cli.md:2 |
| LOW | data_exfiltration | Dangerous data flow in command pipeline | references/cli.md:6 |
| MEDIUM | command_injection | Remote fetch followed by execution | references/cli.md:8 |
