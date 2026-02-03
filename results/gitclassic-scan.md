# Agent Skill Security Scan Report

**Skill:** gitclassic
**Directory:** ./skills/clawhub-gitclassic
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.35s
**Timestamp:** 2026-02-03T16:14:07.672011

## Summary

- **Total Findings:** 5
- **Critical:** 4
- **High:** 0
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:41

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl https://gitclassic.com/facebook/react

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:44

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl https://gitclassic.com/facebook/react/blob/main/README.md

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:47

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl https://gitclassic.com/facebook/react/tree/main/packages

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:53

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl https://gitclassic.com/torvalds

### MEDIUM Severity

#### [MEDIUM] SKILL DISCOVERY ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** skill_discovery_abuse
**Rule ID:** YARA_skill_discovery_abuse
**Location:** SKILL.md:5

**Description:** Detects manipulation of skill discovery to increase unwanted activation: Perfect

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
