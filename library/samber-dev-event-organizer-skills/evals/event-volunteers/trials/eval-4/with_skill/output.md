**Next action:** Send an RFQ to staffing and AV vendors this week. Do not build a volunteer program for this event. Reasons are below.

## 1. Verdict: skill's scope ceiling applies

- The `event-volunteers` skill stops at professionally staffed events. Those are events with a payroll events team and a staffing budget.
- You have both: 3 FTE and a $40k line for on-site staffing.
- The registration/badge desk and AV are the exact posts the skill sends to contracted vendors.
- The skill says to procure the labour with `event-vendor-sourcing`.
- Rung assumed: professionally staffed. At 2,500 attendees over 2 days you would otherwise sit on the "built program" rung.

**Why volunteers fail here (bottom-up arithmetic, not an attendee ratio):**

- The posts need about 585 person-hours (table in section 2).
- At 3-hour shifts that is about 195 shift-slots.
- At 2 shifts per volunteer that is about 100 people. At 1 shift per volunteer it is about 195.
- 3 FTE cannot recruit, confirm, brief and direct 100+ unpaid people while also running the event.
- AV and badge systems handle equipment and attendee records. A fault there stops a session or exposes personal data.

## 2. Provisional post list

This is built before a run of show exists. Reconcile it with `event-run-of-show` when that document exists.

Assumptions (replace them with real values):

- Building opens 07:30. Sessions run 09:00 to 17:30 on both days.
- Day 1 is the registration peak.
- Load-in is the day before.

| Post | Simultaneous | Person-hours | Shift-slots (3h) |
|---|---|---|---|
| Registration stations | Day 1: 8 for 07:30-10:30, 4 until 14:00, 2 until 18:00. Day 2: 4 until 10:00, 2 until 17:00 | 70 | 23 |
| Registration lead and badge reprint/problem desk | 2, both days | 40 | 13 |
| Day-before badge setup and print test | 4 × 4h | 16 | 5 |
| Room monitors | 8 rooms plus 1 extra in the keynote room, 08:45-17:45 | 162 | 54 |
| AV room techs | 8, with 1h pre-session check, both days | 160 | 53 |
| AV lead/roving | 2, both days | 40 | 13 |
| AV load-in and strike | 6 × 6h | 36 | 12 |
| Floaters | 3, 10h, both days | 60 | 20 |
| Closing-session entrance | 2 × 1h on Day 2 | 2 | 1 |
| **Total** | | **~586** | **~195** |

Notes on the table:

- The closing-session entrance is its own post. Without it, latecomers land on whichever organizer is nearest the door.
- The extra monitor in the keynote room covers the opening keynote and the closing ceremony, so no organizer has to run them.
- The code-of-conduct response team needs named, reachable people every hour. Draw them from Northwind staff, not the vendor. Roster rules come from `event-code-of-conduct`.

## 3. Illustrative budget

These rates are my assumptions, not quotes. Replace them with real quotes.

| Line | Hours | Assumed billed rate | Cost |
|---|---|---|---|
| Registration, reprint and setup staff | 126 | $35/h | ~$4.4k |
| Room monitors | 162 | $35/h | ~$5.7k |
| Floaters | 60 | $35/h | ~$2.1k |
| AV techs, load-in and strike | 196 | $85/h | ~$16.7k |
| AV lead/roving | 40 | $110/h | ~$4.4k |
| **Subtotal** | | | **~$33.3k** |
| 10% contingency | | | ~$3.3k |
| **Total** | | | **~$36.6k, inside $40k but thin** |

Levers if quotes come in high:

1. Share AV techs between adjacent small rooms with roaming cover. This is the biggest saving.
2. Move room monitors to Northwind employees. This is my judgment, not the skill's. The post handles no cash, no personal data and no equipment, so it is the safest one to give to unpaid people. Keep a named backup per room and brief them like paid staff.
3. Cut the Day 2 registration stations.

Open question: does the Austin venue require in-house AV or labour? If yes, the AV line changes completely. Check the venue contract first.

## 4. What still applies from the skill

The volunteer mechanics still apply to paid staff. Put them in the vendor contract and the briefing.

### Roles and fit criteria

- **Registration agent**
  - Fit: calm, clear communication, accurate, comfortable with queues.
  - Handles attendee records, so it is a named post.
  - Gate: a 5-minute check on the badge system before the first transaction.
- **Registration lead / reprint desk**
  - Fit: fixes badge errors without escalating every one.
  - Named person, not open-claimed.
- **Room monitor**
  - Fit: confident in front of a room, punctual, calm under pressure, basic technical awareness.
  - Owns the session in the room: speaker intro, time cards, Q&A, transitions.
- **AV tech**
  - Fit: certified on the room's equipment, fixes faults live.
  - Goes through a per-role gate.
- **Floater**
  - Fit: knows the venue, flexible, no fixed post.
  - Name it "floater" so it is never confused with a speaker host.

### Contract clauses

1. Every post has a named person and a named backup.
2. Every person is briefed before their first shift, including the code-of-conduct script.
3. Arrival buffers are inside the published shift time: 15 minutes, or 30 for first-timers. A 14:00 shift means arriving at 13:45.
4. One named referent per shift gives live direction. Nobody takes conflicting orders from whoever walks past.
5. Replacement rule: nobody leaves a post without confirmation of a replacement.
6. Registration staff sign a data-handling clause covering access scope and no copying of attendee records.

### Briefing (per role, numbered, times in minutes before the event)

1. Arrive 15 minutes before the shift, or 30 if new. Collect your shirt and assignment.
2. Be at your post 10 minutes before the first session.
3. Meet each speaker 10 minutes before the slot.
4. Introduce the speaker in 30-60 seconds. Use visible time cards, run Q&A, cover the transition.
5. Route problems to named channels. A no-show speaker goes to the coordinators immediately. A technical fault goes to the AV lead.

### Code-of-conduct escalation script (brief it to every person in a shirt)

1. Ensure immediate safety, first for the affected person and then for yourself.
2. Ask the behaviour to stop only if it is safe. You are **not** required to confront anyone. Say this aloud.
3. Report immediately to the response team.
4. Document what, when, where and who was present, while it is fresh.
5. Support the affected person until the response team arrives.

Use the published policy and channels from `event-code-of-conduct`. Do not rewrite them. A script that differs from the policy is worse than none.

### Coverage protocol (publish with the shift grid)

1. If you cannot make a shift, post your name, post, time slot and late-or-absent status to the staff channel as early as possible. A named coordinator answers it.
2. If your relief has not arrived, wait 10 minutes. Then contact the coordinator by chat, by the published phone number, or in person.
3. **Do not leave until a replacement is confirmed.**
4. The reserve is the floaters. Below that, it is your 3 FTE. Tell them now.

Channels:

- Live coordination: one chat channel with a per-role room.
- Pre- and post-event announcements: email.
- Emergencies: a published phone number.

## 5. Timeline

All dates are relative to the event. The event date is not given.

1. **T-12 weeks:** run the RFQ with `event-vendor-sourcing`. Confirm venue AV rules.
2. **T-10 weeks:** sign contracts with the clauses above.
3. **T-6 weeks:** receive the run of show and reconcile the post list.
4. **T-3 weeks:** vendors submit named staff and named backups for every post.
5. **T-1 week:** hold the briefing as a scheduled session, with the code-of-conduct script and the badge-system gate.
6. **Day before:** walk the venue, test the badge print run, run the AV check in every room.

## 6. Measurement

Track coverage, not sign-ups. Compute it per hour, not as a daily total.

- Post-hours covered, as a share of post-hours required.
- Share of posts with a named backup.
- No-show rate, and the share where a replacement was confirmed before the post was left.
- Share briefed before their first shift, including the script. Target 100%.
- Share of shifts that started on time, with the buffer included.

**Pass threshold:** every post-hour is covered by a named person with a named backup, and every person is briefed on the escalation script before their first shift. I set both thresholds myself. They are not industry standards.

## 7. Questions that change this plan

1. Does the venue mandate in-house AV or labour?
2. Is the run of show drafted, and which posts does it name?
3. Who owns this on your team? The skill calls this person the Volunteer Lead.
4. What is the real Day 1 arrival curve? Pre-registration and mobile check-in could cut the desk by half.
5. Do you want employee volunteers for room monitors? They would need the skill's full program: a role catalog, sign-up, confirmation, shifts and recognition.

I only read `SKILL.md` and its three reference files. I did not read the sibling skills (`event-vendor-sourcing`, `event-code-of-conduct`, `event-run-of-show`), so the details here assume what the skill says about them.