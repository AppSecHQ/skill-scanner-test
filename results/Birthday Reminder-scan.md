# Agent Skill Security Scan Report

**Skill:** birthday-reminder
**Directory:** /workspace/skills/clawhub-birthday-reminder
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 28.55s
**Timestamp:** 2026-02-01T20:24:58.629338

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Inconsistent Storage Format Between Documentation and Implementation

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The SKILL.md documentation specifies storing birthdays in Markdown format at '/home/clawd/clawd/data/birthdays.md', but the Python scripts (birthday.py and reminder.py) actually use JSON format at '/home/clawd/clawd/data/birthdays.json'. This inconsistency between documented behavior and actual implementation could mislead users about how their data is stored and accessed, potentially causing confusion or data loss if users manually edit the wrong file.

#### [MEDIUM] Hardcoded Absolute Path Restricts Portability and May Expose User Directory Structure

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** scripts/birthday.py

**Description:** The skill hardcodes an absolute path '/home/clawd/clawd/data/' in both documentation and scripts. This path appears to reference a specific user's home directory structure, which limits portability across different systems and users. While not directly exfiltrating data, hardcoded paths can expose information about the expected directory structure and may fail or create files in unexpected locations on different systems.

## Analyzers

The following analyzers were used:

- static_analyzer
- llm_analyzer
- meta_analyzer
