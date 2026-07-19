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

# Reorder MSc modules.
html = replace_once(
    html,
    '''                  <ul class="key-module-list">
                    <li>Anthropology of International Development</li>
                    <li>Politics and Theories of International Development</li>
                    <li>Resource Politics and Development</li>
                    <li>Interpreting International Development: Institutions &amp; Practices</li>
                    <li>Development, Poverty and Governance in Africa</li>
                    <li>Sustainability</li>
                    <li>Research Design</li>
                  </ul>''',
    '''                  <ul class="key-module-list">
                    <li>Anthropology of International Development</li>
                    <li>Resource Politics and Development</li>
                    <li>Politics and Theories of International Development</li>
                    <li>Interpreting International Development: Institutions &amp; Practices</li>
                    <li>Research Design</li>
                    <li>Development, Poverty and Governance in Africa</li>
                    <li>Sustainability</li>
                  </ul>''',
    "MSc module ordering",
)

# Reformat the three Edinburgh Centre of African Studies seminars.
html = replace_once(
    html,
    '<li>Landlord State and Precarious Urban Agriculture in Accra, (<a href="https://www.sps.ed.ac.uk/news-events/event/when-state-your-landlord-precarity-urban-agriculture-accra">Centre of African Studies, The University of Edinburgh</a>, 2024)</li>',
    '<li>Landlord State and Precarious Urban Agriculture in Accra (<a href="https://www.sps.ed.ac.uk/news-events/event/when-state-your-landlord-precarity-urban-agriculture-accra">University of Edinburgh Centre of African Studies</a>, Mar 2024)</li>',
    "Edinburgh landlord seminar",
)
html = replace_once(
    html,
    '<li>Political Economy of Extractivist Development in Ghana, (<a href="https://www.sps.ed.ac.uk/news-events/event/political-economy-extractivist-development-ghana">Centre of African Studies, The University of Edinburgh</a>, 2023)</li>',
    '<li>Political Economy of Extractivist Development in Ghana (<a href="https://www.sps.ed.ac.uk/news-events/event/political-economy-extractivist-development-ghana">University of Edinburgh Centre of African Studies</a>, Nov 2023)</li>',
    "Edinburgh extractivism seminar",
)
html = replace_once(
    html,
    '<li>Global Politics of African Identity: Pan-Africanism &amp; Afropolitanism, (<a href="https://www.sps.ed.ac.uk/news-events/event/global-politics-african-identity-pan-africanism-and-challenge-afropolitanism">Centre of African Studies, The University of Edinburgh</a>, 2023)</li>',
    '<li>Global Politics of African Identity: Pan-Africanism &amp; Afropolitanism (<a href="https://www.sps.ed.ac.uk/news-events/event/global-politics-african-identity-pan-africanism-and-challenge-afropolitanism">University of Edinburgh Centre of African Studies</a>, Oct 2023)</li>',
    "Edinburgh identity seminar",
)

# Refine and regroup Grants & Research Support.
html = replace_once(
    html,
    '<p>Research and Project Work Received/Conducted for Programmes with Support from</p>',
    '<p>Research and Project Work Received/Conducted for Programmes with Support from…</p>',
    "support introduction",
)
html = replace_once(
    html,
    '''          <ul class="support-list grouped-list">
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
          </ul>''',
    '''          <ul class="support-list grouped-list">
            <li>National Social Science Fund of China</li>
            <li>PRC Ministry of Education</li>
            <li class="group-start">Kunshan Federation of Humanities and Social Sciences Circles</li>
            <li>HQSW Agency for Foreign Affairs Administration</li>
            <li class="group-start">Nanjing University of Finance and Economics</li>
            <li class="institution-gap">Fudan University</li>
            <li class="institution-gap">University of Edinburgh</li>
            <li class="institution-gap">SOAS University of London</li>
            <li class="group-start">Jiangsu Administration for Market Regulation</li>
            <li>Kunshan Office of Foreign Affairs</li>
            <li>Kunshan Bureau of Finance</li>
            <li>Kunshan Administration for Market Regulation</li>
            <li>Kunshan Office of Press and Communication</li>
            <li>Shanghai, Jiangsu, Kunshan, Shuyang Governments and Affiliated Public Bodies</li>
          </ul>''',
    "support body ordering",
)

# Make the school/workshop/seminar listings half a size smaller and add whitespace
# between the four university entries without adding extra divider lines.
css = replace_once(
    css,
    '''.training-list li,
.support-list li {
  padding: 7px 0;
  border-top: 0;
}''',
    '''.training-list li,
.support-list li {
  padding: 7px 0;
  border-top: 0;
}

.training-list {
  font-size: 0.94rem;
  line-height: 1.55;
}

.support-list li.institution-gap {
  margin-top: 10px;
}''',
    "training and institution spacing",
)

index_path.write_text(html, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")
