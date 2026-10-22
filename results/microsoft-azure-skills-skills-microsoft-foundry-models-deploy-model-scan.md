# Scan: deploy-model

- **Verdict:** SAFE
- **Max severity:** MEDIUM
- **Findings:** 2
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:36:03.156985+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | preset/references/preset-workflow.md:70 |
| LOW | unauthorized_tool_use | Script contacts a destination the documentation never mentions | scripts/generate_deployment_url.sh:87 |
