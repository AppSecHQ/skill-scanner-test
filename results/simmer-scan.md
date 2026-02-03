# Agent Skill Security Scan Report

**Skill:** simmer
**Directory:** ./skills/clawhub-simmer
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.68s
**Timestamp:** 2026-02-03T16:12:47.519531

## Summary

- **Total Findings:** 4
- **Critical:** 2
- **High:** 0
- **Medium:** 1
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:78

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl https://api.simmer.markets/api/sdk/agents/me

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:180

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl https://api.simmer.markets/api/sdk/markets

### MEDIUM Severity

#### [MEDIUM] SKILL DISCOVERY ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** skill_discovery_abuse
**Rule ID:** YARA_skill_discovery_abuse
**Location:** SKILL.md:341

**Description:** Detects manipulation of skill discovery to increase unwanted activation: Use this before

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
