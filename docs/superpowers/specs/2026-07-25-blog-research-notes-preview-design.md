# Blog & Research Notes Preview Design

## Purpose

Add a private branch-only preview of a `BLOG & RESEARCH NOTES` feature without changing the published `gh-pages` site. The preview must preserve the current homepage’s restrained academic style, spacing, typography, and responsive behaviour.

## Public-site constraint

The published `gh-pages` branch must remain unchanged until at least one substantive note exists and the user explicitly approves publication.

## Navigation

Add `Notes` as a seventh top-navigation label after `Projects` and before `Grants`:

`Home · Research · Publications · Projects · Notes · Grants · CV`

On the homepage preview, `Notes` behaves like the other navigation labels and scrolls to the `BLOG & RESEARCH NOTES` section on the same page. It does not link directly to the independent notes archive.

On independent note and archive pages, the top-navigation `Notes` label returns to the homepage notes section. The archive itself is reached from the single-note page through the `← Back to Blog & Research Notes` link.

## Homepage placement

Insert `BLOG & RESEARCH NOTES` after `REPORTS & PRESENTATIONS` and before the education/CV section.

The homepage displays no full article text and no introductory descriptions. It displays at most three recent notes and at least one note in the eventual public version.

## Homepage item design

Each item contains:

1. A date on its own line in small muted text.
2. A left-aligned linked title on the next line.
3. No duplicate `Read note →` link.

The branch preview uses three placeholder items to test the maximum homepage density. The eventual first public version removes the two unused placeholders and displays only the first substantive note. No public `Coming soon` items are permitted.

## Notes archive

Create an independent notes archive page. It uses the same header, navigation, typography, content width, section-label treatment, dividers, and footer as the homepage.

The archive lists all notes in reverse chronological order. Each note is opened through its linked title. It contains no `Read note →` links, categories, tags, sidebars, comment system, reading-count widgets, or dedicated references section.

The homepage provides no direct link to this archive. The archive is reached from a single-note page through the return link.

## Single-note page

Create one placeholder single-note page to test navigation and reading width. It uses the same global visual language, a narrower reading column, a title, date, body placeholder text, and a `← Back to Blog & Research Notes` return link to the complete notes archive.

The template does not contain a mandatory `References` section, although future note content may contain citations where appropriate.

## Preview-only architecture

To avoid replacing or risking the existing `index.html` and `site-v2.css`, create additive preview files only:

- `notes-preview.html`: loads the current homepage, then injects the preview navigation item and homepage notes section in the browser.
- `notes-preview.css`: contains only preview-specific note styles.
- `notes/index-preview.html`: independent archive preview page.
- `notes/example-note-preview.html`: independent single-note preview page.

This architecture leaves existing published files untouched and makes rollback equivalent to deleting the new preview files or branch.

## Success criteria

- The published `gh-pages` branch remains unchanged by this feature branch.
- The preview homepage shows three balanced note items.
- `Notes` is the seventh navigation item, appears before `Grants`, and scrolls to the homepage notes section.
- Homepage and archive items contain only a date and linked title.
- The single-note return link opens the complete archive.
- Mobile layouts avoid horizontal overflow.
- Archive and single-note pages look native to the existing site.
- All preview links work within the branch preview.
