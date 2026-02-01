# Agent Skill Security Scan Report

**Skill:** browser-use
**Directory:** ./skills/browser-use-browser-use/skills/browser-use
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 43.57s
**Timestamp:** 2026-02-01T09:42:52.124662

## Summary

- **Total Findings:** 4
- **Critical:** 0
- **High:** 2
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Unrestricted Browser Automation with External Command Execution

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill grants unrestricted browser automation capabilities through the browser-use CLI tool, which can navigate to arbitrary URLs, execute JavaScript, interact with web pages, and access user's authenticated browser sessions. The allowed-tools restriction 'Bash(browser-use:*)' permits execution of any browser-use command without validation of target URLs or actions. This enables potential data exfiltration, credential theft via phishing sites, and unauthorized actions on authenticated web services.

#### [HIGH] Authenticated Session Access and Credential Exposure Risk

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The 'real' browser mode explicitly accesses the user's Chrome browser with all cookies, extensions, and logged-in sessions. This provides the skill with access to authenticated sessions across all websites where the user is logged in (email, banking, social media, etc.). Combined with screenshot and state extraction capabilities, this creates a direct path for credential theft and session hijacking.

### MEDIUM Severity

#### [MEDIUM] Data Exfiltration via Screenshot and State Commands

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill can extract page content through 'browser-use state' (returns all page elements and text) and 'browser-use screenshot' (captures visual content as base64). When combined with navigation to arbitrary URLs and form interaction capabilities, this enables systematic data harvesting from any accessible web page, including sensitive information displayed in authenticated sessions.

#### [MEDIUM] Arbitrary Form Submission and Web Interaction Without Validation

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill can interact with any web form through click, type, input, and select commands without validation of target sites or data being submitted. This enables unauthorized actions on behalf of the user including form submissions, button clicks, and data entry on any website. Combined with authenticated session access, this could perform unauthorized transactions, posts, or account modifications.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
