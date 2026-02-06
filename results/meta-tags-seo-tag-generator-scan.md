# Agent Skill Security Scan Report

**Skill:** Meta Tags - SEO Tag Generator
**Directory:** /workspace/skills/clawhub-meta-tags
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 26.50s
**Timestamp:** 2026-02-06T04:36:10.092739

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Unpinned External Dependency - Supply Chain Risk

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md:7

**Description:** The skill instructs users to install an NPM package without version pinning (npm install -g @lxgicstudios/meta-tags). This creates a supply chain security risk where a compromised or malicious package update could be automatically installed. The package source and integrity cannot be verified from the skill manifest alone.

### LOW Severity

#### [LOW] Undeclared Tool Usage - NPM Package Installation

**Severity:** LOW
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill instructions require installing and executing an external NPM package (@lxgicstudios/meta-tags) but the manifest does not declare 'allowed-tools'. While this field is optional, the skill's functionality depends entirely on executing external commands (npm/npx) which should be explicitly declared for transparency. The skill cannot function without Bash tool access to run npm commands.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
