# Academic Website Redesign Notes

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
