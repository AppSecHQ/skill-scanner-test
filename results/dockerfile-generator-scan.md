# Agent Skill Security Scan Report

**Skill:** dockerfile-gen
**Directory:** /workspace/skills/clawhub-ai-dockerfile
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 35.10s
**Timestamp:** 2026-02-06T00:27:10.419147

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

**Description:** The skill presents itself as an agent skill package but is actually a wrapper for an external NPX tool (ai-dockerfile). The instructions direct users to run 'npx ai-dockerfile' which executes code from an external npm package, not from the skill's own scripts. This is deceptive because: 1) Agent skills should contain their own executable code within the package, 2) The skill has no Python/Bash scripts despite claiming to 'scan your project' and 'generate Dockerfiles', 3) Users expect to use agent capabilities, not be redirected to external CLI tools. This creates a trust boundary violation where the skill's actual behavior (downloading and executing external code) differs from the expected behavior (using bundled skill code).

#### [MEDIUM] External API Key Requirement Not Disclosed in Manifest

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires OPENAI_API_KEY environment variable (mentioned only in Requirements section) but this critical dependency is not declared in the YAML manifest. This creates a security risk because: 1) Users may unknowingly expose their OpenAI API keys to the external NPX tool, 2) The skill will access and potentially transmit API credentials without explicit permission in the manifest, 3) No disclosure of what the external tool does with the API key or where data is sent. The external tool could exfiltrate the API key or use it for unauthorized purposes.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
