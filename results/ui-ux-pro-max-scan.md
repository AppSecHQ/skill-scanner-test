# Agent Skill Security Scan Report

**Skill:** ui-ux-pro-max
**Directory:** /workspace/skills/clawhub-ui-ux-pro-max
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 4.35s
**Timestamp:** 2026-02-06T07:52:12.633024

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 2
- **Medium:** 0
- **Low:** 1
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Accessing sensitive system or credential files

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_SENSITIVE_FILES
**Location:** scripts/design_system.py:52

**Description:** Pattern detected: open(filepath

#### [HIGH] Accessing sensitive system or credential files

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_SENSITIVE_FILES
**Location:** scripts/core.py:161

**Description:** Pattern detected: open(filepath

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
