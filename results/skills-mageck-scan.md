# Scan: mageck

- **Verdict:** SAFE
- **Max severity:** MEDIUM
- **Findings:** 3
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-21T21:37:53.344837+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| MEDIUM | command_injection | Remote fetch followed by execution | references/runtime.md:14 |
| LOW | supply_chain_attack | Archive extraction followed by execution | references/runtime.md:15 |
| MEDIUM | command_injection | Glob or find pattern targeting hidden (dot) files, which may expose sensitive configurations | scripts/screen_analysis.py:214 |
