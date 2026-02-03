# Agent Skill Security Scan Report

**Skill:** tinyfish
**Directory:** ./skills/clawhub-tinyfish-web-agent
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 0.49s
**Timestamp:** 2026-02-03T16:19:30.149886

## Summary

- **Total Findings:** 6
- **Critical:** 0
- **High:** 1
- **Medium:** 4
- **Low:** 1
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Suspicious URL detected: https://mino.ai/v1/automation/run-sse

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-tinyfish-web-agent/scripts/extract.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

### MEDIUM Severity

#### [MEDIUM] HTTP client library imports that enable external communication

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_NETWORK_REQUESTS
**Location:** scripts/extract.py:19

**Description:** Pattern detected: import urllib.request

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/extract.py:25

**Description:** Pattern detected: os.environ.get("MINO_API_KEY

#### [MEDIUM] Undeclared network usage

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_UNDECLARED_NETWORK

**Description:** Skill code uses network libraries but doesn't declare network requirement

#### [MEDIUM] Environment variable harvesting detected

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_HARVESTING
**Location:** skills/clawhub-tinyfish-web-agent/scripts/extract.py

**Description:** Script iterates through environment variables in skills/clawhub-tinyfish-web-agent/scripts/extract.py

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
