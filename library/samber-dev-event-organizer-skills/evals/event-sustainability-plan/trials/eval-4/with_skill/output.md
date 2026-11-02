**Verdict: I can't confirm the carbon saving. The data you gave doesn't contain it, and "going fully hybrid fixes the footprint" is a claim the evidence doesn't support.**

Next action: pull last edition's registration by country and origin, and send me the in-person ticket price and an AV/streaming quote. Those three inputs turn the ranges below into a real estimate and let me finish the pricing.

## 1. Why I can't confirm it

- A remote tier saves only the trips of people who switch from in-person to remote. Everyone who still flies is unchanged.
- Remote buyers who would never have come add a small digital line and save nothing.
- The 55% who fly in (40% US, 15% Europe/Asia) are not equal. Long-haul flyers carry most of the travel line. In the studies the skill cites, 10% of trips produced about half the emissions at one meeting, and 36% of attendees produced 75% at another.
- The board's "fully hybrid" outcome depends on uptake, and uptake is the weakest evidence. ACM CHI lost money on full hybrid and dropped remote attendance. ACM SIGMETRICS stopped hybrid for lack of participation.
- Time zones hurt your target group. Toronto is about 5-6 h behind western Europe and 10-14 h behind Asia. Live sessions land at night for Asian attendees. Their remote tier is mostly replay, which lowers engagement and willingness to pay.

**Format check:** the format call belongs to `event-format-selection`, and I never decide format for carbon alone. The board decided, so I treat "hybrid" as proposed until that sibling confirms it.

## 2. Saving ceiling (formula, not a point estimate)

No emission factor is typed from memory. Replace the placeholders with your own computed values.

`Saving (% of total) = T × [ M_EA × u_EA + M_US × u_US ]`

- `T` = travel share of the total footprint. Published conference studies put it at 80-97%. They are mostly science conferences and modelled, so label it "estimated".
- `M_EA` = Europe/Asia share of travel emissions. **To compute** from registration data.
- `M_US` = US share of travel emissions. **To compute.**
- `u` = share of that group that switches from in-person to remote.

Illustration only. `M_EA` values are hypothetical until you compute them, and I assume `u_US = 0`:

| `M_EA` (hypothetical) | uptake 10% | uptake 30% | uptake 50% |
| --- | --- | --- | --- |
| 30% | 2-3% | 7-9% | 12-15% |
| 45% | 4% | 11-13% | 18-22% |
| 60% | 5-6% | 14-17% | 24-29% |

- Each cell is the saving as a share of the total footprint, using T = 80-97%.
- Even if half of Europe and Asia switched, the saving is a fraction of the total, not a fix.
- 15% of 1,200 is 180 people. A 30% uptake is 54 remote tickets.
- Subtract the digital line (streaming, devices). It is usually small and should be reported as estimated.
- Rebound risk: remote buyers who add nothing to the saving inflate the ticket count while the footprint stays flat.

**Concentration line to write once the data is in:** "Europe/Asia attendees are 15% of participants and [M_EA]% of travel emissions."

**Lever profile:** I can't pick between the long-haul profile (long-haul above about 60% of travel) and the domestic-flying profile until `M_EA` is computed. The 40% US group is mixed: New York to Toronto is short, the US West Coast is medium. If `M_EA` falls between 40% and 60%, show both profiles. Toronto sits well for a North American audience, so the off-centre host-city override is unlikely to fire.

## 3. Nudging Europe and Asia to remote: I won't design it as asked

- The skill's rule is "Offer, never steer one region to it." Region-targeted nudges also single out people by origin and flight footprint, which the skill forbids.
- Regional steering also risks pushing out speakers and grant recipients whose access commitments sit with `event-accessibility-inclusion`.
- A nudge that works against the long-haul group is the one most likely to lower their engagement.

**What I'll design instead (same for every registrant):**

1. Show the same three options to everyone at equal prominence: in-person, remote live, remote on-demand. Don't geo-target the page, email or pricing.
2. Collect origin and planned mode for everyone (required, with "prefer not to say"). This is the measurement field, not a nudge.
3. Offer every speaker a remote slot with the same length and billing. Travel grants stay unchanged and are never swapped for remote.
4. Build a timezone-friendly block on the programme (a replay hour or a Europe-friendly live block). It helps remote buyers in every region without targeting any.
5. State the remote tier's carbon logic once, neutrally, for all: "Remote tickets avoid travel emissions. We report how many used them."

## 4. Remote tier design (provisional; the format sibling decides)

**Platform criteria** (pick after the AV quote; no vendor claims invented here):

- Low-latency live stream plus on-demand replay available within hours.
- Live captioning, to match published access commitments.
- Moderated Q&A and chat.
- Per-session analytics: watch time, concurrency, replay completion. These are your engagement evidence for the next decision.
- Export of aggregate data only. No attendee origin fields in sponsor exports.

**Pricing logic** (in-person price unknown, so formulas):

- Break-even remote tickets `N = incremental hybrid cost ÷ (49 − marginal cost per remote attendee)`.
- Cannibalization cost per switch = `(in-person price − 49) − costs saved` (badge, catering, seat).
- The $49 price is a commercial decision, not a carbon one. A lower price raises uptake but also raises cannibalization of in-person revenue.
- Test remote live vs remote on-demand as two SKUs. Don't price by region.
- Route the cost lines to `event-budget` and any sponsor-visible changes to `event-sponsor-pricing`.

## 5. Lever plans (choose one)

| Plan | This edition | Next edition | Trade-off |
| --- | --- | --- | --- |
| A. Board plan: fully hybrid now | Everything streamed, $49 remote tier | Review | Highest AV cost, uptake unproven, carbon saving unknown until measured |
| **B. Recommended: quick rungs + universal remote pilot** | Organizer travel policy, remote speaking option, plant-based default, venue energy ask, remote tier offered to all as a measured pilot | Decide on cadence or hub from measured uptake and engagement | Smaller claim now, evidence for the next call |
| C. Structural | Same as B | Biennial or alternating in-person/online years | Largest value, largest effort, splits the community |

I recommend B with a decision gate: if measured switches are under your threshold, the tier doesn't scale. Your effort ceiling (owner and hours per month) is still open. Structural rungs that miss it become next-edition commitments.

## 6. Closed and open (assumptions to confirm)

- **Closed:** none confirmed. Board agreement is a decision, not a signed contract.
- **Open, ask me:** venue contract status, streaming/recording today, in-person ticket price, registration form status, speaker count and grants, effort ceiling and deadline, where tickets are marketed (Canada, US, EU?).

## 7. Boundary (9 categories)

| Category | In/out | Owner |
| --- | --- | --- |
| Travel | in | organizer (event-paid trips); participants' own trips counted, owner named |
| Accommodation | in | organizer inventory, hotels' own too |
| Food and beverage | in | caterer |
| Energy | in | venue (also reports it) |
| Production and materials | in | organizer |
| Waste | in | venue/caterer |
| Local transport | in if material | organizer |
| Freight | in if material | sponsors |
| Digital (streaming) | **in, because you stream** | organizer |

Count attendees, speakers, volunteers and sponsor staff as separate rows.

## 8. Data capture schedule

- **Before registration opens:** origin city or distance band, main mode, nights. Required with "prefer not to say". Fallback is billing country, labelled estimated.
- **Before venue and caterer signature:** metered kWh, supply type, meals by menu, food waste kg, donation partner.
- **Remote tier:** per-session watch time and replay completion.
- **After event:** a one-question survey on actual mode. Delete raw values after the report is published.

## 9. Sibling handoffs

- `event-format-selection`: footprint delta per option, plus the uptake and engagement caveats above.
- `hybrid-event-design`: builds the remote side if the format is confirmed.
- `event-budget`: AV cost, break-even `N`, any contribution line.
- `event-accessibility-inclusion`: travel grants and access exceptions override every lever.
- `event-sponsor-pricing`: any change to sponsor-bought swag or lanyards.
- `event-hospitality`, `event-vendor-sourcing`, `event-landing-page`: plant-based default and food-waste ask, contract clauses, publishing the page.

## 10. Draft public page (pre-event variant; fill brackets from your own data)

> ### Our footprint
> We estimate [low]-[high] t CO2e for RiverforkJS [edition 6] (screening estimate), [low]-[high] t per attendee. Method: Net Zero Carbon Events categories, [factor set and edition], flights with radiative forcing. Registration answers give travel; venue energy and catering are measured from this edition; materials are estimated.
>
> ### Where it comes from
> Travel is the large majority of our footprint. Attendees flying from Europe and Asia are 15% of participants and [M_EA]% of travel emissions.
>
> ### What we change this edition
> - Every speaker may present remotely, with the same slot and billing. Travel grants are unchanged.
> - Lunch is plant-based by default, other meals on request.
> - We offer a remote ticket to everyone, alongside in-person tickets, and will report how many used it.
>
> ### What we will change next edition
> - We will review measured remote uptake before deciding on cadence or hubs, and report the result here.
>
> ### How you can help
> Tell us how you travelled at registration. It is how we measure.
>
> ### What we do not claim
> We do not call this event carbon neutral.

**Claim cautions:** don't write "hybrid cuts our emissions by X%" or any future target without a verified plan. Offsets can't support a neutral claim. Canada's Competition Act requires substantiation, and EU rules apply if tickets are marketed to EU consumers. This isn't legal advice, so get a qualified review before publishing.

## 11. Post-event report skeleton

| Category | In/out | Activity data | Factor (set, edition) | Low | High | Quality | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Travel | | | | | | | |
| Accommodation | | | | | | | |
| Food and beverage | | | | | | | |
| Energy | | | | | | | |
| Materials | | | | | | | |
| Waste | | | | | | | |
| Local transport | | | | | | | |
| Freight | | | | | | | |
| Digital | | | | | | | |

Then, in order:
1. Totals and per attendee, as ranges.
2. Concentration line.
3. Screening estimate versus result, with the main reason for the gap.
4. Actions taken and their labelled effect (remote switches counted separately from remote-only buyers).
5. Boundary or factor changes since last edition.
6. Data coverage (target at least 80%).
7. Waste kg and kg donated.
8. Next-edition commitments.
9. Contribution, if any, on its own line.

## Next

Send me last edition's registrations by country, the in-person ticket price and the AV quote. I'll compute `M_EA`, fix the profile and replace the placeholders with a real range.