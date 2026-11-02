## Pinhook 2.1 — "What's New" copy

Two placeholders need your input before you publish — the actual shortcut key combo and which side the sidebar now opens on. I've marked both with `[ ]` rather than guessing, since wrong info in a store listing is worse than no info.

### Chrome Web Store

Chrome has no dedicated "release notes" field — put this at the top of your description, dated, and keep older entries below it.

```
What's new in 2.1

⌨️ Keyboard shortcut — pin the current page without touching your mouse.
   Default: [Ctrl+Shift+P]. Change it anytime at chrome://extensions/shortcuts.

📌 Sidebar now opens on the [left/right] — quicker to reach, stays out of
   your way while you browse.

🛠️ Fixed a memory leak — Pinhook now stays light even after hours of
   heavy tab use.
```

### Firefox Add-ons (AMO)

AMO has a real per-version "Release Notes" field (Developer Hub → your version → Release Notes) — use that field for this, not the description. Firefox users skew more power-user / long-session, so the memory leak fix goes first.

```
🛠️ Fixed a memory leak that built up over long browsing sessions.

⌨️ New keyboard shortcut to pin the current page instantly.
   Default: [Ctrl+Shift+P]. Change it in about:addons → Pinhook → Options,
   or at about:preferences#general (Firefox Shortcuts section).

📌 The sidebar now opens on the [left/right] side — easier to reach,
   less overlap with page content.
```

Both are short by design — store listings get skimmed, not read.

## On auto-update being off

The store listing itself can't fix this: a user who never visits the store page and has auto-update disabled will never see either of the texts above. Two separate problems, two separate fixes:

1. **Reach them at all.** Add an in-extension update check — a small badge on the toolbar icon (or a one-line banner in the popup) that pings a version endpoint you control and shows "Update available" with a link straight to the store page. This doesn't touch auto-update settings or self-install code (which would violate both stores' policies), it just makes the *existing* update visible to someone who'd otherwise never look.

2. **Reduce how many opt out going forward.** Add one line to your options/popup footer, shown once after a manual update: "Auto-updates are off — turn them on in `about:addons` (Firefox, gear icon → Allow automatic updates) or `chrome://extensions` (Chrome) to get fixes like this without doing it by hand." Firefox exposes the per-add-on opt-out far more visibly than Chrome does, so if the "annoying" complaint is coming disproportionately from one side, it's almost certainly Firefox.

Neither requires code beyond a small popup/badge check — no server-side infra beyond a static version file you already control.