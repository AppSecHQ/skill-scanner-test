# Agent Skill Security Scan Report

**Skill:** humanize-ai
**Directory:** ./skills/clawhub-humanize-ai
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 0.97s
**Timestamp:** 2026-02-02T03:06:12.671246

## Summary

- **Total Findings:** 4
- **Critical:** 0
- **High:** 1
- **Medium:** 1
- **Low:** 2
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Python scripts present but Python tool not in allowed-tools

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** ALLOWED_TOOLS_PYTHON_VIOLATION

**Description:** Skill restricts tools to ['Read', 'Write', 'StrReplace', 'Shell', 'Glob'] but includes Python scripts

### MEDIUM Severity

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:16

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): " | python 

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

#### [LOW] Code uses search/grep patterns but Grep tool not in allowed-tools

**Severity:** LOW
**Category:** unauthorized_tool_use
**Rule ID:** ALLOWED_TOOLS_GREP_VIOLATION

**Description:** Skill restricts tools to ['Read', 'Write', 'StrReplace', 'Shell', 'Glob'] but code uses regex search patterns

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
