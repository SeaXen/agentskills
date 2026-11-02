# FluxConf: green light for 600 → 1,200 seats?

**Call: 🟠 hold-and-fix. Don't green-light 1,200 yet.** Demand from attendees looks real. The sponsor axis is failing, and sponsors fund the budget. Keep 600 flat, or defer the doubling until the sponsor number is understood.

I ran the interview from my reading of your brief. The assumptions are listed at the end. The composite below is a synthesis of individually sourced thresholds. It is not an industry-standard test.

## 1. Job statement and stage

- **Stage:** edition 3 completed. Lagging signals exist, so they outrank any proxy.
- **Owner:** community-run (paid tickets, external sponsors). I assume this holds. If FluxConf is company-run, sponsor renewal weakens as a signal and the read changes.
- **Attendee job (draft, please confirm):** "When running observability at scale in a region with few peer events, I want to compare real incident and tooling practice with peers, so I can bring back decisions I trust."
- **Sponsor job (the unwritten one):** "When I need observability buyers and practitioners in my pipeline, I want qualified conversations I can trace to revenue, so I can justify next year's budget."
- The sponsor job is the one the data is questioning. 7 of 16 sponsors decided the logo didn't do it.

## 2. Baseline and saturation

- **Baseline:** edition 3's own sales curve is the strongest evidence, so no pre-launch proxy is needed.
- **Saturation scan (not yet run):** check confs.tech, the CNCF and observability-vendor event calendars, and Denver-area dates. Doubling seats widens the buyer pool you compete for, and it competes for sponsor budget too.
- **Size threshold:** the verified thresholds are 7/13/50/90/150, with intimacy breaking around 60–100 participants. 600 is already far past that. At 1,200 the format and the attendee experience change, which could hit the return axis. That belongs to the format sibling.

## 3. Signals: threshold vs actual

| Signal | Threshold | Actual | Confidence | Read |
| --- | --- | --- | --- | --- |
| Attendee return | >30% floor (sourced). About 50% is "healthy" for a recurring event. | 44% | Floor sourced, aim self-set | 🟢 green, but under the healthy mark |
| Sponsor renewal | ≥70% per edition | **9 of 16 = 56%** | Sourced | 🔴 red, 14 points short, 2 sponsors short of 11 |
| Sellout-speed trend | Edition-over-edition trend | 31 days → 9 days | Method sourced | 🟢 green, pending the batching check |
| Attendee survey | No threshold | 4.6/5 | n/a | ℹ️ context, not one of the three signals |

- **Return.** 44% clears the floor, but a tight developer community should beat it. The edition-2 attendee count is the denominator, so please confirm it.
- **Renewal.** The result is 56.25%. To clear 70% you needed 11 of 16.
- **Sellout trend.** Check whether tickets were released in batches. Batching triggers the platform's "almost sold out" banner early and manufactures speed.
  - If sales were organic, a waitlist that formed after the sellout is high-intent evidence. Please send its size.
- **Survey.** Satisfaction isn't return, and it doesn't speak for sponsors. Respondents are the people who showed up and answered.
  - Organizers overestimate the "peak moment" they deliver: 78% believe they deliver one, and 40% of attendees agree.

## 4. Composite read

- **Mechanical score:** 2 of 3 green, which is the scale gate. The team is reading this correctly as far as it goes.
- **Why it still isn't a go:** the one red axis is the high-confidence one. Renewal is deliberate repeat budget money, and it is independent of ticket buzz.
- **The documented failure pattern:** XOXO ended on sponsor-demand collapse while attendee sentiment stayed positive. A sold-out event with falling sponsor demand dies with its watched signals still green.
- **What 1,200 asks for:**
  - Roughly 600 more paying attendees. Nine-day sellouts suggest headroom, but only a waitlist or pace data proves it.
  - Probably more sponsor money to fund a bigger venue. That money is coming from the axis that just lost 44% of its accounts.
- **Two ways to read it:**
  - If demand is real and sponsors left for fixable ROI reasons, the bigger audience is the lever to win them back.
  - If sponsors left because the audience didn't match their buyers, doubling the audience dilutes that fit.
  - The data doesn't separate these yet.
- **Acquisition vs retention:** "did they buy" is excellent. "Did they come back" is good but not great. Report the two separately.

## 5. The call, with the differential

- **Marketing execution gap?** Doesn't apply. Tickets sold out in 9 days.
- **Price misfit?** Doesn't apply. A 9-day sellout points the other way, if anything toward underpricing. That is a question for the pricing sibling, not this verdict.
- **Sponsor-side demand shift?** This is the matching row: attendee signals green, renewal collapsing. The verdict is **hold scale, route to sponsor value-prop and fulfillment work.**
- **Trust, governance or fraud story?** Nothing in your brief suggests it. Confirm that none of the 7 departures were about conduct, governance or a sponsor-experience incident.
- **Genuine concept or demand failure?** No evidence. Pivot and stop are off the table.

**Two diagnostics to run before the next scale call, as read-only checks:**
1. Did all 16 sponsors get a 72-hour post-event ROI report with leads, sessions, and attributable pipeline? If not, 56% may be a reporting failure rather than a value failure.
2. Why did the 7 leave? Ask each. The reason is either "no ROI", "budget cut", "audience mismatch" or "logistics". Each points to a different fix, and only "no ROI" or "budget cut" would be unaffected by doubling seats.

**What turns this into a go:** re-read the three signals together next cycle. Renewal at or above 70% on the edition-4 sponsor cycle, with return holding at or above 44%, would make 2 of 3 green with the sponsor axis fixed. If the venue deposit deadline lands before sponsor commitments do, treat the deposit as the risk to avoid. A smaller step (say 800 seats) is a scaling choice for the growth sibling, not something I can validate from these numbers.

## 6. Routing

- **Sponsor diagnosis and ROI reporting:** `samber/dev-event-organizer-skills@event-sponsor-fulfillment`.
- **Scaling levers, once the composite is green:** `event-growth-strategy`. It consumes a green read and is blocked until then.
- **Format at 1,200 seats, if pursued:** `event-format-selection`.
- **Underpricing question:** `event-ticket-pricing`.

## Assumptions to confirm

1. FluxConf is community-run, with paid tickets and external sponsors.
2. The 44% return rate is measured against the edition-2 attendee list. It could be a survey-intent number, which would be weaker.
3. Sellout speed was organic, with no batched releases.
4. Edition-1 and edition-2 sponsor counts weren't given, so I can't see the sponsor trend across editions.
5. The venue deposit deadline is unknown. A near deadline would argue for fast instruments, and I'd need it to date the re-read.