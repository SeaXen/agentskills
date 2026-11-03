# Mobile responsive layout reference

Concrete implementation notes for adding a dedicated mobile-only layer to the static SPA library site without breaking desktop. Companion to the main SKILL.md "Mobile-first responsive layout with separate code paths" section.

## Why a separate layer instead of media queries on the desktop header

User explicitly asked: *"make separate code for mobile so that it not touch desktop for better arrangement"*.

Three approaches were tried in this session:

| Approach | Outcome | Why it failed |
|---|---|---|
| A. Add `flex-wrap: wrap` to desktop header, hide stats on mobile | Header became cramped, search moved out of line | User immediately complained ("better header") |
| B. Keep one header, reorder children at 900px | Search snapped off-center, dropdown leaked into wrong row | Layout was technically functional but visually wrong |
| C. **Two separate blocks: desktop `<header class="site">` + mobile `<div class="mobile-bar">`, swap via `display: none/flex`** | Clean desktop, clean mobile, user happy | Took more code but the two paths never compete |

The C-pattern is the right answer. It also enables the chapter dropdown to become a slide-in drawer on mobile (better UX than a 280px-wide dropdown next to a search input).

## Exact files changed in this session

`/mnt/tb/Sea-knowledge/#MedSea/scripts/site/build_site.py`:

1. **`PAGE_CSS` constant (CSS)** — added ~200 lines of dedicated mobile CSS at the end, before the existing `@media (max-width: 900px)` block. The new block declares `.mobile-bar { display: none; }` (default), then `@media (max-width: 900px) { header.site { display: none; } .mobile-bar { display: flex; } }`. The `@media (max-width: 550px) { .chapters-grid { grid-template-columns: 1fr; } }` rule was changed to `repeat(2, 1fr)` so phones stay 2-col.

2. **`page_header()` function (Python + HTML template)** — after `</header>`, added a `<div class="mobile-bar">` block (logo + chapters button + search row + chapter-label + github link row) and a `<div class="mobile-menu">` drawer (chapter list + close button). The mobile bar uses an `f-string` ternary to show current chapter label only when `current_ch_slug` is set. Required initializing `ch_display = ''` before the `if` block that assigns it (otherwise `ch_display` is unbound on the index page).

3. **JS script block** — added a second IIFE `Mobile search (separate code, doesn't touch desktop)` after the existing `Universal topic search` IIFE. First line is `if (!input) return;` to guard against pages where mobile HTML wasn't injected.

## Verification probes (browser_console)

When vision is unavailable (returns "Unknown Model" errors), use these DOM probes to verify the mobile layout works. Run them with the browser at default 1280px viewport.

**Desktop at default viewport (should be unchanged):**
```javascript
(() => {
  const mb = document.querySelector('.mobile-bar');
  const hdr = document.querySelector('header.site');
  const grid = document.querySelector('.chapters-grid');
  return JSON.stringify({
    mobile_bar_display: getComputedStyle(mb).display,    // expect "none"
    header_display:     getComputedStyle(hdr).display,   // expect "flex"
    grid_columns:       getComputedStyle(grid).gridTemplateColumns,
    mobile_search_present: !!document.getElementById('searchInputMobile'),
    mobile_menu_present:   !!document.getElementById('mobileMenu'),
  });
})()
```

**Force-mobile CSS injection:**
```javascript
(() => {
  const s = document.createElement('style');
  s.textContent = `
    @media (min-width: 1px) {
      header.site { display: none !important; }
      .mobile-bar { display: flex !important; }
      .chapters-grid { grid-template-columns: repeat(2, 1fr) !important; gap: 8px !important; }
    }`;
  document.head.appendChild(s);
  return 'injected';
})()
```

**After injection (should match the user's request):**
```javascript
(() => {
  const mb = document.querySelector('.mobile-bar');
  const grid = document.querySelector('.chapters-grid');
  const cards = grid.querySelectorAll('button, .ch-card, a.chapter-card');
  return JSON.stringify({
    mobile_bar_display: getComputedStyle(mb).display,      // expect "flex"
    mobile_bar_height:  mb.getBoundingClientRect().height, // expect ~144px sticky
    grid_columns:       getComputedStyle(grid).gridTemplateColumns, // "612px 612px" on 1280 viewport
    grid_gap:           getComputedStyle(grid).gap,         // expect "8px"
    card_count:         cards.length,                       // expect 32
  });
})()
```

**Open the mobile chapter drawer (tap simulation):**
```javascript
document.getElementById('mobileMenu').classList.add('open')
// then probe: getComputedStyle(document.getElementById('mobileMenu')).display  // expect "block"
// then click a chapter link: document.querySelector('.mobile-menu .item').click()
```

## Common pitfalls from this session

1. **Two `@media (max-width: 900px)` blocks survived in the file** — when I added the new mobile CSS, the OLD 900px rule (with `header.site { padding: 8px 16px; } header.site .header-inner { flex-wrap: wrap; }`) was still at the bottom of `PAGE_CSS`. CSS cascade applies both, with the later one winning on shared properties but neither fully wins. Fix: deleted the duplicate via `patch(replace)` with the unique signature of the old block as `old_string`. **After any CSS edit, run `grep -n '@media' build_site.py` and verify each breakpoint appears exactly once.**

2. **`f"{'' if x else '...'}"` ternary in template needs `ch_display` initialized** — I added `ch_display` to the mobile bar with `('<span class="current-ch-label">'+ch_display+'</span>' if current_ch_slug else '<span></span>')`. But `ch_display` was only assigned inside `if current_ch_slug and current_ch_slug in BUILT_CHAPTERS`, so on the index page (no `current_ch_slug`) the variable didn't exist. LSP flagged it. Fix: `ch_display = ''` initialization before the if block.

3. **`mobile_menu` `<div>` cannot use raw dropdown items without their own CSS** — the chapter dropdown HTML produced by `chapter_dropdown_html()` uses classes `item`, `item soon`, `num`, `name`, `badge`. The mobile drawer CSS needs to style these specifically under `.mobile-menu .panel a`, not the `.drop-menu` namespace used on desktop. Otherwise items render unstyled (white on white text, full-width).

4. **`<main>` tag was missing from the template after a header refactor** — easy to lose during edits. After every header change, `grep -c '<main>' site/index.html` should return ≥1 (typically exactly 1 on the landing page, plus 1 per chapter SPA).

5. **Docker build with 3.3GB site directory takes ~5 min** — `COPY site/ /usr/share/nginx/html/` is the bottleneck. Run with `background=true` + `notify_on_complete=true`, then continue other work. Don't poll.

## Iteration loop for layout fixes

User feedback pattern observed across multiple sessions:

1. User says "X is too big / cramped / wrong placement"
2. Open browser at default viewport (1280px), screenshot or DOM-probe the offending element
3. **Ask what "better" means in concrete dimensions**: gap = N px, columns = N, font = N px. Don't guess.
4. Edit CSS in the build script (NOT the generated HTML — it's regenerated)
5. Rebuild site, rebuild docker, restart container
6. Verify with browser_console probes — both desktop and mobile views
7. **Then** ask the user to verify visually — they have the actual phone

The "ask what better means in numbers" step is critical. "Better mobile header" can mean "more padding", "bigger touch targets", "fewer rows", "search at top instead of middle", or "remove stats pill". All are valid interpretations; only the user knows which.

## Reference

- SKILL.md "Mobile-first responsive layout with separate code paths" section — the canonical pattern
- `/mnt/tb/Sea-knowledge/#MedSea/scripts/site/build_site.py` — live implementation (search for `MOBILE-ONLY BAR`, `mobile-bar {`, `Mobile search`)
- `/mnt/tb/Sea-knowledge/#MedSea/site/index.html` — generated output (search for `mobile-bar`, `searchInputMobile`)
