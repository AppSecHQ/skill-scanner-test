# Scan: autoskill

- **Verdict:** ISSUES FOUND
- **Max severity:** CRITICAL
- **Findings:** 11
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-21T21:37:00.126566+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| CRITICAL | data_exfiltration | Cross-file env var exfiltration: 3 files |  |
| CRITICAL | data_exfiltration | Cross-file exfiltration chain: 3 files |  |
| CRITICAL | data_exfiltration | Environment variable access with network calls detected | /home/runner/work/skill-scanner-test/skill-scanner-test/skills/K-Dense-AI-scientific-agent-skills/skills/autoskill/scripts/backends.py |
| CRITICAL | data_exfiltration | Environment variable access with network calls detected | /home/runner/work/skill-scanner-test/skill-scanner-test/skills/K-Dense-AI-scientific-agent-skills/skills/autoskill/scripts/doctor.py |
| CRITICAL | data_exfiltration | Environment variable access with network calls detected | /home/runner/work/skill-scanner-test/skill-scanner-test/skills/K-Dense-AI-scientific-agent-skills/skills/autoskill/scripts/run.py |
| MEDIUM | unauthorized_tool_use | Code makes network requests | SKILL.md |
| LOW | unauthorized_tool_use | Code uses glob/file patterns but Glob tool not in allowed-tools | SKILL.md |
| LOW | unauthorized_tool_use | Code uses search/grep patterns but Grep tool not in allowed-tools | SKILL.md |
| HIGH | data_exfiltration | Sensitive source reaches a network sink | scripts/doctor.py:22 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/doctor.py:22 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/doctor.py:38 |
