Using the `developer-keyword-research` skill to answer this. Below is the actual deliverable — scope, refusals, and the plan that replaces the 128-cell matrix.

---

# Keyword map: Antimatter Streams client/task docs — Q(next 2) scoping pass

## Scope

- **Product**: Antimatter Streams, managed Kafka-compatible broker.
- **Officially supported client axis**: Java, Go, Python only. Rust, Ruby, PHP, Elixir, .NET ship no client — they are **not a valid axis** and are refused below, not deprioritized.
- **Version axis**: v2, v3 — but only as a per-cluster flag, not a blanket multiplier. Only 6 of 47 error codes have version-dependent message text; nothing stated shows the 8 proposed tasks behave differently across versions.
- **Task axis, as given**: produce, consume, exactly-once, schema registry, dead letter, consumer groups, ACLs, compaction. This mixes two different query families (task how-to and evaluation/trust) that this skill routes to different surfaces — treated separately below, not as one column.
- **Adoption mode**: both, unresolved which dominates — this run can't split them because the one input that would tell you (solutions-engineer questions) hasn't been captured as data yet, only characterized qualitatively ("nothing like this list").
- **Owned surfaces**: docs site confirmed (has search logs). Blog/repo/changelog status not stated — ask before scoring anything as "update vs. new."
- **Sources used**: one docs-search figure ("antimatter timeout," 290 searches/90d, Measured, intent unresolved). The error catalog itself (47 codes, 6 with v2/v3 text diffs) — code existence is Measured, but occurrence/search frequency per code is not supplied, so it's a checklist, not evidence.
- **Sources unavailable this run** (stated per this skill's rule, not guessed): first-party query-console export (tier 1) — N/A. Full docs-search log including zero-result queries (tier 2) — only one query given. Support tickets / issue tracker (tier 3) — N/A as data, though the SE statement is a strong qualitative signal something's missing. Error telemetry counts per code (tier 4) — N/A. Q&A/forums (tier 5), ecosystem counters (tier 6), autocomplete (tier 7), keyword-tool volume (tier 8) — all N/A.
- Because essentially 0% of candidate clusters currently carry countable tier 1-4 evidence, the 70% floor is **lowered to 0% and stated here explicitly** — this run is a Scope + Do-not-target + Fix-the-inputs pass, not a ranked map. Treat what follows as gating, not as a page count to hand to writers.

## Ranked clusters

Empty. No candidate has evidence yet — "a candidate with no evidence goes to the parking list, not the map." Filling this table is the point of Immediate actions, below.

## Company-adoption set

Also empty, but flagged: ACLs and cross-version schema-registry behavior read as champion/compliance-shaped questions, not individual-developer-shaped ones. When the SE question list comes in, expect it to populate this table, not the docs-search table — SEs are exactly the source this skill names for "limits, permissions, compliance and migration questions [that] rarely reach public channels."

## Fix first

N/A this pass. Step 2 (screen what you already own) needs a page inventory or sitemap crawl that wasn't supplied — check before anyone writes a "new" page that might already exist and just need a v3 update.

## Do not target

- **Rust, Ruby, PHP, Elixir, .NET × anything.** No shipped client. A worked example against an SDK that doesn't exist can't be kept correct, and a broken sample costs more credibility than the traffic is worth. This alone removes 5 of 8 language columns before any evidence gate runs — 62 of the 128 literal cells (8 langs × 8 tasks × 2 versions = 128, not quite "several hundred," but already too large before this cut).
- **41 of the 47 error codes, forked by version.** Message text is identical v2/v3 for these; the skill's own recipe crosses an error catalog with versions "only where the message text actually changed." Ship one canonical page per code, note both versions apply, don't fork.
- **Any of the 8 tasks phrased as generic Kafka concepts** ("what is a consumer group," "what is exactly-once semantics") where Antimatter doesn't diverge from stock Kafka behavior. Owned by Apache Kafka's/Confluent's own docs — a reference lookup this skill says to refuse outright. Antimatter only has a winnable page where its *managed* implementation differs (e.g., how ACLs are provisioned on the control plane), not on the underlying concept.
- **"antimatter timeout," as currently scoped.** Can't be routed to one surface yet — see Immediate action 3. Guessing which intent it is and shipping a page against the wrong one is exactly the intent-collision trap this skill names using this literal example.

## Backlog

- Rust/Ruby/PHP/Elixir/.NET matrix: parked indefinitely, not "next quarter" — reopen only if one of these ships an officially supported client, and then only as one validated column, not a bulk re-add of all five.
- Full 8-task matrix for Java/Go/Python: parked pending the task-inventory check in action 2 below and real per-cluster evidence.

## Immediate actions — do these, not the matrix

In pull-efficiency order:

1. **Get the solutions engineers' actual question list, verbatim and dated.** This is the single highest-signal, lowest-cost action available: the people closest to real demand already told you the proposed list doesn't match what they field. That list — not the matrix — is the real task inventory. This is exactly the "sales-visible questions missing" failure mode this skill calls out by name.
2. **Pull the real docs-search export**, not just the one figure: top queries by volume, zero-result queries, and queries where the top click isn't the actual answer. Validate that "produce, consume, exactly-once, schema registry, dead letter, consumer groups, ACLs, compaction" is even the right task list, rather than one someone assembled by intuition.
3. **Disambiguate "antimatter timeout" before routing it anywhere.** Check what the current top-clicked result actually answers. If nothing does, this is worth a five-minute look at a handful of the underlying support/search sessions rather than a guess — it may split into two pages (a connection-timeout error entry and a `request.timeout.ms`-style config reference), or it may collapse into one. Don't build either until you know.
4. **Pair the 47-code error catalog with real occurrence data** — telemetry counts per code and/or ticket mentions, trailing 90 days minimum — before writing a single error page. Right now the catalog tells you the codes exist, not which ones anyone actually hits. Frequency × time-to-resolve × self-serviceability is what ranks them, per this skill's normalization step, and none of those three are known yet.
5. **Re-run steps 4-9 of this skill for real** once 1-4 land: normalize and cluster, expand only Java/Go/Python cells that clear the evidence gate, name the incumbent for each surviving cluster (own stale page, dead forum thread, or upstream Kafka docs — refuse the last), route each cluster to exactly one surface, then score by outcome-per-page-hour and cut to whatever the docs team can ship *and keep current* in two quarters — a number nobody has stated yet (interview Q7) and that should set the real page count, not "one cell per combination."

## Why not build the matrix as specified

Four independent reasons, any one of which is disqualifying on its own:

- **Axis violation.** 5 of 8 languages have no client. This is the textbook "matrix explosion" failure mode — an ungated cross-product, not a keyword map.
- **Zero evidence.** Every one of the ~128 literal cells would be invented, not observed. This isn't a low-volume problem a keyword tool could rescue (per the 93%-below-10-searches finding this skill leads with) — it's zero first-party evidence for effectively 100% of cells, which no tool fixes.
- **Wrong granularity on the version axis.** Only 6/47 error codes actually differ v2→v3; blanket-versioning everything doubles maintenance on content that's mostly identical.
- **The two data points you do have both point away from this matrix.** The SEs — the people who field real questions — say this list isn't it. The one search figure you have is too ambiguous to route anywhere yet. Both are reasons to go collect signal before laying out pages, not reasons to fill in placeholders while waiting.

"Owning the space" is a legitimate compounding-asset goal, but it's won by clusters that clear a winnability and evidence bar and compound over several quarters — not by cell count. A generated page nobody searches for and nobody else answers either doesn't help you "own" anything; it just sits there needing a re-test on every SDK or protocol release.

## Pass threshold (stated per this skill's requirement)

This pass fails on purpose — it's a scoping-and-refusal pass, not a finished map:

1. Evidence per ranked keyword — N/A, nothing ranked yet.
2. 70% tier 1-4 floor — floor explicitly lowered to 0% and stated above.
3. No cluster ranked on tool volume alone — trivially true, no tool volume used at all.
4. One canonical surface per cluster — N/A, no clusters yet.
5. Do-not-target list non-empty — **pass**, four refusals stated above.
6. Sort stated, demotions named, company-adoption set filled independently — N/A, deferred pending real data.

Re-run this threshold after immediate actions 1-4 land data — that run is the one that should hit all six and produce the actual ranked page list.