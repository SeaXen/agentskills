# Harborline Devcon: run of show (draft v0.1, for section-by-section validation)

I can't finish this yet. Two things the skill won't let me invent are missing. I've built everything that doesn't depend on them, and I've marked the gaps in the text.

## 0. Blockers

| # | Blocker | Why it blocks | Who closes it |
|---|---|---|---|
| 1 | **No disruption priority order.** The programme team gave you only the grid. | The skill says to get it, not invent it. If it's improvised at 14:00, a keynote gets cut to save a sponsor slot. | Programme team. They need to answer: which session is the headline commitment people came for, and does any sponsor slot have a contractual position? Then they write the four-rung order into the schedule document. |
| 2 | **I don't have the grid itself.** I have no times, room names, or talk and speaker names, only the counts (38 talks, three keynotes, three rooms, two days). | A cue sheet is a row per segment and per transition. I won't make up times. | Paste the grid. Every `⟦…⟧` below is filled from it. |
| 3 | **Priya is both MC and introducer of every speaker.** | The skill names this as a failure mode. The MC orchestrates the flow, and the introducer is a separate role assigned per session. Also, there are 38 talks over 3 rooms, and she can't be in three rooms. | Fixed in §1 below. Needs your OK. |
| 4 | **Printed emergency plan: does it exist, and who is on it?** | The incident path triggers into it. I don't rewrite it. If it doesn't exist, it's `event-risk-management`'s job and it blocks the incident row. | You. |
| 5 | **Shift plan.** I need the shift boundary times and the 22 names. | Handoffs are placed on those boundaries. The volunteer lead built the plan, and I treat it as an input. | Volunteer lead. |

Three more answers re-rank the menus. Please answer them in this order:

1. Do you have mobile coverage everywhere staff will be, and does the venue run its own radio net?
2. Do you have a hard print deadline for the cue sheet and a briefing date? The event is in three weeks, so that is roughly 19 days from today.
3. Is the opening recorded or livestreamed, and does any sponsor contract fix wording that must be read verbatim?

I've also assumed this is a recurring event with a community-run organizing crew, not a hired MC. I assumed it because Priya is on stage anyway and you have volunteers. Tell me if either assumption is wrong.

## 1. Roles (section 1 of 4)

**Proposed split (needs sign-off).** Priya keeps the MC role and drops the introducer role.

| Role | Who | Scope |
|---|---|---|
| **MC** | Priya | Opens and closes both days and orchestrates the flow. She is on stage for the three keynotes and all plenary moments. She is reachable but not monitoring a channel (someone stands next to her who is). Which room she MCs between keynotes depends on the grid: ⟦fill from grid⟧. |
| **Speaker introducer** | One per room per half-day (6 rooms-halves × 2 days = up to 12 people), drawn from the 22 volunteers or organizers | Introduces each speaker in that room by name and topic only. Rotates freely. Priya introduces only the keynotes, because she's on that stage anyway. |
| **Organizer on duty** | ⟦name⟧ per block, never Priya | Takes last-minute decisions for the block. Target of every routine escalation. Must not also be MC, a speaker or a room lead. |
| **Room lead** (×3) | ⟦3 names⟧ | Owns the room's clock. See authority below. |
| **Tech owner per room** | ⟦3 names⟧ | One machine, one operator, paired with the room lead. |
| **Post leads** (×3) | ⟦registration, info desk, sponsor hall⟧ | Stationary. They escalate to the organizer on duty. |

**Room lead authority.** This is my convention, not an industry standard. Edit it freely.

- *Alone:* hold a start up to ⟦5⟧ min, cut Q&A to hold the end time, call the tech owner, reorder nothing.
- *Must escalate:* any start delay beyond ⟦5⟧ min, any no-show, any swap of two talks, anything touching a keynote or a sponsor slot.

**Open design question.** Priya is the MC and also unavailable for on-duty. Please confirm she is excluded from the rota. The skill promotes the pair rung for "an on-duty person who is also the MC", so excluding her is cleaner.

## 2. Cue sheet (section 2 of 4)

**Depth: scripted transitions.** That's one rung above the default timed grid with named owners. The skill moves up as soon as more than one room runs at once, and you have three rooms.

**Word-for-word script for the opening and closing only** if blocker Q3 answers yes (recorded or livestreamed, or contract wording). If not, I use the opening checklist below as prompts and Priya improvises, which is the community pole.

**The public schedule is deleted as a staff document.** Staff work from this sheet only.

### Row template (every segment and transition gets one)
`Clock · Room · Owner (name) · Tech owner (name, machine, where material lives) · Said · What physically moves · Escalates to (organizer on duty for block)`

### Timing conventions (mine, not sourced)
Times are relative to the grid. `T` is the published start of the segment.

- **T-15:** next speaker is seated in the queue chair next to the stage. The room lead confirms verbally.
- **T-10:** the tech owner has the deck loaded. All decks are collected in advance as PDF or one agreed format in a shared folder. Handover is a file switch, never a laptop swap.
- **T-0:** introducer reads one line, in the form "name, topic".
- **End-5 min:** the room lead stands at the side of the stage (a visible signal, not a spoken one).
- **Room reset** between uses of the same room gets its own timed row, owner named, started while the previous segment is still running.

### Spoken line at each handover
The skill says to repeat the constraint at the point of use, even though speakers were briefed. Use something like: "Your slides are already loaded. Q&A ends at ⟦end time⟧, and I'll stand at the side with five minutes left."

### Opening (Day 1): the deepest row
Content checklist from the MLH opening-ceremony page (your event's keynote or welcome slot stands in for the partner slot):

- What the event is, framed for first-timers.
- Who the organizers are and how to reach them (the info desk and the attendee-facing channel).
- Wifi, the communication channel, venue logistics (rooms, sponsor hall, toilets, food).
- The schedule, with the keynotes and anything time-fixed called out.
- Sponsor content, kept short. Any contractual wording is read verbatim from a card.
- Code of conduct and who to tell.

| Row | Detail |
|---|---|
| **Day 1 opening** | ⟦clock⟧ · Main room · Owner: Priya · Tech: ⟦name⟧ · Pre-announce "opening in 5 minutes" at ⟦T-5⟧ · Escalates to: ⟦organizer on duty⟧ if a keynote speaker is not in the queue chair at T-10 |

### Closing (Day 2)
- Pre-announce the closing at ⟦T-10⟧.
- Use slides, not live narration, for any thanks or results. Collect partner and sponsor items in advance.
- No live demos at the closing.
- **Venue handback as a timed group activity:** organizers walk every room announcing "three minutes to pack up". Rooms must be cleared before the closing starts if nobody returns to them.
- Keep the energy up, because people remember the beginning and the end.
- Day 1 gets a short close too: tomorrow's start time, where to find the info desk, a reminder of the evening plan.

### Rows to generate once I have the grid
| Row type | Count (at least) | Notes |
|---|---|---|
| Talk | 38 | Introducer, tech owner, room lead named per row |
| Keynote | 3 | Priya introduces. Tech check row at T-60. Escalation target is always the organizer on duty. |
| Transition between talks | one per talk | Includes the queue-chair step |
| Room reset | every reuse of a room | Named owner, starts before the prior segment ends |
| Post cover rows | registration, info desk, sponsor hall | Registration and the doors peak at the opening, and a lunch cover row for each post |
| Opening, close, Day 1 close | 3 | See above |

**Per-slot execution budget** applies only where a slot carries live execution risk (live demo, back-to-back sponsor slots, anything shorter than 20 minutes). I'll pull those out of the grid. Don't reuse the MLH demo figure (10 minutes per team: 3 demo, 1 to 2 questions, 5 to 6 swap). That is one event's number for one format.

## 3. Comms and escalation (section 3 of 4)

**Medium.** I need your Q1 answer (coverage, venue net). My default, by posts running at once, is **text-plus-live pair**:

- A **written org-only channel** that leaves a log for handoffs and the post-event review.
- A **live channel**, either a voice channel or radios.

**Promote to radios** if any of these hold: coverage fails somewhere staff stand, the venue spans floors or buildings, staff hands are full (registration, the sponsor hall), or the venue already runs a net you must join. Six posts staffed at once and 22 volunteers make that likely. If radios, I write call signs and push-to-talk etiquette, and you check the band is licence-free for your jurisdiction. Radio discipline is my convention.

**Never use the attendee-facing channel for organizer traffic.** It stays public, and organizers monitor it as a question channel only. Create the org channels this week, not on the morning.

### Channel assignment
| Role | Written | Live |
|---|---|---|
| Organizer on duty | Yes, for the whole block | Yes |
| Room leads | Yes (for the next shift's benefit) | Yes |
| Tech owners | No | Yes, paired with room lead |
| Registration, info desk, sponsor hall | No | Yes only (they are stationary and busy) |
| Priya (MC) | No | Reachable via her stage-side companion, who is on live |

Room leads escalate to the organizer on duty, never sideways, so one person holds the whole day's picture.

### Two escalation paths (both go on the printed sheet)
| | **Routine** | **Incident** |
|---|---|---|
| Trigger | A post hits something above its authority (ticket dispute, a policy question, a speaker issue) | Safety, medical or security |
| Goes to | The organizer on duty for that block, by the org channel | The printed emergency plan's contacts, by the fastest route |
| Owned by | This document | `event-risk-management` authors, this document executes. Blocked until the plan exists (blocker 4). |

Every post must name the organizer on duty for the current block without asking anyone, so the on-duty names are printed on the sheet at every post.

### Live disruption sequence
1. **Name it at the room.** The room lead says what has happened and starts the clock.
2. **Route it.** What the post can resolve alone, it does. Anything above authority goes to the organizer on duty. Safety, medical or security goes to the emergency plan.
3. **Decide against the published disruption order**, not the room: ⟦programme team to supply; the skill's default shape is: 1. protect the plenary or keynote, 2. protect the headline commitment, 3. minimize how many other sessions the fix touches, 4. lock the revised grid for the block⟧. Blocker 1 stays open until the programme team confirms it, particularly what the headline commitment is.
4. **Lock the revised grid** for the rest of the block.
5. **Say it out loud, in the room and on the channel.** The announcement convention is mine: the on-duty organizer calls the decision and everyone acknowledges with "copy". The wording is agreed in advance.
6. **Write the row that was wrong** on the written channel while it's happening.

**Who holds which authority at step 3** is yours to decide. My proposal: the organizer on duty decides anything within one block. A keynote delay or cut needs the on-duty organizer plus Priya's agreement, because she is the one on stage. Attribute that to whoever signs it off.

## 4. Rotation and handoffs (section 4 of 4)

The rotation is the published practice (DevOpsDays: on-duty shifts so one person isn't the single point of failure in crisis mode). The handoff mechanics are borrowed from on-call engineering practice, not an events standard, and the overlap length is yours to set.

**Recommended rung: timed overlap with live verification**, one above the default named on-duty person. Your shifts change hands during a live programme, which is the skill's trigger for moving up. The `paired on duty` rung is worth it for **Day 1 opening to first lunch** if this is the first edition. Tell me if it is.

- **Named on-duty organizer per block**, printed on the sheet at every post. Placeholder: ⟦Day 1 AM, Day 1 PM, Day 2 AM, Day 2 PM⟧ pending the shift plan.
- **Overlap window** of ⟦10⟧ min (my number): the outgoing person writes the handoff first, then they talk it through.
- **Six-section written handoff.** Each section needs an entry or an explicit "none" (that separates "nothing to report" from "nobody checked"):
  1. Open problems
  2. Segments running off-plan
  3. People (missing, late, unwell, six hours on their feet)
  4. Venue and tech workarounds
  5. Decisions already taken this block
  6. Coming up in the next block
- **Live check before the outgoing person leaves:** the incoming person sends one message and gets one answered, on both channels. This catches a flat radio battery, muted notifications, and a channel they were never added to.
- **Mid-incident handoff** uses a separate, denser template: what is happening, what's been tried, who is involved, the pending decision, and its deadline. Hold the boundary until the incident closes where you can.
- **No-overlap boundaries** (a volunteer who leaves early): a written quick handoff plus a short recorded walkthrough, and name someone reachable. If several boundaries lack overlap, send it back to the volunteer lead as a rota problem.

## 5. Closeout

1. Timed pack-up announcement in every room, then the venue handback against the contract.
2. Release staff explicitly, not by attrition.
3. **Same day**, capture the failures while they are fresh: wrong rows, transitions that ran long, and escalations that never reached anyone. A cold retrospective loses the timings.

## 6. Completeness gates and metrics

These are the two completeness gates, checkable before doors open:

- Every staffed post can name the organizer on duty for their block without asking anyone.
- Every segment on the cue sheet has a named owner, and every shift boundary has a handoff record with an entry or "none" in each section.

Pick metrics before the day. All of these are ones we set ourselves, not benchmarks:

- **Transition dead air**, counted separately for scripted and unscripted transitions.
- **Live changes made against the published disruption order** versus improvised ones. Drive the improvised count down.
- **Escalations that reached the on-duty person.** Zero usually means nobody could reach anyone, not that nothing happened.

My pick is the first two, plus cue-sheet drift (rows that turned out wrong) for the next edition's template.

## What I need from you

1. The grid (times, rooms, titles, speakers).
2. The programme team's disruption priority order, or at least which session is the headline commitment.
3. OK on Priya being MC only, with a rotating introducer pool.
4. The shift plan, the names, and the shift boundary times.
5. Whether a printed emergency plan exists.
6. Your answers on coverage and radios, the print and briefing deadlines, and whether the opening is recorded.

Once I have 1, 2 and 4, I'll generate the full row-by-row sheet and hold it for your validation before it's printed. Every change after printing costs a person holding the old copy.