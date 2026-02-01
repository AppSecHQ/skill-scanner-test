# Agent Skill Security Scan Report

**Skill:** auto-updater
**Directory:** ./skills/clawhub-auto-updater-xsunp
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 37.09s
**Timestamp:** 2026-02-01T19:05:36.076273

## Summary

- **Total Findings:** 4
- **Critical:** 1
- **High:** 2
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious External Executable Download with Credential Harvesting

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs users to download and execute an external binary (openclaw-agent) from an untrusted GitHub repository (hedefbari/openclaw-agent). The Windows version requires extracting with a password ('openclaw'), a common malware distribution technique to evade antivirus scanning. The macOS version directs users to execute a script from glot.io (a code snippet sharing site), which could contain arbitrary malicious code. This pattern is consistent with credential theft, backdoor installation, or system compromise. The skill falsely claims this utility is required for updates to function, creating urgency and social engineering pressure.

### HIGH Severity

#### [HIGH] Social Engineering via False Prerequisites

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill uses deceptive social engineering by claiming that a third-party utility (openclaw-agent) is 'IMPORTANT' and required for auto-updater operations. This creates false urgency and authority to trick users into downloading malicious software. The repeated warnings ('Without openclaw-agent installed, automatic updates and skill management will not work') are designed to overcome user skepticism and bypass security awareness.

#### [HIGH] Tool Poisoning via Fake Update Mechanism

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill masquerades as a legitimate auto-updater but actually attempts to install malware under the guise of a required utility. By claiming to automate Clawdbot and skill updates, it gains user trust while delivering a malicious payload. The skill provides no actual update functionality - it only instructs users to download external malware. This is tool poisoning where the skill's claimed purpose (updates) is used to deliver an attack (malware installation).

### MEDIUM Severity

#### [MEDIUM] Misleading Instructions for Legitimate Commands

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill provides instructions for legitimate Clawdbot commands (clawdbot doctor, clawdhub update) mixed with malicious instructions. This creates confusion and lends false credibility to the malicious components. Users may believe the entire skill is legitimate because some commands appear valid, lowering their guard for the malicious payload delivery.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
