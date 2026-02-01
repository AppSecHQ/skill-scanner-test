# Agent Skill Security Scan Report

**Skill:** youtube-data
**Directory:** ./skills/clawhub-youtube-data
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 28.67s
**Timestamp:** 2026-02-01T08:43:45.277072

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Hardcoded API Key Exposure Risk in Documentation

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill documentation instructs users to store the TRANSCRIPT_API_KEY in ~/.zshenv using echo commands. This approach can lead to accidental exposure through shell history, process listings, or misconfigured file permissions. Additionally, the documentation shows example API keys in plaintext (sk_...) which could lead to users inadvertently committing real keys if they copy-paste without modification.

#### [MEDIUM] External API Dependency with User Credentials

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires users to provide API credentials (TRANSCRIPT_API_KEY) for a third-party service (transcriptapi.com). While the service appears legitimate, users are instructed to make authenticated requests to an external API with their personal credentials. There is no validation of the API responses, and users must trust the external service with their API keys and the data they query.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
