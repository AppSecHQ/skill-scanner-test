# Agent Skill Security Scan Report

**Skill:** google-gemini-media
**Directory:** /workspace/skills/clawhub-google-gemini-media
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 25.48s
**Timestamp:** 2026-02-06T02:40:05.636086

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Hardcoded API Key Environment Variable Without Validation

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires users to store their Gemini API key in the GEMINI_API_KEY environment variable without any guidance on secure storage, validation, or rotation. The instructions explicitly state 'Put your API key in GEMINI_API_KEY' without warnings about credential exposure risks, secure storage practices, or validation mechanisms. This could lead to accidental credential exposure through environment variable leaks, process listings, or logs.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
