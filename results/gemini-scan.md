# Agent Skill Security Scan Report

**Skill:** gemini
**Directory:** ./skills/softaworks-agent-toolkit/skills/gemini
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 0.32s
**Timestamp:** 2026-02-02T02:56:31.768748

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 2
- **Medium:** 0
- **Low:** 1
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] SYSTEM MANIPULATION detected by YARA

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** YARA_system_manipulation
**Location:** SKILL.md:30

**Description:** Detects system manipulation, privilege escalation, and destructive file operations: pkill -9

#### [HIGH] SYSTEM MANIPULATION detected by YARA

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** YARA_system_manipulation
**Location:** SKILL.md:189

**Description:** Detects system manipulation, privilege escalation, and destructive file operations: pkill -9

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
