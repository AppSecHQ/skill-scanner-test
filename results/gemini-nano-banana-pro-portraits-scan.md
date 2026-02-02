# Agent Skill Security Scan Report

**Skill:** gemini-nano-banana-pro-portraits
**Directory:** ./skills/clawhub-gemini-nano-banana-pro-portraits
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.38s
**Timestamp:** 2026-02-02T03:05:14.247956

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] SKILL DISCOVERY ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** skill_discovery_abuse
**Rule ID:** YARA_skill_discovery_abuse
**Location:** SKILL.md:279

**Description:** Detects manipulation of skill discovery to increase unwanted activation: Flawless

#### [MEDIUM] SKILL DISCOVERY ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** skill_discovery_abuse
**Rule ID:** YARA_skill_discovery_abuse
**Location:** SKILL.md:285

**Description:** Detects manipulation of skill discovery to increase unwanted activation: perfect

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
