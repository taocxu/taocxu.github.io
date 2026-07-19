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
    '''          <ul class="research-interest-list">
            <li>Institutionalist Political Economy of Development and Change</li>
            <li>Political Settlements Framework</li>
            <li>Evolutionary Institutional and Development Economics</li>
            <li>Institutional and Ideological Change</li>
            <li>Distribution of Power and Rents</li>
            <li>Critical Urban, International and Global Development Studies</li>
            <li>Industrial Policy and Development</li>
            <li>Micro-foundations of Industrial Policy and Political Settlements</li>
          </ul>''',
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
    "research-interest list",
)

html = replace_once(
    html,
    '<p class="item-meta">with Yabei Hu, <i>Technology in Society</i>, 2024, 77, 102583; honoured by Jiangsu Provincial Distinguished Award · <a href="TSP.pdf">[PDF]</a></p>',
    '<p class="item-meta">with Yabei Hu, <i>Technology in Society</i>, 2024, 77, 102583, honoured by Jiangsu Provincial Distinguished Award · <a href="TSP.pdf">[PDF]</a></p>',
    "published-paper metadata punctuation",
)

html = replace_once(
    html,
    '<h3>Urban Development Economics of High-Speed Railway New Town Planning</h3>',
    '<h3>The Urban Economics of High-Speed Railway New Town Planning and Development</h3>',
    "HSR project title",
)

path.write_text(html, encoding="utf-8")
