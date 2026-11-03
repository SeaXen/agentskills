# TradingX audit-hardening wave (2026-07)

Reusable lessons from pushing a Next.js 16 trading dashboard closer to production quality after a final audit.

## High-value fixes that moved the score most

1. **Redeploy freshness is a first-class audit gate**
   - Repo/build passing is not enough. Probe the running container for new pages/APIs.
   - Add `/api/deployment` returning `buildSha`, `buildTime`, Node version, env, and auth mode.
   - Add a small `/diagnostics/deployment` page so stale deploys are visible from the UI.
   - If the deploy script bakes git SHA into the image, commit first, then rebuild/redeploy again so the live SHA is the final pushed commit.

2. **Next 16 lint gate: use flat config, not `next lint`**
   - `next lint` is no longer a reliable script target in this setup.
   - Install: `@next/eslint-plugin-next`, `eslint-plugin-react`, `eslint-plugin-react-hooks`, `typescript-eslint`, `@typescript-eslint/parser`, `@typescript-eslint/eslint-plugin`.
   - Use `eslint.config.mjs` with TypeScript parser support and ignore `.next`, `node_modules`, `test-results`, `playwright-report`, backups.
   - Keep hard errors for syntax, rules-of-hooks, Next core rules. Treat `exhaustive-deps` and `no-console` as warnings unless the user asks for full cleanup.
   - React Compiler rules such as `react-hooks/set-state-in-effect`, `purity`, `immutability`, `static-components`, and `refs` can produce large legacy-code walls. Disable them initially so lint becomes useful instead of impossible.

3. **Do not inject API bearer tokens into browser HTML**
   - Avoid patterns like `window.__AUTH_TOKEN__ = process.env.AUTH_TOKEN` and client fetch monkey-patching.
   - For internal/LAN dashboards, prefer auth disabled if that matches user preference.
   - For public exposure, use a real session/cookie login flow; do not use frontend bearer injection.
   - Remove `?token=` auth support where possible because query tokens leak via logs, history, and copied URLs.

4. **Sanitize untrusted RSS/external links**
   - Any feed URL rendered into `href` should pass a helper that allows only `http:`/`https:` and returns `#` otherwise.
   - Apply the helper both on dedicated news pages and compact trade-context cards.

5. **RSS aggregators need per-feed timeouts**
   - Use `AbortController` per feed, a short timeout such as 3.5s, and `Promise.allSettled`.
   - A single slow feed should not block `/api/news` or pages that depend on it.

6. **E2E coverage must include newly added pages/APIs**
   - Add smoke coverage for new pages immediately: `/funding`, `/portfolio-heat`, `/portfolio-overlap`, `/diagnostics/deployment`.
   - Add request probes for `/api/deployment` and `/api/market-context?symbol=BTCUSDT`.
   - If Docker/LAN auth is intentionally disabled, run E2E with `AUTH_TOKEN=` so tests reflect the deployed mode.

## Verification sequence that worked

```bash
npm run lint
npm run typecheck
npm test
npm run build
bash scripts/redeploy.sh
AUTH_TOKEN= npm run e2e
python3 - <<'PY'
import urllib.request, time
base='http://127.0.0.1:8799'
for p in ['/', '/funding', '/portfolio-heat', '/portfolio-overlap', '/diagnostics/deployment', '/api/deployment', '/api/market-context?symbol=BTCUSDT', '/api/portfolio/heat', '/api/news']:
    t=time.time()
    try:
        with urllib.request.urlopen(base+p, timeout=15) as r:
            print(p, r.status, int((time.time()-t)*1000), 'ms')
    except Exception as e:
        print(p, 'ERR', e)
PY
```

## Audit scoring rule

After this wave, do not claim literal 10/10. Report the verified score and remaining structural blockers:
- upstream dependency advisories that cannot be safely force-fixed
- lint warnings still present
- no real testnet exchange lifecycle E2E
- no mobile visual/Lighthouse QA
- LAN-auth mode vs public-grade session auth
