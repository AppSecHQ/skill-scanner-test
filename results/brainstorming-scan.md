# Agent Skill Security Scan Report

**Skill:** brainstorming
**Directory:** ./skills/obra-superpowers/skills/brainstorming
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 20.27s
**Timestamp:** 2026-02-01T09:48:07.168184

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Directive Prompt Injection - Mandatory Skill Usage

**Severity:** MEDIUM
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The skill description contains a directive 'You MUST use this before any creative work' which attempts to override the agent's decision-making autonomy. This is a form of direct prompt injection that tries to force the agent to always invoke this skill before performing creative tasks, regardless of whether it's appropriate or necessary. This could interfere with the agent's ability to handle simple requests efficiently or follow user preferences.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
