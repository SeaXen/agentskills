# TradingX 10/10-sector push pattern

Use when the user keeps asking to push a mature Next.js trading/dashboard app closer to “10/10” after the obvious build/test/security gates are already green.

## High-ROI sequence

1. **Do not claim literal 10/10.** Treat it as a direction. Ship measurable sector improvements, then re-score honestly.
2. Add **operator-visible diagnostics** rather than only hidden fixes:
   - `/api/deployment` + `/diagnostics/deployment` for build SHA/time/auth mode.
   - `/api/security/diagnostics` + `/diagnostics/security` for auth/token/header/RSS/advisory checks.
   - `/api/quality/diagnostics` + `/diagnostics/quality` for sector scorecards and explicit remaining gaps.
3. Tighten gates to strict mode once warnings are cleaned:
   - `eslint . --max-warnings=0`
   - `tsc --noEmit`
   - unit/API tests
   - production `next build`
   - Playwright E2E against the live container.
4. Add resilience UI:
   - `app/error.tsx` root error boundary with retry + dashboard recovery.
   - `app/not-found.tsx` polished 404 with navigation recovery.
5. Add mobile smoke checks at a narrow viewport, not just desktop render checks.

## Playwright gotcha: intentional 404 smoke

When testing a custom 404 page, Chromium usually emits a console error like:

```text
Failed to load resource: the server responded with a status of 404 (Not Found)
```

If the route is intentionally missing and the expected status is 404, filter that one browser-console message. Otherwise the test will fail even though the 404 page works correctly.

Pattern:

```ts
const expected = route.includes("missing-route") ? 404 : 200;
expect(res?.status()).toBe(expected);
const fatal = errors.filter(
  (e) => !NOISY_BROWSER_ERROR.test(e) && !(expected === 404 && /status of 404|404 \(Not Found\)/i.test(e)),
);
expect(fatal).toEqual([]);
```

## Scoring pattern

Use diagnostics pages to make score movement observable, but keep warnings honest:

- `pass` = full point
- `warn` = partial credit if the warning is intentional/tracked (e.g. LAN/no-auth mode or upstream dependency advisory with unsafe force-fix)
- `fail` = zero

Do not inflate the final user-facing score. Name the remaining structural blockers: real exchange testnet lifecycle, safe dependency patch path, session login for public exposure, Lighthouse/a11y baseline, and portfolio hard caps.

## Commit/deploy pattern

After each wave:

```bash
npm run lint && npm run typecheck && npm test && npm run build
AUTH_TOKEN= npm run e2e
git add -A && git commit -m "..." && git push origin main
npm run build && bash scripts/redeploy.sh
# live probe /api/deployment and key pages; buildSha must match HEAD
```

If `git push` times out, retry push first, then rebuild/redeploy so `/api/deployment` reports the final pushed SHA.
