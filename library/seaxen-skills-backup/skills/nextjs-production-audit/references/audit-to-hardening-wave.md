# Audit-to-hardening wave lessons

Use when a user asks to turn a Next.js trading/dashboard app from an audit finding list into a higher score, e.g. "make it 10/10".

## Operating posture

- Do not claim literal 10/10 after one wave. Say the honest new rating and what still blocks 10/10.
- Fix P0 safety first, not cosmetic issues first.
- Keep the work scoped to the app root and verify repo + live deployment before reporting.
- For trading apps, treat automation/risk defects as production blockers even when UI/build/tests pass.

## Good first hardening wave

1. Add regression tests for audit findings before patching.
2. Centralize order/request normalization:
   - reject zero/negative/NaN/infinite quantity,
   - reject invalid limit price,
   - reject invalid SL/TP,
   - strip or ignore client-supplied trusted risk inputs such as equity and daily limit.
3. Ensure every automated execution path checks a server-side risk gate:
   - manual order route,
   - signal/webhook direct execution,
   - signal rules,
   - DCA bot,
   - grid bot,
   - position manager.
4. Fail closed on automation config:
   - no fallback to first exchange when configured exchange is absent,
   - no fallback default order size when sizing fails,
   - no place-order rules unless auto-trading is explicitly enabled.
5. Remove dangerous default automation rules. Do not auto-register live positions with percentage-looking values unless units are explicit and validated.
6. Clamp partial close quantities to live position size and include position side in in-memory keys.
7. Fix high-confidence small correctness bugs found during audit, such as RSS CDATA URL cleanup.
8. Keep build-time and runtime side effects separate. `next build` must not start schedulers, bots, exchange sync, alerts, snapshots, or position management.
9. Harden deployment metadata and Docker packaging:
   - exclude `.env`, `data/`, DB files, backups, keys, test reports from build context,
   - avoid world-writable data directories,
   - inject app version, framework version, git SHA, build time into the image.
10. Apply quick accessibility wins only after safety is under control: skip link, one page-owned `h1`, main landmark.

## Verification pattern

Run and report real outputs:

```bash
npm run typecheck
npm test
npm run lint
npm run build
npx playwright test --reporter=line
```

Then deploy only if the user asked for action and container state is safe:

1. Inspect compose, mounts, network, restart policy, health.
2. Backup persistent data before recreate if persistent state exists.
3. Use the project redeploy script or compose path, not ad-hoc `docker run`.
4. Wait for Docker health.
5. Probe live pages/APIs and browser console.

Minimum live probes:

```text
/
/dashboard
/trade
/positions
/api/health
/api/deployment
/api/news
/api/risk/status
```

## Reporting after hardening

Include:

- exact live URL,
- files changed,
- safety defects closed,
- verification table,
- deployment/container health,
- remaining blockers to 10/10.

Do not hide unresolved findings behind a successful build. A trading dashboard with unresolved automation/idempotency/analytics correctness gaps is not 10/10 even if all tests pass.
