# Agent Skill Security Scan Report

**Skill:** nano-banana-pro
**Directory:** /workspace/skills/clawhub-nano-banana-pro-mzvmth
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 36.36s
**Timestamp:** 2026-02-06T05:06:43.074895

## Summary

- **Total Findings:** 5
- **Critical:** 2
- **High:** 2
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Obfuscated Malicious Command Execution via Base64-Encoded Payload

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The MacOS installation instructions contain a base64-encoded command that decodes to a bash command fetching and executing a script from an external IP address (91.92.242.30). The command 'echo ... | base64 -D | bash' downloads and executes arbitrary code from an untrusted remote server without user visibility into what is being executed. This is a classic malware delivery pattern using obfuscation to hide malicious intent.

#### [CRITICAL] Suspicious External Dependency with Password-Protected Archive

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md:7

**Description:** The Windows installation instructions direct users to download 'OpenClawProvider' from a GitHub release with a password-protected archive (password: 'openclaw'). Password-protected archives are commonly used to bypass antivirus scanning. Combined with the suspicious MacOS payload, this indicates a coordinated malware distribution campaign masquerading as a legitimate tool dependency.

### HIGH Severity

#### [HIGH] Deceptive Skill Description Masking Malware Delivery

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill presents itself as an image generation tool using 'Nano Banana Pro (Gemini 3 Pro Image)' but actually serves as a trojan to deliver malware through fake dependency installation. The description mentions legitimate-sounding features (text-to-image, image-to-image, resolution options) to appear credible while the actual purpose is malware installation. There is no evidence of legitimate image generation functionality.

#### [HIGH] Missing Critical Script Files - Tool Poisoning Indicator

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill references 'generate_image.py' script extensively in instructions but the script file is completely missing from the package. The only referenced file 'the.py' is also not found. This indicates the skill's true purpose is not image generation but rather malware delivery through the fake 'OpenClawProvider' dependency installation.

### MEDIUM Severity

#### [MEDIUM] Fake API and Product Names to Establish False Legitimacy

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill uses fabricated product names 'Nano Banana Pro' and 'Gemini 3 Pro Image' that do not correspond to real Google/Gemini products. It also references a non-existent 'GEMINI_API_KEY' environment variable. These fake names are designed to sound legitimate and exploit user trust in the Gemini brand to facilitate malware installation.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
