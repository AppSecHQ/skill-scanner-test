# Agent Skill Security Scan Report

**Skill:** gitlab-cli-skills
**Directory:** /workspace/skills/clawhub-gitlab-cli-skills
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 26.79s
**Timestamp:** 2026-02-06T02:22:52.578574

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Transitive Trust in Sub-Skill Delegation

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** This routing skill delegates all actual functionality to 33 separate sub-skills without any apparent validation, security checks, or trust boundaries. The skill blindly trusts that all listed sub-skills (glab-auth, glab-api, glab-ci, etc.) are safe and properly implemented. If any of the 33 sub-skills are compromised, malicious, or contain vulnerabilities, this router will direct users to them without warning. This creates a transitive trust chain where the security of this skill depends entirely on the security of 33 other skills that are not analyzed here.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
