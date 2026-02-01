# Agent Skill Security Scan Report

**Skill:** ez-google
**Directory:** ./skills/clawhub-ez-google
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 27.09s
**Timestamp:** 2026-02-01T17:35:47.300289

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/auth.py:62

**Description:** Pattern detected: os.environ.get("GOOGLE_CLIENT_SECRET

#### [MEDIUM] Hardcoded External OAuth Service URL

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** scripts/auth.py:23

**Description:** The auth.py script contains a hardcoded URL to an external OAuth service (OAUTH_WORKER_URL = 'https://ezagentauth.com'). This creates a dependency on an external service for authentication flow. If this service is compromised, malicious actors could intercept OAuth tokens and gain access to users' Google Workspace data. The skill trusts this external service to handle sensitive OAuth credentials without verification.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
