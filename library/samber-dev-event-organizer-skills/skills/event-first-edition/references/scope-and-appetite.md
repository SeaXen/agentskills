# Scope, appetite, and the validation ladder

A first edition is structurally a product launch: one bet, no track record, a feedback loop that only closes at doors-open. The scope and validation mechanics below reflect this reality.

## MVP types mapped to first-edition shapes

| MVP type                        | First-edition transposition                                                                        | When it fits                                                                                            |
| ------------------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Concierge (manual service)      | Organizer-run by hand: personal invites, spreadsheet registration, no ticketing platform           | Testing whether people show up before building any infrastructure                                       |
| Wizard of Oz (manual backend)   | Advertise a feature not yet built (e.g. attendee matchmaking) and deliver it by hand for edition 1 | One differentiating promise, no budget to build it yet                                                  |
| Smoke test (signup, no product) | Waitlist/interest page before venue or date is locked                                              | Belongs to `samber/dev-event-organizer-skills@event-market-fit` - demand validation, not edition sizing |
| Single feature                  | One core format only: talks, no workshops, no expo                                                 | The default single-focus tier                                                                           |
| Piecemeal (existing tools)      | Borrow an existing meetup's list, a free venue, an existing community's chat                       | The borrowed-edition tier                                                                               |

What NOT to transpose: Lean Startup's growth-engine machinery (viral coefficient, CAC/LTV, cohort retention) measures sustained usage over time, which one edition cannot generate. That vocabulary belongs to `samber/dev-event-organizer-skills@event-growth-strategy`.

## The validation ladder as a spending gate

Evidence strength, weakest to strongest:

1. Opinion.
2. Stated interest.
3. Deposit or claimed ticket.
4. Actually shows up.

Require level 3 (real registrations) before committing spend beyond the Good budget tier. Committing Best-tier budget on levels 1-2 is premature scaling with a venue contract attached.

## Appetite, rabbit holes, no-gos

Set the appetite - organizer hours and money this launch is worth - before shaping the program. The appetite bounds the program, never the reverse. Then write down, explicitly:

- **Rabbit holes** likely to swallow a first-edition team: a custom mobile app, elaborate stage production, simultaneous livestream, a multi-city launch.
- **No-gos** for edition 1, named so nobody re-litigates them mid-planning.

Worked example (a 3-person team, one day/week each, launching a one-day community conference):

> Appetite: ~10 organizer-hours/week for 9 months, break-even budget at the Good tier.
> No-gos for edition 1: no international speakers, no second track, no livestream, no paid keynote, no expo hall.
> Rabbit hole watch: "let's just build a small talk-voting app" - use the ticketing platform's built-ins or a form.

"Underdo the competition": a first edition competing on breadth against a tenth-edition conference loses; competing on being sharply focused on one underserved audience doesn't. Half an event done well beats a thin version of everything a mature edition has.

Opinionated defaults, decide-don't-hedge: every axis left open (city, date, price, format) is a decision attendees and sponsors need someone to make with confidence. Pick the best default per question, ship it, revisit only on evidence.

## Good / Better / Best budget tiers (sourced: DevOpsDays organizing guide)

Plan three versions of the same event before selling a single ticket:

- **Good** - the bare-minimum viable version: no catered food, pared-down badges, no evening event.
- **Better** - adds the expected niceties.
- **Best** - real headroom: an extra sponsored evening activity, better catering.

Write downgrade dates into the timeline: Best → Better → Good, triggered by sponsorship revenue actually received by each date. DevOpsDays targets 80%+ of budget from sponsorship, so this decouples "will we run at all" from "did tickets sell fast" - a soft ticket signal downgrades the tier instead of forcing cancellation.

The tier mechanism is sourced; every specific downgrade date and revenue threshold is self-set per event. The full P&L behind the tiers: `samber/dev-event-organizer-skills@event-budget`.
