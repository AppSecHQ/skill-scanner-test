# Scan: finetuning

- **Verdict:** ISSUES FOUND
- **Max severity:** CRITICAL
- **Findings:** 11
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:36:04.102937+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| CRITICAL | data_exfiltration | Cross-file env var exfiltration: 11 files |  |
| CRITICAL | data_exfiltration | Cross-file exfiltration chain: 11 files |  |
| CRITICAL | data_exfiltration | Environment variable access with network calls detected | /Users/brianlevine/claude-projects/skill-scanner-test/skills/microsoft-azure-skills/skills/microsoft-foundry/finetuning/scripts/common.py |
| CRITICAL | data_exfiltration | Environment variable access with network calls detected | /Users/brianlevine/claude-projects/skill-scanner-test/skills/microsoft-azure-skills/skills/microsoft-foundry/finetuning/scripts/submit_training.py |
| MEDIUM | unauthorized_tool_use | Undeclared network usage | SKILL.md |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | scripts/calibrate_grader.py:54 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/deploy_model.py:120 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/deploy_model.py:141 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/deploy_model.py:167 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/deploy_model.py:178 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/submit_training.py:84 |
