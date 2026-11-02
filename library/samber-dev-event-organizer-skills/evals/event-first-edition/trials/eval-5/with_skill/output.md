# InfraDays Krakow: edition 1 launch brief (7 months)

I read `event-first-edition/SKILL.md` and its three references. The skill wants you interviewed one question at a time. You asked for the full deliverable, so this is a draft brief. Anything I assumed is marked **[ASSUMED]**, and anything the skill can't ground is marked **[NOT DECIDED]**.

## Verdict

1. **Drop the 8-month plan.** The skill lists "blending the two timelines" as a named failure mode.
   - ~12 months is a conference figure, from the DevOpsDays guide. It is driven by year-ahead venue booking and a ~4-month CFP-to-program pipeline.
   - 4 to 9 months is a hackathon figure, from the MLH guide. It carries neither of those items.
   - Averaging them gives a number that belongs to neither format.
2. **Your event is conference-scale**, so the planning basis is the 12-month timeline. You have 7 months, which is 5 months short. "At 7 we're basically fine" is wrong as stated.
3. **It is still feasible.** The deadline is hard, so the skill's rule applies: the date never moves, and scope moves to fit it. Your free 280-seat auditorium and the city's tech week are two of the skill's four compression levers.
4. **Your biggest risk isn't the 5-month gap.** It is the team gate and neutrality. A TerraNimbus-sponsored person, in a TerraNimbus venue, with TerraNimbus-sponsored time, risks looking like a company event instead of the independent one you intend (details in § 3).

## 1. Appetite and no-gos

**[NOT DECIDED]** Appetite (organizer hours/week, budget, reversibility) needs your numbers. Interview Q5 is unanswered. The skill also suggests asking an organizer who has run a comparable, larger event for their actual number. Do that this week.

Proposed no-gos for edition 1, for you to confirm or cut:
- No second track and no second day.
- No livestream.
- No custom conference app. Use the ticketing platform's built-ins.
- No international speakers.
- No paid keynote.
- No expo hall.
- No multi-city launch. The skill rules this out for a first edition.

"Annual fixture" is a mandate for edition 2 onward. Keep it from inflating edition 1 scope.

## 2. Scope tier

Pole assumed: **community-run**, because you say it is independent. TerraNimbus's support is in-kind (time and venue).

| Candidate | Fit | Verdict |
|---|---|---|
| **Single-focus standalone**: one day, single track, own brand and registration | Matches your plan. | **Recommended.** |
| **Borrowed edition**: a special edition of your meetup in the auditorium during tech week | Needs almost no infrastructure. | **Fallback rung** (see the T-5 go/no-go in § 4). |
| **Full-footprint** (multi-track, expo, evening event) | Nothing in your inputs supports it. | Rejected. |

Validation gap:
- A waitlist is "stated interest" on the skill's ladder (level 2).
- Spending past the Good budget tier needs real registrations (level 3).
- The 400 meetup members are your baseline. Your 250 target is ~62% of them, which is very high. Sizing belongs to `event-market-fit`. Check that the waitlist is for the conference, not the meetup.
- Open registration early and use early-bird to convert the waitlist into claimed tickets.

## 3. Team and neutrality

**Team gate:** at least 3 organizers from at least 3 different organizations before venue or date is locked.

**[NOT DECIDED]** Interview Q7: who is on the team today? If every organizer works at TerraNimbus, you fail the gate. The skill treats it as both a neutrality check and an early demand check.
- Recruit 2 outside co-organizers in week 1-2, from other companies in your meetup.
- The gate relaxes only for company-run events. Yours is not, so don't waive it.

Neutrality rules for a free corporate venue:
- Use a neutral shared email alias for all public contact, never a TerraNimbus address.
- Use a shared credential vault.
- Publish the code of conduct before the first public listing. It is the earliest hard gate, ahead of venue and date.
- Set TerraNimbus's visible role (venue sponsor, plus any speaking or branding rights) in writing, before announcement.

Venue risk and the annual-fixture goal:
- "Offered" is not a contract. Get written confirmation of the date, capacity, AV, access, catering rules and cancellation terms.
- Ask for multi-year or first-refusal terms. The annual-fixture goal depends on a corporate venue still being free in year 2.
- Capacity is 280 for a 250 target. That headroom is thin, so cap registration.

**Team structure:** start with the 3-person cross-org core. Add roles as work appears. The 9-role team is for conference scale at the "confirm organizers" milestone, but compressed timelines make role-splitting urgent by month 2. Assign owners to talks, sponsors, venue, registration and volunteers early.

**Elephant:** bandwidth. Ask each organizer to state weekly hours out loud. TerraNimbus "sponsoring" your time should mean protected hours in writing, not goodwill.

## 4. Reverse timeline (T-7 compression)

Today is 2026-10-14. **[ASSUMED]** doors open ~2027-05-14. Replace this with the real tech-week date; dates below slide with it.

Compression levers applied, in the skill's terms:
- **Borrowed venue (promote).** Collapses the T-12 search and T-9.5 lock into a confirmation task.
- **Piggybacked scheduling (condition met if confirmed).** Interview Q8 is unanswered. The condition is that an anchor event exists in the city and season, and the tech week appears to satisfy it. Confirm that out-of-town attendees will actually travel for it. The cost is calendar competition (other events, hotels, speakers).
- **Invited-speaker program vs full CFP.** The skill ranks the invited program as the faster option. It also says a compounding mandate (your annual-fixture goal) favors the slower full CFP, so the two pull against each other. My judgment, not sourced: invite roughly half the slots, then run a short 4-5 week CFP for the rest. That keeps the community-openness signal and saves time.
- **Cut a scope rung** is the standing circuit-breaker.

| Offset | ~Date | Milestone | Gate or breaker |
|---|---|---|---|
| T-7 (wk 0-2) | Oct 2026 | Appetite, no-gos, tech-week date confirmed, recruit co-organizers, CoC, neutral alias, vault, join a peer organizer network, written venue terms, budget draft | **Admin + team + venue gates: no public announcement until all pass** |
| T-6.5 | early Nov | Public listing, sponsor prospectus out, registration and early-bird open (fast, since the waitlist exists) | |
| T-6 | mid Nov | Invited speakers contacted; CFP opens (4-5 weeks) | |
| T-5 | mid Dec | CFP closes (before the holidays); invited line-up confirmed | **Go/no-go 1** |
| T-4.5 | Dec 18 at the latest | Organizers vote; speakers notified | Keep this lead time, since speakers need employer approval and travel |
| T-4 | mid Jan | Sponsor revenue check | **Budget-tier downgrade 1:** Best → Better |
| T-3.5 | Feb 1 | Program public; early-bird closes | **Go/no-go 2 / downgrade 2:** Better → Good |
| T-1 | mid Apr | Volunteer check-in; pre-mortem revisit | |

All dates and thresholds are **proposals**. The sourced part is the mechanism, and you set the numbers.

The two circuit breakers, with my proposed triggers:
- **T-5 go/no-go:**
  - Trigger: fewer than half of the program slots confirmed, or the team gate still unmet.
  - Action: cut a scope rung (shorter day, fewer talks). If that fails, drop to the borrowed edition and keep the date.
- **T-3.5 go/no-go:**
  - Trigger: claimed tickets below your threshold. **[NOT DECIDED]** — set the number yourself.
  - Action: downgrade the budget tier. Don't cancel and don't move the date.

The holiday collision (CFP close and vote in late Dec) is the main reason the sourced offsets can't be copied directly.

## 5. Pre-mortem

| Risk | Category | Urgency | Owner | Mitigation | Decision date |
|---|---|---|---|---|---|
| Employer withdraws or changes the auditorium terms | Tiger | Launch-blocking | Logistics owner | Written terms; backup venue shortlisted at reduced capacity | T-4 |
| Sponsors' annual budgets are already committed, or payment lands after deposits | Tiger | Launch-blocking | Sponsorship owner | Good tier funded by free venue plus floor commitments; invoice at signature | T-5 |
| Speaker or keynote cancels | Tiger | Launch-blocking | Speaker relations | Two pre-briefed local backups | T-1 |
| Tech-week crowding (speakers, hotels, attendee attention) | Tiger | Launch-blocking | Lead organizer | Pick the least-contested day; confirm anchor attendance | T-6 |
| TerraNimbus-only team looks like a company event | Tiger | Launch-blocking | Lead organizer | Team gate; written neutral-roles agreement | Week 2 |
| "We're unknown, nobody comes" | Paper tiger | Track | None | Waitlist plus meetup baseline; watch registration checkpoints | None |
| Weekly hours vs day jobs and employer support | Elephant | Launch-blocking | Lead organizer | Hours stated out loud; cut a rung if two organizers miss two check-ins running | T-6 |

## Open items before this is final

1. Real tech-week date, and whether attendees travel for it (Q8).
2. Current team: names, and employers (Q7).
3. Hours/week and budget ceiling (Q5).
4. Whether the 400 waitlist is for the conference or the meetup.
5. The legal entity and bank account that sign contracts and hold the money. The skill doesn't cover this, but it affects the neutrality point above.

Doors-open ends this skill's scope. Hand off to `event-budget`, `event-venue-sourcing`, `event-planning-timeline`, `event-risk-management` and `event-debrief`.