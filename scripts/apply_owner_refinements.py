#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


index_path = Path("index.html")
css_path = Path("site-v2.css")
audit_path = Path("scripts/audit_links.py")
inventory_path = Path("LINK_INVENTORY.md")

index = index_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")
audit = audit_path.read_text(encoding="utf-8")
inventory = inventory_path.read_text(encoding="utf-8")

index = replace_once(
    index,
    '<p class="eyebrow">The Political Economy of Development</p>',
    '<p class="eyebrow">The Political Economy of Development · <a href="mailto:tao.louie.xu+webpage@gmail.com">tao.louie.xu[at]outlook[dot]com</a></p>',
    "add obfuscated email to hero eyebrow",
)

index = replace_once(
    index,
    '          <a href="#contact">[Email]</a>\n',
    '',
    "remove redundant hero email button",
)

index = replace_once(
    index,
    '<a href="CV.pdf">[CV]</a>',
    '<a href="https://drive.google.com/file/d/1KK9XKIFsuQbmF-dt_7UL8yj2v2Q2wZtI/view?usp=sharing" target="_blank" rel="noopener">[CV]</a>',
    "replace CV destination",
)

index = replace_once(
    index,
    'href="https://scholar.google.com/citations?user=KSSSjNQAAAAJ"',
    'href="https://scholar.google.com/citations?user=KSSSjNQAAAAJ&amp;hl=en"',
    "use English Google Scholar profile",
)

index = replace_once(
    index,
    '<p>Email: tao.louie.xu[at]outlook[dot]com</p>',
    '<p>Email: <a href="mailto:tao.louie.xu+webpage@gmail.com">tao.louie.xu[at]outlook[dot]com</a></p>',
    "link contact email",
)

css = replace_once(
    css,
    '''.eyebrow {
  margin: 0 0 15px;
  color: var(--muted);
  font-size: 0.84rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}
''',
    '''.eyebrow {
  margin: 0 0 15px;
  color: var(--muted);
  font-size: 0.84rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.eyebrow a { color: inherit; text-decoration: none; }
.eyebrow a:hover, .eyebrow a:focus-visible { text-decoration: underline; }
''',
    "style hero email link",
)

audit = replace_once(
    audit,
    '''        (
            normalise_text("Prof Yingbao Huo"),
            normalise_href("http://gsglxy.nufe.edu.cn/info/1064/1553.htm"),
        ),
    }''',
    '''        (
            normalise_text("Prof Yingbao Huo"),
            normalise_href("http://gsglxy.nufe.edu.cn/info/1064/1553.htm"),
        ),
        (
            normalise_text("[CV]"),
            normalise_href("CV.pdf"),
        ),
    }''',
    "approve CV destination replacement",
)

inventory = replace_once(
    inventory,
    '| [CV] | CV.pdf | Preserved |',
    '| [CV] | https://drive.google.com/file/d/1KK9XKIFsuQbmF-dt_7UL8yj2v2Q2wZtI/view?usp=sharing | Owner-approved replacement for the former local PDF link |',
    "update CV inventory",
)

inventory = replace_once(
    inventory,
    '| [Google Scholar] | https://scholar.google.com/citations?user=KSSSjNQAAAAJ | Added |',
    '| [Google Scholar] | https://scholar.google.com/citations?user=KSSSjNQAAAAJ&hl=en | Added |',
    "update Google Scholar inventory",
)

inventory = replace_once(
    inventory,
    '| [Email] | #contact | Replaced direct email action with an in-page link to the obfuscated address |',
    '| tao.louie.xu[at]outlook[dot]com | mailto:tao.louie.xu+webpage@gmail.com | Displayed in the hero and Contact section; the former hero [Email] button was removed |',
    "update email inventory",
)

inventory = replace_once(
    inventory,
    'The July 2026 refinements explicitly replaced nine legacy mappings:',
    'The July 2026 refinements explicitly replaced ten legacy mappings:',
    "update replacement count",
)

inventory = replace_once(
    inventory,
    '1. The former obfuscated address `tao.clovis.xu[at]outlook[dot]com` linked to Outlook was replaced by the current plain-text obfuscated address `tao.louie.xu[at]outlook[dot]com`; the hero `[Email]` button now scrolls to Contact.',
    '1. The former obfuscated address `tao.clovis.xu[at]outlook[dot]com` linked to Outlook was replaced by `tao.louie.xu[at]outlook[dot]com`, displayed in the hero and Contact section and linked to `mailto:tao.louie.xu+webpage@gmail.com`; the redundant hero `[Email]` button was removed.',
    "revise email replacement note",
)

inventory = replace_once(
    inventory,
    '9. `Prof Yingbao Huo` was shortened to `Prof Huo` while retaining the same NUFE profile destination.',
    '9. `Prof Yingbao Huo` was shortened to `Prof Huo` while retaining the same NUFE profile destination.\n10. `[CV]` was changed from the local `CV.pdf` destination to the owner-specified Google Drive file.',
    "document CV replacement",
)

index_path.write_text(index, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")
audit_path.write_text(audit, encoding="utf-8")
inventory_path.write_text(inventory, encoding="utf-8")
