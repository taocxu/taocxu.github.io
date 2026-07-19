#!/usr/bin/env python3
from pathlib import Path


def replace_if_present(text: str, old: str, new: str, label: str) -> str:
    if old in text:
        if text.count(old) != 1:
            raise RuntimeError(f"{label}: expected one old match, found {text.count(old)}")
        return text.replace(old, new, 1)
    if new not in text:
        raise RuntimeError(f"{label}: neither approved old nor new text was found")
    return text


index_path = Path('index.html')
notes_path = Path('REDESIGN_NOTES.md')
inventory_path = Path('LINK_INVENTORY.md')
html = index_path.read_text(encoding='utf-8')
inventory = inventory_path.read_text(encoding='utf-8')

html = replace_if_present(
    html,
    'content="Academic Website of Tao Louie Lunhe Xu, Upcoming PhD Student Working on the Political Economy of Development."',
    'content="Academic website of Tao Louie Lunhe Xu, an upcoming PhD student working on the political economy of development."',
    'meta description',
)
html = replace_if_present(
    html,
    '<p class="hero-role">Upcoming PhD Student of Development Economics at SOAS University of London</p>',
    '<p class="hero-role">Upcoming PhD Student in Development Economics at SOAS University of London</p>',
    'hero role',
)
old_about = '''          <p class="lead">An upcoming PhD student of development economics at SOAS. Graduating with the highest distinction from NUFE and a merit from the University of Edinburgh, preparing my doctoral research in the political economy of development on the micro-foundations of industrial policy and political settlements from an ideological (Žižekian) and institutional (evolutionary) perspective. Proficient in NVivo, Stata, ArcMap, Python, Matlab, open to both qualitative &amp; quantitative methodologies, with extensive industrial and academic experience from CITIC, Mazars, Deloitte, HQSW, Duke Kunshan, NUFE, UoEdin, UoSheff, HNU, SUFE, Fudan, Bayes, several public and private organisations. Involved in a range of heterodox and evidence-based economic research on such as the political economy of urban &amp; international development, political settlements, informal institutions, industrial policy, transport infrastructure policy, and entrepreneurship alike, looking for the most and least represented local samples with diverse formal &amp; informal institutions. Seeking more professional challenges and mission-oriented policy-relevant academic environments in international research universities where methodological and theoretical pluralism is valued to apply my knowledge of real-world economics and a transferable skill set.</p>'''
new_about = '''          <p class="lead">An upcoming PhD student in development economics at SOAS. Having graduated with the highest distinction from NUFE and a merit from the University of Edinburgh, I am preparing doctoral research in the political economy of development on the micro-foundations of industrial policy and political settlements from ideological (Žižekian) and institutional (evolutionary) perspectives. Proficient in NVivo, Stata, ArcMap, Python, and MATLAB, and open to both qualitative and quantitative methodologies, with extensive industrial and academic experience at CITIC, Mazars, Deloitte, HQSW, Duke Kunshan, NUFE, UoEdin, UoSheff, HNU, SUFE, Fudan, Bayes, and several public and private organisations. Involved in a range of heterodox and evidence-based economic research, including the political economy of urban and international development, political settlements, informal institutions, industrial policy, transport infrastructure policy, and entrepreneurship, with an interest in the most- and least-represented local samples across diverse formal and informal institutional settings. Seeking further professional challenges and mission-oriented, policy-relevant academic environments at international research universities where methodological and theoretical pluralism is valued, applying my knowledge of real-world economics and a transferable skill set.</p>'''
html = replace_if_present(html, old_about, new_about, 'About Tao copy')
html = replace_if_present(
    html,
    'International Business Management, (<a href="https://www.ucla.edu">UCLA</a>',
    'International Business Management (<a href="https://www.ucla.edu">UCLA</a>',
    'International Business Management punctuation',
)
html = replace_if_present(
    html,
    'Law Society of England & Wales',
    'Law Society of England &amp; Wales',
    'Law Society ampersand',
)

notes = '''# Academic Website Redesign Notes

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
'''

inventory = inventory.replace(
    'This file records the link text-to-destination relationships governing the redesign. The production branch remains `gh-pages`; redesign work is isolated on `feature/google-sites-v2`.',
    'This file records the link text-to-destination relationships governing the published redesign on `gh-pages`. The original site remains preserved on `archive/site-v1-2026-07-19`.',
    1,
)
inventory = inventory.replace('| [CV] |', '| CV |').replace('| [LinkedIn] |', '| LinkedIn |').replace('| [ORCID] |', '| ORCID |').replace('| [GoogleScholar] |', '| GoogleScholar |').replace('| [SSRN] |', '| SSRN |').replace('| [ResearchGate] |', '| ResearchGate |')

index_path.write_text(html, encoding='utf-8')
notes_path.write_text(notes, encoding='utf-8')
inventory_path.write_text(inventory.rstrip() + '\n', encoding='utf-8')

for stale in [
    '.github/workflows/apply-about-text.yml',
    '.github/workflows/apply-research-list-update.yml',
    '.github/workflows/apply-typography-polish.yml',
    '.github/workflows/final-polish.yml',
    'scripts/apply_about_text.py',
    'scripts/apply_key_modules_layout.py',
    'scripts/apply_typography_polish.py',
]:
    Path(stale).unlink(missing_ok=True)
