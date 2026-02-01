# Agent Skill Security Scan Report

**Skill:** clickup
**Directory:** ~/skill-scanner-test/skills/clawhub-clickup-skill
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.84s
**Timestamp:** 2026-01-31T17:34:57.801814

## Summary

- **Total Findings:** 14
- **Critical:** 3
- **High:** 6
- **Medium:** 4
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:23

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export CLICKUP_API_TOKEN

#### [CRITICAL] Environment variable access with network calls detected

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_EXFILTRATION
**Location:** skills/clawhub-clickup-skill/scripts/clickup_client.py

**Description:** Script accesses environment variables and makes network calls in skills/clawhub-clickup-skill/scripts/clickup_client.py

#### [CRITICAL] Cross-file env var exfiltration: 1 files

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_CROSSFILE_ENV_VAR_EXFILTRATION

**Description:** Environment variable access with network calls in scripts/clickup_client.py

### HIGH Severity

#### [HIGH] Infinite loop without clear exit condition

**Severity:** HIGH
**Category:** resource_abuse
**Rule ID:** RESOURCE_ABUSE_INFINITE_LOOP
**Location:** scripts/clickup_client.py:427

**Description:** Pattern detected: while True:

#### [HIGH] Suspicious URL detected: https://api.clickup.com/api/v3

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-clickup-skill/scripts/clickup_client.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: https://app.clickup.com/

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-clickup-skill/scripts/clickup_client.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: https://app.clickup.com/

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-clickup-skill/scripts/clickup_client.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: https://app.clickup.com/docs/

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-clickup-skill/scripts/clickup_client.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: https://api.clickup.com/api/v2

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-clickup-skill/scripts/clickup_client.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

### MEDIUM Severity

#### [MEDIUM] HTTP client library imports that enable external communication

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_NETWORK_REQUESTS
**Location:** scripts/clickup_client.py:11

**Description:** Pattern detected: import requests

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/clickup_client.py:19

**Description:** Pattern detected: os.getenv("CLICKUP_API_TOKEN

#### [MEDIUM] Undeclared network usage

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_UNDECLARED_NETWORK

**Description:** Skill code uses network libraries but doesn't declare network requirement

#### [MEDIUM] Environment variable harvesting detected

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_HARVESTING
**Location:** skills/clawhub-clickup-skill/scripts/clickup_client.py

**Description:** Script iterates through environment variables in skills/clawhub-clickup-skill/scripts/clickup_client.py

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
- trigger_analyzer
