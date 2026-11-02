## What's actually wrong with the brief, before touching a dashboard

**1. The 25% stat isn't a target you can inherit.**
That number (attributed to a "well-known productivity company") is almost certainly:
- Self-reported by that company, with no published methodology — you don't know if it counts template-gallery virality, workspace invites, or affiliate codes as "community referral," none of which map to a champions/ambassador program.
- Measured at a user base and product-led-growth scale (viral loops baked into the product itself) that has nothing in common with a B2B/dev-tool champions program run by a handful of named advocates.
- Possibly a conference-talk anecdote, not an audited figure — treat any unsourced competitor percentage as a story, not a benchmark, until you can find the primary source.

Adopting it as a 12-month goal means you're aiming at a number you can't verify, from a growth mechanism you don't have. **Don't put 25% in front of the board as the target.** Build your *own* baseline first, then set a target as a multiple of that baseline.

**2. "Revenue attributed to each individual ambassador" is the wrong organizing metric for this dashboard**, for three concrete reasons:

| Failure mode | What it looks like in practice |
|---|---|
| **Small-N luck, not signal** | One ambassador's referral link happens to touch a $200K enterprise deal that was going to close anyway. They look like your best ambassador. A champion who answered 40 forum questions and wrote two tutorials that quietly seeded five mid-market deals shows $0, because none of that has a trackable link. |
| **Most influence is invisible by construction** | Word of mouth, Slack/Discord mentions, a conference hallway conversation, a "someone at my company recommended it" — none of it carries a referral code. A dashboard that only counts *trackable* revenue will systematically under-count your best advocates and over-count whoever happened to paste their link into a deal that was already moving. |
| **Gaming risk the moment it's legible as a leaderboard** | The instant ambassadors know a public/semi-public revenue number determines who "earns their keep," you get self-referrals, pressuring existing contacts to route through their link, and disputes over shared credit. This is the exact "commission-based referral feels like MLM" failure mode — it kills the goodwill the program depends on. |

Building this as asked would hand your CRO a dashboard that is precise-looking and directionally wrong — confident numbers built on an incomplete, gameable signal. That's worse than no dashboard.

---

## What to build instead: a two-layer dashboard

### Layer 1 — Program scoreboard (answers the CRO's real question: "is this program moving the needle")

| Metric | Definition | Source | Cadence |
|---|---|---|---|
| New users, total | All new signups/accounts this period | Product/CRM | Monthly |
| Community-attributed new users | Signed up via a per-ambassador trackable link/code **or** self-reported "an ambassador/community member told me" at signup | Link tool (e.g. Dub) + a signup survey field | Monthly |
| **% community-attributed** | Community-attributed ÷ total new users — this is the *only* honest counterpart to the 25% claim, defined transparently so it can be defended in a QBR | Computed | Monthly, trended |
| Influenced pipeline value | Opportunities with an ambassador touch **logged before the opportunity was created** (anti-retrofit rule), 365-day lookback | CRM | Quarterly |
| Influenced → closed-won revenue | Same cohort, closed-won only | CRM | Quarterly |
| Trend vs. baseline quarter | This quarter's % and $ vs. the first measured quarter | Computed | Quarterly |

The **anti-retrofit rule** matters: the touch must be recorded in the CRM *before* the opportunity is created, not backfilled after a deal closes by joining a spreadsheet of workshop attendees to closed accounts. Sign this rule off with sales ops *before* the first quarter starts. Report "influenced pipeline," never "sourced" — and expect the first-quarter number to be smaller than any hallway estimate. Report it, don't target it, for the first two quarters while you validate the baseline.

### Layer 2 — Ambassador scorecard (answers "who's earning their keep," without a revenue leaderboard)

A multi-signal recognition score per ambassador, none of it comp-linked:

| Signal | What it captures |
|---|---|
| Trackable referral signups | Direct, link-based — the *lower bound* of their influence |
| Content published | Blog posts, videos, talks — count + reach where measurable |
| Community support | Questions answered, forum/Discord/Slack activity |
| Contributions | PRs, docs, integrations |
| Recency | Active in the last 30/90 days |
| Composite score | Weighted roll-up → tiering for recognition (spotlight, swag, conference sponsorship, early access) |

This is the thing you actually put in front of the CRO to show engagement quality and spot who to invest more in — as a **recognition tier**, not a commission statement. If he wants a dollar figure per person anyway, you can give him one, clearly labeled:

> *"Estimated directly-attributed revenue: [trackable referral signups] × [win rate] × [avg deal size]. This is a floor, not a total — it excludes word-of-mouth and any untracked influence, and must never be used to rank or compensate people."*

---

## What to tell the CRO

1. "The 25% figure isn't something we can adopt as-is — we don't know how that company measured it, and their growth mechanism (product-led virality) isn't ours (a champions program). I'd rather set a target off our own first measured baseline than chase an unverified outside number."
2. "We *can* build a defensible '% of new users community-attributed' metric, and I'll show you the trend toward whatever target we set, quarter over quarter."
3. "A per-ambassador revenue leaderboard would actively mislead you — it rewards whoever got lucky with a trackable link on a deal that was already closing, and it invisibles the ambassadors doing the highest-value work (support, content) because that influence isn't trackable. Worse, if ambassadors know it exists, we create an incentive to game it, and we damage the goodwill the whole program runs on."
4. "Here's what I'll build instead: a program-level scoreboard you can put in front of the board, and an individual scorecard that shows engagement quality so we know who to invest more in — recognition-based, not commission-based."
5. "First quarter's number will look smaller than any hallway estimate — that's expected, it means the rule is honest. I'd like your sign-off on the attribution rule before the quarter starts, so it can't be relitigated after the fact to flatter a number."

---

## What's needed to build it

- A per-ambassador trackable link/code (short-link tool with click + conversion attribution).
- A CRM field for "ambassador touch," populated before opportunity creation — sales ops needs to agree to log this at deal-creation time, not backfill it.
- A one-field addition to the signup flow: "How did you hear about us?" with an ambassador-tagged option + free text, to catch word-of-mouth that no link can see.
- Sign-off from the CRO and sales ops on the attribution rule (365-day lookback, anti-retrofit clause, "influenced" not "sourced") *before* the first quarter of measurement starts.
- A decision from the CRO on whether Layer 2 stays purely recognition-based (recommended) or he wants the caveated $-floor number too.

**Open questions to flag back to him**, not to block on:
- Does the CRM already have a lead-source/touch field we can reuse, or does this need net-new schema?
- How many active ambassadors are we talking about — if it's under ~15, per-person numbers of any kind will be extremely noisy quarter to quarter, and that's worth saying out loud before the first readout.
- Is there budget appetite for a short-link/attribution tool, or does this need to be duct-taped from UTM params in the interim?