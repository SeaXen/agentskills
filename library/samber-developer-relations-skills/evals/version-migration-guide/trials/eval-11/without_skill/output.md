v3 adoption %, projected against EOL date. That's headline number leadership need. Build dashboard around it.

## Headline tile (top of dashboard)

1. **v3 share of downloads** — rolling 4-week avg, vs raw weekly (raw too noisy for leadership view)
2. **Weeks to v2 EOL** — countdown
3. **Projected v2 residual % at EOL** — extrapolate current adoption curve forward to EOL date. This is the number that answers "is migration working." Color RAG: green if trending to near-zero, red if flat.

## Panel 1: Adoption curve (npm)

- v2 vs v3 weekly downloads, stacked or dual-line, since v3 launch (6 weeks ago)
- Mark EOL date as vertical line on chart, dotted projection line extending current trend to it
- Break v2 downloads by minor/patch too — shows if stragglers even on latest v2 patch, matters for security-patch planning
- Use `api.npmjs.org/versions/<pkg>/last-week` for per-version split (undocumented but works), not the default aggregate endpoint

## Panel 2: Docs signal (Plausible + thumbs widget)

- Pageviews on migration/upgrade guide, trend over time
- v2-docs vs v3-docs traffic ratio, if docs versioned by URL — shift toward v3 docs = leading indicator, precedes actual download shift by days/weeks
- Thumbs up/down ratio, migration guide only (not site-wide average — dilutes signal)
- Top referrers into migration guide (changelog? blog post? GitHub release?) — tells you which announcement channel actually drives action

## Panel 3: Support risk (Zendesk)

- Ticket volume tagged "migration" / "v2-v3", trend over time
- Breakdown by breaking-change category — tells you which v3 change burns most support time, prioritize doc fixes there
- Avg resolution time, migration tickets vs baseline — slow resolution = migration friction, not just volume
- Pre-migration tickets ("how do I upgrade") vs post-migration tickets ("upgrade broke X") ratio — tells you if pain is deciding or executing

Needs a tag/field on tickets first if not already enforced. Check that before trusting this panel.

## Must state as caveats (leadership will over-read the numbers otherwise)

1. npm downloads ≠ unique users. CI pulls, mirrors, bots inflate count. Treat as trend signal, not headcount.
2. No real usage-by-version data exists today (no telemetry). Download-based % is best proxy available, not ground truth.
3. Zendesk panel only as good as tag discipline. Audit tagging before first dashboard version ships.

## Gap — not buildable from current 4 sources, flag as follow-up

- Anonymous opt-out version-check ping in CLI (most CLIs already have update-check call) — only way to get real active-usage-by-version instead of download proxy. Separate instrumentation ask, not blocking dashboard v1.
- One-question "why haven't you migrated" prompt for v2 users (deprecation banner + link) — direct blocker signal, cheaper than inferring from tickets.

Next: pull `api.npmjs.org/versions/nettlefold/last-week` now, confirm v2/v3 split actually resolves before building panel 1 on it.