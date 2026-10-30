# Calendar spines and phase targets

Two sourced checkpoint ladders, the worked calendars behind them, and the method for turning either into per-phase funnel targets.

Contents: Spine A (ticketed conference) · Spine B (free event) · Why they must never be blended · Net of comps · Worked calendars · Setting per-phase targets · Re-forecasting.

## Table of Contents

- [Spine A - ticketed conference: percent of expected ticket sales](#spine-a-ticketed-conference-percent-of-expected-ticket-sales)
- [Spine B - free event: percent of the attendance goal](#spine-b-free-event-percent-of-the-attendance-goal)
- [Why the two must never be blended](#why-the-two-must-never-be-blended)
- [Net of comps](#net-of-comps)
- [Worked calendars](#worked-calendars)
- [Setting per-phase targets](#setting-per-phase-targets)
- [Re-forecasting](#re-forecasting)

## Spine A - ticketed conference: percent of expected ticket sales

Source: DevOpsDays organizing guide (`devopsdays/devopsdays-web`, `content/page/organizing.md`).

Sales spike at named moments, not evenly over time. The published spike list:

1. Tickets first announced.
2. Early-bird pricing ends.
3. Speakers announced.
4. Full agenda announced, when separate from the speaker announcement.
5. Ticket codes go out to sponsors, speakers, organizers and volunteers.
6. After any reminder email.
7. The final two weeks - normal, not a red flag on its own.

The checkpoint ladder, all percentages of expected sales **net of comps**:

| Checkpoint                    | Expected                                                       | Reading if missed                                                                                                       |
| ----------------------------- | -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| First sales week              | Any real spike at all                                          | No spike is the earliest warning sign that no audience exists                                                           |
| Early-bird close              | ~15% of expected sales (worked example: 60 of an expected 400) | Materially lower means weak demand, visible before the bulk of marketing effort is committed                            |
| Speaker / agenda announcement | ~another 10%                                                   | The program is not pulling; check whether the announcement actually reached the list                                    |
| One month out                 | 40-50% of expected sales                                       | 25-30% is where a team that skipped or delayed its visibility push lands - an execution shortfall, not a demand verdict |
| Final two weeks               | A surge                                                        | Its absence, after healthy earlier checkpoints, points at the page or the price                                         |

The guide states these percentages shifted after the fragmentation of social-media audiences and may keep shifting. Treat the ladder as an order-of-magnitude checkpoint set, not a formula.

Earliest calendar anchor from the same guide's reverse timeline: **T-7 months, "ensure marketing is off and running"**, with the stated reason that "marketing is tricky, especially as a new event in a world where social media is quickly changing."

## Spine B - free event: percent of the attendance goal

Source: MLH hackathon organizer guide (`MLH/mlh-hackathon-organizer-guide`, `general-information/marketing-your-event/`).

The target deliberately exceeds 100% because signups are not attendance.

- MLH states an expected **50% drop-off rate for free hackathons**.
- A second file in the same repository states "most events have a 30-50% drop-off in attendance" and instructs organizers to "over-market and overbook."

Report the **30-50% range**, not a single figure.

Worked timeline for a 500-attendee goal (≈1,000 registrations needed to net 500):

| Timeline        | Registrations               |
| --------------- | --------------------------- |
| 3 months before | Registrations open          |
| 2 months before | 100                         |
| 1 month before  | 250                         |
| 2 weeks before  | 600 (100%+ of the 500 goal) |
| 1 week before   | 1,000 (200% of the goal)    |

The stated rule: **100% of the attendance goal signed up two weeks out, 200% one week out.** The doubling absorbs the drop-off. It is not a stretch target.

Hackathon-specific hard deadline: MLH requires partner-event registration to **close one week before the event** so MLH can prepare its pre-event email and run a bad-actor check. Flag it as hackathon-specific rather than generalizing it into a registration-close rule for conferences.

## Why the two must never be blended

The denominators differ, and so does the risk each spine manages.

|                             | Spine A                                                           | Spine B                                  |
| --------------------------- | ----------------------------------------------------------------- | ---------------------------------------- |
| Denominator                 | Expected paid ticket sales, net of comps                          | Attendance goal                          |
| Checkpoint anchors          | Marketing moments (announcements, cutoffs)                        | Fixed calendar offsets (2 weeks, 1 week) |
| Healthy end state           | ~100% of expected sales by doors                                  | ~200% of goal one week out               |
| Risk managed                | Under-selling                                                     | No-shows                                 |
| Revenue structure behind it | Sponsorship-funded (~80%+ of budget), tickets as a secondary line | Free entry, sponsorship-funded entirely  |

A 200%-style target applied to a paid conference asks the event to sell twice its own expectation. A 40-50% one-month-out target applied to a free hackathon is met trivially and hides a no-show catastrophe. There is no average of the two that is meaningful for any event.

**In-between events.** A nominal-fee event (a small charge used to spread risk and suppress no-shows) or a free event with a hard capacity cap sits between the poles. Pick the spine matching the failure that would actually hurt: unsold seats or empty seats.

Run it as the only target line, and read the other spine's checkpoint as a secondary sanity check that never enters a target or a go/no-go decision.

## Net of comps

Spine A's percentages are of tickets that had to be _sold_. Before setting any target, subtract every ticket that will be given away:

- Sponsor allocations.
- Speakers.
- Organizers.
- Volunteers.
- Scholarship or diversity tickets.
- Press or partner passes.

An event expecting 400 attendees with 80 comps is running a campaign against 320, not 400. Using the gross number silently inflates every checkpoint by a quarter and manufactures a miss that never happened.

## Worked calendars

**Ticketed conference, 320 expected sales net of comps, doors in October.**

| When       | Moment                                                                                    | Cumulative target        |
| ---------- | ----------------------------------------------------------------------------------------- | ------------------------ |
| T-7 months | Marketing off and running; comms hub live; list building starts                           | -                        |
| T-5 months | Announcement + tickets on sale                                                            | First-week spike present |
| T-4 months | Early-bird close (date fixed by `samber/dev-event-organizer-skills@event-ticket-pricing`) | ~48 sold (15%)           |
| T-3 months | CFP closes; speaker announcement                                                          | ~80 (adds ~10%)          |
| T-2 months | Full agenda published; partner and swap pushes land                                       | -                        |
| T-1 month  | Reminder send; sponsor/speaker codes out                                                  | ~130-160 (40-50%)        |
| T-2 weeks  | Final surge campaign                                                                      | Surge visible            |
| Doors      | -                                                                                         | ~320                     |

**Free hackathon, 500 attendance goal.** The MLH table above is already the calendar. Add the marketing moments that produce each step:

- Registration opens.
- Campus tabling weeks.
- Partner and ambassador cross-posts.
- The final week's reminder push.

Mark registration close at T-1 week.

## Setting per-phase targets

1. Take the spine's checkpoint percentages as the target line - do not invent new ones. Both ladders were published by organizations running these events at scale. A self-invented percentage carries none of that weight.
2. Convert each percentage into an absolute number against the net-of-comps target (Spine A) or the attendance goal (Spine B), so a checkpoint is a countable number and not a ratio to re-derive under pressure.
3. Attach each checkpoint to a **date**, taken from the fixed dates collected in the interview. A checkpoint without a date cannot be missed, which means it cannot be acted on.
4. Name, per checkpoint, the action a miss triggers - diagnose, add a channel, promote the budget posture, or trigger the event's own Good/Better/Best downgrade. Decide this before launch, while nobody is panicking.
5. Where a prior edition exists, overlay its own curve and treat the spine as the fallback. An event's own prior curve beats any published ladder, because it already encodes that event's audience, list and season.

## Re-forecasting

At each checkpoint, compute actual against the planned line, then diagnose before reacting:

- **Below the line, weak reach signals** (low page traffic, low send opens, no partner referrals) → execution shortfall. The sourced 25-30% band exists precisely for this case: add or re-weight channels.
- **Below the line, healthy reach but low conversion** → the price or the registration page, not the channel mix. Route out rather than buying more reach.
- **Below the line, healthy reach and healthy conversion** → genuine demand shortfall. This is the read that belongs to `samber/dev-event-organizer-skills@event-market-fit` and to the event's own Good/Better/Best downgrade decision, not to a bigger campaign.
- **Above the line early** → confirm it is not a comp-inflated or batch-release artifact before moving budget elsewhere.
