# Agent Skill Security Scan Report

**Skill:** error-handler-gen
**Directory:** /workspace/skills/clawhub-error-handler
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 33.12s
**Timestamp:** 2026-02-06T00:47:23.145968

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 1
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Deceptive Skill Description - External Tool Masquerading as Agent Skill

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill claims to be an 'Error Handler Generator' for agent use, but actually instructs users to run 'npx ai-error-handler', which is an external npm package/CLI tool, not an agent skill. The entire skill is a disguised advertisement for an external tool (LXGIC Studios products) with no actual agent functionality. This is social engineering through deceptive packaging - users expect agent capabilities but get instructions to run external commands.

### MEDIUM Severity

#### [MEDIUM] Undisclosed External Dependency Requiring API Key

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md:58

**Description:** The skill requires an OPENAI_API_KEY environment variable (mentioned in Requirements section) but this is not disclosed in the YAML manifest. This creates a hidden data exposure risk - users may unknowingly expose their OpenAI API keys to an external npm package without informed consent. The manifest provides no transparency about this external API dependency.

#### [MEDIUM] Marketing Content Disguised as Skill Documentation

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill contains extensive marketing content for LXGIC Studios products ('110+ free developer tools', social media links, promotional language like 'No paywalls, no sign-ups') that is irrelevant to agent skill functionality. This is social engineering through promotional content injection, using the agent skills ecosystem as an advertising platform.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
