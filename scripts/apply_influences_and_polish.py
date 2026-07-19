#!/usr/bin/env python3
from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


index_path = Path("index.html")
css_path = Path("site-v2.css")
inventory_path = Path("LINK_INVENTORY.md")

html = index_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")
inventory = inventory_path.read_text(encoding="utf-8")

html = replace_once(
    html,
    '[Google Scholar]',
    '[GoogleScholar]',
    "Google Scholar label",
)

research_section_end = '''        </div>
      </div>
    </section>

    <section class="content-section" id="publications">'''

influences_section = '''        </div>
      </div>
    </section>

    <section class="content-section" id="influences">
      <div class="section-heading">
        <h2 class="section-label">INFLUENCES</h2>
        <div class="section-body">
          <ul class="influence-list">
            <li>Karl Marx</li>
            <li>Max Weber</li>
            <li>John Maynard Keynes</li>
            <li>Joseph Schumpeter</li>
            <li>Karl Polanyi</li>
            <li>Arthur Lewis</li>
            <li>Anthony Giddens</li>
            <li>Justin Yifu Lin</li>
            <li>Mushtaq Khan</li>
            <li>Ha-Joon Chang</li>
            <li>Hazel Gray</li>
            <li>Antonio Andreoni</li>
            <li>Albert Hirschman</li>
            <li>Freeman and Nelson</li>
            <li>Amartya Sen</li>
            <li>Alice Amsden</li>
            <li>Peter Evans</li>
            <li>Roy Bhaskar</li>
            <li>Yuen Yuen Ang</li>
            <li>Isabella Weber</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="content-section" id="publications">'''

html = replace_once(
    html,
    research_section_end,
    influences_section,
    "influences section insertion",
)

css = replace_once(
    css,
    '''.portrait-frame {
  background: #ffffff;
  padding: 9px;
  border: 1px solid #d0d0d0;
  box-shadow: 0 2px 8px rgba(60, 64, 67, 0.12);
}''',
    '''.portrait-frame {
  background: #ffffff;
  padding: 4px;
  border: 1px solid #d0d0d0;
  box-shadow: 0 2px 8px rgba(60, 64, 67, 0.12);
}''',
    "portrait padding",
)

css = replace_once(
    css,
    '''.research-interest-list li::before {
  content: "•";
  position: absolute;
  left: 0;
  top: 0;
  color: #303134;
  font-size: 0.92em;
}

.subsection-title {''',
    '''.research-interest-list li::before {
  content: "•";
  position: absolute;
  left: 0;
  top: 0;
  color: #303134;
  font-size: 0.92em;
}

.influence-list {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 10px 28px;
  margin: 0;
  padding: 0;
  list-style: none;
}

.influence-list li {
  position: relative;
  min-width: 0;
  padding-left: 1.05rem;
  line-height: 1.45;
}

.influence-list li::before {
  content: "•";
  position: absolute;
  left: 0;
  top: 0;
  color: #303134;
  font-size: 0.9em;
}

.subsection-title {''',
    "influence list styles",
)

css = replace_once(
    css,
    '''  .research-interest-list { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px 34px; }
}''',
    '''  .research-interest-list { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px 34px; }
  .influence-list { grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px 24px; }
}''',
    "tablet influence layout",
)

css = replace_once(
    css,
    '''  .research-interest-list { grid-template-columns: 1fr; gap: 10px; }
  .timeline-item { grid-template-columns: 1fr; gap: 4px; }''',
    '''  .research-interest-list { grid-template-columns: 1fr; gap: 10px; }
  .influence-list { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 9px 18px; }
  .timeline-item { grid-template-columns: 1fr; gap: 4px; }''',
    "mobile influence layout",
)

inventory = replace_once(
    inventory,
    '| [Google Scholar] | https://scholar.google.com/citations?user=KSSSjNQAAAAJ&hl=en | Added |',
    '| [GoogleScholar] | https://scholar.google.com/citations?user=KSSSjNQAAAAJ&hl=en | Added |',
    "inventory GoogleScholar label",
)

index_path.write_text(html, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")
inventory_path.write_text(inventory, encoding="utf-8")
