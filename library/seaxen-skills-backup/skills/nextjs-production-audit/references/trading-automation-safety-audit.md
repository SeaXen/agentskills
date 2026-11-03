# Trading automation safety audit

Use this checklist when auditing a trading dashboard that can place orders manually or through bots, signals, schedulers, or position managers.

## Central execution-path invariant

Enumerate every direct exchange execution call (`placeOrder`, `closePosition`, cancel/replace calls). Verify that every caller passes through one server-owned execution service that enforces:

- global/manual kill switch,
- daily-loss and consecutive-loss locks,
- exchange/account trade permissions,
- positive finite quantity and price,
- maximum notional and leverage,
- symbol/precision validation,
- idempotency key or durable execution claim,
- audit event and structured failure result.

Do not infer safety from the manual order route. Bots, signal rules, webhooks, DCA/grid workers, and position managers frequently bypass it.

## Semantic-unit mismatch checks

Trace configuration values from creation/defaults through persistence to execution. Explicitly verify whether each field is:

- percentage vs absolute price,
- percentage vs base quantity,
- quote notional vs base quantity,
- trigger price vs distance,
- intended quantity vs exchange-reported fill.

A UI/default such as `50` may mean 50% while execution interprets 50 base units. A TP value such as `2.0` may mean 2% while execution treats it as an absolute price. Treat mismatches as critical.

## Automation reliability

Check every timer/cron worker for:

- overlapping async ticks,
- durable lock/lease,
- crash window between order submission and state persistence,
- restart-safe watermarks and partial-fill state,
- hedge-mode keys that include position side,
- actual fill reconciliation before advancing bot progress,
- pagination and overlap/dedup during trade sync,
- fail-closed exchange selection.

An accepted order is not necessarily filled. Intended quantity/notional must not be recorded as executed quantity without reconciliation.

## Data-integrity checks

- Position snapshots must mark positions absent from the latest exchange response as closed.
- Avoid `INSERT OR REPLACE` when rows contain local enrichment; use conflict-aware updates that preserve portfolio/tags/slippage fields.
- Composite identities such as `(exchange_id, trade_id)` must remain fully scoped in update/delete operations.
- Verify analytics queries return every field consumed by calculations.
- Detect silent hard caps where callers request more rows than the database layer permits.

## Analytics honesty

- Correlate timestamp-aligned returns, not raw price levels aligned by array index.
- Never substitute synthetic market data in a production analytic without an unmistakable demo label and explicit provenance.
- Use configured/actual equity baselines rather than hardcoded starting capital.
- Verify duration, MAE/MFE, setup ratings, drawdown, and risk calculations against the real selected columns and complete intended sample.

## Build/runtime separation

Run a production build and inspect output for worker startup messages. Static generation and build-time imports must never start exchange sync, alerts, snapshots, bots, or position management. Background workers need an explicit runtime-only entrypoint.

## LAN no-auth posture

If no-auth LAN mode is intentional, rate it separately from public exposure. Still identify high-impact actions reachable by any LAN process: order placement, close/cancel-all, reset, credential changes, imports, and backup download/delete. Recommend capability protection or trusted-subnet firewalling without forcing full UI authentication.

## Evidence standard

For every critical trading finding, report:

1. configuration/default source,
2. persistence/transport path,
3. execution interpretation,
4. concrete failure scenario,
5. exact file and line references,
6. confirmed defect vs plausible risk.

Do not call an app production-ready merely because typecheck, lint, build, unit tests, and page smoke tests pass. Those gates rarely exercise live automation semantics.