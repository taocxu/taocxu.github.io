# Blog & Research Notes Preview Design

## Purpose

Add a private branch-only preview of a `BLOG & RESEARCH NOTES` feature without changing the published `gh-pages` site. The preview must preserve the current homepage’s restrained academic style, spacing, typography, and responsive behaviour.

## Public-site constraint

The published `gh-pages` branch must remain unchanged until at least one substantive note exists and the user explicitly approves publication.

## Navigation

Add `Notes` as a seventh top-navigation label after `Grants` and before `CV`:

`Home · Research · Publications · Projects · Grants · Notes · CV`

In the preview, `Notes` opens an independent notes archive page rather than scrolling to the homepage section.

## Homepage placement

Insert `BLOG & RESEARCH NOTES` after `REPORTS & PRESENTATIONS` and before the education/CV section.

The homepage displays no full article text and no introductory descriptions. It displays at most three recent notes and at least one note in the eventual public version.

## Homepage item design

Each item contains:

1. A date on its own line in small muted text.
2. A second row containing a left-aligned title and a right-aligned `Read note →` link.
3. On narrow screens, the title and link stack naturally onto separate lines.

The branch preview uses three placeholder items to test the maximum homepage density. The eventual first public version removes the two unused placeholders and displays only the first substantive note. No public `Coming soon` items are permitted.

## Notes archive

Create an independent notes archive page. It uses the same header, navigation, typography, content width, section-label treatment, dividers, and footer as the homepage.

The archive lists notes in reverse chronological order. No categories, tags, sidebars, comment system, reading-count widgets, or dedicated references section are included.

## Single-note page

Create one placeholder single-note page to test navigation and reading width. It uses the same global visual language, a narrower reading column, a title, date, body placeholder text, and a return link to `BLOG & RESEARCH NOTES`.

The template does not contain a mandatory `References` section, although future note content may contain citations where appropriate.

## Preview-only architecture

To avoid replacing or risking the existing `index.html` and `site-v2.css`, create additive preview files only:

- `notes-preview.html`: loads the current homepage, then injects the preview navigation item and homepage notes section in the browser.
- `notes-preview.css`: contains only preview-specific note styles.
- `notes/index-preview.html`: independent archive preview page.
- `notes/example-note-preview.html`: independent single-note preview page.

This architecture leaves existing published files untouched and makes rollback equivalent to deleting the new preview files or branch.

## Success criteria

- The published `gh-pages` branch remains byte-for-byte unchanged.
- The preview homepage shows three balanced note items.
- `Notes` is the seventh navigation item.
- Desktop items keep title left and `Read note →` right when space permits.
- Mobile items stack without horizontal overflow.
- Archive and single-note pages look native to the existing site.
- All preview links work within the branch preview.
