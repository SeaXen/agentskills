# Community Launch Brief — Kestrel Metrics

## 1. Verdict: Do not launch a Discord right now

Running the five readiness gates against what you've described:

| Gate | Result | Evidence |
|---|---|---|
| Demand | **Fail** | ~6 tickets/month, none repeating, all one-off integration questions. No sign of users answering each other anywhere, private or public. |
| Owner | **Fail** | No named person with protected weekly hours. "Marketing will keep an eye on it" is not ownership — it's the exact gap that produces a dead server. |
| Purpose | **Fail** | No measurable outcome stated. "We need a Discord" (post-conference) isn't a claim you can hit or miss. |
| Venue vacuum | **Fail** | An ecosystem Discord for the monitoring space already exists, and at least 3 of your users are already in it. That space already serves this audience. |
| Seed supply | **Weak/fail** | 40 paying customers total, only 3 confirmed active anywhere community-adjacent. No named list of 20+ people you could invite with topic/time-zone coverage. |

Zero gates clearly pass. The threshold for "launch" is 5, for "launch late with mitigation" is 4 — this doesn't clear "do not launch."

This is worth saying plainly to your CTO: the two facts that triggered this ("competitors have thousands of members," "we should have one too") are explicitly *not* evidence of readiness. Competitor community existence and a leadership impression from a conference are the two most common false signals in this decision — they tell you nothing about whether your own users want to talk to each other. A thousand-member Discord with 20 weekly posters (very plausible for those competitors, per Nielsen's well-established 90-9-1 participation split — ~90% of members never post) is a failed community with good PR, not a benchmark to chase.

## 2. What channels you'd actually be asking for — and why not yet

If you launched today, the instinct would produce something like:

`#announcements #general #help #integrations #feature-requests #showcase #off-topic`

That's the standard shape, and it's also the standard failure mode: a full channel tree opens with zero content in six of seven rooms, and every empty channel signals "nobody's here" louder than no channel at all. With 40 customers and a support load that doesn't even repeat, you don't have the traffic to keep two channels alive, let alone seven.

There's a second, sharper problem specific to your situation: you already have a room. Opening a second, unrelated Discord doesn't add capacity — it splits the three users you know about between your server and the one they're already in, and both end up looking quieter than either would alone. Two owned venues before either has critical mass is the one mistake this framework flags hardest.

So: no channel list yet. The channels are the easy 30 minutes; keeping any of them alive is the actual cost, and nothing here says you have the demand or the staffing to carry it.

## 3. What to do instead

Ranking the no-launch alternatives by evidence bought per hour of standing effort:

- **Efficiency (best return per hour):** answer publicly where the audience already is → forge-native discussions → FAQ/troubleshooting page → office hours → issue-based feedback loop
- **Value toward re-deciding later:** answering publicly > forge-native discussions > office hours > FAQ > feedback loop

One fact collapses this to a single pick: **you already know where your audience is, and it's not empty.** When an audience is already gathered in an active ecosystem space, answering publicly there outranks everything else so decisively that nothing else is worth starting first.

**The plan:**

1. **Pick one named person** (not "marketing," not a rotation — one person, even if it's you) to spend ~1 hour/week in the ecosystem Discord's relevant channel(s). This alone fixes the ownership gap that killed the Discord idea.
2. Have that person answer integration questions there under the Kestrel Metrics name — proactively, not just when @-mentioned. This is the same content your support inbox already handles; you're just putting the answers where other monitoring-space users can find and reuse them.
3. **Turn your 6 monthly tickets into a short public troubleshooting page** (a week to write, near-zero to maintain). Even though none of your specific tickets repeat, integration questions cluster into predictable categories (auth setup, SDK install, webhook config, etc.) — link to it when you answer in the ecosystem Discord. This is close to free and tests the demand gate for you: if the page gets traffic and questions keep coming anyway, that's a data point your current 6-ticket number can't give you.
4. **Track two numbers for 90 days**, both observable, neither a vanity metric: (a) do repeat questions start appearing — same integration issue from a different customer, and (b) does anyone in that ecosystem Discord answer a Kestrel question before your person does. Either one moving is the actual demand signal you don't have today.

This costs about an hour a week, forever, in a room someone else already keeps alive — no seeding, no moderation obligation, no empty channels for your CTO or your competitors' Discords to be compared against.

## 4. Ownership — fix this regardless of the venue decision

"Marketing will keep an eye on it" needs to become one name before you revisit this at all. That's not a community-strategy problem, it's a management one: someone needs 1 hour/week protected now and a sustained weekly number after that, confirmed by whoever manages them — not volunteered in a meeting. Until that person exists, the venue question is moot; a launch with no owner fails before the channel list matters.

## 5. When to re-open the Discord question

Not on a calendar date — on these triggers, checked against the alternative above:

- Repeat integration questions start showing up (same issue, different customer) — this is the demand signal you currently lack.
- Someone other than your team answers a question in the ecosystem Discord unprompted — evidence users will do this for each other.
- You can name 20+ engaged users by name, with some spread across integration topics.
- A specific person volunteers real weekly hours and their manager confirms it.

Two of these landing is enough to re-run the full gate check, not to launch immediately — a Discord's standing cost only makes sense once several of these are true at once, not one.

## 6. Open risks / things I assumed answering this without the full interview

- Assumed Kestrel Metrics is pure B2B SaaS (buyer and integrating engineer may be different people) — if your users are more indie/self-serve than that, some of this shifts, especially seed supply.
- Assumed no existing public GitHub repo/SDK with real issue traffic. If you ship a public client library and it already gets GitHub issues, that's a free secondary surface (forge-native discussions) worth turning on before anything else — confirm whether that exists.
- Didn't get a hard deadline or who judges the outcome — if the CTO needs *something* to report by a specific date, say so; "we tested presence in the ecosystem Discord and here's what we learned" is a legitimate 90-day answer to bring back, and cheaper to be wrong about than a dead server with your name on it.
- Didn't confirm any data-residency/privacy constraints on your customers — irrelevant for now since you're not hosting anything, but relevant again if this ever reaches an owned-venue verdict.