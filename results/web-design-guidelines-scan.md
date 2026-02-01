# Agent Skill Security Scan Report

**Skill:** web-design-guidelines
**Directory:** ./skills/vercel-labs-agent-skills/skills/web-design-guidelines
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 31.96s
**Timestamp:** 2026-02-01T20:35:43.515179

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 1
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Indirect Prompt Injection via External URL Content

**Severity:** HIGH
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The skill instructs the agent to fetch and follow instructions from an external URL (https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md) without any validation or sanitization. The fetched content explicitly contains 'all the rules and output format instructions' that the agent must follow. This creates a transitive trust vulnerability where an attacker controlling or compromising that URL could inject arbitrary instructions that the agent would execute. The skill delegates complete trust to external content, allowing potential instruction override, data exfiltration commands, or malicious directives.

### MEDIUM Severity

#### [MEDIUM] Potentially Deceptive Scope - External Dependency Not Disclosed

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill description claims to 'Review UI code for Web Interface Guidelines compliance' but does not disclose that it fetches and executes instructions from an external GitHub repository. Users may reasonably expect a self-contained local analysis tool, not one that depends on and trusts external network resources. This lack of transparency about the external dependency and trust model could mislead users about the skill's actual behavior and security posture.

#### [MEDIUM] Implicit Tool Use Without Declaration

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill requires WebFetch tool to retrieve external guidelines ('Use WebFetch to retrieve the latest rules') but does not declare this in the allowed-tools manifest field. While allowed-tools is optional, the skill's core functionality depends on network access capabilities that are not documented in the manifest. This creates a mismatch between declared and actual tool requirements, potentially bypassing user expectations about network access.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
