#!/usr/bin/env python3
from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


path = Path("index.html")
html = path.read_text(encoding="utf-8")

html = replace_once(
    html,
    "            <li>Karl Marx</li>",
    "            <li>Karl Marx and Friedrich Engels</li>",
    "influence name",
)

anchor = '''            <article class="timeline-item">
              <div class="timeline-date">2025 – Present</div>
              <div class="timeline-content">
                <h3>The Growth Pathway of Tech-Lead Firms in Emerging Industries, Digital Social Innovation, and Gradient-Heterogeneous Policy Toolkit</h3>
                <p>Supervised by <a href="https://fddi.fudan.edu.cn/fddien/af/b1/c19479a307121/page.htm">Dr Liu</a>, 
                  Research Associate, 
                  Fudan</p>
              </div>
            </article>'''

addition = anchor + '''
            <article class="timeline-item">
              <div class="timeline-date">2025 – Present</div>
              <div class="timeline-content">
                <h3>Gu Yanwu’s Neoclassical Confucianism and Entrepreneurship in Contemporary Kunshan, China</h3>
                <p>Co-directed with Xiaoyi Tao, Kunshan Federation of Humanities and Social Sciences Circles Programme, Kunshan Office of Press and Communication</p>
              </div>
            </article>'''

html = replace_once(html, anchor, addition, "Kunshan project insertion")
path.write_text(html, encoding="utf-8")
