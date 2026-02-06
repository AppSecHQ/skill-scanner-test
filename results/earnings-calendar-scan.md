# Agent Skill Security Scan Report

**Skill:** earnings-calendar
**Directory:** /workspace/skills/clawhub-earnings-calendar
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 27.44s
**Timestamp:** 2026-02-06T00:38:28.928281

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Hardcoded API Key Exposure Risk in User Prompts

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The SKILL.md instructions explicitly prompt users to provide their FMP API key as a command-line argument or through interactive prompts in web environments. While the scripts don't hardcode secrets, the workflow encourages users to expose API keys in command history, logs, or session storage. The instruction 'API key will be requested during skill execution (stored only for current session)' suggests temporary storage without clear security guarantees.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
