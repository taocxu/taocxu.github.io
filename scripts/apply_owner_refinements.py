#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


def regex_once(text: str, pattern: str, replacement: str, label: str) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.DOTALL)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one regex match, found {count}")
    return updated


index_path = Path("index.html")
css_path = Path("site-v2.css")
inventory_path = Path("LINK_INVENTORY.md")

index = index_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")
inventory = inventory_path.read_text(encoding="utf-8")

# Split the former umbrella Fudan project into two distinct projects.
old_fudan = '''            <article class="timeline-item">
              <div class="timeline-date">2025–Present</div>
              <div class="timeline-content">
                <h3>Innovation Policy, Connectivity and Corporate Change</h3>
                <p>Co-Investigator and Research Associate, Fudan Development Institute. Supervised by <a href="https://fddi.fudan.edu.cn/fddien/af/b1/c19479a307121/page.htm">Dr Li Liu</a>.</p>
              </div>
            </article>'''
new_fudan = '''            <article class="timeline-item">
              <div class="timeline-date">2025–Present</div>
              <div class="timeline-content">
                <h3>Digital Social Innovation and Emerging Industries</h3>
                <p>Supervised by <a href="https://fddi.fudan.edu.cn/fddien/af/b1/c19479a307121/page.htm">Dr Liu</a>, Research Associate, Fudan Development Institute</p>
              </div>
            </article>
            <article class="timeline-item">
              <div class="timeline-date">2025–Present</div>
              <div class="timeline-content">
                <h3>Tech Lead Firm Growth Pathway and Gradient-Heterogeneous Policy Toolkit</h3>
                <p>Supervised by <a href="https://fddi.fudan.edu.cn/fddien/af/b1/c19479a307121/page.htm">Dr Liu</a>, Research Associate, Fudan Development Institute</p>
              </div>
            </article>'''
index = replace_once(index, old_fudan, new_fudan, "split Fudan project")

index = replace_once(
    index,
    '                <p>Co-Investigator and Research Assistant, Shanghai University of Finance and Economics. Advised by <a href="https://cpi.sufe.edu.cn/45/1b/c13242a214299/page.htm">Dr Yi Zhu</a>.</p>',
    '                <p>Advised by <a href="https://cpi.sufe.edu.cn/45/1b/c13242a214299/page.htm">Prof Zhu</a>, RA, Shanghai University of Finance and Economics</p>',
    "revise SUFE project description",
)

index = replace_once(
    index,
    '                <p>Co-Investigator and Research Associate, National Social Science Fund of China Programme 19BJY109. Supervised by <a href="https://gmxy.nufe.edu.cn/info/1013/4509.htm">Prof Yabei Hu</a>.</p>',
    '                <p>Supervised by <a href="https://gmxy.nufe.edu.cn/info/1013/4509.htm">Prof Hu</a>, Co-Investigator and Research Associate, National Social Science Fund of China Programme 19BJY109</p>',
    "revise NSSF project description",
)

index = replace_once(
    index,
    '                <p>National ‘Culture, Science &amp; Health to Rural China’ Programme. <a href="http://sxx.youth.cn/zytz/hdgg/202112/W020211223591937418265.pdf">National Excellent Team Award, Provincial Special Team Award, NUFE Best Report Award 1st Class</a>.</p>',
    '                <p>Honoured by <a href="http://sxx.youth.cn/zytz/hdgg/202112/W020211223591937418265.pdf">National Excellent Team Award, Provincial Special Team Award, NUFE Best Report Award 1st Class</a>, National ‘Bringing Culture, Science &amp; Health to Rural China’ Programme</p>',
    "revise rural programme description",
)

index = replace_once(
    index,
    '                <h3>Digital Economy, New Retailing and Decent Work</h3>',
    '                <h3>Digital Economy and Decent Work</h3>',
    "rename digital economy project",
)

index = replace_once(
    index,
    '                <p>NUFE Undergraduate ‘Challenge Cup’ Academic Competition. Supervised by <a href="http://gmxy.nufe.edu.cn/info/1020/4536.htm">Prof Guanyi Li</a> and advised by <a href="https://baike.baidu.com/item/周春来/44246">Deputy Mayor of Lhasa and Permanent Secretary of Tibet Chunlai Zhou</a>.</p>',
    '                <p>Supervised by <a href="http://gmxy.nufe.edu.cn/info/1020/4536.htm">Dr Li</a> and advised by <a href="https://baike.baidu.com/item/周春来/44246">Deputy Mayor of Lhasa and Permanent Secretary of Tibet Zhou</a>, NUFE ‘Challenge Cup’ Academic Competition</p>',
    "revise Challenge Cup description",
)

index = replace_once(
    index,
    '                <p>Research Assistant, Jiangsu Administration for Market Regulation Programme. Supervised by <a href="http://gsglxy.nufe.edu.cn/info/1064/1553.htm">Prof Yingbao Huo</a>.</p>',
    '                <p>Supervised by <a href="http://gsglxy.nufe.edu.cn/info/1064/1553.htm">Prof Huo</a>, RA, Jiangsu Administration for Market Regulation Programme &amp; School of Business Administration</p>',
    "revise Jiangsu programme description",
)

# Use the requested abbreviation throughout the page.
index = index.replace("Undergraduate", "UG")

# Make the three parts of each degree entry visibly separate in HTML.
index = regex_once(
    index,
    r'''<p>Development Economics\s+Working Dissertation Title: ‘Who Secured the Ladder\? Industrial Policy Micro-foundations, Ideological Change, and Political Settlements’\s+Supervisor: (<a href="https://www\.soas\.ac\.uk/about/antonio-andreoni">Antonio Andreoni, Ph\.D\., Professor of Development Economics</a>)</p>''',
    r'''<p>Development Economics<br>
                  Working Dissertation Title: ‘Who Secured the Ladder? Industrial Policy Micro-foundations, Ideological Change, and Political Settlements’<br>
                  Supervisor: \1</p>''',
    "format DPhil entry",
)

index = regex_once(
    index,
    r'''<p>International Development Studies, Merit\s+Dissertation: ‘The Road Not Taken\? Industrial Policy and Political Settlements in China and Indonesia 1990–2022’\s+Supervisor: (<a href="https://www\.sps\.ed\.ac\.uk/staff/hazel-gray">Hazel Gray, Ph\.D\., Senior Lecturer in African Studies &amp; International Development</a>)</p>''',
    r'''<p>International Development Studies, Merit<br>
                  Dissertation: ‘The Road Not Taken? Industrial Policy and Political Settlements in China and Indonesia 1990–2022’<br>
                  Supervisor: \1</p>''',
    "format MSc entry",
)

index = regex_once(
    index,
    r'''<p>Industrial &amp; Commercial Economics, 1st: 91\.29\s+Dissertation: ‘Towards Sustainable Prosperity\? Policy Evaluation of Jiangsu Advanced Manufacturing Clusters’\s+Supervisor: (<a href="https://gmxy\.nufe\.edu\.cn/info/1019/4537\.htm">Yabei Hu, Ph\.D\., Professor of Industrial Economics</a>)</p>''',
    r'''<p>Industrial &amp; Commercial Economics, 1st: 91.29<br>
                  Dissertation: ‘Towards Sustainable Prosperity? Policy Evaluation of Jiangsu Advanced Manufacturing Clusters’<br>
                  Supervisor: \1</p>''',
    "format BSc entry",
)

# Keep the certificate link portable when the development branch is deployed.
index = replace_once(
    index,
    'href="https://raw.githack.com/taocxu/taocxu.github.io/feature/google-sites-v2/CertificateMMCM.pdf"',
    'href="CertificateMMCM.pdf"',
    "make modelling certificate link relative",
)

# Typography requested by the site owner.
css = replace_once(
    css,
    '  font-family: "Helvetica Neue", Arial, sans-serif;',
    '  font-family: Aptos, "Segoe UI", "Helvetica Neue", Arial, sans-serif;',
    "update body font stack",
)
css = replace_once(
    css,
    '  font-family: Georgia, "Times New Roman", serif;\n  font-size: 1.42rem;',
    '  font-family: "Palatino Linotype", Palatino, Georgia, serif;\n  font-size: 1.42rem;',
    "unify section-heading font",
)
css = css.replace('\n font-family: "Palatino Linotype", Palatino, Georgia, serif;', '\n  font-family: "Palatino Linotype", Palatino, Georgia, serif;')

inventory = replace_once(
    inventory,
    '| Economic and Mathematical Modelling | https://raw.githack.com/taocxu/taocxu.github.io/feature/google-sites-v2/CertificateMMCM.pdf |',
    '| Economic and Mathematical Modelling | CertificateMMCM.pdf |',
    "update certificate inventory",
)
inventory = inventory.replace(
    'linked to the branch preview certificate URL.',
    'linked to the local certificate file.',
)

index_path.write_text(index, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")
inventory_path.write_text(inventory, encoding="utf-8")
