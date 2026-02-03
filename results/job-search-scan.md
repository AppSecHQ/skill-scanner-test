# Agent Skill Security Scan Report

**Skill:** Job Search MCP
**Directory:** ./skills/clawhub-job-search-mcp
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.41s
**Timestamp:** 2026-02-03T16:06:53.986807

## Summary

- **Total Findings:** 5
- **Critical:** 1
- **High:** 0
- **Medium:** 2
- **Low:** 2
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:50

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: claude_desktop_config.json

### MEDIUM Severity

#### [MEDIUM] AUTONOMY ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** autonomy_abuse
**Rule ID:** YARA_autonomy_abuse
**Location:** SKILL.md:531

**Description:** Detects unbounded autonomy patterns that could lead to runaway behavior: Ignore Error

#### [MEDIUM] SKILL DISCOVERY ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** skill_discovery_abuse
**Rule ID:** YARA_skill_discovery_abuse
**Location:** SKILL.md:84

**Description:** Detects manipulation of skill discovery to increase unwanted activation: Primary Tool

### LOW Severity

#### [LOW] Skill name does not follow agent skills naming rules

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_INVALID_NAME
**Location:** SKILL.md

**Description:** Skill name 'Job Search MCP' is invalid. Agent skills require lowercase letters, numbers, and hyphens only, with a maximum length of 64 characters.

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
