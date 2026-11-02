## Verdict first

Don't write 30 new entries yet. Fix 2 rotting things in existing 22 first, and diagnose why 190 searches miss pages you already have. Writing more pages on top of a findability problem just triples the pages nobody finds.

## Do this week — mechanical, hours not days

⚠️ **1. Dead escape hatch, all 22 entries.** #support-legacy archived July, every entry still points there. Per skill's maintenance trigger: "escape hatch channel closes → fix every entry pointing at it; dead escape hatch converts a helped reader into an angry one." Same string in all 22 files — batch find/replace, not a rewrite. Need: what channel/form replaced #support-legacy? Confirm, then patch all 22 same day.

⚠️ **2. Six zombie known-issues entries, fixed in 5.0 (June).** Named failure mode: "entries for bugs fixed three releases ago." 3 months overdue. Per Step 10: bug ships fix → move entry into changelog, delete it, add version note ("Fixed in 5.0"). Not archive — delete. Do this for all 6 now.

Both are why ticket volume reads flat: readers hitting a dead escalation link file fresh tickets instead of using "Still stuck," and unretired known-issues entries make 5.0-fixed bugs look unresolved. That alone can eat your "down 4%, noise" signal.

## Diagnose before scaling — this is the real quarterly finding

Flat ticket volume on documented errors is not "pages didn't help." Skill's own line: "the same clusters reappearing unchanged means the entries are not being found — a discoverability problem, not a volume problem." 190 zero-result searches for strings you have pages for is the same signal on the search surface. Metric target is zero; nonzero usually means the string isn't verbatim on the page.

Audit, per entry, before writing anything new:

1. Pull the 190 query strings. Match each against your 22 pages: is the string verbatim in title, first heading, and body?
2. Check indexability: login wall, client-side-only render, URL that moved without redirect.
3. Check the emitted product string against the page title — one typo or reformatting and match rate halves.
4. Re-run `error-cluster.py` on this quarter's tickets/issues + the docs-search log. Compare against the original 22 clusters — are they still top, or did new ones spike?

## On the writer's 30-entry proposal

Reframe the ask, don't reject the writer's instinct. The skill's own baseline is coverage of the ranked queue, not a headcount: 80% of top 20 clusters per cycle. "30" is arbitrary until it's checked against that queue and against real writing/verification hours available — ask the writer what those hours are, that number gates everything else.

Sequence: fix escape hatch + zombies (mechanical) → run the audit above → re-cluster → merge writer's 30 candidates into that fresh ranked queue → run Step 3's document-vs-fix gate (any cluster hitting several postmortems gets escalated as a product fix, not a page) and the self-serviceability gate (drop what a reader can't act on alone) → cut to what capacity funds. Real number after that cut is very likely under 30, and some of the "30" may turn out to be the same 22 clusters worded differently — that's a discoverability fix, not a new page.

## Quarter plan

1. Week 1: escape-hatch batch fix + known-issues retirement. Both ship this week.
2. Week 1–2: zero-result-search audit, fix what's found (title/verbatim/indexing defects on the existing 22).
3. Week 2: re-run cluster script on tickets + issues + docs-search log since last pass. Fresh ranked queue.
4. Week 3: merge with writer's 30 candidates, apply ranking + document-vs-fix gate + self-serviceability gate, cut to capacity. Agree the number with the writer, write it down.
5. Week 3+: write/verify the cut list at normal cadence — 6 parts each, reproduced before publishing, no exceptions.
6. End of quarter: re-run cluster pass again. Track cluster coverage, ticket-volume-per-covered-error, zero-result-search count — not raw deflection rate.

## Confirm before I lock this in

- Replacement channel/surface for #support-legacy (blocks item 1).
- Does an AI assistant or search bot answer from these docs? If yes, re-index after the escape-hatch batch edit and the known-issues deletions — corrected pages served from a stale index is its own failure mode.
- Writer's actual writing+verification hours this cycle — sizes the real cut in step 4.

Next: tell me the replacement support channel so item 1 ships today.