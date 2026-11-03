# Mobile CSS Patterns — Concrete Recipes

Battle-tested CSS patterns from real mobile-only fixes. Each recipe lists the user's complaint, the exact CSS that fixed it, and the verification probe.

## Recipe 1: Compact single-row mobile header from stacked rows

**User complaint (verbatim):** "mobile header is big and take much space"

**Before:** 3 stacked rows in `.mobile-bar` (logo+menu / search / chapter+github) = ~140px tall.

**HTML structure (do NOT change):**
```html
<div class="mobile-bar">
  <div class="row top">
    <div class="logo-mini">⚕ MedSea</div>
    <button class="menu-btn">☰ Chapters</button>
  </div>
  <div class="row search-row">
    <input type="text" placeholder="Search...">
  </div>
  <div class="row">
    <span class="current-ch-label">Cardiology</span>
    <a class="github-btn">GitHub</a>
  </div>
</div>
```

**CSS fix (add to mobile `@media` block):**
```css
@media (max-width: 900px) {
  .mobile-bar {
    padding: 6px 8px;
    gap: 4px;
    flex-direction: row;       /* override default column */
    align-items: center;
  }
  .mobile-bar .row.top,
  .mobile-bar .row.search-row { display: contents; }

  .mobile-bar .logo-mini { font-size: 13px; flex: 0 0 auto; }
  .mobile-bar .menu-btn { padding: 6px 8px; font-size: 12px; }
  .mobile-bar .search-row { flex: 1; min-width: 0; }
  .mobile-bar .search-row input { padding: 6px 10px 6px 28px; font-size: 12px; }
  .mobile-bar .current-ch-label { font-size: 10px; flex: 0 0 auto; white-space: nowrap; }
  .mobile-bar .github-btn { padding: 6px 8px; font-size: 11px; }
}
```

**Result:** ~140px → ~45px tall. All elements share one flex line.

**Verify:** `document.querySelector('.mobile-bar').offsetHeight` should be ~45px (was ~140).

**Key technique:** `display: contents` flattens intermediate `<div class="row">` wrappers so their children become direct flex items of `.mobile-bar`.

---

## Recipe 2: Edge-to-edge content (zero horizontal padding)

**User complaint:** "notes are on middle small are many space are on left and right on mobile"

**CSS fix:**
```css
@media (max-width: 900px) {
  .chapter-page {
    padding: 4px 0 60px !important;   /* no horizontal */
    min-height: auto !important;
  }
  .hub-accordion { gap: 4px !important; }
  .hub-acc, .hub-acc[open],
  .hub-summary, .topic-acc, .topic-summary, .topic-body {
    border-radius: 0 !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
  }
}
```

**Verify:** `getComputedStyle(document.querySelector('.chapter-page')).padding` returns `"4px 0px 60px"`.

---

## Recipe 3: Hide duplicate search/toolbar

When `.mobile-bar` already has a search and a page-level `.chapter-toolbar` also has one:

```css
@media (max-width: 900px) {
  .chapter-mobile .chapter-toolbar { display: none !important; }
}
```

**Why `!important`:** toolbar's own CSS may use `display: flex`. Be defensive.

**Verify:** `getComputedStyle(document.querySelector('.chapter-mobile .chapter-toolbar')).display` returns `"none"`.

---

## Recipe 4: Full-bleed code blocks, blockquotes, images

When `.topic-body` has `padding: 12px 14px`, code blocks look inset. To extend them to screen edges:

```css
@media (max-width: 900px) {
  .topic-body { padding: 12px 14px 18px; }
  .topic-content pre,
  .topic-content blockquote,
  .topic-content img,
  .topic-image-toggle {
    margin-left: -14px !important;
    margin-right: -14px !important;
    border-radius: 0 !important;
    max-width: calc(100% + 28px) !important;
  }
}
```

The negative margin (`-14px`) cancels the parent `.topic-body` padding (`14px`). For tables:

```css
.topic-content table {
  display: block;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}
```

---

## Recipe 5: Tiny phone breakpoints (≤380px)

```css
@media (max-width: 380px) {
  .mobile-bar .logo-mini a { display: none; }      /* keep only ⚕ icon */
  .mobile-bar .current-ch-label { display: none; }
  .mobile-bar .stats-mini { display: none; }
  .chapters-grid { grid-template-columns: repeat(2, 1fr); gap: 6px; }
}
```

---

## Recipe 6: Mobile-readable font sizes

User said mobile content was "hard to read". Don't shrink fonts on mobile — increase them:

```css
@media (max-width: 900px) {
  .topic-content { font-size: 14px !important; line-height: 1.6 !important; }
  .topic-content h1 { font-size: 19px !important; }
  .topic-content h2 { font-size: 17px !important; padding-left: 8px; }
  .topic-content h3 { font-size: 15px !important; }
  .topic-content pre { font-size: 11px !important; }   /* code stays compact */
  .topic-content table { font-size: 12px !important; }
}
```

**Rule of thumb for mobile:**
- Body text: 14–16px (was 13px on desktop sometimes — go UP not down on mobile)
- H1: 19–22px
- H2: 17–19px
- Code: 11–12px (keep compact; long lines need to fit)

---

## Recipe 7: Hide desktop elements via the same visibility classes

Use `.d-only` / `.m-only` consistently:

```css
/* Default (desktop) */
.d-only { display: block; }
.m-only { display: none; }

/* Mobile: flip them */
@media (max-width: 900px) {
  .d-only { display: none !important; }
  .m-only { display: block !important; }
}
```

Then in HTML:
```html
<aside class="chapter-sidebar d-only">...</aside>      <!-- desktop only -->
<section class="chapter-main d-only">...</section>      <!-- desktop only -->
<div class="chapter-mobile m-only">...</div>            <!-- mobile only -->
```

`!important` is needed because other CSS may set `display: grid` / `display: flex` on these elements.

---

## Recipe 8: Force mobile layout in browser for testing

Can't resize browser window from JS. Use CSS injection + matchMedia override:

```js
// Step 1: inject CSS that mirrors mobile media query
const mobileRules = `
  .d-only { display: none !important; }
  .m-only { display: block !important; }
  .mobile-bar { display: flex !important; flex-direction: row !important; }
  /* ... all other mobile overrides ... */
`;
const s = document.createElement('style');
s.textContent = mobileRules;
document.head.appendChild(s);

// Step 2: override matchMedia so JS that checks width thinks we're mobile
const orig = window.matchMedia;
window.matchMedia = function(q) {
  if (q === '(max-width: 900px)')
    return { matches: true, media: q, addListener: () => {}, removeListener: () => {} };
  return orig.call(window, q);
};

// Step 3: probe the DOM
console.log({
  mobileBarHeight: document.querySelector('.mobile-bar')?.offsetHeight,
  chapterPagePadding: getComputedStyle(document.querySelector('.chapter-page')).padding,
  duplicateHidden: getComputedStyle(document.querySelector('.chapter-toolbar')).display,
});
```

This lets you verify mobile CSS in a desktop browser without resizing.

---

## Recipe 9: Verify both viewports after a change

After editing mobile-only CSS, probe both viewports:

```js
// Desktop probe (no injection)
const desktopProbe = {
  sidebarVisible: getComputedStyle(document.querySelector('.chapter-sidebar')).display,
  mobileBarHidden: getComputedStyle(document.querySelector('.mobile-bar')).display,
};

// Mobile probe (after injecting mobile CSS)
const mobileProbe = {
  sidebarHidden: getComputedStyle(document.querySelector('.chapter-sidebar')).display,
  mobileBarVisible: getComputedStyle(document.querySelector('.mobile-bar')).display,
  mobileBarHeight: document.querySelector('.mobile-bar')?.offsetHeight,
  pagePadding: getComputedStyle(document.querySelector('.chapter-page')).padding,
  duplicateHidden: getComputedStyle(document.querySelector('.chapter-toolbar'))?.display,
};
```

If `desktopProbe` changes after your mobile edit, you touched desktop by mistake — revert.

---

## Recipe 10: Common mobile gotchas

| Gotcha | Fix |
|---|---|
| Mobile bar 3-row stack (140px) | `display: contents` on inner rows |
| Code block too narrow | Negative margin equal to parent padding |
| Tables overflow | `display: block; overflow-x: auto` |
| Images too small | `max-width: calc(100% + 28px); margin: 0 -14px` |
| Header/search takes 100px+ | Move search to dedicated row, logo+menu+chapter+github on one row |
| Topic list nested too deep | Flatten indentation on mobile (remove `margin-left`) |
| Font too small to read | 14px+ body, 17–19px headings on mobile |
| Section headers with border-radius waste space | `border-radius: 0` on mobile |
| Sidebar hover styles not touch-friendly | Replace hover with active/tap on mobile |

---

## End-to-end example: full mobile @media block

```css
@media (max-width: 900px) {
  /* Header */
  header.site { display: none; }
  .mobile-bar { display: flex; padding: 6px 8px; gap: 4px; flex-direction: row; align-items: center; }
  .mobile-bar .row.top, .mobile-bar .row.search-row { display: contents; }
  .mobile-bar .logo-mini { font-size: 13px; flex: 0 0 auto; }
  .mobile-bar .menu-btn { padding: 6px 8px; font-size: 12px; }
  .mobile-bar .search-row { flex: 1; min-width: 0; }
  .mobile-bar .search-row input { padding: 6px 10px 6px 28px; font-size: 12px; }
  .mobile-bar .current-ch-label { font-size: 10px; flex: 0 0 auto; white-space: nowrap; }
  .mobile-bar .github-btn { padding: 6px 8px; font-size: 11px; }
  .mobile-bar .stats-mini { display: none; }

  /* Layout visibility */
  .d-only { display: none !important; }
  .m-only { display: block !important; }

  /* Hide duplicate toolbar */
  .chapter-toolbar { display: none !important; }

  /* Edge-to-edge page */
  .chapter-page { padding: 4px 0 60px !important; min-height: auto !important; }
  .hub-accordion { gap: 4px !important; }
  .hub-acc, .hub-acc[open], .hub-summary,
  .topic-acc, .topic-summary, .topic-body {
    border-radius: 0 !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
  }
  .hub-summary { padding: 12px 12px !important; }
  .topic-summary { padding: 10px 12px !important; }
  .topic-body { padding: 12px 14px 18px !important; }

  /* Typography */
  .topic-content { font-size: 14px !important; line-height: 1.6 !important; }
  .topic-content h1 { font-size: 19px !important; }
  .topic-content h2 { font-size: 17px !important; padding-left: 8px; }
  .topic-content h3 { font-size: 15px !important; }
  .topic-content pre { font-size: 11px !important; }

  /* Full-bleed */
  .topic-content pre,
  .topic-content blockquote,
  .topic-content img,
  .topic-image-toggle {
    margin-left: -14px !important;
    margin-right: -14px !important;
    border-radius: 0 !important;
    max-width: calc(100% + 28px) !important;
  }

  /* Tables */
  .topic-content table { display: block; overflow-x: auto; }
}

@media (max-width: 380px) {
  .mobile-bar .logo-mini a { display: none; }
  .mobile-bar .current-ch-label { display: none; }
}
```
