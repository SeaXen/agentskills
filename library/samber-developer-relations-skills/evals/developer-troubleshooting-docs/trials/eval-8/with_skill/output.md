**Split this into two projects. Don't run them as one.** Different owners, different risk, different pace. Bundling them means both slip together.

## Problem 1: the codes reference

**Don't assign 140 pages to 2 writers.** Wrong shape of work. Reasons below.

### Why "one page per code" is the wrong frame

- 3 declaration sites (`internal/errs/codes.go`, TS enum, Confluence) means drift already happened — Confluence stuck at 90 codes proves it. Writing pages against the current mess just encodes the drift into a fourth place.
- Not every code fires in production. Some are dead, some fire never, some fire constantly. Writing 140 pages with equal effort ignores that — same mistake as "one page per ticket" (skill's own failure mode: cluster first, then write).
- 2 writers × 2 weeks = ~7 pages/writer/day. Each entry needs: reproduce the failure, run the fix from a cold state, get a second person to follow it, record a verification signal. 7/day does not fit that bar. Entries shipped without it are guesses in a trustworthy font.

### Sequence instead

1. **Fix the source-of-truth problem first — this is an engineering ticket, not a writing task.** Pick one canonical file (`internal/errs/codes.go` is the obvious pick, it's what the product actually emits). Generate the TS enum and the docs table from it. Same pattern as PostgreSQL (`errcodes.txt` → C header + SGML docs) and Rust (`rustc_error_codes` → error index + `--explain`). **Retire the Confluence page once the generator ships** — a hand-maintained fourth copy just re-creates the drift you're fixing. Owner: whoever owns `internal/errs`, not the docs team. Do not let this get folded into "the docs project."
2. **Pull real evidence before ranking anything.** Error telemetry (counts per code, since last N releases) plus one reported source (tickets/issues). Telemetry alone tells you which of the 140 codes anyone actually hits — likely a long tail, a small set doing most of the volume. Run:
   ```bash
   python3 scripts/error-cluster.py tickets.csv issues.jsonl --min-count 3 --top 40
   ```
   from the skill's `scripts/` dir, or by hand over the top ~50 tickets if no export access.
3. **Gate each code: page vs. fix.** Any code that's a pure defect (message doesn't say what to do, cause is a bug nobody should hit) gets escalated to product, not documented — documenting it makes it permanent.
4. **Split the 140 into two treatment tiers, not one:**
   - **Tier A — codes with real hit volume, reproducible:** full 6-part entry (message, applies-to, cause, fix, confirm, still-stuck). Writer time goes here. This is what your 2 writers actually work on.
   - **Tier B — everything else:** thin, generated stub straight from the source file (message + applies-to, no elaborated fix) — same idea as Rust's index, zero writer-hours, output of step 1's generator.
5. **Size Tier A against real capacity, not 140.** Skill's own baseline: 80% of the top 20 clusters in a cycle. Negotiate that number with your writers against the 2-week budget — don't inherit 140 as the target by default.

### Before writers touch anything, get answers to

- Signal sources reachable: tickets, issues, telemetry, docs search logs, AI-assistant unanswered-query log?
- Self-serve audience, contract-bound, or both? (Changes sourcing and which failures matter.)
- Is this a one-off pass or a standing capture habit? (If standing, worth also wiring a KCS-style capture field into the ticket tool so this doesn't rot again.)
- Who owns `internal/errs/codes.go`, and will they take the generator ticket?

### Named frameworks behind this (so it's auditable, not opinion)

KCS (capture/evolve loop) for the sourcing step. OASIS DITA `<troubleshooting>` for the entry's condition→cause→remedy shape. Nielsen heuristic 9 for the prose bar. Google SRE postmortem practice for the "page is an interim measure, not a fix" gate.

## Problem 2: Hugo → Docusaurus

**Run this fully separate. Different track, different owner, no shared deadline.**

- Migrating now means migrating pages you're about to regenerate — double work, and a generator that emits Hugo shortcodes today would need rewriting for Docusaurus anyway.
- Sequence: ship the generated catalog on the current Hugo site first (source-of-truth fix has a permanent payoff regardless of theme). Migrate the site after content stabilizes.
- This isn't a call this skill scopes — it's a docs-infra decision. If you want, `developer-docs-structure-audit` is closer to that question; this skill stops at page content and findability.

## What "done" looks like in 2 weeks

1. Generator shipped, Confluence retired, TS enum + docs table both build from `codes.go` (or its successor).
2. Ranked cluster queue from real telemetry/tickets, agreed coverage target (not "140").
3. Tier A entries written, verified (reproduced, fix executed cold, second-person check), Tier B stubs auto-generated.
4. Coverage target + maintenance trigger stated: a release that changes a code's text/cause updates the entry in that release, since it's now generated, this should be close to automatic.

**Next: get the codes.go owner to commit to the generator ticket — that unblocks everything else.**