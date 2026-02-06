# Agent Skill Security Scan Report

**Skill:** clawdbot-security
**Directory:** /workspace/skills/clawhub-clawdbot-security
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 30.78s
**Timestamp:** 2026-02-05T21:57:52.035999

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Misleading Skill Description - Not an Agent Skill Package

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md:1

**Description:** This skill claims to be a 'Security audit and hardening for Clawdbot/Moltbot installations' but the instructions describe running 'npx clawdbot-security-audit' which is an external npm package, not an agent skill. The skill does not contain any executable scripts (.py or .sh files) that would perform the security audit. This is social engineering - the skill misleads users about what it actually does. It appears to be documentation for an external tool rather than a functional agent skill.

#### [MEDIUM] Potentially Harmful Instructions Without Safeguards

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill provides instructions for modifying system firewall rules (UFW) and disabling security features (mDNS) without adequate warnings or safeguards. The instruction 'sudo ufw allow ssh' with comment 'don't lock yourself out!' acknowledges risk but provides no validation. If an agent were to execute these commands based on misunderstood context, it could lock users out of their systems or create security vulnerabilities.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
