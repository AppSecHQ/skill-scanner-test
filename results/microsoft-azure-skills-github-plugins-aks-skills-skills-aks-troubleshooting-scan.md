# Scan: aks-troubleshooting

- **Verdict:** SAFE
- **Max severity:** MEDIUM
- **Findings:** 3
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:35:48.967516+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | references/symptom-map.md:222 |
| LOW | unauthorized_tool_use | Script contacts a destination the documentation never mentions | scripts/pod-deep-dive.sh:25 |
| LOW | unauthorized_tool_use | Script contacts a destination the documentation never mentions | scripts/pod-deep-dive.sh:33 |
