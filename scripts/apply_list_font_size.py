#!/usr/bin/env python3
from pathlib import Path

path = Path("site-v2.css")
css = path.read_text(encoding="utf-8")
old = '''.training-list {
  font-size: 0.92rem;
  line-height: 1.5;
}'''
new = '''.training-list,
.support-list,
#activities .section-body > p {
  font-size: 0.92rem;
  line-height: 1.5;
}'''
count = css.count(old)
if count != 1:
    raise RuntimeError(f"Expected one training-list typography block, found {count}")
path.write_text(css.replace(old, new, 1), encoding="utf-8")
