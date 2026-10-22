#!/usr/bin/env python3
"""Scan every skill in one or more local target directories with the Cisco
scanner (static, behavioral and trigger analyzers; one process per target).

A target is either a cloned GitHub repo under ``skills/<owner>-<repo>`` or a
``.well-known`` site under ``skills/site-<host>`` (see fetch_wellknown.py).
Result files are named ``<target-dir>-<relative-skill-path>-scan.json`` so two
repos that both contain ``skills/tdd`` cannot overwrite each other.

Usage:
    python scripts/scan_targets.py mattpocock/skills heygen-com/hyperframes
    python scripts/scan_targets.py site:open.feishu.cn site:uizze.sh
    python scripts/scan_targets.py --all-new            # every skills/ dir with no result yet
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from run_scans import repo_to_dirname, run_batch_scan, sanitize_filename  # noqa: E402

logger = logging.getLogger(__name__)


def target_to_dir_and_origin(target: str, skills_dir: Path) -> tuple[Path, dict]:
    """``owner/repo`` -> skills/owner-repo; ``site:host`` -> skills/site-host."""
    if target.startswith("site:"):
        host = target[len("site:"):]
        return skills_dir / f"site-{host}", {"source": host, "repo_url": f"https://{host}/.well-known/skills/index.json"}
    if target.startswith("https://github.com/"):
        target = target[len("https://github.com/"):].rstrip("/")
    owner = target.split("/")[0]
    return skills_dir / repo_to_dirname(target), {"source": owner, "repo_url": f"https://github.com/{target}"}


def skill_names(repo_dir: Path) -> dict[Path, str]:
    """Map each skill directory to a result-file stem prefixed with the target dir name."""
    names: dict[Path, str] = {}
    for skill_md in sorted(repo_dir.rglob("SKILL.md")):
        if any(part in (".git", "node_modules") for part in skill_md.parts):
            continue
        rel = skill_md.parent.relative_to(repo_dir)
        stem = repo_dir.name if rel == Path(".") else f"{repo_dir.name}-{str(rel).replace('/', '-').lstrip('.')}"
        names[skill_md.parent] = sanitize_filename(stem)
    return names


def scan_target(target: str, skills_dir: Path, output_dir: Path, scanner_path: str) -> dict[str, dict] | None:
    repo_dir, origin = target_to_dir_and_origin(target, skills_dir)
    if not repo_dir.is_dir():
        logger.error("%s: %s does not exist (clone or fetch it first)", target, repo_dir)
        return None
    names = skill_names(repo_dir)
    if not names:
        logger.error("%s: no SKILL.md files", target)
        return None
    logger.info("%s: %d skill(s) in %s", target, len(names), repo_dir)
    return run_batch_scan(repo_dir=repo_dir, output_dir=output_dir, names=names,
                          scanner_path=scanner_path, origin=origin)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("targets", nargs="*", help="owner/repo or site:host")
    ap.add_argument("--skills-dir", type=Path, default=Path("skills"))
    ap.add_argument("-o", "--output", type=Path, default=Path("results"))
    ap.add_argument("--scanner", default="skill-scanner")
    ap.add_argument("--manifest", type=Path, default=None, help="Write a JSON summary of what was scanned")
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", datefmt="%H:%M:%S")
    if not args.targets:
        ap.error("no targets given")

    manifest = {}
    failed = []
    for target in args.targets:
        got = scan_target(target, args.skills_dir, args.output, args.scanner)
        if got is None:
            failed.append(target)
            continue
        manifest[target] = {
            "skills": len(got),
            "unsafe": sum(1 for r in got.values() if r.get("is_safe") is False),
            "results": sorted(got),
        }
        logger.info("%s: %d scanned, %d unsafe", target, manifest[target]["skills"], manifest[target]["unsafe"])
    if args.manifest:
        args.manifest.write_text(json.dumps(manifest, indent=1))
    if failed:
        logger.error("failed targets: %s", ", ".join(failed))
    return 1 if failed and not manifest else 0


if __name__ == "__main__":
    raise SystemExit(main())
