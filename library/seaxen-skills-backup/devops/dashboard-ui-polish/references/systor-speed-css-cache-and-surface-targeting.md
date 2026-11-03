# Systor Speed-page CSS cache + surface-targeting lessons

Use this reference when a user is iterating on the Systor `Speed` page from screenshots and keeps saying "nothing changed" or "you changed the wrong thing".

## Surface-mapping rule
The Speed hero has multiple visible layers:
- outer dark container: `.speed-live-hero`
- outer runner shell: `.speed-live-runner`
- inner GO tile/button: `#speed-go-btn` + `.speed-go-panel`
- Stop button: `#speed-stop-btn` + `.speed-stop-btn`

If the user says:
- "only GO button blue"
- "not full card"
- "hero dark, GO blue"

then inspect computed backgrounds for **all four** layers. Do not assume the visible blue surface is the same node you styled.

## Public-vs-local verification rule
Localhost can be correct while the public page is stale.

Always verify:
1. deployed/public URL the user is actually viewing
2. stylesheet URL version (`style.min.css?v=...`)
3. computed background on `.speed-live-hero`, `.speed-live-runner`, and `#speed-go-btn`

If the user still sees the old layout on mobile, it is often cache rather than logic.

## Cache-busting pattern
When visual CSS changes matter:
- update the stylesheet link in `base.html` from `?v=X` to `?v=X+1`
- rebuild minified CSS
- redeploy/restart
- confirm the public HTML now serves the new version string

Without this, a phone screenshot can stay on stale CSS for several turns and create fake regressions.

## Helper-copy pitfall
For this user, visible helper/accessibility strings are read as clutter/regressions.
Examples to avoid unless explicitly requested:
- `Skip to content`
- `Live system overview...`
- explanatory blurbs under dense dashboard headings

Keep ARIA/focus semantics, but do not surface visible helper copy.

## Mobile compacting pitfall
If mobile KPI cards still look large after several spacing tweaks, check for a late override forcing `min-height` back up. One bad late rule can silently undo earlier compacting.

Concrete regression seen here:
- mobile KPI cards remained big because a late override forced `min-height: 68px`
- fixing that one line was more important than more padding tweaks

## Geometry reminder
For this user, words like:
- `only`
- `full`
- `same`
- `like screenshot`

are literal geometry requirements, not approximate intent.