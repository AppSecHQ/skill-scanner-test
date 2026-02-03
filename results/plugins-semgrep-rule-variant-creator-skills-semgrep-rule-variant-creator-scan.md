# Agent Skill Security Scan Report

**Skill:** semgrep-rule-variant-creator
**Directory:** ./skills/trailofbits-skills/plugins/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.41s
**Timestamp:** 2026-02-03T14:15:36.798933

## Summary

- **Total Findings:** 2
- **Critical:** 1
- **High:** 0
- **Medium:** 0
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:164

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: Dump AST | `semgrep --dump-ast -l <lang> <file

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
