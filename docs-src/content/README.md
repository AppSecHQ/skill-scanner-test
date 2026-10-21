# Site content

Markdown source for the static pages on skillscan.io. The generator in `scripts/build_site.py` renders every `.md` here.

## Frontmatter contract

```yaml
---
title: "Page title (used for <title> and H1)"
description: "One sentence, 140-160 chars, used for meta description and OG"
slug: "url-segment"          # optional; defaults to filename without date prefix
date: 2026-10-21             # required for research/, optional elsewhere
updated: 2026-10-21          # optional
order: 1                     # optional; sort key within a section for nav
tags: [a, b]                 # research/ only
---
```

## Sections

| Directory | Renders to | Notes |
|---|---|---|
| `methodology/index.md` | `/methodology/` | |
| `about/index.md` | `/about/` | |
| `learn/<slug>.md` | `/learn/<slug>/` | `order` controls nav |
| `scanners/index.md` | `/scanners/` | |
| `data/index.md` | `/data/` | |
| `research/YYYY-MM-DD-<slug>.md` | `/research/YYYY/<slug>/` | date prefix sets the year; legacy posts come from `docs/notes.json` |

Body is CommonMark. Tables and fenced code are expected. Links to other site pages are root-relative (`/categories/data-exfiltration/`). Category and registry pages are not authored here; they render from `docs/data/categories.json` and `docs/data/summary.json`.

Numbers quoted in pages are as of the scan run named in `docs/data/summary.json` (`scan_date`). Pages that quote counts should say "as of <date>" so they do not go silently stale.
