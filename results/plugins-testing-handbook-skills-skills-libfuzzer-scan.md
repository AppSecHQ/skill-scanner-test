# Agent Skill Security Scan Report

**Skill:** libfuzzer
**Directory:** ./skills/trailofbits-skills/plugins/testing-handbook-skills/skills/libfuzzer
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.33s
**Timestamp:** 2026-02-03T14:14:29.192183

## Summary

- **Total Findings:** 4
- **Critical:** 3
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
**Location:** SKILL.md:626

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl -O 

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:632

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl -o 

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:633

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl -O 

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
