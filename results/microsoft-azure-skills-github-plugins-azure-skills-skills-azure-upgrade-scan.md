# Scan: azure-upgrade

- **Verdict:** SAFE
- **Max severity:** MEDIUM
- **Findings:** 3
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:35:59.233233+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| MEDIUM | unauthorized_tool_use | Undeclared network usage | SKILL.md |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | references/languages/java/scripts/upgrade_bom.py:82 |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | references/services/functions/consumption-to-flex/windows/automation/deployment-package.md:15 |
