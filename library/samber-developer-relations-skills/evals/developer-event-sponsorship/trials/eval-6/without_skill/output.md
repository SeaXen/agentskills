## The core problem to solve first

⚠️ Table + workshop + dinner + two people is not fully compatible without a fix. A 90-minute workshop pulls one of you off the table entirely; if the same person also runs the dinner logistics, you're stretched across three jobs with two humans. Address this before anything else — otherwise the plan looks complete on paper and breaks on day one.

**Fix: recruit a third body for table-only coverage.** Options, cheapest first:
1. Ask an existing customer or vocal community user near the venue to work the table for 2-3 hours in exchange for swag, a dinner seat, and thanks from the stage. Costs nothing but goodwill.
2. Ask the organizers if student/community volunteers can cover a sponsor table for paid tiers — common at volunteer-run conferences, worth a direct email.
3. Hire a local contractor/booth staffer for the day (roughly EUR 150-300). Last resort, but cheap insurance against an empty table during your own workshop.

Without a third person, plan B is: accept the table sits empty (with a sign: "At our workshop, Room X, back at 3pm") for that one 90-minute block. Not ideal, but not fatal for a 1,100-person, multi-day event.

## Role split (2 people)

- **Founder:** owns the table, relationship conversations, the 2-minute stage pitch, and hosts the dinner.
- **Engineer:** owns the 90-minute workshop and is the natural face for a CFP talk submission (technical credibility sells better from an engineer than a founder at a dev conference).
- Both work the table jointly during peak traffic (arrival, lunch, coffee breaks, end of day) — that's when scan/conversation volume actually happens, not during quiet talk-in-progress hours.

## Schedule template (confirm actual grid with organizers, then slot into it)

1. **Pick your workshop slot deliberately.** Ask for the schedule grid before confirming your slot. Request early-afternoon (post-lunch trough) or last slot of a day — never a coffee-break-adjacent slot, since that's peak table traffic you'd be sacrificing.
2. **Day 1 evening: dinner.** Do it the first night, not the last — gives you a full second day at the table/workshop without post-dinner fatigue, and lets people you met on day 1 accept on day 2.
3. **Day 2:** table coverage both people, full day, no workshop conflict.
4. **T+1 day after conference ends:** block a half-day for follow-up before flying home if possible — the 24-48h window is where event ROI is actually won or lost.

## The 90-minute workshop

Design it as an activation funnel, not a talk — this is the single highest-leverage thing you do at this event for a $99/month self-serve product, because it converts attention into actual signed-up trial accounts on the spot, not just brand awareness.

- **Format:** hands-on. "Build a real-time Postgres change-data-capture pipeline in 90 minutes" — attendees bring laptops, spin up a free Ferrite account live, wire up logical replication, stream changes somewhere visible (a terminal, a dashboard, Kafka/webhook — pick one concrete downstream target for the demo).
- **CTA built into the exercise, not bolted on:** the only way to complete the workshop is to have signed up for the free tier. That's your real lead list — an activated account beats a badge scan by an order of magnitude.
- **Give a workshop-only code** (extra free-tier days, or a discount) so you can measure workshop → paid conversion specifically, separate from general conference traffic.
- **Record it.** A recorded, public "Postgres CDC in 90 minutes" session is durable content — YouTube, docs site, blog recap — long after the conference ends.

## The 20-person dinner

- **Curate the guest list 3-4 weeks out**, not from stage. Target: local Postgres/data-engineering meetup organizers, a couple of the conference's own speakers, existing paying customers within travel range, one or two organizers as a thank-you for the volunteer-run event. No open invite, no pitch at the table.
- **Book the venue now.** Private dining rooms in a conference host city get claimed fast by other sponsors during conference week — 4-6 weeks lead time minimum.
- **Budget:** roughly EUR 80-150/head for a good-not-extravagant dinner with wine → EUR 1,600-3,000, on top of the EUR 9,000 tier. Get this pre-approved as a separate line item now.
- One of you (founder) hosts; don't script a pitch — the dinner's job is relationship depth, not conversion.

## The diversity scholarship fund

- **Ask the organizers what a scholarship actually costs to fund** (many conferences have a set package — e.g., "EUR 300 covers one attendee's ticket + travel stipend"). Fund a specific number of named scholarships rather than wiring a vague amount — "Ferrite funded 5 diversity scholarships" is a concrete, usable line; "we donated to the fund" is not.
- Let the organizers decide whether/how to acknowledge it publicly — don't self-promote it from your own stage slot, that reads as buying goodwill rather than giving it.

## Getting badge-scan data off the table

1. **Ask organizers in writing, now, exactly what the EUR 9,000 tier includes for lead capture.** Volunteer-run, 1,100-attendee conferences frequently have no formal lead-retrieval system (that's Cvent/Bizzabo-tier infrastructure most community conferences can't afford). Get a straight answer and the export format before assuming anything exists.
2. **Don't rely on passive badge scanning even if it exists** — it's a vanity metric (per the events framework: "a scan is a person who walked slowly"), and passive scanning without explicit opt-in is a GDPR problem at a EUR-priced European conference.
3. **Bring your own active capture instead:** a tablet at the table running a simple opt-in form (or straight to Ferrite's own signup page with a conference-specific referral code). Tie it to an incentive — "sign up to grab a workshop seat" or a small raffle — so the form is the funnel, not an afterthought next to the badge scanner.
4. **One tracked link/code for every channel** — table signup, workshop signup, stage-pitch QR code — so you can tell which activity actually produced accounts, not just foot traffic.
5. **Capture context by hand for real conversations**, not just contact info: a one-line note per person (what they're building, what they said) written down same-day. This is what makes 24-48h follow-up personal instead of a generic blast — and personal is what a two-person team can actually pull off at this scale.

## Getting an engineer onto the main stage

- **You already have stage time** — the 2-minute pitch, and 90 minutes at the workshop lectern. For a self-serve dev tool, the workshop is arguably more valuable than a full talk slot: it produces activated trial accounts, a talk produces awareness.
- **For an actual full-length talk, two real paths:**
  1. **Submit a genuine CFP talk** if it's still open — a real technical topic (e.g., "Debugging Postgres logical replication lag," "What WAL-based CDC actually costs you at scale"), not a thinly-dressed product pitch. Best long-term credibility, usually free, and juried acceptance carries more weight with a dev audience than a bought slot ever will.
  2. **Ask organizers directly whether any tier includes a speaking slot**, and what it costs on top of what you've already paid. Say plainly you'd upgrade specifically for that — let them price it.
- ⚠️ **Expect "no."** Many volunteer-run, community-juried conferences (this looks like that kind) deliberately refuse to sell speaking slots at any price, specifically to keep the program's content trustworthy and separate from sponsorship — this is a values line for a lot of organizing committees, and pushing on it risks the kind of reputational friction that follows a small community around. If they say no, don't escalate — bank the CFP route for next year and lean harder into the workshop, which nobody can gatekeep as "pay to play."
- If they do offer a paid upgrade, get specifics before committing more budget: which tier, slot length, time-of-day (a graveyard slot isn't worth an upgrade), and whether it replaces or adds to your existing 2-minute pitch.

## Pre-event checklist (timeline)

- **T-6 weeks:** confirm schedule grid, request workshop slot, ask about lead-capture tooling and paid-speaking-slot possibility, start dinner venue search.
- **T-4 weeks:** lock dinner venue, finalize and send dinner invites, submit CFP talk if pursuing it, confirm third-person table coverage.
- **T-2 weeks:** build workshop materials + signup flow + tracked codes, finalize table capture tool, confirm scholarship fund amount/structure with organizers.
- **T-1 week:** rehearse the 2-minute pitch out loud (script it tight, one clear CTA — plug the workshop, give room/time), print/pack signage for the empty-table window.
- **Day-of:** work the table jointly at peak windows, run the workshop, capture notes per real conversation.
- **T+1 day:** tier and send follow-up — hot conversations get a personal note, workshop signups get a product-specific nurture, cold scans get one light touch or nothing.
- **T+1 week:** tag every lead's source in the CRM, publish workshop recording + recap post, pull a few quotes/photos for social.

## What "success" actually looks like here

Given the ICP (self-serve, $99/month, developer buyer), don't measure this like enterprise pipeline. Track: workshop signups → trial → paid conversion rate, number of real qualified conversations at the table (not scan count), and whether the dinner produces 2-3 durable relationships (community leads, potential integration partners, future speakers/advocates for you). Judge the tier's ROI on those three numbers, not on attendee-list size or how full the table looked.