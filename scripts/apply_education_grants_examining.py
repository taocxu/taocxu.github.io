#!/usr/bin/env python3
from pathlib import Path

# One-shot update for the current owner-approved education, grants, and examining copy.

def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


index_path = Path("index.html")
css_path = Path("site-v2.css")
html = index_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

html = replace_once(
    html,
    "<p><strong>Working Dissertation Title:</strong> ‘Who Secured the Ladder? Industrial Policy Micro-foundations, Ideological Change, and Political Settlements’<br>",
    "<p><strong>Dissertation:</strong> (Working Title) ‘Who Secured the Ladder? Industrial Policy Micro-foundations, Ideological Change, and Political Settlements’<br>",
    "doctoral dissertation label",
)

html = replace_once(
    html,
    "MSc Dissertation in Financial Economics, Southwestern University of Finance and Economics&nbsp;&nbsp;·&nbsp;&nbsp;MSc Dissertation in International Business Studies, Hunan University&nbsp;&nbsp;·&nbsp;&nbsp;MSc Dissertation in International Business Studies, Shanghai University of Finance and Economics",
    "MSc Dissertation in Financial Economics, SWUFE&nbsp;&nbsp;·&nbsp;&nbsp;MSc Dissertation in International Business, HNU&nbsp;&nbsp;·&nbsp;&nbsp;MSc Dissertation in Business Studies, SUFE",
    "examining entries",
)

css = replace_once(
    css,
    '''.training-list li,
.support-list li {
  padding: 7px 0;
  border-top: 0;
}''',
    '''.training-list li,
.support-list li {
  padding: 6px 0;
  border-top: 0;
}''',
    "list row spacing",
)

css = replace_once(
    css,
    '''.support-list li.institution-gap {
  margin-top: 10px;
}''',
    '''.support-list li.institution-gap {
  margin-top: 5px;
}''',
    "institution spacing",
)

css = replace_once(
    css,
    '''.training-list li.group-start,
.support-list li.group-start {
  margin-top: 8px;
  padding-top: 16px;
  border-top: 1px solid #eceff1;
}''',
    '''.training-list li.group-start,
.support-list li.group-start {
  margin-top: 7px;
  padding-top: 12px;
  border-top: 1px solid #eceff1;
}''',
    "group separator spacing",
)

css = replace_once(
    css,
    '''.support-list li {
  position: relative;
  padding-left: 1.05rem;
}''',
    '''#grants .section-body > p {
  margin: 0 0 10px;
  font-size: 0.92rem;
  line-height: 1.5;
}

.support-list li {
  position: relative;
  padding-left: 1.05rem;
}''',
    "grant intro spacing",
)

index_path.write_text(html, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")
