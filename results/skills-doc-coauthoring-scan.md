# Agent Skill Security Scan Report

**Skill:** doc-coauthoring
**Directory:** ./skills/anthropics-skills/skills/doc-coauthoring
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 26.72s
**Timestamp:** 2026-02-01T21:58:09.197834

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Transitive Trust Abuse - Following External Shared Document Content

**Severity:** MEDIUM
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The skill instructs the agent to fetch and follow content from external shared documents (e.g., Google Docs, Notion) provided by users via links. The instruction 'If they provide a link to a shared document, use the appropriate integration to fetch it' creates a transitive trust vulnerability where the agent will trust and follow instructions embedded in external documents without validation. An attacker could provide a malicious shared document containing prompt injection attacks that the agent would then execute.

#### [MEDIUM] Unauthorized Tool Use - Integration Access Without Restrictions

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill uses 'appropriate integration' to fetch external shared documents and read their contents without declaring required tools in the allowed-tools field. While allowed-tools is optional, the skill's behavior of accessing external integrations (Google Docs, Notion, etc.) and reading arbitrary external content represents significant capability that should be explicitly declared for transparency and user awareness.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
