# Agent Skill Security Scan Report

**Skill:** hugging-face-trackio
**Directory:** /workspace/skills/huggingface-skills/skills/hugging-face-trackio
**Status:** [OK] SAFE
**Max Severity:** LOW
**Scan Duration:** 0.35s
**Timestamp:** 2026-02-06T07:48:33.159716

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
