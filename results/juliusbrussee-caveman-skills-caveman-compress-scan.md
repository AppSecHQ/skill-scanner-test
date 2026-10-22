# Scan: caveman-compress

- **Verdict:** ISSUES FOUND
- **Max severity:** HIGH
- **Findings:** 7
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:35:30.390756+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| HIGH | data_exfiltration | Credential file access detected | /Users/brianlevine/claude-projects/skill-scanner-test/skills/juliusbrussee-caveman/skills/caveman-compress/scripts/compress.py |
| MEDIUM | social_engineering | Potential description-behavior mismatch | SKILL.md |
| MEDIUM | unauthorized_tool_use | Undeclared network usage | SKILL.md |
| INFO | policy_violation | Skill does not specify a license | SKILL.md |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/compress.py:679 |
| HIGH | data_exfiltration | Sensitive source reaches a network sink | scripts/compress.py:690 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/compress.py:690 |
