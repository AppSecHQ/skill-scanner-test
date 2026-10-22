# Scan: scaffold

- **Verdict:** ISSUES FOUND
- **Max severity:** CRITICAL
- **Findings:** 4
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:36:00.048708+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| MEDIUM | obfuscation | Deeply nested file references detected | SKILL.md |
| LOW | social_engineering | Skill description is too short | SKILL.md |
| INFO | policy_violation | Strict manifest load failed; inert fallback scan used | SKILL.md |
| CRITICAL | command_injection | Discovery and execution chain (find -exec) | scripts/scaffold-conformance.sh:21 |
