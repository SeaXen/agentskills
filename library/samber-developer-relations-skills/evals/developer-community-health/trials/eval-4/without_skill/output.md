# Brambleweave — Q3 2026 Community Health Report

## Summary

Activity metrics look strong this quarter. The underlying trend does not. Growth in community volume has not been matched by growth in maintainer capacity, and that gap is now visible: one of two maintainers is signaling burnout. That is the headline finding of this report, not a footnote to it. A community health report that leads with engagement numbers and buries maintainer sustainability at the bottom would be misleading the board about what "healthy" means for a two-person project.

## The quarter, by the numbers

| Metric | This quarter | Trend |
|---|---|---|
| Discord messages | 1,140/month | +40% QoQ |
| Distinct posters | 61 | — |
| Merged PRs | 23 | — |
| Maintainers | 2 | unchanged |

These are good top-line numbers for a project this size. Read in isolation, they'd support a "things are going great" narrative. Read against maintainer capacity, they tell a different story: every one of those 1,140 messages and 23 merged PRs still routes through the same two people it did a year ago. Growth in surface area with flat growth in capacity is not a sustainability story — it's a countdown.

## What the numbers don't show

We don't currently track the metrics that would tell us whether this growth is *healthy* growth:

- **Who answers questions in Discord.** If most of the 1,140 messages/month are questions to Ines and me rather than community members helping each other, the +40% is +40% more load on two people, not evidence of a self-sustaining community.
- **PR review latency and reviewer concentration.** 23 merged PRs is a healthy quarter's output, but if both of us are the only reviewers, that's a second bottleneck sitting on top of the first — support load and review load compounding on the same two people.
- **Response time and unanswered-question rate.** Without this, we can't distinguish "the community is thriving" from "the community is waiting."

None of this is a criticism of past reporting — these weren't the numbers that mattered until growth made the bus-factor risk concrete. They're the numbers that matter now, and we should start tracking them next quarter (see Asks, below).

## The actual risk this quarter

Ines told me last week she's dreading opening the repo and is considering stepping back. I'm flagging this to the board directly rather than softening it, because it's the material risk to Brambleweave's continuity right now — more material than any metric in the table above.

Brambleweave has a bus factor of two. If it drops to one, the project doesn't have a health problem, it has a survival problem: one person can't sustainably carry triage, review, and roadmap for a project generating 1,140 messages and 23 PRs a quarter. The growth we're reporting this quarter is, unaddressed, the direct cause of the strain that's producing this risk — more users, more questions, more PRs, same two inboxes.

This isn't a personnel aside to mention after the metrics. It's the finding the metrics point to once you read them as a capacity story instead of a popularity story.

## What we're asking the board for

1. **Budget or approval to build a triage/helper tier.** A meaningful slice of the 61 distinct posters this quarter are almost certainly capable of answering common Discord questions and doing first-pass PR review. Formally recognizing and delegating to 3-5 of them is the single highest-leverage fix available — it converts community growth from a load multiplier into a load reliever.
2. **Explicit, board-endorsed response-time norms.** Right now the implicit standard is "whenever Ines or I see it," which scales to zero. A published, modest SLA (e.g., "we triage within 3 business days") gives us permission to stop treating every message as urgent, and gives the board language to point to if a user complains about slower answers.
3. **A real conversation about Ines's role**, now, not after Friday's report. Whatever she decides — stepping back partially, taking a defined break, redefining scope — the board should hear it from us before it becomes a surprise resignation. A report that says "61 posters, up 40%" without this context would leave the board unable to act until it's too late to help.
4. **Consideration of compensation or funding for a part-time contributor/community role**, if budget allows. Volunteer-only maintenance scaling linearly with community growth is what produced this quarter's risk; it will produce the same result again next quarter if nothing structural changes.

## What we'll track starting next quarter

- % of Discord questions answered by non-maintainers (community self-sufficiency)
- PR review turnaround time, and reviewer concentration (how much of the 23 fell to each of us)
- A direct, non-metric check-in: are the two of us finding this sustainable, asked explicitly each quarter, not inferred from silence

## Bottom line for the board

Brambleweave had its best quarter on paper. It's also the quarter in which the project's actual constraint — two maintainers, no depth behind them — became visible. The right response isn't to celebrate the numbers and move on; it's to treat this quarter's growth as the trigger for building capacity behind Ines and me, starting now.