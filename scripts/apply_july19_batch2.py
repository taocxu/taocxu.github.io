#!/usr/bin/env python3
from pathlib import Path


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

# Latest About text.
old_about = '''          <p class="lead">Upcoming PhD student of development economics at SOAS. Graduating with the highest distinction from NUFE and a merit from the University of Edinburgh, preparing my doctoral research in the political economy of development on the micro-foundations of industrial policy and political settlements from an ideological (Žižekian) and institutional (evolutionary) perspective. Proficient in NVivo, Stata, ArcMap, Python, open to both qualitative &amp; quantitative methodologies, with extensive industrial and academic experience from CITIC, Mazars, Deloitte, HQSW, Duke Kunshan, NUFE, UoEdin, UoSheff, HNU, SUFE, Fudan, several public &amp; private organisations. Involved in a range of heterodox and evidence-based economic research on the political economy of urban &amp; international development, political settlements framework, industrial policy, transport infrastructure policy, and entrepreneurship, looking for the most and least represented samples from localities with diverse formal and informal institutions. Committed to continuous personal development, and seeking more professional challenges in international research universities to apply my knowledge of real-world economics and a transferable skill set.</p>'''
new_about = '''          <p class="lead">Upcoming PhD Student of Development Economics at SOAS. Graduating with the Highest Distinction from NUFE and a Merit from the University of Edinburgh, preparing my doctoral research in the political economy of development on the micro-foundations of industrial policy and political settlements from an ideological (Žižekian) and institutional (evolutionary) perspective. Proficient in NVivo, Stata, ArcMap, Python, open to both qualitative &amp; quantitative methodologies, with extensive industrial and academic experience from CITIC, Mazars, Deloitte, HQSW, Duke Kunshan, NUFE, UoEdin, UoSheff, HNU, SUFE, Fudan, several public &amp; private organisations. Involved in a range of heterodox and evidence-based economic research on the political economy of urban &amp; international development, political settlements framework, industrial policy, transport infrastructure policy, and entrepreneurship, looking for the most and least represented samples from localities with diverse formal and informal institutions. Committed to continuous personal development, seeking more professional challenges and mission-oriented policy-relevant academic environments in international research universities where theoretical and methodological pluralism is valued to apply my knowledge of real-world economics and a transferable skill set.</p>'''
html = replace_once(html, old_about, new_about, "About text")

# Profile-link order.
html = replace_once(
    html,
    '''          <a href="https://drive.google.com/file/d/1KK9XKIFsuQbmF-dt_7UL8yj2v2Q2wZtI/view?usp=sharing" target="_blank" rel="noopener">[CV]</a>
          <a href="https://scholar.google.com/citations?user=KSSSjNQAAAAJ&amp;hl=en" target="_blank" rel="noopener">[Google Scholar]</a>
          <a href="https://papers.ssrn.com/Sol3/Cf_Dev/AbsByAuth.cfm?per_id=6287434" target="_blank" rel="noopener">[SSRN]</a>
          <a href="https://www.researchgate.net/profile/Tao-Xu-168?ev=hdr_xprf" target="_blank" rel="noopener">[ResearchGate]</a>
          <a href="https://orcid.org/0000-0003-0510-3343" target="_blank" rel="noopener">[ORCID]</a>
          <a href="https://www.linkedin.com/in/tao-c-xu" target="_blank" rel="noopener">[LinkedIn]</a>''',
    '''          <a href="https://drive.google.com/file/d/1KK9XKIFsuQbmF-dt_7UL8yj2v2Q2wZtI/view?usp=sharing" target="_blank" rel="noopener">[CV]</a>
          <a href="https://orcid.org/0000-0003-0510-3343" target="_blank" rel="noopener">[ORCID]</a>
          <a href="https://www.linkedin.com/in/tao-c-xu" target="_blank" rel="noopener">[LinkedIn]</a>
          <a href="https://scholar.google.com/citations?user=KSSSjNQAAAAJ&amp;hl=en" target="_blank" rel="noopener">[Google Scholar]</a>
          <a href="https://www.researchgate.net/profile/Tao-Xu-168?ev=hdr_xprf" target="_blank" rel="noopener">[ResearchGate]</a>
          <a href="https://papers.ssrn.com/Sol3/Cf_Dev/AbsByAuth.cfm?per_id=6287434" target="_blank" rel="noopener">[SSRN]</a>''',
    "profile-link order",
)

# Uppercase section and subsection headings requested by the owner.
heading_updates = {
    '<h2 class="section-label">About Tao</h2>': '<h2 class="section-label">ABOUT TAO</h2>',
    '<h2 class="section-label">Research</h2>': '<h2 class="section-label">RESEARCH</h2>',
    '<h2 class="section-label">Publications</h2>': '<h2 class="section-label">PUBLICATIONS</h2>',
    '<h3 class="subsection-title">Working Papers</h3>': '<h3 class="subsection-title">WORKING PAPERS</h3>',
    '<h2 class="section-label">Research Projects</h2>': '<h2 class="section-label">PROJECTS</h2>',
    '<h2 class="section-label">Reports and Presentations</h2>': '<h2 class="section-label">REPORTS &amp; PRESENTATIONS</h2>',
    '<h2 class="section-label">Education</h2>': '<h2 class="section-label">EDUCATION</h2>',
    '<h3 class="subsection-title">Academic Training</h3>': '<h3 class="subsection-title">ACADEMIC TRAINING</h3>',
    '<h2 class="section-label">Research and Professional Experience</h2>': '<h2 class="section-label">RESEARCH &amp; PROFESSIONAL EXPERIENCE</h2>',
    '<h2 class="section-label">Grants and Research Support</h2>': '<h2 class="section-label">GRANTS &amp; RESEARCH SUPPORT</h2>',
    '<h2 class="section-label">Academic Activities</h2>': '<h2 class="section-label">ACADEMIC ACTIVITIES</h2>',
    '<h3 class="subsection-title">Peer Review and Examining</h3>': '<h3 class="subsection-title">PEER REVIEW &amp; EXAMINING</h3>',
    '<h3 class="subsection-title">Professional Memberships</h3>': '<h3 class="subsection-title">PROFESSIONAL MEMBERSHIPS</h3>',
    '<h2 class="section-label">Contact</h2>': '<h2 class="section-label">CONTACT</h2>',
}
for old, new in heading_updates.items():
    html = replace_once(html, old, new, f"heading {old}")

# Working-paper metadata refinements.
html = replace_once(
    html,
    '<p class="item-meta">with Yi Zhu, 2025<br><span class="item-source">ResearchSquare 7374795</span></p>',
    '<p class="item-meta">with Yi Zhu, ResearchSquare 7374795, 2025</p>',
    "ResearchSquare metadata",
)
html = replace_once(
    html,
    '<p class="item-meta">supervised by Dr Hazel Gray, UoE PGSP11291 s2475073, marked as Dissertation of Distinction, 2024</p>',
    '<p class="item-meta">supervised by Dr Hazel Gray, UoE PGSP11291 S2475073 Dissertation of Distinction, 2024</p>',
    "dissertation metadata",
)
html = replace_once(
    html,
    '<p class="item-meta">with Zhengyi Hu, advised by Dr Yongliang Wu, arXiv 2204.00785, 2022</p>',
    '<p class="item-meta">with Zhengyi Hu, advised by Yongliang Wu, arXiv 2204.00785, 2022</p>',
    "Yongliang Wu metadata",
)

# Merge the two current Fudan projects into one owner-specified entry.
html = replace_once(
    html,
    '''            <article class="timeline-item">
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
            </article>''',
    '''            <article class="timeline-item">
              <div class="timeline-date">2025–Present</div>
              <div class="timeline-content">
                <h3>The Growth Pathway of Tech-Lead Firms in Emerging Industries, Digital Social Innovation, and Gradient-Heterogeneous Policy Toolkit</h3>
                <p>Supervised by <a href="https://fddi.fudan.edu.cn/fddien/af/b1/c19479a307121/page.htm">Dr Liu</a>, Research Associate, Fudan University</p>
              </div>
            </article>''',
    "merge Fudan projects",
)

# Project wording refinements.
html = replace_once(
    html,
    '<p>Investigator and Leader, NUFE UG Innovative Training Programme. Supervised by <a href="http://gmxy.nufe.edu.cn/info/1020/4647.htm">Prof Qifei Chen</a>.</p>',
    '<p>Supervised by <a href="http://gmxy.nufe.edu.cn/info/1020/4647.htm">Prof Chen</a>, Principal Investigator and Team Leader, NUFE UG Research Programme</p>',
    "NUFE UG research programme",
)
html = replace_once(
    html,
    '<p>Supervised by <a href="http://gsglxy.nufe.edu.cn/info/1064/1553.htm">Prof Huo</a>, RA, Jiangsu Administration for Market Regulation Programme &amp; School of Business Administration</p>',
    '<p>Supervised by <a href="http://gsglxy.nufe.edu.cn/info/1064/1553.htm">Prof Huo</a>, RA, Jiangsu Administration for Market Regulation Programme &amp; NUFE School of Business Administration</p>',
    "Huo affiliation",
)

# Education: merge programme lines and style dates/degree titles.
html = replace_once(
    html,
    '''              <div class="timeline-date">Expected 2030</div>
              <div class="timeline-content">
                <h3>D.Phil. Economics,  <a href="https://www.soas.ac.uk/about/colleges/college-social-sciences/department-economics">SOAS University of London</a></h3>
                <p>Development Economics<br>
                  Working Dissertation Title: ‘Who Secured the Ladder? Industrial Policy Micro-foundations, Ideological Change, and Political Settlements’<br>
                  Supervisor: <a href="https://www.soas.ac.uk/about/antonio-andreoni">Antonio Andreoni, Ph.D., Professor of Development Economics</a></p>''',
    '''              <div class="timeline-date"><strong><em>Expected 2030</em></strong></div>
              <div class="timeline-content">
                <h3><strong><em>D.Phil. Economics (Development Economics)</em></strong>, <a href="https://www.soas.ac.uk/about/colleges/college-social-sciences/department-economics">SOAS University of London</a></h3>
                <p>Working Dissertation Title: ‘Who Secured the Ladder? Industrial Policy Micro-foundations, Ideological Change, and Political Settlements’<br>
                  Supervisor: <a href="https://www.soas.ac.uk/about/antonio-andreoni">Antonio Andreoni, Ph.D., Professor of Development Economics</a></p>''',
    "DPhil education block",
)
html = replace_once(
    html,
    '''              <div class="timeline-date">2024</div>
              <div class="timeline-content">
                <h3>M.Sc. Development Studies, <a href="https://www.sps.ed.ac.uk/">University of Edinburgh</a></h3>
                <p>International Development Studies, Merit<br>
                  Dissertation: ‘The Road Not Taken? Industrial Policy and Political Settlements in China and Indonesia 1990–2022’<br>
                  Supervisor: <a href="https://www.sps.ed.ac.uk/staff/hazel-gray">Hazel Gray, Ph.D., Senior Lecturer in African Studies &amp; International Development</a></p>''',
    '''              <div class="timeline-date"><strong><em>2024</em></strong></div>
              <div class="timeline-content">
                <h3><strong><em>M.Sc. Development Studies (International Development Studies, Merit)</em></strong>, <a href="https://www.sps.ed.ac.uk/">The University of Edinburgh</a></h3>
                <p>Dissertation: ‘The Road Not Taken? Industrial Policy and Political Settlements in China and Indonesia 1990–2022’<br>
                  Supervisor: <a href="https://www.sps.ed.ac.uk/staff/hazel-gray">Hazel Gray, Ph.D., Senior Lecturer in African Studies &amp; International Development</a></p>''',
    "MSc education block",
)
html = replace_once(
    html,
    '''              <div class="timeline-date">2023</div>
              <div class="timeline-content">
                <h3>B.Sc. Economics, <a href="http://english.nufe.edu.cn/">Nanjing University of Finance &amp; Economics</a></h3>
                <p>Industrial &amp; Commercial Economics, 1st: 91.29<br>
                  Dissertation: ‘Towards Sustainable Prosperity? Policy Evaluation of Jiangsu Advanced Manufacturing Clusters’<br>
                  Supervisor: <a href="https://gmxy.nufe.edu.cn/info/1019/4537.htm">Yabei Hu, Ph.D., Professor of Industrial Economics</a></p>''',
    '''              <div class="timeline-date"><strong><em>2023</em></strong></div>
              <div class="timeline-content">
                <h3><strong><em>B.Sc. Economics (Industrial &amp; Commercial Economics, 1st: 91.29)</em></strong>, <a href="http://english.nufe.edu.cn/">Nanjing University of Finance &amp; Economics</a></h3>
                <p>Dissertation: ‘Towards Sustainable Prosperity? Policy Evaluation of Jiangsu Advanced Manufacturing Clusters’<br>
                  Supervisor: <a href="https://gmxy.nufe.edu.cn/info/1019/4537.htm">Yabei Hu, Ph.D., Professor of Industrial Economics</a></p>''',
    "BSc education block",
)
html = replace_once(html, 'Advanced Modern Economics', 'Frontiers in Microeconomics &amp; Econometrics', "SUFE training title")

# Research and professional experience refinements.
html = replace_once(html, '<h3>Fudan University, Shanghai</h3>', '<h3>Fudan University (Shanghai)</h3>', "Fudan location")
html = replace_once(html, '<h3>Shanghai University of Finance and Economics</h3>', '<h3>Shanghai University of Finance and Economics (Shanghai)</h3>', "SUFE location")
html = replace_once(
    html,
    '''            <article class="timeline-item">
              <div class="timeline-date">2023–2025</div>
              <div class="timeline-content">
                <h3>Nanjing University Department of Finance</h3>
                <p>Peer Advisor and research tutor, including guidance on applied econometrics and Bartik-IV research design</p>
              </div>
            </article>
''',
    '',
    "remove Nanjing University experience",
)
html = replace_once(html, '<h3><a href="DKU.pdf">DKU (Kunshan, Suzhou)</a></h3>', '<h3><a href="DKU.pdf">Duke Kunshan University (Kunshan)</a></h3>', "DKU name")
html = replace_once(html, '<h3><a href="Deloitte.pdf">Deloitte (Industrial Park, Suzhou)</a></h3>', '<h3><a href="Deloitte.pdf">Deloitte (Suzhou)</a></h3>', "Deloitte name")
html = replace_once(html, '<h3><a href="Mazars.pdf">Mazars (Industrial Park, Suzhou)</a></h3>', '<h3><a href="Mazars.pdf">Mazars (Suzhou)</a></h3>', "Mazars name")
html = replace_once(html, '<h3><a href="CITIC.pdf">CITIC (Kunshan, Suzhou)</a></h3>', '<h3><a href="CITIC.pdf">CITIC (Kunshan)</a></h3>', "CITIC name")

# Grants and research-support list refinements.
html = replace_once(html, '<li>NUFE, School of International Economics and Business</li>', '<li>School of International Economics and Business (NUFE)</li>', "NUFE funder order")
html = replace_once(html, '<li>Fudan University, Fudan Development Institute</li>', '<li>Fudan Development Institute (Fudan University)</li>', "Fudan funder order")
html = replace_once(
    html,
    '<li>Kunshan Office of Foreign Affairs, Bureau of Finance, Administration for Market Regulation, and Office of Press and Communication</li>',
    '''<li>Kunshan Office of Foreign Affairs</li>
            <li>Kunshan Bureau of Finance</li>
            <li>Kunshan Administration for Market Regulation</li>
            <li>Kunshan Office of Press and Communication</li>''',
    "split Kunshan funders",
)

# Contact links and punctuation.
html = replace_once(
    html,
    '<p>Centre for Sustainable Structural Transformation, SOAS University of London, 10 Thornhaugh Street, Russell Square, London WC1H 0XG, UK</p>',
    '<p><a href="https://www.soas.ac.uk/centre-sustainable-structural-transformation">Centre for Sustainable Structural Transformation</a>, <a href="https://www.soas.ac.uk/">SOAS University of London</a>, 10 Thornhaugh Street, Russell Square, London WC1H 0XG, UK</p>',
    "contact affiliations",
)
html = replace_once(
    html,
    '<p class="inline-note">Previously: <a href="https://www.sps.ed.ac.uk/">Graduate School of Social and Political Science</a>, <a href="https://www.ed.ac.uk/">The University of Edinburgh</a>.</p>',
    '<p class="inline-note">Previously: <a href="https://www.sps.ed.ac.uk/">Graduate School of Social and Political Science</a>, <a href="https://www.ed.ac.uk/">The University of Edinburgh</a></p>',
    "contact punctuation",
)
html = replace_once(html, '<span><a href="https://github.com/taocxu">Tao Louie</a>.</span>', '<span><a href="https://github.com/taocxu">Tao Louie</a></span>', "footer punctuation")

# Document owner-approved link-text replacements in the audit.
audit = replace_once(
    audit,
    '''        (
            normalise_text("[CV]"),
            normalise_href("CV.pdf"),
        ),
    }''',
    '''        (
            normalise_text("[CV]"),
            normalise_href("CV.pdf"),
        ),
        (
            normalise_text("University of Edinburgh"),
            normalise_href("https://www.sps.ed.ac.uk/"),
        ),
        (
            normalise_text("DKU (Kunshan, Suzhou)"),
            normalise_href("DKU.pdf"),
        ),
        (
            normalise_text("Deloitte (Industrial Park, Suzhou)"),
            normalise_href("Deloitte.pdf"),
        ),
        (
            normalise_text("Mazars (Industrial Park, Suzhou)"),
            normalise_href("Mazars.pdf"),
        ),
        (
            normalise_text("CITIC (Kunshan, Suzhou)"),
            normalise_href("CITIC.pdf"),
        ),
        (
            normalise_text("Prof Qifei Chen"),
            normalise_href("http://gmxy.nufe.edu.cn/info/1020/4647.htm"),
        ),
    }''',
    "audit approved mappings",
)

# Update inventory rows and replacement log.
row_updates = {
    '| University of Edinburgh | https://www.sps.ed.ac.uk/ |': '| The University of Edinburgh | https://www.sps.ed.ac.uk/ |',
    '| DKU (Kunshan, Suzhou) | DKU.pdf |': '| Duke Kunshan University (Kunshan) | DKU.pdf |',
    '| Deloitte (Industrial Park, Suzhou) | Deloitte.pdf |': '| Deloitte (Suzhou) | Deloitte.pdf |',
    '| Mazars (Industrial Park, Suzhou) | Mazars.pdf |': '| Mazars (Suzhou) | Mazars.pdf |',
    '| CITIC (Kunshan, Suzhou) | CITIC.pdf |': '| CITIC (Kunshan) | CITIC.pdf |',
    '| Prof Qifei Chen | http://gmxy.nufe.edu.cn/info/1020/4647.htm |': '| Prof Chen | http://gmxy.nufe.edu.cn/info/1020/4647.htm |',
}
for old, new in row_updates.items():
    inventory = replace_once(inventory, old, new, f"inventory row {old}")

inventory = replace_once(
    inventory,
    '''The July 2026 refinements explicitly replaced ten legacy mappings:

1. The former obfuscated address `tao.clovis.xu[at]outlook[dot]com` linked to Outlook was replaced by `tao.louie.xu[at]outlook[dot]com`, displayed in the hero and Contact section and linked to `mailto:tao.louie.xu+webpage@gmail.com`; the redundant hero `[Email]` button was removed.
2. `“MathorCup” Mathematical Contest in Modelling` linked to the local certificate was replaced by `Economic and Mathematical Modelling` linked to the same local certificate file.
3. Footer text `Tao Xu` linked to the former website URL was replaced by `Tao Louie` linked to the GitHub profile.
4. `Dr Li Liu` was shortened to `Dr Liu` while retaining the same Fudan profile destination.
5. `Dr Yi Zhu` was changed to `Prof Zhu` while retaining the same SUFE profile destination.
6. `Prof Yabei Hu` was shortened to `Prof Hu` while retaining the same NUFE profile destination.
7. `Prof Guanyi Li` was changed to `Dr Li` while retaining the same NUFE profile destination.
8. `Deputy Mayor of Lhasa and Permanent Secretary of Tibet Chunlai Zhou` was shortened to `Deputy Mayor of Lhasa and Permanent Secretary of Tibet Zhou` while retaining the same destination.
9. `Prof Yingbao Huo` was shortened to `Prof Huo` while retaining the same NUFE profile destination.
10. `[CV]` was changed from the local `CV.pdf` destination to the owner-specified Google Drive file.''',
    '''The July 2026 refinements explicitly replaced sixteen legacy mappings:

1. The former obfuscated address `tao.clovis.xu[at]outlook[dot]com` linked to Outlook was replaced by `tao.louie.xu[at]outlook[dot]com`, displayed in the hero and Contact section and linked to `mailto:tao.louie.xu+webpage@gmail.com`; the redundant hero `[Email]` button was removed.
2. `“MathorCup” Mathematical Contest in Modelling` linked to the local certificate was replaced by `Economic and Mathematical Modelling` linked to the same local certificate file.
3. Footer text `Tao Xu` linked to the former website URL was replaced by `Tao Louie` linked to the GitHub profile.
4. `Dr Li Liu` was shortened to `Dr Liu` while retaining the same Fudan profile destination.
5. `Dr Yi Zhu` was changed to `Prof Zhu` while retaining the same SUFE profile destination.
6. `Prof Yabei Hu` was shortened to `Prof Hu` while retaining the same NUFE profile destination.
7. `Prof Guanyi Li` was changed to `Dr Li` while retaining the same NUFE profile destination.
8. `Deputy Mayor of Lhasa and Permanent Secretary of Tibet Chunlai Zhou` was shortened to `Deputy Mayor of Lhasa and Permanent Secretary of Tibet Zhou` while retaining the same destination.
9. `Prof Yingbao Huo` was shortened to `Prof Huo` while retaining the same NUFE profile destination.
10. `[CV]` was changed from the local `CV.pdf` destination to the owner-specified Google Drive file.
11. `University of Edinburgh` was changed to `The University of Edinburgh` while retaining the same SPS destination.
12. `DKU (Kunshan, Suzhou)` was expanded to `Duke Kunshan University (Kunshan)` while retaining the same local PDF destination.
13. `Deloitte (Industrial Park, Suzhou)` was shortened to `Deloitte (Suzhou)` while retaining the same local PDF destination.
14. `Mazars (Industrial Park, Suzhou)` was shortened to `Mazars (Suzhou)` while retaining the same local PDF destination.
15. `CITIC (Kunshan, Suzhou)` was shortened to `CITIC (Kunshan)` while retaining the same local PDF destination.
16. `Prof Qifei Chen` was shortened to `Prof Chen` while retaining the same NUFE profile destination.''',
    "inventory replacement log",
)

index_path.write_text(html, encoding="utf-8")
audit_path.write_text(audit, encoding="utf-8")
inventory_path.write_text(inventory, encoding="utf-8")
