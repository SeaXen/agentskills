# Third-party tracker button verification lessons

Use this when polishing or changing a tracker-style dashboard tab with update/copy/scan controls.

## Durable checks

- Do not stop at visual verification. After CSS/layout changes, click every non-destructive control in the live dashboard.
- For mutation controls, verify the safe precursor instead of executing blindly:
  - `Dry run` should return HTTP 200 and a concrete plan/count.
  - `Run all` may become enabled after dry-run, but do not click it unless the user explicitly wants updates executed.
  - Per-row `Run` also mutates state; verify command construction/dry-run/API path where available.
- `Run live scan` can legitimately take ~25–30 seconds because it shells out to the inventory generator and network/git checks. Wait long enough before declaring it hung.
- Verify clipboard behavior by stubbing/intercepting `navigator.clipboard.writeText` in the browser and checking the captured text, not just checking that a notice appeared.
- Validate copied command content, not just that something was copied. In updates-only mode, copied commands must exclude non-updating fallback inventory rows such as a core `hermes update -y` command when core has zero updates.
- If a hide/show manual toggle exists, verify that manual/local plugin rows are removed from every visible list they appear in, not only from a separate manual section.
- When asserting that a manual plugin is hidden, avoid using a name that may also appear as a separate git repo row. Use copied/local-only names or inspect row/source context.

## Good smoke-test shape

1. Load the live user-facing route with a cache-busting query.
2. Click `View updates`; intercept `Copy visible`; confirm exact commands.
3. Click first visible row `Copy`; confirm exact row command.
4. Click `View inventory`; confirm copied/local manual rows are visible.
5. Click `Hide manual plugins`; confirm copied/local rows vanish and the button becomes `Show manual plugins`.
6. Click `Show manual plugins`; confirm copied/local rows return.
7. Click `Dry run`; confirm the plan count and commands; do not run updates unless asked.
8. Click `Run live scan`; wait 30–40 seconds; confirm the page returns from loading and shows refreshed/live API state.
9. Check browser console for JS errors.
