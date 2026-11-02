# PyLisbon volunteer portal: what to include

**Short answer: build almost none of it.** At 150 people, one room and a 3.5-hour evening, the skill names a custom volunteer site as a failure mode ("Building the volunteer site for a 150-person event"). It would cost a month of your time to replace a spreadsheet and a chat group. Build the lightweight version below, and keep the portal as a trigger-based upgrade.

Assumptions, because I haven't seen your run of show:
- This is the informal, network-sourced rung.
- The post list below is provisional. Reconcile it with the real run of show.
- Doors open 18:30, the check-in desk opens 18:15, and talks end around 21:15.

## 1. Why not the portal

A dedicated volunteer site only pays off when one of these holds:
- More rooms than one coordinator can staff by hand. **You have one room. ❌**
- Volunteers must self-serve across a multi-day, multi-room grid. **You have one evening. ❌**
- The event recurs, so the site is built once and reused. **Twice a year. ✅**

Only one of three holds. The reuse is also tiny: roughly 8–10 people, twice a year.

Each portal feature you listed has a cheaper equivalent:

| Portal feature | What to use instead |
|---|---|
| Account sign-up | One sign-up form, tied to your existing registration if it can carry a checkbox |
| Shift self-service | A published shift grid (shared sheet). Volunteers pick a role and a slot on the form, and a named coordinator confirms each one. |
| Automated reminder emails | 2–3 scheduled emails from the mail tool you already use (see §6) |
| Profile page per volunteer | Skip. It adds personal data for people who aren't attendees and needs a retention rule and an owner. Keep a minimal consented past-volunteer list instead (§7). |

## 2. Post list (the sizing basis)

Size from posts and hours, never from attendee count.

| Post | Simultaneous | Window | Shift-slots |
|---|---|---|---|
| Setup | 3 | 17:15–18:15 | 3 |
| Check-in desk | 2 | 17:45–19:45 (opens 18:15, rush) | 2 |
| Latecomer door (own post, closing session) | 1 | 19:45–22:00 | 1 |
| Room lead (introduces speakers, keeps time, Q&A) | 1 | 18:15–22:00 | 2 |
| Speaker host (meets speaker, tests slides, walks them in) | 1 | 18:00–21:15 | 1 |
| Floater (no fixed post) | 1 | 18:00–22:00 | 2 |
| Teardown | 3 | 22:00–22:45 | 3 |
| **Total** | | | **14** |

- Name the room lead and the speaker host as separate roles. Two independent conferences split them, and one person doing both is in the wrong place at every handover.
- Treat the floater as a real post. Without one, every surprise pulls someone off a post.
- Count setup and teardown as posts. Otherwise the organizers carry chairs at 22:45.

Roster size depends on one answer: how many shifts each volunteer will take. Evening events mostly get one shift each, and setup or teardown pairs naturally with a post.

| Shifts per volunteer | Volunteers needed (plus backups) |
|---|---|
| 2 | about 7 |
| 1 | about 14 |

- Ask the shifts question on the sign-up form and sum the actual answers.
- Recruit against the pessimistic end, around 10–12, and release people if you over-fill. Don't recruit optimistically and then cut posts.

Code of conduct: the response team (at least 2 identifiable people reachable all evening) comes from the organizers or a separate application. It is not drawn from the general pool. Pull its roster from your code-of-conduct doc.

## 3. Roles and fit criteria

Publish this page before sign-up opens. People choose a role, not a slot.

- **Check-in:** calm and clear with strangers, punctual. This post handles the attendee list, so assign **named people**, not open claims.
- **Latecomer door:** same as check-in, plus comfortable with a short, firm "we'll get you in at the next break".
- **Room lead:** comfortable speaking to about 150 people, keeps time, calm under pressure.
- **Speaker host:** punctual, confident with the projector and slides, good at reassuring nervous speakers.
- **Floater:** knows the venue, flexible. Reliable floaters are your first promotion pool.
- **Setup/teardown:** can lift, show up on time. These are the unglamorous shifts.

Add routing questions to the form ("Like talking to people? → check-in or door. Want variety? → floater.").

One training gate only: a 5-minute briefing for check-in covering what is on the list, no screenshots or photos of it, and where it lives afterwards. If any post takes cash, tell me and it gets the same treatment.

## 4. Recruitment (default channels, re-ranked)

1. **Past-volunteer call-back.** If you have last edition's list, this is one email and it jumps to first. You didn't say, so I'm assuming not.
2. **Direct network ask.** Regulars and organizers' contacts, with named posts and times.
3. **Call from the stage** at the next meetup, naming concrete posts and hours, with a named coordinator who answers every reply within days.
4. **Registration-gated form**, or a checkbox on the ticket flow if your registration tool can carry one.

Cut from the plan: an open call with no coordinator and no confirmation step. It produces a list of names and an empty desk.

Timing, working back from the event (T = event day):
- T-4 weeks: publish the roles page and open sign-up.
- T-3 weeks: confirm every sign-up individually, by name.
- T-1 week: close the roster and hold the briefing.

If a t-shirt or lanyard order sets an earlier deadline, that date wins.

## 5. Sign-up form (minimum fields)

- Name, email.
- Role preference (using the routing questions).
- "How many shifts can you cover?"
- What you want from the evening (a talk, people to meet, a skill to practise). Match posts to it.
- First time volunteering? (This sets a longer arrival buffer.)
- Dietary needs (you're feeding them, see §8).
- Consent checkbox for keeping their name and email for the next edition.

Collect nothing else. Name an owner and a retention rule for this data before the form goes live.

## 6. Shift grid, confirmation and reminders

- Every slot gets a **named person and a named backup**, and every post gets a confirmation reply from a named coordinator.
- **Publish arrival buffers inside the shift time.** A desk that opens at 18:15 has a shift that starts at 17:45. First-timers get an extra 15 minutes. Publish "arrive at 17:45", not "shift starts 18:15".
- **Reminder emails** (scheduled sends from your mail tool, no portal needed):
  - Confirmation, on sign-up.
  - T-7 days: briefing time and grid.
  - T-1 day: shift time, buffer, venue entrance and emergency contact.
- **Three channels:** a coordination chat for the evening, an email list for announcements before and after only, and an emergency phone number. Tell people to ask in the shared chat, not in DMs.
- **One named referent per shift** who owns live direction. Volunteers check with that person, not with whoever walks past.

## 7. Briefing (all volunteers, before their first shift)

Hold one scheduled 20–30 minute session around T-1 week. A hallway chat on the night doesn't count. Cover all three items. Together they cost about the same as skipping one, so there is no cheaper subset.

1. **Post choreography.** Numbered steps with times as minutes-before (for example, "meet the speaker 10 minutes before their slot"), and which channel each exception goes to.
2. **Escalation contacts.** Who to call for what, and on which channel.
3. **Code-of-conduct script,** for everyone, because any volunteer may be the first person a report reaches:
   1. Ensure immediate safety (the affected person first, then yourself).
   2. Ask the behaviour to stop **only if it is safe**. Say out loud that volunteers are **not required to confront anyone**.
   3. Report immediately, in person or through the anonymous path.
   4. Document what was said and done, when, where and who was there.
   5. Support the affected person until the response team arrives.

   Brief the script exactly as your published policy words it. A script that differs from the policy is worse than none.

**Coverage protocol** (publish it with the grid):
- If you can't make a shift, post in the volunteer channel early with your name, post, slot, and whether you'll be late or absent.
- If your relief hasn't arrived after 10 minutes, contact the coordinator by chat, phone or in person.
- **Don't leave your post until a replacement is confirmed.** The usual failure is not a no-show. It is the person on post leaving into an empty handover.
- Name the coordinator who finds the replacement, and name who covers if there are no floaters (the organizers, who should know it in advance).

## 8. Recognition

- **Access in exchange for the shift.** Room leads and speaker hosts hear the talks, and you can save others a seat in the room.
- **Food at the post.** The 18:00–22:00 window covers dinner, which is one of the cases where feeding them properly moves up. Tell your caterer or pizza sponsor the headcount ahead of time. Floaters and the door can't leave, so bring food to them.
- **Identifiable volunteers.** A coloured lanyard or shirt works, since attendees need to find them. In one room a lanyard is probably enough. That is my judgment, not from the sources.
- No cash stipend.
- Naming volunteers in a public thank-you, and the alumni and retention loop, belong to the volunteer-experience skill and carry a consent gate. Handle them there. Until then, keep only the consented list from the form.

## 9. What to measure

Don't track sign-ups. Track:
- Post-hours covered as a share of post-hours required, computed **per hour**, not as a daily total.
- Share of posts with a named backup.
- No-show rate, and the share where a replacement was confirmed before the post was left.
- Share of volunteers briefed (including the escalation script) before their first shift. Target 100%.
- Share of shifts that started on time, measured against published times with the buffer included.

**Pass:** every post-hour is covered by a named person with a named backup, and every volunteer is briefed on the escalation script before their first shift.

## 10. When to build the portal later

Revisit only if:
- You add rooms, days, or a second venue.
- Volunteers regularly exceed what one coordinator can confirm individually (roughly 30 or more).
- The shared sheet and scheduled emails visibly stop scaling.

Until then, spend that quarter on the roles page, the briefing and the coverage protocol. Those are what actually prevent an empty desk.

## Questions to settle (they could change the plan)

1. Do you have a past-volunteer list from earlier editions? If yes, call-back becomes the first channel.
2. Does any post handle cash or tickets sold at the door?
3. Can your registration tool carry a volunteer checkbox?
4. Who is the named volunteer coordinator, and what is your actual run of show (talk end time, any closing session)?
5. What is the roster deadline, and does a shirt or lanyard order fix it?
6. How many shifts per person do you realistically expect, based on your regulars?