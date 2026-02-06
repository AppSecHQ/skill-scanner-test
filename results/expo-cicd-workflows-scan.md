# Agent Skill Security Scan Report

**Skill:** expo-cicd-workflows
**Directory:** /workspace/skills/expo-skills/plugins/expo-deployment/skills/expo-cicd-workflows
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 37.05s
**Timestamp:** 2026-02-06T01:04:54.440968

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Transitive Trust Abuse - Following External Documentation Without Validation

**Severity:** MEDIUM
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The skill instructs the agent to fetch and follow instructions from external URLs (api.expo.dev, raw.githubusercontent.com) without any validation or sanitization. The skill explicitly states 'Do not rely on memorized values' and directs the agent to fetch remote content that will guide workflow generation. This creates a transitive trust vulnerability where an attacker who compromises these external resources could inject malicious instructions that the agent would follow.

### LOW Severity

#### [LOW] Undeclared Node.js Dependency Installation

**Severity:** LOW
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill instructs the agent to run 'npm install' to install dependencies for the validation script, but the package.json and specific dependencies are not provided for review. The allowed-tools declaration includes 'Bash(node:*)' which permits Node.js execution, but the automatic dependency installation could: (1) install packages with vulnerabilities, (2) execute post-install scripts from npm packages, (3) introduce supply chain risks if package.json is not pinned to specific versions.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
