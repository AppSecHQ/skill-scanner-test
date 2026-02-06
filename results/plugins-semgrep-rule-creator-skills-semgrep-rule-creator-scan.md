# Agent Skill Security Scan Report

**Skill:** semgrep-rule-creator
**Directory:** /workspace/skills/trailofbits-skills/plugins/semgrep-rule-creator/skills/semgrep-rule-creator
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 33.02s
**Timestamp:** 2026-02-06T07:15:35.980274

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Transitive Trust Abuse via WebFetch Tool

**Severity:** MEDIUM
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The skill declares 'WebFetch' in allowed-tools and instructs users to 'Fetch external documentation' before writing rules. This creates a transitive trust risk where the agent may follow instructions from untrusted external web content. If external documentation contains malicious instructions (e.g., 'ignore safety guidelines', 'execute this code'), the agent could be indirectly manipulated through content fetched from the web.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
