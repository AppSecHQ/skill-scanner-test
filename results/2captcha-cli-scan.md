# Agent Skill Security Scan Report

**Skill:** 2captcha
**Directory:** /workspace/skills/clawhub-2captcha
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 44.18s
**Timestamp:** 2026-02-05T17:36:47.280047

## Summary

- **Total Findings:** 5
- **Critical:** 1
- **High:** 2
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Arbitrary Code Execution via Unverified Remote Script Download

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill instructs users to download and execute a bash script directly from GitHub without any integrity verification (no checksum, no signature verification). The curl command pipes directly to a file with execute permissions. An attacker who compromises the GitHub repository or performs a man-in-the-middle attack could inject malicious code that would be executed with the user's privileges.

### HIGH Severity

#### [HIGH] Hardcoded API Key Storage in Plaintext

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs users to store their 2Captcha API key in plaintext in ~/.config/2captcha/api-key without any encryption or secure storage mechanism. API keys are credentials that provide access to paid services and should be protected. Plaintext storage exposes keys to any process or malware that can read user files.

#### [HIGH] Facilitates CAPTCHA Bypass for Potentially Malicious Purposes

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill's stated purpose is to 'bypass captchas during web automation, account creation, or form submission.' CAPTCHAs exist as security controls to prevent automated abuse (spam, credential stuffing, scraping, fake account creation). This skill explicitly enables circumventing these security measures. The description and examples promote use cases that could violate terms of service, enable fraud, or facilitate malicious automation at scale.

### MEDIUM Severity

#### [MEDIUM] Misleading Skill Description Omits Security and Legal Risks

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill description presents CAPTCHA solving as a neutral utility without disclosing significant risks: 1) Downloading unverified remote code, 2) Storing API credentials insecurely, 3) Legal/ethical implications of bypassing security controls, 4) Potential terms of service violations. Users may install this skill without understanding they are being instructed to execute arbitrary remote code and bypass website security measures.

#### [MEDIUM] Unauthorized External Tool Dependency Without Disclosure

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill relies entirely on an external binary (solve-captcha) downloaded from GitHub, but this critical dependency is not declared in the manifest. The allowed-tools field is missing, and there is no disclosure that the skill requires downloading and executing third-party code. Users cannot assess the security implications before installation.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
