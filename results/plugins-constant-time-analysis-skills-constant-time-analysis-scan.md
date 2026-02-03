# Agent Skill Security Scan Report

**Skill:** constant-time-analysis
**Directory:** ./skills/trailofbits-skills/plugins/constant-time-analysis/skills/constant-time-analysis
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.46s
**Timestamp:** 2026-02-03T14:13:02.345302

## Summary

- **Total Findings:** 5
- **Critical:** 4
- **High:** 0
- **Medium:** 0
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** SKILL.md:1

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: # 

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** SKILL.md:171

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: function (

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:3

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: leak secret

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:3

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: leak secret

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
