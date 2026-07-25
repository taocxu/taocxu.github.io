# Blog & Research Notes Preview Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a branch-only, fully navigable preview of a `BLOG & RESEARCH NOTES` feature while leaving the published homepage and stylesheet untouched.

**Architecture:** Add four isolated preview files. `notes-preview.html` fetches and renders the existing homepage at runtime, injects the seventh navigation item and the homepage notes section, and loads `notes-preview.css`. The notes archive and single-note page are standalone HTML documents that reuse `site-v2.css` plus the preview stylesheet.

**Tech Stack:** Static HTML5, CSS Grid/Flexbox, minimal vanilla JavaScript, existing `site-v2.css`.

## Global Constraints

- Modify only `feature/blog-research-notes-preview`.
- Do not modify `index.html` or `site-v2.css`.
- Do not modify `gh-pages`.
- Homepage preview displays exactly three placeholder notes.
- No categories, tags, descriptions, cards, sidebars, comments, reading counts, or mandatory references section.
- Navigation order must be `Home · Research · Publications · Projects · Grants · Notes · CV`.
- Desktop note row: title left, `Read note →` right.
- Mobile note row: stacked without horizontal overflow.

---

### Task 1: Preview stylesheet

**Files:**
- Create: `notes-preview.css`

**Interfaces:**
- Consumes: existing CSS variables and layout classes from `site-v2.css`.
- Produces: `.notes-list`, `.note-preview`, `.note-date`, `.note-preview-row`, `.note-preview-title`, `.note-read-more`, `.notes-archive`, `.note-article`, `.note-back-link`.

- [ ] **Step 1: Create the preview-only stylesheet**

Use existing colour variables and typography. Keep section spacing consistent with `.content-section`. Set `.note-preview-row` to flex with `justify-content: space-between`, `align-items: baseline`, and a fixed gap. Add a mobile rule at `680px` that changes the row to block layout.

- [ ] **Step 2: Verify style isolation**

Confirm the file contains no selectors that alter `.site-header`, `.content-section`, `.section-heading`, `.timeline`, or other existing site components globally.

- [ ] **Step 3: Commit**

```bash
git add notes-preview.css
git commit -m "Add preview styles for research notes"
```

### Task 2: Branch-only homepage preview

**Files:**
- Create: `notes-preview.html`

**Interfaces:**
- Consumes: `index.html`, `site-v2.css`, `notes-preview.css`.
- Produces: a complete rendered homepage preview with a seventh `Notes` navigation link and a three-item `BLOG & RESEARCH NOTES` section.

- [ ] **Step 1: Create a loading shell**

The page must fetch `index.html`, parse it with `DOMParser`, append `notes-preview.css` to the parsed `<head>`, and copy the parsed head and body into the preview document.

- [ ] **Step 2: Inject navigation**

Insert `<a href="notes/index-preview.html">Notes</a>` immediately after the existing `Grants` link and before `CV`.

- [ ] **Step 3: Inject homepage section**

Create a `.content-section#notes-preview-section` after `#reports` and before the next section. The section label is `BLOG & RESEARCH NOTES`. Add exactly three placeholder note entries with dates, titles, and `Read note →` links to `notes/example-note-preview.html`.

- [ ] **Step 4: Preserve homepage links**

Do not rewrite existing navigation or document links. Only add the preview-specific links.

- [ ] **Step 5: Commit**

```bash
git add notes-preview.html
git commit -m "Add branch-only homepage notes preview"
```

### Task 3: Notes archive preview

**Files:**
- Create: `notes/index-preview.html`

**Interfaces:**
- Consumes: `../site-v2.css`, `../notes-preview.css`.
- Produces: independent archive page listing the same three placeholder notes in reverse chronological order.

- [ ] **Step 1: Reuse the existing header and footer language**

Use the current site name, seven-item navigation, footer wording, content width, and section heading structure.

- [ ] **Step 2: Add archive listing**

Display `BLOG & RESEARCH NOTES` as the main section label and list the three placeholder notes using the same date-title-link structure as the homepage preview.

- [ ] **Step 3: Verify relative links**

Home links point to `../index.html`; preview Notes links point to `index-preview.html`; note links point to `example-note-preview.html`.

- [ ] **Step 4: Commit**

```bash
git add notes/index-preview.html
git commit -m "Add research notes archive preview"
```

### Task 4: Single-note template preview

**Files:**
- Create: `notes/example-note-preview.html`

**Interfaces:**
- Consumes: `../site-v2.css`, `../notes-preview.css`.
- Produces: independent readable note page with no mandatory references block.

- [ ] **Step 1: Add unified header and navigation**

Use the same seven-item navigation as the archive page.

- [ ] **Step 2: Add article structure**

Include the placeholder title, date, three short placeholder paragraphs, and a `← Back to Blog & Research Notes` link.

- [ ] **Step 3: Constrain reading width**

Use `.note-article` to cap the article body at `760px` while remaining left-aligned within the section body.

- [ ] **Step 4: Commit**

```bash
git add notes/example-note-preview.html
git commit -m "Add single research note template preview"
```

### Task 5: Verification

**Files:**
- Verify: `notes-preview.html`
- Verify: `notes-preview.css`
- Verify: `notes/index-preview.html`
- Verify: `notes/example-note-preview.html`

**Interfaces:**
- Produces: evidence that the preview is isolated, responsive, and linked correctly.

- [ ] **Step 1: Confirm public branch isolation**

Compare `gh-pages` with its pre-preview state and confirm no public file changed.

- [ ] **Step 2: Confirm branch diff scope**

Compare `gh-pages...feature/blog-research-notes-preview`. Expected changed files are only the two documentation files and four preview files.

- [ ] **Step 3: Validate HTML structure**

Confirm every preview page has one `<main>`, one `<header>`, one `<footer>`, and no broken relative stylesheet paths.

- [ ] **Step 4: Validate responsive rules**

Confirm `notes-preview.css` contains a `max-width: 680px` rule that stacks `.note-preview-row` and prevents link compression.

- [ ] **Step 5: Open branch preview**

Use a branch-capable static preview URL and inspect desktop and mobile widths before proposing any merge.
