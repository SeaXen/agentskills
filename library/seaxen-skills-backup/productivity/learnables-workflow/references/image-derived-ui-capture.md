# Image-derived UI capture

Use this when a Learnables thread asks Hermes to "learn this image", "remember this design", or recreate a screenshot-driven UI later.

## Goal
Turn one screenshot into reusable reconstruction notes without pretending pixel-perfect certainty.

## Capture checklist
1. Source path/URL of the image
2. What the screen is (settings page, dashboard card, pricing table, modal, etc.)
3. Visible text
4. Structural layout
   - sections
   - columns/rows
   - cards/panels
   - alignment
5. Visual system
   - background
   - text hierarchy
   - colors
   - typography feel
   - spacing density
   - borders/radius/shadows
6. Component patterns
   - tables
   - pills/badges
   - input rows
   - icons/checkmarks
   - labels/helper text
7. Rebuild spec
   - concise CSS/Tailwind-facing notes
   - optional JSON data model if the UI is data-driven
8. Confidence split
   - high-confidence facts
   - medium-confidence reconstruction
   - uncertain details

## Tooling notes
- Prefer vision first.
- If vision fails, OCR + manual reconstruction is acceptable.
- OCR output alone is not enough; convert it into a layout/design spec.
- Keep exact env vars, labels, and provider names when readable.
- Do not claim exact fonts/icons unless clearly visible.

## Example pattern from this session
Dark comparison table UI with columns like provider / env var / search / extract / free tier. OCR established provider names and env vars; final notes preserved uncertainty around exact iconography and title text.
