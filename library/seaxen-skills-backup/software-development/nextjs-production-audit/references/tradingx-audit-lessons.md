# TradingX audit lessons

Captured from a final audit of a self-hosted Next.js trading dashboard.

## 1. Repo clean does not mean live app current

In the session, the repo built and pushed cleanly, but the running Docker app on `:8799` was stale:

- repo contained `/funding`, `/portfolio-heat`, `/portfolio-overlap`, `/api/market-context`, `/api/portfolio/heat`
- live runtime returned 404 for those pages/APIs
- Docker health was still `healthy`

Lesson: final audits must rate **repo/source** and **live deployment** separately. Probe newly-added routes against the actual running port/container.

## 2. Deployment diagnostics are high ROI

Recommend adding a route like `/diagnostics/deployment` showing:

- running git SHA / build SHA,
- build timestamp,
- Docker image ID,
- app version,
- route manifest or key feature flags,
- warning if repo HEAD differs from deployed SHA.

This catches stale deployments faster than manual curl checks.

## 3. Next 16 lint can be a gate failure itself

`npm run lint` may fail because `next lint` is removed/changed in modern Next versions or because legacy `.eslintrc` and package versions conflict. Treat this as a quality-gate finding:

- do not pretend lint passed,
- do not let it block all other audit work,
- recommend migrating to a supported ESLint flat config / command.

## 4. Frontend token injection is not public auth

Injecting an API token into frontend HTML/JS, e.g. `window.__AUTH_TOKEN__`, is convenient for a trusted LAN dashboard but is not security for public exposure. Anyone who can load the page can read the token and call APIs.

Safer alternatives:

- no auth for trusted LAN if the user explicitly prefers that,
- session login with httpOnly cookie for public exposure,
- avoid query-string tokens except for narrow machine/webhook cases.

## 5. RSS/news links need URL sanitization

If news feeds provide external links rendered as `href={item.url}`, validate protocols before rendering:

```ts
function safeExternalUrl(url: string) {
  try {
    const u = new URL(url);
    return u.protocol === "https:" || u.protocol === "http:" ? u.toString() : "#";
  } catch {
    return "#";
  }
}
```

Also add per-feed timeouts and partial-result behavior so one slow RSS source does not stall `/api/news`.

## 6. E2E route coverage must follow new features

Smoke tests that cover old routes can all pass while newly added routes 404 live. Add new pages/APIs to E2E probes whenever a feature batch adds routes.
