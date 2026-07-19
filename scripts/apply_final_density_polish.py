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

# Mark the Working Papers list as a no-divider group.
html = replace_once(
    html,
    '''          <h3 class="subsection-title">WORK IN PROGRESS &amp; WORKING PAPERS</h3>
          <ol class="item-list">''',
    '''          <h3 class="subsection-title">WORK IN PROGRESS &amp; WORKING PAPERS</h3>
          <ol class="item-list no-dividers">''',
    "working-paper list class",
)

# Experience wording requested by the owner.
html = replace_once(
    html,
    '<p>Co-Investigator and Research Associate, Fudan Development Institute and related project collaborations</p>',
    '<p>Research Associate, Fudan Development Institute</p>',
    "Fudan experience wording",
)
html = replace_once(
    html,
    '<p>Research Assistant, School of Public Economics &amp; Administration</p>',
    '<p>RAt, School of Public Economics &amp; Administration</p>',
    "SUFE experience wording",
)
html = replace_once(
    html,
    '<p>Co-Investigator and Research Associate, School of International Economics &amp; Business</p>',
    '<p>Research Associate, School of International Economics &amp; Business</p>',
    "NUFE experience wording",
)
html = replace_once(
    html,
    '''                <h3><a href="DKU.pdf">Duke Kunshan University (Kunshan)</a></h3>
                <p>Coordinator Assistant, Office of Student Affairs</p>''',
    '''                <h3><a href="DKU.pdf">Duke Kunshan University (Kunshan)</a></h3>''',
    "DKU description removal",
)

# Left-top name uses the same font family as body copy.
css = replace_once(
    css,
    '  font-family: "Palatino Linotype", Palatino, Georgia, serif;\n  font-size: 1.05rem;',
    '  font-family: inherit;\n  font-size: 1.05rem;',
    "site-name font family",
)

# Remove internal dividers from the Working Papers, Reports, and Experience groups.
css = replace_once(
    css,
    '''.item { padding: 21px 0; border-top: 1px solid var(--line); }
.item:first-child { border-top: 0; padding-top: 0; }''',
    '''.item { padding: 21px 0; border-top: 1px solid var(--line); }
.item:first-child { border-top: 0; padding-top: 0; }
.item-list.no-dividers .item { border-top: 0; padding: 11px 0; }
.item-list.no-dividers .item:first-child { padding-top: 0; }''',
    "working-paper divider styles",
)
css = replace_once(
    css,
    '''.compact-list li {
  padding: 10px 0;
  border-top: 1px solid #eceff1;
}

.compact-list li:first-child {
  border-top: 0;
  padding-top: 0;
}''',
    '''.compact-list li {
  padding: 10px 0;
  border-top: 1px solid #eceff1;
}

.compact-list li:first-child {
  border-top: 0;
  padding-top: 0;
}

.report-list li {
  border-top: 0;
  padding: 7px 0;
}''',
    "report divider styles",
)
css = replace_once(
    css,
    '''.timeline-item:first-child { border-top: 0; padding-top: 0; }
#cv .timeline-item { grid-template-columns: 112px minmax(0, 1fr); gap: 16px; }''',
    '''.timeline-item:first-child { border-top: 0; padding-top: 0; }
#cv .timeline-item { grid-template-columns: 112px minmax(0, 1fr); gap: 16px; }
#experience .timeline-item { border-top: 0; padding: 10px 0; }
#experience .timeline-item:first-child { padding-top: 0; }''',
    "experience divider styles",
)

index_path.write_text(html, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")
