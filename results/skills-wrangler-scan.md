# Agent Skill Security Scan Report

**Skill:** wrangler
**Directory:** /workspace/skills/cloudflare-skills/skills/wrangler
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.24s
**Timestamp:** 2026-02-06T07:49:18.033281

## Summary

- **Total Findings:** 3
- **Critical:** 1
- **High:** 1
- **Medium:** 0
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:840

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl http://localhost:8787/__scheduled

### HIGH Severity

#### [HIGH] Database connection string with embedded credentials

**Severity:** HIGH
**Category:** hardcoded_secrets
**Rule ID:** SECRET_CONNECTION_STRING
**Location:** SKILL.md:480

**Description:** Pattern detected: postgres://user:pass@

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
