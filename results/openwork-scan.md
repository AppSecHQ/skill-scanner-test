# Agent Skill Security Scan Report

**Skill:** openwork
**Directory:** ./skills/clawhub-openwork
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.41s
**Timestamp:** 2026-02-03T16:14:26.655725

## Summary

- **Total Findings:** 5
- **Critical:** 4
- **High:** 0
- **Medium:** 0
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:103

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl https://www.openwork.bot/api/onboarding

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:149

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl https://www.openwork.bot/api/jobs/JOB_ID/submissions

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:220

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl https://www.openwork.bot/api/agents/me

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:264

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl https://www.openwork.bot/api/jobs/JOB_ID/submissions

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
