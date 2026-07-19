#!/usr/bin/env python3
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
            normalise_text("Chinese Academy of Sciences"),
            normalise_href("https://sem.ucas.ac.cn/en"),
        ),
    }''',
    '''        (
            normalise_text("Chinese Academy of Sciences"),
            normalise_href("https://sem.ucas.ac.cn/en"),
        ),
        (
            normalise_text("[Certificate]"),
            normalise_href("UCASRoP.pdf"),
        ),
        (
            normalise_text("[Certificate-Outstanding Student Award]"),
            normalise_href("NAURoP.pdf"),
        ),
        (
            normalise_text("[Certificate-Distinguished Paper Award]"),
            normalise_href("WHURoP.pdf"),
        ),
        (
            normalise_text("[Certificate-Outstanding Student Award]"),
            normalise_href("NNURoP.pdf"),
        ),
        (
            normalise_text("[Certificate-Excellent A]"),
            normalise_href("RoP&Transcript.pdf"),
        ),
        (
            normalise_text("Edinburgh CAS, Landlord State and Precarious Urban Agriculture in Accra"),
            normalise_href("https://www.sps.ed.ac.uk/news-events/event/when-state-your-landlord-precarity-urban-agriculture-accra"),
        ),
        (
            normalise_text("Edinburgh CAS, Political Economy of Extractivist Development in Ghana"),
            normalise_href("https://www.sps.ed.ac.uk/news-events/event/political-economy-extractivist-development-ghana"),
        ),
        (
            normalise_text("Edinburgh CAS, Global Politics of African Identity: Pan-Africanism & Afropolitanism"),
            normalise_href("https://www.sps.ed.ac.uk/news-events/event/global-politics-african-identity-pan-africanism-and-challenge-afropolitanism"),
        ),
    }''',
    "approved legacy changes",
)

for old, new in [
    ('| [CV] |', '| CV |'),
    ('| [ORCID] |', '| ORCID |'),
    ('| [LinkedIn] |', '| LinkedIn |'),
    ('| [GoogleScholar] |', '| GoogleScholar |'),
    ('| [ResearchGate] |', '| ResearchGate |'),
    ('| [SSRN] |', '| SSRN |'),
]:
    inventory = inventory.replace(old, new)

inventory = replace_once(
    inventory,
    'The July 2026 refinements explicitly replaced seventeen legacy mappings:',
    'The July 2026 refinements explicitly replaced twenty-five legacy mappings:',
    "replacement count",
)
inventory = replace_once(
    inventory,
    '17. `Chinese Academy of Sciences` was expanded to `University of Chinese Academy of Sciences` while retaining the same UCAS destination.',
    '''17. `Chinese Academy of Sciences` was expanded to `University of Chinese Academy of Sciences` while retaining the same UCAS destination.
18. The UCAS certificate label and link were temporarily removed from the public page.
19. The Nanjing Agricultural University certificate label and link were temporarily removed from the public page.
20. The Wuhan University certificate label and link were temporarily removed from the public page.
21. The Nanjing Normal University certificate label and link were temporarily removed from the public page.
22. The UCLA and University of Saint Joseph certificate label and link were temporarily removed from the public page.
23. The Landlord State seminar link was moved from the full seminar title to `Centre of African Studies, The University of Edinburgh`.
24. The Extractivist Development seminar link was moved from the full seminar title to `Centre of African Studies, The University of Edinburgh`.
25. The African Identity seminar link was moved from the full seminar title to `Centre of African Studies, The University of Edinburgh`.''',
    "replacement log",
)

audit_path.write_text(audit, encoding="utf-8")
inventory_path.write_text(inventory, encoding="utf-8")
