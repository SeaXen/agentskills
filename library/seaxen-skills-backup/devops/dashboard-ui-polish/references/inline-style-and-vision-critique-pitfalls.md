# Inline `<style>` blocks & vision-critique pitfalls

Session lessons from polishing AceRoute's dashboard after tiered KPI work appeared to do nothing.

## 1) Inline `<style>` blocks in monolithic SPAs defeat external CSS edits

**Symptom:** You append new tiered-KPI / hero-card CSS to `layout-v2.css?v=N`, the file grows, the browser fetches it, but the rendered layout is unchanged.

**Root cause:** Large single-file dashboards often have a big `<style>` block inline in `<head>` with `!important` rules on the same selectors you just styled in the external file. Inline rules load after the external link, so they win.

**Real example from AceRoute:**
- External `layout-v2.css` (appended): `#homeSummary .mini-stat.kpi-hero { grid-column: span 4 !important; ... }`
- Inline `<style>` in `index.html` (line 179): `#homeSummary.tools-stats-row { display: grid !important; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)) !important; ... }` and `#homeSummary .mini-stat { ... flex-direction: column; ... }`

Result: KPI tiles wrap onto 7 rows of 1–3 tiles each instead of the intended 12-col grid with heroes.

**Diagnostic:**
1. After CSS edit, use the browser console to read `getComputedStyle(targetEl).gridTemplateColumns`. If it shows your intended value, the CSS loaded. If it shows the old `auto-fit minmax` value, the inline `<style>` block is winning.
2. `rg -n "selector-name" index.html` will reveal inline overrides.

**Fixes (in order of preference):**
1. **Patch the inline `<style>` block** — replace the offending selector with your new rule. This is almost always the right call for monolithic single-file dashboards.
2. **Move the inline `<style>` to the external CSS file** — risky if you don't fully understand all the rules; can break other pages.
3. **Use higher specificity** — `#pageSpecificId #homeSummary .mini-stat.kpi-hero { ... }` works but couples your CSS to markup IDs and makes future changes harder.

**Rule of thumb for monolith SPAs:** any new layout pattern must be diff'd against the inline `<style>` block in `index.html` before assuming the external CSS will apply.

## 2) Don't trust upstream vision-tool design critiques uncritically

**Symptom:** A vision model returns a long, confident critique with specific claims like "all filter chips say 'All events'", "timestamps appear in the Owner column", or "20+ (untitled) sessions visible". You start patching based on those claims.

**Root cause:** Vision LLMs often **confabulate** plausible-sounding specifics to match generic dashboard tropes (admin-template complaints, generic SaaS critique). The specifics may not match the actual rendered UI.

**Diagnostic:**
- `rg` for the specific string in the served HTML or JS source — e.g. `rg -n "All events"` in the JS will show whether "All events" is even rendered.
- Cross-reference with `browser_console(expression=...)` reading actual `getComputedStyle` or DOM text content.
- Use your own vision model (`vision_analyze` with `image_url=<screenshot>` and a concrete question) for the screenshot — that gives you direct pixel evidence.

**Real example from this session:**
- Upstream `browser_vision` claimed Sessions page had "All filter chips say 'All events'", "timestamps in wrong columns", and "20+ (untitled) sessions".
- These claims were not findable in the actual HTML/JS. The vision tool confabulated admin-template complaints.
- A second pass with `vision_analyze` (a different vision path) correctly identified the real issues: flat KPI hierarchy, mixed time formats, empty cost chart, raw session IDs.

**Rule:** For UI critique work, use vision tools for **layout/shape description** (which row layout is visible, what colors dominate, what icons are present). Do **not** treat their prose critiques as verified fact. Always ground specific textual claims in code or DOM inspection before patching.

## 3) Real polish wins worth shipping (verified patterns)

After the noise is filtered, the genuine fixes for a dense operator dashboard:
- **3-tier KPI grid**: 12-col CSS grid; `kpi-hero` span 4, `kpi-secondary` span 2, `kpi-tertiary` span 2. Inside hero tiles, render delta% as a small colored chip (`up`/`down`/`flat`) next to the value.
- **Empty-state charts**: when a chart has no samples, hide the canvas and render a centered dashed panel with a title + 1-line hint. Show a flat zero-line chart instead and the product looks broken.
- **Time format consistency**: pick 24h for operator tools. Make `fmtTime24` a separate helper so locale-driven 12h isn't accidentally called from headers.
- **Demote raw IDs in user-facing lists**: if a session has no `title`, show `(untitled)` and demote the raw session ID to a muted mono sub-line. Better still, hide the row entirely.
- **Nav icons via inline SVG mask**: a single `::before` with `-webkit-mask-image: url("data:image/svg+xml;...")` per `data-page` selector gives clean monochrome nav icons without bundling icon fonts.
- **`:focus-visible` rings**: 2px solid accent + 2px offset, applied to buttons/links/inputs. Costs nothing, helps keyboard ops and accessibility.

## 4) Be honest about ceiling scores

When the user asks to push to "10/10", check whether the gap is:
- **Incremental CSS/polish** → ship it.
- **Requires design system / new theme / nav redesign / data hygiene fix** → say so. Don't fake the score.
- **Requires source data cleanup (sessions without titles, missing cost records)** → that's not a UI problem.

Realistic ceiling for a single-author, single-repo, no-real-design-system dashboard is roughly 9.2–9.4. Pushing past needs Figma → tokens, content audit, and dedicated IA work — not another CSS patch.
