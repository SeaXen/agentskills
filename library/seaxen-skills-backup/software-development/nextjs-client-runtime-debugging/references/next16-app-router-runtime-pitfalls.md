# Next.js App Router runtime pitfalls

Condensed notes from a successful debug session.

## Symptom pattern
- Page HTML renders.
- Build passes.
- Browser shows placeholder values.
- API works in curl and even from browser fetch.
- Buttons appear present but visible UI state does not update.

## High-value probes
- Inspect concrete DOM values with browser JS, not just snapshots.
- Check whether handlers exist, e.g. `typeof el.onclick`.
- Count rendered table rows after a click.
- Compare direct browser fetch result with DOM state.

## Durable fixes
1. **Inline script rendered inside React component may not execute**
   - In App Router, a literal `<script>` emitted inside the rendered component tree can be ignored for client execution.
   - Deliver ad-hoc runtime code with `next/script` and `strategy="afterInteractive"`.

2. **Dev-origin restrictions can mimic app breakage**
   - If the app is opened through `127.0.0.1`, LAN IP, or Tailscale hostname/IP, Next dev mode may block `/_next/*` assets.
   - Add exact hosts to `allowedDevOrigins` and restart dev server.

3. **Ad-hoc DOM runtime prefers simple rebinding**
   - When replacing chunks of DOM, prior listeners can effectively become stale.
   - For small pages, direct `.onclick` reassignment on current nodes is often the least fragile fix.

## Non-bugs that looked scary
- Exit code `143` or `-15` on prior dev servers during restart cycles: normal termination.
- `tcsetattr: Inappropriate ioctl for device` after background-process shutdown: terminal noise, not application logic failure.
- Slow filesystem warning under `/mnt/...`: real performance note, not functional breakage.

## Verification examples that mattered
- After the runtime fix, verify one price fetch, one conversion, one market-table mode switch, one watchlist add, and one code/demo action.
- Record the visible outputs, not just “works now”.
