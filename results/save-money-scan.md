# Agent Skill Security Scan Report

**Skill:** save-money
**Directory:** ./skills/clawhub-save-money
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.44s
**Timestamp:** 2026-02-03T15:59:15.914064

## Summary

- **Total Findings:** 3
- **Critical:** 1
- **High:** 0
- **Medium:** 1
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] PROMPT INJECTION detected by YARA

**Severity:** CRITICAL
**Category:** prompt_injection
**Rule ID:** YARA_prompt_injection
**Location:** SKILL.md:129

**Description:** Detects prompt strings used to override or force malicious tool calls: Do NOT mention

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
