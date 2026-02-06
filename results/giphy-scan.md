# Agent Skill Security Scan Report

**Skill:** giphy-gif
**Directory:** /workspace/skills/clawhub-giphy
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 33.46s
**Timestamp:** 2026-02-06T02:01:31.779039

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 1
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Hardcoded API Key Exposure Risk in Documentation

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill's documentation instructs users to store their Giphy API key in plaintext configuration files (~/.openclaw/openclaw.json) and environment variables. While the skill itself doesn't contain hardcoded secrets, the instructions create a pattern that could lead to credential exposure if the config file has improper permissions or is accidentally committed to version control. The bash commands also echo the API key in process arguments, which may be visible in process listings.

### MEDIUM Severity

#### [MEDIUM] Command Injection Risk via Unvalidated Query Parameter

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill uses bash exec() with user-controlled query strings that are passed through jq for URL encoding. While jq provides some protection via '@uri', the pattern 'QUERY="$query"' in the examples could be vulnerable to command injection if the query variable contains malicious shell metacharacters before being passed to jq. The use of exec() with string interpolation of user input is inherently risky.

#### [MEDIUM] External API Data Exfiltration via User Queries

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md:36

**Description:** The skill sends user search queries to an external third-party API (api.giphy.com) without explicit user consent or privacy warnings. User search terms may contain sensitive information, personal preferences, or contextual data from conversations that gets transmitted to Giphy's servers. This represents potential data leakage of conversation context to external parties.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
