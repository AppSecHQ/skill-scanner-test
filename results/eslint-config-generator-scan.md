# Agent Skill Security Scan Report

**Skill:** eslint-gen
**Directory:** /workspace/skills/clawhub-eslint-gen
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 40.70s
**Timestamp:** 2026-02-06T00:50:09.151707

## Summary

- **Total Findings:** 4
- **Critical:** 0
- **High:** 1
- **Medium:** 3
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Unauthorized External Package Execution

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill instructs users to execute an external npm package 'ai-eslint-config' via npx without any verification, provenance checking, or security warnings. This package is not included in the skill, has unknown authorship, and could contain malicious code. The skill effectively acts as a trojan to get users to run unvetted third-party code on their systems.

### MEDIUM Severity

#### [MEDIUM] Deceptive Skill Description - Not an Agent Skill

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** This skill claims to be an ESLint config generator but provides instructions for using 'npx ai-eslint-config', which is an external npm package, not an agent skill. The skill contains no executable scripts (Python/Bash) and provides no agent instructions. This is misleading packaging that misrepresents what the skill actually does. Users expecting an agent skill will instead be directed to run an external, unvetted npm package.

#### [MEDIUM] Potential Data Exposure via External Package

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The external npm package 'ai-eslint-config' is instructed to scan the user's entire codebase (via 'npx ai-eslint-config .'). Without being able to audit this package's source code, there is no guarantee it doesn't exfiltrate code patterns, file structures, or sensitive information to external servers. The skill description mentions it's 'part of LXGIC Dev Toolkit' with links to external websites, suggesting potential data collection.

#### [MEDIUM] Misleading Marketing Content

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill contains extensive marketing content ('110+ free developer tools', 'No paywalls, no sign-ups', social media links) that is inappropriate for an agent skill and serves to promote external services rather than provide legitimate agent functionality. This content appears designed to drive traffic to external websites rather than provide security-auditable agent capabilities.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
