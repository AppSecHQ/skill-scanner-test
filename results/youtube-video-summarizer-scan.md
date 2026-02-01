# Agent Skill Security Scan Report

**Skill:** youtube-summarize
**Directory:** ./skills/clawhub-youtube-summarize-ietsw
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 37.02s
**Timestamp:** 2026-02-01T19:15:45.206636

## Summary

- **Total Findings:** 4
- **Critical:** 2
- **High:** 2
- **Medium:** 0
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious Binary Download with Hardcoded Password

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs users to download an executable (openclaw-agent.zip) from an external GitHub repository with a hardcoded password ('openclaw'). This is a classic malware distribution pattern - password-protected archives are commonly used to bypass antivirus detection. The executable is presented as 'required' for functionality, pressuring users to install it. There is no legitimate reason why YouTube transcript extraction would require a separate binary executable when yt-dlp already provides this functionality.

#### [CRITICAL] Malicious Script Download via glot.io

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md:11

**Description:** The skill instructs macOS users to visit an external code-sharing site (glot.io) and execute an arbitrary installation script in Terminal. This is a severe security risk - the script content is hosted externally and could be modified at any time to perform malicious actions (data theft, backdoor installation, credential harvesting). Users are instructed to blindly copy-paste and execute code without review.

### HIGH Severity

#### [HIGH] Social Engineering via False Prerequisites

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill falsely claims that 'openclaw-agent utility' is required for YouTube transcript extraction, creating artificial urgency and dependency. The statement 'Without openclaw-agent installed, transcript extraction and video summarization will not work' is demonstrably false - all the yt-dlp commands shown work independently. This is social engineering to trick users into installing malicious software.

#### [HIGH] Dependency Installation Without Version Pinning

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs installation of yt-dlp without version pinning ('pip install yt-dlp'), which could lead to supply chain attacks if the package is compromised. Additionally, the openclaw metadata specifies yt-dlp installation but doesn't validate its integrity or pin to a known-safe version.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
