# Static Notes Pilot Design

## Production architecture

Production remains fully static. The `gh-pages` branch serves complete HTML and CSS files through the existing static Pages workflow. No production HTML contains Liquid tags, Jekyll includes, collection iteration, or YAML front matter.

The homepage contains a `Notes` navigation item before `Grants`, linking to the homepage section `#notes`. The homepage section lists the two approved Notes. The full archive lives at `/notes/`, and each approved Note has its own complete static `index.html` page.

## Deployment discipline

Before publication, the current restored `gh-pages` commit is preserved in a new archive branch. A clean release branch is created from that commit. The conflicting Jekyll Pages workflow is removed from the release, leaving only the raw static deployment workflow.

Publication occurs through a pull request after static-source checks confirm that served HTML contains no `{%`, `{{`, or front matter and that all links and anchors resolve.

## Preview architecture

A separate preview branch is created from the static release. It contains the two approved Notes plus four newly uploaded Notes. The four new Notes do not enter production. Their wording and paragraph order are preserved, Word formatting is restored, and additional emphasis is restrained and conceptual.

The preview homepage lists the latest three Notes by date; the preview archive lists all six.

## Rollback

The new archive branch, the earlier pre-pilot archive branch, and the release branch are all retained. Restoring the public site requires moving `gh-pages` to the chosen archive commit.
