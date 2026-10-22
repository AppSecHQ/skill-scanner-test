#!/usr/bin/env python3
"""Run NVIDIA SkillSpector (static mode, no LLM) over every skill that already
has a Cisco scan result, so the two scanners can be compared on the same corpus.

For each ``results/<name>-scan.json`` the skill directory recorded in
``skill_path`` is resolved to the local ``skills/`` tree and scanned with
``skillspector scan <dir> --no-llm --format json``. Output goes to
``results/skillspector/<name>-skillspector.json`` (full SkillSpector report plus
a ``_meta`` block linking it back to the Cisco result).

Usage:
    python scripts/run_skillspector.py                 # scan everything not yet scanned
    python scripts/run_skillspector.py --force -j 4    # rescan all, 4 workers
    python scripts/run_skillspector.py --limit 20      # smoke test
"""
from __future__ import annotations

import argparse
import json
import logging
import re
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

logger = logging.getLogger(__name__)

SCAN_TIMEOUT_SECONDS = 300
# Path prefixes used by the GitHub Actions runners; everything after ``skills/``
# is the same layout as the local ``skills/`` directory.
_CI_SKILLS_RE = re.compile(r"^(?:/workspace|/home/runner/work/[^/]+/[^/]+/scripts/\.\.|/home/runner/work/[^/]+/[^/]+)/skills/(.+)$")


def resolve_local_skill_path(skill_path: str, skills_dir: Path) -> Path | None:
    """Map the ``skill_path`` recorded in a scan result to a local directory."""
    if not skill_path:
        return None
    p = Path(skill_path)
    if p.is_dir():
        return p
    m = _CI_SKILLS_RE.match(skill_path)
    if m:
        local = skills_dir / m.group(1)
        if local.is_dir():
            return local
    # Last resort: the path may be relative to the repo root.
    if "/skills/" in skill_path:
        local = skills_dir / skill_path.split("/skills/", 1)[1]
        if local.is_dir():
            return local
    return None


def find_skillspector(explicit: str | None) -> str:
    if explicit:
        return explicit
    found = shutil.which("skillspector")
    if not found:
        raise SystemExit("skillspector not found; pass --skillspector /path/to/skillspector")
    return found


def scan_one(skillspector: str, skill_dir: Path, out_file: Path, cisco_file: Path) -> dict:
    """Run SkillSpector on one skill directory. Returns a slim summary row."""
    out_file.parent.mkdir(parents=True, exist_ok=True)
    cmd = [skillspector, "scan", str(skill_dir), "--no-llm", "--format", "json", "--output", str(out_file)]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=SCAN_TIMEOUT_SECONDS)
    except subprocess.TimeoutExpired:
        return {"name": out_file.stem, "error": "timeout"}
    # Exit 1 means risk_score > 50, which is a result, not a failure. Exit 2 is an error.
    if proc.returncode == 2 or not out_file.exists():
        return {"name": out_file.stem, "error": (proc.stderr or proc.stdout).strip()[-500:] or f"rc={proc.returncode}"}
    report = json.loads(out_file.read_text())
    report["_meta"] = {
        "cisco_result": cisco_file.name,
        "skill_dir": str(skill_dir),
        "scanned_at": datetime.now(timezone.utc).isoformat(),
        "mode": "static",
        "exit_code": proc.returncode,
    }
    out_file.write_text(json.dumps(report, indent=2))
    ra = report.get("risk_assessment", {})
    return {
        "name": out_file.stem,
        "score": ra.get("score"),
        "severity": ra.get("severity"),
        "recommendation": ra.get("recommendation"),
        "issues": len(report.get("issues", [])),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--results", type=Path, default=Path("results"))
    ap.add_argument("--skills-dir", type=Path, default=Path("skills"))
    ap.add_argument("--skillspector", default=None, help="Path to the skillspector executable")
    ap.add_argument("-j", "--jobs", type=int, default=4)
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--force", action="store_true", help="Rescan skills that already have output")
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", datefmt="%H:%M:%S")

    skillspector = find_skillspector(args.skillspector)
    out_dir = args.results / "skillspector"
    jobs: list[tuple[Path, Path, Path]] = []
    unresolved: list[str] = []
    for cisco_file in sorted(args.results.glob("*-scan.json")):
        stem = cisco_file.name[: -len("-scan.json")]
        out_file = out_dir / f"{stem}-skillspector.json"
        if out_file.exists() and not args.force:
            continue
        skill_path = json.loads(cisco_file.read_text()).get("skill_path", "")
        local = resolve_local_skill_path(skill_path, args.skills_dir)
        if local is None:
            unresolved.append(stem)
            continue
        jobs.append((local, out_file, cisco_file))
    if args.limit:
        jobs = jobs[: args.limit]
    logger.info("%d skills to scan, %d skipped (already done), %d without a local checkout",
                len(jobs), len(list(out_dir.glob("*.json"))) if out_dir.exists() else 0, len(unresolved))
    if unresolved:
        (out_dir if out_dir.exists() else args.results).mkdir(parents=True, exist_ok=True)
        (args.results / "skillspector-unresolved.json").write_text(json.dumps(sorted(unresolved), indent=1))

    rows = []
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futs = {pool.submit(scan_one, skillspector, d, o, c): o for d, o, c in jobs}
        for i, fut in enumerate(as_completed(futs), 1):
            row = fut.result()
            rows.append(row)
            if "error" in row:
                logger.warning("[%d/%d] %s: ERROR %s", i, len(jobs), row["name"], row["error"][:120])
            else:
                logger.info("[%d/%d] %s: %s score=%s issues=%s", i, len(jobs), row["name"],
                            row["severity"], row["score"], row["issues"])
    errors = [r for r in rows if "error" in r]
    logger.info("done: %d scanned, %d errors", len(rows) - len(errors), len(errors))
    return 1 if errors and len(errors) == len(rows) else 0


if __name__ == "__main__":
    sys.exit(main())
