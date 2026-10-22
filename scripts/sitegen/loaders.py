"""Load scan data, notes and Markdown content into plain dicts."""
from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass, field
from pathlib import Path

from .slugs import SlugRegistry, ascii_slug

logger = logging.getLogger(__name__)

SEVERITY_ORDER = {"CRITICAL": 4, "HIGH": 3, "MEDIUM": 2, "LOW": 1, "INFO": 0, None: -1}


@dataclass
class Skill:
    name: str
    source: str
    slug: str
    repo_url: str | None
    scan_file: str | None
    is_safe: bool | None
    findings_count: int
    max_severity: str | None
    analyzers: list[str]
    scan: dict = field(default_factory=dict)
    history: list[dict] = field(default_factory=list)  # all scans, newest first
    profile: dict | None = None  # package description from skill_profile.py, newest scan
    skillspector: dict | None = None  # second-scanner verdict from docs/data/skillspector.json, newest scan
    # Byte-identical copies of the same skill published in other registries
    # (see build_site.link_identical_copies). canonical_of is None on the
    # copy that owns the canonical URL.
    copies: list["Skill"] = field(default_factory=list, repr=False, compare=False)
    canonical_of: "Skill | None" = field(default=None, repr=False, compare=False)

    @property
    def findings(self) -> list[dict]:
        return self.scan.get("findings", []) or []

    @property
    def scan_count(self) -> int:
        return max(1, len(self.history))

    @property
    def first_scanned(self) -> str | None:
        return self.history[-1].get("timestamp") if self.history else self.timestamp

    @property
    def severity_counts(self) -> dict[str, int]:
        counts = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}
        for f in self.findings:
            sev = (f.get("severity") or "").upper()
            if sev in counts:
                counts[sev] += 1
        return counts

    @property
    def verdict(self) -> str:
        if self.is_safe is True:
            return "SAFE"
        if self.is_safe is False:
            return "ISSUES FOUND"
        return "SCAN ERROR"

    @property
    def timestamp(self) -> str | None:
        return self.scan.get("timestamp")

    @property
    def scanner_version(self) -> str | None:
        return self.scan.get("scanner_version")

    @property
    def categories(self) -> list[str]:
        seen: dict[str, int] = {}
        for f in self.findings:
            c = f.get("category")
            if c:
                seen[c] = seen.get(c, 0) + 1
        return sorted(seen, key=lambda c: -seen[c])

    @property
    def summary_text(self) -> str | None:
        for f in self.findings:
            meta = f.get("metadata") or {}
            text = meta.get("overall_assessment")
            if text:
                return text
        return None

    @property
    def description(self) -> str | None:
        """The author's own one-paragraph description from SKILL.md frontmatter."""
        if self.profile and self.profile.get("description"):
            return self.profile["description"]
        return None

    @property
    def url(self) -> str:
        return f"/skills/{self.slug}/"


def _scan_json_name(scan_file: str | None, name: str) -> str:
    """summary.json records the .md report; the JSON sits beside it."""
    if scan_file and scan_file.endswith("-scan.md"):
        return scan_file[: -len(".md")] + ".json"
    return f"{name}-scan.json"


def _load_profile(profiles_dir: Path, json_name: str) -> dict | None:
    """results/profiles/<stem>-profile.json, where <stem>-scan.json is the scan."""
    stem = json_name.lstrip(".")
    if stem.endswith("-scan.json"):
        stem = stem[: -len("-scan.json")]
    path = profiles_dir / f"{stem}-profile.json"
    if not path.exists():
        return None
    try:
        prof = json.loads(path.read_text())
    except json.JSONDecodeError as e:
        logger.warning("Bad JSON in %s: %s", path, e)
        return None
    return prof if isinstance(prof, dict) else None


def _load_skillspector(data_dir: Path) -> dict[str, dict]:
    """docs/data/skillspector.json: {published stem: verdict}, written by compare_scanners.py."""
    path = data_dir / "skillspector.json"
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as e:
        logger.warning("Bad JSON in %s: %s", path, e)
        return {}
    return data if isinstance(data, dict) else {}


def _published_stem(json_name: str) -> str:
    stem = json_name.lstrip(".")
    return stem[: -len("-scan.json")] if stem.endswith("-scan.json") else stem


def load_skills(data_dir: Path) -> tuple[dict, list[Skill], dict[str, dict]]:
    summary = json.loads((data_dir / "summary.json").read_text())
    scans_dir = data_dir / "scans"
    profiles_dir = data_dir / "profiles"
    skillspector = _load_skillspector(data_dir)
    registry = SlugRegistry()
    groups: dict[tuple[str, str], list[tuple[dict, dict, str]]] = {}
    for entry in summary.get("skills", []):
        name = entry["name"]
        source = entry.get("source") or "unknown"
        json_name = _scan_json_name(entry.get("scan_file"), name)
        # GitHub Pages does not serve dotfiles; build-site.sh strips the dot.
        candidates = [scans_dir / json_name, scans_dir / json_name.lstrip(".")]
        scan: dict = {}
        for c in candidates:
            if c.exists():
                try:
                    scan = json.loads(c.read_text())
                except json.JSONDecodeError as e:
                    logger.warning("Bad JSON in %s: %s", c, e)
                break
        else:
            logger.warning("No scan JSON for %s (tried %s)", name, json_name)
        scan.setdefault("_scan_file", json_name.lstrip("."))
        scan.setdefault("_profile", _load_profile(profiles_dir, json_name))
        scan.setdefault("_skillspector", skillspector.get(_published_stem(json_name)))
        groups.setdefault((source, name), []).append((entry, scan, json_name))

    skills: list[Skill] = []
    for (source, name), scans in groups.items():
        # Newest scan first; the same skill may have been scanned several times.
        scans.sort(key=lambda t: t[1].get("timestamp") or "", reverse=True)
        entry, scan, json_name = scans[0]
        skills.append(
            Skill(
                name=name,
                source=source,
                slug=registry.assign(source, name),
                repo_url=entry.get("repo_url"),
                scan_file=json_name.lstrip(".") if scan.get("findings") is not None else None,
                is_safe=entry.get("is_safe"),
                findings_count=entry.get("findings_count", 0),
                max_severity=entry.get("max_severity"),
                analyzers=entry.get("analyzers", []),
                scan=scan,
                history=[s for _, s, _ in scans],
                profile=next((s.get("_profile") for _, s, _ in scans if s.get("_profile")), None),
                skillspector=next((s.get("_skillspector") for _, s, _ in scans if s.get("_skillspector")), None),
            )
        )
    skills.sort(key=lambda s: (-SEVERITY_ORDER.get(s.max_severity, -1), -s.findings_count, s.name))
    slug_map = {
        s.slug: {"name": s.name, "source": s.source, "scan_files": [h["_scan_file"] for h in s.history]}
        for s in skills
    }
    return summary, skills, slug_map


def load_notes(docs_dir: Path) -> list[dict]:
    path = docs_dir / "notes.json"
    if not path.exists():
        return []
    notes = json.loads(path.read_text())
    for n in notes:
        n["year"] = (n.get("date") or "1970")[:4]
        n["slug"] = ascii_slug(n.get("id") or n["title"])
        n["url"] = f"/research/{n['year']}/{n['slug']}/"
    return sorted(notes, key=lambda n: n.get("date", ""), reverse=True)


_FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
_DATE_PREFIX = re.compile(r"^(\d{4})-\d{2}-\d{2}-(.+)$")


def _parse_value(v: str):
    v = v.strip()
    if v.startswith("[") and v.endswith("]"):
        return [x.strip().strip('"').strip("'") for x in v[1:-1].split(",") if x.strip()]
    return v.strip('"').strip("'")


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Minimal YAML subset: `key: value` lines, with `[a, b]` lists."""
    m = _FRONTMATTER.match(text)
    if not m:
        return {}, text
    meta: dict = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.lstrip().startswith("#"):
            k, v = line.split(":", 1)
            meta[k.strip()] = _parse_value(v)
    return meta, text[m.end():]


def load_content(content_dir: Path) -> list[dict]:
    """Markdown pages under docs-src/content/.

    <section>/index.md      -> /<section>/
    <section>/<slug>.md     -> /<section>/<slug>/
    research/YYYY-MM-DD-<slug>.md -> /research/YYYY/<slug>/
    """
    pages = []
    if not content_dir.exists():
        return pages
    for md in sorted(content_dir.rglob("*.md")):
        if md.name.upper() == "README.MD":
            continue
        meta, body = parse_frontmatter(md.read_text())
        rel = md.relative_to(content_dir).with_suffix("")
        parts = list(rel.parts)
        section = parts[0] if len(parts) > 1 else None
        stem = parts[-1]
        year = None
        dm = _DATE_PREFIX.match(stem)
        if dm:
            year, stem = dm.group(1), dm.group(2)
        slug = meta.get("slug") or stem
        if section == "research":
            year = year or str(meta.get("date", "1970"))[:4]
            url = f"/research/{year}/{slug}/"
        elif stem == "index" and section:
            slug = section
            url = f"/{section}/"
        elif section:
            url = f"/{section}/{slug}/"
        else:
            url = f"/{slug}/"
        tags = meta.get("tags") or []
        if isinstance(tags, str):
            tags = [tags]
        pages.append(
            {
                **meta,
                "slug": slug,
                "section": section or slug,
                "year": year,
                "tags": tags,
                "url": url,
                "body_md": body,
                "path": md,
                "order": int(meta["order"]) if str(meta.get("order", "")).isdigit() else 999,
            }
        )
    return pages


def load_categories(data_dir: Path, summary: dict) -> list[dict]:
    """Taxonomy from docs/data/categories.json ({_meta, categories[]}) merged
    with finding counts from summary.json. Categories present in scans but
    missing from the taxonomy still get a page with a generated name."""
    path = data_dir / "categories.json"
    known: dict[str, dict] = {}
    if path.exists():
        raw = json.loads(path.read_text())
        entries = raw["categories"] if isinstance(raw, dict) else raw
        for c in entries:
            known[c["slug"]] = c
    counts = summary.get("findings_by_category") or {}
    keys = list(counts) + [k for k in known if k not in counts]
    cats = []
    for key in keys:
        c = known.get(key, {})
        slug = ascii_slug(key)
        cats.append(
            {
                **c,
                "key": key,
                "slug": slug,
                "name": c.get("name") or key.replace("_", " ").title(),
                "count": counts.get(key, 0),
                "url": f"/categories/{slug}/",
            }
        )
    return sorted(cats, key=lambda c: -c["count"])
