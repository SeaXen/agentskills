# Mission Control Phase 6 — Operator Console Redesign

Use this when the user likes the companion dashboard idea but says Mission Control still feels too similar to the main dashboard, too repetitive, too card-heavy, or not premium/compact enough.

## Trigger phrases

- "this looks repetitive"
- "make Mission Control different from the main dashboard"
- "premium / beautiful / compact / organized"
- "show session ID so I can continue later"
- "make it more like a real control center"

## Core design lesson

A good Hermes **Mission Control** page should not feel like "dashboard cards again." The built-in dashboard already covers broad status/analytics. Mission Control should instead behave like an **operator console for continuity and action**.

Default hierarchy:
1. **Session Queue** — the primary lane
2. **Live Context** — details for the selected session
3. **Action Dock** — compact commands and next actions
4. **Runbook Dock** — skills/profiles/toolsets relevant to current work

Keep the page obviously distinct from the main dashboard by reducing generic telemetry and increasing continuation/resume affordances.

## What to emphasize

### 1) Session continuity first
Prominently show:
- full session ID
- source/platform
- relative recency
- message/tool counts
- resume affordances:
  - `Resume in Chat`
  - `Open Sessions`
  - `Copy Resume Command`
- latest descendant / branch continuation when available

The user should be able to glance at the page and immediately answer: **"Which session do I pick up, and how?"**

### 2) Center panel should be operational, not decorative
The central detail area should prefer:
- transcript preview / recent exchange snippets
- current model/provider
- loaded or inferred skills
- toolsets in play
- queue/source metadata
- branch/continuation relationships

This panel is for **working context**, not vanity charts.

### 3) Right rail should be a compact action dock
Prefer a small set of actions with strong hierarchy:
- resume/continue
- copy CLI resume command
- open sessions list
- open chat
- pin/unpin
- model switch
- cron quick actions

Avoid flooding the right rail with many equal-weight buttons.

### 4) Premium visual direction
Aim for:
- tight spacing
- stronger typography hierarchy
- fewer but higher-value cards
- more panel/dock language, fewer generic metric tiles
- dark operator-console mood (closer to Linear/Vercel/trading-terminal than a generic admin template)

## What to de-emphasize or remove

When the page feels repetitive, remove or demote sections like:
- generic mission telemetry
- workflow radar
- current brain
- duplicate global analytics already present elsewhere
- decorative metrics that do not help resume/continue decisions

If a metric does not help the user **continue work faster**, it should usually move down or disappear.

## Recommended information architecture

A reliable compact layout is:

- **Hero / command header**
  - Mission Control label
  - one-line explanation of the page's purpose
  - refresh / open chat controls

- **Session Queue (left)**
  - source filter: All / Telegram / Discord / CLI / etc.
  - sort: Newest / Most Messages / Most Tools
  - queue cards with visible session IDs and resume affordances

- **Live Context (center)**
  - selected session summary
  - transcript preview
  - model/provider
  - skills/toolsets
  - continuation/branch info

- **Action Dock (right)**
  - high-priority buttons only

- **Runbook Dock / lower rail**
  - related skills
  - profiles
  - cron hooks
  - optional pinned threads lane

## UX rules

- Session ID must remain visible without extra clicks.
- Resume actions should be one click or one copy action away.
- Distinguish the selected session clearly from the queue.
- Keep button copy short and imperative.
- Prefer a smaller number of decisive controls over many neutral cards.

## Verification checklist

After a redesign pass, verify:
- Mission Control is visually and structurally distinct from `/`
- session IDs are visible in queue cards or detail header
- the page exposes at least one direct resume path and one copyable CLI resume path
- model/provider is visible in the selected-session context
- skills/toolsets are surfaced somewhere in the detail or runbook area
- repetitive analytics sections were reduced or moved behind lower priority zones
- the page still works after hard refresh / private window test (to catch cached bundle confusion)

## Good summary language to use with the user

- "Mission Control is now session-first instead of analytics-first."
- "The queue, live context, and action dock are the primary surfaces."

## Anti-pattern

Do **not** keep layering more metric cards onto Mission Control just because data is available. If the page starts resembling the main dashboard, refactor the information architecture instead of adding more sections.
