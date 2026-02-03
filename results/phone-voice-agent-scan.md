# Agent Skill Security Scan Report

**Skill:** phone-agent
**Directory:** ./skills/clawhub-phone-agent
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 8.68s
**Timestamp:** 2026-02-03T16:13:48.299075

## Summary

- **Total Findings:** 15
- **Critical:** 4
- **High:** 0
- **Medium:** 10
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Base64 encoding (often used before data exfiltration)

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_BASE64_AND_NETWORK
**Location:** scripts/server.py:502

**Description:** Pattern detected: base64.b64encode

#### [CRITICAL] Base64 encoding (often used before data exfiltration)

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_BASE64_AND_NETWORK
**Location:** scripts/server.py:567

**Description:** Pattern detected: base64.b64encode

#### [CRITICAL] Base64 encoding (often used before data exfiltration)

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_BASE64_AND_NETWORK
**Location:** scripts/server_realtime.py:160

**Description:** Pattern detected: base64.b64encode

#### [CRITICAL] Base64 encoding (often used before data exfiltration)

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_BASE64_AND_NETWORK
**Location:** scripts/server_realtime.py:196

**Description:** Pattern detected: base64.b64encode

### MEDIUM Severity

#### [MEDIUM] HTTP client library imports that enable external communication

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_NETWORK_REQUESTS
**Location:** scripts/server.py:14

**Description:** Pattern detected: import httpx

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/server.py:25

**Description:** Pattern detected: os.getenv("DEEPGRAM_API_KEY

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/server.py:26

**Description:** Pattern detected: os.getenv("OPENAI_API_KEY

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/server.py:27

**Description:** Pattern detected: os.getenv("ELEVENLABS_API_KEY

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/server.py:30

**Description:** Pattern detected: os.getenv("BRAVE_API_KEY

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/server.py:32

**Description:** Pattern detected: os.getenv("TWILIO_AUTH_TOKEN

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/server_realtime.py:24

**Description:** Pattern detected: os.getenv("OPENAI_API_KEY

#### [MEDIUM] Undeclared network usage

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_UNDECLARED_NETWORK

**Description:** Skill code uses network libraries but doesn't declare network requirement

#### [MEDIUM] Environment variable harvesting detected

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_HARVESTING
**Location:** skills/clawhub-phone-agent/scripts/server.py

**Description:** Script iterates through environment variables in skills/clawhub-phone-agent/scripts/server.py

#### [MEDIUM] Environment variable harvesting detected

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_HARVESTING
**Location:** skills/clawhub-phone-agent/scripts/server_realtime.py

**Description:** Script iterates through environment variables in skills/clawhub-phone-agent/scripts/server_realtime.py

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
