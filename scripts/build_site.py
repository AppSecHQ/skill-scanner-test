#!/usr/bin/env python3
"""Generate the static skillscan.io site into docs/.

Inputs:  docs/data/summary.json, docs/data/scans/*.json, docs-src/data/categories.json,
         docs/notes.json, docs-src/content/**/*.md, docs-src/static/*, docs-src/legacy/*
Outputs: HTML pages with real URLs, sitemap.xml, robots.txt, feed.xml, 404.html,
         badge/<slug>.svg, data/slugs.json, data/redirects.json

Usage: python scripts/build_site.py [--root .] [--base-url https://skillscan.io]
"""
from __future__ import annotations

import argparse
import html
import json
import logging
import shutil
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

sys.path.insert(0, str(Path(__file__).parent))
from sitegen.loaders import SEVERITY_ORDER, Skill, load_categories, load_content, load_notes, load_skills  # noqa: E402
from sitegen.slugs import ascii_slug  # noqa: E402

logger = logging.getLogger("build_site")

SITE_NAME = "skillscan.io"
DEFAULT_BASE_URL = "https://skillscan.io"
GENERATED_DIRS = ["skills", "categories", "registries", "research", "badge", "learn", "app"]
LEGACY_DIR = "app"  # old SPA served at /app/ during the cutover window; noindex, not in sitemap
PROTECTED_DIRS = {"data", "notes_draft"}  # never rmtree these under docs/
SEVERITY_COLORS = {"CRITICAL": "#f87171", "HIGH": "#fb923c", "MEDIUM": "#facc15", "LOW": "#60a5fa", "SAFE": "#4ade80"}

ANALYZER_BLURBS = {
    "static_analyzer": "Pattern rules over SKILL.md and bundled files: known-bad commands, exfiltration URLs, secrets, obfuscation.",
    "behavioral_analyzer": "Checks what the skill asks the agent to do against what its description claims it does.",
    "trigger_analyzer": "Looks for instructions that fire on conditions the user did not ask for.",
    "llm_analyzer": "A language model reads the skill and reports intent-level issues the rules cannot express.",
    "meta_analyzer": "A second model pass that validates, deduplicates and re-scores the other analyzers' findings.",
}


# --------------------------------------------------------------------------- helpers
def fmt_date(value) -> str:
    if not value:
        return "unknown"
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00")).strftime("%Y-%m-%d")
    except ValueError:
        return str(value)[:10]


def md_to_html(text: str) -> str:
    return markdown.markdown(text, extensions=["tables", "fenced_code", "toc", "attr_list"], output_format="html")


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def badge_svg(label: str, value: str, color: str) -> str:
    lw = 6 * len(label) + 12
    vw = 6 * len(value) + 12
    w = lw + vw
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="20" role="img" aria-label="{html.escape(label)}: {html.escape(value)}">'
        f'<rect width="{lw}" height="20" fill="#555"/><rect x="{lw}" width="{vw}" height="20" fill="{color}"/>'
        f'<g fill="#fff" font-family="Verdana,DejaVu Sans,sans-serif" font-size="11" text-anchor="middle">'
        f'<text x="{lw / 2}" y="14">{html.escape(label)}</text>'
        f'<text x="{lw + vw / 2}" y="14" fill="#111">{html.escape(value)}</text></g></svg>'
    )


def severity_breakdown(skill: Skill) -> str:
    """'27 critical, 47 medium, 1 info' including INFO, which severity_counts omits."""
    counts = Counter((f.get("severity") or "INFO").upper() for f in skill.findings)
    order = ["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFO"]
    return ", ".join(f"{counts[k]} {k.lower()}" for k in order if counts.get(k))


def summary_sentence(skill: Skill) -> str:
    when = fmt_date(skill.timestamp)
    times = f"{skill.scan_count} time{'s' if skill.scan_count != 1 else ''}"
    if skill.findings_count == 0:
        return f"No security findings. Scanned {times}, most recently {when}."
    parts = severity_breakdown(skill)
    cats = ", ".join(k.replace("_", " ") for k in skill.categories[:3])
    lead = "Verdict safe, but " if skill.is_safe else ""
    return (
        f"{lead}{skill.findings_count} finding{'s' if skill.findings_count != 1 else ''}"
        f"{' (' + parts + ')' if parts else ''}"
        f"{', mainly ' + cats if cats else ''}. Most recent scan {when}."
    )


# --------------------------------------------------------------------------- aggregates
def build_registries(skills: list[Skill], cat_by_key: dict) -> list[dict]:
    groups: dict[str, list[Skill]] = defaultdict(list)
    for s in skills:
        groups[s.source].append(s)
    out = []
    for key, members in groups.items():
        sev = Counter()
        cats = Counter()
        for s in members:
            for k, v in s.severity_counts.items():
                sev[k] += v
            for f in s.findings:
                if f.get("category"):
                    cats[f["category"]] += 1
        repo_urls = Counter(s.repo_url for s in members if s.repo_url)
        out.append(
            {
                "key": key,
                "slug": ascii_slug(key),
                "url": f"/registries/{ascii_slug(key)}/",
                "skills": sorted(members, key=lambda s: (-SEVERITY_ORDER.get(s.max_severity, -1), -s.findings_count, s.name)),
                "skill_count": len(members),
                "flagged": sum(1 for s in members if s.is_safe is False),
                "total_findings": sum(s.findings_count for s in members),
                "severity_counts": {k: sev.get(k, 0) for k in ("CRITICAL", "HIGH", "MEDIUM", "LOW")},
                "categories": sorted(
                    ({**cat_by_key[k], "count": n} for k, n in cats.items() if k in cat_by_key),
                    key=lambda c: -c["count"],
                ),
                "top": [s for s in members if s.findings_count][:10] if members else [],
                "repo_url": repo_urls.most_common(1)[0][0] if len(repo_urls) == 1 else None,
            }
        )
        out[-1]["top"] = sorted(members, key=lambda s: (-SEVERITY_ORDER.get(s.max_severity, -1), -s.findings_count))[:10]
    return sorted(out, key=lambda r: -r["skill_count"])


def category_context(cat: dict, skills: list[Skill], registries: list[dict]) -> dict:
    affected = []
    sev = Counter()
    by_reg_f = Counter()
    by_reg_s = Counter()
    examples = []
    for s in skills:
        hits = [f for f in s.findings if f.get("category") == cat["key"]]
        if not hits:
            continue
        affected.append(s)
        by_reg_s[s.source] += 1
        by_reg_f[s.source] += len(hits)
        for f in hits:
            sev[(f.get("severity") or "INFO").upper()] += 1
        best = max(hits, key=lambda f: (SEVERITY_ORDER.get(f.get("severity"), -1), bool(f.get("snippet")), len(f.get("description") or "")))
        if best.get("snippet") and best.get("description"):
            examples.append({"skill": s, "finding": best})
    examples.sort(key=lambda e: -SEVERITY_ORDER.get(e["finding"].get("severity"), -1))
    reg_url = {r["key"]: r["url"] for r in registries}
    return {
        "affected": affected,
        "severity_counts": {k: sev[k] for k in ("CRITICAL", "HIGH", "MEDIUM", "LOW", "INFO") if sev[k]},
        "by_registry": sorted(
            ({"key": k, "url": reg_url.get(k, "/registries/"), "findings": by_reg_f[k], "skills": by_reg_s[k]} for k in by_reg_s),
            key=lambda r: -r["findings"],
        ),
        "examples": examples[:4],
    }


def related_skills(skill: Skill, skills: list[Skill], limit: int = 6) -> list[Skill]:
    top_cat = skill.categories[0] if skill.categories else None
    same_cat = [s for s in skills if s is not skill and top_cat and top_cat in s.categories[:1]]
    same_src = [s for s in skills if s is not skill and s.source == skill.source and s not in same_cat]
    return (same_cat[: limit // 2] + same_src)[:limit]


# --------------------------------------------------------------------------- build
class SiteBuilder:
    def __init__(self, root: Path, base_url: str = DEFAULT_BASE_URL) -> None:
        self.root = root
        self.docs = root / "docs"
        self.data = self.docs / "data"
        self.src = root / "docs-src"
        self.base_url = base_url.rstrip("/")
        self.env = Environment(
            loader=FileSystemLoader(Path(__file__).parent / "sitegen" / "templates"),
            autoescape=select_autoescape(["html"]),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        self.env.filters["date"] = fmt_date
        self.env.filters["slug"] = ascii_slug
        self.pages: list[dict] = []  # for sitemap: url, lastmod

    def load(self) -> None:
        self.summary, self.skills, self.slug_map = load_skills(self.data)
        self.categories = load_categories(self.data, self.summary)
        self.cat_by_key = {c["key"]: c for c in self.categories}
        self.notes = load_notes(self.docs)
        self.content = load_content(self.src / "content")
        for f in (f for s in self.skills for f in s.findings):
            f["severity_rank"] = SEVERITY_ORDER.get((f.get("severity") or "").upper(), -1)
        self.registries = build_registries(self.skills, self.cat_by_key)
        versions = sorted({s.scanner_version for s in self.skills if s.scanner_version})
        self.site = {
            "name": SITE_NAME,
            "base_url": self.base_url,
            "scan_date": fmt_date(self.summary.get("scan_date")),
            "skill_count": len(self.skills),
            "scan_count": sum(s.scan_count for s in self.skills),
            "scanner_versions": versions,
        }
        for c in self.categories:
            c["affected_count"] = sum(1 for s in self.skills if c["key"] in s.categories)

    def render(self, template: str, out_path: str, page: dict, **ctx) -> None:
        page.setdefault("url", out_path if out_path.endswith("/") else out_path)
        page.setdefault("description", f"{SITE_NAME}: security scan results for AI agent skills.")
        page.setdefault("jsonld", None)
        tpl = self.env.get_template(template)
        html_out = tpl.render(site=self.site, page=page, summary=self.summary, categories=self.categories,
                              registries=self.registries, cat_by_key=self.cat_by_key, analyzer_blurbs=ANALYZER_BLURBS, **ctx)
        target = self.docs / out_path.lstrip("/")
        if out_path.endswith("/"):
            target = target / "index.html"
        write(target, html_out)
        if not page.get("noindex"):
            self.pages.append({"url": page["url"], "lastmod": page.get("lastmod") or self.site["scan_date"]})

    def breadcrumbs(self, *crumbs: tuple[str, str]) -> list[dict]:
        return [{"name": "Home", "url": "/"}] + [{"name": n, "url": u} for n, u in crumbs]

    def jsonld_breadcrumbs(self, crumbs: list[dict]) -> dict:
        return {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": c["name"], "item": self.base_url + c["url"]}
                for i, c in enumerate(crumbs)
            ],
        }

    # ---- pages
    def build_home(self) -> None:
        recent_critical = sorted(
            (s for s in self.skills if s.severity_counts["CRITICAL"]),
            key=lambda s: (s.timestamp or "", s.severity_counts["CRITICAL"]), reverse=True,
        )[:5]
        posts = self.all_posts()[:3]
        self.render("home.html", "/", {
            "title": "skillscan.io: security scan results for AI agent skills",
            "description": f"Security scan results for {len(self.skills)} AI agent skills from skills.sh, ClawHub and other registries, with per-skill findings, scan history and a downloadable dataset.",
            "section": "home",
            "jsonld": {
                "@context": "https://schema.org", "@type": "WebSite", "name": SITE_NAME, "url": self.base_url + "/",
                "potentialAction": {"@type": "SearchAction", "target": f"{self.base_url}/skills/?q={{search_term_string}}", "query-input": "required name=search_term_string"},
            },
        }, recent_critical=recent_critical, latest_posts=posts)

    def build_skills(self) -> None:
        crumbs = self.breadcrumbs(("Skills", "/skills/"))
        self.render("skills_index.html", "/skills/", {
            "title": f"All {len(self.skills)} scanned AI agent skills | skillscan.io",
            "description": f"Sortable security scan results for {len(self.skills)} AI agent skills across {len(self.registries)} registries: verdict, severity counts and findings per skill.",
            "section": "skills", "breadcrumbs": crumbs, "jsonld": self.jsonld_breadcrumbs(crumbs),
        }, skills=self.skills)
        for s in self.skills:
            crumbs = self.breadcrumbs(("Skills", "/skills/"), (s.name, s.url))
            sev_bits = severity_breakdown(s)
            plural = "s" if s.findings_count != 1 else ""
            # "safe" is the scanner's verdict; it can coexist with low-severity findings,
            # so the title must never say "no findings" unless the count really is zero.
            if s.findings_count == 0:
                title_tail = f"{s.verdict.lower()}, no findings"
            elif s.is_safe:
                title_tail = f"safe, {sev_bits or s.findings_count} finding{plural}"
            else:
                title_tail = f"{s.verdict.lower()}, {s.findings_count} finding{plural}{' (' + sev_bits + ')' if sev_bits else ''}"
            desc = (s.summary_text or summary_sentence(s)).strip()
            if len(desc) > 300:
                desc = desc[:297].rsplit(" ", 1)[0] + "…"
            jsonld = [
                self.jsonld_breadcrumbs(crumbs),
                {
                    "@context": "https://schema.org", "@type": "SoftwareApplication", "name": s.name,
                    "applicationCategory": "AI agent skill", "url": s.repo_url or self.base_url + s.url,
                    "review": {
                        "@type": "Review", "name": f"{s.name} security scan", "url": self.base_url + s.url,
                        "datePublished": fmt_date(s.timestamp), "reviewBody": desc,
                        "author": {"@type": "Organization", "name": SITE_NAME, "url": self.base_url + "/"},
                    },
                },
            ]
            self.render("skill.html", s.url, {
                "title": f"{s.name} security scan: {title_tail} | skillscan.io",
                "description": f"{s.name} ({s.source}): {desc}",
                "section": "skills", "breadcrumbs": crumbs, "jsonld": jsonld, "og_type": "article",
                "lastmod": fmt_date(s.timestamp),
            }, skill=s, summary_sentence=summary_sentence(s), related=related_skills(s, self.skills))
            color = SEVERITY_COLORS.get(s.max_severity or "SAFE", SEVERITY_COLORS["SAFE"]) if not s.is_safe else SEVERITY_COLORS["SAFE"]
            label = "safe" if s.is_safe else f"{s.findings_count} findings, {(s.max_severity or 'issues').lower()}"
            write(self.docs / "badge" / f"{s.slug}.svg", badge_svg("skillscan.io", label, color))

    def build_categories(self) -> None:
        crumbs = self.breadcrumbs(("Categories", "/categories/"))
        self.render("categories_index.html", "/categories/", {
            "title": "Agent skill finding categories mapped to OWASP AST10 | skillscan.io",
            "description": "The 13 security finding categories in the skillscan.io dataset, each mapped to the OWASP Agentic Skills Top 10 with examples and affected skills.",
            "section": "categories", "breadcrumbs": crumbs, "jsonld": self.jsonld_breadcrumbs(crumbs),
        })
        for c in self.categories:
            ctx = category_context(c, self.skills, self.registries)
            crumbs = self.breadcrumbs(("Categories", "/categories/"), (c["name"], c["url"]))
            self.render("category.html", c["url"], {
                "title": f"{c['name']} in AI agent skills: {c['count']} finding{'' if c['count'] == 1 else 's'} across {len(ctx['affected'])} skill{'' if len(ctx['affected']) == 1 else 's'} | skillscan.io",
                "description": (c.get("definition") or f"Findings classified as {c['name']} in scanned AI agent skills.")[:300],
                "section": "categories", "breadcrumbs": crumbs, "jsonld": self.jsonld_breadcrumbs(crumbs),
            }, category=c, **ctx)

    def build_registries(self) -> None:
        crumbs = self.breadcrumbs(("Registries", "/registries/"))
        self.render("registries_index.html", "/registries/", {
            "title": "AI agent skill registries scanned: skills.sh, ClawHub and more | skillscan.io",
            "description": "Per-registry security results for AI agent skills: how many skills from skills.sh, ClawHub and vendor repositories had findings, and how severe.",
            "section": "registries", "breadcrumbs": crumbs, "jsonld": self.jsonld_breadcrumbs(crumbs),
        })
        for r in self.registries:
            crumbs = self.breadcrumbs(("Registries", "/registries/"), (r["key"], r["url"]))
            self.render("registry.html", r["url"], {
                "title": f"{r['key']} security: {r['flagged']} of {r['skill_count']} skills with findings | skillscan.io",
                "description": f"Security scan results for {r['skill_count']} AI agent skills from {r['key']}: {r['flagged']} with findings, {r['severity_counts']['CRITICAL']} critical and {r['severity_counts']['HIGH']} high severity, with a per-skill breakdown.",
                "section": "registries", "breadcrumbs": crumbs, "jsonld": self.jsonld_breadcrumbs(crumbs),
            }, registry=r)

    def all_posts(self) -> list[dict]:
        posts = []
        for n in self.notes:
            posts.append({**n, "body_html": n.get("body", ""), "excerpt": n.get("excerpt", ""), "tags": n.get("tags", [])})
        for p in self.content:
            if p["section"] == "research":
                body_html = md_to_html(p["body_md"])
                posts.append({**p, "body_html": body_html, "excerpt": p.get("description", ""), "id": p["slug"]})
        return sorted(posts, key=lambda p: str(p.get("date", "")), reverse=True)

    def build_research(self) -> None:
        posts = self.all_posts()
        crumbs = self.breadcrumbs(("Research", "/research/"))
        self.render("research_index.html", "/research/", {
            "title": "Research on AI agent skill security | skillscan.io",
            "description": "Analysis posts from scanning hundreds of AI agent skills: registry comparisons, scanner false positives, methodology findings and incident notes.",
            "section": "research", "breadcrumbs": crumbs, "jsonld": self.jsonld_breadcrumbs(crumbs),
        }, posts=posts)
        for p in posts:
            crumbs = self.breadcrumbs(("Research", "/research/"), (p["title"], p["url"]))
            self.render("post.html", p["url"], {
                "title": f"{p['title']} | skillscan.io",
                "description": (p.get("description") or p.get("excerpt") or p["title"])[:300],
                "section": "research", "breadcrumbs": crumbs, "og_type": "article", "lastmod": str(p.get("updated") or p.get("date"))[:10],
                "jsonld": [self.jsonld_breadcrumbs(crumbs), {
                    "@context": "https://schema.org", "@type": "Article", "headline": p["title"],
                    "datePublished": str(p.get("date"))[:10], "dateModified": str(p.get("updated") or p.get("date"))[:10],
                    "url": self.base_url + p["url"], "author": {"@type": "Organization", "name": SITE_NAME},
                }],
            }, post=p)
        self.write_feed(posts)
        self.posts = posts

    def build_content_pages(self) -> None:
        by_section: dict[str, list[dict]] = defaultdict(list)
        for p in self.content:
            if p["section"] != "research":
                by_section[p["section"]].append(p)
        for section, pages in by_section.items():
            pages.sort(key=lambda p: (p["order"], p["slug"]))
            for p in pages:
                p["body_html"] = md_to_html(p["body_md"])
                crumbs = self.breadcrumbs((p["title"], p["url"])) if p["url"] == f"/{section}/" else self.breadcrumbs((section.capitalize(), f"/{section}/"), (p["title"], p["url"]))
                self.render("page.html", p["url"], {
                    "title": f"{p['title']} | skillscan.io",
                    "description": (p.get("description") or p["title"])[:300],
                    "section": section, "breadcrumbs": crumbs, "jsonld": self.jsonld_breadcrumbs(crumbs),
                    "lastmod": str(p.get("updated") or p.get("date") or self.site["scan_date"])[:10],
                }, content=p, siblings=pages if len(pages) > 1 else None)
            if section == "learn" and not any(p["url"] == "/learn/" for p in pages):
                index = {"title": "Learn", "section": "learn", "url": "/learn/", "updated": None,
                         "body_html": "<ul>" + "".join(f'<li><a href="{p["url"]}">{html.escape(p["title"])}</a>: {html.escape(p.get("description", ""))}</li>' for p in pages) + "</ul>"}
                crumbs = self.breadcrumbs(("Learn", "/learn/"))
                self.render("page.html", "/learn/", {
                    "title": "Learn: guides to AI agent skill security | skillscan.io",
                    "description": "Evergreen guides on what agent skills are, how to audit one before installing, what scanners catch and miss, and how to read a skillscan.io report.",
                    "section": "learn", "breadcrumbs": crumbs, "jsonld": self.jsonld_breadcrumbs(crumbs),
                }, content=index, siblings=None)

    def build_404(self) -> None:
        self.render("404.html", "/404.html", {"title": "Page not found | skillscan.io", "description": "Page not found.", "section": "", "noindex": True, "url": "/404.html"})

    # ---- supporting files
    def write_feed(self, posts: list[dict]) -> None:
        now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        entries = []
        for p in posts[:20]:
            d = str(p.get("date", "1970-01-01"))[:10]
            entries.append(
                f"<entry><title>{html.escape(p['title'])}</title><link href=\"{self.base_url}{p['url']}\"/>"
                f"<id>{self.base_url}{p['url']}</id><updated>{d}T00:00:00Z</updated>"
                f"<summary>{html.escape(p.get('excerpt') or p.get('description') or '')}</summary></entry>"
            )
        feed = (
            '<?xml version="1.0" encoding="utf-8"?><feed xmlns="http://www.w3.org/2005/Atom">'
            f"<title>{SITE_NAME} research</title><link href=\"{self.base_url}/research/\"/>"
            f"<link rel=\"self\" href=\"{self.base_url}/feed.xml\"/><id>{self.base_url}/research/</id><updated>{now}</updated>"
            + "".join(entries) + "</feed>"
        )
        write(self.docs / "feed.xml", feed)

    def write_sitemap(self) -> None:
        urls = "".join(
            f"<url><loc>{html.escape(self.base_url + p['url'])}</loc><lastmod>{p['lastmod']}</lastmod></url>" for p in self.pages
        )
        write(self.docs / "sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + urls + "</urlset>")
        write(self.docs / "robots.txt", f"User-agent: *\nAllow: /\nDisallow: /{LEGACY_DIR}/\nSitemap: {self.base_url}/sitemap.xml\n")

    def write_maps(self) -> None:
        write(self.data / "slugs.json", json.dumps(self.slug_map, indent=1, ensure_ascii=False))
        by_name: dict[str, str] = {}
        for s in self.skills:  # first (highest severity) wins on name collisions across sources
            by_name.setdefault(s.name, s.url)
        notes = {n["id"]: n["url"] for n in self.notes}
        write(self.data / "redirects.json", json.dumps({"skills": by_name, "notes": notes}, indent=1, ensure_ascii=False))

    def copy_taxonomy(self) -> None:
        """docs-src/data/categories.json is the source of truth; copy it into docs/data/
        so the published dataset and the loader both see it. Runs before load()."""
        src = self.src / "data" / "categories.json"
        if src.exists():
            self.data.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, self.data / "categories.json")

    def publish_legacy(self) -> None:
        """Copy the pre-redesign SPA from docs-src/legacy/ to docs/app/ verbatim.
        The sources already use absolute /app/ and /data/ paths and carry a noindex meta."""
        legacy = self.src / "legacy"
        if not legacy.exists():
            return
        out = self.docs / LEGACY_DIR
        out.mkdir(parents=True, exist_ok=True)
        for f in legacy.iterdir():
            if f.is_file():
                shutil.copy2(f, out / f.name)

    def copy_static(self) -> None:
        static = self.src / "static"
        if static.exists():
            for f in static.iterdir():
                if f.is_file():
                    shutil.copy2(f, self.docs / f.name)
        (self.docs / "og-default.svg").unlink(missing_ok=True)  # replaced by og-default.png in static/
        if not (self.docs / "og-default.png").exists():
            logger.warning("docs-src/static/og-default.png missing; social cards will have no image")

    def clean(self) -> None:
        """Remove previously generated page directories. Never touches docs/data/,
        which holds the scan corpus and is also the URL of the /data/ content page."""
        sections = {p["section"] for p in self.content if p["section"] != "research"}
        for d in set(GENERATED_DIRS) | sections:
            if d in PROTECTED_DIRS:
                # Only remove the generated index page, leave everything else.
                (self.docs / d / "index.html").unlink(missing_ok=True)
                continue
            shutil.rmtree(self.docs / d, ignore_errors=True)

    def build(self) -> dict:
        self.copy_taxonomy()
        self.load()
        self.clean()
        self.copy_static()
        self.publish_legacy()
        self.build_home()
        self.build_skills()
        self.build_categories()
        self.build_registries()
        self.build_research()
        self.build_content_pages()
        self.build_404()
        self.write_sitemap()
        self.write_maps()
        return {"pages": len(self.pages), "skills": len(self.skills), "categories": len(self.categories),
                "registries": len(self.registries), "posts": len(self.posts), "content": len(self.content)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO, format="%(levelname)s %(message)s")
    stats = SiteBuilder(args.root, args.base_url).build()
    logger.info("Built %s", ", ".join(f"{k}={v}" for k, v in stats.items()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
