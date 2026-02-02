# Agent Skill Security Scan Report

**Skill:** session-handoff
**Directory:** ./skills/softaworks-agent-toolkit/skills/session-handoff
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 3.41s
**Timestamp:** 2026-02-02T02:57:21.834968

## Summary

- **Total Findings:** 4
- **Critical:** 0
- **High:** 2
- **Medium:** 1
- **Low:** 1
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Database connection string with embedded credentials

**Severity:** HIGH
**Category:** hardcoded_secrets
**Rule ID:** SECRET_CONNECTION_STRING
**Location:** scripts/validate_handoff.py:31

**Description:** Pattern detected: postgres://[^/\s]+:[^@

#### [HIGH] Database connection string with embedded credentials

**Severity:** HIGH
**Category:** hardcoded_secrets
**Rule ID:** SECRET_CONNECTION_STRING
**Location:** scripts/validate_handoff.py:32

**Description:** Pattern detected: mysql://[^/\s]+:[^@

### MEDIUM Severity

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** evals/setup_test_env.py:29

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): subprocess.run(

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
