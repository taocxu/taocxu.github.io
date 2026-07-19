#!/usr/bin/env python3
from pathlib import Path
import re


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


index_path = Path("index.html")
audit_path = Path("scripts/audit_links.py")
inventory_path = Path("LINK_INVENTORY.md")

html = index_path.read_text(encoding="utf-8")
audit = audit_path.read_text(encoding="utf-8")
inventory = inventory_path.read_text(encoding="utf-8")

# Project affiliations and role descriptions.
project_updates = {
    '<p>Supervised by <a href="https://gmxy.nufe.edu.cn/info/1013/4509.htm">Prof Hu</a>, Co-Investigator and Research Associate, National Social Science Fund of China Programme 19BJY109</p>':
    '<p>Supervised by <a href="https://gmxy.nufe.edu.cn/info/1013/4509.htm">Prof Hu</a>, Co-Investigator and Research Associate, National Social Science Fund of China Programme 19BJY109, Nanjing University of Finance and Economics</p>',

    '<p>Honoured by <a href="http://sxx.youth.cn/zytz/hdgg/202112/W020211223591937418265.pdf">National Excellent Team Award, Provincial Special Team Award, NUFE Best Report Award 1st Class</a>, National ‘Bringing Culture, Science &amp; Health to Rural China’ Programme</p>':
    '<p>Honoured by <a href="http://sxx.youth.cn/zytz/hdgg/202112/W020211223591937418265.pdf">National Excellent Team Award, Provincial Special Team Award, NUFE Best Report Award 1st Class</a>, National ‘Bringing Culture, Science &amp; Health to Rural China’ Programme, Nanjing University of Finance and Economics</p>',

    '<p>Supervised by <a href="http://gmxy.nufe.edu.cn/info/1020/4536.htm">Dr Li</a> and advised by <a href="https://baike.baidu.com/item/周春来/44246">Deputy Mayor of Lhasa and Permanent Secretary of Tibet Zhou</a>, NUFE ‘Challenge Cup’ Academic Competition</p>':
    '<p>Supervised by <a href="http://gmxy.nufe.edu.cn/info/1020/4536.htm">Dr Li</a> and advised by <a href="https://baike.baidu.com/item/周春来/44246">Deputy Mayor of Lhasa and Permanent Secretary of Tibet Zhou</a>, ‘Challenge Cup’ Academic Competition, Nanjing University of Finance and Economics</p>',

    '<p>Supervised by <a href="http://gmxy.nufe.edu.cn/info/1020/4647.htm">Prof Chen</a>, Principal Investigator and Team Leader, NUFE UG Research Programme</p>':
    '<p>Supervised by <a href="http://gmxy.nufe.edu.cn/info/1020/4647.htm">Prof Chen</a>, Principal Investigator and Team Leader, UG Research Programme, Nanjing University of Finance and Economics</p>',

    '<p>Supervised by <a href="http://gsglxy.nufe.edu.cn/info/1064/1553.htm">Prof Huo</a>, RA, Jiangsu Administration for Market Regulation Programme &amp; NUFE School of Business Administration</p>':
    '<p>Supervised by <a href="http://gsglxy.nufe.edu.cn/info/1064/1553.htm">Prof Huo</a>, RA, Jiangsu Administration for Market Regulation Programme &amp; School of Business Administration, Nanjing University of Finance and Economics</p>',
}
for old, new in project_updates.items():
    html = replace_once(html, old, new, "project wording")

# Reports and presentation metadata.
html = replace_once(
    html,
    'advised by Prof Dr Wenwu Zhang, MPRA 112908, 2021',
    'advised by Prof Zhang, MPRA 112908, 2021',
    "Prof Zhang wording",
)
html = replace_once(
    html,
    'with Y Gu, Y Wang, Dapeng Zhu, Wei Li, Zhenyu Zhang, Jingxia Hou and Yuhan Yang, 2021',
    'with Yukun Gu, Yibo Wang, Dapeng Zhu, Wei Li, Zhenyu Zhang, Jingxia Hou and Yuhan Yang, advised by Prof Jinguo Tao, 2021',
    "survey author names",
)

# Key modules for each degree.
html = replace_once(
    html,
    '''                <p>Working Dissertation Title: ‘Who Secured the Ladder? Industrial Policy Micro-foundations, Ideological Change, and Political Settlements’<br>
                  Supervisor: <a href="https://www.soas.ac.uk/about/antonio-andreoni">Antonio Andreoni, Ph.D., Professor of Development Economics</a></p>''',
    '''                <p>Working Dissertation Title: ‘Who Secured the Ladder? Industrial Policy Micro-foundations, Ideological Change, and Political Settlements’<br>
                  Supervisor: <a href="https://www.soas.ac.uk/about/antonio-andreoni">Antonio Andreoni, Ph.D., Professor of Development Economics</a><br>
                  <strong>Key Modules:</strong> Research Methods for Development Economics · Schools of Thought in Economics · Political Economy of Growth and Development · Political Economy of Institutions · Development Macroeconomics &amp; Microeconomics</p>''',
    "PhD key modules",
)
html = replace_once(
    html,
    '''                <p>Dissertation: ‘The Road Not Taken? Industrial Policy and Political Settlements in China and Indonesia 1990–2022’<br>
                  Supervisor: <a href="https://www.sps.ed.ac.uk/staff/hazel-gray">Hazel Gray, Ph.D., Senior Lecturer in African Studies &amp; International Development</a></p>''',
    '''                <p>Dissertation: ‘The Road Not Taken? Industrial Policy and Political Settlements in China and Indonesia 1990–2022’<br>
                  Supervisor: <a href="https://www.sps.ed.ac.uk/staff/hazel-gray">Hazel Gray, Ph.D., Senior Lecturer in African Studies &amp; International Development</a><br>
                  <strong>Key Modules:</strong> Anthropology of International Development · Politics and Theories of International Development (Political Economy of Development) · Resource Politics and Development · Interpreting International Development: Institutions &amp; Practices · Development, Poverty and Governance in Africa · Sustainability · Research Design</p>''',
    "MSc key modules",
)
html = replace_once(
    html,
    '''                <p>Dissertation: ‘Towards Sustainable Prosperity? Policy Evaluation of Jiangsu Advanced Manufacturing Clusters’<br>
                  Supervisor: <a href="https://gmxy.nufe.edu.cn/info/1019/4537.htm">Yabei Hu, Ph.D., Professor of Industrial Economics</a></p>''',
    '''                <p>Dissertation: ‘Towards Sustainable Prosperity? Policy Evaluation of Jiangsu Advanced Manufacturing Clusters’<br>
                  Supervisor: <a href="https://gmxy.nufe.edu.cn/info/1019/4537.htm">Yabei Hu, Ph.D., Professor of Industrial Economics</a><br>
                  <strong>Key Modules:</strong> Microeconomics · Macroeconomics · Econometrics · International Economics · Regional Market and Interregional Trade · Regional &amp; Urban Economics · Business Economics · Industrial Organisation · Marketing · Platform Economics · Retailing and Wholesaling Studies · Business Design &amp; Innovation · Economic History</p>''',
    "BSc key modules",
)

# Rename and comprehensively reorder the academic training section.
html = replace_once(
    html,
    '<h3 class="subsection-title">ACADEMIC TRAINING</h3>',
    '<h3 class="subsection-title">WINTER/SUMMER SCHOOLS, WORKSHOPS &amp; SEMINARS</h3>',
    "academic training heading",
)

old_training = '''          <ul class="training-list">
            <li>Aug 2023, 2025, 2026 · <a href="https://english.njau.edu.cn/">Nanjing Agricultural University</a>, Research Methodology in Applied Economics · <a href="NAURoP.pdf">[Certificate-Outstanding Student Award]</a></li>
            <li>Jul 2024, 2025, 2026 · <a href="https://sem.ucas.ac.cn/en">Chinese Academy of Sciences</a>, AI in Economic Theory &amp; Methodology, Advanced/Graduate · <a href="UCASRoP.pdf">[Certificate]</a></li>
            <li>Jul 2025, 2026 · <a href="https://econ.sufe.edu.cn/main.htm">Shanghai University of Finance and Economics</a>, Frontiers in Microeconomics &amp; Econometrics</li>
            <li>Jul 2023, 2024 · <a href="https://en.whu.edu.cn/">Wuhan University</a>, Marxian Political Economy · <a href="WHURoP.pdf">[Certificate-Distinguished Paper Award]</a></li>
            <li>Aug 2023 · <a href="https://en.njnu.edu.cn/">Nanjing Normal University</a>, Big Data Analytics in GISciences · <a href="NNURoP.pdf">[Certificate-Outstanding Student Award]</a></li>
            <li>Jan 2022 · <a href="https://www.ucla.edu">UCLA</a> and <a href="https://www.usj.edu.mo/en/">University of Saint Joseph</a>, International Business Management · <a href="RoP&amp;Transcript.pdf">[Certificate-Excellent A]</a></li>
            <li>2021 · Chinese Society for Optimisation &amp; Economic Mathematics, <a href="CertificateMMCM.pdf">Economic and Mathematical Modelling</a></li>
            <li><a href="https://www.sps.ed.ac.uk/news-events/event/when-state-your-landlord-precarity-urban-agriculture-accra">Edinburgh CAS, Landlord State and Precarious Urban Agriculture in Accra</a></li>
            <li><a href="https://www.sps.ed.ac.uk/news-events/event/political-economy-extractivist-development-ghana">Edinburgh CAS, Political Economy of Extractivist Development in Ghana</a></li>
            <li><a href="https://www.sps.ed.ac.uk/news-events/event/global-politics-african-identity-pan-africanism-and-challenge-afropolitanism">Edinburgh CAS, Global Politics of African Identity: Pan-Africanism &amp; Afropolitanism</a></li>
          </ul>'''

new_training = '''          <ul class="training-list">
            <li>Organisational Theory &amp; Methodology: Race, Equity, and Power in Organisations, PhD - Stanford University, Jul 2026</li>
            <li>Emerging Issues in Law: AI, Crypto &amp; Global Change, Adv - University of Bradford, Jun 2026</li>
            <li>Research Methodology in Applied Economics, Adv - <a href="https://english.njau.edu.cn/">Nanjing Agricultural University</a>, Aug 2023, 2025, 2026 · <a href="NAURoP.pdf">[Certificate-Outstanding Student Award]</a></li>
            <li>Frontiers in Microeconomics &amp; Econometrics, Adv - <a href="https://econ.sufe.edu.cn/main.htm">Shanghai University of Finance and Economics</a>, Jul 2025, 2026</li>
            <li>AI in Economic Theory &amp; Methodology, Adv - <a href="https://sem.ucas.ac.cn/en">University of Chinese Academy of Sciences</a>, Jul 2024, 2025, 2026 · <a href="UCASRoP.pdf">[Certificate]</a></li>
            <li>Marxian Political Economy, Adv - <a href="https://en.whu.edu.cn/">Wuhan University</a>, Jul 2023, 2024 · <a href="WHURoP.pdf">[Certificate-Distinguished Paper Award]</a></li>
            <li>Big Data Analytics in GISciences, Adv - <a href="https://en.njnu.edu.cn/">Nanjing Normal University</a>, Aug 2023 · <a href="NNURoP.pdf">[Certificate-Outstanding Student Award]</a></li>
            <li>International Business Management, Prof David French - <a href="https://www.ucla.edu">UCLA</a> &amp; <a href="https://www.usj.edu.mo/en/">University of Saint Joseph</a>, Jan 2022 · <a href="RoP&amp;Transcript.pdf">[Certificate-Excellent A]</a></li>
            <li>Economic and Mathematical Modelling - Chinese Society for Optimisation &amp; Economic Mathematics, 2021 · <a href="CertificateMMCM.pdf">[Certificate]</a></li>
            <li>Firm Innovation Strategy Seminar, Profs Xiaobo Wu &amp; Wenwei Xu - Fudan Centre for Technovation Strategy, Dec 2025</li>
            <li><a href="https://www.sps.ed.ac.uk/news-events/event/when-state-your-landlord-precarity-urban-agriculture-accra">Edinburgh CAS, Landlord State and Precarious Urban Agriculture in Accra</a></li>
            <li><a href="https://www.sps.ed.ac.uk/news-events/event/political-economy-extractivist-development-ghana">Edinburgh CAS, Political Economy of Extractivist Development in Ghana</a></li>
            <li><a href="https://www.sps.ed.ac.uk/news-events/event/global-politics-african-identity-pan-africanism-and-challenge-afropolitanism">Edinburgh CAS, Global Politics of African Identity: Pan-Africanism &amp; Afropolitanism</a></li>
          </ul>'''
html = replace_once(html, old_training, new_training, "training list")

# Replace all straight apostrophes in visible text while preserving tag attributes and URLs.
parts = re.split(r'(<[^>]+>)', html)
for i, part in enumerate(parts):
    if not part.startswith('<'):
        parts[i] = part.replace("'", "’")
html = ''.join(parts)

# Add the one owner-approved anchor-label change to the audit exceptions.
audit = replace_once(
    audit,
    '''        (
            normalise_text("Prof Qifei Chen"),
            normalise_href("http://gmxy.nufe.edu.cn/info/1020/4647.htm"),
        ),
    }''',
    '''        (
            normalise_text("Prof Qifei Chen"),
            normalise_href("http://gmxy.nufe.edu.cn/info/1020/4647.htm"),
        ),
        (
            normalise_text("Chinese Academy of Sciences"),
            normalise_href("https://sem.ucas.ac.cn/en"),
        ),
    }''',
    "audit UCAS mapping",
)

inventory = replace_once(
    inventory,
    '| Chinese Academy of Sciences | https://sem.ucas.ac.cn/en |',
    '| University of Chinese Academy of Sciences | https://sem.ucas.ac.cn/en |',
    "inventory UCAS label",
)
inventory = replace_once(
    inventory,
    'The July 2026 refinements explicitly replaced sixteen legacy mappings:',
    'The July 2026 refinements explicitly replaced seventeen legacy mappings:',
    "inventory replacement count",
)
inventory = replace_once(
    inventory,
    '16. `Prof Qifei Chen` was shortened to `Prof Chen` while retaining the same NUFE profile destination.',
    '16. `Prof Qifei Chen` was shortened to `Prof Chen` while retaining the same NUFE profile destination.\n17. `Chinese Academy of Sciences` was expanded to `University of Chinese Academy of Sciences` while retaining the same UCAS destination.',
    "inventory replacement log",
)

index_path.write_text(html, encoding="utf-8")
audit_path.write_text(audit, encoding="utf-8")
inventory_path.write_text(inventory, encoding="utf-8")
