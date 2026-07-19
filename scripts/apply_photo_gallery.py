#!/usr/bin/env python3
from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


rename_map = {
    "1 (1).jpg": "photos/studio-portrait.jpg",
    "1 (2).jpg": "photos/winter-cafe-portrait.jpg",
    "1 (3).jpg": "photos/night-waterfront-portrait.jpg",
    "1 (4).jpg": "photos/cathedral-visit.jpg",
    "1 (5).jpg": "photos/gym-portrait.jpg",
    "1 (6).jpg": "photos/neoclassical-building-portrait.jpg",
    "1 (7).jpg": "photos/historic-ruins-portrait.jpg",
    "1 (8).jpg": "photos/seaside-portrait.jpg",
}

Path("photos").mkdir(exist_ok=True)
for old_name, new_name in rename_map.items():
    old_path = Path(old_name)
    new_path = Path(new_name)
    if not old_path.exists():
        raise FileNotFoundError(f"Missing uploaded photograph: {old_name}")
    if new_path.exists():
        raise FileExistsError(f"Destination already exists: {new_name}")
    old_path.rename(new_path)

index_path = Path("index.html")
css_path = Path("site-v2.css")
html = index_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

contact_block = '''          <div class="contact-block">
            <p><strong>Tao Louie Lunhe Xu, MSc</strong>&nbsp;&nbsp;·&nbsp;&nbsp;ze/they</p>
            <p><a href="https://www.soas.ac.uk/centre-sustainable-structural-transformation">Centre for Sustainable Structural Transformation</a>, <a href="https://www.soas.ac.uk/">SOAS University of London</a>, 10 Thornhaugh Street, Russell Square, London WC1H 0XG, UK</p>
            <p>Email: <a href="mailto:tao.louie.xu+webpage@gmail.com">tao.louie.xu[at]outlook[dot]com</a></p>
            <p class="inline-note">Previously: <a href="https://www.sps.ed.ac.uk/">Graduate School of Social and Political Science</a>, <a href="https://www.ed.ac.uk/">The University of Edinburgh</a></p>
          </div>'''

gallery = contact_block + '''
          <div class="photo-gallery-wrap">
            <p class="photo-gallery-label">SELECTED PHOTOGRAPHS</p>
            <div class="photo-gallery" aria-label="Selected personal photographs">
              <figure class="photo-gallery-item"><img src="photos/studio-portrait.jpg" alt="Studio portrait" loading="lazy" decoding="async"></figure>
              <figure class="photo-gallery-item"><img src="photos/winter-cafe-portrait.jpg" alt="Winter portrait in a café" loading="lazy" decoding="async"></figure>
              <figure class="photo-gallery-item"><img src="photos/cathedral-visit.jpg" alt="Two people outside a cathedral" loading="lazy" decoding="async"></figure>
              <figure class="photo-gallery-item"><img src="photos/neoclassical-building-portrait.jpg" alt="Portrait outside a neoclassical building" loading="lazy" decoding="async"></figure>
              <figure class="photo-gallery-item"><img src="photos/night-waterfront-portrait.jpg" alt="Night waterfront portrait" loading="lazy" decoding="async"></figure>
              <figure class="photo-gallery-item"><img src="photos/historic-ruins-portrait.jpg" alt="Portrait at historic ruins" loading="lazy" decoding="async"></figure>
              <figure class="photo-gallery-item"><img src="photos/seaside-portrait.jpg" alt="Seaside portrait" loading="lazy" decoding="async"></figure>
              <figure class="photo-gallery-item"><img src="photos/gym-portrait.jpg" alt="Two people at a gym" loading="lazy" decoding="async"></figure>
            </div>
          </div>'''

html = replace_once(html, contact_block, gallery, "contact photo gallery insertion")

css = replace_once(
    css,
    '''.contact-block p { margin: 0.3em 0; }

.site-footer { background: #f1f3f4; border-top: 1px solid var(--line); }''',
    '''.contact-block p { margin: 0.3em 0; }

.photo-gallery-wrap {
  margin-top: 22px;
  padding-top: 16px;
  border-top: 1px solid var(--line);
}

.photo-gallery-label {
  margin: 0 0 10px;
  color: var(--muted);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.055em;
}

.photo-gallery {
  column-count: 4;
  column-gap: 12px;
}

.photo-gallery-item {
  margin: 0 0 12px;
  break-inside: avoid;
}

.photo-gallery-item img {
  display: block;
  width: 100%;
  height: auto;
  border: 1px solid var(--line);
  background: var(--panel-soft);
}

.site-footer { background: #f1f3f4; border-top: 1px solid var(--line); }''',
    "photo gallery styles",
)

css = replace_once(
    css,
    '''  .research-interest-list { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px 34px; }
  .influence-list { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px 28px; }
}''',
    '''  .research-interest-list { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px 34px; }
  .influence-list { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px 28px; }
  .photo-gallery { column-count: 3; }
}''',
    "tablet gallery columns",
)

css = replace_once(
    css,
    '''  .key-module-list li { font-size: 0.82rem; }
  .footer-shell { flex-direction: column; }
}

@media print {''',
    '''  .key-module-list li { font-size: 0.82rem; }
  .photo-gallery { column-count: 2; }
  .footer-shell { flex-direction: column; }
}

@media (max-width: 430px) {
  .photo-gallery { column-count: 1; }
}

@media print {''',
    "mobile gallery columns",
)

index_path.write_text(html, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")

for temporary_path in (
    ".github/workflows/build-photo-contact-sheet.yml",
    "scripts/build_photo_contact_sheet.py",
    ".github/workflows/apply-photo-gallery.yml",
    "scripts/apply_photo_gallery.py",
):
    Path(temporary_path).unlink(missing_ok=True)
