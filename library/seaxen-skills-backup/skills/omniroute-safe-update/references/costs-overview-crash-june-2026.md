# Costs Overview Page Crash — June 2026

## What happened
After updating OmniRoute to v3.8.42, the Costs Overview page (`/dashboard/costs`) showed "Internal Server Error". The user asked if the agent's pricing patches caused it.

## Root cause
**Upstream OmniRoute bug**, NOT caused by the agent's sed patches. The error was `ReferenceError: t is not defined` in client-side React chunk `4bd1b696-7281820e82fc5615.js` (React internals, position 124429). This chunk was never touched by the agent's patches.

## Proof it was upstream
1. Agent's sed patches only touched **server-side** chunks (`/app/.build/next/server/chunks/11203,44021,95577,30038,68131.js`)
2. Error was in a **client-side** chunk (`/app/.build/next/static/chunks/4bd1b696-7281820e82fc5615.js`)
3. After `docker compose force-recreate` (fresh container from image), error persisted
4. Other pages (Dashboard, Pricing, Providers) all worked fine
5. Server returned HTTP 200 — error was in client-side React hydration
6. No server-side errors in Docker logs

## Diagnosis path
1. `docker compose ps` → container healthy
2. `curl /dashboard/costs` → HTTP 200 (not a server error)
3. Browser console → `ReferenceError: t is not defined` at chunk `4bd1b696:1:124429`
4. Checked which chunks were patched vs which had the error → different directories
5. `docker compose force-recreate` → error persisted → confirmed upstream
6. `/dashboard/costs/pricing` worked fine → page-specific bug

## Key learnings
- **Server chunks ≠ client chunks** in Next.js. They're in completely different directories.
- **HTTP 200 + "Internal Server Error"** = client-side React hydration error, not server-side.
- **`force-recreate`** proves upstream vs self-inflicted: if error persists after fresh container, it's the image.
- **DB-only pricing is safer** than sed-patching minified JS. The sed regex can match unrelated code.
- **The Costs Overview page has an upstream bug** in v3.8.42. File at github.com/diegosouzapw/OmniRoute/issues.

## What the agent should have done differently
1. Never sed-patch minified JS chunks — the regex is too greedy and can corrupt unrelated code
2. Use DB overrides only — they're persistent, safe, and sufficient for the Pricing page
3. When diagnosing a page error, check browser console FIRST (not server logs) when curl returns 200
4. When the user asks "did you do anything to this page?", check if the error is in code you actually touched before assuming responsibility
