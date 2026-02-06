# Agent Skill Security Scan Report

**Skill:** database
**Directory:** /workspace/skills/clawhub-database
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 29.50s
**Timestamp:** 2026-02-05T23:52:43.457021

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Missing Implementation Scripts for Database Operations

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE

**Description:** The skill claims to provide database management capabilities (PostgreSQL, MySQL, SQLite, MongoDB, Redis) including queries, schema management, data export/import, backup/restore, and performance monitoring. However, no Python or Bash scripts are provided to implement these features. This creates a tool exploitation risk where the agent may attempt to execute database operations without proper validation, error handling, or security controls that would normally be implemented in dedicated scripts.

#### [MEDIUM] SQL Injection Risk Without Implementation Controls

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill accepts arbitrary SQL queries from users ('Run query: SELECT * FROM users LIMIT 10') but provides no script implementation to sanitize or validate these queries. Without proper parameterization or input validation in code, this creates a command injection vector where malicious SQL could be executed directly against databases. The markdown instructions alone cannot enforce security controls.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
