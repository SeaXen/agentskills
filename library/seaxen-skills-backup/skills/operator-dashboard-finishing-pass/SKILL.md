---
name: operator-dashboard-finishing-pass
description: Finishing-pass workflow for dense operational dashboards after the core data views already exist — prioritize compactness, cross-page consistency, and actionable drilldowns over passive widget sprawl.
---

# Operator Dashboard Finishing Pass

Use this when a dashboard already has the main pages and data, and the user wants the **next pass** to make it feel sharper, denser, and more useful to operate.

This is especially relevant for:
- analytics dashboards
- admin/operator consoles
- monitoring surfaces
- multi-page internal tools with cards, tables, chips, and drawers

## What this pass is for

Not the first implementation.
Not the raw data plumbing.
Not random cosmetic tweaks.

This pass is for turning a working dashboard into a **faster investigation surface**.

## Core rule
After compactness/brightness/shared-surface cleanup is mostly in place, the highest-value next step is usually **click-through intelligence**, not adding more passive summary cards.

If the user asks for “next pass”, “add/improve feature”, or “what more can we add?”, prefer:
1. actionable insight chips
2. direct drilldowns
3. operator watchlists / outlier rails
4. quick filters from summary surfaces

Only add more widgets if they answer a question the current UI cannot answer.

## User-pattern lesson embedded here
For this user class, passive summary widgets are less valuable than:
- clickable insight chips
- rows that open drawers directly
- source/model/provider/session drill actions
- outlier surfacing that lands on the exact object to inspect

Also: when the user references another product (for example a trading app) they often want the **design language only** — density, dark rhythm, hierarchy, compact operator feel — **not** a same-to-same clone of that product or of a sibling internal dashboard.

## Design-source discipline
When the user says "take the idea only" or explicitly rejects a clone:
- copy layout principles, not product structure
- do not mirror the source app's feature map one-for-one
- do not insert fake domain widgets just to match the inspiration (for example equity, order book, buy/sell, or market rails when the product is actually a Hermes operator console)
- every top-level panel must map to real local data or a real operator action
- if two internal dashboards must be merged into one home surface, prefer one dense unified dashboard over a tab soup or a visual reskin of one source

See `references/design-language-only-not-clone.md` for the concrete anti-clone checklist and the single-batched-endpoint pattern that came out of this class of work.

## Recommended order for a finishing pass

### 1. Shared UI first
Fix shared surfaces before page-local tweaks:
- card padding
- table density
- chart heights
- chip rhythm
- hover behavior
- mobile density
- shared page bars / headers

### 2. Identify operator questions per page
For each page, ask:
- what changed?
- what is hottest?
- what is riskiest?
- what is abnormal?
- what should I click next?

### 3. Prefer lightweight derived insight rails
Build compact insight strips from existing payloads first:
- top source
- top model
- hottest finish reason
- heaviest session
- costliest session
- freshest channel
- tool-heavy object
- best efficiency object

Do not start by inventing new backend queries if the current payload already exposes enough.

### 4. Convert summaries into actions
The insight layer should open something precise when possible:
- source insight -> filtered page or source drawer
- model insight -> model drawer or model-filtered page
- session/outlier insight -> session drawer
- provider insight -> provider/model filtered view
- tool bundle insight -> tool detail or tool-filtered page
- pressure/ops insight -> ops page

### 5. Only then add new panels
If the page still lacks useful operator signal, add a new compact panel. Good additions:
- role breakdown
- handoff/compression issues
- burn-risk strip
- outlier session list
- platform health strip

## Layout guidance

### Prefer these
- one shared insight row near the top
- one compact watchlist card instead of several medium cards
- same chip/card language across pages
- compact hover cues that imply clickability
- equal-height top surfaces when feasible
- **KPI / stats rows on ONE horizontal line** across every page (Home-style). Use `display:flex; flex-wrap:nowrap; overflow-x:auto` with children `flex:1 1 0; min-width:~100px`. Never leave a single orphan KPI on a second row.
- insight chips and filter chip bars also stay one scrollable line (`nowrap` + overflow-x), not multi-line wrap soup
- nav for 10+ pages: **flat primary nav with horizontal scroll + Cmd-K palette** is preferred when all pages are peer-importance. Reserve **primary 6–8 tabs + More ▾ menu** for cases where the IA genuinely has primary/secondary tiers. Hiding peer pages behind "More ▾" is an IA smell. See `references/cmdk-palette-and-inline-sparks.md`.
- default global time window to a short range (**7d**), not all-time; all-time deltas are often meaningless and look broken

### Avoid these
- passive stats repeated in three places
- giant decorative summary cards
- page-local styles that break the shared rhythm
- adding a full new tab when an existing page can hold the new signal
- passive insight chips with no follow-through path
- **`grid-template-columns: repeat(N, minmax(0,1fr))` that still orphans** on real widths, or `auto-fit minmax(150px,1fr)` for 7–8 KPIs (wraps the last card)
- mobile CSS that switches KPI rows to wrapping grids and undoes desktop one-line rules
- raw LLM session titles with `<think>…</think>` / markup in chips, tables, or podiums — strip server-side and client-side (`cleanTitle` / `clean_title`)
- stuck header “Loading…” after data is already painted — every page paint should `markUpdated(ts)`

### Shared KPI CSS pattern (canonical)
```css
.tools-stats-row, .stats-inline-row {
  display: flex !important;
  flex-wrap: nowrap !important;
  gap: 8px !important;
  overflow-x: auto !important;
  grid-template-columns: none !important;
}
.tools-stats-row > .mini-stat {
  flex: 1 1 0 !important;
  min-width: 104px !important;
}
```
Use one shared `statCards([...])` builder on every page; do not hand-roll page-local KPI HTML that drifts.

See `references/kpi-single-line-and-nav-density.md` for the AceRoute-class audit findings and verification checklist.

## Interaction rules

When an insight can be acted on, make it clickable and visibly so:
- pointer cursor
- hover elevation/border cue
- direct jump to filtered page/drawer

If a chip cannot land anywhere meaningful, keep it passive.
Do not fake clickability.

## Verification checklist
- shared CSS still compact after the pass
- new chips/rows actually appear in served HTML
- click targets map to real handlers/functions
- JS syntax passes (`node --check`)
- backend syntax/type checks pass
- asset version/cache-bust updated when needed (`?v=N` on css/js)
- live page serves the new version (for Docker host-mounted `./static`, no rebuild needed for CSS/JS; restart only for Python)
- **visual:** every major page’s KPI strip is one row with no orphan card (browser screenshot)
- header shows real `Updated: …`, not stuck Loading
- sample titles/insights do not contain `<think` or raw reasoning tags

## Good examples of this pass
- convert “Top source” chip to open filtered Sessions
- convert “Burn risk” chip to open the risky session drawer
- convert “Most costly channel” chip to open channel drawer
- convert “Best $/M” chip to open model drawer
- convert “Top bundle” tool chip to open tool detail

## Bad examples of this pass
- add another row of passive KPIs with no action path
- create a new page for information that fits in an existing page
- add dense text blocks instead of compact operator cues
- expand layout size when the user already wants compactness

## Multi-pass upgrade when user wants “10/10 all sectors”
Do **not** only retheme. Sequence:
1. Shared layout (KPI one-line, nav flat with optional More, chip rails, loading/title hygiene, default 7d)
2. Data trust (local TZ day boundaries, clean titles server-side, **verify actual timeline field names by curling the API — do not assume**)
3. Security (optional API key for write/test; never leave extract-test unauth on a public bind without a key path)
4. Page IA (Search/long pages → subtabs, not card soup)
5. Deploy truth (static mount ≠ Python live; short smoke suite)
6. **JS module split** — extract shared utils (`escapeHtml`, `cleanTitle`, `fmt*`, `statCards`, `apiFetch`, `authHeaders`, `getApiKey`, `markUpdated`, `emptyPanel`) out of the monolithic `dashboard.js` into a small `core.js` that bridges back to globals so existing call sites still work. Last because it must come after the surface area has settled. See `references/js-monolith-module-split.md`.
7. Empty-state polish — every Chart.js site calls `paintChartEmpty(canvasId, msg)` when its data array is empty, and `clearChartEmpty(canvasId)` immediately before `new Chart(...)`. See the empty-state pair code block below.
8. Expand the smoke suite and replace any bash subshell `python3 -c 'json.load'` field checks with `grep -F` substring probes (see pitfall below and `scripts/dashboard-smoke.sh`).
9. **3-tier KPI grid** — hero/secondary/tertiary tile hierarchy on Home. Heroes hold delta chips + click-through to deep pages. CSS lives in inline `<style>` block, not external (see inline-style pitfall in `dashboard-ui-polish`).
10. **Flat primary nav + Cmd-K palette** — for 10+ peer-importance pages, prefer a flat horizontally-scrollable nav strip plus a Cmd-K palette as the primary discovery mechanism over a "More ▾" menu that hides peer pages. See `references/cmdk-palette-and-inline-sparks.md` for full code.
11. **Inline SVG sparklines** in hero KPIs (zero Chart.js cost, ~50 LOC, race-condition free). Same reference.
12. **Design-token architecture** — proper layered tokens (`--c-*` primitives → semantic `--bg`/`--text`/`--card` aliases, plus motion/spacing/z-index/radius/shadow/typography scales). Enables real light theme + future themes without touching components. See `references/design-token-architecture.md` for the full token sheet + cascade traps.
13. **Polish features bundle** — page transition animation, keyboard help panel (`?`), sticky table headers, drag-to-reorder Home KPIs (with MutationObserver re-bind pattern), two-key nav (`g`+key), number-key nav (`1-9`), `r` refresh. See `references/polish-features-bundle.md` for the polish.js template + ordering.
14. **Browser-verify discipline** — `browser_vision` resets the page to `about:blank`; the next `browser_console` returns `hasAR: false` even though scripts loaded fine. Test with `navigate + console` in the same turn, never interleave vision + console. See `references/browser-verify-discipline.md`.

See `references/kpi-single-line-and-nav-density.md`, `references/cmdk-palette-and-inline-sparks.md`, `references/design-token-architecture.md`, `references/polish-features-bundle.md`, and `references/browser-verify-discipline.md` for the full AceRoute-class checklists.

### Be honest about the ceiling
When the user asks to push to "10/10", check whether the remaining gap is:
- **Incremental CSS / polish / interactivity** → ship it.
- **Requires a real design system** (Figma → tokens, light theme done properly, icon library) → say so, score ~9.3 honestly.
- **Requires source-data cleanup** (sessions without titles, missing cost records) → not a UI problem, tell the user.

Realistic ceiling for a single-author, single-repo dashboard with no design system: **~9.4**. Pushing past needs a dedicated design pass, not another CSS edit. The user respects an honest ceiling more than a faked 10/10.

**Revised ceiling with proper design-token layer + polish features bundle shipped:** **~9.7**. Beyond that requires real Figma → tokens round-trip with a designer, light-theme parity audit, e2e Playwright suite, and source-data cleanup (sessions without titles etc.). State the ceiling honestly per pass.

### Data-shape assumption trap (always curl first)
Before writing series extraction code, `curl` the API and inspect field names:
```bash
curl -sS "http://localhost:8866/api/home/dashboard?days=7&fresh=1" \
  | python3 -c 'import sys,json;d=json.load(sys.stdin); print(list((d.get("timeline") or [{}])[0].keys()))'
```
Guessing `input_tokens` / `cost_usd` / `latency_ms` when the API returns `tokens` / `cost` / `latency` produces flat-zero sparklines with no obvious error. The fix is "look first, code second."

### Python heredoc + JS arrow function pitfall
When patching JS via `execute_code` and the JS contains `=>`, Python's heredoc will choke on the arrow. Use `write_file`, `patch`, or shell `cat <<'EOF'` (single-quoted heredoc — no shell interpolation). Full pattern in `references/cmdk-palette-and-inline-sparks.md`.

## JS module split — bridge-to-global pattern (monolithic SPAs)
When the SPA is a single 5k-LOC `dashboard.js` with `defer` scripts in order:

1. Create `static/js/core.js` that defines helpers on a `window.AceRoute` namespace, then aliases the names back onto `window` so the existing `dashboard.js` body, which calls `escapeHtml(...)` as a free identifier, keeps working without rewriting thousands of call sites:
   ```js
   (function (global) {
     'use strict';
     var AR = global.AceRoute = global.AceRoute || {};
     AR.escapeHtml = function (s) { /* ... */ };
     AR.statCards  = function (rows) { /* ... */ };
     // ...
     var bridge = ['escapeHtml','cleanTitle','fmt$','statCards','apiFetch' /*...*/];
     bridge.forEach(function (name) { global[name] = AR[name]; });
   })(window);
   ```
2. From `dashboard.js`, **delete the duplicate function definitions** with a brace-counting regex pass in Python (sed/awk escapes badly). Full script lives in `references/js-monolith-module-split.md`.
3. Load order in `index.html`: `core.js` then any page module then `theme.js` then `dashboard.js`. Use `?v=N` cache-bust on each.
4. Verify: `node --check` on all three; smoke on the live HTML to confirm `AceRoute` namespace is set; one screenshot to confirm zero visual regression.
5. Do **not** attempt this before layout/TZ/auth/search-tabs are settled — moving helpers while the surface is still in flux wastes the deletion pass.

## Empty-state pattern for Chart.js (and any canvas/panel)
After every `new Chart($('canvasId'), ...)` site, wrap with two guards. Add to `core.js`:
```js
AR.paintChartEmpty = function (canvasId, message) {
  var c = document.getElementById(canvasId); if (!c) return;
  var wrap = c.parentElement; if (!wrap) return;
  c.style.display = 'none';
  var old = wrap.querySelector('.empty-panel'); if (old) old.remove();
  var div = document.createElement('div');
  div.className = 'empty-panel chart-empty';
  div.innerHTML = '<div class="empty-panel-title">No chart data</div>' +
                  '<div class="empty-panel-hint">' + AR.escapeHtml(message || 'No samples in this window.') + '</div>';
  wrap.appendChild(div);
};
AR.clearChartEmpty = function (canvasId) {
  var c = document.getElementById(canvasId); if (!c) return;
  var wrap = c.parentElement; if (!wrap) return;
  c.style.display = '';
  var old = wrap.querySelector('.empty-panel'); if (old) old.remove();
};
```
At each chart site:
```js
if (!d.hourly || !d.hourly.length) { paintChartEmpty('timelineChart', 'No search volume in last 7 days.'); return; }
clearChartEmpty('timelineChart');
charts.timeline = new Chart($('timelineChart'), { /* ... */ });
```
And pair with `.empty-panel` / `.empty-panel-title` / `.empty-panel-hint` CSS:
```css
.empty-panel{padding:32px 20px;text-align:center;background:rgba(255,255,255,.02);border:1px dashed rgba(255,255,255,.08);border-radius:var(--radius-md,12px);color:var(--muted)}
.empty-panel-title{font-size:var(--font-base,14px);font-weight:600;color:var(--text);margin-bottom:4px}
.empty-panel-hint{font-size:var(--font-small,12px);color:var(--muted);max-width:46ch;margin:0 auto;line-height:1.5}
.chart-empty{min-height:120px;display:flex;flex-direction:column;justify-content:center}
```
Without this, empty windows show a bare blank canvas — looks broken even when the backend is correct.

## Smoke-script pitfall (bash + JSON field assertions)
A common smoke template uses:
```bash
expect_field() {
  val=$(curl -sS "$url" | python3 -c "import sys,json;d=json.load(sys.stdin);print(d.get(\"$field\",\"\"))" 2>/dev/null || true)
  if [[ -z "$val" ]]; then echo FAIL; fi
}
```
…where the inner `"$field"` interpolation gets eaten by bash subshell escaping and the field name arrives as the literal string `"field"` or empty. Symptom: every field check fails even though `curl … | jq` shows the value clearly. Fix: switch to substring probing with `grep -F` (no regex, no escaping):
```bash
expect_substr() {
  local name="$1" url="$2" needle="$3"
  body=$(curl -sS -m 5 "$url" || true)
  if printf '%s' "$body" | grep -qF "$needle"; then echo "OK   $name has '$needle'"; else echo "FAIL $name missing '$needle'"; fi
}
expect_substr meta_tz  "$BASE/api/meta" '"timezone":"Asia/Dhaka"'
expect_substr sess_win "$BASE/api/sessions/dashboard?days=7" '"window_label"'
```
A reusable smoke template lives at `scripts/dashboard-smoke.sh`.

## Deploy pitfall (self-hosted Docker dashboards)
- Host-mounted `./static` updates CSS/JS immediately.
- App code `COPY`’d into the image does **not** update until rebuild **or** bind-mount of `app.py` / module `.py` files.
- Symptom: UI looks fixed but `/api/meta`, timezone labels, or window math stay old. Fix mounts or rebuild, then recreate container and re-smoke.
- Details: `dashboard-ui-operations` → `references/static-mount-vs-baked-python.md`

## Cmd-K palette (the highest-impact "feel premium" move)

For any dense dashboard with 10+ peer pages, a Cmd-K palette is the single
highest-impact feature you can ship. Pattern: own file `static/js/cmd-k.js`,
own modal markup in `index.html`, own CSS. Verified working end-to-end.

Loading order: `core.js` → `search-ui.js` → `cmd-k.js` → `theme.js` → `dashboard.js`.

**Full code, modal HTML, CSS, and live verification** (how to drive the modal
via `browser_press('Meta+k')` and confirm via `browser_console`):
see `references/cmdk-palette-and-inline-sparks.md`.

Triggers: ⌘K / Ctrl+K, or `/`. Keyboard: ↑↓ navigate, Enter select, Esc close.
Include a visible trigger button in the nav header — users won't find
keyboard-only features without it.

## Inline SVG sparklines (no Chart.js)

For hero KPI tiles, a 26px SVG sparkline gives trend context without Chart.js
overhead, race conditions during paintHome rebuilds, or a second canvas. ~50
LOC, drop-in. CSS: `.kpi-spark { display:block; width:100%; height:26px; margin-top:6px }`.

Helper signature, heroHtml builder wiring, and the live verification probe
(`document.querySelector('#homeSummary .kpi-hero .kpi-spark polyline')`) all
in `references/cmdk-palette-and-inline-sparks.md`.

**Verify a sparkline is rendering real data, not a flat line.** A flat line
usually means the field name was wrong. Check the API directly.

## Flat primary nav (when to drop "More ▾")

The original advice in this skill was "primary 6–8 tabs + More ▾ menu". That's
still right when the IA genuinely has primary/secondary tiers. But for ops
dashboards where Sessions, Requests, Messages, Models, Tools, Providers,
Channels are all peer-importance, "More ▾" is an IA smell — users will find
the hidden pages via Cmd-K anyway.

**Promote all to flat primary nav with horizontal scroll.** Pattern, HTML,
CSS in `references/cmdk-palette-and-inline-sparks.md`.

For >16 peer pages, the Cmd-K palette becomes the primary discovery
mechanism and the nav strip becomes the always-visible shortcut bar.

## Be honest about the ceiling

When the user asks to push to "10/10", check whether the remaining gap is:
- **Incremental CSS / polish / interactivity** → ship it.
- **Requires a real design system** (Figma → tokens, light theme done properly, icon library) → say so, score ~9.3 honestly.
- **Requires source-data cleanup** (sessions without titles, missing cost records) → not a UI problem, tell the user.

Realistic ceiling for a single-author, single-repo dashboard with no design
system: **~9.4**. Pushing past needs a dedicated design pass, not another CSS
edit. The user respects an honest ceiling more than a faked 10/10.

## Data-shape assumption trap

**Always curl the actual API and inspect field names before writing the
wiring code.** Common trap:

```js
// guessed (wrong)
var tokensSeries = tl7.map(function(x){
  return Number(x.input_tokens || 0) + Number(x.output_tokens || 0);
});
// actual API returns
// [{day, sessions, tokens, cost}]   // single `tokens` field, single `cost` field
```

Symptom: sparkline renders flat-zero line because every series point is 0,
and there is no error — just visually wrong.

Fix: before writing series extraction,
```bash
curl -sS "http://localhost:8866/api/home/dashboard?days=7&fresh=1" \
  | python3 -c 'import sys,json;d=json.load(sys.stdin); print(list((d.get("timeline") or [{}])[0].keys()))'
```
Then write the JS against the actual keys. Especially watch for:
`input_tokens` vs `tokens`, `cost_usd` vs `cost`, `latency_ms` vs `latency`.

## Python heredoc + JS arrow function pitfall

When patching JS via `execute_code` and the JS source contains `=>`
(arrow functions), Python's heredoc will choke:
```python
src = """
return (d.timeline || []).slice(-7).map(x => Number(x[f] || 0));
"""
# SyntaxError: invalid syntax on the => token even though the JS itself is fine
```

Fix: don't use Python heredocs for JS source. Use one of:
- `write_file(path, content)` with the raw JS string
- `patch(mode='replace', old_string=..., new_string=...)` for surgical edits
- Shell `cat > file <<'EOF'` (single-quoted heredoc → no shell interpolation → JS stays intact)

When you must use `execute_code`, write the JS to a temp file via Python's
`open()` and verify with `terminal(command='node --check <tmpfile>')`.

## Notes
This overlaps with `dashboard-ui-polish` and `dashboard-ui-operations`. Prefer this skill for operator analytics finishing; use operations skill for reverse-proxy / mount / privileged-API deploy traps. Curator may consolidate later.

## Subagent file-edit awareness
When a sibling subagent edits the same file you are patching (e.g. `dashboard.js`), `patch` will warn `"the file was modified since you last read it"` and may fail. Pattern: re-read the file before re-attempting. If a patch silently succeeded but the change seems lost, check the patch's diff output — your `old_string` may have been matched against an older buffer the system rewinds.
