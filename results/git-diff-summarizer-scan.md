# Agent Skill Security Scan Report

**Skill:** diff-summary
**Directory:** /workspace/skills/clawhub-ai-diff-summary
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 27.24s
**Timestamp:** 2026-02-06T02:04:46.961606

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Misleading Package Type - NPM Package Presented as Agent Skill

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill presents itself as an Agent Skill package but is actually an NPM package (npx ai-diff-summary). The instructions tell users to run 'npx ai-diff-summary' which executes external Node.js code from the NPM registry, not local skill scripts. This is deceptive because Agent Skills should be self-contained local packages with SKILL.md and optional scripts, not wrappers for external package managers.

#### [MEDIUM] External API Key Requirement Not Disclosed in Manifest

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md:42

**Description:** The skill requires OPENAI_API_KEY environment variable but this is only mentioned in the instruction body, not in the YAML manifest. This is a security concern because the skill will access and potentially transmit data to OpenAI's API without clear upfront disclosure in the metadata. Users may not realize their git diffs (which could contain sensitive code, credentials, or proprietary information) will be sent to a third-party API.

### LOW Severity

#### [LOW] Missing Script Implementation - Referenced File Not Found

**Severity:** LOW
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE

**Description:** The instructions reference 'main.py' but this file is not included in the skill package. This creates a broken skill that cannot function as described. While not a direct security threat, it indicates incomplete or potentially deceptive packaging.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
