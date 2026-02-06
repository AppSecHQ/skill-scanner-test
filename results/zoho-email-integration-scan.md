# Agent Skill Security Scan Report

**Skill:** zoho-email
**Directory:** /workspace/skills/clawhub-zoho-email-integration
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 8.65s
**Timestamp:** 2026-02-06T07:54:56.684230

## Summary

- **Total Findings:** 69
- **Critical:** 25
- **High:** 4
- **Medium:** 39
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Direct socket connection to external server

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_SOCKET_CONNECT
**Location:** scripts/zoho-email.py:1796

**Description:** Pattern detected: socket.create_connection

#### [CRITICAL] Base64 encoding (often used before data exfiltration)

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_BASE64_AND_NETWORK
**Location:** scripts/zoho-email.py:99

**Description:** Pattern detected: base64.b64encode

#### [CRITICAL] Base64 encoding (often used before data exfiltration)

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_BASE64_AND_NETWORK
**Location:** scripts/apply_oauth2.py:103

**Description:** Pattern detected: base64.b64encode

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:62

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: Export your Zoho credentials

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:500

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export credentials

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** test-app-password.sh:8

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;32m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** test-app-password.sh:9

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;31m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** test-app-password.sh:10

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[1;33m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** test-app-password.sh:11

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;34m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** test-app-password.sh:12

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/oauth-setup.py:57

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: <script>

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/oauth-setup.py:57

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: </script>

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/oauth-setup.py:57

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: setTimeout(

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/oauth-setup.py:57

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: function(

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** scripts/apply_oauth2_cli.py:131

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export ZOHO_EMAIL='your-email@domain.com'", file

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** scripts/apply_oauth2_cli.py:132

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export ZOHO_PASSWORD='your-app-specific-password'", file

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** scripts/apply_oauth2_cli.py:137

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export ZOHO_EMAIL='your-email@domain.com'", file

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** scripts/apply_oauth2_cli.py:138

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export ZOHO_PASSWORD='your-app-specific-password'", file

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** scripts/add_oauth_cli.py:114

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export ZOHO_EMAIL='your-email@domain.com'", file

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** scripts/add_oauth_cli.py:115

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export ZOHO_PASSWORD='your-app-specific-password'", file

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** scripts/add_oauth_cli.py:119

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export ZOHO_EMAIL='your-email@domain.com'", file

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** scripts/add_oauth_cli.py:120

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export ZOHO_PASSWORD='your-app-specific-password'", file

#### [CRITICAL] Environment variable access with network calls detected

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_EXFILTRATION
**Location:** skills/clawhub-zoho-email-integration/scripts/zoho-email.py

**Description:** Script accesses environment variables and makes network calls in skills/clawhub-zoho-email-integration/scripts/zoho-email.py

#### [CRITICAL] Cross-file exfiltration chain: 3 files

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_CROSSFILE_EXFILTRATION_CHAIN

**Description:** Multi-file exfiltration chain detected: examples/batch-cleanup.py, scripts/zoho-email.py collect data → scripts/zoho-email.py, scripts/oauth-setup.py → scripts/zoho-email.py, scripts/oauth-setup.py transmit to network

#### [CRITICAL] Cross-file env var exfiltration: 3 files

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_CROSSFILE_ENV_VAR_EXFILTRATION

**Description:** Environment variable access with network calls in examples/batch-cleanup.py, scripts/zoho-email.py

### HIGH Severity

#### [HIGH] Suspicious URL detected: https://mail.zoho.com/api

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-zoho-email-integration/scripts/zoho-email.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: https://accounts.zoho.com/oauth/v2/token

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-zoho-email-integration/scripts/zoho-email.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: https://accounts.zoho.com/oauth/v2/auth

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-zoho-email-integration/scripts/oauth-setup.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: https://accounts.zoho.com/oauth/v2/token

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-zoho-email-integration/scripts/oauth-setup.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

### MEDIUM Severity

#### [MEDIUM] User input used in command substitution - potential injection risk

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_USER_INPUT
**Location:** test-app-password.sh:52

**Description:** Pattern detected: eval "$

#### [MEDIUM] User input used in command substitution - potential injection risk

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_USER_INPUT
**Location:** test-batch-operations.sh:16

**Description:** Pattern detected: $(dirname "$0")

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** examples/batch-cleanup.py:163

**Description:** Pattern detected: os.environ.get('ZOHO_PASSWORD

#### [MEDIUM] HTTP client library imports that enable external communication

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_NETWORK_REQUESTS
**Location:** scripts/zoho-email.py:75

**Description:** Pattern detected: import urllib.request

#### [MEDIUM] HTTP client library imports that enable external communication

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_NETWORK_REQUESTS
**Location:** scripts/zoho-email.py:114

**Description:** Pattern detected: import requests

#### [MEDIUM] HTTP client library imports that enable external communication

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_NETWORK_REQUESTS
**Location:** scripts/zoho-email.py:141

**Description:** Pattern detected: import requests

#### [MEDIUM] HTTP client library imports that enable external communication

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_NETWORK_REQUESTS
**Location:** scripts/zoho-email.py:1808

**Description:** Pattern detected: import urllib.request

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/zoho-email.py:26

**Description:** Pattern detected: os.environ.get('ZOHO_PASSWORD

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/zoho-email.py:1768

**Description:** Pattern detected: os.environ.get("ZOHO_PASSWORD

#### [MEDIUM] HTTP client library imports that enable external communication

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_NETWORK_REQUESTS
**Location:** scripts/apply_oauth2.py:79

**Description:** Pattern detected: import urllib.request

#### [MEDIUM] HTTP client library imports that enable external communication

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_NETWORK_REQUESTS
**Location:** scripts/oauth-setup.py:99

**Description:** Pattern detected: import urllib.request

#### [MEDIUM] HTTP client library imports that enable external communication

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_NETWORK_REQUESTS
**Location:** scripts/oauth-setup.py:126

**Description:** Pattern detected: import urllib.request

#### [MEDIUM] Undeclared network usage

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_UNDECLARED_NETWORK

**Description:** Skill code uses network libraries but doesn't declare network requirement

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** examples/batch-cleanup.py:163

**Description:** Pattern detected: os.environ.get('ZOHO_PASSWORD

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:114

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: Get a specific email

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:220

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: Get Specific Email

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:332

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: Get latest email

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:365

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: Get specific email

#### [MEDIUM] SKILL DISCOVERY ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** skill_discovery_abuse
**Rule ID:** YARA_skill_discovery_abuse
**Location:** SKILL.md:201

**Description:** Detects manipulation of skill discovery to increase unwanted activation: Perfect

#### [MEDIUM] SKILL DISCOVERY ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** skill_discovery_abuse
**Rule ID:** YARA_skill_discovery_abuse
**Location:** SKILL.md:562

**Description:** Detects manipulation of skill discovery to increase unwanted activation: Perfect

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** test.sh:60

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: Get email: python3 scripts/zoho-email

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** examples/attachment-demo.py:73

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: Get attachments for this email

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/zoho-email.py:4

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: Read, Search, Monitor, Send

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/zoho-email.py:183

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: GET, POST

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/zoho-email.py:357

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: get('email', EMAIL

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/zoho-email.py:641

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: get('email') or EMAIL

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/zoho-email.py:922

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: Get a specific email

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/zoho-email.py:1669

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: Get unread:      python3 zoho-email

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/zoho-email.py:1670

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: Get email:       python3 zoho-email

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/zoho-email.py:1678

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: read:    python3 zoho-email

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/zoho-email.py:1718

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: Get unread:      python3 zoho-email

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/zoho-email.py:1719

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: Get email:       python3 zoho-email

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/zoho-email.py:1728

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: read:    python3 zoho-email

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/zoho-email.py:1788

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: get("email

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/apply_oauth2.py:16

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: Read, Search, Monitor, Send

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/apply_oauth2.py:20

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: Read, Search, Monitor, Send

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/apply_oauth2.py:201

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: get('email') or EMAIL

#### [MEDIUM] Environment variable harvesting detected

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_HARVESTING
**Location:** skills/clawhub-zoho-email-integration/examples/batch-cleanup.py

**Description:** Script iterates through environment variables in skills/clawhub-zoho-email-integration/examples/batch-cleanup.py

#### [MEDIUM] Environment variable harvesting detected

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_HARVESTING
**Location:** skills/clawhub-zoho-email-integration/scripts/zoho-email.py

**Description:** Script iterates through environment variables in skills/clawhub-zoho-email-integration/scripts/zoho-email.py

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
