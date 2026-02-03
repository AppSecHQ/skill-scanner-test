# Agent Skill Security Scan Report

**Skill:** clawhub
**Directory:** ./skills/clawhub-clawhub1
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 0.36s
**Timestamp:** 2026-02-03T16:09:54.059667

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 1
- **Medium:** 0
- **Low:** 1
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] SYSTEM MANIPULATION detected by YARA

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** YARA_system_manipulation
**Location:** SKILL.md:335

**Description:** Detects system manipulation, privilege escalation, and destructive file operations: rm -rf

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
