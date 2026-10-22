#!/usr/bin/env python3
"""Describe what a skill package contains, independent of what the scanner found.

A profile is written next to every scan result (results/profiles/<name>-profile.json)
and gives the site enough per-skill material to say what the skill does, which
files were in scope, what external hosts and environment variables it mentions,
and how big it is. Nothing here is a security judgement.

Usage:
    python skill_profile.py <skill_dir> [-o out.json]
    python skill_profile.py --backfill results/ [--skills-dir ../skills]
"""
from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

logger = logging.getLogger(__name__)

PROFILE_SCHEMA = 1
MAX_FILES_LISTED = 200
MAX_TEXT_BYTES = 2 * 1024 * 1024
MAX_DOMAINS = 30
MAX_ENV_VARS = 30
MAX_HEADINGS = 12
MAX_DESCRIPTION = 600

SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", ".mypy_cache", ".pytest_cache", "dist", "build"}

KIND_BY_EXT = {
    "doc": {".md", ".mdx", ".txt", ".rst", ".adoc"},
    "script": {".py", ".sh", ".bash", ".zsh", ".js", ".mjs", ".cjs", ".ts", ".tsx", ".jsx", ".rb", ".pl", ".ps1", ".bat", ".cmd", ".go", ".rs", ".php", ".lua", ".applescript", ".swift", ".java", ".kt", ".c", ".cpp", ".h"},
    "config": {".json", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".env", ".xml", ".plist", ".lock"},
    "data": {".csv", ".tsv", ".sql", ".parquet", ".jsonl", ".ndjson", ".html", ".htm", ".css", ".svg", ".tex", ".ipynb"},
    "image": {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".bmp"},
    "binary": {".zip", ".tar", ".gz", ".tgz", ".bz2", ".xz", ".7z", ".whl", ".pdf", ".docx", ".xlsx", ".pptx", ".so", ".dylib", ".dll", ".exe", ".bin", ".pyc", ".wasm", ".ttf", ".otf", ".woff", ".woff2", ".mp3", ".mp4", ".wav"},
}
EXT_KIND = {ext: kind for kind, exts in KIND_BY_EXT.items() for ext in exts}
TEXT_KINDS = {"doc", "script", "config", "data"}
LANG_BY_EXT = {
    ".py": "Python", ".sh": "Shell", ".bash": "Shell", ".zsh": "Shell", ".js": "JavaScript", ".mjs": "JavaScript",
    ".cjs": "JavaScript", ".ts": "TypeScript", ".tsx": "TypeScript", ".jsx": "JavaScript", ".rb": "Ruby",
    ".pl": "Perl", ".ps1": "PowerShell", ".bat": "Batch", ".cmd": "Batch", ".go": "Go", ".rs": "Rust",
    ".php": "PHP", ".lua": "Lua", ".applescript": "AppleScript", ".swift": "Swift", ".java": "Java",
    ".kt": "Kotlin", ".c": "C", ".cpp": "C++", ".h": "C",
}

_FRONTMATTER = re.compile(r"\A﻿?---\s*\r?\n(.*?)\r?\n---\s*(?:\r?\n|\Z)", re.S)
_URL = re.compile(r"https?://([A-Za-z0-9.-]+\.[A-Za-z]{2,})(?::\d+)?(?=[/\s\"'`<>)\]}|,;]|$)")
_ENV = re.compile(r"(?:\$\{?|os\.environ(?:\.get)?\(\s*[\"']|process\.env\.|getenv\(\s*[\"'])([A-Z][A-Z0-9_]{2,})")
_ENV_DOC = re.compile(r"`([A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+)`")
_HEADING = re.compile(r"^#{1,3}\s+(.+?)\s*#*\s*$", re.M)
_TOOL_LINE = re.compile(r"^\s*-\s*(.+?)\s*$")

IGNORED_DOMAINS = {"localhost", "schema.org", "www.w3.org", "spdx.org", "opensource.org", "creativecommons.org"}
IGNORED_DOMAIN_SUFFIXES = (".local", ".test", ".invalid", "example.com", "example.org", "example.net")
# Shell-local and cosmetic variables that read as environment variables to the regex.
NOISE_ENV = {"TODO", "FIXME", "README", "SKILL", "API", "URL", "JSON", "HTTP", "HTTPS", "PATH", "HOME", "USER", "PWD", "SHELL",
             "TRUE", "FALSE", "NULL", "NONE", "GET", "POST", "PUT", "DELETE", "PATCH", "BASH_SOURCE", "SCRIPT_DIR", "SCRIPT_PATH",
             "RED", "GREEN", "YELLOW", "BLUE", "CYAN", "MAGENTA", "BOLD", "NC", "RESET", "DIM", "IFS", "RANDOM", "LINENO", "EUID",
             "OSTYPE", "HOSTNAME", "TMPDIR", "TEMP", "TMP", "LANG", "LC_ALL", "TERM", "EDITOR", "PAGER", "PS1", "OLDPWD"}
# Keep only names that plausibly configure or authenticate something.
ENV_KEEP = re.compile(r"KEY|TOKEN|SECRET|PASS|API|URL|URI|ENDPOINT|HOST|_ID$|^ID_|ACCOUNT|WEBHOOK|CRED|AUTH|REGION|BUCKET|ORG|PROJECT|DSN|EMAIL|USERNAME|CLIENT|TENANT|DOMAIN|PORT|DATABASE|DB_|REDIS|MONGO|AWS_|GCP_|GOOGLE_|AZURE_|OPENAI|ANTHROPIC|HF_|HUGGING|GITHUB|GITLAB|SLACK|DISCORD|TELEGRAM|NOTION|STRIPE|TWILIO|SENDGRID|VERCEL|CLOUDFLARE|SUPABASE|FIREBASE|CONFIG|HOME$|DIR$|PATH$|MODEL|PROVIDER|CHANNEL|WORKSPACE|TEAM|PROFILE|LICENSE")


# ------------------------------------------------------------------ frontmatter
def _yaml_scalar(v: str):
    v = v.strip()
    if not v:
        return ""
    if v[0] in "\"'" and v[-1] == v[0] and len(v) >= 2:
        return v[1:-1]
    if v.startswith("[") and v.endswith("]"):
        return [x.strip().strip("\"'") for x in v[1:-1].split(",") if x.strip()]
    if v.startswith("{") and v.endswith("}"):
        try:
            return json.loads(v)
        except json.JSONDecodeError:
            return v
    return v


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Small YAML subset: scalar keys, inline lists/objects, one level of
    nested `key:` followed by indented `- item` or `sub: value` lines, and
    `key: >` / `key: |` block scalars. Good enough for SKILL.md in the wild;
    anything stranger is kept as raw text."""
    m = _FRONTMATTER.match(text)
    if not m:
        return {}, text
    meta: dict = {}
    lines = m.group(1).splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        i += 1
        if not line.strip() or line.lstrip().startswith("#") or line.startswith((" ", "\t")):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value in (">", "|", ">-", "|-"):
            block = []
            while i < len(lines) and (lines[i].startswith((" ", "\t")) or not lines[i].strip()):
                block.append(lines[i].strip())
                i += 1
            meta[key] = (" " if value.startswith(">") else "\n").join(x for x in block if x).strip()
            continue
        if value == "":
            block = []
            while i < len(lines) and (lines[i].startswith((" ", "\t")) or not lines[i].strip()):
                block.append(lines[i])
                i += 1
            items = [_TOOL_LINE.match(b).group(1).strip("\"'") for b in block if _TOOL_LINE.match(b)]
            if items:
                meta[key] = items
            else:
                sub: dict = {}
                for b in block:
                    if ":" in b:
                        k2, _, v2 = b.strip().partition(":")
                        sub[k2.strip()] = _yaml_scalar(v2)
                meta[key] = sub if sub else ""
            continue
        meta[key] = _yaml_scalar(value)
    return meta, text[m.end():]


def _as_list(v) -> list[str]:
    if v is None or v == "":
        return []
    if isinstance(v, list):
        return [str(x) for x in v]
    if isinstance(v, dict):
        return [str(k) for k in v]
    return [t for t in re.split(r"[,\s]+", str(v)) if t]


# ------------------------------------------------------------------ profiling
PROJECT_ROOT = Path(__file__).resolve().parent.parent


def _git_commit(path: Path, stop_at: Path | None = PROJECT_ROOT) -> str | None:
    """HEAD of the enclosing skill checkout, read from .git directly so profiling
    never shells out. The walk stops before stop_at (this project's own root) so
    a skill downloaded as plain files does not report skill-scanner-test's HEAD."""
    path = path.resolve()
    for parent in [path, *path.parents]:
        if stop_at is not None and parent == stop_at.resolve():
            return None
        git = parent / ".git"
        if git.is_file():  # worktree or submodule: "gitdir: <path>"
            try:
                target = git.read_text().strip().split(":", 1)[1].strip()
                git = (parent / target).resolve()
            except (OSError, IndexError):
                return None
        if not git.is_dir():
            continue
        try:
            head = (git / "HEAD").read_text().strip()
            if head.startswith("ref:"):
                ref = head.split(":", 1)[1].strip()
                ref_file = git / ref
                if ref_file.is_file():
                    return ref_file.read_text().strip()[:12]
                packed = git / "packed-refs"
                if packed.is_file():
                    for line in packed.read_text().splitlines():
                        if line.endswith(" " + ref):
                            return line.split(" ", 1)[0][:12]
                return None
            return head[:12] if head else None
        except OSError:
            return None
    return None


def _iter_files(root: Path):
    for p in sorted(root.rglob("*")):
        if any(part in SKIP_DIRS for part in p.relative_to(root).parts):
            continue
        if p.is_file() and not p.is_symlink():
            yield p


def _read_text(p: Path) -> str:
    try:
        if p.stat().st_size > MAX_TEXT_BYTES:
            return ""
        return p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def profile_skill(skill_dir: Path) -> dict:
    skill_dir = Path(skill_dir)
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        alt = next((p for p in skill_dir.iterdir() if p.is_file() and p.name.lower() == "skill.md"), None) if skill_dir.is_dir() else None
        skill_md = alt or skill_md

    meta: dict = {}
    body = ""
    if skill_md.is_file():
        meta, body = parse_frontmatter(_read_text(skill_md))

    files = []
    languages: dict[str, int] = {}
    kinds: dict[str, int] = {}
    total_bytes = 0
    domains: dict[str, int] = {}
    env_vars: dict[str, int] = {}
    for p in _iter_files(skill_dir):
        rel = p.relative_to(skill_dir).as_posix()
        size = p.stat().st_size
        ext = p.suffix.lower()
        kind = EXT_KIND.get(ext)
        if kind is None:
            kind = "script" if (ext == "" and _looks_executable(p)) else "other"
        total_bytes += size
        kinds[kind] = kinds.get(kind, 0) + 1
        if kind == "script":
            lang = LANG_BY_EXT.get(ext, "Other")
            languages[lang] = languages.get(lang, 0) + 1
        files.append({"path": rel, "bytes": size, "kind": kind})
        if kind in TEXT_KINDS or kind == "other" and size < 256 * 1024:
            text = _read_text(p)
            for host in _URL.findall(text):
                host = host.lower()
                if host not in IGNORED_DOMAINS and not host.endswith(IGNORED_DOMAIN_SUFFIXES):
                    domains[host] = domains.get(host, 0) + 1
            found = list(_ENV.findall(text)) + (list(_ENV_DOC.findall(text)) if kind == "doc" else [])
            for var in found:
                if var not in NOISE_ENV and ENV_KEEP.search(var):
                    env_vars[var] = env_vars.get(var, 0) + 1

    files.sort(key=lambda f: (f["path"].count("/"), f["path"]))
    description = str(meta.get("description") or "").strip()
    if len(description) > MAX_DESCRIPTION:
        description = description[: MAX_DESCRIPTION - 1].rsplit(" ", 1)[0] + "…"

    requires = {}
    md = meta.get("metadata")
    if isinstance(md, dict):
        for owner in md.values():
            if isinstance(owner, dict) and isinstance(owner.get("requires"), dict):
                for k, v in owner["requires"].items():
                    requires[k] = _as_list(v)

    return {
        "schema": PROFILE_SCHEMA,
        "name": str(meta.get("name") or skill_dir.name),
        "description": description,
        "license": str(meta.get("license") or "") or None,
        "compatibility": str(meta.get("compatibility") or "") or None,
        "version": str(meta.get("version") or "") or None,
        "homepage": str(meta.get("homepage") or meta.get("repository") or "") or None,
        "allowed_tools": _as_list(meta.get("allowed-tools") or meta.get("tools")),
        "requires": requires or None,
        "frontmatter_keys": sorted(meta),
        "skill_md": {
            "present": skill_md.is_file(),
            "bytes": skill_md.stat().st_size if skill_md.is_file() else 0,
            "words": len(body.split()),
            "headings": [h.strip() for h in _HEADING.findall(body)][:MAX_HEADINGS],
        },
        "file_count": len(files),
        "total_bytes": total_bytes,
        "kinds": dict(sorted(kinds.items())),
        "languages": dict(sorted(languages.items(), key=lambda kv: -kv[1])),
        "files": files[:MAX_FILES_LISTED],
        "files_truncated": max(0, len(files) - MAX_FILES_LISTED),
        "domains": [d for d, _ in sorted(domains.items(), key=lambda kv: (-kv[1], kv[0]))[:MAX_DOMAINS]],
        "env_vars": [v for v, _ in sorted(env_vars.items(), key=lambda kv: (-kv[1], kv[0]))[:MAX_ENV_VARS]],
        "git_commit": _git_commit(skill_dir),
        "profiled_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def _looks_executable(p: Path) -> bool:
    try:
        with open(p, "rb") as fh:
            return fh.read(2) == b"#!"
    except OSError:
        return False


def write_profile(skill_dir: Path, output_dir: Path, name: str) -> Path | None:
    """Profile skill_dir into output_dir/profiles/<name>-profile.json. Never raises."""
    try:
        prof = profile_skill(skill_dir)
        out_dir = output_dir / "profiles"
        out_dir.mkdir(parents=True, exist_ok=True)
        out = out_dir / f"{name}-profile.json"
        out.write_text(json.dumps(prof, indent=1, ensure_ascii=False) + "\n")
        return out
    except Exception as e:  # profiling must never fail a scan
        logger.warning("Could not profile %s: %s", skill_dir, e)
        return None


# ------------------------------------------------------------------ backfill
def _local_skill_dir(skill_path: str, skills_dir: Path) -> Path | None:
    """Map a recorded scan path (CI, local, or ./ shortened) onto skills_dir."""
    if not skill_path:
        return None
    norm = skill_path.replace("\\", "/")
    marker = "/skills/"
    idx = norm.find(marker)
    while idx != -1:
        cand = skills_dir / norm[idx + len(marker):]
        if cand.is_dir():
            return cand
        idx = norm.find(marker, idx + 1)
    cand = Path(norm)
    return cand if cand.is_dir() else None


def backfill(results_dir: Path, skills_dir: Path, force: bool = False) -> tuple[int, int, list[str]]:
    scan_files = sorted(set(results_dir.glob("*-scan.json")) | set(results_dir.glob(".*-scan.json")))
    done = skipped = 0
    missing: list[str] = []
    for jf in scan_files:
        name = jf.name[: -len("-scan.json")]
        out = results_dir / "profiles" / f"{name}-profile.json"
        if out.exists() and not force:
            skipped += 1
            continue
        try:
            scan = json.loads(jf.read_text())
        except (json.JSONDecodeError, OSError):
            missing.append(name)
            continue
        skill_dir = _local_skill_dir(scan.get("skill_path") or scan.get("skill_directory") or "", skills_dir)
        if skill_dir is None:
            missing.append(name)
            continue
        if write_profile(skill_dir, results_dir, name):
            done += 1
        else:
            missing.append(name)
    return done, skipped, missing


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("skill_dir", nargs="?", type=Path, help="Skill directory to profile")
    ap.add_argument("-o", "--output", type=Path, help="Write JSON here instead of stdout")
    ap.add_argument("--backfill", type=Path, metavar="RESULTS_DIR", help="Profile every *-scan.json in RESULTS_DIR")
    ap.add_argument("--skills-dir", type=Path, default=Path(__file__).resolve().parent.parent / "skills")
    ap.add_argument("--force", action="store_true", help="Rewrite profiles that already exist")
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    if args.backfill:
        done, skipped, missing = backfill(args.backfill, args.skills_dir, args.force)
        print(f"profiled {done}, kept {skipped}, no local copy for {len(missing)}")
        for m in missing[:20]:
            print("  missing:", m)
        return 0
    if not args.skill_dir:
        ap.error("skill_dir or --backfill required")
    prof = profile_skill(args.skill_dir)
    text = json.dumps(prof, indent=1, ensure_ascii=False)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
