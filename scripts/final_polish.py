#!/usr/bin/env python3
from pathlib import Path

index_path = Path("index.html")
css_path = Path("site-v2.css")
notes_path = Path("REDESIGN_NOTES.md")
inventory_path = Path("LINK_INVENTORY.md")
audit_path = Path("scripts/audit_links.py")

html = index_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")
inventory = inventory_path.read_text(encoding="utf-8")
audit = audit_path.read_text(encoding="utf-8")

replacements = {
    "<!doctype html>": "<!DOCTYPE html>",
    'content="Academic Website of Tao Louie Lunhe Xu, Upcoming PhD Student Working on the Political Economy of Development."': 'content="Academic website of Tao Louie Lunhe Xu, an upcoming PhD student working on the political economy of development."',
    '<p class="hero-role">Upcoming PhD Student of Development Economics at SOAS University of London</p>': '<p class="hero-role">Upcoming PhD Student in Development Economics at SOAS University of London</p>',
    'International Business Management, (<a href="https://www.ucla.edu">UCLA</a>': 'International Business Management (<a href="https://www.ucla.edu">UCLA</a>',
    "Law Society of England & Wales": "Law Society of England &amp; Wales",
    "WHU Outstanding Student & Distinguished Paper Award": "WHU Outstanding Student &amp; Distinguished Paper Award",
    '<div class="profile-links" aria-label="Academic profiles">': '<nav class="profile-links" aria-label="Academic profiles">',
    '<div class="photo-gallery" aria-label="Selected personal photographs">': '<div class="photo-gallery" role="group" aria-label="Selected personal photographs">',
    '<span>Development Draft&nbsp;&nbsp;·&nbsp;&nbsp;July 2026</span>': '<span>Last updated&nbsp;&nbsp;·&nbsp;&nbsp;July 2026</span>',
}
for old, new in replacements.items():
    html = html.replace(old, new)

old_about = """          <p class="lead">An upcoming PhD student of development economics at SOAS. Graduating with the highest distinction from NUFE and a merit from the University of Edinburgh, preparing my doctoral research in the political economy of development on the micro-foundations of industrial policy and political settlements from an ideological (Žižekian) and institutional (evolutionary) perspective. Proficient in NVivo, Stata, ArcMap, Python, Matlab, open to both qualitative &amp; quantitative methodologies, with extensive industrial and academic experience from CITIC, Mazars, Deloitte, HQSW, Duke Kunshan, NUFE, UoEdin, UoSheff, HNU, SUFE, Fudan, Bayes, several public and private organisations. Involved in a range of heterodox and evidence-based economic research on such as the political economy of urban &amp; international development, political settlements, informal institutions, industrial policy, transport infrastructure policy, and entrepreneurship alike, looking for the most and least represented local samples with diverse formal &amp; informal institutions. Seeking more professional challenges and mission-oriented policy-relevant academic environments in international research universities where methodological and theoretical pluralism is valued to apply my knowledge of real-world economics and a transferable skill set.</p>"""
new_about = """          <p class="lead">An upcoming PhD student in development economics at SOAS. Having graduated with the highest distinction from NUFE and a merit from the University of Edinburgh, I am preparing doctoral research in the political economy of development on the micro-foundations of industrial policy and political settlements from ideological (Žižekian) and institutional (evolutionary) perspectives. Proficient in NVivo, Stata, ArcMap, Python, and MATLAB, and open to both qualitative and quantitative methodologies, with extensive industrial and academic experience at CITIC, Mazars, Deloitte, HQSW, Duke Kunshan, NUFE, UoEdin, UoSheff, HNU, SUFE, Fudan, Bayes, and several public and private organisations. Involved in a range of heterodox and evidence-based economic research, including the political economy of urban and international development, political settlements, informal institutions, industrial policy, transport infrastructure policy, and entrepreneurship, with an interest in the most- and least-represented local samples across diverse formal and informal institutional settings. Seeking further professional challenges and mission-oriented, policy-relevant academic environments at international research universities where methodological and theoretical pluralism is valued, applying my knowledge of real-world economics and a transferable skill set.</p>"""
html = html.replace(old_about, new_about)
html = html.replace('<div class="key-modules" aria-label="Key modules">', '<div class="key-modules">')
html = html.replace(
    '          <a href="https://papers.ssrn.com/Sol3/Cf_Dev/AbsByAuth.cfm?per_id=6287434" target="_blank" rel="noopener">SSRN</a>\n        </div>',
    '          <a href="https://papers.ssrn.com/Sol3/Cf_Dev/AbsByAuth.cfm?per_id=6287434" target="_blank" rel="noopener">SSRN</a>\n        </nav>',
)
html = "\n".join(line.rstrip() for line in html.splitlines()) + "\n"

mobile_hero = '  .hero-shell { grid-template-columns: 1fr; gap: 30px; padding: 36px 0 46px; }'
if '  .hero-shell > * { min-width: 0; }' not in css:
    css = css.replace(
        mobile_hero,
        mobile_hero + '\n  .hero-shell > * { min-width: 0; }\n  .eyebrow a { overflow-wrap: anywhere; }',
        1,
    )
if '  .influence-list li { white-space: normal; }' not in css:
    css = css.replace(
        '  .influence-list { grid-template-columns: 1fr; justify-content: stretch; gap: 9px; }',
        '  .influence-list { grid-template-columns: 1fr; justify-content: stretch; gap: 9px; }\n  .influence-list li { white-space: normal; }\n  .section-body, .timeline-content, .contact-block { overflow-wrap: anywhere; }',
        1,
    )

notes = """# Academic Website Redesign Notes

## Published and rollback states

- Published branch: `gh-pages`
- Protected original archive: `archive/site-v1-2026-07-19`
- Protected original commit: `eaef20cad5af4f34270cf0ab94ae67c6486bc4b0`

The July 2026 redesign replaces the former Jemdoc-style homepage with a responsive HTML and CSS academic profile. The protected archive preserves the complete original site and can be used for rollback.

## Rollback

Restore the original site by moving `gh-pages` to `archive/site-v1-2026-07-19` or directly to commit `eaef20cad5af4f34270cf0ab94ae67c6486bc4b0`.

## Current structure

- Home and identity
- About Tao
- Research interests and influences
- Publications and work in progress
- Research projects
- Reports and presentations
- Education and academic training
- Research and professional experience
- Grants and research support
- Academic activities and professional memberships
- Contact and selected photographs

## Design and content rules

1. British English is used throughout visible site copy.
2. Existing and owner-approved hyperlink mappings are documented in `LINK_INVENTORY.md`.
3. Local PDFs and image assets must continue to resolve.
4. The site uses plain HTML and CSS without a Jekyll dependency.
5. The current layout is responsive at desktop, tablet and mobile widths.
"""

inventory = inventory.replace(
    "This file records the link text-to-destination relationships governing the redesign. The production branch remains `gh-pages`; redesign work is isolated on `feature/google-sites-v2`.",
    "This file records the link text-to-destination relationships governing the published redesign on `gh-pages`. The original site remains preserved on `archive/site-v1-2026-07-19`.",
)
for old, new in {
    "| [CV] |": "| CV |",
    "| [LinkedIn] |": "| LinkedIn |",
    "| [ORCID] |": "| ORCID |",
    "| [GoogleScholar] |": "| GoogleScholar |",
    "| [SSRN] |": "| SSRN |",
    "| [ResearchGate] |": "| ResearchGate |",
    "| ‘When Polanyi Met Schumpeter: Social Trust and Entrepreneurship’ | https://mpra.ub.uni-muenchen.de/123894/ |": "| ‘When Polanyi Met Schumpeter: Social Trust and Entrepreneurship’ | https://doi.org/10.31235/osf.io/nka6s_v3 |",
}.items():
    inventory = inventory.replace(old, new)

polanyi_exception = '''        (
            normalise_text("When Polanyi Met Schumpeter: Social Trust and Entrepreneurship"),
            normalise_href("https://mpra.ub.uni-muenchen.de/123894/"),
        ),'''
road_exception = '''        (
            normalise_text("The Road Not Taken? Industrial Policy and Political Settlements in China and Indonesia 1990–2022"),
            normalise_href("https://mpra.ub.uni-muenchen.de/id/eprint/122669"),
        ),'''
if polanyi_exception not in audit:
    audit = audit.replace(road_exception, polanyi_exception + "\n" + road_exception, 1)

index_path.write_text(html, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")
notes_path.write_text(notes, encoding="utf-8")
inventory_path.write_text(inventory.rstrip() + "\n", encoding="utf-8")
audit_path.write_text(audit, encoding="utf-8")

for stale in [
    ".github/workflows/apply-about-text.yml",
    ".github/workflows/apply-research-list-update.yml",
    ".github/workflows/apply-typography-polish.yml",
    ".github/workflows/final-polish.yml",
    "scripts/apply_about_text.py",
    "scripts/apply_key_modules_layout.py",
    "scripts/apply_typography_polish.py",
    "audit-trigger.txt",
    "audit-run.txt",
]:
    Path(stale).unlink(missing_ok=True)
