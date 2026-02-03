# Agent Skill Security Scan Report

**Skill:** llm
**Directory:** ./skills/clawhub-llm
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.36s
**Timestamp:** 2026-02-03T16:00:13.958431

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Potential Anthropic brand impersonation

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** SOCIAL_ENG_ANTHROPIC_IMPERSONATION
**Location:** SKILL.md

**Description:** Skill name or description contains 'Anthropic', suggesting official affiliation

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
