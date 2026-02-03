# Agent Skill Security Scan Report

**Skill:** send-email
**Directory:** ./skills/clawhub-send-email
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.35s
**Timestamp:** 2026-02-03T16:03:26.915358

## Summary

- **Total Findings:** 4
- **Critical:** 0
- **High:** 0
- **Medium:** 3
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** send_email.py:20

**Description:** Pattern detected: os.getenv("EMAIL_SMTP_PASSWORD

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:34

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: read config files. OpenClaw injects `skills.entries.send-email

#### [MEDIUM] Environment variable harvesting detected

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_HARVESTING
**Location:** skills/clawhub-send-email/send_email.py

**Description:** Script iterates through environment variables in skills/clawhub-send-email/send_email.py

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
