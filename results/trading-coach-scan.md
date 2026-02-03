# Agent Skill Security Scan Report

**Skill:** trading-coach
**Directory:** ./skills/clawhub-trading-coach
**Status:** [OK] SAFE
**Max Severity:** LOW
**Scan Duration:** 0.46s
**Timestamp:** 2026-02-03T16:07:17.342174

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 0
- **Low:** 2
- **Info:** 0

## Findings

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

#### [LOW] Skill description is too short

**Severity:** LOW
**Category:** social_engineering
**Rule ID:** TRIGGER_DESCRIPTION_TOO_SHORT
**Location:** SKILL.md

**Description:** Description has only 0 words. Short descriptions may not provide enough context for the agent to determine when this skill should be used.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
