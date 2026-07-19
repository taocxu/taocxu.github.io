#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


audit_path = Path("scripts/audit_links.py")
inventory_path = Path("LINK_INVENTORY.md")

audit = audit_path.read_text(encoding="utf-8")
inventory = inventory_path.read_text(encoding="utf-8")

audit = replace_once(
    audit,
    '''        (
            normalise_text("Tao Xu"),
            normalise_href("https://taocxu.github.io/"),
        ),
    }''',
    '''        (
            normalise_text("Tao Xu"),
            normalise_href("https://taocxu.github.io/"),
        ),
        (
            normalise_text("Dr Li Liu"),
            normalise_href("https://fddi.fudan.edu.cn/fddien/af/b1/c19479a307121/page.htm"),
        ),
        (
            normalise_text("Dr Yi Zhu"),
            normalise_href("https://cpi.sufe.edu.cn/45/1b/c13242a214299/page.htm"),
        ),
        (
            normalise_text("Prof Yabei Hu"),
            normalise_href("https://gmxy.nufe.edu.cn/info/1013/4509.htm"),
        ),
        (
            normalise_text("Prof Guanyi Li"),
            normalise_href("http://gmxy.nufe.edu.cn/info/1020/4536.htm"),
        ),
        (
            normalise_text("Deputy Mayor of Lhasa and Permanent Secretary of Tibet Chunlai Zhou"),
            normalise_href("https://baike.baidu.com/item/周春来/44246"),
        ),
        (
            normalise_text("Prof Yingbao Huo"),
            normalise_href("http://gsglxy.nufe.edu.cn/info/1064/1553.htm"),
        ),
    }''',
    "extend approved legacy mappings",
)

row_updates = {
    '| Dr Li Liu | https://fddi.fudan.edu.cn/fddien/af/b1/c19479a307121/page.htm |':
        '| Dr Liu | https://fddi.fudan.edu.cn/fddien/af/b1/c19479a307121/page.htm |',
    '| Dr Yi Zhu | https://cpi.sufe.edu.cn/45/1b/c13242a214299/page.htm |':
        '| Prof Zhu | https://cpi.sufe.edu.cn/45/1b/c13242a214299/page.htm |',
    '| Prof Yabei Hu | https://gmxy.nufe.edu.cn/info/1013/4509.htm |':
        '| Prof Hu | https://gmxy.nufe.edu.cn/info/1013/4509.htm |',
    '| Prof Guanyi Li | http://gmxy.nufe.edu.cn/info/1020/4536.htm |':
        '| Dr Li | http://gmxy.nufe.edu.cn/info/1020/4536.htm |',
    '| Deputy Mayor of Lhasa and Permanent Secretary of Tibet Chunlai Zhou | https://baike.baidu.com/item/周春来/44246 |':
        '| Deputy Mayor of Lhasa and Permanent Secretary of Tibet Zhou | https://baike.baidu.com/item/周春来/44246 |',
    '| Prof Yingbao Huo | http://gsglxy.nufe.edu.cn/info/1064/1553.htm |':
        '| Prof Huo | http://gsglxy.nufe.edu.cn/info/1064/1553.htm |',
}
for old, new in row_updates.items():
    inventory = replace_once(inventory, old, new, f"inventory row {old}")

inventory = replace_once(
    inventory,
    '''The July 2026 refinement explicitly replaced three legacy mappings:

1. The former obfuscated address `tao.clovis.xu[at]outlook[dot]com` linked to Outlook was replaced by the current plain-text obfuscated address `tao.louie.xu[at]outlook[dot]com`; the hero `[Email]` button now scrolls to Contact.
2. `“MathorCup” Mathematical Contest in Modelling` linked to the local certificate was replaced by `Economic and Mathematical Modelling` linked to the local certificate file.
3. Footer text `Tao Xu` linked to the former website URL was replaced by `Tao Louie` linked to the GitHub profile.''',
    '''The July 2026 refinements explicitly replaced nine legacy mappings:

1. The former obfuscated address `tao.clovis.xu[at]outlook[dot]com` linked to Outlook was replaced by the current plain-text obfuscated address `tao.louie.xu[at]outlook[dot]com`; the hero `[Email]` button now scrolls to Contact.
2. `“MathorCup” Mathematical Contest in Modelling` linked to the local certificate was replaced by `Economic and Mathematical Modelling` linked to the same local certificate file.
3. Footer text `Tao Xu` linked to the former website URL was replaced by `Tao Louie` linked to the GitHub profile.
4. `Dr Li Liu` was shortened to `Dr Liu` while retaining the same Fudan profile destination.
5. `Dr Yi Zhu` was changed to `Prof Zhu` while retaining the same SUFE profile destination.
6. `Prof Yabei Hu` was shortened to `Prof Hu` while retaining the same NUFE profile destination.
7. `Prof Guanyi Li` was changed to `Dr Li` while retaining the same NUFE profile destination.
8. `Deputy Mayor of Lhasa and Permanent Secretary of Tibet Chunlai Zhou` was shortened to `Deputy Mayor of Lhasa and Permanent Secretary of Tibet Zhou` while retaining the same destination.
9. `Prof Yingbao Huo` was shortened to `Prof Huo` while retaining the same NUFE profile destination.''',
    "document approved linked-text changes",
)

audit_path.write_text(audit, encoding="utf-8")
inventory_path.write_text(inventory, encoding="utf-8")
