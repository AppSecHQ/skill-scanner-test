# Agent Skill Security Scan Report

**Skill:** clawdbot-self-security-audit
**Directory:** ./skills/clawhub-clawdbot-security-check
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.31s
**Timestamp:** 2026-02-03T15:53:25.972953

## Summary

- **Total Findings:** 7
- **Critical:** 3
- **High:** 2
- **Medium:** 1
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:403

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: exfiltrate credential

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:64

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export CLAWDBOT_GATEWAY_TOKEN

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:403

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: exfiltrate credentials

### HIGH Severity

#### [HIGH] SYSTEM MANIPULATION detected by YARA

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** YARA_system_manipulation
**Location:** SKILL.md:392

**Description:** Detects system manipulation, privilege escalation, and destructive file operations: rm -rf

#### [HIGH] SYSTEM MANIPULATION detected by YARA

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** YARA_system_manipulation
**Location:** SKILL.md:408

**Description:** Detects system manipulation, privilege escalation, and destructive file operations: rm -rf

### MEDIUM Severity

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:311

**Description:** Detects skills that delegate trust to untrusted external content: execute code

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
