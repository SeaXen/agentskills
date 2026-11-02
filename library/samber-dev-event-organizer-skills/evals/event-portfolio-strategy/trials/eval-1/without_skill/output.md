# Kotlin Northside: 2027 portfolio plan

## Next action

Collect last year's door attendance and organizer count from all nine crews. Every item below is gated on that data. A one-question form per crew takes about 30 minutes to send. Expect replies in about two weeks.

## Summary

- ✅ **Podcast.** Do it. It is cheap, central and needs no crew permission.
- 🟠 **Hackathon.** Do it as an opt-in pilot in 2–3 ready cities, not nine at once.
- 🔴 **Single nine-city sponsorship.** Do it last and restructure it. As described, you can't deliver it.
- Sequence: foundations (Q4 2026–Q1 2027), then podcast, then hackathon pilots, then the sponsorship.
- I didn't read anything under skill-wip/.

## The core problem

You run a federation, not a company. The crews pick their own dates, hold their own bank accounts and sign their own sponsors. The network owns three things: the name, the logo kit and a code of conduct.

Each of your three ideas assumes more central authority than that:

| Idea | What it assumes | Reality |
|---|---|---|
| Hackathon in every city | You can set each crew's calendar and workload | Each crew is volunteer-run and decides its own dates |
| Network podcast | Someone produces it | No central team exists yet |
| One deal for nine cities | You can promise delivery in nine cities | You can't sign for crews, and you can't guarantee dates, headcount or audience |

Fix this by giving the network a thin shared layer that crews join voluntarily. The three ideas then become one system:

> **The pan-network sponsor pays for the shared layer (podcast, hackathon prize pool, speaker exchange). Crews opt in. Local sponsors stay local.**

## Step 1: Foundations (Q4 2026–Q1 2027)

Don't sell or launch anything before these four exist.

1. **Baseline scorecard per city.** Record door attendance (not RSVPs), editions in the last 12 months, repeat-attendee share, organizer count and number of employers.
   - Why: a sponsor buys audience composition, and you have no network-wide numbers today.
   - Use CNCF's published bars as reference. Active means more than 10 attendees per event, no gap over 90 days, at least 2 organizers and at most 50% from one company. These are sourced figures.
   - Anything else I give you below is a baseline, meaning my default, not an industry standard. Replace each with your own median after three editions.
2. **Network charter, one page.** Cover who the network is for, what members get, what members must do and what the network refuses to do.
   - Name one primary outcome for the network. I suggest "a Kotlin community in every member city that survives its founders."
   - Put the code of conduct and a published **sponsor rule set** in the charter. The rules: never a paid speaking slot, never an attendee list, sponsor stage time capped at 15 minutes (CNCF's figure).
3. **A legal and financial vehicle.** Pick one:
   - A fiscal host, such as an existing non-profit or a fiscal-sponsorship platform.
   - A small association you create.
   - Decide this first, because it determines who can sign a sponsor contract and receive money. Get local legal advice in the UK, Ireland and the EU states. Currencies will include GBP, EUR, PLN and SEK.
4. **Name and trademark check.** Confirm what you may do with the "Kotlin" name and logo under the owner's brand policy, and whether a sponsor deal affects that. I haven't verified this. Treat it as a blocker until checked.

Also classify each city:

| Tier | Test (baseline) | Role in 2027 |
|---|---|---|
| Ready | 2 or more organizers from 2 or more employers, no gap over 90 days, a repeat audience | Hackathon pilot candidate, sponsor-package participant |
| Steady | Holds editions, but only 1–2 organizers or thin pipeline | Podcast and speaker exchange only |
| Fragile | Over 90-day gaps or a single organizer | Help recruit a second organizer; no new load |

Don't add load to a Fragile crew. A hackathon on a single-organizer crew risks losing that city.

## Step 2: Podcast (start Q1 2027)

**Verdict:** the best-value, lowest-risk addition. It adds no work to the crews and builds an asset sponsors can see.

**Design (my recommendation):**
- One central owner: one producer and one co-host. The cities don't produce anything.
- Season 1: 8–10 episodes, one every two weeks. Don't promise weekly.
- Content comes from the cities: speaker interviews, "how we run our city" episodes, and the best talk from a recent local edition, re-recorded as a conversation.
- This doubles as the speaker pipeline. Each city nominates one speaker per quarter, and the podcast gives them a second audience.
- Add a standing "city crew of the month" segment. It rewards crews and makes the shared layer visible.

**Success test for season 1:**
- Nine of nine cities appear at least once.
- Episode downloads trend stable or rising across 3 consecutive episodes.
- At least 2 guests become local speakers.
- The producer can sustain it with no more than a few hours per episode. Check this after episode 4, and cut cadence rather than quality if it fails.

**Risk:** one owner is a single point of failure. Name a deputy before episode 1.

## Step 3: Hackathon (pilot Q2–Q3 2027)

**Verdict:** valuable, but the most labor-intensive format you listed. It needs a weekend of presence, judging, prize rules and mentors. Nine at once fails the capacity test for your volunteer crews.

**Plan:**
- **Pilot in 2–3 Ready cities.** Pick them by the scorecard, spread across time zones, and have them run in different months so the network can learn between runs.
- **Network provides a kit, not a mandate.** The kit contains:
  - A format template (one weekend, a themed challenge, 5-minute demos).
  - Judging criteria and a published prize-rules template. Fix these before registration opens.
  - A mentor roster drawn from the other cities and the podcast guests.
  - A code-of-conduct addendum for the event.
  - A sponsor-handling guide, so local sponsors know the rules.
- **Money:** local crews fund their own hackathons with local sponsors, as now. The network's pan-sponsor adds a prize pool or travel grants.
- **Success test per pilot** (baseline numbers, adjust after the first): the event runs on time, projects are submitted, and a measurable share of participants return to a regular meetup within 90 days.
- **Rollout rule:** only after 2 pilots meet the test does the network offer the kit to the remaining Ready cities for 2028. A city can decline at no cost.

**Delete, don't postpone:** a hackathon in any Fragile city, and any plan that requires all nine to run one in the same year.

## Step 4: One deal for nine cities (restructure; sell from Q3 2027)

**The deal as you described it isn't sellable today** because:
- You can't sign for the crews.
- You can't guarantee dates, audience size or venue in any city.
- Local sponsors already hold local relationships. A network deal can collide with them (category exclusivity: two competing companies).
- You have no network-wide audience data to show a sponsor.

**Restructure it into a "Network Partner" package:**

| Element | Design |
|---|---|
| Who contracts | The network vehicle from Step 1, never an individual crew |
| What it funds | The shared layer: podcast, hackathon prize pool and mentor travel, speaker exchange between cities |
| What the sponsor receives | Logo on the network site, podcast sponsor mention, a thank-you at network-wide moments, an annual report with audience numbers |
| What it never includes | Paid speaking slots, attendee lists, editorial control. It may include a stage-time cap of 15 minutes at any participating event |
| City participation | **Opt-in per city.** A city that opts in agrees to display the partner and honor the stage cap. It receives a share of the funds. |
| Local sponsors | Stay untouched. Rule: the network partner is a *network* relationship; each crew keeps full control of its local sponsors and may keep local competitors of the network partner, provided it signs the same conduct rules |
| Category conflict | The network states in the contract which categories it exclusive-sells, and which it doesn't. Don't sell exclusivity you can't enforce. |

**Revenue split (my suggestion, tune with the crews):** a fixed share to the shared layer's operating costs, the rest split equally among opted-in cities. Equal splits are simpler than pro-rata and avoid ranking cities against each other. Agree it with the crews before you approach any sponsor, in writing.

**Price and tiers:** build the price from cost, not from a guess. Use the fully loaded cost of the shared layer (podcast production, prize pool, travel, vehicle admin, your own time) plus the share going to cities. Check it against what each city currently earns from its largest local sponsor. If the network package costs more than the sponsor could spend on a local deal in those same cities, it fails on price. I have no figures from you, so I'm not giving numbers.

**Sponsor timing.** Large sponsors budget annually and sign weeks to months before the year they spend. Approach prospects in H1 2027 with the pilot evidence, aiming to close for the 2028 budget cycle. A 2027 close is possible only for a small first package, so treat it as a bonus.

**Prospects:** the obvious one is the owner of the Kotlin language and tooling, plus companies that hire Kotlin developers. They may already support user groups, so ask what they already fund before you pitch. Because I haven't verified any of their programs, check each directly.

## Calendar

| When | Do | Gate |
|---|---|---|
| Q4 2026 | Send scorecard form; classify the nine cities; choose the vehicle; check name/logo policy | All nine crews answer |
| Q1 2027 | Ratify the charter and sponsor rules with the crews; hire/name podcast producer and deputy; record the first episodes | Crews agree in writing |
| Q2 2027 | Podcast season 1 live; choose pilot cities; ship hackathon kit | At least 2 Ready cities volunteer |
| Q2–Q3 2027 | Run 2–3 hackathon pilots; approach prospects with season 1 data | Pilot test met |
| H2 2027 | Close first Network Partner deal; roll out opt-in to cities | Deal signed through the vehicle |
| 2028 | Offer hackathon kit to all Ready cities; podcast season 2 | Provisional. Re-plan after the pilots |

Anything past Q3 2027 is provisional.

## Scorecard (review quarterly)

| Signal | Target |
|---|---|
| Cities with no gap over 90 days | 9 of 9 (sourced bar: CNCF) |
| Cities with 2 or more organizers from 2 or more employers | Rising; Fragile cities converted first |
| Podcast cadence kept | 100% of planned episodes |
| Cities represented in the podcast | 9 of 9 in season 1 |
| Hackathon pilots meeting their test | 2 of 2 before any rollout |
| Sponsor-rule violations (paid slot, list sharing, stage overrun) | 0 |
| Network Partner funds reaching cities | On schedule, per written split |

## Biggest risks

- 🔴 **Overpromising the sponsor.** Selling delivery you don't control destroys trust with the sponsor and the crews. Mitigation: opt-in package, written rules.
- 🔴 **Eroding crew autonomy.** If crews feel the network is taxing them, they leave and take the brand with them. Mitigation: ratify everything with the crews first, and keep the network's footprint thin.
- 🟠 **Central burnout.** You are the single coordinator. Name a deputy and cap what you personally run.
- 🟠 **Legal and tax surprises** across five or more jurisdictions. Mitigation: use the vehicle and get local advice before the first contract.
- 🟠 **Data protection** for any shared attendee, hackathon or podcast-guest data. Mitigation: collect nothing centrally except what the vehicle needs, and write the consent text once.

## Questions that would change this plan

1. Does any legal entity already hold the name, or does it exist only informally? (Changes Step 1.)
2. Is the hackathon aimed at growth, hiring or sponsor visibility? (Changes the format and who we pick as pilots.)
3. Is the single sponsor deal meant to cover costs or to be a growth engine? (Changes the price and split.)
4. How many hours per month can you personally hold on a bad month? (Caps the podcast cadence and the pilot count.)
5. Do any crews already have conflicting local sponsors in the same category? (Changes the exclusivity terms.)

I can draft the one-page charter, the scorecard form for the crews, or the Network Partner one-pager next. Tell me which one you want first.