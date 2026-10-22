# Scan: lark-im

- **Verdict:** SAFE
- **Max severity:** LOW
- **Findings:** 64
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:36:14.749009+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| LOW | obfuscation | Hidden data file detected | .wellknown-origin.json |
| LOW | obfuscation | File extension does not match actual content type | SKILL.md |
| LOW | social_engineering | Skill description is too short | SKILL.md |
| INFO | policy_violation | Strict manifest load failed; inert fallback scan used | SKILL.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/card-2.0-schema.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/components/button.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/components/chart.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/components/checker.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/components/collapsible_panel.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/components/column_set.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/components/date_picker.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/components/div.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/components/form.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/components/header.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/components/hr.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/components/img.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/components/img_combination.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/components/input.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/components/interactive_container.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/components/markdown.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/components/multi_select_person.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/components/multi_select_static.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/components/overflow.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/components/person.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/components/person_list.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/components/picker_datetime.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/components/picker_time.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/components/recycling_container.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/components/select_img.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/components/select_person.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/components/select_static.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/components/table.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/lark-im-card-create.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/lark-im-card-style.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/resource/colors.md |
| LOW | obfuscation | File extension does not match actual content type | references/card/resource/icons.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-im-card-action-reply.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-im-chat-create.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-im-chat-identity.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-im-chat-list.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-im-chat-members-list.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-im-chat-messages-list.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-im-chat-search.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-im-chat-update.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-im-feed-group-list-item.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-im-feed-group-list.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-im-feed-group-query-item.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-im-feed-groups.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-im-feed-shortcut-create.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-im-feed-shortcut-list.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-im-feed-shortcut-remove.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-im-flag-cancel.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-im-flag-create.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-im-flag-list.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-im-message-enrichment.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-im-message-read-status.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-im-messages-edit.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-im-messages-mget.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-im-messages-reply.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-im-messages-resources-download.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-im-messages-search.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-im-messages-send.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-im-reactions.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-im-threads-messages-list.md |
