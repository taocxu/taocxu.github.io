# Pages CMS + Jekyll Notes Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a safe, browser-editable Pages CMS authoring path backed by a Jekyll notes collection, without changing the published branch.

**Architecture:** Markdown notes live in `_notes/`; Pages CMS edits those files; Jekyll renders individual notes and an archive. A modular homepage include exposes the latest three published notes later, while the current public homepage remains untouched.

**Tech Stack:** GitHub Pages, Jekyll, Liquid, HTML, CSS, YAML, Markdown, Pages CMS.

## Global Constraints

- Work only on `feature/blog-research-notes-preview`.
- Do not modify `gh-pages`.
- New notes default to `published: false`.
- No categories, tags, summaries, images, comments, reading counts, or mandatory References field.
- Preserve unmanaged front-matter keys when Pages CMS saves a file.
- Keep the existing approved visual language.

---

### Task 1: Configure Pages CMS

**Files:**
- Create: `.pages.yml`

**Interfaces:**
- Consumes: Markdown files in `_notes/`.
- Produces: browser fields `title`, `date`, `published`, and `body`; create, rename, edit, and delete operations.

- [ ] Create a YAML-frontmatter collection at `_notes/`.
- [ ] Make the filename editable only when creating a note.
- [ ] Set `published` to default false.
- [ ] Enable merge mode to preserve unmanaged keys.
- [ ] Disable rich-text media uploads in this version.
- [ ] Validate YAML parsing.

### Task 2: Configure the Jekyll collection

**Files:**
- Modify: `_config.yml`
- Create: `_notes/infrastructure-test.md`

**Interfaces:**
- Consumes: `_notes/*.md` with front matter.
- Produces: rendered note URLs at `/notes/:name/` for published documents.

- [ ] Add the output-enabled `notes` collection.
- [ ] Add the `/notes/:name/` permalink.
- [ ] Add front-matter defaults for `layout: note` and `published: false`.
- [ ] Add one unpublished infrastructure fixture.
- [ ] Validate both YAML files.

### Task 3: Add the production note layout and styles

**Files:**
- Create: `_layouts/note.html`
- Create: `notes.css`

**Interfaces:**
- Consumes: `page.title`, `page.date`, and rendered `content`.
- Produces: a standalone note page with site navigation and archive return link.

- [ ] Reuse the current site header, navigation, content width, typography, and footer.
- [ ] Point the top `Notes` link to the homepage notes anchor.
- [ ] Add `← Back to Blog & Research Notes` linking to `/notes/`.
- [ ] Keep the reading column at 760px maximum.
- [ ] Add responsive article styling.

### Task 4: Add dynamic archive and homepage include

**Files:**
- Create: `notes/index.html`
- Create: `_includes/homepage-notes.html`

**Interfaces:**
- Consumes: `site.notes`.
- Produces: reverse-chronological archive and latest-three homepage fragment.

- [ ] Filter out documents with `published: false`.
- [ ] Sort published notes by date descending.
- [ ] Use title-only links.
- [ ] Limit the homepage fragment to three notes.
- [ ] Avoid public placeholder or `Coming soon` text.

### Task 5: Document mixed authoring workflows

**Files:**
- Create: `docs/notes-authoring.md`

**Interfaces:**
- Consumes: Pages CMS and direct Markdown workflows.
- Produces: concise operating instructions and publication safeguards.

- [ ] Explain selecting the repository and feature branch in Pages CMS.
- [ ] Explain create, edit, publish, rename, and delete operations.
- [ ] Document the direct Markdown schema.
- [ ] State that `published: true` is the publication switch.
- [ ] Explain that the unpublished infrastructure fixture can be deleted.

### Task 6: Verify branch safety and configuration

**Files:**
- Verify all files above.

**Interfaces:**
- Consumes: final feature branch.
- Produces: evidence that configuration and branch isolation are intact.

- [ ] Parse `.pages.yml`, `_config.yml`, and the fixture front matter as YAML.
- [ ] Confirm `.pages.yml` contains merge mode and all four operations.
- [ ] Confirm the archive and homepage include filter unpublished notes.
- [ ] Confirm the homepage include contains `limit: 3`.
- [ ] Compare the feature branch against `gh-pages` and verify no public-branch write occurred.
