#!/usr/bin/env python3
from pathlib import Path
import re


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


index_path = Path("index.html")
css_path = Path("site-v2.css")
html = index_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

# Expand and alphabetise the Research list. Entries containing conjunctions
# alternate between 'and' and '&' in alphabetical order, beginning with 'and'.
html = replace_once(
    html,
    '''          <ul class="research-interest-list">
            <li>Critical Urban &amp; Global Development Studies</li>
            <li>Development Economics</li>
            <li>Distribution of Power and Rents</li>
            <li>Evolutionary Institutional Economics</li>
            <li>Industrial Policy &amp; Development</li>
            <li>Institutional and Ideological Change</li>
            <li>Micro-foundations of Industrial Policy</li>
            <li>Political Economy of Development</li>
            <li>Political Economy of Institutions</li>
            <li>Political Settlements Framework</li>
          </ul>''',
    '''          <ul class="research-interest-list">
            <li>Agglomeration and Spillovers</li>
            <li>Applied Micro-econometrics</li>
            <li>Critical Urban &amp; Global Development Studies</li>
            <li>Development Economics</li>
            <li>Distribution of Power and Rents</li>
            <li>Evolutionary Institutional Economics</li>
            <li>Industrial Policy &amp; Development</li>
            <li>Industrial Value Chains and Ecosystems</li>
            <li>Institutional &amp; Ideological Change</li>
            <li>Micro-foundations of Industrial Policy</li>
            <li>New Structural Economics</li>
            <li>Pluralist Heterodox Economics</li>
            <li>Political Economy of Development</li>
            <li>Political Economy of Institutions</li>
            <li>Political Settlements Framework</li>
            <li>Productive Capabilities</li>
            <li>Strategy-as-Practice</li>
            <li>Techno-nationalism and Innovation</li>
            <li>Transport Policy &amp; Infrastructure</li>
            <li>Urban Industrialisation and Structural Change</li>
          </ul>''',
    "research-interest list",
)

# Replace the two ongoing appointments and standardise spacing around en dashes
# in all timeline date ranges only.
html = replace_once(
    html,
    '''              <div class="timeline-date">2025–2027</div>
              <div class="timeline-content">
                <h3>Fudan University (Shanghai)</h3>''',
    '''              <div class="timeline-date">2025 – Present</div>
              <div class="timeline-content">
                <h3>Fudan University (Shanghai)</h3>''',
    "Fudan appointment date",
)
html = replace_once(
    html,
    '''              <div class="timeline-date">2024–2027</div>
              <div class="timeline-content">
                <h3>Shanghai University of Finance and Economics (Shanghai)</h3>''',
    '''              <div class="timeline-date">2024 – Present</div>
              <div class="timeline-content">
                <h3>Shanghai University of Finance and Economics (Shanghai)</h3>''',
    "SUFE appointment date",
)

pattern = re.compile(r'(<div class="timeline-date">(?:<strong><em>)?)(\d{4})\s*–\s*(\d{4}|Present)((?:</em></strong>)?</div>)')
html = pattern.sub(lambda m: f"{m.group(1)}{m.group(2)} – {m.group(3)}{m.group(4)}", html)

# Increase the shared page width and use genuinely equal-width influence columns
# whenever the desktop or tablet layout has enough horizontal space.
css = replace_once(css, "  --content: 1120px;", "  --content: 1180px;", "overall content width")
css = replace_once(
    css,
    '''.influence-list {
  display: grid;
  grid-template-columns: repeat(3, max-content);
  justify-content: space-between;
  gap: 9px 30px;
  margin: 0;
  padding: 0;
  list-style: none;
}''',
    '''.influence-list {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 9px 30px;
  margin: 0;
  padding: 0;
  list-style: none;
}''',
    "desktop influence columns",
)
css = replace_once(
    css,
    '''  .influence-list { grid-template-columns: repeat(2, max-content); justify-content: space-between; gap: 10px 28px; }''',
    '''  .influence-list { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px 28px; }''',
    "tablet influence columns",
)

index_path.write_text(html, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")
