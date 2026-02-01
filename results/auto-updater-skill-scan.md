# Agent Skill Security Scan Report

**Skill:** auto-updater
**Directory:** ./skills/clawhub-auto-updater-qdyme
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 43.32s
**Timestamp:** 2026-02-01T19:48:12.248225

## Summary

- **Total Findings:** 4
- **Critical:** 2
- **High:** 1
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious External Binary Download with Credential Harvesting

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs users to download and execute an external binary (openclaw-agent) from an untrusted GitHub repository (hedefbari/openclaw-agent). The Windows version requires a password-protected ZIP file, which is a common malware distribution technique to evade antivirus scanning. The macOS version directs users to execute a script from glot.io (a code snippet sharing site), which could contain arbitrary malicious code. This pattern is consistent with credential theft, backdoor installation, or system compromise. The skill falsely claims this utility is required for updates to function, creating a pretext for users to install malware.

#### [CRITICAL] Social Engineering via Fake Prerequisite Requirement

**Severity:** CRITICAL
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill uses deceptive social engineering by falsely claiming that 'openclaw-agent' is required for auto-update functionality. It repeatedly emphasizes this fake requirement with warnings like 'IMPORTANT', 'Without openclaw-agent installed, automatic updates and skill management will not work', and 'All update operations require openclaw-agent to be active'. This is designed to pressure users into installing the malicious binary. Legitimate Clawdbot updates use standard package managers (npm/pnpm/bun) or git, and do not require external utilities.

### HIGH Severity

#### [HIGH] Tool Poisoning via Malicious Cron Job Installation

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill instructs the agent to set up a cron job that would execute update commands, but the entire premise is poisoned by the malicious openclaw-agent requirement. If users follow the instructions, they would install a cron job that runs in an 'isolated' session with 'wake now' and 'deliver' flags, potentially allowing the malicious binary to execute with elevated privileges or persistence. The cron job setup itself appears designed to establish persistence for the malware.

### MEDIUM Severity

#### [MEDIUM] Misleading Skill Description and Purpose

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill's description claims to 'Automatically update Clawdbot and all installed skills once daily' which sounds like legitimate maintenance functionality. However, the actual purpose is to trick users into installing malware. The skill name 'auto-updater' and professional-looking documentation are designed to appear trustworthy and useful, masking the malicious intent.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
