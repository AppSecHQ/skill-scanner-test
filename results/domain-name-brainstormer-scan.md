# Agent Skill Security Scan Report

**Skill:** domain-name-brainstormer
**Directory:** ./skills/softaworks-agent-toolkit/skills/domain-name-brainstormer
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.29s
**Timestamp:** 2026-02-02T02:56:14.394741

## Summary

- **Total Findings:** 4
- **Critical:** 0
- **High:** 0
- **Medium:** 3
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] SKILL DISCOVERY ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** skill_discovery_abuse
**Rule ID:** YARA_skill_discovery_abuse
**Location:** SKILL.md:3

**Description:** Detects manipulation of skill discovery to increase unwanted activation: perfect

#### [MEDIUM] SKILL DISCOVERY ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** skill_discovery_abuse
**Rule ID:** YARA_skill_discovery_abuse
**Location:** SKILL.md:73

**Description:** Detects manipulation of skill discovery to increase unwanted activation: Perfect

#### [MEDIUM] SKILL DISCOVERY ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** skill_discovery_abuse
**Rule ID:** YARA_skill_discovery_abuse
**Location:** SKILL.md:89

**Description:** Detects manipulation of skill discovery to increase unwanted activation: Perfect

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
