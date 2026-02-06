# Agent Skill Security Scan Report

**Skill:** memory-hygiene
**Directory:** /workspace/skills/clawhub-memory-hygiene
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 31.73s
**Timestamp:** 2026-02-06T04:29:23.967404

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 1
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Destructive Data Deletion Without User Confirmation

**Severity:** HIGH
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The skill instructs the agent to execute 'rm -rf ~/.clawdbot/memory/lancedb/' which permanently deletes the user's entire vector memory database. This is a destructive operation with no confirmation, backup, or recovery mechanism. The command uses 'rm -rf' which forcefully removes directories recursively, risking data loss if executed accidentally or maliciously.

### MEDIUM Severity

#### [MEDIUM] Automated Cron Job with Destructive Operations

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill sets up a monthly cron job that automatically wipes the entire memory database without user intervention. This automated destructive operation runs at 4 AM on the first of every month, potentially causing unexpected data loss. The cron job combines multiple operations (wipe, parse, store) in an automated chain that could fail partially, leaving the system in an inconsistent state.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
