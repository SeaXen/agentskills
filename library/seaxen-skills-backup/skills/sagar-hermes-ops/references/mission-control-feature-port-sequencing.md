# Mission Control feature-port sequencing

Use this when extending the built-in Hermes Mission Control tab by borrowing ideas from third-party dashboard repos.

## Durable pattern

Prefer **incremental feature-porting into the built-in Mission Control** over installing or renaming a third-party clone when:
- the upstream repo collides on plugin identity/path
- the upstream frontend bundle is broken or incomplete
- the built-in Hermes Mission Control already has a working runtime surface

## Good feature order

For Dr. Sagar's Hermes workflow, the highest-value low-risk order proved to be:
1. config snapshot + redaction
2. snapshot diff
3. health + telemetry + session stats
4. activity timeline + operator notes + checklist
5. mission telemetry + workflow radar + cron health + top skills

This order matters because each step builds naturally on existing safe surfaces before adding denser operator views.

## Verification discipline

For each feature-port pass:
1. patch the shipped `dist/` bundle minimally
2. extend/update smoke tests first or alongside the patch
3. run `node --check` on the dashboard bundle
4. run the focused pytest plugin tests
5. verify live in the browser, not just by file diff

## Common regression to watch for

A later redesign can accidentally **drop an earlier analytics block** while leaving the helper state/computed values in the bundle.

Symptoms:
- helper variables like `analyticsDaily`, `topSkills`, `modelLeaders`, or `cronHealth` still exist
- `getAnalytics(7)` / `getModelsAnalytics(30)` still run
- but live page text no longer contains `Mission telemetry` or `Workflow radar`

Fix pattern:
- compare the current `dist/index.js` against a working backup or earlier bundle
- restore the analytics/radar render block
- keep the newer surrounding UI intact
- re-run live browser verification after patching

## Frontend time formatting pitfall

Hermes dashboard helper `timeAgo(...)` expects epoch seconds, not raw ISO datetime strings.

If dashboard data returns ISO strings like:
- `next_run_at`
- `last_run_at`
- `previous_generated_at`

convert them first:
```js
timeAgo(Math.floor(Date.parse(value) / 1000))
```

Otherwise the UI may render nonsense such as `NaNd ago`.

## Why this fits Mission Control

- compact
- scannable
- low-risk
- backed by existing Hermes SDK calls when possible

Do not jump straight to heavyweight backend analytics or big chart libraries when compact meters/cards already answer the operator question.
