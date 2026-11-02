## Straight answer to your CFO

There is no industry-benchmark ratio of advocates-to-registered-developers to give you, and if someone hands you one, it's not a standard — it's one company's anecdote wearing a decimal point. Every "X advocates per Y developers" figure in circulation (Slack decks, DevRel newsletters, HR benchmarking tools) comes from a single company's headcount at a single point in time, not from a measured cross-company study. No published DevRel survey — including the largest one running (*State of Developer Relations*, DevRel.Agency, 310 respondents, 2024 edition) — publishes a developer-to-advocate ratio, for the same reason: the denominator is undefined. "Registered developers" mixes people who signed up once in 2019 and never came back with your 12,000 MAU. Divide 2 advocates by 84,000 and you get one number; divide by 12,000 MAU and you get a number 7x larger — same team, same day, two "industry ratios" a decimal point apart. That instability is exactly why the number doesn't exist as a standard: it can't be, because the input isn't standardized either.

**Don't bring your CFO a ratio. Bring them a coverage gap.** That argument survives a finance review; a ratio doesn't survive the first follow-up question ("ratio of what, exactly?").

## What to bring instead

Replace "industry says N per developer" with "here are the surfaces we own, here's who's covering them, here's what breaks." Concretely:

1. **List every recurring surface** your 2 advocates currently touch or are expected to touch: docs, quickstarts, blog, community venues (Discord/forum/Slack), event calendar and travel, SDK/sample-app maintenance, champions program, changelog, support escalations, OSS repo triage.
2. **For each one, record:** who owns it today, hours/week it actually takes, and what happens if it stops (nothing / slow decay / visible outage).
3. **Cap planned capacity at 70%** of the two advocates' declared hours — support load, launches and travel eat the rest, so a plan built on 100% turns into unplanned overtime by the first launch.
4. **Headcount follows the math:** `target headcount = ceil(total weekly surface-hours required ÷ (0.7 × 40))`. Whatever that number is, it's your ask — sourced from your own surfaces, not from an anecdote.

That table is also what makes "four more heads" defensible line by line: each new hire maps to a named surface currently unowned, understaffed, or running at bus-factor-one (one person, no backup — an outage waiting for a resignation), not to a headcount-per-developer formula a CFO can poke a hole in.

## What I need from you to actually produce that number

I can build the sizing table and the headcount justification with you, but I need the inventory, not the developer count:

1. Which surfaces are your 2 advocates covering today, even partially (docs, events, community, sample apps, etc.)?
2. Roughly how many hours/week does each surface take?
3. Which of those surfaces has no backup right now if one advocate leaves?
4. What's driving the 4-head ask specifically — new surfaces you're about to take on, or existing ones already failing under 2 people?
5. Is the January ask funded by adoption/awareness, product-input/enablement, or sales enablement? That changes both the pitch and which surfaces matter most.

Give me those five and I'll turn them into the actual sized number and the one-page brief your CFO can approve — built on your surface load, not on a ratio that wouldn't survive their own follow-up question.