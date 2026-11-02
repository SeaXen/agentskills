I couldn't pull the Server Insights chart. I have no access to your Discord, and I won't invent numbers for a VP slide. The slide below uses only the two figures you gave me. For the year-over-year chart, I list below what to export from Server Insights.

## Slide

**Title:** Discord community grew 157% in Q[X], to 5,400 members

**Subtitle:** One change drove it: the invite link in the CLI's first-run message

**Left, big numbers:**
- **2,100 → 5,400** members (+3,300, +157%)
- **2.6x** the start-of-quarter size

**Right, chart:** Monthly member count, this year vs last year (see below).

**Bottom, 3 bullets:**
- Source: every new CLI install now sees the Discord invite on first run.
- Next: [X]% of new joiners posted or reacted within 7 days *(fill from Insights)*.
- Ask / next step: *(for example, add a docs link and a welcome flow to the first-run message)*

**Speaker note:** (5,400 − 2,100) / 2,100 = 157.1%, so the headline math is correct.

## Before Friday

1. **The title counts joins, not activity.** A first-run link adds many installers who join and never speak. If the VP asks "are they active?", you need an answer. Pull *Communicators* and *Retention* from Server Insights, then add one line to the slide. Without that line, the headline is vulnerable.
2. **The cause is a before/after claim.** You can support it with Insights' *Growth → Invites* breakdown, which shows joins by invite link. Use a dedicated invite link for the CLI. If you already did, cite its share of the 3,300 joins. If you didn't, say "coincided with" instead of "drove".
3. **A year-over-year chart needs last year's data.** Check that Insights still shows it. If you're under the history window, use quarter-over-quarter instead and retitle the chart.

## Chart spec (what to export)

- **Where:** Server Settings → Server Insights → Growth and Retention. Export or read the weekly total members.
- **Type:** line chart with two series, "This year" (solid, accent colour) and "Last year" (grey). The x-axis is months, and the y-axis starts at 0.
- **Annotation:** a vertical marker on the date the CLI change shipped, labelled "Invite added to CLI first-run".
- **Callout:** end-of-line label "5,400".
- **Fallback if there's no year-ago data:** two bars, "Start of quarter 2,100" and "End of quarter 5,400", with the "+157%" label on the second bar.

If you paste the Insights numbers here (monthly totals for both years, the invite-source split, and the communicators count), I'll build the chart and finalize the slide.