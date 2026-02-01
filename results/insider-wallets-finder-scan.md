# Agent Skill Security Scan Report

**Skill:** insider-wallets-finder
**Directory:** ./skills/clawhub-insider-wallets-finder-gxgfy
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 45.05s
**Timestamp:** 2026-02-01T18:56:48.534350

## Summary

- **Total Findings:** 6
- **Critical:** 2
- **High:** 2
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Malicious Binary Download with Social Engineering

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill instructs users to download and execute an untrusted binary (openclaw-agent.zip) from GitHub with password-protected extraction. This is a classic malware distribution pattern disguised as a legitimate prerequisite. The password protection ('openclaw') is used to bypass antivirus scanning. The binary's true purpose cannot be verified, and it could contain arbitrary malicious code including ransomware, keyloggers, or backdoors.

#### [CRITICAL] Remote Code Execution via Untrusted Script

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md:9

**Description:** The macOS installation directs users to visit an external URL (glot.io/snippets/hfdxv8uyaf) and execute arbitrary code directly in Terminal. This is a remote code execution attack vector where the attacker controls the script content. The script could perform any malicious action including data exfiltration, credential theft, backdoor installation, or system compromise. Users are instructed to blindly execute this code without review.

### HIGH Severity

#### [HIGH] API Key Exposure and Credential Harvesting Pattern

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill repeatedly instructs users to insert their API keys directly into bash commands and Python scripts (Etherscan API keys, Birdeye API keys). These keys are exposed in command history, process listings, and potentially logged. The skill creates a pattern where users become accustomed to pasting sensitive credentials into untrusted code, which could be exploited by the malicious binaries to harvest these credentials.

#### [HIGH] Deceptive Skill Description Masking Malware Distribution

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill presents itself as a legitimate blockchain analysis tool ('Find and analyze smart money addresses') but its primary purpose is to trick users into downloading and executing malicious binaries. The actual blockchain analysis code is secondary to the malware distribution mechanism. This is social engineering designed to exploit users' trust in the agent skills ecosystem.

### MEDIUM Severity

#### [MEDIUM] Unbounded API Calls Without Rate Limiting

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The skill makes multiple API calls to external services (Etherscan, Birdeye, TheGraph) without any rate limiting, error handling, or retry logic. This could lead to API quota exhaustion, service bans, or denial of service if executed repeatedly. The code also lacks timeout configurations, potentially causing hanging processes.

#### [MEDIUM] Unsafe JSON Parsing and Code Injection Risk

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill uses python3 -c with inline scripts that parse JSON from untrusted API responses without validation. The json.load(sys.stdin) pattern combined with direct execution of API response data could lead to code injection if API responses are compromised or contain malicious payloads. Additionally, the use of eval-like patterns in inline Python increases attack surface.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
