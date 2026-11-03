# Settings page layout pattern

The Settings page is a recurring class of dashboard UI work — multi-section,
many-form-fields, save-state page. The user expects it to be balanced,
scannable, and have a real Save action even when fields auto-save.

## Layout: 3-2-1 responsive columns

Settings pages tend to have 8–15 sections. Single column wastes horizontal
real estate; 2 columns leaves one side heavy when sections are uneven
(integrations/credentials naturally cluster on one side). Use:

```
grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-3 items-start
```

- `items-start` is critical — `items-stretch` makes short sections look
  like failures next to tall ones.
- `gap-3` (~12px) reads denser than `gap-4` for settings pages.

## Column balancing rule of thumb

Order sections so the heavy/credential-bearing column is **last**, not
middle. Visual/behavioral sections on the left, account/preferences in the
middle, integrations on the right. The right column is allowed to be
taller — users expect integrations to scroll.

## Sticky top action bar

Settings pages must have a sticky top bar containing:
- Page title + small key counter (e.g. "Settings · 32 keys · localStorage")
- Save badge ("✓ Saved" — auto-hide after ~1.5s)
- Hydration status ("hydrating…") for SSR-safe settings stores
- Action buttons (right-aligned): Export / Import / **Save** / Reset

Use:
```
className="sticky top-0 z-20 -mx-4 px-4 py-2 bg-bg/85 backdrop-blur
           border-b border-bg-line"
```

The `-mx-4 px-4` trick bleeds the bar to the viewport edges while keeping
content padding — looks clean without nested wrappers.

## Save button with pending counter

Settings auto-save on each change (UX) but the user expects an explicit
**Save** action. Wire both:

```
const [pendingChanges, setPendingChanges] = useState(0);
function flash(changed = false) {
  if (changed) setPendingChanges(c => c + 1);
  setSaved(true);
  setTimeout(() => setSaved(false), 1500);
}

<button disabled={pendingChanges === 0}>
  <Save /> Save
  {pendingChanges > 0 && <span>{pendingChanges}</span>}
</button>
```

State machine: disabled (grey) → toggle setting → `Save 1` (enabled, badge)
→ click Save → counter resets → disabled again.

This pattern was developed after the user explicitly complained "there are
not save button" — even though the fields auto-saved.

## Compact section styling

Settings sections need to be denser than dashboard cards:

- `surface p-3.5` (not `p-5`)
- Title: `text-[11px] uppercase tracking-wide`
- Subtitle: `text-[10px] text-fg-mute`
- Field label: `text-[10px] uppercase tracking-wide text-fg-mute mb-1`
- Spacing between fields: `space-y-2.5` (not `space-y-4`)

## What to remove

The user explicitly said to remove "Settings / Personal preferences. Saved
locally to your browser." — decorative subtitle text under titles. If the
subtitle doesn't add information the section header doesn't already convey,
drop it. Replace with small inline metadata in the title bar.

## Section h3 styling

Use uppercase tracking-wide for section titles so they read as
categorical labels, not headlines. This frees the page title to be
`text-sm` instead of `text-lg`.

## Sections per page guideline

- 6-8 sections: 2 columns OK
- 9-12 sections: 3 columns on wide screens (xl+)
- 13+ sections: split into tabs or a sub-nav; don't just keep stacking

## Verification checklist

- Toggle any field → Save button enables + counter increments
- Click Save → counter resets, button disables
- Sticky bar stays at top while scrolling
- All three responsive breakpoints actually change layout (test at 375 / 1024 / 1440)
- No decorative subtitle text under main page title
- Section count per column: 3-2-2 or 3-3-4 (not 2-2-7 — that means wrong split)

## Anti-patterns seen in this session

1. Single column on a 10-section page → bottom 60% empty looking
2. 2 columns with integrations on right → right column 2x taller than left
3. Auto-save with no Save button → user thinks nothing happened
4. Decorative "Personal preferences. Saved locally to your browser." text → user explicitly asked to remove
5. Section h3 styled like a page h2 (large, normal case) → visual hierarchy breaks
