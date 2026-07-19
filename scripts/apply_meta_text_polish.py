#!/usr/bin/env python3
from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


index_path = Path("index.html")
css_path = Path("site-v2.css")

html = index_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

# Correct the only clear typographical error found in the visible British-English copy.
html = replace_once(
    html,
    '<p>RAt, School of Public Economics &amp; Administration</p>',
    '<p>RA, School of Public Economics &amp; Administration</p>',
    "SUFE role typo",
)

# Project and professional-role descriptions are one half-step smaller than body text.
css = replace_once(
    css,
    '.timeline-content p { margin: 0; color: #3c4043; }',
    '''.timeline-content p { margin: 0; color: #3c4043; }

#projects .timeline-content p,
#experience .timeline-content p {
  font-size: 0.96rem;
  line-height: 1.58;
}''',
    "project and experience metadata typography",
)

index_path.write_text(html, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")
