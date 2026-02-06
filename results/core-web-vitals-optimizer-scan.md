# Agent Skill Security Scan Report

**Skill:** core-vitals-fixer
**Directory:** /workspace/skills/clawhub-ai-core-vitals
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 26.75s
**Timestamp:** 2026-02-05T23:31:27.950330

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Deceptive Tool Description - Not an Agent Skill

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill presents itself as an agent skill for fixing Core Web Vitals issues, but the instructions describe an NPX command-line tool (npx ai-core-vitals) that operates independently of the agent. The skill contains no executable scripts, no agent instructions, and no integration with agent capabilities. Users expecting an agent skill will instead find documentation for an external NPX package that requires separate installation and API keys.

#### [MEDIUM] Undisclosed External API Dependency and Data Transmission

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires users to set OPENAI_API_KEY environment variable and transmits code files to GPT-4o-mini (OpenAI's API) for analysis. This external data transmission is buried in the documentation ('sends them to GPT-4o-mini') rather than prominently disclosed in the manifest. Users' source code would be sent to third-party servers without clear upfront consent or privacy implications explained.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
