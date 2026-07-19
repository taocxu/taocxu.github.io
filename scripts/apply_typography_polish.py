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

# Adviser links requested by the site owner.
html = replace_once(
    html,
    'advised by Prof Zhang, 2021, MPRA 112908',
    'advised by <a href="https://cem.njfu.edu.cn/zww/list.htm">Prof Zhang</a>, 2021, MPRA 112908',
    "Prof Zhang link",
)
html = replace_once(
    html,
    'advised by Prof Jinguo Tao, 2021',
    'advised by <a href="https://gmxy.nufe.edu.cn/info/1020/4538.htm">Prof Tao</a>, 2021',
    "Prof Tao link",
)

# Conservative site-wide typography and spacing improvements.
replacements = [
    ('font-size: 17px;\n  line-height: 1.68;', 'font-size: 16.5px;\n  line-height: 1.62;', 'body typography'),
    ('min-height: 72px;', 'min-height: 68px;', 'navigation height'),
    ('gap: 28px;\n}', 'gap: 24px;\n}', 'navigation shell gap'),
    ('padding: 10px 14px;\n  font-size: 0.92rem;', 'padding: 9px 12px;\n  font-size: 0.9rem;', 'navigation links'),
    ('padding: 68px 0 66px;', 'padding: 60px 0 58px;', 'hero spacing'),
    ('gap: 64px;', 'gap: 54px;', 'hero gap'),
    ('margin: 24px 0 0;', 'margin: 20px 0 0;', 'hero role spacing'),
    ('margin-top: 27px;', 'margin-top: 23px;', 'profile link spacing'),
    ('font-size: 0.86rem;', 'font-size: 0.84rem;', 'profile link size'),
    ('padding: 62px 0;', 'padding: 56px 0;', 'section spacing'),
    ('grid-template-columns: minmax(190px, 0.34fr) minmax(0, 1fr);\n  gap: 52px;', 'grid-template-columns: minmax(180px, 0.31fr) minmax(0, 1fr);\n  gap: 44px;', 'section grid'),
    ('font-size: 1.42rem;', 'font-size: 1.36rem;', 'section label size'),
    ('.lead { max-width: 820px; font-size: 1.06rem; }', '.lead { max-width: 840px; font-size: 1.02rem; line-height: 1.7; }', 'about typography'),
    ('gap: 13px 48px;', 'gap: 11px 40px;', 'research spacing'),
    ('gap: 10px 34px;', 'gap: 9px 30px;', 'influence spacing'),
    ('margin: 42px 0 16px;\n  padding-top: 10px;', 'margin: 36px 0 14px;\n  padding-top: 9px;', 'subsection spacing'),
    ('.item-list.no-dividers .item { border-top: 0; padding: 11px 0; }', '.item-list.no-dividers .item { border-top: 0; padding: 9px 0; }', 'working-paper spacing'),
    ('.item-title { margin: 0; color: var(--ink); font-size: 1.01rem; font-weight: 700; line-height: 1.45; }', '.item-title { margin: 0; color: var(--ink); font-size: 0.99rem; font-weight: 700; line-height: 1.42; }', 'item titles'),
    ('.item-meta { margin: 5px 0 0; color: var(--muted); font-size: 0.94rem; }', '.item-meta { margin: 4px 0 0; color: var(--muted); font-size: 0.91rem; line-height: 1.5; }', 'item metadata'),
    ('gap: 25px;\n  padding: 20px 0;', 'gap: 20px;\n  padding: 17px 0;', 'timeline spacing'),
    ('#cv .timeline-item { grid-template-columns: 112px minmax(0, 1fr); gap: 16px; }', '#cv .timeline-item { grid-template-columns: 104px minmax(0, 1fr); gap: 14px; }', 'education timeline spacing'),
    ('.timeline-date { color: var(--muted); font-size: 0.91rem; font-weight: 700; }', '.timeline-date { color: var(--muted); font-size: 0.88rem; font-weight: 700; }', 'timeline date size'),
    ('.timeline-content h3 { margin: 0 0 3px; font-size: 1rem; }', '.timeline-content h3 { margin: 0 0 4px; font-size: 0.98rem; line-height: 1.45; }', 'timeline headings'),
    ('grid-template-columns: 92px minmax(0, 1fr);\n  gap: 10px 14px;\n  align-items: start;\n  margin-top: 13px;\n  padding-top: 12px;', 'grid-template-columns: 84px minmax(0, 1fr);\n  gap: 8px 12px;\n  align-items: start;\n  margin-top: 11px;\n  padding-top: 10px;', 'key-modules layout'),
    ('font-size: 0.76rem;', 'font-size: 0.72rem;', 'key-modules label'),
    ('gap: 7px;\n  margin: 0;', 'gap: 6px;\n  margin: 0;', 'key-module gap'),
    ('padding: 5px 9px;', 'padding: 4px 8px;', 'key-module padding'),
    ('font-size: 0.84rem;\n  line-height: 1.35;', 'font-size: 0.82rem;\n  line-height: 1.34;', 'key-module type'),
    ('#projects .timeline-content p,\n#experience .timeline-content p {\n  font-size: 0.96rem;\n  line-height: 1.58;', '#projects .timeline-content p,\n#experience .timeline-content p {\n  font-size: 0.93rem;\n  line-height: 1.52;', 'secondary timeline text'),
    ('.report-list li {\n  border-top: 0;\n  padding: 7px 0;\n}', '.report-list li {\n  border-top: 0;\n  padding: 6px 0;\n  font-size: 0.95rem;\n  line-height: 1.52;\n}', 'report list typography'),
    ('.training-list {\n  font-size: 0.94rem;\n  line-height: 1.55;\n}', '.training-list {\n  font-size: 0.92rem;\n  line-height: 1.5;\n}', 'training list typography'),
]

for old, new, label in replacements:
    css = replace_once(css, old, new, label)

# Mobile rhythm: slightly tighter while retaining readable tap targets.
css = replace_once(
    css,
    '''  body { font-size: 16px; }
  .nav-shell, .hero-shell, .content-section, .footer-shell { width: min(100% - 28px, var(--content)); }''',
    '''  body { font-size: 15.75px; line-height: 1.6; }
  .nav-shell, .hero-shell, .content-section, .footer-shell { width: min(100% - 28px, var(--content)); }''',
    "mobile body typography",
)
css = replace_once(css, '  .content-section { padding: 48px 0; }', '  .content-section { padding: 44px 0; }', 'mobile section spacing')

index_path.write_text(html, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")
