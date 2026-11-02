# LatticeDays 10: growth plan check and announcement sequence

I ran this through the `event-growth-strategy` skill. I answered its interview from your message and marked every gap as an assumption. Each gap is a question for you at the end.

## Verdict

❌ **Do not do the plan as written.** Venue step-up, second track and workshop day together make three rungs at once, and the skill deletes that option. The venue jump is 350 → 1,200, about 3.4×, and the skill's rule is no jump past roughly 2× in one edition.

✅ **Do edition 10 as one lever, one rung.** Squeeze capacity at the current venue first, and fall back to a capped step-up of about 600 seats or fewer only if the squeeze fails. Use the anniversary as the story, not as the size.

ℹ️ **Take the 40k EUR, but do not let it set the size.** Details are in Financial gate and Sponsor.

## 1. Demand evidence

| Signal | Your figure | Skill threshold | Status |
|---|---|---|---|
| Sellout, 3 editions in a row | yes | Repeated across editions | ✅ repeated |
| Sellout speed | not given | Well under 1 hour | ⚠️ unknown |
| Waitlist | ~120 on 350 = 34% | 30-50% of capacity | ✅ low end of the band |
| Unsolicited sponsor inbound | one offer, tied to "make it huge" | Unsolicited interest | ⚠️ partial: it is one sponsor, and it is conditional |
| Attendee return, sponsor renewal, sellout-speed trend | not given | Needed for the `event-market-fit` read | ❌ missing |

- **Figure status:** the threshold column is the skill's headroom heuristic, a research synthesis and not an industry standard. Your figures come from your own record. Nothing here is self-set yet.
- **What the waitlist proves:** proven demand is about 350 + 120 = **470 at most**, and less once waitlist drop-off is counted. It does not prove 1,200. The 1,200 room would be about 61% empty (730 of 1,200 seats) at today's demand.
- **Missing demand read:** the skill requires the `event-market-fit` read before any lever. It can be minimal: attendee return rate, sponsor renewal, and sellout minutes for each of the three years. Please send these. Until then, treat this plan as conditional.
- **Check for batch releases:** batch-released ticket drops manufacture sellout speed. If any edition used staggered drops, discount that sellout.

## 2. Ceiling diagnostic

- **Saturation:** not indicated. The waitlist shows the local pool is not tapped.
- **Channel decay:** unknown. If sellout time lengthened over three years, route to `event-marketing-plan` before touching capacity.
- **Quality collapse:** not yet, but this is the risk the plan creates. The documented loop is "intimate → popular → broken open → no longer intimate."
- **Closest precedent:** Brooklyn Beta went from about 300 to a one-day 1,300-person event in a very expensive venue. The founder noted more hiccups than in previous years, and the community said it did not scale from 300 to 1,300. Your plan is about the same ratio, plus two more rungs.

## 3. Reach vs. intimacy call

This is your call, and the plan depends on it.

- **Assumption:** a database-internals conference prizes the hallway track, where people corner the speaker after a talk. If so, you are in the intimacy menu, and the skill warns against drifting into a middle size that serves neither.
- **If the answer is reach:** the growth menu applies, and the recommendation below still holds. The size is capped at about 2× per step.
- **Settle this inside the team first.** The skill says to brainstorm before recommending if the team is split. The 10-year milestone and the 40k offer tilt people toward "bigger." Do not let that decide it.

## 4. Chosen lever and rejected rungs

**Chosen: venue squeeze.**
- Ask the current venue for a layout re-plan. Occupancy and fire-code sign-off bounds it.
- **Precedent:** Rails World fit about a third more attendees into a hall that was already at capacity, using tighter layout and slimmer chairs. A third on your 350 is about **465**, which is almost exactly your proven demand of 470.
- **Fallback, only if the squeeze fails:** a venue step-up capped at proven demand plus a modest buffer, about 500-600 seats. That stays under 2× and avoids the deleted multi-x leap.
- **Decide the fallback trigger now:** if the venue cannot reach at least 450 seats safely, execute the fallback via `event-venue-sourcing`.

**Rejected for edition 10:**

| Rung | Why rejected now |
|---|---|
| Venue step-up to 1,200 | Beyond 2× in one jump, so deleted. Contract exposure sized to aspiration, not proof. |
| Second track | Adds program, not seats, so it does nothing for the 120 waitlisted. It dilutes the hallway track, which is the exact lever intimacy events refuse. |
| Workshop day | Extends every cost line (venue, catering, volunteers, hotel nights) and needs a contract amendment. Same value as a track at higher effort. |

**Sequencing for later:** the skill orders rungs by adjacency, track → day → satellite city. If edition 10 passes all four watch signals, consider a track or workshop day for edition 11. The workshop day can be pitched now as a "coming after the anniversary" teaser. That is a promise to the community, so only say it if the team agrees.

## 5. Financial gate

Venue-touching levers must clear this gate. Squeeze needs the least, and the step-up fallback needs all of it.

- **Deposits:** typically 25-50% at signing, balance due 14-30 days before the event.
- **Attrition and F&B minimums:** owed even when attendance falls short. At 1,200 seats and about 470 attendees, you would owe minimums on roughly 730 empty seats.
- **Lead time:** 9-18 months for 300+ attendee events. If edition 10 is about 12 months out, a step-up is already at the edge. If it is under 9 months, a step-up is not realistic, and squeeze becomes the only option.
- **Contract climate:** post-pandemic venues rarely renegotiate minimums.
- **Exposure cap (self-set, you declare it):** propose that non-refundable exposure (deposit + attrition + F&B shortfall at proven fill) must not exceed money already in hand, and in particular must not depend on the anchor sponsor's 40k. Fill in the number once you have a quote.
- **Whole-product layer** (needed for any bigger edition, even 465): check AV, networking and registration flow at the new scale. Check volunteer bench depth too. If the bench is thin, route to `event-team-structure`.

## 6. Pricing posture

Decide this before the announcement, per the skill.

- **Default:** a public community-price commitment, cross-subsidized by sponsorship. PyCon US held individual prices flat and cut student tickets over 40% across five years of venue growth.
- **Complements:** an early-bird ladder (volume-gated or dated) and an optional supporter tier that funds scholarships.
- **How the 40k fits:** use it to back the price commitment, for example flat individual prices and a funded student or scholarship allocation. Do not use it to underwrite recurring venue costs.
- **Dependency:** the commitment is only as durable as the sponsor base behind it. That is why the sponsor watch signal below matters more once the pledge is public.
- **Price setting mechanics** (exact tiers and amounts) go to `event-ticket-pricing`.

## 7. Sponsor: handling the 40k offer

- The offer is conditional on "huge," which makes it a steer, not a signal. Ask the sponsor in writing what they actually need: logo reach, recruiting access, a keynote slot, or booth traffic. A 465-seat sellout anniversary may satisfy that.
- **Concentration risk:** sponsors budget a year ahead. XOXO ended after sponsorship that had funded about 20% of free passes receded, with attendee signals still warm. If your anchor sponsor withdraws after you have signed a bigger venue, nothing replaces that revenue in time.
- **Declare now:** the maximum share of total revenue any single sponsor may hold. This is self-set. If you have no number, I suggest you pick one before the sale opens. Crossing it counts as a reversal benchmark even in a successful year.
- **Prefer a one-off, ring-fenced use** (anniversary production, student tickets, recordings) over a commitment that creates ongoing obligations.

## 8. Paired mitigation

Never present a lever as free.

- **Squeeze mitigation (the cost of a tighter room):** get the occupancy and fire-code sign-off in writing, and protect hallway and break space. Keep the unstructured-time share of the schedule at least as large as in edition 9, and record every talk.
- **Allocation under the cap:** hold the cap with a first-come waitlist, and keep the waitlist as your demand instrument. The known bias is that first-come favors those with time and money. If group buyers start dominating allocation, add the group-purchase ban. If the cap exists to shape who is in the room, go to application + lottery. That is your answer to Q10, which I need.
- **If you later add a track or day:** the paired mitigation is full recording plus protected unstructured time.

## 9. Watch plan

Any one firing means hold or shrink edition 11, not push through. Thresholds are **self-set and must be declared before sales open**. I list proposals, and you confirm or replace them.

| # | Signal | Proposed trigger (self-set) | Owner | Check date |
|---|---|---|---|---|
| 1 | Sellout speed | Slower than edition 9 at flat or higher capacity | Ticketing lead | 48 h after sale opens, and at end of sale |
| 2 | No-show / attrition rate | Above edition 9's rate | Registration lead | Day 1 of the event, and 2 weeks after |
| 3 | Single-sponsor revenue share | Above your declared threshold | Treasurer / sponsor lead | At each sponsor signing, and monthly until the event |
| 4 | Organizing team says the work is "actively unpleasant" | Any lead says so, or a pulse survey drops under a set level | Lead organizer | Monthly from announcement, and a retro after the event |

I used role names because I do not have your team. Replace each with a person. Convert the check dates to calendar dates once the edition date is fixed.

## 10. Announcement sequence

Principle: **announce only what is signed.** Capacity numbers, price commitments and sponsor names go public after the paper exists. T is the edition start date, which I need from you.

| Step | When | Action | Gate |
|---|---|---|---|
| 1 | Now | Settle the open questions below. Decide reach vs. intimacy. Declare sponsor-share threshold and exposure cap. Run the `event-market-fit` read. | Team agrees in writing |
| 2 | Next 2 weeks | Reply to the anchor sponsor: thanks, what do you need from a 10th edition, written terms for the 40k. Do not commit to a size. | Terms in writing |
| 3 | Next 2-4 weeks | Ask the current venue for the layout re-plan and fire-code sign-off. Request step-up quotes in parallel with smallest deposit and shortest attrition terms, only as the fallback. | Signed capacity figure |
| 4 | After step 3 | Decide: squeeze capacity, or fallback venue. Record the lever chosen and the rungs rejected. | Decision recorded |
| 5 | Same day as the venue contract | Tell the waitlist first (the 120), with early access to the added seats. This is a loyalty reward and also a conversion test of your demand read. | Venue signed |
| 6 | Within a week of step 5 | Tell past attendees and speakers: "10th edition, date, venue, and the price commitment." Share the sponsor's name only if they have agreed. | Sponsor consent |
| 7 | At T-9 to T-12 months | Open the CFP and public announcement: anniversary, date, venue, price pledge. Mention the workshop day only as "being considered for edition 11," if the team agrees. | Pricing posture decided |
| 8 | Sale opens | One release, no batch drops. Record sellout minutes and waitlist size on day one. | Watch thresholds declared |
| 9 | After sale | Update the memory record: lever, rejected rungs, demand evidence, exposure accepted, pricing commitment, the four signal values. | Record saved |

If edition 10 is under 9 months away, steps 3-4 collapse to squeeze only, and the announcement compresses to steps 5-8.

## Questions for you

Answer these and I will tighten the plan.

1. When is edition 10, and when does the current venue contract renew?
2. What was sellout time in each of the three sellout years?
3. Does the cap exist for the hallway track (intimacy) or for logistics only?
4. What share of revenue is the anchor sponsor today, and is the 40k conditional on 1,200?
5. Is edition 10 a one-off milestone, or a step in an annual asset? The skill's compounding mandate favors slower, more durable levers.
6. Is organizing still pleasant? A "no" is a growth signal on its own, and it moves us toward holding or shrinking.
7. What assets do you already have: a trusted venue with room to grow, a deep sponsor bench, a volunteer bench?
8. Do you have past-year attendee return and sponsor renewal data, for the `event-market-fit` read?

## Caveats

- The headroom thresholds, the 2× ceiling and the squeeze ≈ +⅓ figure come from the skill's research synthesis. They are starting heuristics, not industry standards, and your own history overrides them once two or more editions of data exist.
- I filled in no venue prices, because you did not provide quotes. Every exposure number is a formula, not a result.
- I did not run the `event-market-fit` read. The plan is conditional until it exists.