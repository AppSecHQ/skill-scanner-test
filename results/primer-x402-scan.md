# Agent Skill Security Scan Report

**Skill:** primer-x402
**Directory:** /workspace/skills/clawhub-primer-x402
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.23s
**Timestamp:** 2026-02-06T07:34:54.573453

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 1
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
