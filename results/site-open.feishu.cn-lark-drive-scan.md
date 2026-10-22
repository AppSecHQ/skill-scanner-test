# Scan: lark-drive

- **Verdict:** SAFE
- **Max severity:** LOW
- **Findings:** 64
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:36:13.060954+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| LOW | obfuscation | Hidden data file detected | .wellknown-origin.json |
| LOW | obfuscation | File extension does not match actual content type | SKILL.md |
| LOW | social_engineering | Skill description is too short | SKILL.md |
| INFO | policy_violation | Strict manifest load failed; inert fallback scan used | SKILL.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-add-comment.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-add-reply.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-apply-permission.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-batch-query-comments.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-comment-content.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-comment-location.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-copy.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-cover.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-create-folder.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-create-shortcut.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-delete-reply.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-delete.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-download.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-export-download.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-export.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-files-list.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-import.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-inspect.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-list-comments.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-list-replies.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-member-add.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-member-list.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-member-remove.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-move.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-permission-get-setting.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-permission-guide.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-preview.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-pull.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-push.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-react-reply.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-reactions.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-resolve-comment.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-restore-comment.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-search.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-secure-label.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-status.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-task-result.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-update-reply.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-update-title.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-upload.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-version-delete.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-version-get.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-version-history.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-version-revert.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-workflow-knowledge-organize-analysis.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-workflow-knowledge-organize-discovery.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-workflow-knowledge-organize-execution.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-workflow-knowledge-organize-planning.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-workflow-knowledge-organize-rollback.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-workflow-knowledge-organize.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-workflow-permission-governance-commands.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-workflow-permission-governance-outputs.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-workflow-permission-governance.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-workflow-topic-move-collector-execute.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-workflow-topic-move-collector-recall.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-workflow-topic-move-collector-resolve-verify.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-workflow-topic-move-collector-review-plan.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-workflow-topic-move-collector-setup.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-workflow-topic-move-collector.md |
| LOW | obfuscation | File extension does not match actual content type | references/lark-drive-workflow.md |
