# TradingX automation safety hardening pattern

Use this when a trading Next.js app has several independent order-placement paths: manual orders, webhooks/signals, signal rules, DCA/grid bots, and position-management automation.

## Core pattern

1. **Create a central order execution service**
   - Accepts normalized `PlaceOrderRequest`.
   - Revalidates finite positive qty/price/SL/TP server-side.
   - Calls the central risk gate by default.
   - Allows bypass only for explicit `force + reduceOnly` exits.
   - Delegates to `adapter.placeOrder()` only inside this service.

2. **Wire every order path through it**
   - Manual `/api/orders`.
   - Direct signal auto-trading.
   - Signal-rule `place_order` actions.
   - DCA bot orders.
   - Grid bot orders.
   - Spot position-manager protective/partial exits.

3. **Add focused regression tests first**
   - Client cannot weaken risk gate with `equity` / `limitPct`.
   - Invalid qty/limit price rejected.
   - Signal rules cannot place orders unless automation is explicitly enabled.
   - Central service blocks adapter call when risk gate blocks.
   - `force + reduceOnly` may bypass risk gate for exits only.

4. **Add in-process tick locks for interval automation**
   - Tiny `withRunLock(key, fn)` helper using a module-level `Set`.
   - Wire scheduler sync, DCA tick, grid tick, and position-manager tick.
   - This prevents overlapping interval executions in a single Node process.
   - Be explicit that this is not a distributed lock; multi-instance deployments need DB/advisory locks.

## Data integrity fixes that pair well with this wave

- Replace SQLite `INSERT OR REPLACE` for trade upsert with `INSERT ... ON CONFLICT(exchange_id, id) DO UPDATE` so related side data is not deleted/reinserted.
- When saving position snapshots, write zero-size snapshots for previously-open positions absent from the latest exchange snapshot; otherwise stale positions can appear open forever.
- Avoid low silent analytics caps; if a helper caps rows, make the cap high and explicit.

## Webhook SSRF guard pattern

For user-configured outbound webhook URLs:

- Require `https://`.
- Reject embedded credentials.
- Reject localhost, `.local`, `.lan`, `.internal`.
- Reject private/loopback/link-local/reserved IPs.
- DNS-resolve hostnames before saving or delivery; reject any private resolved address.
- Revalidate again immediately before `fetch()` to reduce stale-DNS risk.
- On GET/config read, detect and clear legacy unsafe stored URLs rather than continuing to display them as active.

## Analytics correctness quick wins

- Do not generate synthetic market series when an adapter lacks kline data; return empty/helpful state.
- Compute correlations on returns, not raw price levels.

## Dirty-worktree triage before committing a safety wave

When inheriting a large uncommitted hardening batch, do **not** blindly `git add -A` even if the user says "do".

1. Inspect intent first:
   - `git status -sb`
   - `git diff --stat`
   - `git diff --name-only`
   - focused `git diff -- <critical files>` for order paths, automation paths, webhook/security paths, Docker/deploy files.
2. Read any new core files fully before trusting them:
   - central order executor
   - input normalizers
   - URL/SSRF guards
   - run locks
   - new regression tests
3. Run a secret scan on the diff before staging:
   - API keys, tokens, private keys, `.env`, DB URLs, hardcoded passwords.
4. Check API signature changes for all callers. Example: if `setWebhookUrl()` becomes async, search every `setWebhookUrl(` caller and ensure route handlers await it while React state setters are unrelated/local.
5. Commit only after strict gates and a focused diff review prove the batch is coherent.

## Docker/deploy hardening that pairs with this wave

- `.dockerignore` should exclude `.env`, `.env.*` except `.env.example`, `data/`, backups, Playwright artifacts, coverage, private keys, SQLite DB/WAL/SHM files.
- Build args should carry `BUILD_SHA`, `BUILD_TIME`, app version, and Next version into runtime diagnostics.
- Prefer restrictive `/app/data` permissions (`750`) over `777` in the image; host bind-mount ownership still has to be correct.
- After commit, redeploy so `/api/deployment` SHA matches `origin/main`; stale live SHA means the app is not actually upgraded.

## Verification bundle

After this wave, run and report exact outputs:

```bash
npm run lint
npm run typecheck
npm test
npm run build
AUTH_TOKEN= npm run e2e
```

Then redeploy safely and live-probe:

```bash
bash scripts/redeploy.sh
curl -fsS http://127.0.0.1:8799/api/health
curl -fsS http://127.0.0.1:8799/api/deployment
curl -fsS http://127.0.0.1:8799/api/notifications/webhook
curl -fsS http://127.0.0.1:8799/api/scheduler/status
curl -fsS http://127.0.0.1:8799/api/market-context?symbol=BTCUSDT
```

Also run Playwright smoke after the live redeploy and verify browser console errors are zero.

## Honest scoring

This wave materially improves trading safety and security, but do not claim 10/10. Remaining blockers usually include distributed locks, idempotency/ledger, real fill reconciliation, secret-manager backing, public auth posture, and dependency CVEs outside the app's direct control.
