# Agent Skill Security Scan Report

**Skill:** code-explain
**Directory:** /workspace/skills/clawhub-ai-explain
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 32.97s
**Timestamp:** 2026-02-05T22:36:57.601187

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 0
- **Medium:** 3
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Misleading Skill Description - External NPM Package Masquerading as Agent Skill

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill presents itself as an agent skill package but actually instructs users to run an external NPM package ('npx ai-explain'). This is deceptive because: (1) Agent skills should contain local SKILL.md + scripts, not redirect to external executables, (2) The skill has no actual implementation - no Python/Bash scripts provided, (3) All usage examples invoke an external NPM package that requires OPENAI_API_KEY, (4) Users expect a self-contained skill but get redirected to install/run untrusted external code, (5) The external package behavior cannot be verified through this skill analysis.

#### [MEDIUM] Undisclosed External API Dependency and Credential Requirement

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md:47

**Description:** The skill requires OPENAI_API_KEY environment variable but this critical requirement is only mentioned briefly at the end. This creates security risks: (1) Users may unknowingly expose their OpenAI API keys to the external NPM package, (2) No disclosure about what data is sent to OpenAI APIs, (3) User code would be transmitted to external servers without explicit consent in the main description, (4) Potential for credential theft if the external package is compromised, (5) No transparency about data handling, retention, or privacy.

#### [MEDIUM] Missing Referenced Implementation File

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE

**Description:** The skill references 'stdin.py' in its documentation but this file is not included in the package. This indicates: (1) Incomplete skill package, (2) Potential tool shadowing risk if users expect Python implementation but get NPM package instead, (3) Broken functionality if the skill attempts to use stdin.py, (4) Inconsistency between documentation and actual package contents.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
