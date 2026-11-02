Used the `devrel-competitor-analysis` skill (and its `signal-collection.md`, `gap-plan-example.md`, `published-findings.md` references) to build this. Two notes before the plan, both required by the skill:

- **This is a peer-set-of-one read**, scoped to the Content surface only, because that's the specific question the CEO asked. The skill's own convention is 3-5 peers — a set of one inherits Beacontree's blind spots (see "Peer set of one" in the skill's failure modes). Treat this as the fast answer to the immediate question, not the standing benchmark.
- **All numbers below are user-reported**, not independently pulled from Beacontree's public blog/RSS archive (no URL was given, and I didn't assume one). The skill requires every quantitative cell to carry a source URL and observation date to count as "observed" — these don't, so they're labeled accordingly. Before this goes on a board slide, run the real collection pass (12-month post count from Beacontree's actual feed) per `signal-collection.md` § Content.

---

# DevRel content-cadence plan: Windlass vs Beacontree

Scoped 2026-09-20 · Peer: Beacontree (named by CEO) · Surface: Content only · Assumed target date: March 2027 (6 months out) — confirm if a different March was meant.

## What changes because of this

1. **"6 posts a month" is Beacontree's team output across 5 DevRel-titled people — 1.2 posts per person. Windlass at 1.5 posts/month solo is already 1.4 posts per person.** The raw comparison the CEO saw is unnormalized by headcount, and normalized, Windlass is ahead, not behind. *Verdict: counter — use the per-head number in the next conversation with the CEO before committing to a volume target set by an un-normalized read.*
2. **Hitting a literal 6/month by March, solo, means a sustained 4x jump from today's 1.5 — a rate 4x higher than Beacontree's own per-person output.** That isn't a discipline problem to fix with effort; it's a capacity ceiling. *Verdict: close, but only via added capacity (guest/community/contractor lanes below), never by one person writing faster.*
3. **Beacontree is 8 years old with 5 dedicated people; Windlass is 2 years old with 1 generalist.** Their format mix, evergreen backlog, and distribution are compounding advantages of age and headcount that cadence alone can't close this year. *Verdict: ignore matching their operating model this year; counter on velocity instead (Windlass can ship developer content closer to the code's ship date than a 5-person editorial process can).*

## Scorecard

| Observation | Windlass (ours) | Beacontree |
|---|---|---|
| Company age | 2 years | 8 years |
| Employees | 19 | ~350 |
| Named DevRel/dev-educator headcount | 1 | 5 |
| Posts/month (as reported) | 1.5 | 6 |
| Posts per named DevRel human/month | 1.5 | 1.2 |
| Format mix | not observable from this data | not observable from this data |
| Evergreen vs release-bound share | not observable from this data | not observable from this data |
| Author mix (staff vs guest/community) | 100% staff (only 1 person) | not observable from this data |

The two rows that carry this analysis: *posts per named DevRel human* (row 5) flips the story from "we're behind" to "we're more productive per head, and understaffed in absolute terms" — the same read the skill's worked example makes for a docs gap, applied here to content. Everything marked "not observable" needs a real pass against Beacontree's actual blog (format tags, author bylines) before it can be cited outside this room — right now it's a gap in the data, not a finding.

## Per-surface read: Content

**Structural difference, not volume difference.** Beacontree isn't out-writing Windlass 4x through better discipline — it's running a 5-person content function against Windlass's 1-person function, on a product 6 years further into its life. The transferable fact for the CEO conversation isn't "they publish more," it's "they have 4 more people whose job is to produce this."

**What Windlass does that a straight volume chase would break.** At 1.5 posts/month with 1 author, every post is presumably solo-authored and reviewed by the person who wrote it. Scaling to 6/month without adding capacity would mean either quality erosion or splitting single articles into thinner pieces to inflate the count — flagged explicitly below as an anti-pattern, not a lever.

## Cadence ramp to March 2027

Reaches 6/month by composition, not by one person typing faster. Each month's jump is tied to a specific capacity lever coming online, not to "try harder."

| Month | Target posts/mo | Composition | Capacity lever unlocked that month |
|---|---|---|---|
| Oct 2026 | 2 | 2 solo | Guest-author pipeline opened: recruit 2-3 engineers, 1 customer, for a rolling contribution queue |
| Nov 2026 | 2 | 2 solo | Pipeline drafting; budget decision made on a freelance/contractor writer (needed now to land by Jan) |
| Dec 2026 | 3 | 2 solo + 1 guest | First guest/community post publishes |
| Jan 2027 | 4 | 2 solo + 1 guest + 1 contractor | Contractor onboarded if approved; second guest post live |
| Feb 2027 | 5 | 2 solo + 2 guest + 1 contractor | Guest cadence steady; short-form/video lane piloted alongside (doesn't count toward this total, but starts distributing effort away from long-form) |
| Mar 2027 | 6 | 2 solo + 2 guest/community + 1 contractor + 1 co-authored customer piece | Target hit — composition, not headcount, closed the gap |

If the Nov budget decision on the contractor doesn't land, the credible ceiling by March is **4-5/month** (solo + guest lanes only) — flag that dependency to the CEO now, not in February.

## Gap plan

Sorted by impact per unit of cost, highest first.

| Gap | Impact | Cost | Verdict | Owner | Date |
|---|---|---|---|---|---|
| CEO comparing raw post counts, not per-head | high | none | **counter** — bring the 1.5 vs 1.2 per-head number to the next conversation | Windlass DevRel lead | before next CEO check-in |
| No guest/community-author pipeline | high | low | **close** — recruit 2-3 engineer + 1 customer contributors | DevRel lead | pipeline open Oct 1, first post Dec |
| No budget for a contractor/freelance writer | high | medium (money, needs approval) | **close**, contingent on CEO sign-off — this is the swing factor between a 4-5/mo ceiling and hitting 6 | DevRel lead + CEO | decision by 2026-11-01 |
| No customer/community co-authored content | medium | medium | **close** — one case study per quarter, customer does the writing, you edit | DevRel lead | first piece Jan 2027 |
| Single format (long-form only) | medium | low | **close** — pilot a short-form/video lane to diversify without adding long-form load | DevRel lead | pilot Feb 2027 |
| Matching Beacontree's 5-person content org this year | low | high | **ignore** — resource mismatch (350 vs 19 employees, 8yr vs 2yr); revisit as a headcount case at next planning cycle, not this quarter | — | review at next annual planning |
| Matching Beacontree's 8-year evergreen backlog | low | high | **ignore** — not closable by cadence; counter with velocity (content shipping closer to code ship date than a larger editorial process allows) instead of trying to out-publish it | — | — |
| Hitting "6" by splitting existing posts into thinner pieces | n/a | n/a | **ignore** — vanity-metric gaming; inflates the count while producing nothing a developer finds more useful, and erodes trust in the number the moment anyone checks | — | — |

The two "ignore" rows on org size and backlog age are the point, not an afterthought: without them written down, "why don't we look like Beacontree yet" gets re-raised every quarter as if it were new information.

## Method and limits

- Scoped to the **Content surface only**, per the CEO's specific question — the other seven surfaces (docs, open source, community, Q&A, events, hiring) weren't collected and shouldn't be assumed comparable.
- Peer set is **one company** (Beacontree), named by the CEO, not the skill's usual 3-5 — the ignore/counter verdicts above lean partly on general resourcing logic rather than a cross-peer pattern. Adding 1-2 more peers (a same-stage direct substitute, and the demand-side answer — what a developer reads if neither existed, e.g. Stack Overflow or a community Discord) would make the counter-arguments sturdier for a board-level ask.
- All cadence and headcount figures are **as reported by the user**, not pulled from a public source with a URL and date — the skill's traceability bar (100% of quantitative cells sourced) isn't met yet. Before the counter-argument goes into a CEO deck, pull Beacontree's actual blog/RSS for a real 12-month count and format-mix read.
- Format mix, evergreen share, and author mix for both companies are marked "not observable from this data" rather than guessed — filling those in is the next collection pass if this repeats.
- **What would change this plan**: if Beacontree's 6/month includes release notes or docs updates counted as "posts" (release-bound material, per the skill, "resets to zero every cycle and compounds nothing") rather than being all deep technical content, the real comparison is even more favorable to Windlass than shown here.
- **Re-run trigger**: before the next CEO/board conversation that references this comparison, and again in March 2027 to check the ramp against actuals.