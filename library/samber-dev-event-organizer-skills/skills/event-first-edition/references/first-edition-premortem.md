# First-edition pre-mortem

Run a pre-mortem once team and rough scope exist (not before), and revisit it at the one-month-out checkpoint both sourced timelines already carry. Use the Tigers / Paper Tigers / Elephants categorization and the urgency ladder below. No separate date is needed for the revisit.

## The three categories, in first-edition terms

- **Tigers - real risks, backed by evidence or clear logic:**
  - The venue contract falls through.
  - The anchor sponsor's payment lands after the deposits it was meant to cover.
  - A lead speaker cancels with no backup identified.
  - Nobody volunteers for day-of roles.
- **Paper tigers - surface-plausible worries that don't hold up.** "Nobody will come because we're a brand-new, unknown event" is the single most common one a first-time organizer fixates on. It is directly answered by the existing-community attendance baseline (sizing owned by `samber/dev-event-organizer-skills@event-market-fit`) - name it explicitly so the team stops treating it as a tiger and starts watching the real ones.
- **Elephants - assumptions nobody on the team is testing.** The classic first-edition elephant: whether the 3-person core actually has bandwidth alongside day jobs to hit the reverse-timeline dates - enough headcount on paper, untested in hours. Surface it by asking each organizer to commit a weekly hour count out loud.

## Urgency ladder, mapped to the budget tiers

- **Launch-blocking** - a tiger that, if it fires, forces a downgrade Best → Better → Good on the budget ladder. Downgrade, don't cancel: the tier mechanism exists to absorb exactly this.
- **Fast-follow** - solvable within ~30 days after the event; explicitly handed to `samber/dev-event-organizer-skills@event-debrief` and edition 2, never solved by delaying edition 1.
- **Track** - monitored, not acted on for edition 1, consistent with the scope discipline in the main skill.

## Action-plan structure

For every launch-blocking tiger: risk, mitigation, **owner, decision date**. Assign owners from the delegation roles already stood up (the venue/logistics owner takes the venue-contract tiger; the sponsorship owner takes the late-payment tiger) - don't invent a separate risk-owner role. The general risk register, insurance, and cancellation planning beyond edition 1: `samber/dev-event-organizer-skills@event-risk-management`.

## Worked example (one-day community conference, 3-person core)

| Risk                                            | Category    | Urgency                                                          | Owner             | Mitigation                                                                                             | Decision date |
| ----------------------------------------------- | ----------- | ---------------------------------------------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------ | ------------- |
| Venue cancels after deposit                     | Tiger       | Launch-blocking                                                  | Logistics owner   | Backup venue shortlisted at half capacity; contract reviewed for cancellation terms                    | T-4 months    |
| Anchor sponsor pays net-60, deposits due sooner | Tiger       | Launch-blocking                                                  | Sponsorship owner | Invoice at signature; Good-tier floor covers deposits without the sponsor                              | T-5 months    |
| Keynote speaker cancels                         | Tiger       | Fast-follow at meetup scale, launch-blocking at conference scale | Speaker relations | Two local backups pre-briefed                                                                          | T-1 month     |
| "We're unknown, nobody comes"                   | Paper tiger | Track                                                            | -                 | Baseline sizing from the existing meetup; watch registration checkpoints instead of worrying           | -             |
| Core team bandwidth vs day jobs                 | Elephant    | Launch-blocking                                                  | Lead organizer    | Weekly hour commitments stated out loud; cut a scope rung if two organizers miss two check-ins running | T-6 months    |

**Negative example - what a first-edition pre-mortem should not look like:** ten rows of paper tigers ("what if it rains", "what if the wifi is slow", "what if a competitor launches the same week"), no owners, no decision dates, and the bandwidth elephant absent because raising it feels like accusing teammates. A pre-mortem where every risk is external and none is about the team itself has skipped its most valuable category.
