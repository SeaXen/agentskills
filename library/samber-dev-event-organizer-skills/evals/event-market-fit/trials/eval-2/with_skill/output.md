# Kernel & Crust, edition 2: demand read at day 5

**Short answer:** the event isn't dying on this evidence, and it isn't healthy either. Day 5 is too early for a verdict, and a public 30% cut is the wrong first move. The call is a **provisional hold with a diagnosis**, and the next read is at day 14.

I used the `event-market-fit` skill. It normally interviews one question at a time. You asked for the full answer, so I made assumptions where data was missing and listed the questions at the end.

## 1. Job statement and stage

- **Stage:** tickets on sale, with one completed edition. Mid-sale data and last year's own results beat any pre-launch proxy, so I read those first.
- **Job statement (draft, please confirm):** "When I'm the only systems programmer in my company, or I'm evaluating Rust/Zig/kernel work, I want to validate my approach against peers and meet 20 relevant people in a day, so I can [outcome]."
- Edition 2 has two forces working against it:
  - **Anxiety is lower** than it was for edition 1, because the event is now proven.
  - **Habit is stronger.** Conference budgets and travel plans have already been spent elsewhere this year.

## 2. Baseline and the real number

| Figure | Value | Note |
|---|---|---|
| Tickets reported | 38 | |
| Comp codes redeemed | 12 | speakers and sponsors, not demand |
| **Paid demand** | **26** | 5.2% of 500 |
| Last year at day 5 | 61 | |

- **Comp redemption is not demand.** 12 of 38 (32%) are free codes, so the real number is 26. The skill requires judging the curve net of comps.
- **The comparison to last year depends on one fact I don't have.** Did last year's 61 include comps?
  - If 61 was gross, the gap is 38 vs 61, or −38%.
  - If 61 was net, the gap is 26 vs 61, or −57%.
  - Either way it is a gap, and the net-vs-net comparison is the only honest one. Please check before anyone quotes a percentage.
- **One data point is not a curve.** Sales are U-shaped: an announcement spike, a quiet middle, and a final surge. A day-5 snapshot tests reach, not demand. The skill treats week two as the first real read.

## 3. Instruments: thresholds declared now, before more data arrives

These are thresholds I propose you set before you look at the next numbers.

| Signal | Threshold | Actual | Label | Read |
|---|---|---|---|---|
| Pace index vs. edition-1 own curve (net of comps) | ≥80 at day 14 | 26 ÷ (edition-1 net at day 5), so 43 to 62 | method sourced; gate synthesis | 🔴 early, unconfirmed |
| Early-bird close | ≈15% of expected net sales | unknown | sourced | ⏳ pending |
| One month out | 40–50% of expected net sales | not reached | sourced | ⏳ pending |
| One month out, if the visibility push is skipped | 25–30% | not reached | sourced | ⏳ pending |
| Attendee return from edition 1 | >30% | unknown | sourced floor | ⏳ need data |
| Sponsor renewal | ≥70% | unknown | sourced | ⏳ need data |

- **The pace index is the weakest part of this table.** I can't give an exact figure until I know whether the 61 was net, and 80 is a gate I'm proposing. The skill's own sourced stop trigger is a pace index persistently below 80 at the one-month checkpoint across two editions. You are nowhere near that test yet.
- **Edition 1 gives you the strongest signals, and you haven't read them yet.** Attendee return and sponsor renewal are lagging signals, which carry the highest confidence. Read them before trusting any day-5 number.

## 4. The failure differential

Three explanations fit a slow start. They need different responses, and only the third is a verdict on fit.

1. **Marketing execution gap.** Did the speaker or agenda announcement go out? Did the last-edition attendees get emailed? Did the visibility push start? Teams that skip it sit at 25–30% at one month instead of 40–50%. This is the most common cause of a slow start and the most fixable.
2. **Price misfit.** The signature is healthy page traffic with low conversion in the first two weeks. You haven't told me traffic or conversion yet, and this is the check that would justify touching price.
3. **Genuine demand gap.** The signs are low traffic, weak CFP oversubscription, and falling return or sponsor renewal.

## 5. The call, and why not the 30% cut

**Call: provisional hold-and-diagnose.** It is not go, pivot, or stop.

- The call currently rests on one signal class, sales. The skill requires at least two independent classes before any verdict. Edition-1 return, sponsor renewal, and this year's CFP oversubscription would supply them.
- **I'd advise against a public 30% cut this week**, for these reasons:
  - **It's premature.** Nothing distinguishes a price problem from an execution problem yet. A cut is the price-misfit response, and you haven't shown that diagnosis.
  - **It teaches the audience to wait.** Public cuts train buyers to hold off until the next discount.
  - **It hurts the 26 who already paid.** They will want refunds or credit, and early buyers are your most loyal segment.
  - **The volume maths is poor.** Holding revenue after a 30% cut needs about 43% more tickets (1 ÷ 0.7). Your fixed costs don't shrink, so the margin falls further.
  - **It signals weakness** to sponsors, who fund the budget. The event the skill cites that died on sponsor demand kept positive attendee sentiment until the end.
- If the diagnosis does point at price, the skill's preferred response is targeted codes or bundles, not a public discount. That work belongs to `event-ticket-pricing`.

**What would change my call:**
- Pace index still below 80 at day 14, with healthy traffic but low conversion → price misfit → route to pricing.
- Pace index low and the visibility push never happened → execution gap → route to marketing, then re-read.
- Return below 30% or renewal below 70% → hold the format flat and fix the experience or sponsor ROI before pushing sales.
- CFP undersubscribed → the audience for this topic is smaller than hoped, so scale back toward meetup size.
- Pace index below 80 at one month out in both editions → pivot.

## 6. Routing

- Execution gap → `event-marketing-plan`.
- Price misfit → `event-ticket-pricing`.
- Genuine demand gap and a pivot → `event-positioning`, with a brainstorm first.
- Green read → `event-growth-strategy`.

## Questions I need answered

1. Did last year's 61 at day 5 include comps? What was edition 1's final attendance and its sales curve at days 14 and 30?
2. How much of edition 1's attendance has re-bought? What is your sponsor renewal so far?
3. How many CFP submissions did you get, for how many slots?
4. What is the traffic-to-conversion ratio on the ticket page?
5. When does the early bird close? Has the speaker or agenda announcement gone out? Have the last-edition attendees been emailed?
6. Is there a hard date, such as a venue deposit, by which the go/no-go call must land?
7. Is your co-organizer's concern price, or momentum? A visibility push or sponsor-driven bundles might answer the momentum concern without cutting the price.

Send those and I'll tighten the read to a final call.