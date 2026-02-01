# Agent Skill Security Scan Report

**Skill:** captions
**Directory:** ./skills/clawhub-captions
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 26.92s
**Timestamp:** 2026-02-01T09:04:23.093245

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] External API Key Required Without Security Guidance

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires users to store a TRANSCRIPT_API_KEY environment variable but provides no security guidance on key protection, rotation, or scope limitations. The instructions recommend storing the key in ~/.zshenv, which persists the credential in plaintext in the user's shell configuration. While the API itself appears legitimate (TranscriptAPI.com), there is no validation that the key is properly scoped or guidance on least-privilege access.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
