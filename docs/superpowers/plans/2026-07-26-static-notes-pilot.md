# Static Notes Pilot Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Publish a rollback-safe, fully static Notes pilot with the two approved Notes, while adding four additional Notes only to a separate preview branch.

**Architecture:** Build production from the restored static `gh-pages` tree. Replace no production page with Liquid or runtime templating. The production homepage, Notes archive, and two Note pages are complete HTML files deployed only by the existing static Pages workflow; the Jekyll deployment workflow is removed from the release. A separate preview branch contains six complete static Note pages and a six-note archive, with only the two approved Notes present in production.

**Tech Stack:** Static HTML5, CSS, GitHub Pages static workflow, Git branches and immutable archive refs.

## Global Constraints

- Preserve the current restored public site in a dedicated archive branch before publishing.
- Production must contain no Liquid tags (`{%`, `{{`) and no YAML front matter in served HTML.
- Production publishes only the two already approved Notes.
- The four newly uploaded Notes remain preview-only and unpublished.
- Preserve Word wording and paragraph order; formatting changes are limited to faithful bold/italic restoration plus restrained conceptual emphasis.
- `Notes` appears before `Grants` and scrolls to the homepage Notes section.
- Homepage displays at most the latest three Notes; the production archive displays all two approved Notes.
- Keep the prior feature and archive branches intact.

---

### Task 1: Create rollback and isolated release branches
- [ ] Create a new immutable archive branch from current `gh-pages`.
- [ ] Create a new release branch from current `gh-pages`.
- [ ] Verify both point to the restored commit before edits.

### Task 2: Build complete static production pages
- [ ] Generate a complete static homepage from the restored homepage with Notes navigation and a two-item Notes section.
- [ ] Add `notes.css`.
- [ ] Add `notes/index.html` and two complete static Note pages.
- [ ] Remove the Jekyll deployment workflow from the release branch, retaining only static deployment.
- [ ] Ensure production HTML contains no Liquid or front matter.

### Task 3: Verify and publish production
- [ ] Check all internal paths, anchors, CSS references, and article backlinks.
- [ ] Verify release diff is limited to Notes pages, homepage integration, stylesheet, and removal of the conflicting Jekyll workflow.
- [ ] Merge the release branch into `gh-pages` only after all checks pass.
- [ ] Confirm public source is static HTML after deployment.

### Task 4: Build six-note preview branch
- [ ] Create a new preview branch from the static release branch.
- [ ] Convert the four Word files into faithful static Note pages.
- [ ] Restore Word bold/italic formatting and add restrained conceptual emphasis.
- [ ] Add all six Notes to the preview archive and latest three to the preview homepage.
- [ ] Verify the four new Notes are absent from production.
