# Systor mobile Settings compact patterns

Use when the user says the Settings page on phone is too big, overflows horizontally, needs zoom-out, or the top toolbar feels like a floating block.

## Core rules
- Do not redesign desktop.
- Scope the fix to the Settings page only, ideally with `body:has(.settings-page)` inside the mobile media block.
- If the complaint says the toolbar is floating, sticky positioning is the bug. Remove sticky on mobile rather than trying to shrink a sticky bar forever.

## Recommended mobile-only overlay

```css
@media (max-width:700px){
  body:has(.settings-page) .sticky-actions{
    position:static !important;
    top:auto !important;
  }
  body:has(.settings-page) .page-tab{
    min-width:34px !important;
    width:34px !important;
    height:34px !important;
    padding:0 !important;
  }
  body:has(.settings-page) .tab-icon{font-size:14px !important;}
}
```

## Layout targets that worked
- Top status/meta chips: 2-column grid.
- Top action buttons: 2-column grid.
- ACCESS rows: compact stack (`kind`, `value`, `Copy`) instead of long horizontal rows.
- Settings forms: 1-column mobile grid.
- Buttons/inputs: reduce height/padding slightly; keep touch-safe.

## Active tab / icon mismatch
If the Settings gear icon looks bigger than the other mobile page icons:
- inspect active-state box-shadow and padding, not just the glyph size
- reduce active tile glow/shadow first
- if still heavy, reduce active icon font size by ~1px for that page-surface only

## Verification probes
- Confirm the Settings CSS asset version changed in served HTML.
- Verify mobile Settings toolbar computed style:
  - `position === 'static'`
  - no `top` sticky offset in effect
- Verify action buttons and chips fit the viewport width.
- Verify other pages still use their normal mobile tab styling.

## Why this matters
This user repeatedly rejects desktop-wide fixes for mobile complaints. A page-scoped mobile overlay is safer than broad shared-header edits.