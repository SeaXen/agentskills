# Forced Mobile Verification — Browser DOM Probes

When verifying mobile CSS in a desktop browser (which can't be resized via JS), use this pattern: inject CSS that mimics the mobile media query + override matchMedia + probe the live DOM.

## Why this exists

`window.resizeTo()` is blocked by modern browsers. CDP can resize but requires Playwright/Puppeteer. The cheapest path for live verification is to **fool the browser into thinking it's mobile** by:

1. Injecting CSS rules that mirror the `@media (max-width: 900px)` block (so visual styles apply)
2. Overriding `window.matchMedia` (so JS that checks viewport width thinks we're mobile)
3. Probing `getComputedStyle` and `getBoundingClientRect` on the live DOM

## Single-shot verification snippet

```js
// === Step 1: inject mobile CSS ===
const mobileCSS = `
  .d-only { display: none !important; }
  .m-only { display: block !important; }
  .mobile-bar { display: flex !important; padding: 6px 8px !important; flex-direction: row !important; }
  /* ...paste the full mobile @media block here... */
`;
const style = document.createElement('style');
style.id = 'force-mobile';
style.textContent = mobileCSS;
document.head.appendChild(style);

// === Step 2: override matchMedia ===
const origMM = window.matchMedia;
window.matchMedia = function(q) {
  if (q === '(max-width: 900px)') {
    return { matches: true, media: q, addListener: () => {}, removeListener: () => {} };
  }
  return origMM.call(window, q);
};

// === Step 3: probe the DOM ===
const result = {
  mobileBarHeight: document.querySelector('.mobile-bar')?.offsetHeight,
  mobileBarFlexDir: getComputedStyle(document.querySelector('.mobile-bar'))?.flexDirection,
  chapterPagePadding: getComputedStyle(document.querySelector('.chapter-page'))?.padding,
  sidebarHidden: getComputedStyle(document.querySelector('.chapter-sidebar'))?.display,
  mainHidden: getComputedStyle(document.querySelector('.chapter-main'))?.display,
  mobileVisible: getComputedStyle(document.querySelector('.chapter-mobile'))?.display,
  topicBodyPadding: getComputedStyle(document.querySelector('.topic-body'))?.padding,
  topicContentFontSize: getComputedStyle(document.querySelector('.topic-content'))?.fontSize,
  duplicateToolbarHidden: getComputedStyle(document.querySelector('.chapter-toolbar'))?.display,
};
console.log(JSON.stringify(result, null, 2));
```

Expected output for "compact header + edge-to-edge" fix:
```json
{
  "mobileBarHeight": 45,
  "mobileBarFlexDir": "row",
  "chapterPagePadding": "4px 0px 60px",
  "sidebarHidden": "none",
  "mainHidden": "none",
  "mobileVisible": "block",
  "topicBodyPadding": "12px 14px 18px",
  "topicContentFontSize": "14px",
  "duplicateToolbarHidden": "none"
}
```

## Reset to desktop

```js
document.getElementById('force-mobile')?.remove();
window.matchMedia = origMM;  // restore if you kept a reference
location.reload();  // cleanest reset
```

## Specific failure modes

### "My mobile CSS isn't applying"

Checklist:
1. Did the new CSS actually reach the served page? `curl -s URL | grep "new-rule-name"`
2. Are you inside `@media (max-width: 900px)` in the source CSS? (grep for the rule without the `@media` and you should NOT find it.)
3. Is something setting `display: grid` / `display: flex` on the same element? Add `!important`.
4. Is the JS testing the correct selector? `document.querySelectorAll('.mobile-bar').length` should be > 0.

### "Matchmedia returns false after my override"

You overrode `window.matchMedia` but the JS that checks `window.innerWidth < 900` directly will still see 1280. Look for the actual condition:

```js
// Common patterns to search:
window.innerWidth < 900
window.innerWidth <= 900
document.documentElement.clientWidth
```

Override those too if needed:

```js
Object.defineProperty(window, 'innerWidth', { value: 375, configurable: true });
Object.defineProperty(document.documentElement, 'clientWidth', { value: 375, configurable: true });
```

### "Topic accordion won't open after I forced mobile"

Mobile accordion IIFE only fires on first load. After forcing mobile, manually open:

```js
const t = document.querySelector('#hubAccordionMobile .topic-acc[data-topic="16.1.25"]');
if (t) {
  t.open = true;
  const hub = t.closest('.hub-acc');
  if (hub) hub.open = true;
}
```

Then re-probe height/padding to verify the open state still respects edge-to-edge.

### "I see mobile styles but my desktop is now wrong too"

You added mobile rules outside the `@media` block. Search the CSS for `padding: 4px 0 60px` and verify it's only inside `@media (max-width: 900px) { ... }`.

If you find it outside, the rule applies at ALL widths. Move it.

## Verification at three levels (required before reporting success)

| Level | What to check | Tool |
|---|---|---|
| **Build** | New CSS reaches served HTML | `curl -s URL \| grep "rule-name"` |
| **Structural** | Visibility toggles, hidden duplicates, compact heights | DOM probes (above) |
| **Visual** | Screenshot at narrow viewport + vision check | `browser_vision` (when model is up) |

If vision model is down (common — `Unknown Model: 1211` error), skip visual and lean harder on structural probes. The user will verify visually themselves.

## When vision IS down

Tell the user directly:
> "Vision model is down so I can't describe the screenshot myself. I verified the mobile bar height is 45px (was 140px) and the chapter page padding is now `4px 0 60px` via DOM probes. Please check the live page on your phone or narrow browser window."

Never fabricate visual details you couldn't verify.
