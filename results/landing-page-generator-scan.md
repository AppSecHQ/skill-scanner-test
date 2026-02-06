# Agent Skill Security Scan Report

**Skill:** landing-gen
**Directory:** /workspace/skills/clawhub-ai-landing
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 26.69s
**Timestamp:** 2026-02-06T03:49:50.223928

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Misleading Skill Description - External Tool Masquerading as Agent Skill

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING

**Description:** The skill presents itself as an agent skill package but actually describes an external NPX package (ai-landing) that requires separate installation and API keys. The instructions contain NPX commands ('npx ai-landing') which are not agent skill operations. This is deceptive because users expect a self-contained skill package, not instructions to install and run external tools. The skill does not contain any executable code (no Python/Bash scripts) despite claiming to 'generate landing page code'.

#### [MEDIUM] External API Key Requirement Not Declared in Manifest

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires OPENAI_API_KEY environment variable but this is not declared in the YAML manifest. Users may unknowingly expose their OpenAI credentials to an external NPX package without understanding the data flow or security implications. The manifest lacks transparency about external dependencies and credential requirements.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
