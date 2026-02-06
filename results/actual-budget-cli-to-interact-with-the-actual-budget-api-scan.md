# Agent Skill Security Scan Report

**Skill:** actual-budget
**Directory:** /workspace/skills/clawhub-actual-budget
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 33.81s
**Timestamp:** 2026-02-05T17:55:50.723936

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Hardcoded Credentials in Environment Variables

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION

**Description:** The skill requires sensitive credentials (ACTUAL_PASSWORD, ACTUAL_ENCRYPTION_PASSWORD) to be stored in environment variables. While environment variables are a common practice, the skill documentation does not provide guidance on secure credential management, rotation, or access control. This could lead to credential exposure if environment variables are logged, shared, or accessed by unauthorized processes.

#### [MEDIUM] Network Communication to User-Controlled Server

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION

**Description:** The skill connects to a user-specified server (ACTUAL_SERVER_URL) and transmits authentication credentials over the network. While this is the intended functionality for syncing with Actual Budget servers, there is no validation of the server URL, certificate verification guidance (beyond mentioning NODE_TLS_REJECT_UNAUTHORIZED=0 for self-signed certs), or warnings about man-in-the-middle risks. Users could inadvertently connect to malicious servers.

### LOW Severity

#### [LOW] Missing Security-Critical Metadata

**Severity:** LOW
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill manifest is missing important metadata fields: license, compatibility, and allowed-tools. While allowed-tools is optional, its absence means users cannot verify which agent capabilities this skill requires. The skill performs network operations, file I/O, and credential handling, which should be clearly declared.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
