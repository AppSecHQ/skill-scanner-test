# Agent Skill Security Scan Report

**Skill:** earnings-calendar
**Directory:** ./skills/clawhub-earnings-calendar
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 1.55s
**Timestamp:** 2026-02-03T16:11:03.459291

## Summary

- **Total Findings:** 11
- **Critical:** 3
- **High:** 2
- **Medium:** 5
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Environment variable access with network calls detected

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_EXFILTRATION
**Location:** skills/clawhub-earnings-calendar/scripts/fetch_earnings_fmp.py

**Description:** Script accesses environment variables and makes network calls in skills/clawhub-earnings-calendar/scripts/fetch_earnings_fmp.py

#### [CRITICAL] Cross-file exfiltration chain: 1 files

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_CROSSFILE_EXFILTRATION_CHAIN

**Description:** Multi-file exfiltration chain detected: scripts/fetch_earnings_fmp.py collect data → encode → scripts/fetch_earnings_fmp.py transmit to network

#### [CRITICAL] Cross-file env var exfiltration: 1 files

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_CROSSFILE_ENV_VAR_EXFILTRATION

**Description:** Environment variable access with network calls in scripts/fetch_earnings_fmp.py

### HIGH Severity

#### [HIGH] Accessing sensitive system or credential files

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_SENSITIVE_FILES
**Location:** scripts/generate_report.py:36

**Description:** Pattern detected: open(filepath

#### [HIGH] Suspicious URL detected: https://financialmodelingprep.com/api/v3

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-earnings-calendar/scripts/fetch_earnings_fmp.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

### MEDIUM Severity

#### [MEDIUM] HTTP client library imports that enable external communication

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_NETWORK_REQUESTS
**Location:** scripts/fetch_earnings_fmp.py:23

**Description:** Pattern detected: import requests

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/fetch_earnings_fmp.py:304

**Description:** Pattern detected: os.environ.get('FMP_API_KEY

#### [MEDIUM] Undeclared network usage

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_UNDECLARED_NETWORK

**Description:** Skill code uses network libraries but doesn't declare network requirement

#### [MEDIUM] Potential description-behavior mismatch

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** SOCIAL_ENG_MISLEADING_DESC
**Location:** SKILL.md

**Description:** Skill performs actions not reflected in its description

#### [MEDIUM] Environment variable harvesting detected

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_HARVESTING
**Location:** skills/clawhub-earnings-calendar/scripts/fetch_earnings_fmp.py

**Description:** Script iterates through environment variables in skills/clawhub-earnings-calendar/scripts/fetch_earnings_fmp.py

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
