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

html = replace_once(
    html,
    '''                <p><strong>Working Dissertation Title:</strong> ‘Who Secured the Ladder? Industrial Policy Micro-foundations, Ideological Change, and Political Settlements’<br>
                  <strong>Supervisor:</strong> <a href="https://www.soas.ac.uk/about/antonio-andreoni">Antonio Andreoni, Ph.D., Professor of Development Economics</a><br>
                  <strong>Key Modules:</strong> Research Methods for Development Economics&nbsp;&nbsp;·&nbsp;&nbsp;Schools of Thought in Economics&nbsp;&nbsp;·&nbsp;&nbsp;Political Economy of Growth and Development&nbsp;&nbsp;·&nbsp;&nbsp;Political Economy of Institutions&nbsp;&nbsp;·&nbsp;&nbsp;Development Macroeconomics &amp; Microeconomics</p>''',
    '''                <p><strong>Working Dissertation Title:</strong> ‘Who Secured the Ladder? Industrial Policy Micro-foundations, Ideological Change, and Political Settlements’<br>
                  <strong>Supervisor:</strong> <a href="https://www.soas.ac.uk/about/antonio-andreoni">Antonio Andreoni, Ph.D., Professor of Development Economics</a></p>
                <div class="key-modules" aria-label="Key modules">
                  <div class="key-modules-label">Key Modules</div>
                  <ul class="key-module-list">
                    <li>Research Methods for Development Economics</li>
                    <li>Schools of Thought in Economics</li>
                    <li>Political Economy of Growth and Development</li>
                    <li>Political Economy of Institutions</li>
                    <li>Development Macroeconomics &amp; Microeconomics</li>
                  </ul>
                </div>''',
    "PhD key modules",
)

html = replace_once(
    html,
    '''                <p><strong>Dissertation:</strong> ‘The Road Not Taken? Industrial Policy and Political Settlements in China and Indonesia 1990–2022’<br>
                  <strong>Supervisor:</strong> <a href="https://www.sps.ed.ac.uk/staff/hazel-gray">Hazel Gray, Ph.D., Senior Lecturer in African Studies &amp; International Development</a><br>
                  <strong>Key Modules:</strong> Anthropology of International Development&nbsp;&nbsp;·&nbsp;&nbsp;Politics and Theories of International Development&nbsp;&nbsp;·&nbsp;&nbsp;Resource Politics and Development&nbsp;&nbsp;·&nbsp;&nbsp;Interpreting International Development: Institutions &amp; Practices&nbsp;&nbsp;·&nbsp;&nbsp;Development, Poverty and Governance in Africa&nbsp;&nbsp;·&nbsp;&nbsp;Sustainability&nbsp;&nbsp;·&nbsp;&nbsp;Research Design</p>''',
    '''                <p><strong>Dissertation:</strong> ‘The Road Not Taken? Industrial Policy and Political Settlements in China and Indonesia 1990–2022’<br>
                  <strong>Supervisor:</strong> <a href="https://www.sps.ed.ac.uk/staff/hazel-gray">Hazel Gray, Ph.D., Senior Lecturer in African Studies &amp; International Development</a></p>
                <div class="key-modules" aria-label="Key modules">
                  <div class="key-modules-label">Key Modules</div>
                  <ul class="key-module-list">
                    <li>Anthropology of International Development</li>
                    <li>Politics and Theories of International Development</li>
                    <li>Resource Politics and Development</li>
                    <li>Interpreting International Development: Institutions &amp; Practices</li>
                    <li>Development, Poverty and Governance in Africa</li>
                    <li>Sustainability</li>
                    <li>Research Design</li>
                  </ul>
                </div>''',
    "MSc key modules",
)

html = replace_once(
    html,
    '''                <p><strong>Dissertation:</strong> ‘Towards Sustainable Prosperity? Policy Evaluation of Jiangsu Advanced Manufacturing Clusters’ (Jiangsu Provincial Distinguished UG Dissertation Award 1st Class, 77 1st-class works/over 732k graduates)<br>
                  <strong>Supervisor:</strong> <a href="https://gmxy.nufe.edu.cn/info/1019/4537.htm">Yabei Hu, Ph.D., Professor of Industrial Economics</a><br>
                  <strong>Key Modules:</strong> Microeconomics&nbsp;&nbsp;·&nbsp;&nbsp;Macroeconomics&nbsp;&nbsp;·&nbsp;&nbsp;Econometrics&nbsp;&nbsp;·&nbsp;&nbsp;International Economics&nbsp;&nbsp;·&nbsp;&nbsp;Regional Market and Interregional Trade&nbsp;&nbsp;·&nbsp;&nbsp;Regional &amp; Urban Economics&nbsp;&nbsp;·&nbsp;&nbsp;Business Economics&nbsp;&nbsp;·&nbsp;&nbsp;Industrial Organisation&nbsp;&nbsp;·&nbsp;&nbsp;Marketing&nbsp;&nbsp;·&nbsp;&nbsp;Platform Economics&nbsp;&nbsp;·&nbsp;&nbsp;Retailing and Wholesaling Studies&nbsp;&nbsp;·&nbsp;&nbsp;Business Design &amp; Innovation&nbsp;&nbsp;·&nbsp;&nbsp;Economic History</p>''',
    '''                <p><strong>Dissertation:</strong> ‘Towards Sustainable Prosperity? Policy Evaluation of Jiangsu Advanced Manufacturing Clusters’ (Jiangsu Provincial Distinguished UG Dissertation Award 1st Class, 77 1st-class works/over 732k graduates)<br>
                  <strong>Supervisor:</strong> <a href="https://gmxy.nufe.edu.cn/info/1019/4537.htm">Yabei Hu, Ph.D., Professor of Industrial Economics</a></p>
                <div class="key-modules" aria-label="Key modules">
                  <div class="key-modules-label">Key Modules</div>
                  <ul class="key-module-list">
                    <li>Microeconomics</li>
                    <li>Macroeconomics</li>
                    <li>Econometrics</li>
                    <li>International Economics</li>
                    <li>Regional Market and Interregional Trade</li>
                    <li>Regional &amp; Urban Economics</li>
                    <li>Business Economics</li>
                    <li>Industrial Organisation</li>
                    <li>Marketing</li>
                    <li>Platform Economics</li>
                    <li>Retailing and Wholesaling Studies</li>
                    <li>Business Design &amp; Innovation</li>
                    <li>Economic History</li>
                  </ul>
                </div>''',
    "BSc key modules",
)

css = replace_once(
    css,
    '''.timeline-content h3 { margin: 0 0 3px; font-size: 1rem; }
.timeline-content p { margin: 0; color: #3c4043; }

#projects .timeline-content p,''',
    '''.timeline-content h3 { margin: 0 0 3px; font-size: 1rem; }
.timeline-content p { margin: 0; color: #3c4043; }

.key-modules {
  display: grid;
  grid-template-columns: 92px minmax(0, 1fr);
  gap: 10px 14px;
  align-items: start;
  margin-top: 13px;
  padding-top: 12px;
  border-top: 1px solid #e5e7ea;
}

.key-modules-label {
  color: var(--muted);
  font-size: 0.76rem;
  font-weight: 700;
  letter-spacing: 0.055em;
  line-height: 1.4;
  text-transform: uppercase;
}

.key-module-list {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
  margin: 0;
  padding: 0;
  list-style: none;
}

.key-module-list li {
  max-width: 100%;
  padding: 5px 9px;
  border: 1px solid #dfe3e7;
  border-radius: 3px;
  background: #f7f8f9;
  color: #3c4043;
  font-size: 0.84rem;
  line-height: 1.35;
}

#projects .timeline-content p,''',
    "key module styles",
)

css = replace_once(
    css,
    '''  .timeline-item { grid-template-columns: 1fr; gap: 4px; }
  .footer-shell { flex-direction: column; }''',
    '''  .timeline-item { grid-template-columns: 1fr; gap: 4px; }
  .key-modules { grid-template-columns: 1fr; gap: 7px; }
  .key-module-list { gap: 6px; }
  .key-module-list li { font-size: 0.82rem; }
  .footer-shell { flex-direction: column; }''',
    "mobile key module styles",
)

index_path.write_text(html, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")
