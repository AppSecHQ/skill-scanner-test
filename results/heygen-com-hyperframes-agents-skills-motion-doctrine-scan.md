# Scan: motion-doctrine

- **Verdict:** ISSUES FOUND
- **Max severity:** CRITICAL
- **Findings:** 4
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:36:23.534844+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| INFO | policy_violation | Skill does not specify a license | SKILL.md |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/seam-gate.mjs:14 |
| MEDIUM | data_exfiltration | Outbound network request primitives in JavaScript/TypeScript | scripts/seam-gate.mjs:59 |
| MEDIUM | data_exfiltration | Outbound network request primitives in JavaScript/TypeScript | scripts/seam-gate.mjs:122 |
