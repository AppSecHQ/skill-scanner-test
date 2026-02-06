# Agent Skill Security Scan Report

**Skill:** lighthouse-fixer
**Directory:** /workspace/skills/clawhub-lighthouse-fix
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 27.33s
**Timestamp:** 2026-02-06T03:54:18.279451

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Hardcoded External API Dependency with Required Credentials

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION

**Description:** The skill requires users to set OPENAI_API_KEY environment variable to function. This creates a credential exposure risk where the skill will access and potentially transmit the user's OpenAI API key to external services. The skill documentation states it sends Lighthouse reports to GPT-4o-mini, which means user API credentials are being used for external API calls without explicit security warnings about key exposure or usage limits.

#### [MEDIUM] Unverified External Tool Execution via npx

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE

**Description:** The skill instructs users to execute code directly via 'npx ai-lighthouse' without any verification mechanism, package integrity checks, or source code review. This creates a tool exploitation risk where users may unknowingly execute malicious code from npm registry. The package 'ai-lighthouse' is not bundled with the skill and is fetched at runtime from external sources.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
