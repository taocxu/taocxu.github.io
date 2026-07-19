#!/usr/bin/env python3
from pathlib import Path

path = Path("index.html")
html = path.read_text(encoding="utf-8")

old = '''                    <li>Anthropology of International Development</li>
                    <li>Resource Politics and Development</li>
                    <li>Politics and Theories of International Development</li>
                    <li>Interpreting International Development: Institutions &amp; Practices</li>
                    <li>Research Design</li>
                    <li>Development, Poverty and Governance in Africa</li>
                    <li>Sustainability</li>'''

new = '''                    <li>Anthropology of International Development</li>
                    <li>Resource Politics and Development</li>
                    <li>Politics and Theories of International Development</li>
                    <li>Research Design</li>
                    <li>Interpreting International Development: Institutions &amp; Practices</li>
                    <li>Sustainability</li>
                    <li>Development, Poverty and Governance in Africa</li>'''

count = html.count(old)
if count != 1:
    raise RuntimeError(f"Expected one MSc module block, found {count}")

path.write_text(html.replace(old, new, 1), encoding="utf-8")
