# Thornbury Tech Days: Run of Show (v1)

**Status:** Draft built without your grid, venue plan, or talk list. I assumed one day on **Fri 23 Oct 2026** (9 days from today), doors 08:30, close 18:00. Every `[BRACKET]` is something to fill in or confirm. Change the times if your day differs. The structure holds either way.

**Rooms:** Room A (main, seats 400) and Room B (secondary, about 150).
**Roles:** Show Caller (SC), Stage Manager A / B (SM-A / SM-B), AV Lead, Speaker Wrangler (SW), Safety Lead (SL), Registration Lead.

---

## 1. Fixed schedule

| Time | Room A (main) | Room B | Owner |
|---|---|---|---|
| 06:30 | Crew call, AV load-in check | Crew call | AV Lead |
| 07:30 | Full tech check, mic and slide test, camera check | Tech check | AV Lead |
| 08:00 | Green room open, first speaker arrivals | | SW |
| 08:30 | **Doors**, registration | | Registration Lead |
| 09:15 | Seat the room, house music off at 09:25 | | SM-A |
| 09:30 | **Opening and welcome** (10 min) | | SC |
| 09:40 | **Keynote** (35 min) | Room closed, prep | SC |
| 10:15 | Transition (15 min) | Transition | SM-A / SM-B |
| 10:30 | **Slot 1**: Big Talk 1 | Slot 1: niche or workshop | |
| 11:15 | Break (20 min) | Break | |
| 11:35 | **Slot 2**: standard talk | **Slot 2**: standard talk | |
| 12:20 | Lunch (70 min) | Lunch | |
| 13:30 | **Slot 3**: Big Talk 2 | Slot 3: niche or workshop | |
| 14:15 | Break (20 min) | Break | |
| 14:35 | **Slot 4**: standard talk | **Slot 4**: standard talk | |
| 15:20 | Break (20 min) | Break | |
| 15:40 | **Slot 5**: Big Talk 3 | Slot 5: niche or workshop | |
| 16:25 | Transition (15 min) | Transition | |
| 16:40 | **Slot 6**: lightning talks or panel | Slot 6: open Q&A or hallway | |
| 17:30 | **Closing** (15 min) | | SC |
| 17:45 | Networking, doors stay open | | |
| 18:00 | Official close, then strike | Strike | AV Lead |

**Slot rules**
- Talks run 35 minutes plus 10 minutes of Q&A, which gives a 45-minute slot and a 15–20 minute change.
- The Show Caller holds a hard stop at the end of Q&A. If a talk overruns, the SM walks a "5 min" card, then a "stop" card.
- Overruns are never recovered by shortening breaks. Cut the next talk's Q&A instead.

---

## 2. Grid fix: separating the big talks

I can't see your grid, so I fixed it by rule. The three big talks are moved to **Slots 1, 3 and 5 in Room A**, one per half-day block, with a niche or workshop session opposite each. Nothing of equal draw runs against them.

**Why this works**
- No two big talks share a time slot, so no attendee has to choose between them.
- Room A holds all 400 people, so a big talk never overflows a 150-seat room.
- Room B's competing sessions are narrow-audience by design.
- The big talks are spaced about 3 hours apart, so attention stays spread across the day.

**How to apply it to your grid**
1. Pick the clashing pair and the talk that currently sits in Room B.
2. Move one of the pair into the nearest Room A slot that has no other big talk.
3. Move the Room B talk it displaces into the freed slot.
4. Check each speaker's travel or availability constraints before you confirm the swap.
5. Re-run this check: no slot may contain two sessions that each expect more than 150 attendees.

**Ranking sessions by expected draw** is a quick way to find the problem. Take RSVP or registration interest per session and flag any slot where two sessions exceed 150 each.

⚠️ If one of the clashing talks is a keynote-grade speaker who must be in a specific slot, tell me the constraint and I'll re-plan around it.

---

## 3. Speaker green room

**Location:** a dedicated room within a 2-minute walk of the Room A and Room B stage doors. It must not be a corridor, the catering area, or the public foyer. `[ROOM NAME / LOCATION]`.

**Setup**
- **Seating** for 12 at a time, with soft seating if possible and a few tables for laptops.
- **Power**: 8+ sockets, plus 2 spare chargers each for USB-C and Lightning.
- **Wi-Fi**: a private SSID or a password separate from attendees.
- **Food and drink**: hot drinks, water, light snacks, and a lunch served here 30 minutes before the public lunch. Ask about dietary needs when you confirm speakers.
- **Quiet**: a rule of low volume and no phone calls. One side of the room is for last-minute rehearsal.
- **Screen**: a TV or monitor showing the live stage feed with a visible session clock.
- **Mirror** and a bin.
- **Water and a spare shirt/jacket** for emergencies.
- **Printed run sheet** on the wall with each speaker's slot, their stage-door route, and their SM contact.

**Process**
1. Speaker Wrangler greets each speaker on arrival and checks them in.
2. Speakers do their **slide upload and mic fitting** at the AV desk before moving to the green room.
3. The SW walks the speaker to the stage door **15 minutes before their slot**.
4. The SM-A or SM-B meets them at the door and holds them until the previous talk's Q&A ends.
5. After the talk, the SW collects the speaker from the stage and offers a debrief. Speakers are also sent a thank-you message.

---

## 4. Main camera failure: backup plan

**Goal:** Room A's recording and livestream (if any) never fully stop, and the loss is under 60 seconds.

**Pre-event rigging (by T-1)**
1. **Camera B** (second camera on a tripod or fixed mount) is cabled to the switcher and **always on**. It should be a different make from the main camera if possible, so one fault can't hit both.
2. **Slide capture**: slides record from the presenter laptop feed on a separate recorder, so a slides-only version exists even if both cameras fail.
3. **Audio**: record the mixer's main output to a separate recorder. Audio is the minimum viable record.
4. **Spares**: 2 charged batteries, 2 blank cards, 1 spare HDMI/SDI cable, and 1 spare power adapter in a labelled bag at the AV desk.
5. **Continuous recording** to a local card on every camera, independent of the stream.

**Failure response**

| Step | Time | Action | Owner |
|---|---|---|---|
| 1 | 0–10 s | The AV operator calls "camera down" on the comms channel. | AV Lead |
| 2 | 10–20 s | Switch the program output to Camera B. | AV Lead |
| 3 | 20–60 s | Check the cable, battery and card on the main camera. | AV assistant |
| 4 | 1–3 min | If it isn't fixed, swap the main camera with the spare body or phone rig. | AV assistant |
| 5 | Ongoing | If the stream is live, add a lower-third or slide-only layout while changing over. | AV Lead |
| 6 | Post-session | Log the incident, then check that the full recording exists. | AV Lead |

**Decision triggers**
- A **single failure** switches to Camera B and continues.
- A **double failure** goes to slides plus audio only, with a short on-screen note if streaming.
- After any failure, the Show Caller tells the next speaker before they walk on.

**Test:** run the failover once during the 07:30 tech check by pulling the main camera's power. The switch to B must complete in under 20 seconds.

---

## 5. Evacuation procedure

⚠️ **This is a template.** The venue's own fire plan overrides it where they differ. Before the event, the Safety Lead must confirm every `[BRACKET]` with the venue's fire safety officer, and the venue must approve the final version.

**Roles**
- **Safety Lead (SL)**: owns the decision to evacuate with the venue and is the single point of contact for emergency services. `[NAME, PHONE]`
- **Show Caller**: stops the show, makes announcements, and keeps the SL's instructions flowing.
- **Room marshals** (1 per room plus 1 per exit, at least 6 in total): direct people and sweep rooms. Marshals wear high-visibility vests.
- **Registration Lead**: brings the attendee list to the assembly point.
- **First aider(s)**: `[NAMES]`, who go to the assembly point with a kit.

**Before the event**
1. Get the venue's fire plan, exit map, assembly point, capacity limits, and alarm type.
2. Walk every exit route with all marshals during setup. `[DATE/TIME]`
3. Confirm exits are unlocked and unobstructed. This means no stacked chairs, cables, or exhibition kit in escape routes.
4. Mark the assembly point: `[LOCATION, at least 50 m from the building]`.
5. Agree the plan for attendees who can't use stairs: `[REFUGE POINT / EVACUATION CHAIR / LIFT POLICY, as set by the venue]`.
6. Print exit maps for the registration desk, and show a "know your exits" slide before the first session in each room.
7. Brief all crew and speakers at 08:00. Speakers are told where their nearest exit is.

**On alarm or emergency**
1. **Stop the show.** The Show Caller cuts the sound and slides and announces: *"Ladies and gentlemen, we need to evacuate the building. Please leave calmly by the nearest exit and follow the marshals. Leave your belongings."*
2. Lights up to full and house music off.
3. Marshals open all exit doors and direct people to the nearest safe exit. Nobody uses the lifts.
4. Speakers and crew leave with the audience and don't stop to collect equipment.
5. Marshals sweep rooms, toilets, the green room and backstage areas, then leave. They report "clear" or "not clear" to the SL.
6. Everyone goes to the **assembly point**. The Registration Lead does a headcount against the badge scan list.
7. The SL tells the fire service about anyone missing or any known hazard. **Only the SL talks to the emergency services.**
8. **Nobody re-enters** until the fire service or the venue gives the all-clear.

**Medical emergency (non-evacuation)**
- Call `[EMERGENCY NUMBER]`, send the first aider, and clear a space around the person.
- The Show Caller pauses the session if needed.

**Re-entry or cancellation**
- The SL decides with the venue whether to resume.
- If resuming, the Show Caller re-sequences the day: cut breaks and Q&As, merge slots, and keep the closing session.
- If cancelling, post on the event channels and email all attendees as soon as practical.

**After**
- The SL writes an incident log within 24 hours, with times, actions and issues.

**Risk register**: this procedure replaces the evacuation entries in the old register. I haven't seen the register, so check that no other entry contradicts this section.

---

## 6. Countdown checklist (T-9 to T-0)

| When | Task | Owner |
|---|---|---|
| **T-9 (today, Wed 14 Oct)** | Lock the grid with the big-talk fix. Confirm Room A and B capacity with the venue. | Programme lead |
| T-9 | Ask the venue for their fire plan and a call with their safety officer. | SL |
| T-8 | Email speakers: slot, arrival time, green room, AV needs, and the slide deadline. | SW |
| T-7 | Book or confirm Camera B, spares, and the audio recorder. | AV Lead |
| T-6 | Recruit and brief marshals. Get high-visibility vests. | SL |
| T-5 | Collect slides. Build the master deck per room. | AV Lead |
| T-4 | Print run sheets, exit maps, speaker signage, and room signs. | Ops |
| T-3 | Send the final attendee email with schedule, venue access, and the code of conduct. | Comms |
| T-2 | Check catering counts, including the speaker lunch. | Ops |
| T-2 | Walk-through at the venue: exits, green room, camera positions. | Everyone |
| T-1 | Load-in and rig. Do the failover test and a mic check. | AV Lead |
| T-1 | Marshal briefing and exit-route walk. | SL |
| **T-0** | Follow the schedule in Section 1. | Show Caller |

---

## 7. Open items I need from you

1. **The grid.** Send the current version and I'll apply the swap concretely. Send talk titles and speakers, and I'll fill the table.
2. **Venue name and fire plan**, so Section 5 can lose its brackets.
3. **Real times**: are doors, lunch and close right?
4. **Is Room B really 150 seats?** If it's smaller, some workshops need a cap and a waitlist.
5. **Is the event livestreamed?** That changes how hard the camera plan has to work.