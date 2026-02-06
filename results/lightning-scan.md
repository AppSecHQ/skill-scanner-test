# Agent Skill Security Scan Report

**Skill:** lightning
**Directory:** /workspace/skills/clawhub-lightning
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 78.65s
**Timestamp:** 2026-02-06T03:59:07.893269

## Summary

- **Total Findings:** 10
- **Critical:** 2
- **High:** 2
- **Medium:** 3
- **Low:** 3
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Hardcoded Credentials and Secrets in Configuration File

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires users to store highly sensitive financial credentials (Lightning node macaroons, runes, API keys, seed phrases) in a plaintext JSON configuration file at ~/.lightning-config.json. This includes admin macaroons for LND, rune tokens for CLN, Breez API keys, and 12-word seed phrases for Spark wallets. These credentials provide full control over Lightning wallets and funds. Storing them in plaintext creates multiple attack vectors: file system access by malicious processes, accidental exposure through backups, and potential exfiltration by other compromised skills or malware.

#### [CRITICAL] Unbounded Autonomous Financial Transactions Without User Confirmation

**Severity:** CRITICAL
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The skill provides a '/lightning pay' command that can execute financial transactions autonomously without requiring explicit user confirmation for each payment. While there is a '/lightning confirm' command, the instructions do not enforce its use or implement safeguards to prevent the agent from using the direct 'pay' command. An agent with this skill could be manipulated through prompt injection to send payments without user awareness, especially in multi-turn conversations where context could be exploited. The skill operates in 'RECKLESS MODE' with acknowledged dangers but lacks technical controls to prevent autonomous spending.

### HIGH Severity

#### [HIGH] Missing Binary Integrity Verification for Downloaded Executable

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The installation process downloads a prebuilt native binary from GitHub Releases using 'npm run download' without any documented integrity verification (checksum validation, signature verification, or hash checking). This creates a supply chain attack vector where a compromised binary could be downloaded and executed with full access to Lightning wallet credentials. The binary will have access to the plaintext configuration file containing sensitive financial credentials. Without integrity checks, users cannot verify they are running authentic, unmodified code.

#### [HIGH] Inadequate Risk Disclosure and Social Engineering Through Normalization

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** While the skill includes a warning about 'RECKLESS MODE', the overall presentation normalizes extremely dangerous behavior by providing detailed setup instructions and a polished interface for giving an AI agent autonomous access to financial accounts. The warning is presented as a disclaimer rather than a technical control. The skill's description and branding (emoji, professional documentation, PlebLab attribution) create a false sense of legitimacy and safety. Users may underestimate risks due to the professional presentation, especially less technical users who may not fully understand the implications of giving an AI bot wallet access.

### MEDIUM Severity

#### [MEDIUM] Unrestricted Tool Access Without Declared Constraints

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill manifest does not declare 'allowed-tools', leaving tool usage unrestricted. Given that this skill manages financial transactions and credentials, it should explicitly declare which agent tools it requires (likely Bash for executing the LNI binary, Read for configuration files). Without declared restrictions, the skill could potentially use Write, Grep, Glob, or Python tools in ways not intended by the user, creating additional attack surface. For a financial skill handling sensitive credentials, explicit tool restrictions are a critical security boundary.

#### [MEDIUM] Command Injection Risk Through Unvalidated Payment Destinations

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill accepts various payment destination formats (BOLT11, BOLT12, Lightning addresses, LNURL, contact names) as user input that will be passed to the LNI binary. Without visible input validation or sanitization in the instructions, there is potential for command injection if the LNI binary or shell execution does not properly handle malicious input. An attacker could craft a payment destination string containing shell metacharacters or escape sequences that could be executed when passed to the binary via Bash tool.

#### [MEDIUM] Insecure TLS Configuration with Certificate Validation Bypass

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The configuration examples for CLN and LND backends include 'acceptInvalidCerts: true', which disables TLS certificate validation. This makes the connection vulnerable to man-in-the-middle attacks where an attacker could intercept Lightning node communications, potentially capturing credentials (runes, macaroons) or manipulating payment data. For financial transactions, disabling certificate validation is a critical security flaw that undermines the entire security model of HTTPS connections.

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

#### [LOW] Missing License and Compatibility Metadata

**Severity:** LOW
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill manifest does not specify a license or compatibility information. For a financial skill that handles real money and sensitive credentials, clear licensing terms are important for liability and usage rights. Compatibility information helps users understand which environments are safe to use the skill in. The absence of this metadata reduces transparency and may lead to inappropriate usage contexts.

#### [LOW] Incomplete Installation Documentation for Referenced Files

**Severity:** LOW
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md:120

**Description:** The instructions reference 'your.py' and 'Breez.py' files that are not found in the skill package. The documentation appears incomplete, particularly around Spark wallet provisioning ('If the user does' sentence is cut off). This incomplete documentation could lead to misconfiguration, security mistakes during setup, or users running partially configured systems that may behave unpredictably with financial credentials.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
