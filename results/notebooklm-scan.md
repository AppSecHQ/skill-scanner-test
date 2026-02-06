# Agent Skill Security Scan Report

**Skill:** notebooklm
**Directory:** /workspace/skills/clawhub-notebooklm
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 51.01s
**Timestamp:** 2026-02-06T05:18:07.151155

## Summary

- **Total Findings:** 4
- **Critical:** 0
- **High:** 3
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Python scripts present but Python tool not in allowed-tools

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** ALLOWED_TOOLS_PYTHON_VIOLATION

**Description:** Skill restricts tools to ['Bash', 'Read', 'Write', 'Edit', 'Glob', 'Grep'] but includes Python scripts

#### [HIGH] Browser Session Cookie Theft and Credential Exposure

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** scripts/auth_manager.py

**Description:** The skill stores and manages Google authentication cookies in plaintext JSON files (state.json, auth_info.json) within the skill's data directory. These files contain sensitive session tokens that could be exfiltrated or accessed by other processes. The auth_manager.py and browser_session.py scripts handle Google login credentials and persist browser state with cookies that grant access to the user's NotebookLM account.

#### [HIGH] Subprocess Command Execution Without Input Validation

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** scripts/run.py

**Description:** Multiple scripts use subprocess.run() to execute Python scripts with user-controlled arguments without proper validation or sanitization. The run.py, quick_query.py, and setup_notebooklm.py scripts pass arguments directly to subprocess calls, creating potential command injection vectors if file paths or arguments contain shell metacharacters.

### MEDIUM Severity

#### [MEDIUM] Misleading Description About Local File Analysis

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill description emphasizes 'analyze your local files' and 'local file analyzer' but the actual implementation uploads files to Google's NotebookLM cloud service. This is not truly local analysis - it's cloud-based analysis of local files, which has different privacy and security implications that are not clearly disclosed in the manifest.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
