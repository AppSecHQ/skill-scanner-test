# Agent Skill Security Scan Report

**Skill:** openclaw-checkpoint
**Directory:** /workspace/skills/clawhub-openclaw-checkpoint
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 50.05s
**Timestamp:** 2026-02-06T05:49:31.800302

## Summary

- **Total Findings:** 4
- **Critical:** 0
- **High:** 2
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Remote Code Execution via Unverified Install Script

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill instructs users to execute a remote shell script directly from GitHub using curl piped to bash without any verification. This is a critical security anti-pattern that allows arbitrary code execution on the user's machine. The script at https://raw.githubusercontent.com/AnthonyFrancis/openclaw-checkpoint/main/scripts/install-openclaw-checkpoint.sh could be modified by an attacker (if the repository is compromised) or could contain malicious code. Users are executing this with their full user privileges without any opportunity to review the code first.

#### [HIGH] Potential Credential and Sensitive Data Exposure via Git Repository

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill syncs the entire OpenClaw workspace to a git repository, including SOUL.md, MEMORY.md, conversation history, and custom scripts. While the description claims '.env.* files are not synced', there is no verification that the .gitignore is properly configured or that users understand what constitutes sensitive data. Memory files and conversation history may contain API keys, passwords, personal information, or confidential data that users discussed with the assistant. The checkpoint-setup command 'Commits ALL workspace files (not just .gitignore)' which explicitly overrides gitignore protections. If the GitHub repository is misconfigured as public or if credentials are leaked in the repository, this creates a significant data exposure risk.

### MEDIUM Severity

#### [MEDIUM] Unauthorized Tool Installation and PATH Modification

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The installation process automatically copies executable scripts to ~/.openclaw/workspace/tools/ and modifies the user's PATH environment variable without explicit permission or clear explanation of the security implications. This allows the skill to inject arbitrary executables into the user's command execution path. The scripts (checkpoint, checkpoint-setup, checkpoint-auth, etc.) will be available system-wide and could shadow legitimate commands or be invoked unintentionally. The automatic PATH modification in shell configuration files (~/.zshrc, ~/.bashrc) persists across sessions.

#### [MEDIUM] SSH Key and GitHub Authentication Security Risks

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The checkpoint-auth and checkpoint-setup commands handle SSH keys and GitHub authentication, but the documentation does not specify: 1) How SSH keys are generated or managed, 2) Whether existing SSH keys are reused or new ones created, 3) What permissions are requested for Personal Access Tokens, 4) How credentials are stored locally, 5) Whether the GitHub CLI authentication is properly scoped. The 'Automatically adds GitHub to known_hosts' behavior could be exploited in a MITM attack if not properly verified. The skill has access to authentication credentials that could be misused.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
