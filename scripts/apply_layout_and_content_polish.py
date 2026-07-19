#!/usr/bin/env python3
from pathlib import Path

path = Path("index.html")
html = path.read_text(encoding="utf-8")

replacements = {
    '<strong><strong><strong>Supervisor:</strong></strong></strong>': '<strong>Supervisor:</strong>',
    '<strong><strong>Dissertation:</strong></strong>': '<strong>Dissertation:</strong>',
    '''                  Supervisor: <a href="https://www.sps.ed.ac.uk/staff/hazel-gray">Hazel Gray, Ph.D., Senior Lecturer in African Studies &amp; International Development</a><br>''': '''                  <strong>Supervisor:</strong> <a href="https://www.sps.ed.ac.uk/staff/hazel-gray">Hazel Gray, Ph.D., Senior Lecturer in African Studies &amp; International Development</a><br>''',
    '''                <p>Dissertation: ‘Towards Sustainable Prosperity? Policy Evaluation of Jiangsu Advanced Manufacturing Clusters’ (Jiangsu Provincial Distinguished UG Dissertation Award 1st Class, 77 1st-class works/over 732k graduates)<br>
                  Supervisor: <a href="https://gmxy.nufe.edu.cn/info/1019/4537.htm">Yabei Hu, Ph.D., Professor of Industrial Economics</a><br>''': '''                <p><strong>Dissertation:</strong> ‘Towards Sustainable Prosperity? Policy Evaluation of Jiangsu Advanced Manufacturing Clusters’ (Jiangsu Provincial Distinguished UG Dissertation Award 1st Class, 77 1st-class works/over 732k graduates)<br>
                  <strong>Supervisor:</strong> <a href="https://gmxy.nufe.edu.cn/info/1019/4537.htm">Yabei Hu, Ph.D., Professor of Industrial Economics</a><br>''',
}

for old, new in replacements.items():
    if old not in html:
        print(f"WARNING: pattern not found: {old[:80]}")
    html = html.replace(old, new, 1)

path.write_text(html, encoding="utf-8")
