# Agent Skill Security Scan Report

**Skill:** humanize-ai
**Directory:** /workspace/skills/clawhub-humanize-ai
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 21.02s
**Timestamp:** 2026-02-06T03:05:21.647995

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 1
- **Medium:** 0
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Python scripts present but Python tool not in allowed-tools

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** ALLOWED_TOOLS_PYTHON_VIOLATION

**Description:** Skill restricts tools to ['Read', 'Write', 'StrReplace', 'Shell', 'Glob'] but includes Python scripts

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
