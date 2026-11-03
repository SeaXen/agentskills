# Dark-mode callout box, table, and text fix for mdsagar.com (v4)

## Problem (confirmed in production)

Two distinct dark-mode failure modes on mdsagar.com:

1. **Callout boxes with light pastel backgrounds (e.g. `#eff6ff`, `#f0fdf4`)**: Theme's dark-mode CSS inverts the background to dark while inline `color:#111827` stays dark → dark text on dark background = invisible.
2. **Table `tbody` rows with alternating `background:#f8fafc` (white-ish) inline**: Theme inverts row background to near-black while `color:#111827` stays dark → same problem. AND header rows with white text (`color:#fff`) on dark headers show fine in light mode but invert in dark mode.

**Root cause:** Inline `style=""` attributes that set only ONE of `background` or `color` (not both) are vulnerable to theme dark-mode inversion of the other. The theme can flip either property independently.

## Definitive Fix — [data-theme="dark"] Override Architecture (v4)

The theme sets `data-theme="dark"` on the `<html>` element when dark mode is active. We use this exact same mechanism to override both background AND color together in our CSS, guaranteeing consistency.

### Complete working pattern (used in AIS post v4):

```html
<style>
/* ── Tooltip ── */
.md-tip {
  border-bottom: 2px dotted #2563eb;
  cursor: help;
  position: relative;
  display: inline;
}
.md-tip::after {
  content: attr(data-tip);
  position: absolute;
  bottom: 135%;
  left: 50%;
  transform: translateX(-50%);
  background: #0f172a;
  color: #f1f5f9;
  font-size: 0.81em;
  padding: 8px 13px;
  border-radius: 7px;
  white-space: normal;
  width: 270px;
  text-align: left;
  line-height: 1.55;
  z-index: 9999;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.18s ease;
  box-shadow: 0 6px 20px rgba(0,0,0,0.4);
}
.md-tip::before {
  content: '';
  position: absolute;
  bottom: 127%;
  left: 50%;
  transform: translateX(-50%);
  border: 6px solid transparent;
  border-top-color: #0f172a;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.18s ease;
}
.md-tip:hover::after, .md-tip:focus::after,
.md-tip:hover::before, .md-tip:focus::before { opacity: 1; }

/* ══════════════════════════════
   LIGHT MODE — BASE STYLES
   ══════════════════════════════ */

/* TOC */
.mp-toc {
  background: #dbeafe;
  border-left: 4px solid #2563eb;
  padding: 18px 22px;
  margin: 0 0 32px;
  border-radius: 7px;
}
.mp-toc, .mp-toc * { color: #1e3a8a; }
.mp-toc a { color: #1d4ed8; text-decoration: none; }

/* CALLOUT BOXES */
.mp-box {
  padding: 18px 22px;
  margin: 28px 0;
  border-radius: 7px;
  box-shadow: 0 1px 4px rgba(15,23,42,0.08);
}
.mp-box-yellow { background: #fefce8; border-left: 5px solid #ca8a04; }
.mp-box-green  { background: #f0fdf4; border-left: 5px solid #16a34a; }
.mp-box-red    { background: #fff1f2; border-left: 5px solid #dc2626; }
.mp-box-blue   { background: #eff6ff; border-left: 5px solid #2563eb; }
.mp-box, .mp-box * { color: #111827; }
.mp-box .mp-box-title { font-weight: 700; display: block; margin-bottom: 8px; font-size: 1.04em; }
.mp-box ul, .mp-box ol { margin: 6px 0 0 0; padding-left: 22px; line-height: 1.95; }

/* TABLES */
.mp-table { width: 100%; border-collapse: collapse; margin: 16px 0; }
/* Header rows */
.mp-table thead tr { }
.mp-th-blue  thead tr { background: #2563eb; }
.mp-th-red   thead tr { background: #dc2626; }
.mp-th-green thead tr { background: #065f46; }
.mp-th-slate thead tr { background: #334155; }
.mp-table thead th { color: #ffffff; padding: 10px 14px; font-weight: 600; text-align: left; }
/* Body rows — alternating */
.mp-table tbody tr.row-a  { background: #f1f5f9; }
.mp-table tbody tr.row-b  { background: #ffffff; }
.mp-table tbody tr.row-ra { background: #fff1f2; } /* red-tint A */
.mp-table tbody tr.row-rb { background: #ffffff; } /* red-tint B */
.mp-table tbody tr.row-ga { background: #f0fdf4; } /* green-tint A */
.mp-table tbody tr.row-gb { background: #ffffff; } /* green-tint B */
.mp-table tbody td { color: #111827; padding: 9px 14px; border-bottom: 1px solid #cbd5e1; vertical-align: top; }

/* ══════════════════════════════
   DARK MODE OVERRIDES
   Uses [data-theme="dark"] which
   the theme sets on <html>
   ══════════════════════════════ */

/* TOC in dark mode */
[data-theme="dark"] .mp-toc { background: #1e3a5f; }
[data-theme="dark"] .mp-toc,
[data-theme="dark"] .mp-toc * { color: #bfdbfe; }
[data-theme="dark"] .mp-toc a { color: #93c5fd; }

/* Callout boxes in dark mode */
[data-theme="dark"] .mp-box-yellow { background: #2d2000; border-left-color: #f59e0b; }
[data-theme="dark"] .mp-box-green  { background: #052e16; border-left-color: #22c55e; }
[data-theme="dark"] .mp-box-red    { background: #2d0a0a; border-left-color: #f87171; }
[data-theme="dark"] .mp-box-blue   { background: #0f2240; border-left-color: #60a5fa; }
[data-theme="dark"] .mp-box,
[data-theme="dark"] .mp-box *      { color: #f1f5f9; }

/* Table header rows stay vivid — just lighten text slightly */
[data-theme="dark"] .mp-th-blue  thead tr { background: #1d4ed8; }
[data-theme="dark"] .mp-th-red   thead tr { background: #b91c1c; }
[data-theme="dark"] .mp-th-green thead tr { background: #064e3b; }
[data-theme="dark"] .mp-th-slate thead tr { background: #1e293b; }
[data-theme="dark"] .mp-table thead th { color: #f8fafc; }

/* Table body rows — dark backgrounds with light text */
[data-theme="dark"] .mp-table tbody tr.row-a  { background: #1e293b; }
[data-theme="dark"] .mp-table tbody tr.row-b  { background: #0f172a; }
[data-theme="dark"] .mp-table tbody tr.row-ra { background: #2d0a0a; }
[data-theme="dark"] .mp-table tbody tr.row-rb { background: #1a0505; }
[data-theme="dark"] .mp-table tbody tr.row-ga { background: #052e16; }
[data-theme="dark"] .mp-table tbody tr.row-gb { background: #021a0d; }
[data-theme="dark"] .mp-table tbody td { color: #f1f5f9; border-bottom-color: rgba(255,255,255,0.1); }
</style>

<!-- Usage: -->
<div class="mp-box mp-box-yellow">
  <span class="mp-box-title">⭐ FCPS/MRCP Exam Pearls — High-Yield Summary</span>
  <ul><li>Point one</li></ul>
</div>

<table class="mp-table mp-th-blue">
  <thead><tr><th>Territory</th><th>Key Clinical Features</th></tr></thead>
  <tbody>
    <tr class="row-a"><td><strong>MCA</strong></td><td>Face/arm > leg weakness; aphasia if dominant; neglect if non-dominant</td></tr>
    <tr class="row-b"><td><strong>ACA</strong></td><td>Leg > arm weakness; abulia; frontal signs</td></tr>
  </tbody>
</table>
```

### Key rules
- Use `[data-theme="dark"] .selector { ... }` to override both background and color together when dark mode is active
- Light mode styles use explicit hex colours (no reliance on `!important` alone)
- Do NOT use inline `style=""` for any coloured/background region — use the CSS class system instead
- All text colours are explicitly set in both light and dark mode overrides
- Table row classes (`.row-a`, `.row-b`, etc.) alternate backgrounds and are overridden in dark mode

### Verification checklist
1. Publish updated post content.
2. Open live URL with cache-bust (`?cb=<timestamp>`).
3. Toggle dark mode in the site header.
4. Confirm in light mode: all text is dark (#111827 or similar) on light backgrounds.
5. Confirm in dark mode: all text is light (#f1f5f9 or similar) on dark backgrounds.
6. Confirm: all callout boxes, tables, and TOC maintain readable contrast in both modes.
7. Confirm: tooltips work (hover any dotted-underlined term).
