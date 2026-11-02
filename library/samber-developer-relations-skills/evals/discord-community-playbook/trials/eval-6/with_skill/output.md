I couldn't build the year-over-year chart, and I haven't touched your Server Insights. Insights only keeps 120 days of history, so a YoY view doesn't exist. This quarter's data is also close to rolling off, so export the CSV today. The slide below is ready, with the numbers I can't see left as blanks.

## What I changed from your brief

- **The 157% is correct** (5,400 / 2,100 = 2.57×). A member count only measures joins, though. Discord's own benchmarks use communicators and new-member retention. A first-run CLI message reaches every user, so many will join and never speak. A VP who asks "are they active?" will sink a headline that only shows joins.
- **The CLI link is a legitimate source.** It isn't an invite contest or a join-for-join scheme.
- **I haven't claimed the link caused the growth.** The slide only says the growth followed it. The link can be tied to the joins only if it used its own invite code. Insights has a "Most Popular Invites" table for that.

## Do this first (about 10 minutes)

1. Open Server Settings > Insights > Growth and Activation. Set the range to the full 120 days and **export the CSV**.
2. In the invites table, find the code the CLI uses. Write down its joins.
3. Write down the weekly communicators ÷ visitors and the new-member retention.
4. Send me those numbers, or paste the CSV, and I'll fill in the blanks and build the chart.

## Slide

**Title:** Discord grew 2.6× in one quarter, from 2,100 to 5,400 members, after we linked it from the CLI

**Left: three numbers**

| Metric | Value |
|---|---|
| Members | 2,100 → 5,400 (+3,300, +157%) |
| Joins from the CLI invite link | {N} ({x}% of the 3,300) |
| Weekly communicators ÷ visitors | {x}% (Discord's benchmark is about 30%) |

**Right: chart**
- Chart type: line chart of weekly members, with a second line for weekly communicators.
- Annotation: a vertical marker on the date the CLI message shipped.
- Source line: "Source: Discord Server Insights (alpha, partial counts), {start}–{end}."
- No YoY comparison. Insights keeps only 120 days of history.

**Bottom takeaway:** The CLI first-run message is now our largest single source of Discord joins. Next quarter we track whether those joins turn into active members.

**Speaker notes**
- "157% is member count. The activity number is {x}% against Discord's 30% benchmark."
- "New-member retention after one week is {x}%."
- If asked about causation: "Growth followed the CLI change. This invite code accounts for {N} of the joins."

## Caveats to hold in your pocket

- **Partial counts.** Insights is an alpha feature, members can opt out, and announcement stats need posters' consent. Don't present its counts as exact.
- **Weak activity numbers.** If communicators ÷ visitors comes in far below 30%, say so on the slide and frame it as the next quarter's goal. Don't hide it.
- **No dedicated invite code.** If the CLI link shares an invite with other sources, drop the "{N} joins from the CLI" line. Say "growth coincided with the CLI change" and move to a dedicated code from now on.
- **A real YoY needs your own history.** Use a year-ago member count from your records, if you have one. Make that a separate one-number comparison. Don't present it as a chart from Insights.

## Questions for you

1. Does the CLI link use its own invite code?
2. Which dates define "this quarter"? I need them to set the chart range.
3. Is 5,400 the total member count, or net of leavers and bots?