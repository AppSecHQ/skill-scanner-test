# Agent Skill Security Scan Report

**Skill:** gitclaw
**Directory:** /workspace/skills/clawhub-gitclaw
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 46.24s
**Timestamp:** 2026-02-06T02:10:53.519689

## Summary

- **Total Findings:** 5
- **Critical:** 0
- **High:** 2
- **Medium:** 3
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Unbounded Autonomous Execution Without User Confirmation

**Severity:** HIGH
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The skill instructs the agent to 'Do everything automatically and quietly' and only message the user for specific inputs or failures. This creates an unbounded autonomy pattern where the skill will automatically install system packages (git, cron, gh), modify system configuration (crontab), initialize git repositories, create GitHub repositories, and set up automated background processes without explicit user confirmation for each action. The instruction 'Use this skill automatically when it's installed or reference' further amplifies this by triggering execution without user request.

#### [HIGH] Privilege Escalation via Automated sudo Commands

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill automatically executes multiple sudo commands without user awareness or confirmation, including package installations (apt-get, dnf, yum, pacman, zypper, apk) and system service modifications (systemctl, service, rc-update). The 'do everything automatically and quietly' directive means these privileged operations happen in the background. This represents a significant security risk as it grants the skill root-level system access without explicit authorization.

### MEDIUM Severity

#### [MEDIUM] Persistent Background Process Installation Without Clear Disclosure

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The skill installs a cron job that will run automatically in the background at regular intervals (default 60 minutes) to commit and push workspace changes to GitHub. This persistent background process is installed 'automatically and quietly' without prominent disclosure to the user about the ongoing automated commits. Users may not realize their workspace is being continuously monitored and uploaded to GitHub, potentially exposing sensitive work-in-progress code, credentials, or private data.

#### [MEDIUM] Potential Exposure of Sensitive Data via Automated Git Commits

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill automatically backs up the entire OpenClaw workspace to GitHub without implementing safeguards against committing sensitive data. The instructions do not mention .gitignore configuration, credential scanning, or exclusion of sensitive files. Combined with automated silent operation and the ability to create public repositories, this could lead to accidental exposure of API keys, credentials, private data, or proprietary code. The cron-driven automation means sensitive data could be pushed without user review.

#### [MEDIUM] Missing allowed-tools Declaration for Privileged Operations

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill performs extensive system modifications including package installation, crontab modification, git operations, and GitHub API interactions, but does not declare any allowed-tools restrictions in the YAML manifest. While allowed-tools is optional, its absence for a skill performing privileged system operations represents a security concern as it provides no guardrails against tool misuse. The skill requires at minimum: Bash (for all system commands), Write (for git init, crontab modification), and potentially Python for any scripting.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
