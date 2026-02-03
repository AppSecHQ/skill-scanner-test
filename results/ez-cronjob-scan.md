# Agent Skill Security Scan Report

**Skill:** ez-cronjob
**Directory:** ./skills/clawhub-ez-cronjob
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.33s
**Timestamp:** 2026-02-03T16:00:01.342154

## Summary

- **Total Findings:** 3
- **Critical:** 2
- **High:** 0
- **Medium:** 0
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] PROMPT INJECTION detected by YARA

**Severity:** CRITICAL
**Category:** prompt_injection
**Rule ID:** YARA_prompt_injection
**Location:** SKILL.md:12

**Description:** Detects prompt strings used to override or force malicious tool calls: ignore instructions

#### [CRITICAL] PROMPT INJECTION detected by YARA

**Severity:** CRITICAL
**Category:** prompt_injection
**Rule ID:** YARA_prompt_injection
**Location:** SKILL.md:151

**Description:** Detects prompt strings used to override or force malicious tool calls: Ignore Instructions

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
