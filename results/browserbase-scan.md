# Agent Skill Security Scan Report

**Skill:** browse
**Directory:** /workspace/skills/clawhub-browse
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 32.39s
**Timestamp:** 2026-02-05T21:06:05.235707

## Summary

- **Total Findings:** 7
- **Critical:** 0
- **High:** 0
- **Medium:** 3
- **Low:** 4
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:246

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): eval(selector, els =>
    els.map(el => el.textContent)

#### [MEDIUM] Hardcoded API credentials required without validation

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires BROWSERBASE_API_KEY and BROWSERBASE_PROJECT_ID environment variables but provides no validation, sanitization, or secure handling guidance. The instruction body shows credentials are stored in ~/.stagehand/config.json and copied to .env files in project directories, creating multiple copies of sensitive credentials across the filesystem without encryption or access controls.

#### [MEDIUM] Arbitrary code execution via page.evaluate()

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The instruction body demonstrates using page.evaluate() to execute arbitrary JavaScript in the browser context without any input validation or sanitization guidance. The example shows 'Complex extraction logic' placeholder, encouraging users to write custom JavaScript that will be executed in the browser. If user input flows into these evaluate() calls without proper sanitization, it creates a code injection vector.

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

#### [LOW] Missing resource limits and timeout configurations

**Severity:** LOW
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The automation code examples lack timeout configurations, retry limits, or resource constraints. Browser automation can consume significant resources and hang indefinitely if pages fail to load or selectors never appear. The instruction shows waitForLoadState() but no timeout parameter, and no guidance on handling infinite waits or resource exhaustion.

#### [LOW] Missing optional metadata fields

**Severity:** LOW
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill manifest is missing optional but recommended metadata fields: license, compatibility, and allowed-tools. While these are not required, their absence makes it harder for users to understand the skill's requirements, licensing terms, and which agent tools it expects to use.

#### [LOW] Referenced files not found in skill package

**Severity:** LOW
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The instruction body references four Python files (a.py, invocation.py, page.py, generated.py) that are not included in the skill package. These appear to be example files or documentation artifacts that are missing, which could confuse users or indicate incomplete packaging.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
