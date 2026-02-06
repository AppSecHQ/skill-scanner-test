# Agent Skill Security Scan Report

**Skill:** paid-ads
**Directory:** /workspace/skills/coreyhaines31-marketingskills/skills/paid-ads
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 30.58s
**Timestamp:** 2026-02-06T06:04:36.511497

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Instruction to Read External Product Marketing Context File

**Severity:** MEDIUM
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The skill instructions explicitly direct the agent to check for and read '.claude/product-marketing-context.md' before starting, stating 'If `.claude/product-marketing-context.md` exists, read it before asking questions.' This creates a transitive trust relationship where the skill will follow instructions or use data from an external file outside the skill package without validation. An attacker could place malicious instructions in this file to manipulate the agent's behavior.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
