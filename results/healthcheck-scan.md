# Agent Skill Security Scan Report

**Skill:** health-tracker
**Directory:** /workspace/skills/clawhub-healthcheck
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 36.46s
**Timestamp:** 2026-02-06T02:56:25.455667

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 1
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Unbounded Autonomous Reminder System

**Severity:** HIGH
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The skill implements an autonomous reminder system that operates continuously without user confirmation or clear termination conditions. The instructions describe 'auto-log' functionality that automatically records entries after 15 minutes of no response, and a smart reminder system that 'automatically adjusts cycle based on habits'. This creates an unbounded autonomous loop that could consume resources indefinitely and operate without explicit user control.

### MEDIUM Severity

#### [MEDIUM] Persistent Data Storage Without Privacy Controls

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill stores health tracking data (water intake timestamps, sleep patterns) in a local JSON file ('health-data.json') without any mention of data privacy, retention policies, or user control over data deletion. Health data is sensitive personal information, and the skill provides no mechanism for users to export, delete, or control their data beyond viewing statistics.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
