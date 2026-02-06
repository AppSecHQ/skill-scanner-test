# Agent Skill Security Scan Report

**Skill:** antigravity-image-gen
**Directory:** /workspace/skills/clawhub-antigravity-image-gen
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 32.75s
**Timestamp:** 2026-02-05T19:28:55.855903

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 1
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Credential Theft via OAuth Profile Access

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill explicitly requires access to OAuth credentials stored in `~/.clawdbot/agents/main/agent/auth-profiles.json`. This file likely contains sensitive authentication tokens for Google services. The skill instructions direct users to execute a script that would read these credentials, creating a credential theft vector. While the actual script file is not provided for analysis, the documented requirement to access this sensitive credential file represents a significant security risk.

### MEDIUM Severity

#### [MEDIUM] Deceptive API Endpoint Claims

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill claims to use an 'internal Google Antigravity API' and 'Gemini 3 Pro Image' via the 'daily-cloudcode-pa.sandbox' endpoint. These claims are suspicious: (1) 'Antigravity' is not a known Google API product, (2) 'Gemini 3 Pro Image' does not match Google's actual model naming conventions (Gemini Pro, Gemini Ultra, etc.), (3) The 'sandbox' endpoint naming suggests unofficial or testing infrastructure. This appears to be social engineering to make users trust the skill by invoking Google's brand name with fabricated product names. The actual endpoint behavior cannot be verified without the script.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
