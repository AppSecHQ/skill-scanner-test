# Agent Skill Security Scan Report

**Skill:** discord-voice
**Directory:** /workspace/skills/clawhub-discord-voice
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 41.15s
**Timestamp:** 2026-02-06T00:17:16.453413

## Summary

- **Total Findings:** 4
- **Critical:** 1
- **High:** 1
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Hardcoded API Keys in Configuration Examples

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The SKILL.md documentation contains examples showing hardcoded API keys directly in configuration files (e.g., 'sk-...' for OpenAI). This practice encourages users to store sensitive credentials in plaintext configuration files, which can lead to credential exposure through version control, backups, or unauthorized file access.

### HIGH Severity

#### [HIGH] Multiple Sensitive API Keys Required Without Security Guidance

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires multiple sensitive API keys (DISCORD_TOKEN, OPENAI_API_KEY, ELEVENLABS_API_KEY, DEEPGRAM_API_KEY) but provides no security guidance on key management, rotation, or secure storage. The manifest lists these as required/optional environment variables but the documentation shows configuration examples that could lead to insecure storage practices.

### MEDIUM Severity

#### [MEDIUM] System Dependencies Without Integrity Verification

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill requires installation of system dependencies (ffmpeg, build-essential) via package managers without any integrity verification, version pinning, or security guidance. Users are instructed to install these with sudo privileges, which could be exploited if package repositories are compromised or if users are on networks with MITM attacks.

#### [MEDIUM] Incomplete Disclosure of Network Activity and Data Flow

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill description emphasizes 'real-time voice conversations' but doesn't clearly disclose that user voice data is transmitted to multiple third-party services (OpenAI, Deepgram, ElevenLabs). Users may not understand that their voice recordings leave their Discord server and are processed by external APIs, potentially violating privacy expectations or regulations.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
