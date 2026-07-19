#!/usr/bin/env python3
from pathlib import Path

path = Path("index.html")
html = path.read_text(encoding="utf-8")
old = '‘Building Connectivity for Inclusive Global Development: A Perspective from Global South’, with Li Liu, 2025'
new = '<a href="https://www.researchgate.net/publication/398980881_Building_Connectivity_for_Inclusive_Development_China_and_Global_South">‘Building Connectivity for Inclusive Global Development: A Perspective from Global South’</a>, with Li Liu, 2025'
count = html.count(old)
if count != 1:
    raise RuntimeError(f"Expected exactly one report-title match, found {count}")
path.write_text(html.replace(old, new, 1), encoding="utf-8")
