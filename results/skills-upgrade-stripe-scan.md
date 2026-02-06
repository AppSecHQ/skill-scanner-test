# Agent Skill Security Scan Report

**Skill:** upgrade-stripe
**Directory:** /workspace/skills/stripe-ai/skills/upgrade-stripe
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.23s
**Timestamp:** 2026-02-06T07:49:02.916659

## Summary

- **Total Findings:** 2
- **Critical:** 1
- **High:** 0
- **Medium:** 0
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:150

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl https://api.stripe.com/v1/customers

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
