## The real problem: two different funnels, and you're only feeding one

Stars, downloads, and Discord joins are three different actions with three different amounts of commitment:

| Action | Commitment | Your number |
|---|---|---|
| Star | Zero — one click, no install, no risk | 14,200 |
| Join Discord | Near-zero — one click off a README badge | 3,400 |
| Weekly download | Low but real — you ran `install` | 2,100/wk |
| Dependent (someone shipped it in their own project) | Real — you bet on it | 31 |
| Active Discord member | Real — you came back | ~6 |

Everything above the line grows from awareness (awesome lists, newsletters, trending). Everything below the line only grows from someone deciding fennelwick solves *their* problem better than what they're already using. Awesome lists and newsletters are read by list-curators and tool-browsers — people whose job is to *collect* things, not adopt them. That's not a flaw in the channel, it's what the channel is for. Feeding it harder gets you more stars from the same low-intent audience, not more installs.

**Doing another newsletter round + chasing trending again is optimizing the metric that's already disconnected from usage. It will move stars, not downloads.** Flat downloads and flat dependents *all year*, through 14,200 stars of growth, is the tell — whatever's been driving stars so far has already been tested against usage, for eight months, at increasing scale, and the download line never twitched. There's no reason a ninth month of the same tactic breaks that pattern.

Discord is the same story, not a separate problem: 3,400/6 is a join-button next to a low-intent stargazer population. Growing it further just grows the gap.

## Before doing anything else: find out *why* stars don't convert

You don't have a distribution problem. You have an unanswered question: someone stars fennelwick, then doesn't install it. Why?

Three hypotheses, in the order to check them:

1. **First-run friction.** Time your own quickstart with a stopwatch, cold, as if you'd never seen the code. Count steps from "read README" to "saw it work." Anything past ~2 minutes or requiring config before a first result loses people who were only ever mildly curious. Check GitHub traffic (Insights → Traffic) for clone/view counts around your awesome-list adds and newsletter mentions — if clones spiked but downloads didn't, the leak is in the README/quickstart, not below it. If clones *didn't* spike either, the leak is even earlier (the listing itself isn't prompting click-through).

2. **Category mismatch.** Some projects are genuinely reference material, not dependencies — people star them to bookmark an idea, a pattern, or a list, never intending to `install`. If fennelwick's pitch reads as "here's a clever approach to X" rather than "add this to your stack to get Y," high stars with low dependents isn't a broken funnel, it's the expected shape for that category, and weekly-downloads is the wrong north-star metric for it entirely. Be honest about which one you built before treating the ratio as a bug.

3. **Weak differentiation at the point of decision.** 31 dependents in a category that presumably has incumbents means people who *do* get as far as evaluating it are mostly not switching. Pull up your top 3 alternatives' READMEs next to yours and check whether "why this over X" is answered in the first screen. If it's not there, or not concrete, that's the drop-off point for the highest-intent visitors you already have — the ones who don't need another newsletter to find you, they're already comparing.

**Concrete step, this week:** DM or open a short survey to 15–20 recent stargazers who never installed (cross-reference stargazer list against npm/download telemetry if you have it, or just ask in the issue tracker/Discord for "starred but didn't try it, why?"). Five real answers here will tell you more than another round of outreach.

## What to do instead of more newsletter/trending

- **Redirect the outreach effort into comparison/migration content**, not more mentions. "fennelwick vs. [top alternative]" and "migrating from [alternative] to fennelwick" posts target people who are already evaluating — much higher intent than an awesome-list browser, and it's the piece your funnel is currently missing per point 3 above.
- **Ship 2–3 integration tutorials** with the tools your realistic dependents already use. This is how you move the 31 → higher: not more people finding out fennelwick exists, but the people who already know making the jump to shipping it.
- **Fix Discord before growing it.** Either pull the invite out of prominent README real estate (stop harvesting drive-by joins you can't activate) or add one concrete first-action in the welcome flow (a pinned "run this one command and post your output" style prompt). 3,400 dead members is a support cost and a signal, not an asset — don't scale a channel with no retention loop.
- **Track the right numbers going forward:** weekly downloads trend, dependents trend, returning contributors, issue/PR velocity. Stop treating stars as a progress metric in status updates — it's already told you everything it can.

Skip the next newsletter round and the trending push until the survey/timing check above tells you *which* of the three hypotheses is real — otherwise you're paying for another push down a funnel stage that isn't the bottleneck.