# Agent Skill Security Scan Report

**Skill:** agent-money-tracker
**Directory:** ./skills/clawhub-intelligent-budget-tracker
**Status:** [OK] SAFE
**Max Severity:** LOW
**Scan Duration:** 0.32s
**Timestamp:** 2026-02-03T16:10:29.021146

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 0
- **Medium:** 0
- **Low:** 1
- **Info:** 0

## Findings

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
