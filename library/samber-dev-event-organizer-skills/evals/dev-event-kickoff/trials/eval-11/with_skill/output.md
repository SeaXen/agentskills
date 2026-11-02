**Kelpway Conf 2027: kickoff result, 2026-10-12**

⚠️ The files you named (`budget-2027.xlsx`, `schedule-grid.pdf`, `venue-contract-signed.pdf`) are not in my working directory, which is the example-repo repo. I haven't read them or the Kelpway git log. Everything below comes from your description. I haven't written `event-context.md` either. A draft is at the bottom, ready to commit in the Kelpway repo.

**Do this first:** answer the five questions in the next section. Reply in one line, for example `3c 4a 5? 6 2027-08-xx 7c`.

## Detected, so not asked

- **Block (Q1): (b), decided and being planned.** A signed venue, a committed budget and a published grid put you here. Doors are far off, so the on-site and after-event blocks are not live.
- **Format (Q2): (c), fully fixed.** Two days, three tracks, in-person. I record it as a gate and won't revisit it.
  - Gates opened: `in-room` (physical room) and `conference` (more than one track).
  - Gates still unknown: `hackathon` and `workshop`. The grid should say whether either exists.
  - Gates closed: `virtual` and `hybrid`.
- **Date (Q6): (a), doors on a fixed date.** That is about 2027-08, and I need the exact day.
- **Budget:** break-even is 410 tickets and the budget is committed, so the money-model work is nearly done.
- **Git log (your report):** work stopped about 2026-09-23. The grid went public about 2026-09-28, which is after that. So either the published grid isn't in the repo's history or the repo copy is stale. Check this, because it means the repo may not show the real state.

## Questions I still need

1. **Q3. Edition and properties?**
   - (a) First edition of something new
   - (b) One-off
   - (c) Edition 2 or later
   - (d) More than one property
2. **Q4. Who funds and organizes?**
   - (a) Volunteer organizers
   - (b) A company funds and owns it
   - (c) Foundation or non-profit
   - (d) Mixed
3. **Q5. Goal of this session?** No answer can stand in for this. Why did work stop 19 days ago, and what do you want unblocked?
   - (a) Pick up where the repo left off
   - (b) Revive the team
   - (c) Fix a specific problem. Name it.
   - (d) Don't know. I need the lay of the land.
4. **Q6. Exact doors date?** Also say whether any of these exist: an on-sale date, a CFP deadline, a sponsor budget window.
5. **Q7. One-off or standing, and your effort ceiling?**
   - (a) One-off, hours only
   - (b) One-off, a week of work is fine
   - (c) Standing, a few hours weekly
   - (d) Standing, with paid staff or a funded budget

Three extra checks, which count as part of the detection. They are not extra interview questions.
- Are the talks on the published grid confirmed, or is it a placeholder?
- Is a ticketing system live, and have tickets been on sale?
- Is there a rate card or any signed sponsor?

## Route (provisional until Q5)

**`samber/dev-event-organizer-skills@event-planning-timeline`**: the work-back plan from doors-open, track by track. It shows what slipped during the 19-day silence.

This is a default for "get me going again". If Q5 names a specific problem, I re-route to the skill that owns it.

## Short-list, value per unit of effort, highest first

1. **`event-planning-timeline`** attacks the unknown stall damage. It costs one session and no external commitment.
2. **`event-ticket-pricing`** attacks the fact that 410 tickets is a break-even with no price ladder behind it. The money model jumps above fill-the-room because the committed budget makes it nearly free. The cost is a modelling session, and a published refund policy then binds you.
3. **`event-marketing-plan`** attacks registrations, the input everything else assumes. The fixed doors date promotes this class. It costs a campaign and the list consent you then owe.
4. **`event-landing-page`** attacks the gap between a public grid and a date-gated front door. The cost is a build, and the public CTA states commit you.
5. **`event-risk-management`** attacks a signed contract whose cancellation-fee rungs and go/no-go dates may not be tracked. The signed venue promotes it. The session is cheap, but each fee rung binds you on the venue's terms.
6. **Sponsorship slot, held for Q4/Q7.** I found no rate card. If Q4 is (a) volunteer or (d) mixed, `event-sponsor-value-proposition` enters here. If Q4 is (b) company-funded, `corporate-event-strategy` goes to rung 1 and sponsorship drops. A closing sponsor window (Q6c) would promote the sponsorship class to rung 1.

## Chain

Each link consumes what the one before it produced.
1. `event-planning-timeline` produces the dated plan.
2. `event-ticket-pricing` produces the ladder and refund policy.
3. `event-marketing-plan` produces the campaign calendar.
4. `event-landing-page` carries the campaign's dated CTAs.

## Not now

- `event-run-of-show`, `event-production`, `event-attendee-experience`, `event-hospitality`: after Q1 flips to "doors within weeks".
- `event-no-show-management`: after registrations exist.
- `event-press-relations`, `event-booth-experience`, `event-b2b-matchmaking`: after fill-the-room is running and an expo or press surface actually exists. The `conference` gate is open.
- `event-sponsor-agreement` and `event-sponsor-fulfillment`: after a sponsor is signed.
- `event-feedback` and `event-debrief`: after the doors close.
- `event-speaker-experience`: after Q5 and the grid check confirm accepted speakers.

Deleted outright:
- `event-format-selection`, `event-date-selection` and `event-venue-sourcing`: the format, the date and the venue are fixed and signed.
- `event-schedule-design`: the grid is published.
- The existence-check class.

## Routines, dry-run only. Nothing is created until you approve.

Work-back and go/no-go both claim rung 1. The fixed doors date puts the work-back checkpoint first. The signed venue puts go/no-go first. I pick work-back, because go/no-go needs the contract's fee curve, which I haven't read.

```
Routine: work-back checkpoint
Trigger: each checkpoint date set by event-planning-timeline
Runs: samber/dev-event-organizer-skills@event-planning-timeline
Output channel: dated section in event-context.md + message in the organizers' channel
Cost: one replanning session per firing
First fire: date set in the timeline session
Stops: on the doors-open date

Routine: go/no-go review
Trigger: one step ahead of each venue cancellation-fee rung
Runs: samber/dev-event-organizer-skills@event-risk-management
Output channel: decision note in event-context.md + message to the decision-makers
Cost: one review per rung, with counsel or broker input if the decision is contractual
First fire: before the first rung (needs the contract's dates)
Stops: when the last fee rung has passed or on the doors-open date

Routine: kickoff re-invocation
Trigger: same dates as the work-back checkpoints
Runs: samber/dev-event-organizer-skills@dev-event-kickoff
Output channel: 5-line state summary appended to event-context.md
Cost: near zero
First fire: next checkpoint
Stops: on the doors-open date
```

Deleted for now: the ticket-pace check, because I have detected no ticketing source (see the extra checks). The trend read is held until Q3 settles. The sponsor sweep is held for Q4, Q6 and Q7.

## Gap

- **Registration and ticketing system operation** (platform, checkout, refund processing, tax) has no skill. `event-ticket-pricing` only writes the prices and policy.
- Working out why the team went quiet is not a skill either. Q5 covers it.
- No sibling-repo handoff applies.

## Draft `event-context.md` (not written)

```markdown
# Event context

_Last updated: 2026-10-12_

## Identity
- Event: Kelpway Conf 2027, developer conference.
- Edition: not yet answered (Q3).
- Funding model: not yet answered (Q4).

## Format (the gate source)
- Shape: multi-day conference, two days, three tracks (source: schedule-grid.pdf).
- Delivery mode: in-person.
- Workshop hours and hackathon: unknown, check the grid.
- Properties: not yet answered.

## Dates
- Doors open: about 2027-08, fixed, announced. Exact date not yet given.
- CFP, on-sale, sponsor windows: not yet answered.
- Venue cancellation-fee rungs and go/no-go dates: in venue-contract-signed.pdf, not yet extracted.

## Money
- Budget: budget-2027.xlsx, committed 2026-09, break-even 410 tickets.
- Ticket ladder, sponsor rate card, sponsors signed: none found in the repo.

## Programme
- Grid published on the site around 2026-09-28. Whether the talks are confirmed: unknown.

## State
- In flight: unknown. Commits stopped about 2026-09-23.
- Decided: format (2 days, 3 tracks, in-person), venue signed, grid published.
- Open: why work stopped, the Q5 goal, whether the repo matches the published state.
- Constraints: landing date = doors date; Q7 not yet answered.

## Team
- Not yet answered.

## Session log
- 2026-10-12 - "get going again" → samber/dev-event-organizer-skills@event-planning-timeline (provisional) → artifact drafted from user-reported inventory; 5 questions pending.
```

## Open pass-bar items

- `event-context.md` is not written, because the Kelpway repo isn't here.
- The interview is unfinished: Q3, Q4, Q5, Q6 (exact date) and Q7 remain.
- Routines are awaiting your approval.
- The skill requires memory to come from the artifact, written only after the interview completes. I wrote none.
- When memory is first written, it will exclude personal data, accommodation requests, conduct reports and negotiated sponsor or venue rates.