---
name: web-responsive-mobile-desktop-separation
description: "Build or modify responsive web UIs by rendering BOTH mobile and desktop layouts in the same HTML and toggling via CSS visibility classes, with completely separate code paths so mobile-only changes never touch desktop CSS. Use when the user asks for mobile-only fixes, complains that a desktop change was made when they wanted mobile-only, wants a separate mobile layout, wants edge-to-edge mobile content, or wants compact mobile header/footer. Captures the explicit 'do not touch desktop code' workflow the user repeats."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [responsive, mobile, desktop, css, media-queries, web, ui, dual-rendering]
    related_skills: [devops/dashboard-ui-polish, creative/design-systems, devops/static-spa-library-site]
---

# Web Responsive: Separate Mobile & Desktop Code Paths

Use when the user wants a mobile-only or desktop-only change and has been burned by previous attempts that over-extended to the other viewport. For Dr. Sagar specifically, this is a recurring workflow preference — read the **User signals** section before touching anything.

## User signals (these all mean: do the change ONLY for the requested viewport)

- "make this only for mobile"
- "make it for mobile only, do not change desktop"
- "do not touch/change desktop code"
- "make separate code for mobile"
- "desktop is fine, fix mobile"
- "mobile is fine, fix desktop"
- "why did you change the desktop version"
- "wth hack you doo" / "I told you only for mobile"
- Repeated corrections about a viewport they did NOT ask to change

**Default assumption when the user says "for mobile":** they mean ONLY for `≤900px`. Touching desktop CSS / HTML structure is a hard failure for this user.

## Core pattern: render BOTH, toggle via CSS

For pages where mobile and desktop layouts diverge significantly (chapter pages with sidebar+main vs accordion tree, dashboards with dense tables vs mobile cards, multi-pane editors vs stacked panes), render both layouts in the same HTML and use visibility classes to toggle.

### HTML template

```html
<style>
  /* Desktop default */
  .d-only { display: block; }
  .m-only { display: none; }

  /* Mobile: flip them */
  @media (max-width: 900px) {
    .d-only { display: none !important; }
    .m-only { display: block !important; }
  }
</style>

<body>
  <!-- Desktop layout -->
  <div class="d-only">
    <aside class="desktop-sidebar"> ... </aside>
    <main class="desktop-main"> ... </main>
  </div>

  <!-- Mobile layout (hidden by default) -->
  <div class="m-only">
    <header class="mobile-bar"> ... </header>
    <div class="mobile-content"> ... </div>
  </div>
</body>
```

### Why this works for Dr. Sagar

- **Mobile-only edits never touch desktop CSS.** You only modify rules inside `@media (max-width: 900px) { ... }`. If the desktop file changed, you made a mistake.
- **Desktop-only edits never touch mobile CSS.** Rules outside the `@media` block.
- **Single source of HTML.** Both layouts share data from the same render. No duplicate content.
- **Visibility toggle is predictable.** A future agent can grep for `d-only` / `m-only` and reason about which layout is which.

## Step-by-step: "make X only for mobile"

1. **Read the user's complaint literally.** If they say "header is too big", they mean the mobile header. Do NOT redesign the desktop header.
2. **Locate the existing mobile CSS.** Grep for `@media (max-width:`, `.mobile-`, `m-only`, etc. There is almost always a mobile block already.
3. **Edit ONLY inside the mobile `@media` block.** Add new rules or override existing ones with higher specificity.
4. **Verify with forced-mobile CSS injection** (see Verification below) before reporting success.
5. **Verify desktop is unchanged** at the default viewport width (1280px).

## Page-scoped mobile overlays for one problematic page

When only one page's mobile layout is bad but the rest of the app's mobile header/tabs are acceptable, do **not** widen the fix to the whole site. Use a page-scoped selector inside the mobile media query, for example:

```css
@media (max-width: 700px) {
  body:has(.settings-page) .sticky-actions { position: static !important; top: auto !important; }
  body:has(.settings-page) .page-tab { width: 34px !important; height: 34px !important; padding: 0 !important; }
}
```

This pattern was the safe fix for Systor's mobile Settings page: compact the toolbar and tab chrome for Settings only while leaving Dashboard/Apps/Speed mobile headers untouched.


### 1. Compact single-row mobile header (the most common mobile complaint)

User's literal complaint: "mobile header is big and takes much space". Mobile headers frequently balloon to 100–140px when they stack logo/menu/search/chapter-label/github into vertical rows.

**Important refinement for dashboard-style headers with multiple controls:** a simple wrapped flex row is often still too tall on phones and can consume half the screen. For this user, prefer a **mobile-only grid header** instead of flex-wrap:

- row 1: centered compact logo/app name
- row 2: full-width date/filter strip (or the densest control row)
- row 3: 3 equal action cells (e.g. export / theme / refresh)

Pattern:

```css
@media (max-width: 768px) {
  header {
    flex-direction: column !important;
    height: auto !important;
    padding: 6px 8px !important;
    gap: 4px !important;
  }

  .logo-area {
    width: 100%;
    justify-content: center;
    gap: 6px;
  }
  .logo-area img { width: 20px; height: 20px; }
  .logo-area h1 { font-size: .92rem; line-height: 1; }

  .header-right {
    width: 100% !important;
    display: grid !important;
    grid-template-columns: 1fr 1fr 1fr !important;
    gap: 4px !important;
    align-items: center;
  }

  .date-range {
    grid-column: 1 / -1;
    display: grid !important;
    grid-template-columns: 34px 1fr 24px 34px 1fr 28px;
    gap: 4px;
    align-items: center;
  }
}
```

This is a better fit than generic flex-wrap when the user says the header still "takes half of screen" after an initial mobile pass.

First-pass fix for simpler headers: collapse stacked `<div class="row">` wrappers into a single flex row using `display: contents`:

```css
@media (max-width: 900px) {
  .mobile-bar {
    flex-direction: row;          /* override default column */
    align-items: center;
    padding: 6px 8px;
    gap: 4px;
  }
  .mobile-bar .row.top { display: contents; }       /* flatten stacked rows */
  .mobile-bar .row.search-row { display: contents; }
  .mobile-bar .search-row { flex: 1; min-width: 0; }
}
```

Result when it works: ~140px tall header → ~45px tall header.

### 1b. If the user says "make header in 1 line" and search still wraps or gets clipped

Do **not** keep squeezing every control into the row. On narrow phones, the reliable fix is to preserve only the critical controls and hide the rest.

For this user, the correct priority is usually:
- keep: menu button, small logo/icon, search box
- hide: GitHub button, chapter label text, logo text, stats pills

```css
@media (max-width: 900px) {
  .mobile-bar {
    flex-direction: row;
    align-items: center;
    flex-wrap: nowrap;
    gap: 6px;
  }
  .mobile-bar .row.top,
  .mobile-bar .row.search-row { display: contents; }

  .mobile-bar .logo-mini a,
  .mobile-bar .current-ch-label,
  .mobile-bar .github-btn,
  .mobile-bar .stats-mini {
    display: none !important;
  }

  .mobile-bar .menu-btn { flex: 0 0 auto; }
  .mobile-bar .search-row,
  .mobile-bar .search-row .search-box-m {
    flex: 1 1 auto;
    min-width: 0;
    width: 100%;
  }
  .mobile-bar .search-row input { width: 100%; }
}
```

This is the safe "strict single-line header" pattern for MedSea-style dense mobile bars: icon + menu + search on one row, everything else hidden.

### 2. Edge-to-edge content (no wasted horizontal padding)

User's literal complaint: "notes are on middle small are many space are on left and right on mobile so note cannot see clearly".

Fix: zero out horizontal padding everywhere on mobile, and let the page chrome own its own background:

```css
@media (max-width: 900px) {
  .chapter-page { padding: 4px 0 60px !important; }
  .hub-acc, .hub-summary, .topic-acc, .topic-summary, .topic-body {
    border-radius: 0 !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
  }
}
```

### 3. Hide duplicate UI

If you have both a global search bar (in `.mobile-bar`) and a page-local search (in `.chapter-toolbar`), hide the duplicate on mobile rather than removing it from HTML:

```css
@media (max-width: 900px) {
  .chapter-toolbar { display: none !important; }
}
```

Removing HTML blocks desktop too. Hiding via CSS is the right answer.

### 4. Full-bleed code blocks / blockquotes / images

Use negative margins equal to the body padding to extend code, quotes, and images to screen edges:

```css
@media (max-width: 900px) {
  .topic-body { padding: 12px 14px 18px; }
  .topic-content pre,
  .topic-content blockquote,
  .topic-content img {
    margin-left: -14px !important;
    margin-right: -14px !important;
    border-radius: 0 !important;
    max-width: calc(100% + 28px) !important;
  }
}
```

### 5. Tiny phones (≤380px)

Hide non-essential labels to keep critical controls visible:

```css
@media (max-width: 380px) {
  .mobile-bar .logo-mini a { display: none; }    /* show only ⚕ icon */
  .mobile-bar .current-ch-label { display: none; }
  .mobile-bar .stats-mini { display: none; }
}
```

## Pattern: separate CSS file with media query link

### For dense analytics dashboards: do NOT leave responsive grid counts inside inline JS/HTML strings

A recurring failure mode in single-file dashboards is that desktop-sized inline grids survive on mobile even after adding a separate `mobile.css`, because the grid is emitted by JavaScript as inline HTML such as:

```js
statsDiv.innerHTML = '<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:8px">' + ...
```

Those inline `grid-template-columns` values bypass the clean mobile stylesheet separation and cause exactly the user's complaint: some cards huge, some tiny, some overflowing. The fix is:

1. replace inline grid style strings with semantic classes like `.extract-stats-grid` / `.hermes-stats-grid`
2. define the mobile column counts only in `mobile.css`
3. keep desktop styling in the default stylesheet / inline desktop CSS

Example:

```js
statsDiv.innerHTML = '<div class="extract-stats-grid">' + ...
```

```css
@media (max-width: 768px) {
  .extract-stats-grid,
  .hermes-stats-grid {
    display: grid;
    grid-template-columns: 1fr 1fr !important;
    gap: 6px !important;
  }
}
```

Also apply the same rule to summary/stat cards: on small phones, keep them 2-up and reduce padding/font size rather than switching to oversized 1-column blocks unless readability truly fails.


For monolithic single-file dashboards (SPA in index.html), the cleanest separation is a **separate CSS file** loaded with a media-conditional `<link>`:

```html
<link rel="stylesheet" href="/static/css/mobile.css" media="(max-width:1024px)">
```

This keeps mobile styles completely isolated — zero bytes of mobile CSS load on desktop. No `!important` wars, no specificity conflicts.

### Implementation
1. Create `/static/css/mobile.css` with all `@media(max-width:*)` rules
2. Remove inline responsive CSS from `<style>` block in index.html
3. Add the `<link media="...">` tag in `<head>`
4. Desktop CSS is untouched — mobile file is loaded conditionally
5. If JS renders mobile-sensitive stat grids inline, move those grids to named classes (`.extract-stats-grid`, `.hermes-stats-grid`, etc.) so the mobile stylesheet can control them cleanly
6. For compact dashboard mobile headers/stat rows, see `references/mobile-dashboard-compact-header-and-stats.md`

### When to use this vs d-only/m-only classes
- **Separate CSS file**: When mobile and desktop share the same HTML structure but need different sizing/spacing/layout
- **d-only/m-only classes**: When mobile needs completely different DOM structure (hidden sidebar, stacked vs grid)

### Three breakpoints recommended
```css
@media(max-width:1024px) { /* tablet: 3-col grids */ }
@media(max-width:768px)  { /* mobile: stacked header, 2-col */ }
@media(max-width:480px)  { /* small phones: ultra-compact */ }
```

## Verification (required before reporting success)

The user verifies UI fixes in the browser themselves. Your verification must use the same browser/console approach so they can trust your "done" report.

### Local/LAN first when judging visual truth

When the user is fixing a self-hosted dashboard and says to use localhost or LAN, obey that literally. Verify the rendered UI on `127.0.0.1` or the LAN IP before trusting the public tunnel/domain. Tunnel/proxy/cached public paths can lag behind and create false positives or false negatives.

Practical rule:
- use `http://127.0.0.1:<port>/...` or the LAN IP for visual QA
- only check the public URL after the localhost/LAN result is already correct
- if localhost looks right but the phone/public page still looks old, suspect cache or proxy lag before changing layout again

### Cache-busting is part of the fix, not an afterthought

For CSS-driven mobile fixes on self-hosted dashboards, changing the stylesheet content is often insufficient because the user's phone/browser may still hold the old asset. If the fix is in CSS, bump the stylesheet version/query string or another explicit cache key as part of the same change.

Practical rule:
- patch CSS
- rebuild/minify if applicable
- bump the served CSS version (for example `style.min.css?v=1.8`)
- then verify the browser is loading the new asset URL before trusting the result

Without this, you can think the fix shipped while the user still sees the stale mobile layout.

For single-file static pages where CSS lives inline in `index.html`, the same lesson still applies in practice: after copying the new HTML live, verify with a cache-busting query parameter (for example `?v=2`) or force-refresh the phone before deciding the fix failed.

### 1. Verify mobile styles are loaded in CSS

```bash
curl -s http://localhost:PORT/page/ | grep -A2 "MOBILE BAR\|EDGE-TO-EDGE\|HIDE DUPLICATE"
```

New CSS rules must appear in the rendered HTML.

### 2. Force mobile layout in browser (since desktop browser viewport can't be resized from JS)

```js
// Inject CSS that mimics the mobile media query
const css = `
  /* Mirrors @media (max-width: 900px) rules */
  .d-only { display: none !important; }
  .m-only { display: block !important; }
  /* ... all the new mobile rules ... */
`;
const style = document.createElement('style');
style.textContent = css;
document.head.appendChild(style);

// Override matchMedia so JS that checks viewport width thinks it's mobile
const orig = window.matchMedia;
window.matchMedia = function(q) {
  if (q === '(max-width: 900px)') return { matches: true, media: q, addListener: () => {}, removeListener: () => {} };
  return orig.call(window, q);
};
```

### 3. Probe live DOM for the fix

```js
// Verify mobile bar height is now compact (was 140px, should be ~45px)
const bar = document.querySelector('.mobile-bar');
const barRect = bar.getBoundingClientRect();
console.log(bar.offsetHeight);  // expect ~45

// Verify chapter page has no horizontal padding
const page = document.querySelector('.chapter-page');
console.log(getComputedStyle(page).padding);  // expect "4px 0px 60px"

// Verify duplicate search is hidden
console.log(getComputedStyle(document.querySelector('.chapter-toolbar')).display);  // expect "none"
```

### 4. Verify desktop is unchanged

At 1280px viewport (default browser width):
- Desktop header still visible
- Desktop sidebar+main still rendered
- New mobile rules must NOT apply (`getComputedStyle` returns default values)

### 5. Never claim success from "build succeeded" alone

For this user, "build succeeded" without a live DOM probe showing the fix is in place is a failed task. Always end with concrete measurements (height, padding, computed display value).

## Failure mode to check first on self-hosted mobile chapter pages

If the phone shows **blank body + footer only**, inspect the shipped HTML before changing CSS again.

Common root cause:
- CSS hides desktop markup on mobile (`.d-only`, `header.site`)
- but the generated HTML does **not** actually include the expected mobile-only DOM (`.chapter-mobile`, `.mobile-bar`)
- result: mobile hides the only real content and the user sees a large blank area with just the footer

Fast check:
1. Read the served chapter HTML, not just source templates.
2. Count whether `.chapter-mobile` / `.mobile-bar` markup exists.
3. If absent, do **not** hide desktop markup on mobile. Use a stacked desktop fallback instead:
   - keep `.d-only` visible on mobile
   - keep `header.site` visible and compact it
   - set sidebar/main to block layout with static positioning
4. Only use the separate mobile path when the mobile DOM is genuinely present in the shipped page.

## Cache reality on phone/LAN/Tailscale

When the user says the bug still reproduces on **LAN/Tailscale/local**, treat that as strong evidence against "public proxy lag" and inspect asset caching next.

Important pattern for self-hosted chapter pages:
- a service worker with cache-first CSS/JS can keep serving the old broken stylesheet even after the live file was fixed
- bumping the SW version alone may not rescue the current tab immediately
- safest hotfix is to change the chapter HTML asset URLs too, e.g. `chapter.css?v=mobilefix3` and `chapter.js?v=mobilefix3`
- for future resilience, prefer **network-first** for CSS/JS/JSON and cache-first only for heavier static images/icons

Verification order when the phone still looks wrong:
1. Verify localhost/LAN/Tailscale first.
2. Inspect served HTML for versioned asset URLs.
3. Inspect served `sw.js` for cache version and caching policy.
4. If needed, force a query-string asset bust in the HTML itself.
5. Only then ask the user to reopen a fresh tab or clear site data.

## Anti-patterns

- **Don't rewrite the whole HTML structure for mobile-only changes.** Use `display: none / block` and `m-only`/`d-only` classes. If you find yourself rewriting `write_chapter_spa()` for a "mobile-only" request, stop — you are about to touch the desktop layout.
- **Don't put mobile rules outside `@media`.** Always scope. Future maintainers need to find the mobile rules in one obvious place.
- **Don't ship without forcing mobile styles and probing the DOM.** The user will test in the browser and notice if it didn't actually apply.
- **Don't use `transform: translateX()` or other tricks to hide content that should actually be display:none.** Hidden-but-rendered elements still take paint/layout cycles on weak phones.
- **Don't remove HTML blocks for mobile-only concerns.** Hide via CSS so desktop still has them. Removing HTML is a structural change that bleeds across viewports.

## Verification probes cheat sheet

| Want to verify | Probe |
|---|---|
| Mobile bar compactness | `document.querySelector('.mobile-bar').offsetHeight` (~45px) |
| Edge-to-edge content | `getComputedStyle(document.querySelector('.chapter-page')).padding` (no horizontal) |
| Duplicate hidden | `getComputedStyle(document.querySelector('.duplicate')).display` ('none') |
| Visibility toggle works | `.d-only` display = 'none', `.m-only` display = 'block' on mobile |
| Topic content readability | `getComputedStyle(content).fontSize` (≥14px on mobile) |
| Layout responsiveness | Resize window and re-probe; matchMedia returns true/false correctly |

## References

- `references/mobile-css-patterns.md` — concrete CSS recipes for compact header, edge-to-edge content, full-bleed code blocks, table horizontal scroll, tiny-phone breakpoints.
- `references/forced-mobile-verification.md` — the JS snippet to force mobile layout in a desktop browser for live DOM probing.
