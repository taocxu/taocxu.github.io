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
audit_path = Path("scripts/audit_links.py")
inventory_path = Path("LINK_INVENTORY.md")

html = index_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")
audit = audit_path.read_text(encoding="utf-8")
inventory = inventory_path.read_text(encoding="utf-8")

# Alphabetise research interests. For entries containing a conjunction, alternate
# between 'and' and '&' in their alphabetical order.
html = replace_once(
    html,
    '''          <ul class="research-interest-list">
            <li>Political Economy of Development</li>
            <li>Political Economy of Institutions</li>
            <li>Political Settlements Framework</li>
            <li>Evolutionary Institutional Economics</li>
            <li>Development Economics</li>
            <li>Institutional and Ideological Change</li>
            <li>Distribution of Power and Rents</li>
            <li>Critical Urban and Global Development Studies</li>
            <li>Industrial Policy and Development</li>
            <li>Micro-foundations of Industrial Policy</li>
          </ul>''',
    '''          <ul class="research-interest-list">
            <li>Critical Urban and Global Development Studies</li>
            <li>Development Economics</li>
            <li>Distribution of Power &amp; Rents</li>
            <li>Evolutionary Institutional Economics</li>
            <li>Industrial Policy and Development</li>
            <li>Institutional &amp; Ideological Change</li>
            <li>Micro-foundations of Industrial Policy</li>
            <li>Political Economy of Development</li>
            <li>Political Economy of Institutions</li>
            <li>Political Settlements Framework</li>
          </ul>''',
    "research-interest ordering",
)

# Remove brackets from button labels.
for old, new in [
    ('>[CV]</a>', '>CV</a>'),
    ('>[ORCID]</a>', '>ORCID</a>'),
    ('>[LinkedIn]</a>', '>LinkedIn</a>'),
    ('>[GoogleScholar]</a>', '>GoogleScholar</a>'),
    ('>[ResearchGate]</a>', '>ResearchGate</a>'),
    ('>[SSRN]</a>', '>SSRN</a>'),
]:
    html = replace_once(html, old, new, f"profile label {new}")

# Ensure clean, single-level bold labels in Education.
html = html.replace('<strong><strong><strong>Supervisor:</strong></strong></strong>', '<strong>Supervisor:</strong>')
html = html.replace('<strong><strong>Dissertation:</strong></strong>', '<strong>Dissertation:</strong>')
html = html.replace('                  Supervisor: <a href="https://www.sps.ed.ac.uk/staff/hazel-gray">', '                  <strong>Supervisor:</strong> <a href="https://www.sps.ed.ac.uk/staff/hazel-gray">', 1)
html = html.replace('                <p>Dissertation: ‘Towards Sustainable Prosperity?', '                <p><strong>Dissertation:</strong> ‘Towards Sustainable Prosperity?', 1)
html = html.replace('                  Supervisor: <a href="https://gmxy.nufe.edu.cn/info/1019/4537.htm">', '                  <strong>Supervisor:</strong> <a href="https://gmxy.nufe.edu.cn/info/1019/4537.htm">', 1)

# Add location to the Nanjing professional appointment.
html = replace_once(
    html,
    '<h3>Nanjing University of Finance and Economics</h3>',
    '<h3>Nanjing University of Finance and Economics (Nanjing)</h3>',
    "Nanjing experience location",
)

# Group schools, modelling, and seminars using category separators only.
html = replace_once(
    html,
    '<ul class="training-list">',
    '<ul class="training-list grouped-list">',
    "training grouped-list class",
)
html = replace_once(
    html,
    '<li>Economic and Mathematical Modelling - Chinese Society for Optimisation &amp; Economic Mathematics, 2021</li>',
    '<li class="group-start">Economic and Mathematical Modelling - Chinese Society for Optimisation &amp; Economic Mathematics, 2021</li>',
    "modelling group start",
)
html = replace_once(
    html,
    '<li>Firm Innovation Strategy Seminar, Profs Xiaobo Wu &amp; Wenwei Xu - Fudan Centre for Technovation Strategy, Dec 2025</li>',
    '<li class="group-start">Firm Innovation Strategy Seminar, Profs Xiaobo Wu &amp; Wenwei Xu - Fudan Centre for Technovation Strategy, Dec 2025</li>',
    "seminar group start",
)

# Reorder and group grant-support bodies.
old_support = '''          <ul class="support-list">
            <li>National Social Science Fund of China</li>
            <li>PRC Ministry of Education</li>
            <li>Kunshan Federation of Humanities and Social Sciences Circles</li>
            <li>HQSW Agency for Foreign Affairs Administration</li>
            <li>Nanjing University of Finance and Economics</li>
            <li>SOAS University of London</li>
            <li>University of Edinburgh</li>
            <li>School of International Economics and Business (NUFE)</li>
            <li>Fudan Development Institute (Fudan University)</li>
            <li>Shanghai, Jiangsu, Kunshan, Shuyang Governments and Affiliated Public Bodies</li>
            <li>Jiangsu Administration for Market Regulation</li>
            <li>Kunshan Office of Foreign Affairs</li>
            <li>Kunshan Bureau of Finance</li>
            <li>Kunshan Administration for Market Regulation</li>
            <li>Kunshan Office of Press and Communication</li>
          </ul>'''
new_support = '''          <ul class="support-list grouped-list">
            <li>National Social Science Fund of China</li>
            <li>PRC Ministry of Education</li>
            <li class="group-start">Kunshan Federation of Humanities and Social Sciences Circles</li>
            <li>HQSW Agency for Foreign Affairs Administration</li>
            <li class="group-start">Nanjing University of Finance and Economics (Nanjing)</li>
            <li>School of International Economics and Business (NUFE)</li>
            <li>SOAS University of London</li>
            <li>University of Edinburgh</li>
            <li>Fudan University</li>
            <li>Fudan Development Institute (Fudan University)</li>
            <li class="group-start">Shanghai, Jiangsu, Kunshan, Shuyang Governments and Affiliated Public Bodies</li>
            <li>Jiangsu Administration for Market Regulation</li>
            <li>Kunshan Office of Foreign Affairs</li>
            <li>Kunshan Bureau of Finance</li>
            <li>Kunshan Administration for Market Regulation</li>
            <li>Kunshan Office of Press and Communication</li>
          </ul>'''
html = replace_once(html, old_support, new_support, "support-list grouping")

# Render every visible middle-dot separator with the equivalent of two spaces on
# each side. HTML collapses ordinary spaces, so non-breaking spaces are used.
parts = re.split(r'(<[^>]+>)', html)
for i, part in enumerate(parts):
    if not part.startswith('<'):
        part = re.sub(r'\s*·\s*', '&nbsp;&nbsp;·&nbsp;&nbsp;', part)
        parts[i] = part
html = ''.join(parts)

# Category separators only for grouped training/support lists. Report rows retain
# their existing fine rules.
css = replace_once(
    css,
    '''.training-list li,
.compact-list li,
.support-list li {
  padding: 10px 0;
  border-top: 1px solid #eceff1;
}

.training-list li:first-child,
.compact-list li:first-child,
.support-list li:first-child {
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

.training-list li,
.support-list li {
  padding: 7px 0;
  border-top: 0;
}

.training-list li:first-child,
.support-list li:first-child {
  padding-top: 0;
}

.training-list li.group-start,
.support-list li.group-start {
  margin-top: 8px;
  padding-top: 16px;
  border-top: 1px solid #eceff1;
}''',
    "grouped-list separators",
)

# Record owner-approved profile-label changes in the legacy-link audit.
audit = replace_once(
    audit,
    '''        (
            normalise_text("[CV]"),
            normalise_href("CV.pdf"),
        ),''',
    '''        (
            normalise_text("[CV]"),
            normalise_href("CV.pdf"),
        ),
        (
            normalise_text("[ORCID]"),
            normalise_href("https://orcid.org/0000-0003-0510-3343"),
        ),
        (
            normalise_text("[LinkedIn]"),
            normalise_href("https://www.linkedin.com/in/tao-c-xu"),
        ),''',
    "profile-label audit exceptions",
)

# Keep the inventory aligned with the current labels.
for old, new in [
    ('| [CV] |', '| CV |'),
    ('| [ORCID] |', '| ORCID |'),
    ('| [LinkedIn] |', '| LinkedIn |'),
    ('| [GoogleScholar] |', '| GoogleScholar |'),
    ('| [ResearchGate] |', '| ResearchGate |'),
    ('| [SSRN] |', '| SSRN |'),
]:
    inventory = inventory.replace(old, new)

index_path.write_text(html, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")
audit_path.write_text(audit, encoding="utf-8")
inventory_path.write_text(inventory, encoding="utf-8")
