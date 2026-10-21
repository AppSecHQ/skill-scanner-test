# Scan: qiime2-amplicon

- **Verdict:** ISSUES FOUND
- **Max severity:** HIGH
- **Findings:** 1
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-21T21:36:38.283104+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| HIGH | resource_abuse | Infinite loop without clear exit condition | scripts/amplicon_workflow.py:28 |
