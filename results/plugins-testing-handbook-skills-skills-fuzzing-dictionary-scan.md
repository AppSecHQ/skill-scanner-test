# Agent Skill Security Scan Report

**Skill:** fuzzing-dictionary
**Directory:** /workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/fuzzing-dictionary
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.24s
**Timestamp:** 2026-02-06T07:33:46.171254

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
**Location:** SKILL.md:172

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export AFL_LLVM_DICT2FILE

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
