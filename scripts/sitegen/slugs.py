"""Deterministic, collision-free URL slugs for skill names."""
from __future__ import annotations

import hashlib
import re
import unicodedata

MAX_LEN = 80
_NON_ALNUM = re.compile(r"[^a-z0-9]+")


def ascii_slug(text: str) -> str:
    """Lowercase ASCII slug; empty string if nothing survives transliteration."""
    norm = unicodedata.normalize("NFKD", text)
    ascii_text = norm.encode("ascii", "ignore").decode("ascii").lower()
    slug = _NON_ALNUM.sub("-", ascii_text).strip("-")
    return slug


def short_hash(text: str, length: int = 8) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:length]


def skill_slug(source: str, name: str) -> str:
    """Base slug (before collision handling) for a skill."""
    src = ascii_slug(source) or "unknown"
    base = ascii_slug(name)
    if not base:
        base = "skill-" + short_hash(name)
    slug = f"{src}-{base}"
    if len(slug) > MAX_LEN:
        slug = slug[:MAX_LEN].rstrip("-") + "-" + short_hash(name, 6)
    return slug


class SlugRegistry:
    """Assigns unique slugs; identical (source, name) always map to the same slug."""

    def __init__(self) -> None:
        self._by_key: dict[tuple[str, str], str] = {}
        self._taken: set[str] = set()

    def assign(self, source: str, name: str) -> str:
        key = (source, name)
        if key in self._by_key:
            return self._by_key[key]
        base = skill_slug(source, name)
        slug = base
        n = 2
        while slug in self._taken:
            slug = f"{base}-{n}"
            n += 1
        self._taken.add(slug)
        self._by_key[key] = slug
        return slug

    def items(self):
        return self._by_key.items()
