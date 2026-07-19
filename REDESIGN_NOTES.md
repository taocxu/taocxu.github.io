# Academic Website Redesign Notes

## Protected production state

- Production branch: `gh-pages`
- Protected archive branch: `archive/site-v1-2026-07-19`
- Development branch: `feature/google-sites-v2`
- Protected baseline commit: `eaef20cad5af4f34270cf0ab94ae67c6486bc4b0`

The redesign branch was created from the production branch. No redesign commit is written to `gh-pages`. The published website therefore remains unchanged until an explicit review and merge decision.

## Rollback

The current website can be restored by resetting the deployment branch to the protected baseline commit or by rebuilding the deployment branch from `archive/site-v1-2026-07-19`.

## Content rules

1. The existing ‘About Tao’ paragraph is reproduced verbatim in v2.
2. Existing hyperlink text-to-destination relationships are governed by `LINK_INVENTORY.md`.
3. Existing local PDFs and image paths remain in place.
4. New sections are included only when supported by the current CV, the existing site, or user-provided profile information.
5. The first development version uses plain HTML and CSS. It does not introduce Jekyll dependencies or modify the existing `jemdoc.css` file.

## v2 information architecture

- Home and identity
- About Tao
- Research interests
- Publications
- Working papers
- Research projects
- Reports, presentations and book reviews
- Education and academic training
- Research and professional experience
- Grants and research support
- Academic service and memberships
- Contact

No standalone teaching or media section is included at this stage.

## Latest owner-approved refinements

- Degree details use explicit HTML line breaks for programme, dissertation and supervisor information.
- Site title and section headings use the Palatino font stack; body copy uses Aptos, Segoe UI, Helvetica Neue and Arial fallbacks.
- The modelling certificate uses the portable relative path `CertificateMMCM.pdf`.
- The hero email button was removed. The obfuscated address appears beside the research identity line and again in Contact, with both instances linked to the owner-specified email action.
- The CV button now points to the owner-specified Google Drive file.
- Google Scholar uses the English-language profile URL.
