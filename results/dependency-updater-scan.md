# Agent Skill Security Scan Report

**Skill:** dependency-updater
**Directory:** ./skills/softaworks-agent-toolkit/skills/dependency-updater
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 0.33s
**Timestamp:** 2026-02-02T02:57:26.171092

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 2
- **Medium:** 0
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] SYSTEM MANIPULATION detected by YARA

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** YARA_system_manipulation
**Location:** SKILL.md:287

**Description:** Detects system manipulation, privilege escalation, and destructive file operations: rm -rf

#### [HIGH] SYSTEM MANIPULATION detected by YARA

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** YARA_system_manipulation
**Location:** SKILL.md:288

**Description:** Detects system manipulation, privilege escalation, and destructive file operations: rm -rf

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
