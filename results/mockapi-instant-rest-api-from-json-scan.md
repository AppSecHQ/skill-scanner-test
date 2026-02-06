# Agent Skill Security Scan Report

**Skill:** MockAPI - Instant REST API from JSON
**Directory:** /workspace/skills/clawhub-mockapi
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 30.13s
**Timestamp:** 2026-02-06T04:39:07.240210

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 2
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Misleading Skill Description - Not an Agent Skill

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md:1

**Description:** The skill presents itself as 'MockAPI - Instant REST API from JSON' with instructions to install and run an npm package (@lxgicstudios/mockapi). However, this is NOT an agent skill package - it's documentation for an external CLI tool. Agent skills should contain SKILL.md with instructions for the agent to follow, plus optional Python/Bash scripts the agent executes. This skill contains no executable scripts and instead instructs users to install and run external software via npm/npx commands. The description 'Free CLI tool for frontend developers' confirms this is external tooling, not an agent capability extension.

### LOW Severity

#### [LOW] Skill name does not follow agent skills naming rules

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_INVALID_NAME
**Location:** SKILL.md

**Description:** Skill name 'MockAPI - Instant REST API from JSON' is invalid. Agent skills require lowercase letters, numbers, and hyphens only, with a maximum length of 64 characters.

#### [LOW] Missing Referenced File - Potential Code Execution Risk

**Severity:** LOW
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION

**Description:** The skill references a file 'a.py' in its instructions, but this file is not found in the skill package. If this file were present and contained malicious code, it could pose a security risk. The absence of the file prevents analysis of potential threats. This could indicate incomplete packaging, a typo, or intentional obfuscation.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
