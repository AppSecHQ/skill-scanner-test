# Agent Skill Security Scan Report

**Skill:** smtp-send
**Directory:** ./skills/clawhub-smtp-send
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 0.80s
**Timestamp:** 2026-02-03T16:09:10.956875

## Summary

- **Total Findings:** 4
- **Critical:** 0
- **High:** 1
- **Medium:** 2
- **Low:** 1
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Accessing sensitive system or credential files

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_SENSITIVE_FILES
**Location:** scripts/send_email.py:93

**Description:** Pattern detected: open(filepath

### MEDIUM Severity

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/send_email.py:45

**Description:** Pattern detected: os.getenv('SMTP_PASSWORD

#### [MEDIUM] Environment variable harvesting detected

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_HARVESTING
**Location:** skills/clawhub-smtp-send/scripts/send_email.py

**Description:** Script iterates through environment variables in skills/clawhub-smtp-send/scripts/send_email.py

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
