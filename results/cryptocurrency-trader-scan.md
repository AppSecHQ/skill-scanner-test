# Agent Skill Security Scan Report

**Skill:** cryptocurrency-trader
**Directory:** ./skills/clawhub-cryptocurrency-trader-skill
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 3.31s
**Timestamp:** 2026-02-03T15:54:46.039173

## Summary

- **Total Findings:** 7
- **Critical:** 0
- **High:** 1
- **Medium:** 5
- **Low:** 1
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Infinite loop without clear exit condition

**Severity:** HIGH
**Category:** resource_abuse
**Rule ID:** RESOURCE_ABUSE_INFINITE_LOOP
**Location:** skill.py:181

**Description:** Pattern detected: while True:

### MEDIUM Severity

#### [MEDIUM] User input used in command substitution - potential injection risk

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_USER_INPUT
**Location:** test_claude_code_compat.sh:56

**Description:** Pattern detected: $(python --version 2>&1 | awk '{print $2}')

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** llm_trading_assistant.py:119

**Description:** Pattern detected: os.getenv('OPENAI_API_KEY

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** llm_trading_assistant.py:137

**Description:** Pattern detected: os.getenv('ANTHROPIC_API_KEY

#### [MEDIUM] SKILL DISCOVERY ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** skill_discovery_abuse
**Rule ID:** YARA_skill_discovery_abuse
**Location:** SKILL.md:164

**Description:** Detects manipulation of skill discovery to increase unwanted activation: perfect

#### [MEDIUM] Environment variable harvesting detected

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_HARVESTING
**Location:** skills/clawhub-cryptocurrency-trader-skill/llm_trading_assistant.py

**Description:** Script iterates through environment variables in skills/clawhub-cryptocurrency-trader-skill/llm_trading_assistant.py

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
