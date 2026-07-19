#!/usr/bin/env python3
from pathlib import Path

# One-shot update for the owner-approved research-interest wording and order.
path = Path("index.html")
html = path.read_text(encoding="utf-8")

old = '''          <ul class="research-interest-list">
            <li>Agglomeration and Spillovers</li>
            <li>Applied Micro-econometrics</li>
            <li>Critical Urban &amp; Global Development Studies</li>
            <li>Development Economics</li>
            <li>Distribution of Power and Rents</li>
            <li>Evolutionary Institutional Economics</li>
            <li>Industrial Policy &amp; Development</li>
            <li>Industrial Value Chains and Ecosystems</li>
            <li>Institutional &amp; Ideological Change</li>
            <li>Micro-foundations of Industrial Policy</li>
            <li>New Structural Economics</li>
            <li>Pluralist Heterodox Economics</li>
            <li>Political Economy of Development</li>
            <li>Political Economy of Institutions</li>
            <li>Political Settlements Framework</li>
            <li>Productive Capabilities</li>
            <li>Strategy-as-Practice</li>
            <li>Techno-nationalism and Innovation</li>
            <li>Transport Policy &amp; Infrastructure</li>
            <li>Urban Industrialisation and Structural Change</li>
          </ul>'''

new = '''          <ul class="research-interest-list">
            <li>Agglomeration and Spillovers</li>
            <li>Applied Micro-econometrics</li>
            <li>Critical Urban &amp; Global Development Studies</li>
            <li>Development Economics</li>
            <li>Distribution of Power and Rents</li>
            <li>Evolutionary Institutional Economics</li>
            <li>Industrial Policy and Development</li>
            <li>Industrial Value Chains &amp; Ecosystems</li>
            <li>Institutional &amp; Ideological Change</li>
            <li>Micro-foundations of Industrial Policy</li>
            <li>New Structural Economics</li>
            <li>Pluralist Heterodox Economics</li>
            <li>Institutionalist Political Economy of Development</li>
            <li>Political Settlements Framework</li>
            <li>Productive Capabilities Transformation</li>
            <li>Strategy-as-Practice</li>
            <li>Techno-nationalism and Innovation</li>
            <li>Transport Policy &amp; Infrastructure</li>
            <li>Urban Industrialisation and Growth</li>
            <li>Sustainable Structural Transformation</li>
          </ul>'''

count = html.count(old)
if count != 1:
    raise RuntimeError(f"Expected one research list, found {count}")

path.write_text(html.replace(old, new, 1), encoding="utf-8")
