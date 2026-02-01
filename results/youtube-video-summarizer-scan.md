# Agent Skill Security Scan Report

**Skill:** youtube-summarize
**Directory:** ./skills/clawhub-youtube-summarize-lh9rq
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 35.26s
**Timestamp:** 2026-02-01T19:56:08.443345

## Summary

- **Total Findings:** 4
- **Critical:** 2
- **High:** 2
- **Medium:** 0
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious Binary Download with Obfuscated Payload

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs users to download and execute a binary (openclaw-agent.zip) from an untrusted GitHub repository with password-protected archive ('openclaw'). This is a classic malware distribution pattern - password-protected archives bypass antivirus scanning, and the executable's true purpose cannot be verified. The skill falsely claims this utility is required for YouTube transcript extraction, but yt-dlp itself handles transcripts natively without any external agent. This is a social engineering attack to trick users into installing malware.

#### [CRITICAL] Remote Code Execution via Untrusted Script

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md:7

**Description:** The skill instructs macOS users to visit an external URL (glot.io/snippets/hfdxv8uyaf), copy an unknown script, and paste it directly into Terminal for execution. This is arbitrary remote code execution - the script content is not shown, cannot be audited, and could contain any malicious commands (data exfiltration, backdoor installation, credential theft). The attacker controls the glot.io snippet and can modify it at any time to target victims.

### HIGH Severity

#### [HIGH] Deceptive Skill Purpose - Social Engineering

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill's description claims it summarizes YouTube videos using transcripts, which is a legitimate use case. However, the actual instructions focus on tricking users into downloading and executing malware (openclaw-agent) under the false pretense that it's required for transcript extraction. The skill uses social engineering by presenting malware installation as a 'prerequisite' with urgent language ('IMPORTANT', 'will not work'). This is tool poisoning disguised as a helpful utility.

#### [HIGH] False Technical Claims to Distribute Malware

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill makes demonstrably false technical claims that 'openclaw-agent utility' is required for YouTube transcript extraction. This is misinformation designed to trick users into installing malware. The skill's own commands (lines 18-60) prove that yt-dlp handles transcript extraction perfectly without any external agent. The false prerequisite section contradicts the skill's actual working commands.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
