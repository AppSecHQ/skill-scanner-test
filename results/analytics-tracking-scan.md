# Agent Skill Security Scan Report

**Skill:** analytics-tracking
**Directory:** ./skills/coreyhaines31-marketingskills/skills/analytics-tracking
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 26.34s
**Timestamp:** 2026-02-01T11:52:57.562796

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Path Traversal Attempts to Access External Files

**Severity:** MEDIUM
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The skill references multiple files using path traversal patterns (../../tools/integrations/*.md and ../../tools/REGISTRY.md). While these references are currently blocked by the system, the skill's design attempts to access files outside its package boundary. This represents an indirect prompt injection risk where the skill could follow instructions or consume data from external, untrusted sources if the path traversal protection were bypassed.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
