# Scan: open-notebook

- **Verdict:** ISSUES FOUND
- **Max severity:** CRITICAL
- **Findings:** 7
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-21T21:37:08.557281+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| CRITICAL | data_exfiltration | Cross-file env var exfiltration: 1 files |  |
| CRITICAL | data_exfiltration | Cross-file exfiltration chain: 1 files |  |
| CRITICAL | data_exfiltration | Environment variable access with network calls detected | /home/runner/work/skill-scanner-test/skill-scanner-test/skills/K-Dense-AI-scientific-agent-skills/skills/open-notebook/scripts/_common.py |
| MEDIUM | social_engineering | Potential description-behavior mismatch | SKILL.md |
| HIGH | data_exfiltration | Sensitive source reaches a network sink | scripts/_common.py:29 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | scripts/_common.py:29 |
| HIGH | resource_abuse | Infinite loop without clear exit condition | scripts/source_ingestion.py:56 |
