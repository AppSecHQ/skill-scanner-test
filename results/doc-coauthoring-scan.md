# Agent Skill Security Scan Report

**Skill:** doc-coauthoring
**Directory:** /workspace/skills/clawhub-doc-coauthoring
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 20.90s
**Timestamp:** 2026-02-06T00:21:31.224319

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Transitive Trust Abuse via External Shared Documents

**Severity:** MEDIUM
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The skill instructs the agent to fetch and follow content from external shared documents provided by users (e.g., 'use the appropriate integration to fetch it', 'read the current state'). This creates a transitive trust vulnerability where the agent will trust and follow instructions embedded in user-provided external documents without validation. An attacker could provide a malicious shared document containing prompt injection instructions that the agent would then execute.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
