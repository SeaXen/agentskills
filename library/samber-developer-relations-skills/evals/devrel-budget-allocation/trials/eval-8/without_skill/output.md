## Ravencourt pillar ROI — why the $17/$629/$2,454 comparison doesn't support the reallocation call

**The core problem: you're comparing cost-per-unit, not ROI.** ROI needs a shared outcome — revenue or pipeline influenced per dollar. What you have is four different activity metrics, each measuring a different thing at a different funnel stage, none of which is revenue:

| Pillar | Spend | Unit | Cost/unit | What the unit actually is |
|---|---|---|---|---|
| Events | $88K | Qualified conversation | $629 | Mid-funnel, sales-adjacent, closest of the four to a real buying signal |
| Content | $54K | Published piece | $2,454 | An *output*, not an outcome — one piece can compound traffic/leads for years |
| Community | $31K | Answered question | $17 | Mostly support/retention interaction with existing users, not new-logo acquisition |
| Docs/samples | $46K | — | — | Enablement infrastructure that multiplies every other pillar's conversion rate |

$17 looks cheap because answering a Discord/forum question is the cheapest atomic action of the four to produce — not because community is generating more business value than events or content. That's a unit-cost artifact, not an ROI finding. Ranking pillars by "dollars per easiest-to-count action" will systematically make your cheapest-to-produce activity look like the winner every time, regardless of what it actually returns.

**The units aren't even measuring the same funnel stage, so the comparison is apples to screwdrivers:**
- Events → mid/bottom funnel (someone already engaged enough to have a qualified conversation)
- Content → top funnel, long-tail, compounding (a post from 14 months ago is still doing work today; a 2026 cost-per-piece figure attributes all of a year's spend to zero credit for pieces still driving traffic from prior years)
- Community → mostly post-signup engagement/retention/support deflection, not acquisition
- Docs → invisible multiplier across all three others (bad docs tank trial-to-paid conversion and inflate community's support load; you may be underpaying for docs precisely because good-enough docs are why community only needs $31K to close 1,840 tickets)

**The classic first-touch/last-touch problem is hiding here too.** Your $629/conversation figure implicitly gives 100% credit to the event for a "qualified conversation" — but if that prospect read three blog posts and the docs before ever qualifying, content and docs did real work that this table erases entirely. A raw cost-per-unit table is a single-touch, single-credit model dressed up as ROI. You wouldn't accept "last-touch" as gospel in ad attribution; don't accept it here.

**What "ROI" actually requires before you can rank these:**
1. A common denominator — pipeline $ or closed revenue influenced per pillar, not raw unit counts.
2. Of the 140 qualified conversations: how many became opportunities, how many closed, what revenue? Same question for the fraction of the 1,840 community answers that came from prospects (vs. existing customers vs. churn-risk accounts) — those are very different in value.
3. A self-reported check: ask new qualified-conversation leads and recently closed deals "what did you read/use before this call" — this is the cheapest way to surface content/docs influence that your current metrics can't see (this is exactly the dark-social/multi-touch blind spot — nobody's tracking cross a survey).
4. For docs specifically: stop trying to force a per-unit cost onto it. Instrument it via proxies — trial-to-paid conversion rate with vs. without docs engagement, support ticket deflection $ (tickets community *didn't* have to answer because docs answered them first), time-to-first-value. "Can't put a number on it" today is a measurement gap, not evidence it's low-value — it's plausibly the highest-leverage line item precisely because it's invisible in this table.

**My recommendation: don't move the money yet, and don't rank on this data as-is.** The $17/$629/$2,454 numbers are real costs but not comparable ROI — moving budget from content and events into community on this basis would defund your acquisition-stage motion in favor of a mostly-retention/support pillar, based on a metric that structurally favors whichever pillar has the cheapest atomic unit.

Concrete next step, in priority order:
1. Pull pipeline/closed-revenue data for the 140 qualified conversations (should already exist in CRM) — this alone tells you events' real ROI, not just its cost.
2. Run the self-reported "what did you engage with before this" survey on the last 2 quarters of qualified conversations and closed deals — cheap, fast, and it's the only way to see content/docs' upstream influence.
3. Split community's 1,840 questions by asker type (prospect vs. customer) — you're likely conflating two very different pillars (pre-sale engagement vs. post-sale support) under one number.
4. If you want a real tiebreaker instead of more modeling: hold back content spend in one region/segment for a quarter and watch qualified-conversation volume there vs. a control region. That's the actual test of whether content is doing invisible upstream work or not.

Once you have revenue/pipeline per pillar, re-run this ranking. Until then, treat "community wins at $17/unit" as an artifact of comparing incomparable units, not a funding decision.