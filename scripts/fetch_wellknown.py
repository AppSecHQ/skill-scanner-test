#!/usr/bin/env python3
"""Download skills published under the ``.well-known`` Agent Skills convention.

skills.sh lists non-GitHub sources such as ``site/open.feishu.cn``. These hosts
publish ``https://<host>/.well-known/skills/index.json`` with
``{"skills": [{"name", "description", "files": [...]}]}`` and serve each file at
``https://<host>/.well-known/agent-skills/<name>/<file>``.

Skills are written to ``<skills-dir>/site-<host>/<name>/`` so they sit beside
cloned GitHub repos and can be scanned the same way.

Usage:
    python scripts/fetch_wellknown.py open.feishu.cn uizze.sh
    python scripts/fetch_wellknown.py open.feishu.cn --only lark-doc lark-okr
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path, PurePosixPath

sys.path.insert(0, str(Path(__file__).parent))
from pipeline_utils import get_session  # noqa: E402

logger = logging.getLogger(__name__)
MAX_FILE_BYTES = 5 * 1024 * 1024


def site_dirname(host: str) -> str:
    return "site-" + host.replace("/", "-")


def _safe_relative(name: str) -> PurePosixPath | None:
    p = PurePosixPath(name)
    if p.is_absolute() or any(part in ("..", "") for part in p.parts):
        return None
    return p


def fetch_index(host: str) -> list[dict]:
    session = get_session()
    r = session.get(f"https://{host}/.well-known/skills/index.json", timeout=30)
    r.raise_for_status()
    return r.json().get("skills", [])


def download_skill(host: str, skill: dict, dest_root: Path) -> Path | None:
    name = skill.get("name", "")
    rel_name = _safe_relative(name)
    if rel_name is None or len(rel_name.parts) != 1:
        logger.warning("%s: skipping skill with unsafe name %r", host, name)
        return None
    dest = dest_root / name
    session = get_session()
    files = skill.get("files") or ["SKILL.md"]
    if "SKILL.md" not in files:
        files = ["SKILL.md", *files]
    ok = 0
    for f in files:
        rel = _safe_relative(f)
        if rel is None:
            logger.warning("%s/%s: skipping unsafe file path %r", host, name, f)
            continue
        url = f"https://{host}/.well-known/agent-skills/{name}/{rel}"
        try:
            r = session.get(url, timeout=30)
        except Exception as e:  # noqa: BLE001
            logger.warning("%s: %s", url, e)
            continue
        if r.status_code != 200:
            logger.warning("%s: HTTP %s", url, r.status_code)
            continue
        if len(r.content) > MAX_FILE_BYTES:
            logger.warning("%s: %d bytes, skipped", url, len(r.content))
            continue
        out = dest / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(r.content)
        ok += 1
    if not (dest / "SKILL.md").exists():
        logger.warning("%s/%s: no SKILL.md fetched", host, name)
        return None
    (dest / ".wellknown-origin.json").write_text(json.dumps(
        {"host": host, "index": f"https://{host}/.well-known/skills/index.json", "name": name,
         "description": skill.get("description"), "files_fetched": ok, "files_listed": len(files)}, indent=1))
    return dest


def fetch_site(host: str, skills_dir: Path, only: set[str] | None = None) -> list[Path]:
    dest_root = skills_dir / site_dirname(host)
    dest_root.mkdir(parents=True, exist_ok=True)
    got = []
    for skill in fetch_index(host):
        if only and skill.get("name") not in only:
            continue
        d = download_skill(host, skill, dest_root)
        if d:
            got.append(d)
            logger.info("%s/%s: fetched", host, skill["name"])
    return got


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("hosts", nargs="+")
    ap.add_argument("--skills-dir", type=Path, default=Path("skills"))
    ap.add_argument("--only", nargs="*", default=None, help="Only these skill names")
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    total = 0
    for host in args.hosts:
        total += len(fetch_site(host, args.skills_dir, set(args.only) if args.only else None))
    logger.info("fetched %d skills", total)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
