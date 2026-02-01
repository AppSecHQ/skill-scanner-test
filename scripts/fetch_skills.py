#!/usr/bin/env python3
"""
Module 1: Fetch top skills from skill registries (skills.sh, clawhub.ai)
"""

import json
import logging
import requests
from pathlib import Path

from pipeline_utils import get_session, LOG_FORMAT, LOG_DATE_FORMAT

logger = logging.getLogger(__name__)

VALID_SOURCES = ["skills.sh", "clawhub"]


def _fetch_skillssh(n: int, offset: int, reverse: bool) -> list[dict]:
    """
    Fetch skills from skills.sh API.

    The API only supports `limit` and `offset` params and always returns
    skills sorted by installs descending. To get least-installed skills
    (--reverse), we fetch all skills and take from the end.

    Args:
        n: Number of skills to fetch
        offset: Number of skills to skip from the start
        reverse: If True, fetch lowest-installed skills instead of top

    Returns:
        List of normalized skill dictionaries
    """
    base_url = "https://skills.sh/api/skills"
    session = get_session()

    if reverse:
        # API has no sort param, so fetch all and reverse in memory
        response = session.get(base_url, params={"limit": 50000}, timeout=60)
        response.raise_for_status()
        all_skills = response.json().get("skills", [])
        all_skills.reverse()
    else:
        # Fetch only what we need using server-side offset/limit
        response = session.get(
            base_url, params={"limit": n, "offset": offset}, timeout=30
        )
        response.raise_for_status()
        all_skills = response.json().get("skills", [])
        offset = 0  # Already applied server-side

    # Apply offset and limit
    skills = all_skills[offset:offset + n]

    # Normalize to common schema
    result = []
    for i, skill in enumerate(skills, offset + 1):
        result.append({
            "rank": i,
            "name": skill["name"],
            "id": skill["id"],
            "repo": skill["topSource"],
            "installs": skill["installs"],
            "source": "skills.sh",
        })

    return result


def _fetch_clawhub(n: int, offset: int, reverse: bool) -> list[dict]:
    """
    Fetch skills from clawhub.ai API.

    Args:
        n: Number of skills to fetch
        offset: Number of skills to skip from the start
        reverse: If True, fetch lowest-installed skills instead of top

    Returns:
        List of normalized skill dictionaries
    """
    base_url = "https://www.clawhub.ai/api/v1/skills"

    # Fetch all skills (paginated)
    all_skills = []
    cursor = None
    session = get_session()

    while True:
        url = base_url
        if cursor:
            url = f"{base_url}?cursor={cursor}"

        response = session.get(url, timeout=30)
        response.raise_for_status()

        data = response.json()
        items = data.get("items", [])
        all_skills.extend(items)

        # Check if we have enough
        if len(all_skills) >= offset + n:
            break

        # Check for more pages
        cursor = data.get("nextCursor")
        if not cursor:
            break

    # Sort by installs (descending by default)
    all_skills.sort(key=lambda x: x.get("stats", {}).get("installsAllTime", 0), reverse=True)

    # Reverse if requested (lowest installs first)
    if reverse:
        all_skills = list(reversed(all_skills))

    # Apply offset and limit
    skills = all_skills[offset:offset + n]

    # Normalize to common schema
    result = []
    for i, skill in enumerate(skills, offset + 1):
        stats = skill.get("stats", {})
        result.append({
            "rank": i,
            "name": skill.get("displayName", skill.get("slug", "unknown")),
            "id": skill.get("slug", ""),
            "repo": None,  # Clawhub doesn't have GitHub repos
            "installs": stats.get("installsAllTime", 0),
            "source": "clawhub",
        })

    return result


def fetch_top_skills(
    n: int = 25,
    offset: int = 0,
    reverse: bool = False,
    source: str = "skills.sh",
) -> list[dict]:
    """
    Fetch skills from specified registry.

    Args:
        n: Number of skills to fetch
        offset: Number of skills to skip from the start
        reverse: If True, fetch lowest-installed skills instead of top
        source: Registry to fetch from ("skills.sh" or "clawhub")

    Returns:
        List of skill dictionaries with normalized schema:
        - rank: Position in the list
        - name: Skill display name
        - id: Unique identifier (id for skills.sh, slug for clawhub)
        - repo: GitHub repo (owner/repo) or None for clawhub
        - installs: Install count
        - source: Registry name
    """
    if source not in VALID_SOURCES:
        raise ValueError(f"Invalid source: {source}. Must be one of: {VALID_SOURCES}")

    if source == "skills.sh":
        return _fetch_skillssh(n, offset, reverse)
    elif source == "clawhub":
        return _fetch_clawhub(n, offset, reverse)


def save_inventory(skills: list[dict], output_path: Path) -> None:
    """Save skills inventory to JSON file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(skills, f, indent=2)
    logger.info("Saved %d skills to %s", len(skills), output_path)


def load_inventory(input_path: Path) -> list[dict]:
    """Load skills inventory from JSON file."""
    with open(input_path) as f:
        return json.load(f)


if __name__ == "__main__":
    import argparse

    logging.basicConfig(
        level=logging.INFO,
        format=LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT,
    )

    parser = argparse.ArgumentParser(description="Fetch top skills from skill registries")
    parser.add_argument("-n", "--count", type=int, default=25, help="Number of skills")
    parser.add_argument("--offset", type=int, default=0, help="Skip first N skills")
    parser.add_argument("--reverse", action="store_true", help="Fetch lowest-installed skills instead")
    parser.add_argument("--source", choices=VALID_SOURCES, default="skills.sh",
                        help="Registry to fetch from (default: skills.sh)")
    parser.add_argument("-o", "--output", type=Path, default=Path("skills/skill-inventory.json"))
    args = parser.parse_args()

    skills = fetch_top_skills(args.count, offset=args.offset, reverse=args.reverse, source=args.source)
    save_inventory(skills, args.output)

    label = "Bottom" if args.reverse else "Top"
    range_str = f"{args.offset + 1}-{args.offset + len(skills)}" if args.offset else f"1-{len(skills)}"
    logger.info("%s skills from %s (ranks %s):", label, args.source, range_str)
    for s in skills[:10]:
        repo_info = f" - {s['repo']}" if s['repo'] else ""
        logger.info("  %2d. %s (%s installs)%s", s['rank'], s['name'], f"{s['installs']:,}", repo_info)
