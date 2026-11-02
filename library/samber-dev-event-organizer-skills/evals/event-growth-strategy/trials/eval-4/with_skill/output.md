# PixelForge Days: growth plan for the next edition

**Recommendation:** do neither as framed. Don't rent a bigger paid venue. Don't add event-wide registration with a hard cap yet.

Take one lever: **venue squeeze**, meaning more usable capacity from the venue you already know, with room-level crowd control. Pair it with a light, free registration that you use as a demand meter, not as a gate. That registration is a conditional fallback to a hard cap, described below.

I didn't run the interview one question at a time, because you asked for the full answer at once. Where I assumed an answer, I say so.

## 1. Demand evidence

| Signal | Status |
|---|---|
| ~2,500 attended | Your figure. One edition. |
| Popular rooms impossible to enter, hallways rammed | Your observation. This shows crowding, not headroom. |
| Sellout speed, waitlist size, sponsor inbound | **You have none of these.** A free, no-registration event produces no such signal. |

The skill's growth gate needs all three signals, repeated across editions. That gate is a research heuristic, not an industry standard. You can't pass it today, so "demand clearly keeps growing" is currently an impression.

The skill also requires a demand read from `event-market-fit` (attendee return, sponsor renewal, sellout trend). I didn't have one. Run it before you commit to anything beyond this edition.

## 2. Ceiling diagnostic

- **Saturation:** unknown. Check how many attendees were first-timers.
- **Channel decay:** nothing indicates it.
- **Quality collapse:** possibly already happening. Rooms nobody can enter and rammed hallways are the early form of it. This is the main argument against pure growth.

## 3. Reach vs. intimacy

I assumed **reach**. An open-source tooling event with 30 volunteers and 2,500 people is closer to FOSDEM than to a 150-person invite-only retreat. Please confirm.

If your answer is intimacy, the plan flips to the non-growth menu: cap, application and lottery.

## 4. Chosen lever and rejected rungs

**Chosen: venue squeeze, plus room-level control.**

- Get the venue's real occupancy limit per room and for the building.
- Re-assign sessions so the sessions you know are popular go into your biggest rooms.
- Open overflow spaces.
- Put a volunteer at each door with a "room full" sign. This is the FOSDEM devroom practice.
- Do not push past fire-code sign-off.

**Rejected rungs:**

| Rung | Why rejected |
|---|---|
| **Paid bigger venue (step-up)** | It loses on money and risk. Deposits run 25-50% at signing. Attrition and F&B penalties are owed even if you under-fill. Leads run 9-18 months for 300+ attendee events. Venues rarely renegotiate. A volunteer team with no ticket revenue would carry all of that, sized to an unproven number. You also have no sponsor bench in the facts given. Revisit only after two editions of registration data and a sponsor commitment that covers the exposure. |
| **Day addition** | It adds cost lines and a contract amendment, and doesn't fix room overflow. |
| **Several rungs at once, or a jump past ~2×** | This option is deleted from the menu. Brooklyn Beta went from ~300 to ~1,300 in one edition and the community said it didn't scale. |

**Track addition** is the natural free-event lever, and it is the next rung if squeeze isn't enough. The venue must have spare rooms. If it doesn't, you're back to the cap decision below.

## 5. Where registration fits

**Registration as a gate is not wrong. It is premature, and it may be forced.**

- **If the venue's occupancy limit is close to 2,500,** a cap is a safety requirement, not a strategy choice. Use **hold the cap**: free registration, a waitlist, and overbooking for no-shows. Be aware that first-come-first-served favors people with time and connections. If you care about who is in the room, escalate to application plus lottery (the XOXO approach).
- **If the venue has real headroom,** use registration as an instrument only. Keep entry open, ask people to register for a ticket, and track the numbers. That gives you the sellout, waitlist and no-show data the gate needs. Registration data then settles the "bigger venue" question next year, on evidence.

Do not use batch-released ticket drops to manufacture sellout optics. It corrupts the very signal you want to read.

## 6. Financial gate result

- **Squeeze and room control:** near-zero contract exposure. Only the layout renegotiation with your existing venue.
- **Paid venue:** fails the gate for now, as above.
- **Registration tooling:** low cost, mostly volunteer time.

**Cap on exposure for this edition:** no new deposit and no multi-edition commitment. This is self-set.

## 7. Pricing posture

Stay free. Make it a public commitment, funded by sponsorship, as PyCon did when it held prices flat while venues grew. This is only as durable as your sponsor base, so watch concentration (signal 3 below).

If you introduce an optional supporter tier, it must cross-subsidize other attendees. Price mechanics belong to `event-ticket-pricing`.

## 8. Paired mitigation

Squeeze and tracks dilute the hallway track and make popular rooms harder to enter. Mitigate with:

- recording or streaming popular sessions, so nobody has to be in the room;
- protected unstructured time;
- door volunteers at every room.

## 9. Watch plan

Any one signal firing means hold or shrink the next edition. Don't push through. Thresholds are self-set and must be declared before registration opens. Owners are placeholders for you to assign.

| # | Signal | Declared threshold (self-set, adjust) | Owner | Check date |
|---|---|---|---|---|
| 1 | Registration fills slower year over year at flat or higher capacity | Slower than the first edition's registration curve | TBD (lead organizer) | 2 weeks after registration opens, then monthly |
| 2 | No-show rate rises as you scale | More than 30% no-shows, or up more than 10 points vs. last edition | TBD (registration owner) | Day after the event |
| 3 | Single sponsor concentration | No sponsor above 30% of funding | TBD (sponsor lead) | At each sponsor signing |
| 4 | Organizers report the work is "actively unpleasant" | Any two of the 30 volunteers say so in a retro, or the lead says it | TBD (lead organizer) | Retro within 2 weeks after the event |

The first three are self-set numbers, not documented norms. Signal 4 is a documented reversal trigger (XOXO). With 30 volunteers and no paid staff, the human ceiling will hit before the financial one.

## 10. What to do next

1. Get the venue's occupancy limit per room and building. This decides whether the cap is forced.
2. Mine last edition's data for per-session headcounts and first-timer share.
3. Confirm reach vs. intimacy.
4. Run `event-market-fit` for a proper demand read.
5. Declare the four thresholds above before registration opens.

## Open questions I'd ask you

1. What is the venue's fire-code occupancy, and how many sessions were packed beyond their room capacity?
2. Are you aiming for reach or intimacy?
3. How many editions have run, and how many were growing like this one?
4. Do you have sponsors today, and what share of the budget do they fund?
5. Is organizing still pleasant for the volunteers?

The answers to 1 and 2 could change the pick from squeeze to a forced cap, or from reach to the allocation menu.