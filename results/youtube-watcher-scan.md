# Agent Skill Security Scan Report

**Skill:** youtube-watcher
**Directory:** ./skills/clawhub-youtube-watchar
**Status:** [OK] SAFE
**Max Severity:** LOW
**Scan Duration:** 0.59s
**Timestamp:** 2026-02-03T16:02:31.357082

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
