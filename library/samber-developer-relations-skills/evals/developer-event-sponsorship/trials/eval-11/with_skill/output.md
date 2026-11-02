Reject finance's 41% as a target, not just as a number. All three asks collapse into one budget reset, not three separate cuts. Details below — skills applied: devrel-budget-allocation for the reset, developer-event-sponsorship Step 8 for wind-down, dev-event-organizer-skills (corporate-event-strategy) for new conference, oss-sponsors-brand-strategy for OSS line. Meetup skill doesn't apply — recurring-evening format only, not a one-day conference.

## 1. Kill 41% as stated, before anything else

That number is DevRel.Agency's 2024 State of Developer Relations survey: mean 41.1%, n=47, respondent shares summed to 104.5% (overlapping multi-select, inconsistent base). Sourced, real, but describes where the field's money went — never a target for one company. Quoting it as a target is the exact named failure mode in this skill's own list.

Two more catches before finance gets an answer:

- Does your 55% include staff time (prep, travel, booth staffing), or fee/cash only? ~60% of surveyed programs exclude salaries. Cash-only 55% likely understates real share once hours count.
- "By Q3" — today is 2026-09-20. Calendar Q3 ends in 10 days. Confirm they mean fiscal Q3 of next year, not this one — large sponsorship contracts close roughly a quarter ahead, so an actual Q3-2026 deadline is already unreachable regardless of target.

## 2. Zero-base, don't trim

Rule: zero-base the whole devrel budget when the driver changes OR the envelope moves >20%. You have both — stopping one spend category, starting two new ones. Don't shave the existing 55% number down. Rebuild it.

## 3. Exit third-party sponsorships (Step 8, per contract)

Pull every signed contract's notice date and cancellation-fee curve first. Large-conference contracts close ~1 quarter ahead (KubeCon NA 2026 required signed contracts by Aug 14 for a November event) — assume similar exit windows bind you now.

Default verdict per contract: **Drop**, strategy pivot. Exception: a contract past its notice date for the next edition is committed spend this cycle, exits at the one after. This frees cash on each contract's own schedule, not on a single Q3 date.

## 4. Run the one-day conference (route: dev-event-kickoff → corporate-event-strategy → event-first-edition/event-budget)

Gates implied by your ask: event doesn't exist yet, company funds and owns it, first edition. That's `corporate-event-strategy` territory first, not format/venue work yet.

- **Goal**: don't default to pipeline. Only claim pipeline if attendees are the actual buyer and a sales-system join exists. Otherwise this reads as reach/credibility or ecosystem goal — say which, before building anything.
- **Ownership**: marketing sole owner by default, unless product or sales are already asking for this event.
- **3 mandatory reviews before registration opens**: legal (company's name on a room it doesn't fully control), data (attendee list into sales systems is a separate approval), hospitality (guest travel/gifts vs each guest's own employer's rules — public-sector guests especially).

**Cost warning**: a self-run conference is not automatically cheaper than sponsorship. Fully loaded = venue + AV + catering + staff prep + travel — staff time is the line most teams omit and the one that most often doubles the total. Don't promise finance a number until `event-budget` produces a real one.

**Trade-off finance won't ask about**: stopping every sponsorship kills your presence in ecosystems you don't already own. One flagship event reaches people who already showed up; sponsorships reach rooms you're not in. If "awareness in a new ecosystem" is a real goal, this move deletes the only route to it.

## 5. The $30k/year OSS line

Push back on the VP before accepting "comes from event budget" — that's a choice, not a rule, and it has a real cost.

- **Mandate mismatch**: "projects our product depends on" is a supply-chain assurance mandate, normally owned by engineering or security, not DevRel. Folding it into the events line mixes a security mandate into a marketing spend category. Ask whether engineering should co-fund or own this instead.
- **Sizing check**: industry floor is $2,000/developer/year (Open Source Pledge). One company self-reported paying $3,700/developer. $30k covers ~15 developers at the floor, ~8 at the higher figure — need your dev headcount to know if $30k is a real commitment or a token one.
- **Model**: breadth (small automatic amounts across the full dependency graph) fits a supply-chain mandate and a modest budget best. Needs an SBOM or lockfile to resolve targets.
- **Procurement catch**: the major sponsorship platform's invoiced billing needs a $5,000 minimum per invoice. $30k split thin across many projects may not clear that — route through a fiscal host, or pay by card.

## 6. Does 41% actually happen — worked check

Numbers below are illustrative placeholders. Swap in your real total budget and `event-budget`'s real conference cost.

Assume total discretionary devrel budget = $500,000/year. Current: events 55% = $275,000; everything else 45% = $225,000 (untouched by this reset).

| Scenario | New conference (fully loaded) | Events % of total | Verdict |
|---|---|---|---|
| Low case | $150,000 | 30% (+6% if OSS folded in = 36%) | Clears 41% easily |
| High case | $300,000 | 60% (+6% if OSS folded in = 66%) | Worse than today, even after killing every sponsorship |

OSS sitting inside or outside "events" moves the number by ~6 points either way. The conference's real fully-loaded cost decides pass or fail — not the bookkeeping fight with the VP.

## 7. Answer these before locking any number for finance

1. Real total discretionary devrel budget, salaries in or out.
2. Which fiscal quarter "Q3" actually means.
3. Every signed sponsorship contract's notice date and cancellation fee.
4. Developer headcount (sizes the $30k check).
5. Does the attendee buy your product, or does someone else? (locks what the new conference can honestly claim)

**Next:** run `event-budget` (dev-event-organizer-skills) to get a real fully-loaded cost for the one-day conference. Nothing above resolves finance's 41% question until that number exists.