# Agent Skill Security Scan Report

**Skill:** Docker Pro Diagnostic
**Directory:** ./skills/clawhub-docker-diag
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 0.79s
**Timestamp:** 2026-02-03T15:59:22.151034

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 1
- **Medium:** 0
- **Low:** 2
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Shell command execution with shell=True enabled

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_SHELL_TRUE
**Location:** log_processor.py:14

**Description:** Pattern detected: subprocess.run(cmd, shell=True

### LOW Severity

#### [LOW] Skill name does not follow agent skills naming rules

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_INVALID_NAME
**Location:** SKILL.md

**Description:** Skill name 'Docker Pro Diagnostic' is invalid. Agent skills require lowercase letters, numbers, and hyphens only, with a maximum length of 64 characters.

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
