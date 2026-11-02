# Wireframes and mockups

Six standalone HTML artifacts built to show how an agent can use real product
context instead of applying a generic interface style.

## Effective HTML comparison

- `effective-html-compare-wireframe.html` tests three structures for comparing
  two live artifacts: split, stacked, and focused review.
- `effective-html-compare-mockup.html` applies the Effective HTML Working Atlas
  system to the selected split comparison.
- Source context: `site/DESIGN.md`, `site/PRODUCT.md`, the current catalog, and
  the existing same-origin artifacts.
- Skill use: `html-wireframe` for the structural directions, then
  `design-artifact` with `html-prototype` in mockup mode for the finished view.

## Plannotator review workspace

- `plannotator-review-wireframe.html` tests canvas-first, comments-first, and
  review-queue structures for annotating rendered HTML.
- `plannotator-review-mockup.html` follows Plannotator's current dark review
  surface, annotation rail, selected-comment treatment, and send-feedback
  action.
- Source context: the public Plannotator repository, current HTML annotation
  and code-review screenshots, and the review UI components.
- Skill use: `html-wireframe` for the structure, then `design-artifact` with
  `html-prototype` in mockup mode for system alignment.

## Product change review

- `product-change-review-wireframe.html` compares current and proposed member
  role behavior across direct comparison, states, and mobile views.
- `product-change-review-mockup.html` turns the same synthetic brief into a
  polished review artifact. It is not a production product or a product claim.
- Source context: a bounded synthetic brief about moving role actions out of an
  overflow menu and showing permission limits before submission.
- Skill use: `html-wireframe` for the evidence layout, then `design-artifact`
  with `html-prototype` in mockup mode for the finished review surface.

Every artifact is self-contained and requires no network connection or build
step. Catalog screenshots and static and animated SVG previews sit beside these
files.
