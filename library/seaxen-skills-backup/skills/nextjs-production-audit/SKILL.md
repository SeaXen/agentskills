---
name: nextjs-production-audit
description: Audit a Next.js/React trading or dashboard app before rating or declaring it production-ready. Covers repo-vs-live deployment drift, quality gates, live HTTP probes, security risks, and prioritized sector ratings.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [nextjs, audit, production-readiness, deployment, security, rating]
    related_skills: [requesting-code-review, static-site-performance-optimization, feature-building]
---

# Next.js Production Audit

Use this when the user asks for a final audit, score out of 10, production-readiness review, feature-gap review, or “what should we improve?” for a Next.js/React app.

## Core rule

Separate **source/repo quality** from **live deployed app quality**. A repo can build cleanly while the running Docker/container/host is stale. If they differ, give two scores.

## Audit workflow

1. **Inventory the repo**
   - Git status, last commits, remote sync.
   - Count pages, API routes, components, tests, approximate LOC.
   - Identify newly added routes/features that must exist live.

2. **Run repo quality gates**
   - `npm run typecheck`
   - `npm test`
   - `npm run build`
   - `npm run e2e` if present.
   - Try lint, but treat broken lint config as a finding, not as proof the app is bad.
   - Inspect build output for worker startup. Build/static-generation processes must never start exchange sync, bots, alerts, snapshots, or position management.

3. **Probe the live runtime**
   - Detect whether a process/container is already serving the app.
   - Probe representative pages and APIs with real HTTP status and timings.
   - If auth exists, use headers without printing secrets.
   - Include newly added pages/APIs in probes, not just old smoke-test routes.

4. **Check deployment freshness**
   - Compare repo HEAD vs deployed behavior.
   - Stale deployment signal: repo build includes a route but live returns 404.
   - Recommend adding a diagnostics/deployment page with git SHA, build time, image ID, and route presence.

5. **Security and trading-safety pass**
   - Look for frontend token injection, permissive query-token auth, unsanitized external `href`, `innerHTML`/`dangerouslySetInnerHTML`, hardcoded credentials, missing server-side validation.
   - For LAN-only dashboards, distinguish practical LAN risk from public-exposure risk.
   - Enumerate every direct exchange execution call. Verify manual orders, signals, webhooks, DCA/grid workers, schedulers, and position managers all pass through the same server-owned risk and audit service.
   - Trace units end to end: percent vs absolute price, percent vs base quantity, quote notional vs base quantity, and intended order vs actual fill.
   - Check automation for overlapping ticks, durable locks/idempotency, restart-safe state, fill reconciliation, and fail-closed exchange selection.

6. **Runtime/deployment pass**
   - Docker health, restart policy, memory/CPU, logs.
   - Confirm container serves current artifact; do not assume because `git push` succeeded.

7. **Sector rating report**
   Rate concrete sectors separately: product scope, trading workflow, risk controls, analytics, market data, exchange integration, automation, UI/UX, performance, reliability, security, testing, maintainability, DevOps, documentation.

## Reporting format

Lead with the verdict:

- Repo/source rating: X/10
- Live deployed rating: Y/10
- Reason for any gap.

Then provide:
- verification receipts,
- sector score table,
- P0/P1/P2 issues,
- feature gaps,
- recommended next order.

## Pitfalls

- Do not give one “final” score if the live deployment is stale.
- Do not let passing `next build` imply production deployment is updated.
- Do not print auth tokens while probing APIs.
- Do not call browser smoke tests comprehensive if they omit newly added routes.
- Do not run destructive redeploys unless the user asked for action, not just audit.

## References

- `references/tradingx-audit-lessons.md` — concrete lessons from a TradingX audit: stale Docker detection, Next 16 lint caveat, frontend token injection, and RSS/news safety issues.
- `references/trading-automation-safety-audit.md` — deep checklist for centralized execution, unit semantics, automation idempotency, exchange reconciliation, analytics honesty, and build/runtime separation.
- `references/audit-to-hardening-wave.md` — how to convert audit findings into a safety-first hardening wave with regression tests, Docker/live verification, and honest post-fix rating.
