# Agent Skill Security Scan Report

**Skill:** ai-pdf-builder
**Directory:** /workspace/skills/clawhub-ai-pdf-builder
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 35.26s
**Timestamp:** 2026-02-05T18:46:48.308458

## Summary

- **Total Findings:** 8
- **Critical:** 1
- **High:** 1
- **Medium:** 3
- **Low:** 3
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:37

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export ANTHROPIC_API_KEY="your-key

### HIGH Severity

#### [HIGH] Undeclared External API Dependency with Credential Requirement

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires users to set ANTHROPIC_API_KEY environment variable for AI features, but this external API dependency is not declared in the manifest. The skill will access and potentially transmit this credential to Anthropic's API without explicit disclosure in the metadata. Users may not realize their API key is being used or that their prompts/content are being sent to external servers.

### MEDIUM Severity

#### [MEDIUM] SKILL DISCOVERY ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** skill_discovery_abuse
**Rule ID:** YARA_skill_discovery_abuse
**Location:** SKILL.md:3

**Description:** Detects manipulation of skill discovery to increase unwanted activation: Perfect

#### [MEDIUM] Missing Critical Metadata Fields

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill manifest is missing several important metadata fields including 'license', 'compatibility', and 'allowed-tools'. While 'allowed-tools' is optional, its absence makes it impossible to verify whether the skill's behavior violates any declared tool restrictions. The missing license field creates legal ambiguity, and missing compatibility information prevents users from understanding platform requirements.

#### [MEDIUM] Incomplete Implementation - Missing Core Functionality

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The instruction body shows truncated code example that ends abruptly with 'fs.w', suggesting incomplete documentation or potentially missing implementation details. Additionally, 7 referenced Python files (documents.py, prompt.py, a.py, prompts.py, content.py, Markdown.py, their.py) are mentioned but not found in the package. This creates uncertainty about whether the skill is fully functional or if critical components are missing.

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

#### [LOW] Potential Resource Consumption from LaTeX Installation

**Severity:** LOW
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The skill instructs users to install large LaTeX distributions (texlive-full on Linux, collection-fontsrecommended on macOS) which can consume significant disk space (several GB) and installation time. While not a direct security threat, this could be considered a minor availability concern if users are not warned about the resource requirements upfront.

#### [LOW] Ambiguous Cloud API Reference

**Severity:** LOW
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill mentions 'Option B: Cloud API (Coming Soon)' and references 'ai-pdf-builder.com' for API keys, but provides no verification that this domain/service exists or is legitimate. This could potentially mislead users or create confusion about available features.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
