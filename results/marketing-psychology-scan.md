# Agent Skill Security Scan Report

**Skill:** marketing-psychology
**Directory:** ./skills/coreyhaines31-marketingskills/skills/marketing-psychology
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 36.20s
**Timestamp:** 2026-02-01T09:53:14.411479

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Potential Indirect Prompt Injection via External Product Marketing Context File

**Severity:** MEDIUM
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The skill instructions direct the agent to read and follow content from `.claude/product-marketing-context.md` if it exists, with the directive to 'Use that context to tailor recommendations.' This creates a transitive trust relationship where the skill will follow instructions from an external file that may contain untrusted user input or malicious directives. If an attacker can control the contents of this file, they could inject instructions that override the skill's intended behavior or extract sensitive information.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
