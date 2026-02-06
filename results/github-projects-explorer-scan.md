# Agent Skill Security Scan Report

**Skill:** explorer
**Directory:** /workspace/skills/clawhub-explorer
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 33.92s
**Timestamp:** 2026-02-06T02:18:03.398684

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Optional GitHub Token Usage Without Security Guidance

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requests users to configure a GITHUB_TOKEN environment variable and provides instructions to add it to ~/.zshrc. While using GitHub tokens is legitimate for API rate limiting, the skill lacks security guidance about token permissions, scope restrictions, or secure storage. Users may inadvertently create tokens with excessive permissions (e.g., repo write access) when only public_repo read access is needed. The skill does not validate token permissions or warn about security implications.

### LOW Severity

#### [LOW] Missing Rate Limiting and Error Handling for API Requests

**Severity:** LOW
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE

**Description:** The Python script makes HTTP requests to GitHub API without implementing retry logic, exponential backoff, or rate limit handling. While the script checks for GITHUB_TOKEN to increase rate limits, it does not handle rate limit exhaustion gracefully. Excessive or rapid queries could lead to API rate limit errors (HTTP 403) without proper user feedback or automatic throttling.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
