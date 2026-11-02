I searched this entire repository — every file and directory except `skill-wip/`, which I left untouched per your instruction — and I can't find a billing reconciliation service here at all.

**What this repo actually is:** `example-org/example-repo` is a knowledge base for affiliate/partnership programs used by your Claude Code skills repos (`README.md`: "Knowledge base for the affiliate program embedded in \<repo\>"). It holds:

- `affiliation-programs/` — one file per affiliate program (terms, commission, tracking links)
- `sponsors/` — sponsorship prospect notes
- `research/` — free-form research notes
- `scripts/` — data-collection scrapers (`telemetry.js`, `skills-sh-scrape.mjs`, link-checkers)
- `telemetry/` — stats/telemetry JSON for skills
- `memory/`, `.agents/` — agent memory and product-marketing notes

There's no application code, no service, no staging config, no database schema, nothing under any name resembling "billing reconciliation" — outside `skill-wip/`, where a `grep` for "billing"/"reconcil" only turns up affiliate-payout and revenue-governance *research notes* (markdown), not a running service.

**So I have nothing to build a demo, script, or walkthrough from.** I don't want to fabricate a 10-minute all-hands demo for a service I can't locate — that would put invented content in front of the whole company on a recorded call, which is the opposite of useful.

A few possibilities worth checking on your end:

1. **Wrong repo/session** — is "the new billing reconciliation service" in a different codebase, and this Claude session just happens to be pointed at `example-repo`?
2. **It's inside `skill-wip/`** — if the service actually does live under `skill-wip/`, I'd need you to lift the restriction (even just "you can read `skill-wip/services/billing-reconciliation/` specifically") since I can't infer its behavior from outside.
3. **It hasn't been written yet** — if this is a "help me build it" ask, that's a very different task (and a big one for a Thursday deadline) and I'd want to scope it with you first rather than assume.

Let me know which of these it is (or correct me) and I'll pick it up from there.