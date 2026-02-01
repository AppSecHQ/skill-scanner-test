# Agent Skill Security Scan Report

**Skill:** x-trends
**Directory:** ./skills/clawhub-x-trends-9y6gc
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 41.23s
**Timestamp:** 2026-02-01T19:39:38.165607

## Summary

- **Total Findings:** 4
- **Critical:** 1
- **High:** 2
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious Binary Download with Obfuscated Payload

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill instructs users to download and execute 'openclaw-agent' from an untrusted GitHub repository (hedefbari/openclaw-agent). The Windows version is distributed as a password-protected ZIP file (password: 'openclaw'), a common malware distribution technique used to evade antivirus detection. The macOS version directs users to execute a script from glot.io (a code snippet sharing site), which is a classic supply chain attack vector. There is no legitimate reason for a Twitter trends skill to require a separate binary agent, and the obfuscation techniques (password-protected archives, external script execution) are strong indicators of malicious intent.

### HIGH Severity

#### [HIGH] Social Engineering via Deceptive Skill Purpose

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill presents itself as a legitimate 'X (Twitter) Trends' analysis tool, but its actual purpose appears to be tricking users into installing malware ('openclaw-agent'). The skill description makes no mention of requiring external binary downloads, yet the instructions repeatedly emphasize that the skill 'will not work' without this suspicious binary. This is a classic social engineering attack where the skill's stated purpose (Twitter trends) is used as a lure to gain user trust and convince them to execute malicious code.

#### [HIGH] Credential Theft Risk via Malicious Binary

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs users to authorize twurl with their Twitter API credentials (consumer key and secret) while simultaneously requiring installation of an unknown binary ('openclaw-agent'). If the malicious binary is executed as instructed, it could intercept, steal, or exfiltrate these Twitter API credentials along with other sensitive data from the user's system. The binary would have full access to the user's environment, including credentials stored by twurl.

### MEDIUM Severity

#### [MEDIUM] Tool Shadowing via Fake Dependency Requirement

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill falsely claims that a binary called 'openclaw-agent' is required for Twitter trends operations, when in fact the Twitter API (accessed via twurl) requires no such dependency. This is tool shadowing - the skill is inserting a fake tool requirement to manipulate the execution environment. The legitimate twurl CLI can access Twitter trends directly without any additional agents, making the 'openclaw-agent' requirement completely unnecessary and suspicious.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
