# Mission Control dashboard plugin — Phase 2 pattern

Use this when extending a Hermes companion dashboard plugin beyond a static overview into a practical session-control surface.

## Goal

Keep the built-in Hermes dashboard intact while making the companion page meaningfully interactive for session continuity.

## Recommended Phase 2 additions

1. **Focused session detail panel**
   - Keep the session list on the left.
   - Add a sticky right-hand detail panel for the currently selected session.
   - Show title, full session ID, source, model, last active, message count, tool-call count, and total tokens.

2. **Transcript preview via existing API**
   - Reuse `SDK.api.getSessionMessages(sessionId)`.
   - Do not invent a new endpoint if transcript preview is the only need.
   - Load messages when `selectedSessionId` changes.
   - Show a compact recent-message preview rather than the full transcript.

3. **Session prioritization**
   - Add local pin/unpin state using browser storage:
     - `localStorage.getItem("mission-control:pinned")`
     - `localStorage.setItem("mission-control:pinned", ...)`
   - Sort pinned sessions above non-pinned ones.

4. **Filtering and sorting controls**
   - Source filter: `All sources`, then dynamic values from the loaded sessions (`telegram`, `discord`, `cli`, etc.)
   - Sort options: `Newest`, `Most messages`, `Most tools`
   - Keep these purely client-side unless server-side filtering is truly needed.

5. **Keep action model simple**
   - `Resume in Chat` → `/chat?resume=<session_id>`
   - `Copy CLI` → `hermes --resume <session_id>`
   - `Open Sessions` → `/sessions`
   - Prefer links and read-only affordances before adding mutation controls.

## UX guidance

- The page should still feel like a dashboard, not a transcript viewer.
- The session list remains the primary navigation lane.
- The detail panel should be useful even before deeper mutation features are added.
- Keep session IDs visibly readable, not hidden behind hover-only affordances.

## Verification checklist

- Plugin bundle references `SDK.api.getSessionMessages`.
- The page exposes a visible `Session detail` area.
- Resume buttons still emit `/chat?resume=` links.
- Pin state survives refresh via localStorage.
- Source and sort controls visibly affect the session list.
- Smoke tests assert the new strings/behaviors are present in the shipped bundle and stylesheet.

## Non-goals for this phase

- Replacing built-in Sessions page
- Full transcript search inside the companion plugin
- Direct model mutation or skill toggles unless specifically requested
- Server-side persistence for pins/favorites
