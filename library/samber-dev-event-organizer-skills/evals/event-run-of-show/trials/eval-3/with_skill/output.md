# Northfold Summit: comms setup and who is on what

**Next actions, in order (about 45 min total, this week):**
1. ⏳ **Call the venue (15 min).** Ask for their radio band and channels, a loaned venue-net radio for your AV liaison, a named venue duty contact, and whether the basement has Wi-Fi.
2. ⏳ **Check the 12 radios (15 min).** Confirm the model is licence-free in your jurisdiction, charge them all, and count the chargers.
3. ⏳ **Do a walk test at the venue (about 1 h, the day before at the latest).** Key a radio from the basement to every room and both floors. If the basement fails, use fallback F below.
4. Fill the name slots in the role table and send me the two missing documents (see "Blockers").

I assumed a one-day event, a community-run team (organizer-hosts, not one hired MC) and a venue that allows your own radios. Correct me where those are wrong.

## Blockers

- ⚠️ **Disruption priority order.** The schedule document should have handed it over. I haven't seen one and won't invent it. Paste it into the "Live disruption" section before printing. Deciding it at 14:00 in front of a full hall is how a keynote gets cut to save a sponsor slot.
- ⚠️ **Printed emergency plan with names.** I only wire it in. `event-risk-management` writes it. If it doesn't exist yet, that work blocks the incident path below.

## 1. Architecture: three layers, kept separate

| Layer | Medium | Who is on it | Job |
|---|---|---|---|
| **Live** | Your 12 radios, your own channel | 11 post leads plus 1 spare | Real-time coordination |
| **Log** | Private organizer text channel, separate from the attendee Discord | All 14 organizers, plus the runner on stairwell checks | What the next shift and the next edition read |
| **Public intake** | Attendee Discord, `#ask-organizers` | Watched by one named person | Attendee questions only, never organizer traffic |
| **Venue bridge** | Venue AV net | AV liaison only | Passes AV problems to venue crew |

- **Why radios:** 5 staffed posts across 2 floors plus a basement with no signal. A text channel can't reach the basement, and a text channel scrolls faster than staff can read at that scale.
- **Why the log layer stays:** radio leaves no record, and handoffs and the retro need one.
- ❌ **Don't use `#ask-organizers` or anything attendee-facing for organizer traffic.** It exposes the problem to the people it concerns and buries the message that mattered.
- ❌ **Don't talk over the venue net, and don't put your organizers on it.** Join it through one bridge person.
- ⚠️ **Radios in the basement are unproven.** Basement-to-upper-floor propagation through concrete is often poor, and "no mobile signal" says nothing about it. The walk test settles it. Don't assume.

## 2. Roles: who is on what

Names are slots. "A volunteer" isn't an owner, so fill every slot before printing.

### 14 organizers

| # | Role | Radio | Name |
|---|---|---|---|
| 1-4 | **Organizer on duty**, one per block (see §5). Does nothing else during their block. Off-block they float. | Passes with the role | ____ ×4 |
| 5-8 | **Room lead**, Rooms 1-4. Owns that room's clock. | Yes, 4 | ____ ×4 |
| 9 | **Hack space lead** (basement). Owns the clock and is the only organizer down there. | Yes | ____ |
| 10 | **Registration/info desk lead** | Yes | ____ |
| 11 | **AV liaison**. Holds the organizer radio and a loaned venue-net radio. Bridges the two nets. | Yes, plus the venue radio | ____ |
| 12 | **Incident lead**. Named on the printed emergency plan and never the same person as the one on duty. | Yes | ____ |
| 13 | **MC**. Reachable, not monitoring. Has a minder. | No | ____ |
| 14 | **Discord watcher + log keeper**. Sits at a screen. Triages `#ask-organizers`, and types each radio decision into the log. | Listen-only | ____ |

- **Speaker introducer** is a separate role from the MC, assigned per session. It rotates freely and is staffed from the room's volunteers.
- **MC minder:** the lead of the room the MC is in. A person on stage can't watch a channel.

### Radio count: 12

On-duty 1, room leads 4, hack lead 1, desk 1, AV liaison 1, incident lead 1, watcher 1, basement runner 1 (volunteer), **spare 1**.

- ℹ️ The spare lives in a charger at the desk. It covers a dead battery or a failed radio, and the incoming on-duty person uses it during a handoff overlap.
- ✅ 12 is enough because posts carry radios and individuals don't. The other 33 people reach someone with a radio face to face.

### 30 volunteers (draft sizing; the `event-volunteers` shift plan is the real input)

| Post | Count | Notes |
|---|---|---|
| Rooms 1-4 | 12 (3 each) | Door, timekeeper/introducer, mic runner |
| Hack space | 5 | 1 is the **basement runner** (holds a radio, takes stairwell check-ins) |
| Registration | 6 | Fold to 2 after the doors rush and redeploy the rest |
| Info desk | 2 | |
| Floor runners | 2 | One per floor |
| Float/relief | 3 | |

Volunteers carry no radio. Each gets a printed card with:
- the on-duty organizer's name for every block;
- their post lead's name;
- one rule: **"Can't solve it? Ask your post lead, not an attendee thread."**

## 3. Radio net

These are my conventions, not an industry standard.

- **Channel plan:** Ch1 is Ops for all 12 radios. Ch2 is reserved for a jam or interference fallback, called by Duty. No functional split: 11 users on one net don't need it, and Duty has one radio and can't watch two channels.
- **Venue collision:** pick a Ch1 that differs from the venue's band and channels, once the venue tells you theirs.
- **Call signs by role:** `Duty`, `Room 1`-`Room 4`, `Hack`, `Desk`, `AV`, `Incident`, `Log`, `Runner`.
- **Format:** `[Who you want], [who you are]`, then `go ahead`. Keep it short.
- **Acknowledgement:** every instruction gets an immediate `copy`.
- **Privacy:** no names, medical or conduct detail on air. Say `Incident, Room 3, need you` and move to face-to-face.
- **Session rooms:** earpiece or vibrate, volume low. Step into the corridor to talk.
- **Radio check:** Duty runs a roll call at each block start and mid-block. A silent radio is not a quiet day.
- **Dead battery:** swap from the spare at the desk. The call sign moves with the post, not the radio.
- **Jam:** Duty calls `all stations, move to channel 2`, and everyone confirms.

**Venue net:** AV liaison takes AV problems to the venue crew. In-room venue techs are face to face with the room lead, so a failure produces one escalation, not two.

**Fallback F (if the basement fails the walk test):**
1. Pick the closest spot with working radio, probably the stairwell landing.
2. The basement runner stands there for scheduled check-ins, say every 15 min. That number is mine.
3. The runner also relays by foot on demand.
4. Put a sign in the hack space: "No signal here. Ask the hack lead."

## 4. Escalation: two rows on the cue sheet

**Routine (many times a day):**
- Volunteer → post lead, face to face.
- Post lead → `Duty` on radio.
- Duty decides, then logs the decision.

**Incident (safety, medical, security; rare):**
- Goes straight into the printed emergency plan's contacts.
- `Incident` on the radio, and the venue's own security.
- Duty doesn't improvise and doesn't rewrite the plan.
- If the radio is down, the nearest runner goes to the plan holder in person.

**Attendee questions:**
- Upstairs: Discord → Watcher → Duty via the log, or radio if urgent.
- Basement: Discord is unreachable, so attendees ask the hack lead or the desk. Say so in the pre-event email and in a pinned Discord message.
- 🔐 If the basement has Wi-Fi, this shrinks, but organizer radios are still needed.

## 5. On-duty rotation and handoff

- **4 on-duty organizers, one per block.** The venue spans floors, and a single organizer can't be the point of failure for every call.
- **Block boundaries** fall at lunch or a coffee break. Never inside a keynote or a live incident.
- **Handoff format:** a timed overlap with a written checklist and live verification. The overlap length is yours to set, say 10 min. It's borrowed from on-call practice, not an events standard.
  1. **Write.** The outgoing person fills six sections: open problems, off-plan sessions, people, venue/tech, decisions already taken, next block. Each needs an entry or an explicit **"none"**. "None" separates "nothing to report" from "nobody checked".
  2. **Talk.** Walk through it standing together.
  3. **Verify live.** The radio is physically handed over. The incoming person keys it and the outgoing person hears them, and one text is sent and answered. This catches a flat battery, a muted app, or a missing channel add.
- **Mid-incident:** hold the boundary until the incident closes. If you can't, use a denser brief (what's happening, what's been tried, who's on it, the pending decision and its deadline), and keep the outgoing person reachable.

## 6. Live disruption

1. Room lead names it and starts the clock.
2. Route it. The post resolves what it can. Anything above its authority goes to `Duty`. Safety goes to the plan.
3. Duty decides against the disruption order: **[paste the schedule document's order here]**.
4. Lock the revised grid for the rest of the block.
5. Announce it on the radio and in the room. A change nobody announced gets undone by the next person reading the printed sheet.
6. `Log` writes the wrong row immediately.

**Room lead authority (my proposal, needs your sign-off):**
- Alone: hold a start inside the buffer, cut Q&A, fetch tech, swap a volunteer.
- Escalate: moving or cancelling a session, using the buffer, touching any other room, anything involving the plenary.

## 7. Closeout

- Hand the venue back as the contract requires, and return the venue radio.
- Release staff explicitly, and count the 12 radios back in.
- Capture the day's failures the same day: wrong rows, transitions that ran long, escalations that never reached anyone, and where the radio dropped.

## 8. Gates and metrics (all self-set, not benchmarks)

**Gates, checkable before doors:**
- Every post can name its on-duty organizer without asking anyone.
- Every segment has a named owner, and every shift boundary has a handoff record with an entry or "none" in each section.

**Metrics:**
- Escalations that reached Duty. Zero usually means staff couldn't reach anyone.
- Radio roll-call failures per block. If it's more than 0 in the basement, revisit fallback F.
- Live changes made against the published disruption order versus improvised ones.

## Still to do (next sections, same validation loop)

- The cue sheet. With 5 parallel posts it needs scripted transitions, not just a timed grid.
- Room-lead and introducer briefing cards.

**Questions for you:**
1. What is the event date and print deadline?
2. Do you have the disruption priority order and the emergency plan with names?
3. Is the venue willing to lend a venue-net radio?