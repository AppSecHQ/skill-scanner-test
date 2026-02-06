# Agent Skill Security Scan Report

**Skill:** ansible
**Directory:** /workspace/skills/clawhub-ansible-skill
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 31.96s
**Timestamp:** 2026-02-05T19:23:13.686698

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 1
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Hardcoded SSH Password in Example Inventory

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The SKILL.md instruction body contains an example inventory configuration with a hardcoded SSH password reference using Ansible vault syntax ('ansible_ssh_pass: "{{ vault_eva_password }}"'). While this uses vault syntax, the example demonstrates storing SSH credentials which could encourage insecure practices if users don't properly implement vault encryption. The example shows direct password authentication to a production server (eva at 217.13.104.208), which is a security risk.

### MEDIUM Severity

#### [MEDIUM] Root User Access Encouraged in Examples

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The example inventory configuration shows 'ansible_user: root' for the eva server, which encourages direct root access via SSH. This violates security best practices and contradicts the skill's own security role that claims to implement 'SSH hardening (key-only, no root)'. The documentation promotes insecure practices that conflict with its stated security objectives.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
