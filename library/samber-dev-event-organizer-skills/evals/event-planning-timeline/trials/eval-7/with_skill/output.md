# Foundry Jam: work-back milestones

Don't compress the 9-month conference timeline. A conference runway and a hackathon runway differ for structural reasons, and the timeline skill lists borrowing another format's runway as a failure mode. The conference version carries a CFP-to-program pipeline of about 4 months and venues that book a year out. A hackathon has neither. The sourced hackathon runway is 4–9 months (Major League Hacking organizer guide), and your three candidate dates already fit it.

I'm assuming Q2 means 2027. Today is 2026-10-14, so you have about 28 weeks to the earliest candidate and about 36 to a late-June one. Nothing needs compressing. The real risk is that the date isn't locked, which delays every foundational step.

## Open questions

I can't ask these one at a time here, so I've written the plan on the assumptions below. Tell me where they're wrong.

1. **Who runs it?** I assumed community-run, with volunteer hours as the binding constraint. A company-run event can spend money to recover slips.
2. **One-off or the start of an annual event?** I assumed one-off. If it's annual, the date and the visible scope cost more to change.
3. **Who owns each track?** Today, who owns the venue relationship, sponsors and ticketing? Each track needs exactly one owner.
4. **How many organizers, from how many organizations?** The sourced team floor is 3 organizers from 3 organizations before the venue or date is locked. A university co-host may count as one of them.
5. **Is the budget funded by sponsors not yet booked?** I assumed yes, which turns on the Good/Better/Best scope ladder below.
6. **Is the university also the venue, and does it allow overnight access for 48 hours?** This changes the contract more than any other item.

## 1. Anchor and tracks

**S = doors-open.** Plan to the earliest candidate weekend. The later two then give you slack you chose not to spend. Don't pad every milestone to use it.

Date and venue are one negotiation. Holding several candidate windows open improves venue availability, so give the university all three. Picking the date itself belongs to `event-date-selection`. Student calendars matter here, and I haven't checked the 2027 exam periods.

**Date gate (do this now):**
- Ask the university for a written answer by a fixed date.
- The latest safe answer date is S(earliest) − 4 months. Roughly: early May means early January, late May means late January, mid-June means mid-February.
- If there's no answer by then, drop the earliest candidate and re-anchor on the next one. Moving the date is legitimate until you announce it.

**Tracks.** A hackathon has no CFP, so I trimmed the taxonomy. This follows MLH's 5-function team.

| Track | Owner (one person) | Terminal milestone |
|---|---|---|
| Venue & logistics (includes hardware kits) | Logistics | Final walkthrough, S−1 week |
| Sponsors & budget | Finance | Agreements signed and fulfillment scheduled |
| Marketing & registration | Marketing | Final headcount frozen |
| Judges, mentors, challenge design, volunteers | Operations | Briefing, S−1 week |
| Lead organizer (decisions, gates, checkpoints) | Lead | Doors open |

## 2. Work-back table

Offsets are sourced from the MLH hackathon runway unless marked otherwise.

| When | Venue & logistics | Sponsors & budget | Marketing & registration | Operations |
|---|---|---|---|---|
| **S−9 to S−4 mo (now → date gate)** | Venue locked, including overnight access for 48h. Contract signed. Deposit is a latest-safe commitment, not automatic. | Draft budget and costed Good/Better/Best tiers | Code of conduct, neutral shared alias and credential vault before any public listing | Track owners confirmed. Team gate checked. |
| **S−4 mo** | Hardware needs list drafted (my addition) | Prospectus assembled. Outreach starts. | Placeholder site live | |
| **S−3 mo** | Logistics planning begins | Sponsors in talks | Marketing starts. Main site live. Registration opens. | |
| **S−2 mo** | Food and vendor work begins | Agreements signed | Early-bird or first selection wave closes | Judging and mentorship plans drafted. Judges and mentors booked. |
| **S−1 mo** | Run-of-show, dietary requirements, transport | Fulfillment scheduled | **Final headcount frozen** | Volunteer roster done |
| **S−1 wk** | Physical setup, emergency plan, full run-through | | Reminder emails | Judge and mentor follow-up |

**Hardware track (my judgment, not in the sourced runway).** A hardware hackathon adds work the sources don't cover:
- Parts and kit procurement.
- Bench, power and soldering policy.
- Safety rules.
- Overnight access and sleeping arrangements.
- Insurance.

Start these at venue lock, since the contract has to allow them.

**Order the kits on a headcount estimate.** Supplier lead times can force the kit order before the final headcount freezes at S−1 month. Order at about S−2 months on the registration count, with a margin, and top up later. Shipping and customs lead time is the one place milestone padding is legitimate.

## 3. Cross-track gates

Each gate names both sides.

1. **Code of conduct published ⟸ first public listing.** This is the earliest hard gate, ahead of venue and date.
2. **Payment handling live ⟸ date announced.** If attendance is free, this reduces to "able to receive sponsor funds and pay vendors". That reduction is my judgment.
3. **Venue contract signed ⟸ date announced.**
4. **Team gate (≥3 organizers from ≥3 organizations) ⟸ venue or date locked.**
5. **Draft budget approved ⟸ sponsor prospectus assembled.** Tiers are priced from the budget gap.
6. **Judges and mentors confirmed ⟸ schedule published.**
7. **Final headcount frozen ⟸ catering order.** Hardware kits follow the exception above.
8. **Track owners confirmed ⟸ every track's first milestone.**

## 4. Latest-safe commitment dates

Hold each of these open until its date. Adding plates or seats late is cheap. Unwinding a deposit or an over-order is not.

| Commitment | Latest-safe date | Owner |
|---|---|---|
| Venue deposit | The contract's own deadline. Don't pay early just because cash is available. | Finance |
| Hardware kit order | Supplier lead time + shipping margin, about S−2 mo (to confirm with a supplier quote) | Logistics |
| Catering order | The caterer's real lead time, after the headcount freeze | Logistics |
| Swag and print run | Printer lead time. Artwork locks about 4 weeks out if sponsors are printed on it. | Marketing |

## 5. Checkpoints

The thresholds are yours to set. I've left them blank rather than invent numbers. Demand thresholds belong to `event-market-fit`.

| Date | Condition | Pre-written action | Owner |
|---|---|---|---|
| S(earliest) − 4 mo | No written date and venue answer from the university | Drop the earliest candidate. Re-anchor on the next weekend. | Lead |
| S−3 mo | Payment handling or the code of conduct not ready | Delay the announcement. Never announce without them. | Lead |
| S−2 mo | Sponsor revenue below the Better-tier threshold | Downgrade one tier. Cut the scope items costed for that tier. | Finance |
| S−2 mo | Registrations below the threshold you set | Escalate the community outreach push. Hold the kit order at Good-tier quantity. | Marketing |
| S−1 mo | Any gate into the final month still unmet | Fire the replan procedure. Cut the item whose removal unblocks the most downstream work. | Lead |

**Standing rule:** once the date is announced, it holds and scope moves.

I deliberately left out a weekly per-track review. With volunteers and no standing meeting, it turns into a meeting invite nobody accepts. The pre-written checkpoints do that job instead.

## 6. Dropped from the conference timeline

- **CFP, selection vote and speaker confirmation.** Replaced by judge, mentor and challenge design at S−2 months.
- **A 9-role delegated team.** The 5-function team fits a hackathon.
- **A T−12-month venue search.** Hackathon-scale venues don't book that far ahead, and a university venue is a single negotiation.

## Next steps

1. Send the university your three candidate weekends, with an answer-by date.
2. Name the five track owners and check the team gate.
3. Answer questions 1–6 above so I can lock the owners and thresholds.

I haven't checked 2027 student calendars, so which candidate weekend suits students is still open. Once the date is locked, I can turn this into a dated tracker.