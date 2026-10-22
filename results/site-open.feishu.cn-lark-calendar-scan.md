# Scan: lark-calendar

- **Verdict:** SAFE
- **Max severity:** LOW
- **Findings:** 18
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:36:11.734598+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| LOW | obfuscation | Hidden data file detected | .wellknown-origin.json |
| LOW | obfuscation | File extension does not match actual content type | SKILL.md |
| LOW | social_engineering | Skill description is too short | SKILL.md |
| INFO | policy_violation | Strict manifest load failed; inert fallback scan used | SKILL.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-calendar-create.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-calendar-join-event.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-calendar-list-attendees.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-calendar-meeting-relation.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-calendar-meeting.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-calendar-recurring.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-calendar-room-find.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-calendar-rsvp.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-calendar-schedule-clear-time.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-calendar-schedule-fuzzy-time.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-calendar-schedule-meeting.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-calendar-suggestion.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-calendar-transfer.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-calendar-update.md |
