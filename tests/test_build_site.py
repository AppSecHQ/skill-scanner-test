"""Tests for the static site generator (scripts/build_site.py and scripts/sitegen/)."""
import json
import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from build_site import SiteBuilder, badge_svg, summary_sentence  # noqa: E402
from sitegen.loaders import Skill, load_content, load_skills, parse_frontmatter  # noqa: E402
from sitegen.slugs import SlugRegistry, ascii_slug, skill_slug  # noqa: E402


# ----------------------------------------------------------------- slugs
class TestSlugs:
    def test_ascii_slug_basic(self):
        assert ascii_slug("Hello World!") == "hello-world"
        assert ascii_slug("clawhub.ai") == "clawhub-ai"

    def test_ascii_slug_transliterates_accents(self):
        assert ascii_slug("café-résumé") == "cafe-resume"

    def test_non_latin_name_falls_back_to_hash(self):
        slug = skill_slug("clawhub.ai", "加密货币与贵金属监控")
        assert slug.startswith("clawhub-ai-skill-")
        assert re.fullmatch(r"clawhub-ai-skill-[0-9a-f]{8}", slug)

    def test_long_names_truncated_with_hash(self):
        name = "a-" * 100
        slug = skill_slug("skills.sh", name)
        assert len(slug) <= 90
        assert slug == skill_slug("skills.sh", name)  # deterministic

    def test_registry_is_stable_and_collision_free(self):
        reg = SlugRegistry()
        a = reg.assign("skills.sh", "foo")
        b = reg.assign("skills.sh", "foo")
        c = reg.assign("skills.sh", "Foo!")  # same ascii slug, different name
        assert a == b == "skills-sh-foo"
        assert c == "skills-sh-foo-2"


# ----------------------------------------------------------------- fixtures
def _scan(name, findings, ts, analyzers=("static_analyzer",), is_safe=None):
    return {
        "skill_name": name,
        "is_safe": is_safe if is_safe is not None else not findings,
        "max_severity": max((f["severity"] for f in findings), default=None, key=lambda s: ["INFO", "LOW", "MEDIUM", "HIGH", "CRITICAL"].index(s)),
        "findings_count": len(findings),
        "findings": findings,
        "analyzers_used": list(analyzers),
        "timestamp": ts,
    }


def _finding(sev, cat, title="t", snippet="x=1", analyzer="static_analyzer", meta=None):
    return {
        "id": f"{cat}-{title}", "rule_id": "R", "category": cat, "severity": sev, "title": title,
        "description": "desc " * 5, "file_path": "SKILL.md", "line_number": 3, "snippet": snippet,
        "remediation": "fix it", "analyzer": analyzer, "metadata": meta or {},
    }


@pytest.fixture
def site_root(tmp_path: Path) -> Path:
    docs = tmp_path / "docs"
    scans = docs / "data" / "scans"
    scans.mkdir(parents=True)
    # Three skills, one scanned twice, one with a non-ASCII scan filename.
    f_crit = _finding("CRITICAL", "data_exfiltration", "Exfil", meta={"overall_assessment": "This skill ships keys to a remote host."})
    f_med = _finding("MEDIUM", "prompt_injection", "Inject")
    (scans / "alpha-scan.json").write_text(json.dumps(_scan("alpha", [f_crit, f_med], "2026-02-07T10:00:00")))
    (scans / "alpha-old-scan.json").write_text(json.dumps(_scan("alpha", [f_crit], "2026-02-01T10:00:00")))
    (scans / "gamma-scan.json").write_text(json.dumps(_scan("gamma", [f_med], "2026-02-06T10:00:00", is_safe=True)))
    (scans / "delta-scan.json").write_text(json.dumps(_scan("delta", [_finding("INFO", "policy_violation", "Note")], "2026-02-06T10:00:00", is_safe=True)))
    (scans / "beta-scan.json").write_text(json.dumps(_scan("beta", [], "2026-02-05T10:00:00", analyzers=("static_analyzer", "llm_analyzer"))))
    (scans / "腾讯地图-scan.json").write_text(json.dumps(_scan("tencent-map", [f_med], "2026-02-06T10:00:00")))
    (scans / "twin-scan.json").write_text(json.dumps(_scan("twin", [], "2026-02-06T10:00:00")))
    (scans / "twin-2-scan.json").write_text(json.dumps(_scan("twin", [], "2026-02-06T10:00:00")))
    summary = {
        "scan_date": "2026-02-07",
        "total_skills": 4, "safe_skills": 1, "unsafe_skills": 3, "error_skills": 0,
        "severity_counts": {"CRITICAL": 1, "HIGH": 0, "MEDIUM": 2, "LOW": 0},
        "total_findings": 4,
        "findings_by_category": {"data_exfiltration": 2, "prompt_injection": 2},
        "top_risks": [], "analyzers_used": ["static_analyzer", "llm_analyzer"],
        "skills": [
            {"name": "alpha", "source": "clawhub.ai", "repo_url": "https://example.com/a", "scan_file": "alpha-scan.md", "is_safe": False, "findings_count": 2, "max_severity": "CRITICAL", "analyzers": ["static_analyzer"]},
            {"name": "alpha", "source": "clawhub.ai", "repo_url": "https://example.com/a", "scan_file": "alpha-old-scan.md", "is_safe": False, "findings_count": 1, "max_severity": "CRITICAL", "analyzers": ["static_analyzer"]},
            {"name": "gamma", "source": "skills.sh", "repo_url": None, "scan_file": "gamma-scan.md", "is_safe": True, "findings_count": 1, "max_severity": "MEDIUM", "analyzers": ["static_analyzer"]},
            {"name": "delta", "source": "skills.sh", "repo_url": None, "scan_file": "delta-scan.md", "is_safe": True, "findings_count": 1, "max_severity": "INFO", "analyzers": ["static_analyzer"]},
            {"name": "beta", "source": "skills.sh", "repo_url": "https://example.com/b", "scan_file": "beta-scan.md", "is_safe": True, "findings_count": 0, "max_severity": None, "analyzers": ["static_analyzer", "llm_analyzer"]},
            {"name": "tencent-map", "source": "clawhub.ai", "repo_url": None, "scan_file": "腾讯地图-scan.md", "is_safe": False, "findings_count": 1, "max_severity": "MEDIUM", "analyzers": ["static_analyzer"]},
            {"name": "twin", "source": "clawhub.ai", "repo_url": None, "scan_file": "twin-scan.md", "is_safe": True, "findings_count": 0, "max_severity": None, "analyzers": ["static_analyzer"]},
            {"name": "twin", "source": "skills.sh", "repo_url": None, "scan_file": "twin-2-scan.md", "is_safe": True, "findings_count": 0, "max_severity": None, "analyzers": ["static_analyzer"]},
        ],
    }
    (docs / "data" / "summary.json").write_text(json.dumps(summary))
    profiles = docs / "data" / "profiles"
    profiles.mkdir()
    (profiles / "beta-profile.json").write_text(json.dumps({
        "schema": 1, "name": "beta", "description": "Formats invoices as PDF for small shops.", "license": "MIT",
        "compatibility": None, "version": "1.2.0", "homepage": None, "allowed_tools": ["Bash", "Read"],
        "requires": {"bins": ["pandoc"]}, "frontmatter_keys": ["name", "description"],
        "skill_md": {"present": True, "bytes": 900, "words": 140, "headings": ["Setup", "Usage"]},
        "file_count": 2, "total_bytes": 2048, "kinds": {"doc": 1, "script": 1}, "languages": {"Python": 1},
        "files": [{"path": "SKILL.md", "bytes": 900, "kind": "doc"}, {"path": "scripts/run.py", "bytes": 1148, "kind": "script"}],
        "files_truncated": 0, "domains": ["api.invoices.example.io"], "env_vars": ["INVOICE_API_KEY"],
        "git_commit": "abc123def456", "profiled_at": "2026-10-22T01:00:00Z",
    }))
    # The two twins are a byte-identical re-upload: same description, same files.
    twin_profile = {
        "schema": 1, "name": "twin", "description": "Pairs things.", "license": None, "compatibility": None,
        "version": None, "homepage": None, "allowed_tools": [], "requires": {}, "frontmatter_keys": ["name", "description"],
        "skill_md": {"present": True, "bytes": 300, "words": 40, "headings": []}, "file_count": 1, "total_bytes": 300,
        "kinds": {"doc": 1}, "languages": {}, "files": [{"path": "SKILL.md", "bytes": 300, "kind": "doc"}],
        "files_truncated": 0, "domains": [], "env_vars": [], "git_commit": "feedfacefeed", "profiled_at": "2026-10-22T01:00:00Z",
    }
    (profiles / "twin-profile.json").write_text(json.dumps(twin_profile))
    (profiles / "twin-2-profile.json").write_text(json.dumps(twin_profile))
    (docs / "data" / "skillspector.json").write_text(json.dumps({
        "alpha": {"recommendation": "DO_NOT_INSTALL", "score": 100, "severity": "CRITICAL", "issue_count": 7,
                  "top_categories": ["Data Exfiltration", "Tool Misuse"], "version": "2.12.0", "mode": "static", "scanned_at": "2026-10-22T00:00:00Z"},
        "beta": {"recommendation": "CAUTION", "score": 0, "severity": "LOW", "issue_count": 0,
                 "top_categories": [], "version": "2.12.0", "mode": "static", "scanned_at": "2026-10-22T00:00:00Z"},
        "gamma": {"recommendation": "SAFE", "score": 0, "severity": "LOW", "issue_count": 0,
                  "top_categories": [], "version": "2.12.0", "mode": "static", "scanned_at": "2026-10-22T00:00:00Z"},
    }))
    (docs / "data" / "categories.json").write_text(json.dumps({
        "_meta": {}, "categories": [
            {"slug": "data_exfiltration", "name": "Data Exfiltration", "ast10_id": "AST01", "ast10_title": "Malicious Skills", "secondary_ast10": ["AST03"], "definition": "Sends data out of the skill to somewhere the user did not ask for.", "check_yourself": "Grep for URLs."},
        ]}))
    (docs / "notes.json").write_text(json.dumps([
        {"id": "clawhavoc-validation", "date": "2026-02-12", "title": "ClawHavoc", "tags": ["incident"], "excerpt": "Validation of the ClawHavoc incident findings.", "body": "<p>body</p>"},
    ]))
    content = tmp_path / "docs-src" / "content"
    (content / "methodology").mkdir(parents=True)
    (content / "methodology" / "index.md").write_text("---\ntitle: Methodology\ndescription: How we scan, in enough words to pass the meta check.\n---\n\n## What runs\n\nText with a [link](/categories/data-exfiltration/).\n")
    (content / "learn").mkdir()
    (content / "learn" / "b.md").write_text("---\ntitle: B\ndescription: Second learn page description long enough.\norder: 2\n---\nb\n")
    (content / "learn" / "a.md").write_text("---\ntitle: A\ndescription: First learn page description long enough.\norder: 1\n---\na\n")
    (content / "research").mkdir()
    (content / "research" / "2026-10-21-post.md").write_text("---\ntitle: Post\ndescription: A research post description long enough.\ndate: 2026-10-21\ntags: [a, b]\n---\n\n| h | i |\n|---|---|\n| 1 | 2 |\n")
    (content / "research" / "2026-10-22-two-scanners-one-corpus.md").write_text("---\ntitle: Two scanners\ndescription: The comparison post the skill template links to, described.\ndate: 2026-10-22\ntags: [a]\n---\n\ntext\n")
    (content / "research" / "2026-10-21-false-positive-register.md").write_text("---\ntitle: Register\ndescription: The false-positive register the skill template links to, described.\ndate: 2026-10-21\ntags: [a]\n---\n\ntext\n")
    (content / "README.md").write_text("# not a page\n")
    # Pages the base template links to from the nav and footer.
    for section in ("about", "data", "request-a-scan"):
        (content / section).mkdir()
        (content / section / "index.md").write_text(f"---\ntitle: {section}\ndescription: The {section} page, described at sufficient length.\n---\ntext\n")
    static = tmp_path / "docs-src" / "static"
    static.mkdir()
    for name in ("theme.css", "site.js", "og-default.png", "favicon.svg", "favicon.ico", "apple-touch-icon.png", "icon-512.png"):
        (static / name).write_text("/* static */")
    (static / "fonts").mkdir()
    for font in ("newsreader-latin.woff2", "jetbrainsmono-latin.woff2"):
        (static / "fonts" / font).write_bytes(b"wOF2")
    return tmp_path


# ----------------------------------------------------------------- loaders
class TestLoaders:
    def test_groups_duplicate_scans_into_history(self, site_root):
        _, skills, slug_map = load_skills(site_root / "docs" / "data")
        assert len(skills) == 7
        alpha = next(s for s in skills if s.name == "alpha")
        assert alpha.scan_count == 2
        assert alpha.timestamp == "2026-02-07T10:00:00"  # newest first
        assert alpha.history[1]["timestamp"] == "2026-02-01T10:00:00"
        assert slug_map[alpha.slug]["scan_files"] == ["alpha-scan.json", "alpha-old-scan.json"]

    def test_non_ascii_scan_file_is_found(self, site_root):
        _, skills, _ = load_skills(site_root / "docs" / "data")
        tm = next(s for s in skills if s.name == "tencent-map")
        assert tm.findings_count == 1 and tm.findings
        assert tm.scan_file == "腾讯地图-scan.json"

    def test_summary_text_from_llm_metadata(self, site_root):
        _, skills, _ = load_skills(site_root / "docs" / "data")
        alpha = next(s for s in skills if s.name == "alpha")
        assert alpha.summary_text.startswith("This skill ships keys")
        assert alpha.categories == ["data_exfiltration", "prompt_injection"]

    def test_frontmatter_lists_and_quotes(self):
        meta, body = parse_frontmatter('---\ntitle: "Quoted"\ntags: [a, b]\n---\nbody\n')
        assert meta == {"title": "Quoted", "tags": ["a", "b"]}
        assert body == "body\n"

    def test_content_urls(self, site_root):
        pages = {p["url"]: p for p in load_content(site_root / "docs-src" / "content")}
        assert "/methodology/" in pages
        assert "/learn/a/" in pages and pages["/learn/a/"]["order"] == 1
        assert "/research/2026/post/" in pages and pages["/research/2026/post/"]["tags"] == ["a", "b"]
        assert not any("readme" in u.lower() for u in pages)


# ----------------------------------------------------------------- build
class TestBuild:
    @pytest.fixture
    def built(self, site_root):
        stats = SiteBuilder(site_root, base_url="https://example.test").build()
        return site_root / "docs", stats

    def test_every_skill_gets_a_page_and_badge(self, built):
        docs, stats = built
        assert stats["skills"] == 7
        for slug in ("clawhub-ai-alpha", "skills-sh-beta", "clawhub-ai-tencent-map"):
            assert (docs / "skills" / slug / "index.html").exists()
            assert (docs / "badge" / f"{slug}.svg").exists()

    def test_sitemap_matches_rendered_pages(self, built):
        docs, stats = built
        locs = re.findall(r"<loc>(.*?)</loc>", (docs / "sitemap.xml").read_text())
        assert len(locs) == stats["pages"]
        assert "https://example.test/skills/clawhub-ai-alpha/" in locs
        assert "https://example.test/research/2026/clawhavoc-validation/" in locs
        assert not any(l.endswith("404.html") for l in locs)
        assert "Sitemap: https://example.test/sitemap.xml" in (docs / "robots.txt").read_text()

    def test_every_page_has_title_description_canonical(self, built):
        docs, _ = built
        for page in docs.rglob("index.html"):
            html = page.read_text()
            assert re.search(r"<title>.{5,}</title>", html), page
            assert re.search(r'name="description" content=".{20,}"', html), page
            assert 'rel="canonical" href="https://example.test/' in html, page
            assert "application/ld+json" in html, page

    def test_skill_page_content(self, built):
        docs, _ = built
        html = (docs / "skills" / "clawhub-ai-alpha" / "index.html").read_text()
        assert "This skill ships keys to a remote host." in html
        assert "Scan history" in html and "first scan" in html
        assert 'href="/categories/data-exfiltration/"' in html
        assert "/data/scans/alpha-old-scan.json" in html
        safe = (docs / "skills" / "skills-sh-beta" / "index.html").read_text()
        assert "SAFE" in safe and "Scan history" not in safe

    def test_second_scanner_verdicts_render(self, built):
        docs, _ = built
        alpha = (docs / "skills" / "clawhub-ai-alpha" / "index.html").read_text()
        assert "Second scanner: NVIDIA SkillSpector" in alpha
        assert "Do not install 100" in alpha and "Data Exfiltration" in alpha
        beta = (docs / "skills" / "skills-sh-beta" / "index.html").read_text()
        assert "Caution 0" in beta and "fails closed" in beta
        assert 'class="badge badge-info"' in beta  # not a severity colour
        # No result: the page simply omits the section, and the index shows a dash.
        delta = (docs / "skills" / "skills-sh-delta" / "index.html").read_text()
        assert "Second scanner" not in delta
        index = (docs / "skills" / "index.html").read_text()
        assert "<th data-sort=\"skillspector\"" in index
        assert index.count('<td class="second-verdict">') == 7
        assert "Safe 0" in index and "&mdash;" in index

    def test_skill_page_uses_package_profile(self, built):
        docs, _ = built
        beta = (docs / "skills" / "skills-sh-beta" / "index.html").read_text()
        assert "What this skill does" in beta and "Formats invoices as PDF for small shops." in beta
        assert "scripts/run.py" in beta and "api.invoices.example.io" in beta and "INVOICE_API_KEY" in beta
        assert "Python (1)" in beta and "<code>pandoc</code>" in beta and "abc123def456" in beta
        # Author description leads the meta description, verdict follows, never over 160 chars.
        m = re.search(r'name="description" content="([^"]*)"', beta)
        assert m.group(1).startswith("beta (skills.sh): Formats invoices as PDF for small shops. No security findings")
        assert len(m.group(1)) <= 160
        assert '"license": "MIT"' in beta and '"softwareVersion": "1.2.0"' in beta
        # Skills without a profile render the old way, with the templated description.
        alpha = (docs / "skills" / "clawhub-ai-alpha" / "index.html").read_text()
        assert "What this skill does" not in alpha
        assert re.search(r'name="description" content="alpha \(clawhub.ai\): 2 findings', alpha)

    def test_head_tags_noindex_favicon_article(self, built):
        docs, _ = built
        assert '<meta name="robots" content="noindex">' in (docs / "404.html").read_text()
        home = (docs / "index.html").read_text()
        assert 'name="robots"' not in home and 'rel="icon" href="/favicon.svg"' in home and 'apple-touch-icon' in home
        assert "/404.html" not in (docs / "sitemap.xml").read_text()
        post = (docs / "research" / "2026" / "post" / "index.html").read_text()
        assert '/og-default.png' in post and '"publisher"' in post and '"logo"' in post
        cats = (docs / "categories" / "index.html").read_text()
        assert "The 2 security finding categories" in cats  # 1 taxonomy entry + 1 seen only in scans
        for page in docs.rglob("index.html"):
            if str(page).startswith(str(docs / "app")):
                continue
            d = re.search(r'name="description" content="([^"]*)"', page.read_text()).group(1)
            assert len(d) <= 160, (page, len(d))

    def test_titles_never_contradict_finding_counts(self, built):
        docs, _ = built
        def title(slug):
            return re.search(r"<title>(.*?)</title>", (docs / "skills" / slug / "index.html").read_text()).group(1)
        # Skill titles carry no " | skillscan.io" suffix; the site name comes from WebSite JSON-LD.
        assert title("skills-sh-beta") == "beta security scan: no findings"
        assert title("skills-sh-gamma") == "gamma security scan: safe, 1 medium finding"
        assert title("skills-sh-delta") == "delta security scan: safe, 1 info finding"
        assert title("clawhub-ai-alpha") == "alpha security scan: 2 findings, 1 critical"
        # The registry appears only when the same name exists in more than one registry.
        assert title("clawhub-ai-twin") == "twin (clawhub.ai) security scan: no findings"
        assert title("skills-sh-twin") == "twin (skills.sh) security scan: no findings"
        assert "| skillscan.io" in re.search(r"<title>(.*?)</title>", (docs / "skills" / "index.html").read_text()).group(1)
        for page in (docs / "skills").rglob("index.html"):
            html = page.read_text()
            t = re.search(r"<title>(.*?)</title>", html).group(1)
            assert not ("no findings" in t and re.search(r"\(\d", t)), t
            assert "1 findings" not in t, t
            assert 'property="og:image" content="https://example.test/og-default.png"' in html

    def test_identical_copies_share_one_canonical(self, built):
        docs, stats = built
        assert stats["duplicate_copies"] == 1
        # Same first-scan timestamp, so the registry name breaks the tie: clawhub.ai < skills.sh.
        primary = (docs / "skills" / "clawhub-ai-twin" / "index.html").read_text()
        copy = (docs / "skills" / "skills-sh-twin" / "index.html").read_text()
        assert 'rel="canonical" href="https://example.test/skills/clawhub-ai-twin/"' in primary
        assert 'rel="canonical" href="https://example.test/skills/clawhub-ai-twin/"' in copy
        assert 'property="og:url" content="https://example.test/skills/clawhub-ai-twin/"' in copy
        assert 'name="robots"' not in copy  # indexable, canonicalised, not noindexed
        assert "Byte-identical copies of this skill are also published by" in primary and 'href="/skills/skills-sh-twin/"' in primary
        assert "byte-identical copy of" in copy and 'href="/skills/clawhub-ai-twin/"' in copy
        locs = re.findall(r"<loc>(.*?)</loc>", (docs / "sitemap.xml").read_text())
        assert "https://example.test/skills/clawhub-ai-twin/" in locs
        assert "https://example.test/skills/skills-sh-twin/" not in locs
        # Skills with a profile but no identical twin elsewhere are untouched.
        beta = (docs / "skills" / "skills-sh-beta" / "index.html").read_text()
        assert "copies-note" not in beta and 'rel="canonical" href="https://example.test/skills/skills-sh-beta/"' in beta

    def test_fonts_self_hosted_and_dataset_jsonld(self, built):
        docs, _ = built
        assert (docs / "fonts" / "newsreader-latin.woff2").read_bytes() == b"wOF2"
        home = (docs / "index.html").read_text()
        assert "fonts.googleapis.com" not in home and "fonts.gstatic.com" not in home
        assert 'rel="preload" href="/fonts/newsreader-latin.woff2" as="font"' in home
        data = (docs / "data" / "index.html").read_text()
        m = re.search(r'<script type="application/ld\+json">(.*?)</script>', data, re.S)
        ld = json.loads(m.group(1))
        ds = next(x for x in (ld if isinstance(ld, list) else [ld]) if x.get("@type") == "Dataset")
        assert ds["license"] == "https://creativecommons.org/licenses/by/4.0/"
        assert ds["url"] == "https://example.test/data/"
        assert any(d["contentUrl"].endswith("/data/summary.json") for d in ds["distribution"])
        assert ds["temporalCoverage"] == "2026-02-01/2026-02-07"
        # Only the dataset page carries it.
        assert '"Dataset"' not in (docs / "about" / "index.html").read_text()

    def test_category_page_uses_taxonomy_and_lists_affected(self, built):
        docs, _ = built
        html = (docs / "categories" / "data-exfiltration" / "index.html").read_text()
        assert "OWASP AST01" in html and "Sends data out of" in html and "Grep for URLs." in html
        assert 'href="/skills/clawhub-ai-alpha/"' in html
        # Category missing from taxonomy still renders.
        assert (docs / "categories" / "prompt-injection" / "index.html").exists()

    def test_content_and_research_render_markdown(self, built):
        docs, _ = built
        assert "<h2" in (docs / "methodology" / "index.html").read_text()
        post = (docs / "research" / "2026" / "post" / "index.html").read_text()
        assert "<table>" in post
        assert "<entry>" in (docs / "feed.xml").read_text()
        assert (docs / "learn" / "index.html").exists()

    def test_internal_links_resolve(self, built):
        docs, _ = built
        hrefs = set()
        for page in docs.rglob("*.html"):
            hrefs.update(re.findall(r'(?:href|src)="(/[^"#?]*)', page.read_text()))
        broken = [h for h in hrefs if not ((docs / h.lstrip("/")).exists() or (docs / h.lstrip("/") / "index.html").exists())]
        assert broken == []

    def test_redirect_map_and_data_preserved(self, built):
        docs, _ = built
        redirects = json.loads((docs / "data" / "redirects.json").read_text())
        assert redirects["skills"]["alpha"] == "/skills/clawhub-ai-alpha/"
        assert redirects["notes"]["clawhavoc-validation"] == "/research/2026/clawhavoc-validation/"
        assert (docs / "data" / "summary.json").exists()
        assert (docs / "data" / "scans" / "alpha-scan.json").exists()

    def test_rebuild_is_idempotent_and_keeps_data(self, site_root):
        SiteBuilder(site_root, base_url="https://example.test").build()
        stats = SiteBuilder(site_root, base_url="https://example.test").build()
        assert stats["pages"] > 0
        assert (site_root / "docs" / "data" / "scans" / "alpha-scan.json").exists()
        assert (site_root / "docs" / "data" / "categories.json").exists()


# ----------------------------------------------------------------- misc
def test_badge_svg_escapes():
    svg = badge_svg("skillscan.io", '2 findings, <high>', "#fff")
    assert "&lt;high&gt;" in svg and "<svg" in svg


def test_summary_sentence_safe_and_unsafe():
    safe = Skill("x", "s", "s-x", None, None, True, 0, None, [], {"timestamp": "2026-01-01T00:00:00"})
    assert summary_sentence(safe).startswith("No security findings")
    unsafe = Skill("x", "s", "s-x", None, None, False, 2, "HIGH", [], {"timestamp": "2026-01-01T00:00:00", "findings": [_finding("HIGH", "obfuscation"), _finding("LOW", "obfuscation")]})
    s = summary_sentence(unsafe)
    assert "2 findings" in s and "1 high" in s and "obfuscation" in s


# ----------------------------------------------------------------- cutover: taxonomy source + legacy /app/
def test_taxonomy_copied_from_docs_src_and_legacy_app_published(site_root):
    src_data = site_root / "docs-src" / "data"
    src_data.mkdir(parents=True, exist_ok=True)
    (src_data / "categories.json").write_text(json.dumps({"_meta": {}, "categories": [
        {"slug": "prompt_injection", "name": "Prompt Injection (from source)", "ast10_id": "AST05",
         "ast10_title": "Untrusted External Instructions", "secondary_ast10": [], "definition": "d", "check_yourself": "c"},
    ]}))
    legacy = site_root / "docs-src" / "legacy"
    legacy.mkdir(parents=True)
    (legacy / "index.html").write_text('<!DOCTYPE html><meta name="robots" content="noindex, nofollow"><script src="/app/app.js"></script>')
    (legacy / "app.js").write_text("fetch('/data/summary.json')")

    docs = site_root / "docs"
    SiteBuilder(site_root, base_url="https://example.test").build()

    # docs-src/data wins over whatever was in docs/data and is republished there
    published = json.loads((docs / "data" / "categories.json").read_text())
    assert published["categories"][0]["name"] == "Prompt Injection (from source)"
    assert "Prompt Injection (from source)" in (docs / "categories" / "prompt-injection" / "index.html").read_text()

    # legacy SPA served at /app/, noindex, excluded from sitemap, disallowed in robots
    assert (docs / "app" / "index.html").exists() and (docs / "app" / "app.js").exists()
    assert "noindex" in (docs / "app" / "index.html").read_text()
    assert "/app/" not in (docs / "sitemap.xml").read_text()
    assert "Disallow: /app/" in (docs / "robots.txt").read_text()

    # rebuild is clean: /app/ is regenerated, docs/data untouched
    (docs / "app" / "stale.txt").write_text("x")
    SiteBuilder(site_root, base_url="https://example.test").build()
    assert not (docs / "app" / "stale.txt").exists()
    assert (docs / "data" / "scans").exists()
