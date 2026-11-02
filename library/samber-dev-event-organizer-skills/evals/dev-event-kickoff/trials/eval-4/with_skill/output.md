# FjordCon 4: what to attack first

I read `dev-event-kickoff/SKILL.md` and its four references, then applied them to your message. I didn't ask the interview questions, because you had already answered them. I didn't write `event-context.md` or any memory, because this working directory is the example-repo repo, not your event's. A draft of `event-context.md` is at the bottom for you to save.

## 1. Gates read from your answers

| Q | Your answer | Gate result |
|---|---|---|
| 1 | Edition 4, being planned | Block (e). Opens block M and whichever of A–K edition 4 reopens. |
| 2 | Two days, two tracks, in-person, date announced | Format fully fixed (c). `conference` and `in-room` are open. `hackathon`, `workshop`, `virtual` and `hybrid` are closed. |
| 3 | Edition 4 | `recurring` is open. |
| 4 | Foundation | `company` is closed, so `corporate-event-strategy` and `business-event-formats` are unreachable. |
| 5 | "What order do we attack this in?" | Session goal. |
| 6 | Doors on a fixed date about six months out, and the sponsor budget window closes in six weeks | (a) and (c). |
| 7 | Two funded full-time staff | (d), standing with paid staff. |

⚠️ One thing I couldn't confirm: I'm assuming FjordCon is your only event property. If you run or are weighing a second one, `event-portfolio-strategy` opens and moves up. Tell me and I'll re-rank.

⚠️ Your "end of January, six weeks from now" doesn't match today's date in my environment, 2026-10-12. I anchored on "six weeks" rather than a calendar date. Send me the exact window-close date and the doors date, and I'll write them into the plan and the artifact.

## 2. Route

**`samber/dev-event-organizer-skills@event-sponsor-value-proposition`** is the immediate task. Run it first.

- You haven't started this cycle's sponsor motion, so you are at the first stage of the sponsor chain.
- Sponsorship covered 60% of costs last year, and the window won't reopen this cycle.
- If last year's rate card and prospectus still stand, run this as a short refresh. Then jump to `event-sponsor-pricing` for the delta only.

## 3. Short-list, by value per unit of effort

**How your answers moved the default order**
- Q6c (a closing sponsor window) promotes the sponsorship sale to rung 1, whatever its default efficiency rank.
- Q7d (paid staff) makes the sale affordable and lifts place-and-duty-of-care.
- Q6a (a fixed doors date) promotes fill-the-room and programme intake, and pushes after-and-between to "not now".
- Detection also moves things:
  - Your carried-over budget with a revenue target makes the money model near-free.
  - Fixed format and date delete `event-format-selection` and `event-date-selection`.
- I deleted the existence check and the hackathon, virtual, hybrid and company rows rather than demoting them.

| # | Skill | Bottleneck it attacks | Session cost |
|---|---|---|---|
| 1 | `event-sponsor-value-proposition` | Why each sponsor segment buys, in terms that fit a January budget line. | One working session with last year's sponsor results and feedback. Nothing is published or signed. |
| 2 | `event-sponsor-pricing` | The rate card against the revenue target already on file. | One session. Reads the existing budget instead of remodelling it. Published prices bind. |
| 3 | `event-sponsor-prospectus` | The document sponsors read. | A design and copy pass. Needs audience facts from editions 1–3. |
| 4 | `event-sponsor-outreach` | Target list through to a signed yes, plus renewals, before the window shuts. | The highest cost. It runs on sponsors' calendars and needs a named owner for every account. |
| 5 | `event-planning-timeline` | The six-month work-back plan, with the sponsor window and CFP dates on it. | One sitting. The date is fixed, so don't polish it. |
| 6 | `event-cfp-design` | The CFP text, which doesn't exist yet. The call window is incompressible, and the programme is what sponsors buy access to. | One drafting session, then a weeks-long open window. |
| 7 | `event-marketing-plan` | Attendee marketing, which hasn't begun. Registrations are the audience number the next sponsor conversation needs. | A planning session, then a campaign through to doors. |

`event-budget` has no separate session. The budget is carried over, so read its revenue target inside the pricing session. Book a refresh only if last year's cost lines have drifted.

## 4. Chain (dependency order)

1. `event-budget` figure, read only → gives the sponsorship target (60% of costs is last year's share).
2. `event-sponsor-value-proposition` → gives the claims each segment will pay for.
3. `event-sponsor-pricing` → gives tiers and discount policy that hit the target.
4. `event-sponsor-prospectus` → gives the published packages.
5. `event-sponsor-outreach` → gives conversations and signed yeses.
6. `event-sponsor-agreement` → gives the term sheet. Counsel needs lead time, so brief them while the prospectus is being written.

Run the talks lane in parallel on the second staffer: `event-cfp-design` → `event-talk-selection` → `event-speaker-experience` → `event-schedule-design`.

**Week-by-week, my judgement rather than the skill's:** build links 2–4 in roughly the first two weeks. Open outreach by week two or three, starting with last year's sponsors. Renewals need no new pitch and are your fastest revenue. That leaves about three weeks of decision time before January closes.

**Staffing:** one staffer owns the sponsor chain full-time. The other does the timeline on day one, then the CFP, then the marketing plan. You approve the value proposition and pricing, and you brief counsel.

## 5. Not now (each with its unblocking condition)

- `event-talk-selection`: after the CFP closes with submissions in.
- `event-speaker-experience`, `event-schedule-design`: after `event-talk-selection` returns an accepted list. `event-speaker-sourcing` and `event-speaker-cold-outreach` come in only if you want an invited lane.
- `event-landing-page`: after `event-cfp-design` and `event-marketing-plan` return their dates.
- `event-ticket-pricing`: after the timeline sets an on-sale date. The ticket ladder's status is unknown to me.
- `event-attendee-email-sequences`, `event-no-show-management`: after the on-sale date and the first registrations.
- `event-press-relations`: after the programme is announced.
- `event-sponsor-agreement`: when the first yes lands. Prep counsel now.
- `event-sponsor-fulfillment`: after the first signature.
- `event-booth-experience`, `event-b2b-matchmaking`: after signed tiers define what sponsors bought.
- `event-run-of-show`, `event-production`, `event-comms-channels`, `event-attendee-experience`, `event-hospitality`: after the venue and the grid are fixed.
- `event-feedback`, `event-debrief`, `event-continuous-improvement`, `event-community-building`, `event-growth-strategy`: after doors close. Any past debrief logs can feed the value proposition now.

**One detection fact needed:** is the venue contract signed?
- If yes, `event-venue-sourcing` is deleted and `event-risk-management` moves up. It tracks the cancellation-fee rungs, and a go/no-go review gets installed.
- If no, `event-venue-sourcing` jumps ahead of the CFP.

`event-code-of-conduct`, `event-accessibility-inclusion` and `event-volunteers` are carry-over reviews, not urgent for the next six weeks.

## 6. Gap

- **Registration and ticketing system operation** (platform, checkout, refunds, tax on revenue) has no skill in the collection. `event-ticket-pricing` sets prices and the refund policy. `event-landing-page` wires the CTA to whatever system you run.
- Nothing else today's task needs is uncovered, and no sibling-repo hand-off applies.

## 7. Routines (dry-run only, nothing created)

You have to approve before I create any. They run as cron-style tasks inside this harness, and the fallback is one recurring calendar reminder. Q6c installs the sponsor sweep first. Q6a installs the work-back checkpoint first.

```
Routine: sponsor pipeline and renewal sweep
Trigger: weekly, then twice weekly in the final fortnight, until the budget window closes
Runs: samber/dev-event-organizer-skills@event-sponsor-outreach
Output channel: a dated section in event-context.md, plus a message in the
                organizers' internal channel
Cost: one named person chases each flagged account per firing
Stops: the sponsor budget window close date
```

The sweep names accounts and negotiated terms, so its channel must stay inside the team.

```
Routine: work-back checkpoint
Trigger: each checkpoint date on the new timeline: CFP close, on-sale, sponsor close, doors minus N
Runs: samber/dev-event-organizer-skills@event-planning-timeline
Output channel: dated section in event-context.md; scope-cut proposals go to the ED
Cost: one team huddle per checkpoint
First fire: after the timeline exists
Stops: doors-open date
```

```
Routine: kickoff re-invocation
Trigger: monthly, plus after each major decision
Runs: this skill
Output channel: patches to event-context.md and a refreshed 5-line state summary
Cost: near zero
Stops: doors-open date
```

**Queued, not installed:**
- The ticket-pace check waits for an on-sale date and a ticketing source.
- The go/no-go review waits on the venue contract answer.
- The post-edition trend read can't fire before the edition-4 debrief.

Retire any edition-3 routines before adding these.

## 8. `event-context.md` draft (save at your project root)

```markdown
# Event context
_Last updated: 2026-10-12_

## Identity
- Event: FjordCon. Edition 4.
- Funding model: foundation (Fjordwall Foundation). Sponsors covered 60% of costs last year.

## Format (the gate source)
- Shape: multi-day conference, 2 days, 2 tracks.
- Delivery mode: in-person. No workshop hours recorded.
- Properties: one (unconfirmed).

## Dates
- Doors open: [date], announced, about 6 months out.
- Sponsor budget window closes: [date], about 6 weeks out.
- CFP open and close: not set. On-sale: not set.
- Venue cancellation rungs: unknown, venue contract status unconfirmed.

## Money
- Budget carried from last cycle, revenue target on file: [location].
- Sponsor rate card: [status]. Sponsors signed this cycle: 0.

## Programme
- CFP text not written. No submissions.

## State
- In flight: nothing started.
- Decided: format, in-person, announced date.
- Open: venue contract status, rate card reuse, ticket ladder.
- Constraints: lands before sponsor window closes; standing, 2 funded FTE.

## Team
- Executive director: decision rights on sponsor pricing and value proposition.
- 2 event staff: sponsor chain and programme/marketing.

## Session log
- 2026-10-12 - "what order do we attack this" → event-sponsor-value-proposition
  → artifact created.
```

Keep two things out of memory and out of this file: negotiated sponsor rates and any contract term still under negotiation.