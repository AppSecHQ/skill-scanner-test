# Agent Skill Security Scan Report

**Skill:** agnxi-search
**Directory:** /workspace/skills/clawhub-agnxi-search-skill
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 28.95s
**Timestamp:** 2026-02-05T18:40:18.546935

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Transitive Trust in External XML Content

**Severity:** MEDIUM
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** search.py

**Description:** The skill downloads and parses XML content from an external source (agnxi.com sitemap) without validation. If the external site is compromised or returns malicious XML, the skill could be exploited through XML injection, XXE attacks, or by following malicious URLs embedded in the sitemap. The skill trusts external content implicitly.

#### [MEDIUM] Missing Resource Limits and Error Handling

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** search.py

**Description:** The script lacks timeout controls, size limits on downloaded content, and proper error handling for network operations. This could lead to resource exhaustion if the remote server returns extremely large responses, hangs indefinitely, or causes the script to consume excessive memory/CPU.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
