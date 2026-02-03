# Agent Skill Security Scan Report

**Skill:** omni-stories
**Directory:** ./skills/clawhub-omni-stories
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.42s
**Timestamp:** 2026-02-03T16:07:21.813359

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Large base64 encoded string (possible code obfuscation)

**Severity:** MEDIUM
**Category:** obfuscation
**Rule ID:** OBFUSCATION_BASE64_LARGE
**Location:** SKILL.md:113

**Description:** Pattern detected: ce/aHR0cHM6Ly93aG9w/LmNvbS9ibG9nL2Nv/bnRlbnQvaW1hZ2Vz/L3NpemUvdzIwMDAv/MjAyNC8wNi9XaGF0/LWlzLUJ1eS1NZS1h/LUNvZmZlZS53ZWJw

#### [MEDIUM] Large base64 encoded string (possible code obfuscation)

**Severity:** MEDIUM
**Category:** obfuscation
**Rule ID:** OBFUSCATION_BASE64_LARGE
**Location:** ./README.md:60

**Description:** Pattern detected: ce/aHR0cHM6Ly93aG9w/LmNvbS9ibG9nL2Nv/bnRlbnQvaW1hZ2Vz/L3NpemUvdzIwMDAv/MjAyNC8wNi9XaGF0/LWlzLUJ1eS1NZS1h/LUNvZmZlZS53ZWJw

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
