# Agent Skill Security Scan Report

**Skill:** preview-markdown
**Directory:** ./skills/clawhub-preview-markdown
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.35s
**Timestamp:** 2026-02-03T16:18:40.607614

## Summary

- **Total Findings:** 8
- **Critical:** 5
- **High:** 0
- **Medium:** 2
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Modifying system permissions or configuration

**Severity:** CRITICAL
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_SYSTEM_MODIFICATION
**Location:** run.sh:185

**Description:** Pattern detected: chmod 644

#### [CRITICAL] Modifying system permissions or configuration

**Severity:** CRITICAL
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_SYSTEM_MODIFICATION
**Location:** lib/browser-utils.sh:32

**Description:** Pattern detected: chmod 700

#### [CRITICAL] Modifying system permissions or configuration

**Severity:** CRITICAL
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_SYSTEM_MODIFICATION
**Location:** lib/html-generator.sh:321

**Description:** Pattern detected: chmod 644

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** run.sh:168

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export HTML_STYLE_FILES=("${STYLE_FILES

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** run.sh:173

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export HTML_OUTPUT="$OUTPUT_FILE

### MEDIUM Severity

#### [MEDIUM] User input used in command substitution - potential injection risk

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_USER_INPUT
**Location:** run.sh:86

**Description:** Pattern detected: $(get_additional_params "$@")

#### [MEDIUM] User input used in command substitution - potential injection risk

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_USER_INPUT
**Location:** run.sh:97

**Description:** Pattern detected: $(get_additional_params "$@")

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
