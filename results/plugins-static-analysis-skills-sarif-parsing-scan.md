# Agent Skill Security Scan Report

**Skill:** sarif-parsing
**Directory:** ./skills/trailofbits-skills/plugins/static-analysis/skills/sarif-parsing
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 1.44s
**Timestamp:** 2026-02-03T14:14:05.733379

## Summary

- **Total Findings:** 4
- **Critical:** 0
- **High:** 3
- **Medium:** 0
- **Low:** 1
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Skill declares no Write tool but bundled scripts write files

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** ALLOWED_TOOLS_WRITE_VIOLATION

**Description:** Skill restricts tools to ['Bash', 'Read', 'Glob', 'Grep'] but bundled scripts appear to write to the filesystem, which conflicts with a read-only tool declaration.

#### [HIGH] Python scripts present but Python tool not in allowed-tools

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** ALLOWED_TOOLS_PYTHON_VIOLATION

**Description:** Skill restricts tools to ['Bash', 'Read', 'Glob', 'Grep'] but includes Python scripts

#### [HIGH] Suspicious URL detected: https://json.schemastore.org/sarif-2.1.0.json

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/trailofbits-skills/plugins/static-analysis/skills/sarif-parsing/resources/sarif_helpers.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
