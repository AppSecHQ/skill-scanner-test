---
title: "Request a scan"
description: "How to ask skillscan.io to scan a public GitHub repository of AI agent skills, what the pipeline runs, what it skips, and where the results end up."
slug: request-a-scan
updated: 2026-10-21
---

Anyone can request a scan of a public GitHub repository that contains one or more `SKILL.md` files. Requests go through a GitHub Issue so there is a public record of who asked, who approved, and what the scanner returned.

## How to request

1. Open a new issue using the **Scan Request** template: [github.com/AppSecHQ/skill-scanner-test/issues/new/choose](https://github.com/AppSecHQ/skill-scanner-test/issues/new/choose).
2. Fill in the repository URL and a one-line reason, and tick the acknowledgement box. The template applies the `scan-request` label.
3. Wait for a maintainer to comment `/approve`. Only listed maintainers can approve; anyone else's `/approve` is rejected with a comment and nothing runs.
4. The scan runs in GitHub Actions. Results are posted as a comment on the issue, the issue is closed with the `scan-completed` label, and a pull request adds the results to the dataset. Once merged, the skills appear on this site.

If the scan fails, the issue gets the `scan-failed` label and a comment linking to the workflow run. Common reasons: the repository is private, has no `SKILL.md`, exceeds the size limit, or the scan exceeded the time limit.

## What the community scan runs

- Static, behavioral, and trigger analyzers from cisco-ai-skill-scanner.
- A shallow clone only, after checking the repository's reported size against a 500 MB limit.
- One scan at a time, gated by a protected environment that requires a maintainer to approve the job in the GitHub UI as well as on the issue.

## What it does not run

The LLM and meta analyzers are **disabled** for community-requested scans. The scanner feeds `SKILL.md` content to a model, and a crafted skill could use that path to try to extract the API key. Operator-run scans from the command line use the full pipeline, which is why some skills on this site show `llm` and `meta` in their analyzer list and community-scanned ones do not. The skill page lists exactly which analyzers ran.

## Rate limits and duplicates

There is no per-user quota yet. Each request consumes Actions minutes, so duplicate or frivolous requests are closed without a scan. Re-scans of a skill already in the dataset are welcome when the upstream repository has changed; the new result is added to that skill's scan history rather than replacing it.

## Reporting a wrong finding

If a finding on a skill page is wrong, open an issue with the skill name, the finding title, and why it is a false positive. Confirmed cases are added to the [false-positive register](/research/2026/false-positive-register/).
