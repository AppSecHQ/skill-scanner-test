# Agent Skill Security Scan Report

**Skill:** spec-to-code-compliance
**Directory:** /workspace/skills/trailofbits-skills/plugins/spec-to-code-compliance/skills/spec-to-code-compliance
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 29.60s
**Timestamp:** 2026-02-06T07:22:26.306377

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Transitive Trust Abuse - Skill Follows Untrusted External Content

**Severity:** MEDIUM
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The skill instructions direct the agent to process and follow content from user-provided specification documents and codebases without validation. The instructions state 'Do NOT rely on prior knowledge of known protocols. Only use provided materials' and 'Never infer unspecified behavior', which creates a transitive trust relationship where the agent will follow instructions embedded in untrusted user-provided documents (whitepapers, design docs, etc.). This could allow indirect prompt injection through malicious specification documents.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
