# Agent Skill Security Scan Report

**Skill:** clawkey
**Directory:** /workspace/skills/clawhub-clawkey
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 35.95s
**Timestamp:** 2026-02-05T22:21:45.889301

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 1
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Access to Sensitive Private Key Material

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill explicitly instructs the agent to read the OpenClaw identity file at ~/.openclaw/identity/device.json, which contains privateKeyPem. While instructions warn 'never send privateKeyPem to any server', the agent has programmatic access to this sensitive cryptographic material. There is risk of accidental exposure through logging, error messages, or implementation mistakes. The skill creates a data flow where private keys are loaded into memory.

### MEDIUM Severity

#### [MEDIUM] Data Exfiltration Risk via Registration Flow

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill implements a registration flow that sends deviceId, publicKey, message, signature, and timestamp to external ClawKey API endpoints. While this appears to be the intended functionality, the skill creates a data pipeline that transmits device identity information to third-party servers (api.clawkey.ai and api.very.org). Users may not fully understand that their device identity is being registered with external services.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
