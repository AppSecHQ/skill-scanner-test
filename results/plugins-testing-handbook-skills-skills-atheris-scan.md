# Agent Skill Security Scan Report

**Skill:** atheris
**Directory:** ./skills/trailofbits-skills/plugins/testing-handbook-skills/skills/atheris
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.38s
**Timestamp:** 2026-02-03T14:15:16.596984

## Summary

- **Total Findings:** 7
- **Critical:** 2
- **High:** 4
- **Medium:** 0
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:78

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: & rm -rf

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:91

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: & rm -rf

### HIGH Severity

#### [HIGH] SYSTEM MANIPULATION detected by YARA

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** YARA_system_manipulation
**Location:** SKILL.md:78

**Description:** Detects system manipulation, privilege escalation, and destructive file operations: rm -rf

#### [HIGH] SYSTEM MANIPULATION detected by YARA

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** YARA_system_manipulation
**Location:** SKILL.md:91

**Description:** Detects system manipulation, privilege escalation, and destructive file operations: rm -rf

#### [HIGH] SYSTEM MANIPULATION detected by YARA

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** YARA_system_manipulation
**Location:** SKILL.md:78

**Description:** Detects system manipulation, privilege escalation, and destructive file operations: rm -rf /

#### [HIGH] SYSTEM MANIPULATION detected by YARA

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** YARA_system_manipulation
**Location:** SKILL.md:91

**Description:** Detects system manipulation, privilege escalation, and destructive file operations: rm -rf /

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
