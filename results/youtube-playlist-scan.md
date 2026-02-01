# Agent Skill Security Scan Report

**Skill:** youtube-playlist
**Directory:** ./skills/clawhub-youtube-playlist
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 26.45s
**Timestamp:** 2026-02-01T08:48:52.518196

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Hardcoded API Key Requirement Without Secure Storage Guidance

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires users to store the TRANSCRIPT_API_KEY in ~/.zshenv using echo and export commands. This approach stores the API key in plaintext in a shell configuration file, which is a security risk. If the user's system is compromised, the API key is easily accessible. The skill should recommend more secure credential storage methods (e.g., encrypted credential managers, environment variable managers with encryption).

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
