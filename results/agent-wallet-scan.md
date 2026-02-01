# Agent Skill Security Scan Report

**Skill:** Agent Wallet
**Directory:** ./skills/clawhub-agent-wallet
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 52.39s
**Timestamp:** 2026-02-01T07:18:54.136174

## Summary

- **Total Findings:** 9
- **Critical:** 2
- **High:** 2
- **Medium:** 2
- **Low:** 3
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Hardcoded API Key Exposure and Credential Theft Risk

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires users to store and use API keys as Bearer tokens for all wallet operations. The instructions explicitly tell users to 'store this securely' but then require passing it in plaintext via curl commands. The API key provides full access to the agent's wallet and all transaction capabilities. If the agent logs these commands or the API key is exposed in chat history, it could be stolen and used to drain the wallet. Additionally, the skill creates server-side private keys that users 'never see', creating a custodial trust model where the remote server (safeskill-production.up.railway.app) has complete control over funds.

#### [CRITICAL] Data Exfiltration to External Server with Financial Access

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** All wallet operations (balance checks, transfers, smart contract interactions) send requests to an external server (safeskill-production.up.railway.app) with full transaction authority. The skill creates a custodial wallet where private keys are generated and stored server-side, meaning the external service has complete control over user funds. This creates multiple exfiltration risks: (1) The server can access all wallet data, (2) The server can execute unauthorized transactions, (3) API keys transmitted to the server provide persistent access, (4) No verification that the server is trustworthy or audited.

### HIGH Severity

#### [HIGH] Deceptive Description - Custodial Wallet Misrepresented as Safe

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill description claims 'Use this skill to create a wallet the agent can safely use for EVM chains, without ever exposing the private keys' and 'The agent never sees the private key.' While technically true that the agent doesn't see the key, this is highly misleading because: (1) The private keys are generated and stored on a remote server the user doesn't control, (2) The server has complete access to funds and can execute any transaction, (3) Users must trust an external third party (safeskill-production.up.railway.app) with their funds, (4) This is a custodial wallet, not a non-custodial 'safe' solution. The description creates a false sense of security by emphasizing what the agent can't see while hiding that a remote server has full control.

#### [HIGH] Missing Referenced Script File - Broken Tool Implementation

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The instructions reference a file 'wallet.py' that is not included in the skill package. This creates multiple security concerns: (1) The skill cannot function as described, (2) Users may be directed to download the missing file from an external source, creating supply chain risks, (3) The actual implementation is unknown and unauditable, (4) This could be tool shadowing where the real implementation differs from documentation.

### MEDIUM Severity

#### [MEDIUM] Environment Variable Injection Risk

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill uses environment variables (SAFESKILLS_API_URL and SAFESKILLS_FRONTEND_URL) to determine API endpoints without validation. An attacker who can control the agent's environment variables could redirect all wallet operations to a malicious server, enabling: (1) API key theft, (2) Transaction interception, (3) Phishing attacks via fake claim URLs, (4) Complete wallet compromise. The instructions show these variables being used in curl commands without any validation or allowlisting of acceptable domains.

#### [MEDIUM] No Rate Limiting or Transaction Safeguards

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The skill provides direct transaction capabilities (transfers, smart contract interactions) without any documented rate limiting, spending limits, or safeguards. An agent could potentially: (1) Execute unlimited transactions draining the wallet, (2) Make repeated failed transactions wasting gas, (3) Be manipulated into making unauthorized transfers, (4) Execute transactions without user confirmation. While the description mentions 'spending policies', there's no documentation of how these work or what protections they provide.

### LOW Severity

#### [LOW] Skill name does not follow agent skills naming rules

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_INVALID_NAME
**Location:** SKILL.md

**Description:** Skill name 'Agent Wallet' is invalid. Agent skills require lowercase letters, numbers, and hyphens only, with a maximum length of 64 characters.

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

#### [LOW] Missing Security Metadata - No License or Compatibility Information

**Severity:** LOW
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill manifest is missing critical metadata fields: (1) No license specified - unclear usage rights and liability, (2) No compatibility information - unclear which environments are safe, (3) No allowed-tools specified - no restrictions on agent capabilities, (4) No version information - cannot track updates or security patches. This lack of metadata makes it difficult to assess the skill's trustworthiness and proper usage context.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
