# Scan: figma

- **Verdict:** ISSUES FOUND
- **Max severity:** CRITICAL
- **Findings:** 3
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:36:34.571167+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| INFO | policy_violation | Skill does not specify a license | SKILL.md |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/verify-motion.mjs:24 |
| CRITICAL | command_injection | Node.js child_process module usage for shell command execution | scripts/verify-motion.mjs:113 |
