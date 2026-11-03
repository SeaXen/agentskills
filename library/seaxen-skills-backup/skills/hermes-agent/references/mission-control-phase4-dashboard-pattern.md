# Mission Control Phase 4 dashboard pattern

Use this when evolving a Hermes companion dashboard plugin beyond the read-only MVP and Phase 2/3 controls into a more premium control-center experience.

## Trigger
- The user wants a **beautiful / compact / premium** Hermes dashboard beside the built-in dashboard
- The plugin already has session list, detail panel, resume affordances, and basic control actions
- The next request is about **feedback**, **pinned continuity**, **richer transcript browsing**, or **denser operator UX**

## Recommended Phase 4 additions

### 1) Action feedback via local toast UI
Add a lightweight client-side toast state inside the plugin bundle.

Good targets for success/error feedback:
- model switch
- skill toggle
- cron pause/resume/run
- pin/unpin session
- copy resume command

Practical pattern:
- keep a `toast` state like `{ type: "success" | "error", message: string } | null`
- auto-clear it with `setTimeout` in a `useEffect`
- render a small sticky toast stack near the top of the page
- on failure, set both the page `error` state and the toast so operators get immediate feedback

### 2) Priority lane for pinned sessions
If Phase 2 already stores pinned session IDs in `localStorage`, Phase 4 should surface them in a dedicated top section.

Recommended section:
- heading: `Priority lane`
- source: pinned subset of the already filtered/sorted sessions
- size: keep it compact (for example top 4)

This gives the operator a fast continuity lane without replacing the full session list.

### 3) Richer transcript controls
Keep the Phase 2 detail panel, but add a transcript toolbar.

Useful controls:
- `Transcript mode`
- `Compact`
- `Full transcript`
- badges showing total filtered transcript count and number currently displayed

Simple pattern:
- derive `transcriptMessages` from the fetched session messages
- compact mode shows only the tail slice (for example last 12)
- full mode shows the full filtered transcript

### 4) Skill search inside the skill layer
Once the skill panel is dense, add an inline search box.

Good pattern:
- local `skillFilter` state
- search across `name`, `description`, and `category`
- keep result count visually bounded (for example first 8 cards)
- show a small empty-state line such as `No skills match this filter`

### 5) Resume-command polish
Prefer explicit action wording:
- `Copy resume command`

This is clearer than a generic `Copy CLI` label when the page is specifically about session continuity.

## Verification pattern

### Tests
Extend the plugin smoke tests to assert the bundle/CSS include markers for:
- toast success/error state writes
- `Priority lane`
- `Transcript mode`
- `Full transcript`
- `Compact`
- `Search skills`
- `Copy resume command`
- `.mc-toast-stack`
- `.mc-toast-success`
- `.mc-toast-error`
- `.mc-priority-grid`
- `.mc-transcript-toolbar`
- `.mc-search-stack`

### Browser checks
- direct route loads: `/mission-control`
- pinning a session causes it to appear in `Priority lane`
- transcript controls are visible in the detail panel
- skill search input is visible
- copy resume command buttons are visible on session rows

## Hermes-specific dashboard plugin quirks

### Plugin rescan in browser console
Use the dashboard session token header and an **absolute URL** when rescanning plugins from the browser console.

Pattern:
```js
fetch(window.location.origin + '/api/dashboard/plugins/rescan', {
  headers: { 'X-Hermes-Session-Token': window.__HERMES_DASHBOARD_SESSION_TOKEN__ }
}).then(r => r.json())
```

Important notes:
- A prior working pattern used **GET** here; attempting `POST` can return `Method Not Allowed`
- In browser console snippets, prefer `window.location.origin + '/api/...'` over a relative URL if the relative form is failing in that context

## Design guidance
- Keep the built-in Hermes dashboard intact; continue using a **companion dashboard plugin**
- Make premium UX improvements additive, not invasive
- Prefer compact, operator-centric panels over large explanatory blocks
- Keep the UI fast and mostly local-state driven unless the server must change
