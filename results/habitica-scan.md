# Agent Skill Security Scan Report

**Skill:** habitica
**Directory:** /workspace/skills/clawhub-habitica-skill
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 30.02s
**Timestamp:** 2026-02-06T02:52:52.572087

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Hardcoded Credential File Path Without Validation

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** scripts/habitica.sh

**Description:** The skill reads credentials from ~/.habitica without validating file permissions or checking for secure storage. While reading credentials is necessary for API authentication, the implementation lacks security best practices such as permission checks (should be 0600) or warnings about insecure storage. This could expose credentials if file permissions are misconfigured.

### LOW Severity

#### [LOW] Missing Rate Limiting Implementation

**Severity:** LOW
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** scripts/habitica.sh

**Description:** The SKILL.md documentation mentions 'Rate limit: 30s between automated calls' but the bash script does not implement any rate limiting mechanism. If an agent or user makes rapid successive calls, this could trigger Habitica API rate limits, cause service disruption, or result in API access being temporarily blocked.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
