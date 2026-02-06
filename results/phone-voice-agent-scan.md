# Agent Skill Security Scan Report

**Skill:** phone-agent
**Directory:** /workspace/skills/clawhub-phone-agent
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 73.70s
**Timestamp:** 2026-02-06T06:23:46.778168

## Summary

- **Total Findings:** 4
- **Critical:** 1
- **High:** 1
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Hardcoded API Keys and Credentials in Source Code

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** scripts/server.py

**Description:** The server.py script contains hardcoded Twilio phone number (+18665515246) and references to API keys that may be committed to version control. While environment variables are used for most credentials, the presence of hardcoded values and the pattern of credential handling creates risk of accidental exposure. The script also accesses multiple sensitive API keys (Deepgram, OpenAI, ElevenLabs, Brave, Twilio) which if logged or exposed could enable unauthorized access to paid services.

### HIGH Severity

#### [HIGH] Network Data Exfiltration via External API Calls

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** scripts/server.py

**Description:** The skill makes multiple outbound network calls to external services (Deepgram, OpenAI, ElevenLabs, Brave Search) and transmits audio data, transcripts, and potentially sensitive conversation content. The phone agent processes real-time voice calls and sends this data to third-party APIs without explicit user consent mechanisms. Audio streams from phone calls could contain sensitive personal information, credentials spoken aloud, or confidential business discussions that are then transmitted to multiple external services.

### MEDIUM Severity

#### [MEDIUM] Missing allowed-tools Declaration Enables Unrestricted Execution

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill manifest does not declare allowed-tools, which means there are no restrictions on what agent tools can be used. Given that this skill runs a network-accessible server, makes external API calls, and processes real-time audio streams, it should explicitly declare its tool requirements. The absence of this declaration makes it harder for users to understand the skill's capabilities and potential security implications before activation.

#### [MEDIUM] Incomplete Security Disclosure in Skill Description

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill description focuses on functionality ('Run a real-time AI phone agent') but does not disclose critical security implications: (1) Requires exposing local server to internet via ngrok, (2) Transmits voice call audio to multiple third-party services, (3) Processes potentially sensitive phone conversations through external APIs, (4) Requires multiple paid API keys with billing implications. Users may activate this skill without understanding they are creating a publicly accessible endpoint and sharing voice data with external services.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
