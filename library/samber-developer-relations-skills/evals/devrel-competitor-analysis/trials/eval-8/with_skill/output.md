# DevRel benchmark: Windlass vs Larkspur, Beacontree, Ashgrove

Observed 2026-09-20 · Peer set: Larkspur, Beacontree, Ashgrove · **Windlass column included, not skipped** — a scorecard with only three columns can't produce a gap plan; "ours first" is the skill's own convention (`SKILL.md` § Output shape), and a comparison against nothing has no gaps to sort.

## What changes because of this

1. **The field list is frozen at 20 fields across three surfaces** (Documentation & DX, Open source, Community) — not 40, and not one list for Larkspur and a thinner one for everyone else. A thinner symmetrical table beats a richer asymmetric one (`SKILL.md` step 2): a field only survives if it can be asked, meaningfully, of all four companies. Verdict: **close** — apply this exact list to every future collection pass on this benchmark. Owner: you.
2. **Every quantitative cell in this pass reads "not observable."** Traceability on this benchmark means a source URL and an observation date per cell (100%, this analysis's own bar, not an industry one). Nothing in this conversation carries either — not a single figure, for any of the four companies — so nothing goes in a cell as a value. A guess is a liability; a blank is a finding. Verdict: **close** — the next action is pasting sourced values against this frozen schema, not widening the table. Owner: you.
3. **Collection ran depth-first on Larkspur while Beacontree got one surface and Ashgrove got none** — the reverse of the skill's efficiency order, which runs the cheap rungs (timed quickstart, docs coverage, forge metrics) breadth-first across the whole peer set before any company gets a deep pass. A week of Larkspur depth cannot be compared against zero Ashgrove data no matter how it's tabulated. Verdict: **close** — next session goes to Beacontree's and Ashgrove's rungs 1-3, not further into Larkspur. Owner: you, before the next planning checkpoint.

## Scorecard

One row per observation, one column per company, ours first. Every cell carries a value or **NO** (not observable — no sourced figure exists in this conversation for that cell; see column notes below the table). No cell is estimated.

### Documentation & DX

| Observation | Windlass | Larkspur | Beacontree | Ashgrove |
|---|---|---|---|---|
| Quickstart exists | NO | NO | NO | NO |
| Steps to first result | NO | NO | NO | NO |
| Timed first success (minutes) | NO | NO | NO | NO |
| Payment method required before first result | NO | NO | NO | NO |
| Doc modes present per major feature (tutorial/how-to/reference/explanation) | NO | NO | NO | NO |
| SDK languages, count | NO | NO | NO | NO |
| Languages with their own quickstart (of N) | NO | NO | NO | NO |
| Versioned docs + migration guide per major version | NO | NO | NO | NO |
| Public changelog with a feed | NO | NO | NO | NO |
| Freshness: share of top-10 pages updated in last 90 days | NO | NO | NO | NO |

### Open source

| Observation | Windlass | Larkspur | Beacontree | Ashgrove |
|---|---|---|---|---|
| Releases, last 12 months | NO | NO | NO | NO |
| Median time to first human response (issues/PRs) | NO | NO | NO | NO |
| Change-request closure ratio | NO | NO | NO | NO |
| Elephant factor (fewest orgs producing 50% of activity) | NO | NO | NO | NO |
| Share of merged PRs authored outside the company | NO | NO | NO | NO |
| Community health files present (contributing guide, CoC, templates, security policy) | NO | NO | NO | NO |

### Community

| Observation | Windlass | Larkspur | Beacontree | Ashgrove |
|---|---|---|---|---|
| Primary community venue | NO | NO | NO | NO |
| Median time to first reply | NO | NO | NO | NO |
| Share of questions with no answer | NO | NO | NO | NO |
| Staff share of replies | NO | NO | NO | NO |

**Column notes (why NO, not what it means for the company):**
- **Windlass** — known internally, but not supplied in this conversation. "We obviously know our own numbers" is true and also not the same as those numbers being in this table with a date on them. NO here is not a claim Windlass lacks the capability; it's a claim I wasn't given the figure.
- **Larkspur** — you report roughly 40 collected data points (every doc page, full release history, forum reply times), which almost certainly fills most of the Documentation & DX and Open source rows and several Community rows. None of it was transmitted into this conversation with a source URL or observation date, so none of it can go in a cell without becoming an unsourced guess dressed as a fact. Paste the raw values against these exact 20 rows and they populate directly — no new rows needed.
- **Beacontree** — docs site only. Documentation & DX rows are collectible from what you already have (again, pending the actual values); Open source and Community rows are currently unresearched, not unobservable — those need rungs 3 and 6 run before they can carry anything but NO.
- **Ashgrove** — no collection done. Every row is NO for the same reason, uniformly, until rung 1 starts.

**Two rows deleted rather than left ragged**, per the "delete rather than demote" rule (`SKILL.md` step 2 / § Delete rather than demote):

- *Per-page freshness list* (which specific Larkspur doc page was last touched when) — this is exactly the kind of Larkspur-specific granularity a 40-point week produces, and it has no symmetric equivalent for a company you haven't opened the docs site for. Collapsed into the single aggregate row above ("share of top-10 pages updated in last 90 days"), which can be asked of all four.
- *Full release-by-release changelog* — same problem in the open-source surface. Collapsed into "releases, last 12 months" plus the two forge-health rows, which travel across companies; a scrollable list of Larkspur's tags does not.

Q&A tags, content cadence, events, and hiring signals are **out of scope for this pass**, not demoted to the bottom — nobody has looked at any of those surfaces for any of the four companies, Windlass included, so a row of four NOs each would be four rows of nothing rather than a finding. Per the collection order in `SKILL.md` § Which surfaces to collect first, these sit above the line that a half-day-or-less effort ceiling deletes anyway; pick them up only once rungs 1-3 close out across the peer set.

## Per-surface read

Cannot be written yet. This section compares "what they do that we don't" — with every cell NO, there is nothing on either side of that sentence to write honestly. Writing it anyway is exactly the blank-cell-fabrication failure mode this skill guards against.

## Time-to-first-success

| Company | Minutes | Blocking step |
|---|---|---|
| Windlass | NO | NO |
| Larkspur | NO | NO |
| Beacontree | NO | NO |
| Ashgrove | NO | NO |

No timed run has been reported for any of the four. This is rung 1 in the collection order — cheapest surface, most-felt finding — and none of the described week went to it, even for Larkspur.

## Gap plan

These are process gaps (what's blocking the benchmark itself), not competitive gaps (what a rival does that Windlass doesn't) — the latter needs at least one populated row to exist first. Sorted by impact per unit of cost, highest first.

| Gap | Impact | Cost | Verdict | Owner | Date |
|---|---|---|---|---|---|
| Windlass column has no supplied values | high — no baseline, no gap plan is possible without it | low — you already have the numbers | **close** — supply Windlass figures against the 20 frozen rows | you | before next review |
| Ashgrove has zero collected surfaces | high — blocks any 3-way read | low — rungs 1-3 ≈ 2-3 analyst hours | **close** — run timed quickstart, doc-mode coverage, forge pull | you | next working session |
| Beacontree has Documentation & DX only | medium — one of three in-scope surfaces missing two | low — one forge API pull, one forum sample | **close** — run rungs 3 and 6 for Beacontree | you | next working session |
| Larkspur's 40 points sit outside this conversation | high — richest column is currently the emptiest on paper | low — a paste, not new research | **close** — transcribe existing findings into the 20 rows above | you | before next review |
| A week went to depth on one peer while two peers got none/one surface | medium — already-spent time, can't be recovered | n/a — sunk cost | **counter** — redirect remaining hours to breadth on Beacontree/Ashgrove rather than deepening Larkspur further; the extra Larkspur surfaces (rungs 4 and 6-8) were high-effort rungs the efficiency order runs last anyway | you | this week |

**Starved by this ranking:** the actual competitive gaps (docs coverage, release cadence, community responsiveness) — the ones the benchmark exists to find — sit below every row here, because none of them can be scored without a populated cell on both sides. That's not a demotion the ranking is hiding; it's the direct consequence of finding #2. They return to the table the moment real values land.

## Method and limits

- **Scope of this pass:** Documentation & DX, Open source, Community. Content cadence, Q&A tags, events, and hiring signals are deleted from this pass, not parked — zero collection exists on any of those surfaces for any company, and a row of four NOs is scope creep, not a finding. Re-added once rungs 1-3 close for all four columns.
- **Symmetry and traceability are this analysis's own targets, at 100% each** (`SKILL.md` § Quality bar), not industry benchmarks: every row needs a value or an explicit NO for every company, and every value needs a source URL and an observation date. Both are currently unmet by construction, since no sourced value exists yet for any cell — that's a statement about this conversation's inputs, not about Larkspur, Beacontree, or Ashgrove.
- **No figure in this document is a proxy, an estimate, or a published claim.** Every cell is either a frozen field name or NO. Nothing here should be read as "Larkspur is worse than Windlass at X" — there is no X on the page yet.
- **What would change this:** pasting Larkspur's collected data and Beacontree's docs findings against the frozen rows above populates two of four columns immediately; running rungs 1-3 for Ashgrove and rungs 3/6 for Beacontree closes the rest; supplying Windlass's own figures unblocks the gap plan that this exercise exists to produce.