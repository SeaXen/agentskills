## The trap in the brief

Your CEO listed seven functions — developer adoption, sales enablement, developer enablement, product feedback, ecosystem partnerships, contributor community, employer branding — in one breath because that's what "developer relations" means in his head. It's a team's job description, not a person's. If you try to run all seven at once, you'll touch all seven and own none, and by month six nobody can point to what DevRel actually did for $60k plus your salary.

Your real first job: convert that list into a **sequence**, execute the first link fast enough to prove ROI, and use that proof to buy budget and eng time for the rest. Don't ask "how do I do all seven" — ask "which one, done well, creates leverage for the others."

## Why activation + sales enablement come first, given your specific model

Halberd's growth is two motions stapled together: bottom-up self-serve signups, and two AEs closing six-figure deals with a VP Eng as economic buyer. Both motions run through the same chokepoint — **a technical evaluator deciding whether your database is good enough, fast**. A self-serve engineer decides that alone in twenty minutes on your docs. A VP Eng's team decides it over a multi-week POC, but the person doing the deciding is functionally the same technical evaluator, just with an AE and a deal size attached.

That means docs, quickstart, and evaluation experience are not "developer marketing" in the content sense — they're shared infrastructure for both funnels. Fix that first and you've simultaneously moved developer adoption, developer enablement, and given the AEs something real to hand a VP Eng's engineers. Everything else (community, ecosystem, employer branding) compounds better once that foundation exists, and is close to wasted effort if it doesn't.

Contributor community and ecosystem partnerships specifically fail when started pre-emptively — you need proof people are already showing up before you formalize a program for them, and you need eng bandwidth to build integrations before you can go recruit partners for them. Neither is true on day one.

## Week 1: diagnose, don't build

Don't ship anything publicly this week. Spend it converting the CEO's brief into a scoped plan and finding out where the current funnel actually breaks.

- **1:1s, in this order**: the two AEs first (they'll tell you exactly where deals stall — that's your fastest signal), then CS/support, then eng/product leads, then the CEO again to play back what you heard.
- **Ask the AEs specifically**: what technical objections come up on every call, what they wish they had in the room during a POC, how long the eval cycle runs, and whether they've ever lost a deal to a competitor on a technical basis (InfluxDB, TimescaleDB, ClickHouse, QuestDB, VictoriaMetrics — whichever your team actually loses to).
- **Run the funnel yourself**: sign up as a stranger would, follow the quickstart, time it. If you don't get a successful first query in under ten minutes, you've found your first project before you've finished week one.
- **Check what already exists**: GitHub issues/discussions, any Discord/Slack, Stack Overflow tags, Reddit/HN mentions of the product. Somebody is almost certainly already acting as an informal power user or answering other people's questions for free. Find them before you build a program for them.
- **Check instrumentation**: can anyone currently answer "what % of signups run a successful query" and "what % reach production"? If not, that gap is your first engineering ask — put it in the queue Monday since you need a week's notice.

## The 90-day plan: three pillars, in order

### Pillar 1 — Developer activation (weeks 1-4, your main bet)

Fix the self-serve funnel before you promote it harder. Promoting a leaky funnel just burns more people through the leak.

- Rewrite the quickstart around the 5-minute rule: one install command, one working example, a visible payoff, nothing else. Cut anything explaining architecture before the user has run a query.
- Split docs into the four types that actually get used — quickstart, task-oriented how-tos, API reference, conceptual — and stop burying the quickstart under reference material.
- Get funnel instrumentation shipped (your week-1 eng ask): signup → first query → production usage. This is the metric you'll report to the CEO in place of vanity signup counts, and it's the same data that tells you where enterprise POCs stall too.
- Every code sample gets tested — a stale quickstart is worse than no quickstart, and this is the #1 thing that quietly kills technical credibility with both an individual engineer and a VP Eng's team.

### Pillar 2 — Sales enablement for your two AEs (weeks 3-8, overlapping)

With only two AEs closing six-figure deals, unblocking one stalled deal pays for your entire annual budget. This is also the fastest way to earn political capital with the CEO for everything else on his list.

- Build a technical one-pager and objection doc **with the AEs, not for them** — sit in on calls, use their language, test drafts on whichever AE closes more.
- Stand up a self-serve POC/sandbox environment technical evaluators can run without a sales call — this serves the bottom-up funnel and the enterprise eval cycle identically.
- Build 2-3 architecture/security/benchmark artifacts VP Eng-level buyers actually ask for (this is also your second, more specific engineering ask — flag it to the CEO as an investment in deal velocity, not a marketing nice-to-have).
- Track one number: cycle time or win rate on deals where your material was used vs. not. That's the proof point that justifies the rest of the budget.

### Pillar 3 — Power users and the feedback loop (weeks 6-12)

Light-touch, not a program yet. You already found these people in week 1.

- Personally reach out to the 5-10 people already answering questions or filing sharp bug reports. Ask what they need, not what they'll promote — this is your product feedback channel, cheaper and more honest than a survey.
- Route what you learn back to product/eng as a standing input, not a one-off report — this is the "product feedback" line item from the CEO's brief, and it costs you almost nothing once the relationships exist.
- Recognize contributions publicly and specifically as they happen. Don't build a tiered ambassador program yet — you don't have the volume or bandwidth to run one, and a program with no real benefits behind it reads as hollow.

## What you're explicitly *not* doing yet, and why

Say this part out loud to the CEO — it's the actual deliverable of week one, not a side effect.

- **Ecosystem/integration partnerships**: needs eng bandwidth you don't have standing yet, and partners will ask "how many users do you have" before they'll invest — better numbers in 90 days, not now.
- **Formal contributor community program**: no evidence yet of organic pull strong enough to justify Discord/Slack infrastructure and moderation overhead. Revisit once Pillar 3 shows consistent unprompted activity.
- **Employer branding**: real, but lower urgency than revenue-adjacent work at a 40-person company. Piggyback opportunistically — a good technical blog post or conference talk does double duty — rather than building a dedicated program.
- **Student/university programs**: this is a three-year payoff strategy. Wrong time horizon for a company your size watching burn.

## $60k, allocated

| Line | Amount | Why |
|---|---|---|
| Sandbox/POC environment + docs tooling | $8-10k | Shared infra for Pillars 1 and 2 |
| Content bounties for real users (blog/tutorial, $200-750 each) | $8-10k | Cheaper, more credible than DevRel-authored content; seeds Pillar 3 |
| One well-chosen conference (sponsor or speak, not both) | $15-20k | Pick where bottom-up audience and enterprise buyers overlap, not the biggest booth you can afford |
| Social listening / analytics tooling | $5-7k | Finds power users and mentions you'd otherwise miss |
| Swag (small, quality, given not sold) | $3-5k | Only after Pillar 3 has real recipients |
| Reserve, uncommitted | $10-15k | For the customer story, the surprise conference invite, the thing you can't predict in week one |

Don't commit it all in week one. The reserve is a feature, not an oversight.

## Engineering asks — name them now, they need lead time

1. Signup → first-query → production funnel instrumentation (week 1 ask, foundational).
2. Self-serve POC/sandbox environment (week 2-3 ask, feeds both Pillar 1 and 2).
3. Whatever the quickstart audit turns up as broken (likely week 2 ask, scope depends on what you find).

Queue these early and specifically — "about a week's notice" means vague requests on Thursday get bumped.

## What you report back, and to whom

Report the same three numbers monthly, tied to language the CEO and board already track:

- **Activation rate** (signup → first successful query → production) — this is "developer adoption," measured, not asserted.
- **Deal cycle time / win rate on deals using DevRel material** — this is "sales enablement" with a dollar sign attached, and it's the number that gets you more headcount.
- **Named power users engaged and what they told you** — this is "product feedback" and the seed list for "contributor community," reported honestly even when it's small.

## Your actual first deliverable

By end of week one, send the CEO a one-page memo: what you heard in the 1:1s, the funnel timing you measured yourself, and this three-pillar sequence with the explicit deferrals. Get his sign-off on the sequencing before you build anything public. That memo — not a Discord server, not a swag order — is the thing that turns "do developer relations" into a job you can actually be judged on.