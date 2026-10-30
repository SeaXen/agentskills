# Risk taxonomy and scoring

The taxonomy, the matrix, the escalation bands, and the register fields.

## The taxonomy

Work through every row. Each is drawn from a documented event failure, not invented as a category. Delete a row only with a stated reason.

| #   | Risk category                                     | What it looks like                                                                    | Owner usually sits with    |
| --- | ------------------------------------------------- | ------------------------------------------------------------------------------------- | -------------------------- |
| 1   | Demand shortfall                                  | Ticket sales tracking below break-even inside the last affordable cancellation window | Marketing / ticketing lead |
| 2   | Sponsor withdrawal                                | A concentrated sponsor pulls out, or a signed sponsor never pays                      | Sponsorship lead           |
| 3   | Venue loss or forced change                       | Venue cancels, closes, is damaged, or unilaterally changes terms                      | Venue / logistics lead     |
| 4   | Marquee speaker loss                              | A keynote the program was built around withdraws, falls ill, or cannot travel         | Program lead               |
| 5   | Adverse weather, pre-event                        | Conditions make travel or the venue unusable before doors open                        | Venue / logistics lead     |
| 6   | Adverse weather, in-progress                      | A live event is interrupted or shut mid-run                                           | Day-of operations lead     |
| 7   | Communicable disease or public-health restriction | An outbreak, or a governmental order, prevents the event                              | Whoever holds the go/no-go |
| 8   | Organizer financial capability                    | The team cannot legally invoice, collect, or hold money in time                       | Finance / fiscal host      |
| 9   | Safety, security, or medical incident             | Fire, evacuation, power failure, injury, theft on site                                | Day-of operations lead     |
| 10  | Code-of-conduct or PR incident                    | Harassment, a speaker controversy, a public backlash                                  | CoC response owner         |
| 11  | Technical or production failure                   | AV, streaming, recording, or venue infrastructure fails                               | Production lead            |
| 12  | Registration-platform breach or data loss         | Attendee data exposed, ransomware, platform outage at a critical moment               | Whoever owns the platform  |
| 13  | Key-organizer loss                                | The one person holding a critical function becomes unavailable                        | Whoever owns the team      |
| 14  | Structural or commercial defection                | Exhibitors or sponsors abandon the format itself for their own channels               | Whoever owns the strategy  |
| 15  | Organizer discretion                              | The organizing group itself decides not to run this edition, with no external trigger | Whoever holds the go/no-go |

Rows 8, 14 and 15 are the ones organizers reliably forget, and each has at least one documented cancellation behind it. Row 8 in particular is higher-likelihood for a first edition standing up payment processing than for an established fiscal host.

Three self-set sub-risks worth naming explicitly under rows 11 and 13 at a tech-heavy, many-teams-building event, illustrative rather than drawn from a documented cancellation:

- **Shared venue network as a single point of failure (row 11).** Many teams calling the same third-party API from one venue IP address can get that address rate-limited or blocked by the provider, stopping every team using it at once, not just the one that triggered it.
- **A vendor account or tool held by one person (row 13).** A block on the whole event the moment that person is unreachable - set up and share access to any shared account before the event, not when it is first needed.
- **Physical access to a sensitive room (row 9).** A jury deliberation room or a similar closed-door space needs its own named lock-and-network-isolation check, distinct from the general venue-security row.

## Scoring: 5x5, likelihood x impact

Both axes run 1-5. Score = likelihood x impact, banded 1-25.

**Likelihood**: 1 Remote, 2 Unlikely, 3 Possible, 4 Likely, 5 Almost certain.

**Impact**, re-anchored for events. The source anchors were legal-domain percentages of deal value; these event anchors are this skill's adaptation, not an industry standard:

| Score | Label      | Anchor                                                                                                                |
| ----- | ---------- | --------------------------------------------------------------------------------------------------------------------- |
| 1     | Negligible | Absorbed without changing anything; nobody outside the team notices                                                   |
| 2     | Low        | Costs money the reserve covers, or a visible but recoverable quality drop                                             |
| 3     | Moderate   | A material share of non-recoverable committed spend is lost, or a named commitment to attendees or sponsors is broken |
| 4     | High       | The edition runs materially degraded, or survives only by consuming the reserve entirely                              |
| 5     | Critical   | The edition cannot run, or the organizing entity cannot continue                                                      |

### Three adaptations that make this event-specific

1. **Impact is measured against irreversible sunk cost and a date that cannot move.** A software release slips; an event does not. Schedule risk therefore collapses into a binary go/no-go rather than a spectrum of lateness, and impact is scored in unrecoverable deposits, refund liability and reputational loss - not ongoing operational disruption.
2. **Likelihood is time-phased.** Both the probability and the consequence change as the date approaches: a speaker dropout at T-2 weeks is a different risk from the same dropout at T-6 months. Re-score at every decision date rather than scoring once at register creation.
3. **Treatment maps onto the liability curve.**
   - Prevention reduces likelihood.
   - Reduction reduces impact.
   - Contingency is the pre-written fallback.
   - Transfer moves the loss to an insurer or a counterparty.

   Which of these is even available changes as contractual exposure escalates - transfer in particular has binding lead times that close well before the event.

### Amplifiers

Each of these raises a row's scored impact, or triggers a mandatory named mitigation; none is a note to record and move past:

- Outdoor venue or outdoor elements.
- Alcohol service.
- Complex builds or rigging.
- Presence of minors.
- Pyrotechnics.
- Hands-on hardware.
- Overnight or multi-day duration.
- A single-source dependency of any kind (one venue, one sponsor, one keynote, one organizer).

## Escalation bands and what each authorizes

| Band   | Score | What happens                                                                                                                                                                            |
| ------ | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Green  | 1-4   | Accept and document. One named person monitors it at routine intervals. No escalation.                                                                                                  |
| Yellow | 5-9   | Mitigate with specific controls, assign a named owner, brief the team, and **pre-define the trigger event that would move it to the next band**.                                        |
| Orange | 10-15 | Escalate to whoever holds the go/no-go. Build a specific mitigation plan, tighten the review cadence, and **write the contingency entry: if this fires, here is what we do**.           |
| Red    | 16-25 | Immediate escalation to the decision-holder or governing body. Activate the response team, notify the venue and insurer where relevant, review at the highest frequency until resolved. |

The yellow band's pre-defined trigger and the orange band's written contingency are the two mechanics worth keeping above all others: they are what convert a score into something that acts on its own when the person watching is busy.

## Register fields

Minimum viable row: description, category, likelihood, impact, score, band, owner, treatment, status (open / mitigated / accepted / closed), review date.

Add for anything orange or above: date identified, contingency entry, residual score after treatment, and the named trigger that would re-open or re-escalate it.

A spreadsheet is a perfectly good register. Project-management tools sell event risk-register templates (ClickUp and Smartsheet both ship one; the WHO's mass-gatherings all-hazards assessment tool is public-health-focused but adapts to conferences) - these are examples of the category, not requirements. One genuinely useful pattern to borrow from them: label the outcome in plain language ("OK to proceed" / "place on hold") rather than leaving a bare numeric score, because for a go/no-go-facing register the label is the decision, not an input to one.

## Closing discipline

Not every named risk needs a mitigation plan. Focus the plans on risks that are both material and controllable by this team - a prioritized register with a few real mitigations beats an exhaustive one where every row says "monitor".
