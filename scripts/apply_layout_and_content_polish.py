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

# About text.
old_about = '''          <p class="lead">Upcoming PhD Student of Development Economics at SOAS. Graduating with the Highest Distinction from NUFE and a Merit from the University of Edinburgh, preparing my doctoral research in the political economy of development on the micro-foundations of industrial policy and political settlements from an ideological (Žižekian) and institutional (evolutionary) perspective. Proficient in NVivo, Stata, ArcMap, Python, open to both qualitative &amp; quantitative methodologies, with extensive industrial and academic experience from CITIC, Mazars, Deloitte, HQSW, Duke Kunshan, NUFE, UoEdin, UoSheff, HNU, SUFE, Fudan, several public &amp; private organisations. Involved in a range of heterodox and evidence-based economic research on the political economy of urban &amp; international development, political settlements framework, industrial policy, transport infrastructure policy, and entrepreneurship, looking for the most and least represented samples from localities with diverse formal and informal institutions. Committed to continuous personal development, seeking more professional challenges and mission-oriented policy-relevant academic environments in international research universities where theoretical and methodological pluralism is valued to apply my knowledge of real-world economics and a transferable skill set.</p>'''
new_about = '''          <p class="lead">Upcoming PhD Student of Development Economics at SOAS. Graduating with the Highest Distinction from NUFE and a Merit from the University of Edinburgh, preparing my doctoral research in the political economy of development on the micro-foundations of industrial policy and political settlements from an ideological (Žižekian) and institutional (evolutionary) perspective. Proficient in NVivo, Stata, ArcMap, Python, open to both qualitative &amp; quantitative methodologies, with extensive industrial and academic experience from CITIC, Mazars, Deloitte, HQSW, Duke Kunshan, NUFE, UoEdin, UoSheff, HNU, SUFE, Fudan, Bayes, several public &amp; private organisations. Involved in a range of heterodox and evidence-based economic research on the political economy of urban &amp; international development, political settlements framework, industrial policy, transport infrastructure policy, and entrepreneurship, looking for the most and least represented samples from localities with diverse formal and informal institutions. Committed to continuous personal development, seeking more professional challenges and mission-oriented policy-relevant academic environments in international research universities where methodological and theoretical pluralism is indeed valued to apply my knowledge of real-world economics and a transferable skill set.</p>'''
html = replace_once(html, old_about, new_about, "About text")

# Influences sorted alphabetically by surname, including Lunhe Xu.
old_influences = '''          <ul class="influence-list">
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
          </ul>'''
new_influences = '''          <ul class="influence-list">
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
          </ul>'''
html = replace_once(html, old_influences, new_influences, "influence ordering")

# Working-paper heading.
html = replace_once(
    html,
    '<h3 class="subsection-title">WORKING PAPERS</h3>',
    '<h3 class="subsection-title">WORK IN PROGRESS &amp; WORKING PAPERS</h3>',
    "working papers heading",
)

# Project refinements.
html = replace_once(
    html,
    '<h3>Optimisation of Industrial Ecosystems for Advanced Manufacturing Clusters Based on Producer Services</h3>',
    '<h3>The Optimisation of Industrial Ecosystems for Advanced Manufacturing Clusters Based on Producer Services</h3>',
    "advanced manufacturing project title",
)
html = replace_once(
    html,
    '''<p>Honoured by <a href="http://sxx.youth.cn/zytz/hdgg/202112/W020211223591937418265.pdf">National Excellent Team Award, Provincial Special Team Award, NUFE Best Report Award 1st Class</a>, National ‘Bringing Culture, Science &amp; Health to Rural China’ Programme, Nanjing University of Finance and Economics</p>''',
    '''<p>Honoured by <a href="http://sxx.youth.cn/zytz/hdgg/202112/W020211223591937418265.pdf">National Excellent Team Award, Provincial Special Team Award, NUFE Best Report Award 1st Class</a>, Directed by Weiwei Zhu, National ‘Bringing Culture, Science &amp; Health to Rural China’ Programme, Nanjing University of Finance and Economics</p>''',
    "cultural heritage project direction",
)

# Reports metadata ordering.
html = replace_once(
    html,
    'ResearchGate 385654163, 2024',
    '2024, ResearchGate 385654163',
    "ResearchGate ordering",
)
html = replace_once(
    html,
    'MediArXiv 8kabz, 2024',
    '2024, MediArXiv 8kabz',
    "MediArXiv ordering",
)
html = replace_once(
    html,
    'advised by Prof Zhang, MPRA 112908, 2021',
    'advised by Prof Zhang, 2021, MPRA 112908',
    "MPRA ordering",
)

# Bold education labels.
for old, new, label in [
    ('Working Dissertation Title:', '<strong>Working Dissertation Title:</strong>', 'PhD dissertation label'),
    ('Dissertation:', '<strong>Dissertation:</strong>', 'first dissertation label'),
]:
    html = replace_once(html, old, new, label)
# Remaining two dissertation labels.
html = replace_once(html, 'Dissertation:', '<strong>Dissertation:</strong>', 'second dissertation label')
html = replace_once(html, 'Dissertation:', '<strong>Dissertation:</strong>', 'third dissertation label')
# Three supervisor labels.
html = replace_once(html, 'Supervisor:', '<strong>Supervisor:</strong>', 'first supervisor label')
html = replace_once(html, 'Supervisor:', '<strong>Supervisor:</strong>', 'second supervisor label')
html = replace_once(html, 'Supervisor:', '<strong>Supervisor:</strong>', 'third supervisor label')

# Remove second-line descriptions for Deloitte, Mazars and CITIC.
html = replace_once(
    html,
    '''                <h3><a href="Deloitte.pdf">Deloitte (Suzhou)</a></h3>
                <p>Advisor Assistant, Division of Tax</p>''',
    '''                <h3><a href="Deloitte.pdf">Deloitte (Suzhou)</a></h3>''',
    "Deloitte description removal",
)
html = replace_once(
    html,
    '''                <h3><a href="Mazars.pdf">Mazars (Suzhou)</a></h3>
                <p>Audit Assistant</p>''',
    '''                <h3><a href="Mazars.pdf">Mazars (Suzhou)</a></h3>''',
    "Mazars description removal",
)
html = replace_once(
    html,
    '''                <h3><a href="CITIC.pdf">CITIC (Kunshan)</a></h3>
                <p>Consultant Assistant, Wealth Management</p>''',
    '''                <h3><a href="CITIC.pdf">CITIC (Kunshan)</a></h3>''',
    "CITIC description removal",
)

# About justification, influence columns and tighter education timeline.
css = replace_once(
    css,
    '.lead { max-width: 820px; font-size: 1.06rem; }',
    '.lead { max-width: 820px; font-size: 1.06rem; }\n#about .lead { text-align: justify; text-justify: inter-word; }',
    "About justification style",
)
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
css = replace_once(
    css,
    '  .influence-list { grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px 24px; }',
    '  .influence-list { grid-template-columns: repeat(2, max-content); justify-content: space-between; gap: 10px 28px; }',
    "tablet influence layout",
)
css = replace_once(
    css,
    '  .influence-list { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 9px 18px; }',
    '  .influence-list { grid-template-columns: 1fr; justify-content: stretch; gap: 9px; }',
    "mobile influence layout",
)

index_path.write_text(html, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")
