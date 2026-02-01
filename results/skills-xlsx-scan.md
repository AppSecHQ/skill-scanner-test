# Agent Skill Security Scan Report

**Skill:** xlsx
**Directory:** ./skills/anthropics-skills/skills/xlsx
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 37.34s
**Timestamp:** 2026-02-01T22:08:18.605259

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Subprocess Execution Without Input Validation

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** recalc.py

**Description:** The script executes LibreOffice via subprocess.run() with user-controlled file paths. While the truncated code doesn't show the full implementation, subprocess execution with file paths could enable command injection if file names contain shell metacharacters or if additional arguments are passed without proper sanitization.

#### [MEDIUM] File System Modification Without User Confirmation

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** recalc.py

**Description:** The script automatically creates directories and writes macro files to the user's LibreOffice configuration without explicit user consent. The setup_libreoffice_macro() function modifies ~/.config/libreoffice or ~/Library/Application Support directories, which could interfere with existing LibreOffice configurations or be used for persistence.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
