# Agent Skill Security Scan Report

**Skill:** home-assistant
**Directory:** ./skills/clawhub-home-assistant
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.35s
**Timestamp:** 2026-02-03T15:55:05.237992

## Summary

- **Total Findings:** 6
- **Critical:** 2
- **High:** 0
- **Medium:** 3
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:21

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export HA_TOKEN="your-long-lived-access-token

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/ha.sh:82

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: <script_name>

### MEDIUM Severity

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:61

**Description:** Detects skills that delegate trust to untrusted external content: Run Scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** scripts/ha.sh:81

**Description:** Detects skills that delegate trust to untrusted external content: Run script

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** scripts/ha.sh:154

**Description:** Detects skills that delegate trust to untrusted external content: Run script

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
