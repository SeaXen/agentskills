# Compact dark dashboard CSS — user preference

User (Dr. Sagar) prefers **compact, dense, bright** dashboards. When he says cards are too big or text is too dim, apply these defaults. He will push for **even tighter** on each iteration — start from the tight end, not the spacious end.

IMPORTANT: Text must NOT be too small. User explicitly complained 13px was "so small" and asked for OmniRoute-sized text. Start at **15px**, not 13px.

## Spacing (compact — use these as starting point)
- Card padding: `14px 16px` (user rejected 24px)
- Stat card padding: `10px 6px` (user rejected 28px, then 14px)
- Section gaps: `8-12px` (user rejected 28px, then 16px)
- Chart heights: `150-200px` (user rejected 280px)
- Font base: **`15px`** (user rejected 13px as "too small"; OmniRoute reference is 16px)
- Stat value size: `1.5-1.6rem` (user rejected 2rem)
- Table cell padding: `7-8px 12px` (user rejected 12px padding, but wants text readable)
- Overview grid: fixed `repeat(5,1fr)` not `minmax(200px,1fr)`
- Header padding: `8px 0` (user complained "header still big" at larger sizes)
- Header logo: `26-28px` (not 42px)
- Sticky header: use `position:sticky;top:0;z-index:100` for scroll context

## Text brightness
- Main text: `#f1f5f9` (bright white, not `#e2e8f0`)
- Muted text: `#94a3b8` (visible, not `#64748b` which is too dim)
- Table headers: use **accent color** (`#ffac02`) not gray
- Provider/data names: `color:#fff;font-weight:600` for readability
- Section headers (`h2`): use accent color, not plain gray
- Code/numeric values: use **IBM Plex Mono** (`font-family: var(--font-mono)`)
- Add subtle glow underline under h2:
  ```css
  h2::after { content:''; display:block; height:1px; margin-top:3px;
              background: linear-gradient(90deg, var(--accent), transparent); opacity:.2; }
  ```

## Glow effects on values
- Stat values get text-shadow glow matching their color:
  ```css
  .stat-value.accent { color: var(--accent); text-shadow: 0 0 20px var(--accent-glow); }
  ```
- Status dots get glow: `box-shadow: 0 0 6px rgba(74,222,128,.5);`

## CSS Variable Theme System Pattern
When user wants multiple themes (e.g., "add Tinybird style theme with switch"):

1. **Separate CSS files per theme** — `static/themes/default.css`, `static/themes/tinybird.css`
2. **Each file defines `:root` or `[data-theme="name"]` variables** — ALL colors, spacing, radii, font sizes as CSS variables
3. **Theme manager JS** — `static/js/theme.js` with `localStorage` persistence
4. **Main HTML uses `var()` everywhere** — no hardcoded colors in the main stylesheet
5. **Charts use `cv()` helper** to read computed CSS variables at render time:
   ```js
   function cv(name) { return getComputedStyle(document.documentElement).getPropertyValue(name).trim(); }
   ```
6. **Theme selector** — `<select>` dropdown in header with `onchange="ThemeManager.setTheme(this.value)"`
7. **Theme CSS overrides via `[data-theme]` attribute** on `<html>`:
   ```css
   [data-theme="tinybird"] { --accent: #27C486; --bg: #1A1A2E; ... }
   ```
8. **Chart refresh on theme switch** — call `refreshAll()` after theme change so charts pick up new colors
9. **localStorage key**: `aceroute-theme` (or `<appname>-theme`)

### Tinybird theme reference colors
```css
[data-theme="tinybird"] {
  --bg: #1A1A2E; --card: #292942; --card-border: #40405C;
  --accent: #27C486; --accent-bright: #3DD99A;
  --red: #FF5757; --orange: #F5C518;
  --text: #E8E8F0; --muted: #A1A1B5; --dim: #5E5E7A;
}
```

## Cost display pattern
- `$0.00` in green (`.cost-zero { color: var(--green); font-weight: 600 }`)
- Paid amounts in accent (`.cost-paid { color: var(--accent); font-weight: 600 }`)
- **Always respect free tiers** — don't show cost when usage is within free monthly limit

## Analytics: free-tier-aware cost calculation
When building analytics dashboards that show per-provider costs:
```python
# Count monthly usage per provider
monthly_counts = Counter(l["provider"] for l in logs if l["timestamp"][:7] == current_month)

for provider in providers:
    free_tier = cost_info.get("free_monthly", 0)
    monthly_used = monthly_counts.get(provider, 0)
    billable = max(0, monthly_used - free_tier)
    if monthly_used > 0 and billable > 0:
        cost = searches * (billable / monthly_used) * cost_per_query
    else:
        cost = 0.0
```
Apply this in ALL cost display paths: overview, provider table, cost breakdown, daily chart.

## Provider badge colors (per-provider distinct colors)
- searxng → green, tavily → purple, brave → orange, exa → cyan, serper → blue

## Badges
- Always uppercase, font-size `.55-.6rem`, font-weight 700
- `border-radius: 4px` (not 20px pill — Tinybird style uses square badges)
- Add `.badge-purple` and `.badge-cyan` variants for provider variety

## Logo/favicon pattern
- User will supply a logo image — convert it to multiple sizes (16/32/48/192px PNG + ICO)
- Use the real logo in: favicon, header icon, apple-touch-icon
- Serve via `/static/icons/` with a direct `/favicon.ico` root route in FastAPI
- Header uses 26-28px logo img tag, not a text/emoji placeholder

## Iteration lesson
User corrects in 2-3 passes: first "too big / too dim", then "still big", then "text too small". The text-size correction is critical — do NOT start below 15px even if compact references suggest smaller.

## Two-row page header (toolbar vs stats)
When the user says **stats on a separate line** and **title card above in one line**, use **two sibling blocks** — not one hero mixing title, KPIs, and controls.

- Row 1: slim toolbar card — title, `sync <short time>`, window, icon actions, chips.
- Row 2: stats grid only (`tools-stats-row`, six `mini-stat` cards).

Do not re-merge after a correction. Drop duplicate summary prose under the bar. Markup/CSS: `references/two-row-toolbar-and-stats-strip.md`.

## Analytics tabs (Sessions / Models): chips on same line as toolbar
When the user wants the **title card on one line** (not chips wrapping to a second row), put provider/source chips **inside** `sessions-bar-row` with horizontal scroll. Stats stay in a **separate** `tools-stats-row` (8 columns). Detail: `references/analytics-toolbar-one-line.md`.
