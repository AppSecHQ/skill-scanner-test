# Agent Skill Security Scan Report

**Skill:** google-calendar
**Directory:** /workspace/skills/clawhub-google-calendar-api
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 37.06s
**Timestamp:** 2026-02-06T02:34:05.049675

## Summary

- **Total Findings:** 4
- **Critical:** 0
- **High:** 1
- **Medium:** 3
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Hardcoded API Key Exposure Risk in Documentation

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill documentation contains multiple examples showing 'YOUR_API_KEY' placeholder in Authorization headers and instructs users to set MATON_API_KEY as an environment variable. While these are examples, the skill's design requires users to expose their Maton API key in environment variables where it could be accessed by malicious scripts or processes. The skill does not implement any secure credential storage mechanism and relies entirely on environment variable exposure.

### MEDIUM Severity

#### [MEDIUM] Missing Referenced Script File (Google.py)

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill instructions reference a file 'Google.py' that is not included in the skill package. This creates an incomplete skill that cannot function as documented. This could be tool shadowing where a user might create their own Google.py file, potentially with malicious code, to fill the gap. The missing file also indicates poor package integrity.

#### [MEDIUM] Third-Party API Gateway Dependency Not Disclosed in Description

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill description states 'Google Calendar API integration with managed OAuth' but does not disclose that all requests are proxied through a third-party gateway (gateway.maton.ai and ctrl.maton.ai). This is a form of social engineering through omission - users may believe they're connecting directly to Google's API when actually all their calendar data flows through Maton's infrastructure. The description should clearly state this is a proxy service.

#### [MEDIUM] Data Exfiltration Risk via Third-Party Gateway

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** All Google Calendar API requests are proxied through gateway.maton.ai, meaning all calendar data (events, attendees, schedules, meeting details) passes through Maton's infrastructure. This creates a data exfiltration vector where sensitive calendar information is exposed to a third party. Users may not realize their private calendar data is being transmitted through an intermediary service. There is no documentation about Maton's data retention, logging, or privacy policies.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
