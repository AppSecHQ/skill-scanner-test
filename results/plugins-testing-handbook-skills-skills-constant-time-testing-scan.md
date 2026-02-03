# Agent Skill Security Scan Report

**Skill:** constant-time-testing
**Directory:** ./skills/trailofbits-skills/plugins/testing-handbook-skills/skills/constant-time-testing
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.47s
**Timestamp:** 2026-02-03T14:14:34.468329

## Summary

- **Total Findings:** 10
- **Critical:** 8
- **High:** 0
- **Medium:** 1
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:53

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: leak secret

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:192

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: leak   │      ←     │ Track secret

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:499

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: Leak Secret

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:499

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: leak secret

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:53

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: leak secrets

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:192

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: leak   │      ←     │ Track secret

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:499

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: Leak Secrets

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:499

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: leak secret

### MEDIUM Severity

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:162

**Description:** Detects skills that delegate trust to untrusted external content: Execute code

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
