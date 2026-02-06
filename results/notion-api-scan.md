# Agent Skill Security Scan Report

**Skill:** notion
**Directory:** /workspace/skills/clawhub-notion-api-automation
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 22.89s
**Timestamp:** 2026-02-06T05:21:41.330896

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

**Description:** The skill requires NOTION_API_KEY environment variable but provides fallback mechanisms that may encourage insecure storage practices. While checking ~/.config/notion/api_key is mentioned as a 'fallback for local dev', this could lead users to store API keys in plaintext files. The skill does not provide guidance on secure credential management or warn about the risks of plaintext storage.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
