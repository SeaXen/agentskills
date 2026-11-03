# Browser-verified verification for Next.js dual-deploy apps

Use this after rebuilding a dashboard app that must work in Docker and on Vercel.

## What to verify in the browser
- Open the live app in a browser, not just curl it.
- If the browser snapshot is thin, empty, or missing layout, inspect `document.body.innerText` via browser console.
- Confirm the rendered nav, hero, key actions, and any dynamic status text.
- Exercise the actual click path for timer/start/save/session flows.
- Re-check the browser after a rebuild or container swap; the old container may still be serving.

## Flow checks for dashboards
- Home page nav is visible
- Start/pause/timer countdown changes on screen
- End-early or save-session path persists data
- Sessions list reflects the saved record
- Insights page reflects the same stored data
- Schedule add/remove works
- Settings changes persist across reloads

## Smoke test order
1. `npm run build`
2. run the production server or container
3. curl every route and `/api/health`
4. browser-verify the real UI and state changes