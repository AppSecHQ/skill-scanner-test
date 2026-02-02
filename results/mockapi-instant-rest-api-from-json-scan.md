# Agent Skill Security Scan Report

**Skill:** MockAPI - Instant REST API from JSON
**Directory:** ./skills/clawhub-mockapi
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.42s
**Timestamp:** 2026-02-02T03:07:32.798621

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 2
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] SKILL DISCOVERY ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** skill_discovery_abuse
**Rule ID:** YARA_skill_discovery_abuse
**Location:** SKILL.md:3

**Description:** Detects manipulation of skill discovery to increase unwanted activation: Perfect

### LOW Severity

#### [LOW] Skill name does not follow agent skills naming rules

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_INVALID_NAME
**Location:** SKILL.md

**Description:** Skill name 'MockAPI - Instant REST API from JSON' is invalid. Agent skills require lowercase letters, numbers, and hyphens only, with a maximum length of 64 characters.

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
