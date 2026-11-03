# Browser-verified dashboard flow

Use this when polishing a live dashboard after code changes.

## Verify in browser, not just build
- Open the live app in the browser.
- If the snapshot looks thin/empty, inspect `document.body.innerText` in browser console.
- If the page has dynamic UI, verify the actual click path and resulting text/state.
- Do not trust a successful build alone for UI polish.

## Must-check flows for focus dashboards
- Home landing layout and nav visibility
- Timer start/pause/continue state
- Timer countdown actually changes on screen
- End-early / save-session path
- Schedule add/remove path
- Insights reflect stored sessions after refresh
- Sessions list updates after saves

## Smoke test standard
- Rebuild the app.
- Run the production container.
- Curl every public route and health endpoint for HTTP 200.
- Then verify the browser-rendered UI, not only the HTTP responses.