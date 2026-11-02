Using the changelog-writing skill's non-git-surfaces guidance (Chrome Web Store has no dedicated what's-new field; Firefox AMO does, pinned to `en-US`) and its end-user entry rules (observable effect first, no internal vocabulary, 3–5 items).

**Mode:** working from your spoken description only — no repo or commit history for Pinhook exists in this workspace, so nothing below is diff-verified. Treat every entry as needing your sign-off against the actual code before shipping.

**Tier: 2** (noticeable impact on most active users) — driven by the sidebar relocation, which changes something people rely on by habit even though it requires no action. That's why it leads below, ahead of the purely additive shortcut.

---

## Chrome Web Store

Chrome has no what's-new field — this goes at the top of your **Description**, above the fold, under a dated heading so it doesn't get lost next time you update it:

```
What's new in 2.1

Changed: Pinhook's panel now opens on the [NEW SIDE] instead of the [OLD SIDE]. If it seems to be gone, look there.
New: Open Pinhook without touching the mouse — press [SHORTCUT] (check chrome://extensions/shortcuts to see or change it).
Fixed: A memory leak that built up the longer Pinhook stayed open, which could slow your browser down.
```

## Firefox Add-ons (AMO)

Goes in the version's release-notes field (AMO stores this as `en-US` regardless of your add-on's default locale — file it there specifically, not under your source locale):

```
Changed: Pinhook's panel now opens on the [NEW SIDE] instead of the [OLD SIDE]. If it seems to be gone, look there.
New: Open Pinhook without touching the mouse — press [SHORTCUT] (customize anytime in about:addons → ⚙ → Manage Extension Shortcuts).
Fixed: A memory leak that built up the longer Pinhook stayed open, which could slow your browser down.
```

Optional — AMO's separate **notes-for-reviewers** field (not shown to users):
```
2.1 adds a keyboard shortcut (commands API), moves where the sidebar panel renders, and fixes a memory leak. No new permissions requested. [confirm before submitting]
```

---

## Traceability

| Entry | Source |
|---|---|
| Panel opens on a different side | Your message, 2026-09-18 ("changes where the sidebar opens") — unverified against a diff |
| New keyboard shortcut | Your message, 2026-09-18 ("adds a keyboard shortcut") — unverified against a diff |
| Memory leak fix | Your message, 2026-09-18 ("fixes a memory leak") — unverified against a diff |

## Excluded

None — all three changes you described are consumer-observable and are all included.

## Needs a human

- **Fill the placeholders**: exact shortcut key combo, and which side the panel moved from/to. I didn't invent specifics for either — that's the kind of unsourced detail this skill's verification gate exists to block.
- **Confirm no new permission prompt.** If the `commands` API (keyboard shortcut) triggers Chrome/Firefox's "this extension needs new permissions" re-consent screen on update, that's a bigger deal than store text and probably bumps this to require an in-product note too.
- **Character budget**: neither store documents a hard cap for extension listings (unlike mobile app stores' 500/4,000-char fields), so I kept both versions tight by default discipline, not because a cap forces it — expand if you want more detail.
- **Where's the canonical record?** Per this skill's guidance, the store field should be a pointer, not the source of truth — and it directly answers your auto-update complaint: users who disabled auto-update won't see either store field until they manually check for an update, and have historically filed issues when they can't find "what changed" anywhere else. Point them somewhere persistent — a GitHub releases page, a `/changelog` page, or (most effective for a disabled-auto-update cohort) an in-extension "what's new" panel that opens once after the update actually installs, regardless of how the user got it. That's a separate surface from what you asked for today, but it's the one that actually reaches that group; the store text won't.
- **Existing Description content**: I don't have your current Chrome listing text, so I can't confirm the new heading won't collide with or bury something already there — check before pasting over it.