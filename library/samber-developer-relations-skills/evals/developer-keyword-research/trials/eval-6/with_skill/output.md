# Nimbus Ledger keyword map — pull order and map shape

## Pull order

1. **Sentry error telemetry** (tier 4) — full year, since private beta. Export error-code counts by frequency and by release trend.
2. **npm download trend** (tier 6) — near-free. Sizes population, gives context for why tiers 1-3 are thin.
3. **Docs-search logs** (tier 2) — ~40 queries lifetime. Read all of them, zero-result ones first. Corpus small enough to read whole, no sampling needed.
4. **Support tickets** (tier 3) — 11 total, ever. Read all.
5. **Search Console export** (tier 1) — pull anyway, even with only 6 impressed queries. Join query to landing page, check for split pages.
6. **Public Q&A / forums** (tier 5) — search product name, "double-entry ledger API," known competitor names.
7. **Autocomplete / related-search harvest** (tier 7) — near-free. Supplies phrasing the internal sources are too thin to show.
8. **Keyword-tool volume** (tier 8) — tiebreaker only, catch a category term internal signals missed.

Parallel, not a tier: find whoever fielded pre-sales or design-partner questions during beta/GA and get their repeated-question list. No sales/solution-engineer log confirmed yet — biggest blind spot for the company-adoption set.

## Why Sentry jumps the queue

Normal harvest order ranks tier 4 last — it usually costs a week of borrowed engineering time. Skill overrides that when the product is too young for a support queue to have volume, or the map turns out error-heavy. 11 tickets ever and 40 docs queries ever is exactly that trigger: the cheap tiers are watching an audience that hasn't generated signal yet. Sentry, running since private beta, is the only source with real depth.

Bonus: Sentry still counts as first-party (tiers 1-4) for the map's 70% evidence floor. Leaning on it doesn't cost you the threshold — it's what saves it.

## Scope (fill this in before the first pull)

- **Axes (languages/frameworks/runtimes/deployment modes):** unknown — need from you before generating the task/reference candidate matrix (step 5). Don't guess these.
- **Adoption mode:** both. Company-adoption gets its own target count regardless of ratio ranking — double-entry ledger APIs are compliance-sensitive infra, evaluated by a champion checking audit trail, idempotency guarantees, data residency, before anyone signs.
- **Owned surfaces:** docs site (has search logging). Confirm blog, changelog, repo as targets.
- **Sources used:** Sentry (tier 4), npm (tier 6), docs search (tier 2), support tickets (tier 3), Search Console (tier 1), public Q&A (tier 5), autocomplete (tier 7), keyword tool (tier 8, tiebreak only).
- **Sources unavailable/unconfirmed:** issue-tracker question labels, community archive, sales/solution-engineer question list.
- **Pass-threshold note:** 70% first-party floor likely holds without lowering — Sentry supplies bulk of ranked evidence. State this reasoning in the shipped map, don't treat it as an exception.

## Map shape, section by section

**Ranked clusters** — expect a short list, single digits. Majority Error-string family, sourced from Sentry, evidence mostly Measured (hard counts). A high-frequency Sentry cluster with zero matching ticket or docs-search hit still belongs — that's the silent-failure case tier 4 exists to catch. 1-2 Task how-to clusters only if the 40 docs queries or 11 tickets touch first-hour tasks (create ledger, post a balanced transaction, idempotency key use, check balance) — assumption, confirm the real task list. No evidence on a task candidate → parking list, not the map.

**Company-adoption set** — currently unfillable with confidence. Fast substitute: log this week's most-repeated pre-sales/beta questions as User-provided evidence, tag the source, don't wait for a formal sales-question export that may not exist.

**Fix first** — run the cannibalization check even on 6 GSC rows. Cheap, catches an accidental split early.

**Do not target** — expect concept queries owned by general double-entry bookkeeping docs/textbooks ("what is double-entry accounting"), and any Sentry cluster whose real fix is a product or error-message change, not a page.

**Backlog** — task-how-to candidates lacking evidence go here, dated, not deleted. Docs-search and GSC corpora are 7 weeks old — re-pull next quarter once they've grown, don't treat today's near-zero as permanent.

## Next action

Export Sentry error-code counters by frequency, last 12 months, today.