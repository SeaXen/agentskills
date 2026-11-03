---
name: seadash-nested-layered-card-pattern
description: Concrete CSS technique for "Homarr-style" or "real layered card" look on a single-file dashboard — nested inner panel via ::before overlay with pointer-events: none, plus the browser verification trick using getComputedStyle(el, '::before') to confirm the pseudo-element actually rendered.
---

# SeaDash nested layered card pattern (Homarr-style)

When Dr. Sagar shows a Home Assistant / Homarr / Dashy reference screenshot and asks for "this kind of layered card" or "make my dashboard beautiful, this looks ugly", the working answer on a single-file dashboard with an existing 189-class stylesheet is a **nested inner panel via `::before` pseudo-element overlay** on the card, combined with the **append-overlay pattern** (see `seadash-refined-css-overlay.md`).

This reference captures the specific CSS technique and the browser verification shape that actually worked. The general append-overlay framework is covered in `seadash-refined-css-overlay.md`; this file is the card-design zoom-in.

## When to use

- User shows a reference screenshot of cards with a clear "outer card + inner panel" layered look (Homarr, Dashy, IBM Carbon, most modern app-launcher dashboards)
- User says "ugly", "make it look like this", "modern", "premium", "layered", "nested", "depth", "3D"
- The current dashboard has working `app-card` / `.card` markup with 4+ child elements (icon, name, port, badges, action buttons) that all need their own visual zone
- You do NOT want to break existing class definitions or change DOM structure

## The technique: `::before` pseudo-element as the inner panel

The card is structured as:

```
.outer-card
├── (no DOM element here, just space)         ← ::before pseudo lives in this 8px gutter
├── .icon
├── .name
├── .port
├── .badge-row
└── .action-buttons
```

The `::before` creates a translucent panel that sits between the outer border and the inner content, producing the "card inside a card" illusion without any extra HTML.

```css
.app-card, .card, [class*="card"] {
  position: relative;
  background: var(--card);              /* outer card surface */
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 0;                           /* critical: no padding on outer */
  display: flex;
  flex-direction: column;
  cursor: pointer;
  overflow: hidden;                     /* clip ::before to card bounds */
  box-shadow: var(--shadow-sm);
  transition: background 0.18s, border-color 0.18s, transform 0.18s, box-shadow 0.18s;
}

.app-card::before, .card::before {
  content: '';
  position: absolute;
  inset: 8px;                           /* the 8px gutter creates the layered look */
  background: rgba(255, 255, 255, 0.025);   /* very subtle — most of the "depth" is the border */
  border: 1px solid rgba(255, 255, 255, 0.04);
  border-radius: 10px;                  /* slightly tighter than outer 14px */
  pointer-events: none;                 /* critical: must not block clicks */
  transition: background 0.18s, border-color 0.18s;
  z-index: 0;
}

.app-card:hover::before, .card:hover::before {
  background: rgba(255, 255, 255, 0.04);
  border-color: rgba(255, 255, 255, 0.08);
}
```

## The four "must-have" rules

| Rule | Why it matters | What breaks if you skip it |
|---|---|---|
| `pointer-events: none` on `::before` | The pseudo-element sits on top of the card's children in the visual stack | All clickable children (action buttons, links, status LEDs) become unclickable. The user will say "the cards don't respond" |
| `z-index: 0` (or none) on the pseudo and `z-index: 1` (or position:relative + z-index) on children | The pseudo needs to stay behind the children | Children get visually covered by the inner panel; you see the panel but not the icon/name/port |
| `overflow: hidden` on the outer card | The 8px-inset pseudo must be clipped at the outer card's rounded corners | On rounded corners the pseudo's square corners peek out as a visible "frame" artifact |
| `padding: 0` on the outer card, with child elements using their own margins | Lets the pseudo fill the full interior cleanly | Pseudo only fills the padded area, leaving visible gaps at the edges; loses the nested look |

## Layer the rest of the card content with `position: relative`

Any child element that needs to sit ABOVE the `::before` panel (icon, name, port, badges, action buttons) needs to be in its own stacking context:

```css
.app-card .card-name,
.app-card .card-icon,
.app-card .card-port,
.app-card .app-name,
.app-card .app-url,
.app-card .app-meta,
.app-card .card-actions,
.app-card .card-action-btn,
.app-card .card-badge,
.app-card .card-stat,
.app-card .status-led,
.app-card .card-desc {
  position: relative;
  z-index: 1;
}
```

A single shared rule targeting the common child classes is enough — do not need to wrap each one in `z-index: 1` in HTML.

## Position the corner elements (icon, status LED, badges, actions) absolutely

To get the clean "icon top-left, badge top-right, actions bottom-right" layout that Homarr-style cards use, the standard card structure becomes:

```css
.card-icon, .app-card .icon {
  width: 38px; height: 38px;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.06);
  display: inline-flex; align-items: center; justify-content: center;
  font-size: 20px;
  flex-shrink: 0;
  margin: 16px 0 0 16px;       /* inset from card edges */
}

.card-name, .app-name {
  margin: 14px 16px 2px 16px;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  max-width: calc(100% - 32px);
}

.card-port, .app-meta .port {
  margin: 0 16px 14px 16px;
  color: var(--text-dim);
  font-size: 12px;
  font-variant-numeric: tabular-nums;
}

.status-led {
  position: absolute;
  top: 14px; left: 14px;
  width: 7px; height: 7px;
  border-radius: 50%;
  background: var(--green);
  box-shadow: 0 0 0 2px rgba(52,211,153,0.18), 0 0 8px var(--green);
  z-index: 2;
}

.card-badge, .card-badge-row {
  position: absolute;
  top: 12px; right: 12px;
  z-index: 2;
}

.card-actions, .card-action-btn {
  position: absolute;
  bottom: 12px; right: 12px;
  z-index: 2;
}
```

This produces the "floating zones" layout the user is asking for, without touching the JS or the original class definitions.

## The "selected/active" state with a colored glow

Homarr-style cards have a single blue/indigo glow on hover or active state:

```css
.app-card.active, .card.active,
.app-card[data-status="up"], .card[data-status="up"] {
  border-color: var(--accent);
  background: #181a2c;                    /* slightly bluer tint */
  box-shadow: 0 0 0 1px var(--accent), 0 0 24px 2px var(--accent-glow);
  transform: translateY(-2px);
}
.app-card.active::before, .card.active::before {
  background: rgba(79, 110, 247, 0.06);
  border-color: rgba(79, 110, 247, 0.25);
}
```

The inner panel picking up the accent color is what makes the "selected" state read as cohesive — the entire card tints blue, not just the outer border.

## Browser verification: confirm the `::before` actually rendered

After the append, the most important verification is that the pseudo-element actually exists in the rendered DOM, not just that the CSS rule was parsed. `getComputedStyle(element, '::before')` is the standard browser-console check:

```js
(function(){
  const card = document.querySelector('.app-card') || document.querySelector('.card');
  if (!card) return 'no card found';
  const before = getComputedStyle(card, '::before');
  return JSON.stringify({
    content: before.content,             // should be '""' or 'none' for content-less pseudos
    position: before.position,            // should be 'absolute'
    inset: before.inset,                  // should be '8px'
    background: before.backgroundColor,    // should be 'rgba(255, 255, 255, 0.024)' style
    border: before.border,                // should be the hairline border string
    borderRadius: before.borderRadius,    // should be '10px' (tighter than outer 14px)
    pointerEvents: before.pointerEvents   // should be 'none' — this is the critical one
  });
})()
```

If `pointerEvents` is `auto` or `inherit` instead of `none`, the inner panel is blocking clicks on the children. That is the #1 failure mode for this pattern.

A second check: verify the *outer* card's computed properties too, so the layered geometry is provable:

```js
const s = getComputedStyle(card);
return JSON.stringify({
  borderRadius: s.borderRadius,          // 14px
  background: s.backgroundColor,          // var(--card)
  border: s.border,                      // 1px subtle border
  padding: s.padding,                    // 0px
  boxShadow: s.boxShadow,                // soft drop shadow
  minHeight: s.minHeight                 // card height
});
```

If the outer card's `padding` is not `0`, the pseudo only fills the padded area and the layered look is broken.

A third check: verify the corner elements (icon, LED, badge, actions) are actually positioned and visible:

```js
const card = document.querySelector('.app-card');
const led = card.querySelector('.status-led');
const badge = card.querySelector('.card-badge');
const icon = card.querySelector('.card-icon');
return JSON.stringify({
  led: led ? {pos: getComputedStyle(led).position, top: getComputedStyle(led).top, left: getComputedStyle(led).left, zIndex: getComputedStyle(led).zIndex} : 'missing',
  badge: badge ? {pos: getComputedStyle(badge).position, top: getComputedStyle(badge).top, right: getComputedStyle(badge).right} : 'missing',
  icon: icon ? {pos: getComputedStyle(icon).position, borderRadius: getComputedStyle(icon).borderRadius, fontSize: getComputedStyle(icon).fontSize} : 'inline'
});
```

This confirms the "floating zones" layout that distinguishes Homarr-style cards from generic stacked cards.

## The end-to-end check that saved the original SeaDash modals

A blank `getComputedStyle` check is not enough — the modals must still work. Run the full verification from `seadash-refined-css-overlay.md` PLUS the new pseudo-element check. Concretely:

```bash
curl -sS -o /dev/null -w "HTTP %{http_code} | %{size_download} bytes\n" http://localhost:9090/
```

In the browser console:

```js
// 1. Pseudo element rendered
const card = document.querySelector('.app-card');
const before = getComputedStyle(card, '::before');
console.assert(before.pointerEvents === 'none', 'pseudo blocks clicks!');

// 2. Modal save/close still work
const saveBtn = document.querySelector('#modal-layout button[onclick*="saveLayoutColumn"]');
const closeBtn = document.querySelector('#modal-layout button[onclick*="closeModal"]');
saveBtn.click();
console.assert(document.getElementById('modal-layout').classList.contains('active'), 'save did not fire');
closeBtn.click();
console.assert(!document.getElementById('modal-layout').classList.contains('active'), 'close did not fire');

// 3. 39 critical functions still defined
const fns = ['openAddModal', 'saveApp', 'saveConfig', 'openLayoutModal',
  'newLayoutColumn', 'deleteLayoutColumn', 'applyLayoutPreset', 'toast',
  'cycleTheme', 'refreshAll'];  // sample of the 39
const missing = fns.filter(f => typeof window[f] !== 'function');
console.assert(missing.length === 0, 'missing: ' + missing.join(','));
```

## Why this works on SeaDash specifically

SeaDash is a single-file operator dashboard with 189 class definitions and 9 modals. The `:before` overlay pattern produces a clean Homarr-style look **without**:

- removing any of the 189 original classes
- changing the JS bindings (`saveLayoutColumn`, `closeModal`, `toggleLayoutAutoRule`, etc.)
- touching the modal architecture (`.modal-overlay` backdrop vs `.modal` panel)
- breaking the `.auth-overlay` login screen
- rebuilding the `index.html` from scratch

Because the new CSS lives in a second `<style id="refined">` block that the original rules cannot override (later in the cascade), the existing class definitions stay functional even when the new rules visually replace them.

## Pitfalls learned the hard way

- **Forgetting `pointer-events: none` on the `::before`.** The pseudo-element ends up on top of the icon/name/port in the visual stack and silently blocks clicks. The dashboard will look right but stop responding to clicks. Always verify with `getComputedStyle(el, '::before').pointerEvents === 'none'`.
- **Forgetting `z-index: 1` on the corner elements.** Even with `pointer-events: none`, if the child elements don't have their own stacking context the browser's default stacking can put the pseudo on top during compositing. The icon and badges "disappear" visually.
- **Forgetting `overflow: hidden` on the outer card.** The pseudo's 10px rounded corners don't match the outer 14px corners, so on the rounded corners you see the pseudo's square corners peeking out as a small "frame" artifact. Clipping fixes it.
- **Setting `padding` on the outer card instead of `0`.** The pseudo only fills the padded area, leaving visible gaps at the card edges. The nested look is lost.
- **Skipping the `position: relative` on the outer card.** The `::before` `position: absolute` will then be positioned relative to the nearest positioned ancestor (often the body), not the card.
- **Using `content: ' '` instead of `content: ''` on the pseudo.** Some older browsers don't render `content-less` pseudos. The empty-string form is the modern correct form. `getComputedStyle().content` will return `'""'` (the two-quoted empty string) when the pseudo is rendered, `'none'` when it isn't.
- **Confusing this with the retro CRT pattern.** The retro CRT pattern in `seadash-retro-crt-theme.md` is a full atomic-swap with ASCII decorations and scanlines. The nested-card pattern is a polish pass that keeps the modern look. They are different design systems, not variants of each other.
- **Treating "this looks soooooooo ugly" as a one-line CSS tweak.** The user is asking for a card-design system overhaul, not a color change. The 822-line original CSS stays, the 200-line append-overlay is added, and the verification proves both the new look AND the unchanged 189 class surface.

## File locations

- Source: `/mnt/tb/1Apps/SeaDash/index.html`
- Service: `/etc/systemd/system/seadash.service` → `/usr/bin/python3 /mnt/tb/1Apps/SeaDash/server.py`
- Working dir: `/mnt/tb/1Apps/SeaDash`
- Backups: `index.html.bak.refined.<timestamp>` (after append-overlay)
- Public URL: `https://dash.xuup.top`, local: `http://localhost:9090`
- Server restart: not needed for `index.html` edits; just refresh the browser

The Python `server.py` does not need to be touched — it serves the file as static content.
