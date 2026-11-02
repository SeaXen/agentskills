# Open source strategy — Pelago recommendation engine

## Headline, before the brief

The pitch as framed — "open source the recommendation engine for credibility plus free contributors" — fails two of the five boundary gates as soon as you apply them to the actual asset. Bring the CEO a narrower line, not the literal ask. Below is why, and then the case and metric for the version that survives.

## Step 1 — This is two assets wearing one name

"The recommendation engine" is not one thing to open or close. Split it:

- **The differentiating layer**: the trained ranking model, the feature set built from Pelago's booking/click/cart data, and the business rules that encode what you've learned about travel-intent conversion. This is what you mean when you say "it's why our conversion beats the big OTAs."
- **The enabling layer**: the generic architecture around it — the retrieval/ranking framework, the feature-store scaffolding, the offline evaluation and backtesting harness, the serving pipeline.

Sony ran this exact split on its media stack: contributed the framework, kept camera-effect features like smile recognition closed. That's the shape to copy here, not a binary yes/no on "the recommendation engine."

## Step 2 — Name the motive, and test it

You gave the CEO two motives. Neither survives contact with its own evidence test on the differentiating layer:

- **"Free contributors improving ranking quality"** is the cost-sharing / upstreaming motive, and it's the specific version this skill's own literature flags as the one that fails most often: most published repositories never receive an external contribution. Cost-sharing needs another organization with a reason to co-fund. No other travel company will help you improve the algorithm that beats them at their own business — there is no co-funder here, so this collapses to "publishing code" with no shared-maintenance return.
- **"Credibility in the developer world"** is really the *talent* motive, and it has a real evidence test: the asset has to be work an engineer would want to be seen doing, and it's measured on hiring and reputation signals — never on adoption of the opened component. This one can survive, but only if it's measured honestly on that basis, not on "did outsiders improve our ranking."

You're B2C. This skill is explicit that consumer companies almost never open the consumer product itself — the moat is data, network effects and brand, none of which the code carries — and that the realistic motives here are talent, trust and cost-sharing on infrastructure, judged on hiring and reputation, not on adoption of what you opened. Your instinct to look for credibility is the right one; opening the differentiating layer to get it is the wrong instrument.

## Step 5 — The five gates, applied to the differentiating layer

| Gate | Verdict on trained model + proprietary feature set + business rules |
|---|---|
| **1. Irreversibility** | Once shipped, permanent. If Booking.com or Expedia forks it the day after release, you cannot take it back. Ask: does the decision change if this can never close again? Yes — so the honest verdict is "not this asset." |
| **2. Differentiating or context** | You said it yourself: "why our conversion beats the big OTAs." That's the textbook definition of differentiating, not enabling. Fails outright. |
| **3. Value capture (veto)** | Name what still stops Booking.com — bigger traffic, bigger booking history, bigger ML team — from taking the opened code and outperforming you with it. Nothing does. Hosting, trademark and support don't apply to an algorithm; only the training data and live traffic do, and those don't ship with the code. Veto. |
| **4. Contribution viability** | An outside contributor can't validate whether their pull request improves ranking without your live traffic and booking-conversion labels. That data stays private by necessity, so nobody outside Pelago can meaningfully test a change. This is the "open sourced it and nobody came" trap, except worse: even a motivated contributor structurally cannot contribute here. |
| **5. Ownership** | Unresolved either way — no named maintainer yet. |

Three gates fail, one of them a veto (gate 3). The verdict on the differentiating layer is **Closed**, not "not yet" — nothing you can plausibly do makes a competent competitor unable to redeploy your ranking logic once it's public, so there's no condition that flips this.

Run the same five gates on the **enabling layer** (framework, feature-store scaffolding, eval harness, stripped of your trained weights and feature values): it passes. It's generic, it's CV-worthy work, and if you ship it with a public or synthetic benchmark dataset, outside engineers can actually test a change without touching your production data — that's what makes gate 4 pass here where it failed above.

## Step 6 — Stress it against the named competitor

Write the scenario out plainly: Booking.com's ML org, an order of magnitude bigger than yours, forks the released ranking code, retrains it on their own booking history — which dwarfs yours — and now runs a tuned version of your own architecture against you, at their scale. What do you still hold? Nothing, if you opened the trained model and feature set. That's the tell that the full-engine version of this plan is wrong; move the asset (open the framework, not the model), don't reach for a license to paper over it.

## Step 7 — Who actually decides this

This shouldn't be a VP Engineering call alone. Google's own release criteria ask exactly one question that maps onto this case word for word: *does the release touch our secret sauce — ranking, filtering?* Theirs names ranking as the standard example of what doesn't ship. Since Pelago's booking-commission revenue rides directly on this ranking edge, treat this the way a late-stage software company defending a revenue line should: the business case is yours to propose, but the release decision on anything touching the actual scoring logic should escalate to the CEO, with legal/IP reviewing separately and in parallel — not blocking each other's job. That's the split to bring back, not just an answer.

**Commitment to publish, if you proceed with the narrowed line**: state publicly that Pelago will release the ranking framework and evaluation tooling, and will never release the trained model, the feature set, or the ranking business rules. Say it before anyone asks, so it reads as a boundary, not a concession under pressure.

## Step 8 — What running this actually costs

Assign a named owner and a real hours-per-week number before you announce anything — a repository with no maintainer turns your credibility motive into evidence against you. Size it, roughly: one engineer at ~15–20% for release review, issue triage and contribution review, plus a legal pass at launch (license file, secrets scan, trademark check). No foundation membership needed at this stage. Confirm the actual number with whoever you name as maintainer before this goes to the CEO as a cost line, not an estimate.

## The case for the CEO

Open the framework, not the edge. That gets you a real, defensible version of the credibility motive — recsys/ranking engineering is work good ML engineers want on their CV, and Pelago competes for that talent against companies with far bigger brands — without handing Booking.com the thing that actually converts. "Free contributors improving our ranking quality" was never going to happen even if you shipped the whole engine, because outsiders can't test against your live conversion data; dropping that expectation now avoids grading this initiative against something that structurally can't occur.

## The metric

Because the surviving motive is talent/trust, not cost-sharing, measure on hiring and reputation signals — never on adoption of what you opened, and never on ranking-quality lift attributed to external contributions.

Track, quarterly:

1. **Recruiting funnel**: number of ML/recsys candidates who cite the repo in an application or interview; contributor-to-hire conversions; source-of-hire attribution for ML/recsys roles that name the project. This is the direct test of the talent motive.
2. **Retention of the people who maintain it**: the named maintainer(s) staying, and citing the project as a reason. A talent motive that doesn't show up in retention of your own team isn't working.
3. **Reputation signal, external**: conference talk acceptances referencing the project, inbound press or analyst mentions, and — if it ever comes up — technical due-diligence conversations (investor, partner) where the repo was actually referenced. Require it be *asked for*, not just linked in a deck; a benefit nobody asked about is not evidence, it's decoration.
4. **Program health, underneath the motive**: median first response time on external issues, and whether the repository has a release in the last quarter. Not the success criterion itself — the leading indicator that the repository is alive enough for the motive above to have a chance.

Explicitly **do not** report stars, forks or download counts to the CEO as success evidence — adoption is the mechanism talent recruiting runs on, not the outcome being measured, and it invites grading a hiring bet on a vanity number.

**Guardrail, not a KPI**: watch for a competitor's engineering blog or public repo referencing the architecture you shipped within the following year. That's not failure by itself — the framework was cleared through gate 3 precisely because it carries no conversion edge — but if it happens fast and specifically, it's the signal to re-run gate 3 on what you released next, before shipping more.

**Re-evaluation trigger**: next planning cycle, and immediately if a competitor ships an open equivalent ranking framework, if the maintainer leaves, or if pressure builds to open "just the model too" to get more traction — that request is the moment to re-run gate 3 out loud, not to quietly widen the line.