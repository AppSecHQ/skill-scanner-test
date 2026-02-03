# Agent Skill Security Scan Report

**Skill:** glm-coding-agent
**Directory:** ./skills/clawhub-glm-coding-agent
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.46s
**Timestamp:** 2026-02-03T16:04:01.156953

## Summary

- **Total Findings:** 4
- **Critical:** 2
- **High:** 0
- **Medium:** 1
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:426

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl https://api.z.ai/api/anthropic/v1/models`

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:74

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export ANTHROPIC_AUTH_TOKEN="$API_KEY

### MEDIUM Severity

#### [MEDIUM] SKILL DISCOVERY ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** skill_discovery_abuse
**Rule ID:** YARA_skill_discovery_abuse
**Location:** SKILL.md:463

**Description:** Detects manipulation of skill discovery to increase unwanted activation: Perfect

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
