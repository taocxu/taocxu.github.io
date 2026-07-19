#!/usr/bin/env python3
"""Audit legacy anchor-to-destination mappings and local file targets.

The comparison is intentionally conservative. It normalises whitespace and
cosmetic quotation punctuation, while preserving the words attached to every
legacy destination. It also verifies that every relative link in the v2 page
points to an existing repository file or an in-page fragment.
"""

from __future__ import annotations

import argparse
import html
import re
import subprocess
import sys
import unicodedata
from collections import defaultdict
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


@dataclass(frozen=True)
class Link:
    text: str
    href: str


class TolerantAnchorParser(HTMLParser):
    """Extract anchors from valid and mildly malformed legacy HTML."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[Link] = []
        self._href: str | None = None
        self._text: list[str] = []

    def _finish(self) -> None:
        if self._href is not None:
            text = " ".join("".join(self._text).split())
            self.links.append(Link(text=text, href=html.unescape(self._href.strip())))
        self._href = None
        self._text = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        if tag == "a":
            self._finish()
            attributes = dict(attrs)
            self._href = attributes.get("href")
            self._text = []
        elif self._href is not None and tag in {"br", "p", "li", "h1", "h2", "h3", "div", "section"}:
            self._finish()

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "a":
            self._finish()
        elif self._href is not None and tag.lower() in {"p", "li", "div", "section"}:
            self._finish()

    def handle_data(self, data: str) -> None:
        if self._href is not None:
            self._text.append(data)

    def close(self) -> None:
        super().close()
        self._finish()


def extract_links(source: str) -> list[Link]:
    parser = TolerantAnchorParser()
    parser.feed(source)
    parser.close()
    return [link for link in parser.links if link.href]


def normalise_text(value: str) -> str:
    value = unicodedata.normalize("NFKC", html.unescape(value))
    translations = str.maketrans(
        {
            "‘": "'",
            "’": "'",
            "“": '"',
            "”": '"',
            "–": "-",
            "—": "-",
            "&": "and",
        }
    )
    value = value.translate(translations)
    value = re.sub(r"\s+", " ", value).strip()
    value = value.strip(" \t\r\n\"'[](),.;:")
    return value.casefold()


def normalise_href(value: str) -> str:
    value = html.unescape(value.strip())
    if value.startswith("http://") or value.startswith("https://"):
        parsed = urlparse(value)
        path = parsed.path.rstrip("/") or "/"
        return parsed._replace(path=path, fragment="").geturl()
    return value


def git_show(ref: str, path: str) -> str:
    proc = subprocess.run(
        ["git", "show", f"{ref}:{path}"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
    )
    return proc.stdout


def group_links(links: list[Link]) -> dict[str, list[Link]]:
    grouped: dict[str, list[Link]] = defaultdict(list)
    for link in links:
        grouped[normalise_href(link.href)].append(link)
    return grouped


def is_external(href: str) -> bool:
    return href.startswith(("http://", "https://", "mailto:", "tel:"))


def audit_local_targets(links: list[Link], root: Path) -> list[str]:
    missing: list[str] = []
    ids = set(re.findall(r'\bid=["\']([^"\']+)["\']', (root / "index.html").read_text(encoding="utf-8")))
    for link in links:
        href = html.unescape(link.href.strip())
        if not href or is_external(href):
            continue
        if href.startswith("#"):
            if href[1:] not in ids:
                missing.append(f"Missing in-page target {href!r} linked from {link.text!r}")
            continue
        target = unquote(href.split("#", 1)[0].split("?", 1)[0])
        if target and not (root / target).exists():
            missing.append(f"Missing local file {target!r} linked from {link.text!r}")
    return missing


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", default="eaef20cad5af4f34270cf0ab94ae67c6486bc4b0")
    parser.add_argument("--path", default="index.html")
    args = parser.parse_args()

    baseline_source = git_show(args.baseline, args.path)
    current_path = Path(args.path)
    current_source = current_path.read_text(encoding="utf-8")

    baseline_links = extract_links(baseline_source)
    current_links = extract_links(current_source)
    current_by_href = group_links(current_links)

    missing_destinations: list[Link] = []
    moved_or_changed_text: list[tuple[Link, list[str]]] = []
    preserved = 0

    for old in baseline_links:
        candidates = current_by_href.get(normalise_href(old.href), [])
        if not candidates:
            missing_destinations.append(old)
            continue
        old_text = normalise_text(old.text)
        if any(normalise_text(candidate.text) == old_text for candidate in candidates):
            preserved += 1
        else:
            moved_or_changed_text.append((old, [candidate.text for candidate in candidates]))

    missing_local = audit_local_targets(current_links, Path.cwd())

    print("Legacy hyperlink preservation audit")
    print(f"Baseline links found: {len(baseline_links)}")
    print(f"Current links found:  {len(current_links)}")
    print(f"Preserved mappings:   {preserved}")

    if missing_destinations:
        print("\nMissing legacy destinations:")
        for link in missing_destinations:
            print(f"- {link.text!r} -> {link.href}")

    if moved_or_changed_text:
        print("\nLegacy destinations attached to changed words:")
        for old, current_texts in moved_or_changed_text:
            print(f"- OLD {old.text!r} -> {old.href}")
            print(f"  NOW {current_texts!r}")

    if missing_local:
        print("\nBroken local or fragment targets:")
        for error in missing_local:
            print(f"- {error}")

    errors = len(missing_destinations) + len(moved_or_changed_text) + len(missing_local)
    if errors:
        print(f"\nFAILED: {errors} issue(s) require review.")
        return 1

    print("\nPASSED: every legacy destination remains attached to the same words, and all local targets exist.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
