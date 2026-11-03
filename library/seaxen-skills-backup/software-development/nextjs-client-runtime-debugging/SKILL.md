---
name: nextjs-client-runtime-debugging
description: Debug Next.js App Router pages when UI renders but client-side behavior, data loading, or browser interactions do not work as expected. Covers inline-script pitfalls, dev-origin issues, and browser-first verification.
---

# Next.js client runtime debugging

Use this when a Next.js app looks fine at first glance but buttons, data fetches, hydration-driven updates, or browser-visible behavior are broken or inconsistent.

## Triggers
- App renders static markup but interactive controls do nothing.
- Browser shows placeholders while build succeeds.
- Data fetches work in curl/server checks but not from the page.
- Dev server logs cross-origin warnings for `/_next/*` assets.
- The user asks for browser verification, not just build success.

## Core rule
For this class of task, **build success is not verification**. Verify in a live browser and inspect the DOM plus browser console before claiming the UI works.

## Workflow
1. **Confirm the symptom in browser**
   - Load the page in browser tools.
   - Snapshot the page.
   - Use browser console/DOM inspection to check whether values changed, whether handlers exist, and whether expected rows/nodes were created.

2. **Separate transport from runtime**
   - If API calls work in `curl` or server-side checks, test the same fetch from the browser context.
   - If browser fetch works but UI stays stale, the bug is usually client runtime/binding, not the API.
   - If the app intentionally leaves page HTML public but token-protects `/api/*`, inspect whether legacy client components still use raw `fetch()` without the auth header. Widespread `Unauthorized` across widgets is often a client bootstrap/auth parity bug, not many separate page bugs.

3. **Check the browser console early**
   - Look for hydration/client-runtime errors, not just thrown exceptions.
   - In Next.js App Router, warnings about script handling can explain a fully static-looking page even when markup is present.

4. **If using ad-hoc browser runtime code, verify script execution path**
   - Do **not** assume a literal `<script>` rendered inside a React component will execute on the client.
   - For injected client runtime code in App Router, use `next/script` with a client-safe strategy such as `afterInteractive`.
   - After changing script delivery, re-open the page and verify actual runtime effects in the DOM.

5. **Check event binding survivability**
   - If markup is being re-rendered/replaced by `.innerHTML` or similar ad-hoc updates, handlers attached with prior node references may disappear.
   - Rebind after render, or use explicit reassignment on the current nodes.
   - In small DOM-runtime pages, direct `.onclick = ...` assignment can be more reliable than stacking `addEventListener` calls across repeated init/re-render cycles.

6. **Prefer same-origin API routes when browser fetches are flaky**
   - If direct browser `fetch()` calls to third-party APIs are inconsistent, rate-limited, blocked by CORS/proxy policy, or behave differently across endpoints, move those requests behind Next route handlers under `app/api/*`.
   - Keep the browser talking only to same-origin paths such as `/api/crypto` or `/api/network-fees`; let the server-side route call CoinGecko/RPC/other public APIs.
   - This often stabilizes client behavior, makes browser verification more deterministic, and gives one place to add timeouts, headers, caching rules, and graceful fallbacks.
   - After introducing a proxy route, re-test the original broken widgets individually; do not assume the route fixed the UI wiring by itself.

7. **Handle Next.js dev-origin restrictions**
   - If dev logs show blocked cross-origin access to `/_next/*` resources from LAN/Tailscale/local aliases, add the exact dev hosts to `allowedDevOrigins` in `next.config.*`.
   - Restart the dev server after changing this config.

8. **Sequence initialization when widgets depend on shared price state**
   - If some widgets populate shared caches/state used by others (for example market-table data seeding watchlist/portfolio prices), initialize the shared source first.
   - Parallel `Promise.allSettled()` startup can leave dependent widgets rendering placeholders even when the APIs themselves work.
   - Prefer: shared-market/global refresh first, then dependent widgets such as token detail, chart, converter, watchlist, and portfolio.

9. **Re-verify specific controls, not just page load**
   - Check representative actions end-to-end: one fetch action, one table reload, one form/conversion action, one add/remove action if present.
   - Confirm visible output changed to expected non-placeholder values.
   - For data dashboards, include at least one stateful interaction (e.g. add portfolio item / add alert) and one mode switch (e.g. top → gainers).

## Support files
- `references/nextjs-proxy-routes-for-flaky-browser-fetches.md` — compact notes from the pyhox crypto dashboard case: when to proxy public APIs through Next route handlers, what failed in-browser, and what verification proved the fix.
- `references/token-protected-api-client-fetch.md` — public HTML + protected `/api/*` pattern: inject auth early, patch browser fetch globally when many legacy client components still call raw `fetch`.

## Common pitfalls

### Print-to-PDF pages: the "Event handlers cannot be passed" trap

**Symptom:** Server-rendered review/report page (e.g. `/review/print`) renders fine, but the moment you add a `<button onClick={() => window.print()}>` to it, every request to that page fails at runtime with:

```
Error: Event handlers cannot be passed to Client Component props.
  {className: ..., onClick: function onClick, children: ...}
If you need interactivity, consider converting part of this to a Client Component.
```

The page might even render in `next dev` (with a misleading dev-only warning) but throw at request time in `next start` / production. The build itself passes — `next build` doesn't catch this, only the runtime does.

**Why:** App Router treats the entire file as a Server Component unless `"use client"` is declared. Server Components render to a JSON-friendly output and **cannot carry event handlers** across the server/client boundary. The `onClick` prop on a `<button>` looks like an event handler and trips the runtime guard. This is unrelated to `useState` / `useEffect` — the guard is specifically about props named like event handlers.

**Fix — extract the interactive bit into a `"use client"` child:**

```tsx
// app/review/print/PrintButton.tsx
"use client";
export function PrintButton() {
  return (
    <button
      className="print-btn"
      onClick={() => typeof window !== "undefined" && window.print()}
    >
      Print / Save as PDF
    </button>
  );
}
```

```tsx
// app/review/print/page.tsx (Server Component — does the data work)
import { PrintButton } from "./PrintButton";
import { listTrades } from "@/lib/crypto/db";
import { listJournal, attributionByTag, attributionByExchange, attributionBySymbol } from "@/lib/crypto/db-extras";

export const dynamic = "force-dynamic";

export default function ReviewPrintPage() {
  const trades = listTrades({ limit: 1000 });
  // ... compute analytics from server-side data ...
  return (
    <div>
      <div className="no-print"><PrintButton /></div>
      {/* server-rendered tables of KPIs, attribution, etc. */}
    </div>
  );
}
```

The Server Component can render the Client Component as `<PrintButton />` (no props cross the boundary because the button takes none). For print styling, inline a `<style>` block in the Server Component:

```css
@media print {
  body { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  .no-print { display: none !important; }
  table { page-break-inside: avoid; }
}
```

**Same pattern applies to:** any small interactive widget inside a server-rendered report page — a "copy link" button, a "share" dropdown, a "collapse this section" toggle, etc.

**Why this works:** `"use client"` at the top of `PrintButton.tsx` flips that file (and only that file) to the client bundle. The server page renders it like any other component, but the `onClick` now lives in a client tree, which is allowed.

**Verification:** After splitting, `npm run build` should pass (the dev server sometimes papers over this with a warning; production does not), and `curl http://localhost:8799/review/print` should return a 200 HTML response, not a 500. The Print button works when clicked in the browser, the user picks "Save as PDF" from the dialog, and a real PDF is generated.

- Treating `npm run build` success as proof that the browser runtime is fine.
- Debugging only with server logs while the browser console already states the real cause.
- Forgetting that `allowedDevOrigins` changes require a dev-server restart.
- Testing only initial render instead of clicking real controls.
- Assuming API failure when the actual issue is unexecuted client script or lost event handlers.
- In page-public/API-protected apps, chasing each widget individually instead of fixing auth parity once at client bootstrap or through a shared fetch wrapper.
- When the user says "fix X and make it working", delivering analysis, plans, or summaries instead of actual file edits followed by live verification. For this user, real `write_file` / `patch` operations + browser confirmation are required before claiming completion.

## Fast verification checklist
- Browser console has no blocking runtime warning.
- A known dynamic value changes from placeholder to live data.
- At least one button click causes a visible state change.
- Table/list rows populate beyond placeholder state.
- If LAN/Tailscale host is used in dev, `/_next/*` assets are no longer blocked.

## References
- `references/next16-app-router-runtime-pitfalls.md` — condensed notes from a real debugging session covering inline-script non-execution, `next/script`, dev-origin warnings, and browser verification probes.
