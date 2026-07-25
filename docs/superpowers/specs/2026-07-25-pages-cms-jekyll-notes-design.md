# Pages CMS + Jekyll Notes Design

## Purpose

Add a deliberately modest, Git-backed authoring layer for `BLOG & RESEARCH NOTES`. The infrastructure is supplementary rather than exclusive: notes may still be written or edited through GitHub, local editors, agents, or other workflows.

## Isolation

All work remains on `feature/blog-research-notes-preview`. The published `gh-pages` branch is not changed. Publication still requires at least one substantive note and explicit user approval.

## Content model

Notes live as Markdown documents in `_notes/`. Each document contains:

- `title`
- `date`
- `published`
- Markdown body

There are no required categories, tags, summary, image, or references fields.

## Publication safety

New notes default to `published: false`. Jekyll must not output unpublished notes. Setting `published: true` is the explicit publication switch.

## Pages CMS

The root `.pages.yml` exposes `_notes/` as one collection. It permits create, rename, edit, and delete operations. The editor provides title, date, published toggle, and a Markdown rich-text body.

`settings.content.merge: true` preserves unmanaged front-matter keys so that notes created or extended through other tools are not destructively rewritten by Pages CMS.

The rich-text editor does not configure media uploads in this first version. Images can be added later through ordinary Markdown or a separate media design.

## Jekyll

`_config.yml` defines a `notes` collection with rendered output and stable `/notes/<slug>/` URLs. Front-matter defaults provide the `note` layout and unpublished default.

`_layouts/note.html` renders a standalone note page using the current site header, navigation, typography, footer, and a narrower reading column. It contains no compulsory References section.

`notes/index.html` lists all published notes in reverse chronological order. Titles are the sole entry links.

`_includes/homepage-notes.html` renders the latest three published notes for later insertion into the homepage. It is kept modular so the existing large `index.html` need not be riskily rewritten before the first substantive note is ready.

## Draft fixture

A single `_notes/infrastructure-test.md` document is included with `published: false`. It verifies the schema and CMS collection without creating a public page. It can be deleted once the first real note is created.

## Styling

`notes.css` carries production note-list and article styles derived from the approved preview. It introduces no cards, images, sidebars, comments, reading counts, categories, or mandatory reference block.

## Documentation

`docs/notes-authoring.md` records both workflows:

1. Pages CMS for browser-based create, edit, publish, rename, and delete.
2. Direct Markdown authoring for the user's primary or alternative workflows.

## Success criteria

- `.pages.yml` is valid YAML and exposes the intended fields and operations.
- `_config.yml` defines an output-enabled notes collection with safe defaults.
- The hidden draft remains unpublished.
- The archive lists only published notes.
- The homepage include limits output to three published notes.
- Note pages match the existing academic visual language.
- Existing published files and `gh-pages` remain untouched.
