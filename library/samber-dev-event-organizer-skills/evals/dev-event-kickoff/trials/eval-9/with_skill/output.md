# GreenStack Live edition 2: routing result

**Route: `samber/dev-event-organizer-skills@virtual-event-production`.** All four items on your book's checklist assume a physical room. In this collection, `virtual-event-production` is the skill that replaces them for an event with no room.

This is a cold start, so there is no state summary. I found no `event-context.md` in the working directory, and this repo isn't your event's project. A draft is at the bottom.

## What I read from your message

| Fact | Gate effect |
|---|---|
| Fully remote, no physical component | `virtual` is open. `in-room` is closed, and so is `hybrid`. |
| Edition 2 | `recurring` is open. `first` is closed. |
| Doors in about 7 months (about May 2027; I need the exact date) | Landing date is a fixed doors date. |
| Track count, expo, press surface, funding model | Not stated. `conference`, `hackathon`, `workshop` and `company` stay suspended. I did not infer them from the name "Live". |

The delivery mode is fixed, so `virtual` opens regardless of the shape. Shape and track count are still unknown. If they aren't written down anywhere, `event-format-selection` runs before the virtual route goes deep.

## Your checklist against the collection

| Book item | Verdict |
|---|---|
| Shortlist venues | ❌ `event-venue-sourcing` is `in-room` only. Drop it. |
| Pick a caterer | ❌ `event-hospitality` is `in-room` only. Drop it. |
| Check-in desk and badge flow | ❌ `event-attendee-experience` is `in-room` only. The remote-attendee journey moves into `virtual-event-production`. |
| Hire an AV crew | ❌ `event-production` is `in-room` only. Its virtual replacement is a platform plus a moderator roster and remote-speaker pipeline, inside `virtual-event-production`. |
| Live captions? | Yes, it is a real question. `event-accessibility-inclusion` decides whether captions are required and to what standard. `virtual-event-production` then delivers them on the platform and never sets the bar itself. |

## Short-list (value per unit of effort, highest first)

1. **`virtual-event-production`** is the route. It fixes the bottleneck that the checklist has nothing to attach to. It costs one session, and nothing is booked or signed.
2. **`event-planning-timeline`** attacks the 7-month work-back plan from doors. It costs a session plus a calendar scan.
3. **`event-marketing-plan`** attacks last year's 1,200 registrations, which are your demand signal. It costs a campaign through to doors, plus the list consent you then owe.
4. **`event-no-show-management`** attacks the gap between registered and live attendance. That gap sizes the platform and the moderators. It costs a short modelling session.
5. **`event-budget`** attacks the cost lines. Venue and catering vanish, and platform, captions and moderation appear. It costs one modelling session.
6. **`event-accessibility-inclusion`** attacks the captions question. It costs a session, and the result is a public commitment you then owe.
7. **`event-vendor-sourcing`** attacks the captioning provider and any outsourced streaming. It costs quotes and a contract, and it only starts after the accessibility verdict.

Re-ranks:
- **Q1e, edition N:** moved the order only by deleting `event-first-edition`.
- **Q3c, recurring:** reopens `event-team-structure`, `event-community-building` and `event-growth-strategy`, but only after doors.
- **Q6a, fixed doors date:** promoted fill-the-room and the spine.
- **Accessibility:** it sits at rung 6 on ratio. The chain below puts it ahead of platform lock-in.

## Chain

1. `event-accessibility-inclusion` hands over the caption bar: yes or no, which sessions, which standard.
2. `virtual-event-production` takes that bar, picks the platform and sets the moderator roster. It hands back the platform's caption capability and its reversal deadline.
3. `event-vendor-sourcing` takes the caption and stream requirements and returns quotes.
4. `event-budget` takes the real cost lines from steps 2 and 3.

## Not now

- **`event-market-fit`** returns if the registration pace falls under last year's checkpoint.
- **`event-run-of-show`** and **`event-comms-channels`** wait until the platform is chosen.
- **`event-sponsor-*`** waits for Q4 and Q7, and for a sponsor budget window that closes.
- **`event-cfp-design`** and **`event-talk-selection`** wait for the programme status.
- **`event-feedback`**, **`event-debrief`** and **`event-continuous-improvement`** wait until doors close. The trend read needs two debriefs.
- **`event-community-building`** and **`event-growth-strategy`** wait until after edition 2.
- **`event-booth-experience`**, **`event-b2b-matchmaking`** and **`event-press-relations`** wait for the `conference` gate, which needs a stated expo, matchmaking or press surface.

## Gap

None for today's task. Ticketing platform operation is a collection gap, in case someone raises it.

## Routines (dry-run only, nothing installed)

1. **Work-back checkpoint** fires at each checkpoint date `event-planning-timeline` produces. Output goes to your team channel as a scope-cut decision. It stops at doors.
2. **Kickoff re-invocation** fires monthly. Output goes to a diff of `event-context.md`. It stops at doors.

I left the other candidates out. No ticketing source is detected, which deletes the pace check. There is no venue contract, so the go/no-go review has no cancellation curve. The trend read needs two debriefs.

## Questions that would sharpen this (tappable, one at a time)

1. **What is the shape and track count?** Options: single track, multi-track, or not fixed.
2. **Who funds it?** Options: volunteers, a company, a foundation, or mixed.
3. **What is your effort ceiling?** Options: a few hours a week, paid staff, or a funded budget.
4. **What is the exact doors date, and is it announced?**

## Draft `event-context.md` (not written: this repo isn't the event's project)

```markdown
# Event context
_Last updated: 2026-10-12_
## Identity
- Event: GreenStack Live. Edition 2 (edition 1 had 1,200 registered).
## Format (the gate source)
- Shape / track count: not fixed (to confirm)
- Delivery mode: fully virtual, no physical component
## Dates
- Doors open: about May 2027 (exact date to confirm)
## State
- Decided: no room; venue, catering, check-in desk and AV-crew checklist items dropped
- Open: live captions (event-accessibility-inclusion); platform and reversal deadline
- Constraints: landing date = doors; effort ceiling and funding unanswered
## Session log
- 2026-10-12 - "route me" with in-person checklist → virtual-event-production → recorded mode and dropped items
```

Memory exclusion, as the skill requires: nothing about attendees, accommodation requests, conduct reports or negotiated rates goes into memory.