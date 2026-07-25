# Writing and Managing Blog & Research Notes

This site supports two parallel authoring paths. Pages CMS is a convenient browser interface, while direct Markdown editing remains fully supported and may be the primary workflow.

## Pages CMS workflow

1. Open the hosted Pages CMS application and sign in with GitHub.
2. Select the `taocxu/taocxu.github.io` repository.
3. While this infrastructure is under review, select the `feature/blog-research-notes-preview` branch. Do not select `gh-pages` unless the infrastructure has later been approved and merged.
4. Open `Blog & Research Notes`.
5. Use `Create` to make a new note. The editor provides:
   - Title
   - Date
   - Published toggle
   - Markdown body
6. Keep `Published` off while drafting. Saving with `published: false` keeps the note out of the rendered website.
7. Turn `Published` on only when the note is ready to appear publicly and the infrastructure is already present on the published branch.
8. Use rename to change the Markdown filename when necessary.
9. Use delete to remove a note file. Git history still records the deletion and allows recovery.

Pages CMS writes directly to GitHub. It does not maintain a separate content database.

## Direct Markdown workflow

Create a file in `_notes/` using a concise URL-safe filename, for example:

```text
_notes/hirschman-revolutionary-optimism.md
```

Use this front matter:

```yaml
---
title: Hirschman’s Hiding Hand and China’s Revolutionary Optimism
date: 2026-07-24
published: false
---
```

Write the note in Markdown below the closing `---`.

Change `published: false` to `published: true` only when the note should be rendered. There are no required categories, tags, images, summary, or References section.

## Site behaviour

- Published notes receive stable URLs under `/notes/<filename>/`.
- The full archive at `/notes/` lists all published notes in reverse chronological order.
- The homepage include displays the latest three published notes.
- Unpublished notes are excluded from both lists and from public rendering.
- The `Notes` navigation item belongs before `Grants` and scrolls to the homepage Notes section.
- The archive is reached from a note through `← Back to Blog & Research Notes`.

## Infrastructure fixture

`_notes/infrastructure-test.md` is an unpublished test document. It verifies that Pages CMS can discover the collection without creating a public page. Delete it after the first substantive note is created.
