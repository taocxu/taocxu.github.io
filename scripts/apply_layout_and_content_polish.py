#!/usr/bin/env python3
from pathlib import Path


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

# About text.
html = replace_once(
    html,
    '''          <p class="lead">Upcoming PhD Student of Development Economics at SOAS. Graduating with the Highest Distinction from NUFE and a Merit from the University of Edinburgh, preparing my doctoral research in the political economy of development on the micro-foundations of industrial policy and political settlements from an ideological (Žižekian) and institutional (evolutionary) perspective. Proficient in NVivo, Stata, ArcMap, Python, open to both qualitative &amp; quantitative methodologies, with extensive industrial and academic experience from CITIC, Mazars, Deloitte, HQSW, Duke Kunshan, NUFE, UoEdin, UoSheff, HNU, SUFE, Fudan, several public &amp; private organisations. Involved in a range of heterodox and evidence-based economic research on the political economy of urban &amp; international development, political settlements framework, industrial policy, transport infrastructure policy, and entrepreneurship, looking for the most and least represented samples from localities with diverse formal and informal institutions. Committed to continuous personal development, seeking more professional challenges and mission-oriented policy-relevant academic environments in international research universities where theoretical and methodological pluralism is valued to apply my knowledge of real-world economics and a transferable skill set.</p>''',
    '''          <p class="lead">Upcoming PhD Student of Development Economics at SOAS. Graduating with the Highest Distinction from NUFE and a Merit from the University of Edinburgh, preparing my doctoral research in the political economy of development on the micro-foundations of industrial policy and political settlements from an ideological (Žižekian) and institutional (evolutionary) perspective. Proficient in NVivo, Stata, ArcMap, Python, open to both qualitative &amp; quantitative methodologies, with extensive industrial and academic experience from CITIC, Mazars, Deloitte, HQSW, Duke Kunshan, NUFE, UoEdin, UoSheff, HNU, SUFE, Fudan, Bayes, several public &amp; private organisations. Involved in a range of heterodox and evidence-based economic research on the political economy of urban &amp; international development, political settlements framework, industrial policy, transport infrastructure policy, and entrepreneurship, looking for the most and least represented samples from localities with diverse formal and informal institutions. Committed to continuous personal development, seeking more professional challenges and mission-oriented policy-relevant academic environments in international research universities where methodological and theoretical pluralism is indeed valued to apply my knowledge of real-world economics and a transferable skill set.</p>''',
    "About text",
)

# Influences, alphabetised by surname and kept on one line per person.
html = replace_once(
    html,
    '''          <ul class="influence-list">
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
          </ul>''',
    '''          <ul class="influence-list">
            <li>Antonio Andreoni</li>
            <li>Alice Amsden</li>
            <li>Yuen Yuen Ang</li>
            <li>Roy Bhaskar</li>
            <li>Ha-Joon Chang</li>
            <li>Peter Evans</li>
            <li>Freeman and Nelson</li>
            <li>Anthony Giddens</li>
            <li>Hazel Gray</li>
            <li>Albert Hirschman</li>
            <li>John Maynard Keynes</li>
            <li>Mushtaq Khan</li>
            <li>Arthur Lewis</li>
            <li>Justin Yifu Lin</li>
            <li>Karl Marx</li>
            <li>Karl Polanyi</li>
            <li>Joseph Schumpeter</li>
            <li>Amartya Sen</li>
            <li>Isabella Weber</li>
            <li>Max Weber</li>
            <li>Lunhe Xu</li>
          </ul>''',
    "influence ordering",
)

# Publications, projects and reports.
html = replace_once(html, '<h3 class="subsection-title">WORKING PAPERS</h3>', '<h3 class="subsection-title">WORK IN PROGRESS &amp; WORKING PAPERS</h3>', "working papers heading")
html = replace_once(html, '<h3>Optimisation of Industrial Ecosystems for Advanced Manufacturing Clusters Based on Producer Services</h3>', '<h3>The Optimisation of Industrial Ecosystems for Advanced Manufacturing Clusters Based on Producer Services</h3>', "advanced manufacturing project title")
html = replace_once(
    html,
    '''<p>Honoured by <a href="http://sxx.youth.cn/zytz/hdgg/202112/W020211223591937418265.pdf">National Excellent Team Award, Provincial Special Team Award, NUFE Best Report Award 1st Class</a>, National ‘Bringing Culture, Science &amp; Health to Rural China’ Programme, Nanjing University of Finance and Economics</p>''',
    '''<p>Honoured by <a href="http://sxx.youth.cn/zytz/hdgg/202112/W020211223591937418265.pdf">National Excellent Team Award, Provincial Special Team Award, NUFE Best Report Award 1st Class</a>, Directed by Weiwei Zhu, National ‘Bringing Culture, Science &amp; Health to Rural China’ Programme, Nanjing University of Finance and Economics</p>''',
    "cultural heritage project direction",
)
html = replace_once(html, 'ResearchGate 385654163, 2024', '2024, ResearchGate 385654163', "ResearchGate ordering")
html = replace_once(html, 'MediArXiv 8kabz, 2024', '2024, MediArXiv 8kabz', "MediArXiv ordering")
html = replace_once(html, 'advised by Prof Zhang, MPRA 112908, 2021', 'advised by Prof Zhang, 2021, MPRA 112908', "MPRA ordering")

# Bold education labels.
html = replace_once(html, 'Working Dissertation Title:', '<strong>Working Dissertation Title:</strong>', "PhD dissertation label")
html = replace_once(html, 'Dissertation:', '<strong>Dissertation:</strong>', "MSc dissertation label")
html = replace_once(html, 'Dissertation:', '<strong>Dissertation:</strong>', "BSc dissertation label")
html = replace_once(html, 'Supervisor:', '<strong>Supervisor:</strong>', "PhD supervisor label")
html = replace_once(html, 'Supervisor:', '<strong>Supervisor:</strong>', "MSc supervisor label")
html = replace_once(html, 'Supervisor:', '<strong>Supervisor:</strong>', "BSc supervisor label")

# Summer schools and seminars: add institutional links, remove certificate labels, and reformat Edinburgh entries.
html = replace_once(
    html,
    'Organisational Theory &amp; Methodology: Race, Equity, and Power in Organisations, PhD - Stanford University, Jul 2026',
    'Organisational Theory &amp; Methodology: Race, Equity, and Power in Organisations, PhD - <a href="https://ccsre.stanford.edu/research-institute/summer-research-methods-seminar/2026-summer-seminar">Stanford University</a>, Jul 2026',
    "Stanford link",
)
html = replace_once(
    html,
    'Emerging Issues in Law: AI, Crypto &amp; Global Change, Adv - University of Bradford, Jun 2026',
    'Emerging Issues in Law: AI, Crypto &amp; Global Change, Adv - <a href="https://www.bradford.ac.uk/events/whats-on/law-social-sciences-summer-school/">University of Bradford</a>, Jun 2026',
    "Bradford link",
)
html = replace_once(html, ' · <a href="NAURoP.pdf">[Certificate-Outstanding Student Award]</a>', '', "NAU certificate removal")
html = replace_once(html, ' · <a href="UCASRoP.pdf">[Certificate]</a>', '', "UCAS certificate removal")
html = replace_once(html, ' · <a href="WHURoP.pdf">[Certificate-Distinguished Paper Award]</a>', '', "WHU certificate removal")
html = replace_once(html, ' · <a href="NNURoP.pdf">[Certificate-Outstanding Student Award]</a>', '', "NNU certificate removal")
html = replace_once(
    html,
    'International Business Management, Prof David French - <a href="https://www.ucla.edu">UCLA</a> &amp; <a href="https://www.usj.edu.mo/en/">University of Saint Joseph</a>, Jan 2022 · <a href="RoP&amp;Transcript.pdf">[Certificate-Excellent A]</a>',
    'International Business Management, Prof David French - <a href="https://www.ucla.edu">UCLA</a> &amp; <a href="https://www.usj.edu.mo/en/">University of Saint Joseph</a>, Jan 2022 (Jiangsu Provincial Government Scholarship for Overseas Studies)',
    "UCLA scholarship and certificate removal",
)
html = replace_once(
    html,
    'Economic and Mathematical Modelling - Chinese Society for Optimisation &amp; Economic Mathematics, 2021 · <a href="CertificateMMCM.pdf">[Certificate]</a>',
    'Economic and Mathematical Modelling - Chinese Society for Optimisation &amp; Economic Mathematics, 2021',
    "modelling certificate removal",
)
html = replace_once(
    html,
    '<li><a href="https://www.sps.ed.ac.uk/news-events/event/when-state-your-landlord-precarity-urban-agriculture-accra">Edinburgh CAS, Landlord State and Precarious Urban Agriculture in Accra</a></li>',
    '<li>Landlord State and Precarious Urban Agriculture in Accra, <a href="https://www.sps.ed.ac.uk/news-events/event/when-state-your-landlord-precarity-urban-agriculture-accra">Centre of African Studies, The University of Edinburgh</a>, 2024</li>',
    "Edinburgh landlord seminar",
)
html = replace_once(
    html,
    '<li><a href="https://www.sps.ed.ac.uk/news-events/event/political-economy-extractivist-development-ghana">Edinburgh CAS, Political Economy of Extractivist Development in Ghana</a></li>',
    '<li>Political Economy of Extractivist Development in Ghana, <a href="https://www.sps.ed.ac.uk/news-events/event/political-economy-extractivist-development-ghana">Centre of African Studies, The University of Edinburgh</a>, 2023</li>',
    "Edinburgh extractivism seminar",
)
html = replace_once(
    html,
    '<li><a href="https://www.sps.ed.ac.uk/news-events/event/global-politics-african-identity-pan-africanism-and-challenge-afropolitanism">Edinburgh CAS, Global Politics of African Identity: Pan-Africanism &amp; Afropolitanism</a></li>',
    '<li>Global Politics of African Identity: Pan-Africanism &amp; Afropolitanism, <a href="https://www.sps.ed.ac.uk/news-events/event/global-politics-african-identity-pan-africanism-and-challenge-afropolitanism">Centre of African Studies, The University of Edinburgh</a>, 2023</li>',
    "Edinburgh identity seminar",
)

# Streamline selected professional-experience entries.
html = replace_once(html, '''                <h3><a href="Deloitte.pdf">Deloitte (Suzhou)</a></h3>
                <p>Advisor Assistant, Division of Tax</p>''', '''                <h3><a href="Deloitte.pdf">Deloitte (Suzhou)</a></h3>''', "Deloitte description removal")
html = replace_once(html, '''                <h3><a href="Mazars.pdf">Mazars (Suzhou)</a></h3>
                <p>Audit Assistant</p>''', '''                <h3><a href="Mazars.pdf">Mazars (Suzhou)</a></h3>''', "Mazars description removal")
html = replace_once(html, '''                <h3><a href="CITIC.pdf">CITIC (Kunshan)</a></h3>
                <p>Consultant Assistant, Wealth Management</p>''', '''                <h3><a href="CITIC.pdf">CITIC (Kunshan)</a></h3>''', "CITIC description removal")

# Grants wording.
html = replace_once(
    html,
    'Shanghai, Jiangsu, Kunshan, and Shuyang Governments as well as Affiliated Public Bodies',
    'Shanghai, Jiangsu, Kunshan, Shuyang Governments and Affiliated Public Bodies',
    "government support wording",
)

# Layout refinements.
css = replace_once(css, '.lead { max-width: 820px; font-size: 1.06rem; }', '.lead { max-width: 820px; font-size: 1.06rem; }\n#about .lead { text-align: justify; text-justify: inter-word; }', "About justification style")
css = replace_once(
    css,
    '''.influence-list {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 10px 28px;
  margin: 0;
  padding: 0;
  list-style: none;
}''',
    '''.influence-list {
  display: grid;
  grid-template-columns: repeat(3, max-content);
  justify-content: space-between;
  gap: 10px 34px;
  margin: 0;
  padding: 0;
  list-style: none;
}''',
    "influence desktop columns",
)
css = replace_once(
    css,
    '''.influence-list li {
  position: relative;
  min-width: 0;
  padding-left: 1.05rem;
  line-height: 1.45;
}''',
    '''.influence-list li {
  position: relative;
  min-width: 0;
  padding-left: 1.05rem;
  line-height: 1.45;
  white-space: nowrap;
}''',
    "influence no-wrap",
)
css = replace_once(
    css,
    '''.timeline-item:first-child { border-top: 0; padding-top: 0; }
.timeline-date { color: var(--muted); font-size: 0.91rem; font-weight: 700; }''',
    '''.timeline-item:first-child { border-top: 0; padding-top: 0; }
#cv .timeline-item { grid-template-columns: 112px minmax(0, 1fr); gap: 16px; }
.timeline-date { color: var(--muted); font-size: 0.91rem; font-weight: 700; }''',
    "education timeline spacing",
)
css = replace_once(css, '  .influence-list { grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px 24px; }', '  .influence-list { grid-template-columns: repeat(2, max-content); justify-content: space-between; gap: 10px 28px; }', "tablet influence layout")
css = replace_once(css, '  .influence-list { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 9px 18px; }', '  .influence-list { grid-template-columns: 1fr; justify-content: stretch; gap: 9px; }', "mobile influence layout")

# Record owner-approved legacy-link removals and relabellings.
audit = replace_once(
    audit,
    '''        (
            normalise_text("Chinese Academy of Sciences"),
            normalise_href("https://sem.ucas.ac.cn/en"),
        ),
    }''',
    '''        (
            normalise_text("Chinese Academy of Sciences"),
            normalise_href("https://sem.ucas.ac.cn/en"),
        ),
        (
            normalise_text("[Certificate]"),
            normalise_href("UCASRoP.pdf"),
        ),
        (
            normalise_text("[Certificate-Outstanding Student Award]"),
            normalise_href("NAURoP.pdf"),
        ),
        (
            normalise_text("[Certificate-Distinguished Paper Award]"),
            normalise_href("WHURoP.pdf"),
        ),
        (
            normalise_text("[Certificate-Outstanding Student Award]"),
            normalise_href("NNURoP.pdf"),
        ),
        (
            normalise_text("[Certificate-Excellent A]"),
            normalise_href("RoP&Transcript.pdf"),
        ),
        (
            normalise_text("Edinburgh CAS, Landlord State and Precarious Urban Agriculture in Accra"),
            normalise_href("https://www.sps.ed.ac.uk/news-events/event/when-state-your-landlord-precarity-urban-agriculture-accra"),
        ),
        (
            normalise_text("Edinburgh CAS, Political Economy of Extractivist Development in Ghana"),
            normalise_href("https://www.sps.ed.ac.uk/news-events/event/political-economy-extractivist-development-ghana"),
        ),
        (
            normalise_text("Edinburgh CAS, Global Politics of African Identity: Pan-Africanism & Afropolitanism"),
            normalise_href("https://www.sps.ed.ac.uk/news-events/event/global-politics-african-identity-pan-africanism-and-challenge-afropolitanism"),
        ),
    }''',
    "audit approved removals",
)

inventory = replace_once(inventory, 'The July 2026 refinements explicitly replaced seventeen legacy mappings:', 'The July 2026 refinements explicitly replaced twenty-five legacy mappings:', "inventory replacement count")
inventory = replace_once(
    inventory,
    '17. `Chinese Academy of Sciences` was expanded to `University of Chinese Academy of Sciences` while retaining the same UCAS destination.',
    '''17. `Chinese Academy of Sciences` was expanded to `University of Chinese Academy of Sciences` while retaining the same UCAS destination.
18. The UCAS certificate label and link were temporarily removed from the public page.
19. The Nanjing Agricultural University certificate label and link were temporarily removed from the public page.
20. The Wuhan University certificate label and link were temporarily removed from the public page.
21. The Nanjing Normal University certificate label and link were temporarily removed from the public page.
22. The UCLA and University of Saint Joseph certificate label and link were temporarily removed from the public page.
23. The Landlord State seminar link was moved from the full seminar title to `Centre of African Studies, The University of Edinburgh`.
24. The Extractivist Development seminar link was moved from the full seminar title to `Centre of African Studies, The University of Edinburgh`.
25. The African Identity seminar link was moved from the full seminar title to `Centre of African Studies, The University of Edinburgh`.''',
    "inventory replacement log",
)

index_path.write_text(html, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")
audit_path.write_text(audit, encoding="utf-8")
inventory_path.write_text(inventory, encoding="utf-8")
