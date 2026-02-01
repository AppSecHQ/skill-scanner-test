# Agent Skill Security Scan Report

**Skill:** subtitles
**Directory:** ./skills/clawhub-subtitles
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 19.81s
**Timestamp:** 2026-02-01T08:57:49.033759

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Required API Key Without Security Guidance

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires TRANSCRIPT_API_KEY environment variable but provides no security guidance on key protection, rotation, or scope limitations. Users are instructed to store the key in ~/.zshenv which persists it in plaintext. No warnings about key exposure risks, no mention of read-only vs write scopes, and no guidance on limiting key permissions.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
