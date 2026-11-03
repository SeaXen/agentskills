# Systor Speed-page regression lessons

Session-specific lessons from a real polish/debug pass.

## 1. Visible helper/accessibility copy is a correctness issue for this user
For dense operator dashboards, if the user says remove helper text or complains about page chrome clutter, remove it literally.

Do not leave visible strings like:
- `Live system overview...`
- `Skip to content`

If you add accessibility affordances, they must not become visible page chrome. A visible skip link on a dense dashboard will be read as a regression.

## 2. Functional vs visual breakage on the Speed GO hero
A GO button can be functionally working while still reading as broken if styling collapses.

Observed pattern:
- click path works
- backend run starts
- phase/status update correctly
- but computed hero styles become effectively transparent / dull
- user reports "GO not working" because the control looks dead

Debug rule:
- verify both the click path and computed styles
- inspect `background`, `border`, `box-shadow`, and text color on the live hero button
- if behavior works but visuals read dead, treat it as a real bug, not user confusion

## 3. Do not replace the hero label with cryptic phase abbreviations
On this class of Speed page, keep the hero core label as `GO` even while a run is active.

Bad regression pattern:
- `ST`, `DO`, `UP` from phase abbreviations in the center of the hero

Preferred pattern:
- hero core remains `GO`
- phase/status text is shown elsewhere (`starting`, `download running`, `upload running`, etc.)

## 4. Cache-bust CSS after live style fixes
When UI still appears unchanged after a real CSS fix, verify whether the deployed page is still loading the old asset URL.

Pattern:
- update CSS
- rebuild/minify
- if the browser still shows old layout/styling, bump the stylesheet query version in the base template
- verify the live page loads the new `style.min.css?v=...` URL

## 5. For this user, screenshot complaint beats geometry optimism
DOM/geometry verification is useful, but if the user says the page still looks wrong, continue.

Use DOM probes to isolate structure/state, but do not claim success until the visible complaint is gone.
