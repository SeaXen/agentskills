# Token-protected API client fetch parity

Use when a Next.js app deliberately leaves page HTML public but protects `/api/*` routes with a token.

## Symptom pattern
- Pages render normally.
- Many widgets show `Unauthorized`.
- `curl` with auth header works.
- Browser fetches fail across many pages/components.
- The app already injects an auth token into the page (for example `window.__AUTH_TOKEN__`), but old components still call raw `fetch('/api/...')`.

## Lesson
When the failure is widespread, do not patch each widget first. Fix auth parity once at client bootstrap or via a shared fetch wrapper.

## Strong fix
Patch browser `fetch` early so any request to `/api/*` automatically gets the token header unless the request already set auth explicitly.

Why early matters:
- if the patch happens too late, child components may fire `useEffect` fetches before auth injection exists
- an inline script in the root layout can patch `window.fetch` before the rest of the app starts using it

## Minimum verification
- browser page renders
- one previously broken widget loads real data instead of `Unauthorized`
- one previously broken CRUD/admin page loads without auth errors
- `/api/health` still works
- live DOM/browser checks confirm the page is using the patched runtime, not stale assets
