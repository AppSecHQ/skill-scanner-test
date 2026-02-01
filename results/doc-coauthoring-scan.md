# Agent Skill Security Scan Report

**Skill:** doc-coauthoring
**Directory:** ./skills/anthropics-skills/skills/doc-coauthoring
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 27.94s
**Timestamp:** 2026-02-01T12:04:57.349441

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Transitive Trust Abuse via External Shared Documents

**Severity:** MEDIUM
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The skill instructs the agent to fetch and trust content from external shared documents provided by users via links. When users provide links to shared documents (e.g., Google Docs, Notion), the skill directs the agent to 'use the appropriate integration to fetch it' and then follow any templates or formats found in those documents. This creates a transitive trust vulnerability where malicious instructions embedded in external documents could be executed by the agent. An attacker could share a document containing prompt injection attacks that would be followed when the agent reads the document.

#### [MEDIUM] Transitive Trust via Existing Shared Document Editing

**Severity:** MEDIUM
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The skill instructs the agent to read and potentially modify existing shared documents when users mention editing them. The instruction 'If user mentions editing an existing shared document: Use the appropriate integration to read the current state' creates a pathway for indirect prompt injection if the existing document contains malicious instructions. An attacker could pre-populate a shared document with prompt injection attacks, then have a victim user ask the agent to edit that document, causing the agent to follow the malicious instructions.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
