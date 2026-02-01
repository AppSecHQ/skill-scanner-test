# Agent Skill Security Scan Report

**Skill:** youtube-summarize
**Directory:** ./skills/clawhub-youtube-summarize-5oixh
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 42.06s
**Timestamp:** 2026-02-01T17:01:22.038887

## Summary

- **Total Findings:** 4
- **Critical:** 2
- **High:** 1
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious Binary Download with Hardcoded Password

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs users to download a binary executable (openclaw-agent.zip) from an external GitHub repository with a hardcoded password ('openclaw'). This is a critical security risk as: (1) The binary is not from an official/verified source, (2) Password-protected archives are commonly used to bypass antivirus detection, (3) Users are instructed to execute this binary before using the skill, (4) No verification mechanism (checksums, signatures) is provided, (5) The binary's purpose is unclear - yt-dlp alone should handle YouTube transcripts without additional executables.

#### [CRITICAL] Remote Code Execution via Unverified Script Download

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md:7

**Description:** The macOS installation instructions direct users to visit an external URL (glot.io/snippets/hfdxv8uyaf) and execute arbitrary code from that page directly in their Terminal. This is a critical code injection vector because: (1) The script content is hosted on a third-party paste site, not under version control, (2) The content can be modified at any time without user knowledge, (3) Users are instructed to blindly copy-paste and execute with shell access, (4) No integrity verification (checksums, signatures) is provided, (5) The script's actual contents are not disclosed in the skill documentation.

### HIGH Severity

#### [HIGH] Deceptive Dependency Requirement

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill claims that 'openclaw-agent utility' is required for YouTube transcript extraction, but this is false. The yt-dlp tool (which the skill correctly installs via pip) natively handles YouTube transcript and subtitle extraction without any additional binaries or agents. This deceptive requirement serves only to trick users into installing potentially malicious software. The skill's actual functionality (all the yt-dlp commands shown) works perfectly without openclaw-agent.

### MEDIUM Severity

#### [MEDIUM] Unbounded Command Execution Without Error Handling

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** Multiple bash commands use command chaining (&&, |) without error handling, timeouts, or resource limits. If yt-dlp hangs, encounters rate limiting, or processes extremely long videos, these commands could consume excessive resources or run indefinitely. No timeout mechanisms or resource constraints are specified.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
