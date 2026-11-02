# Sablecourt DevRel: Year 2 Success Criteria

## Why the draft won't survive VP scrutiny

All four lines fail the same test: **can someone challenge this number in six months and you have an answer?**

| Draft target | Problem |
|---|---|
| Discord → 10,000 members | Raw headcount is a vanity metric — buyable, not indicative of value. No baseline stated, so "10,000" is arbitrary. |
| Blog → #1 for "event-driven architecture" | A generic head term competing against Confluent, AWS, Martin Fowler, Red Hat. Unwinnable in a year, and a single SERP position isn't a business outcome. |
| Booths → "strong pipeline" | Not measurable. No number, no owner, no cost baseline. |
| Docs → "stay current" | Not a criterion at all — no threshold, no cadence, nothing to fail. |

The deeper issue: **you have no baseline.** Analytics went live in August, nobody owns the numbers, and you're about to commit to absolute targets with no data behind them. Walking into your VP's office with "10,000 Discord members" invites one question you can't answer: *"why 10,000, and not 5,000 or 20,000?"*

## The reframe: Year 1 of measurement, not Year 5 of optimization

Pitch it this way to your VP directly — it's a stronger position than fake precision: **"This is the first year we can measure DevRel. Q4 2026 sets the baseline; 2027 targets are directional growth off that baseline, with an owner and a review cadence attached to every number."** That's a credible, senior thing to say. Pretending you have conviction on "10,000" when you don't is the weaker move.

Structure every line the same way:
1. **Baseline** — what August–December 2026 data shows (fill in once you have it; don't publish a made-up baseline).
2. **Leading indicator** — what DevRel fully controls, reviewed monthly.
3. **Lagging outcome** — the business result it's supposed to produce, reviewed quarterly.
4. **Owner** — one named person per metric. "Nobody owns the numbers" is itself the finding to bring to your VP — fix it in this doc, don't let it carry into next year.

---

## 1. Community (Discord)

**Drop the headcount target.** Member count is gameable (one Product Hunt spike or bot wave inflates it for free) and says nothing about whether the community produces value.

- **Leading indicators (DevRel-owned, monthly):**
  - 30-day retention of new joiners ≥ [benchmark from your Aug–Dec cohort, typically 20–40% is healthy]
  - Monthly active / total members ratio ≥ 20% (below 10% = warning per community-health norms)
  - % of support questions answered within 24h ≥ 90%
- **Lagging outcome (quarterly):** community-sourced signups or self-reported "found us via Discord" — tie to a `source` field at signup, not a guess.
- **Headline target to give your VP:** *"Grow monthly active members by X% quarter over quarter, with 30-day retention above [baseline+10pts]."* Set X once you have a Q4 baseline — don't publish a number today that you'd have to defend with no data.
- **Owner:** name a community manager or the DevRel lead explicitly. If nobody owns Discord day-to-day today, that's the actual gap — say so.

## 2. Blog / SEO

**Kill "#1 for 'event-driven architecture.'** That head term isn't winnable in 12 months by a team that "never really tracked" before, and even if you hit it, a single ranking says nothing about pipeline.

- **Reframe the goal:** build a keyword cluster around terms Sablecourt can realistically own — mid-tail, buyer-intent terms tied to your actual product surface (e.g. "event-driven architecture with [your category]," "[your product] vs [alternative]," "how to [specific problem you solve]") rather than the category-defining head term everyone already competes for.
- **Leading indicators (monthly):** organic sessions to the blog (baseline from August GA4 data), number of ranking keywords in positions 1–10 within your target cluster, not the head term.
- **Lagging outcome (quarterly):** organic-assisted signups/pipeline — requires UTM + source tagging, which is exactly what "analytics only set up in August" means you can finally do going forward.
- **Headline target to give your VP:** *"Grow organic sessions X% and organic-assisted pipeline $Y, anchored on a defined keyword cluster — not a single vanity ranking."* If your VP specifically wants a ranking story, give them "top 3 for [5 realistic mid-tail terms]" instead of #1 on the hardest term in the category.
- **Owner:** whoever owns content/SEO — name them.

## 3. Conference booths

"Strong pipeline" becomes measurable the same way the events skill frames it — **vanity vs. real vs. decisive**:

| Tier | Metric | Verdict |
|---|---|---|
| Vanity | Badge scans, foot traffic | Track, never report as success |
| Real | Qualified conversations, meetings booked, opportunities created | The actual scoreboard |
| Decisive | Cost per qualified meeting, pipeline $ influenced, closed-won influenced | What decides if you keep sponsoring |

- **Leading indicators (per event):** qualified conversations logged with next-step (not scan count), meetings booked pre-event (target a specific % of total via outbound before the event even starts).
- **Lagging outcome (quarterly):** pipeline $ influenced within a defined attribution window, cost per qualified meeting compared across events — this is how you decide which of this year's events to repeat and which to cut.
- **Headline target to give your VP:** *"$Z pipeline influenced across [N] events, at ≤$W cost per qualified meeting"* — both numbers computable once source-tagging is wired into the CRM (a same-quarter fix, not a 2027 one).
- **Owner:** whoever works the booth needs to own the qualified-conversation count; sales/revops owns the pipeline-influence number once it's tagged.
- **One flag for your VP conversation:** don't judge "conference booths" as one channel. A bad result at one event doesn't indict the motion — each event is its own ecosystem with its own audience fit. Ask for per-event ROI, not a blended average.

## 4. Docs

Turn "stay current" into a threshold with a review cadence:

- **Leading indicators (monthly):** % of docs pages reviewed/updated within 30 days of a related product release; number of pages flagged via "was this helpful?" feedback with no fix in >14 days.
- **Lagging outcome (quarterly):** support-ticket deflection attributable to docs (tickets referencing a topic that has a doc page vs. doesn't), docs-to-signup assisted conversions if you gate anything behind docs traffic.
- **Headline target to give your VP:** *"100% of docs pages touched by a release get reviewed within 30 days; support deflection improves X% quarter over quarter."*
- **Owner:** name whoever actually edits docs — if it's shared/nobody, say that explicitly; it's the same ownership gap as Discord.

---

## What to actually say to your VP

Lead with the reframe, not the numbers: *"We couldn't set credible targets before because we had no tracking and no named owners. Both are fixed now. Here's a baseline-plus-growth target per channel, each with an owner and a monthly review."*

Then present the four tables above with the baseline column filled in once you have Q4 data — probably a short follow-up conversation in January rather than something to force today. A VP who sees "here's exactly how we'll know if this worked, and who's accountable" reads as more credible than round numbers with no math behind them.