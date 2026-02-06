# Agent Skill Security Scan Report

**Skill:** calendar
**Directory:** /workspace/skills/clawhub-calendar
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 30.16s
**Timestamp:** 2026-02-05T21:13:56.928175

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Misleading Description - No Implementation Provided

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING

**Description:** The skill claims to provide 'Calendar management and scheduling' with features like creating events, managing meetings, and syncing across calendar providers (Google Calendar, Apple Calendar, Outlook Calendar). However, the skill package contains no script files or implementation code. This is deceptive as users would expect functional calendar integration based on the description, but the skill cannot actually perform any of the advertised operations. The skill appears to be a placeholder or incomplete package masquerading as a functional tool.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
