# Atlas Forge mentor side

✅ **Next action:** ask Kelvara for engineers, in writing, this week. Everything below depends on their answer.

## Core problem

Kelvara is the only allowed backend, so every team has the same single dependency. One platform blocker can stall teams in all four tracks. Money doesn't unblock a team at 3am. Mentoring therefore has two layers:

- **Platform layer** is the critical one, and it's the layer Kelvara hasn't staffed.
- **Track layer** is ordinary domain mentoring.

## Step 1: Ask Kelvara for more than money (this week)

A mandatory platform needs a staffed platform. Make these requests, in priority order:

1. **4 to 6 engineers** who can answer platform questions, on shifts, on site or remote.
2. **A named escalation contact** with a response target, for example 15 minutes during the day and 60 minutes overnight.
3. **A sandbox with enough quota** for 24 teams, provisioned before kickoff, so nobody spends hour 1 on signup.
4. **A starter template and docs link** your team has tested.
5. **A 45-minute onboarding workshop** at hour 1.
6. **An outage clause** in the rules. If the platform is degraded, the schedule extends or judging accounts for it.

⚠️ Also get these rule questions answered in writing:

- What counts as "backend"? Auth, static hosting, and third-party APIs (for example an LLM) are all unclear.
- What happens to a team if Kelvara has an outage?

**If Kelvara refuses the engineers:** recruit 4 to 6 independent mentors with Kelvara experience, and have your own team build and publish a starter template before the event. State openly in the rules that the sponsor staffs nothing. Don't pretend the gap is covered.

## Step 2: Mentor roster

24 teams means 6 per track. Target one mentor per 3 to 4 teams on the floor at any time.

| Role | Count | Job |
|---|---|---|
| **Platform mentors** | 6 to 8 | Kelvara questions only: setup, quotas, errors, data modeling on the platform |
| **Track mentors** | 8 (2 per track) | Domain, scope, and feasibility for that track's challenge |
| **Pitch and product mentors** | 2 | Demo scripts, story, cutting scope. Active from hour 24 |
| **Mentor lead** (an organizer) | 1 | Owns the queue, the roster, and the known-issues doc |

Around 17 people in total, with maybe 8 on the floor at once.

## Step 3: Two-room layout

- **Room A:** 12 teams, tracks 1 and 2.
- **Room B:** 12 teams, tracks 3 and 4.
- Track mentors stay in their room, so they don't walk between rooms.
- **A platform desk in each room.** Platform questions are the most frequent, so they can't wait for someone to cross the building.
- Pitch mentors rove between rooms.
- The mentor lead sits at the room boundary or near the door, with a shared channel to both desks.

## Step 4: Coverage by phase (36 hours)

| Hours | Phase | Platform coverage |
|---|---|---|
| 0 to 2 | Kickoff, onboarding workshop | All platform mentors present |
| 2 to 8 | **Peak 1:** setup and data modeling | 2 per room |
| 8 to 20 | Heads-down, overnight | 1 awake per room. Overnight, one shared desk plus Kelvara's on-call contact |
| 20 to 30 | **Peak 2:** integration and breakage | 2 per room |
| 30 to 36 | Polish, pitch coaching | 1 per room, plus both pitch mentors |

Shifts run 6 hours with a 30-minute overlap. Each platform mentor takes at most 2 non-consecutive shifts.

## Step 5: Operating rules

1. **One queue, not wandering.** Teams submit a request with a track or platform tag. The mentor lead assigns it. Slots are 15 minutes.
2. **Cap of 3 sessions per team** before hour 24, so loud teams don't absorb everyone.
3. **Mentors advise, they don't type.** Say this in the briefing.
4. **Known-issues doc**, live and shared. Any platform bug found once gets written down, so the 20th team doesn't rediscover it.
5. **Judging conflict rule.** Anyone who mentored a team can't score that team. Kelvara staff don't judge, since they have a stake in how the platform looks.
6. **Mentor briefing 48 hours before.** Cover the rules, the queue, the tone, and what to do on a platform outage.

## Step 6: Two weeks before

- Dry run: one organizer builds a minimal project on Kelvara from the docs, timed. The gaps they hit become the starter template and the known-issues doc.
- Send mentors the schedule, the challenge briefs, and the Kelvara docs link.

## Open questions for you

1. What are the event dates and the hour-0 clock time? I used relative hours above.
2. Is the venue open overnight, and do teams sleep on site? That changes the night shift.
3. Is Kelvara a company with reachable engineers, or only a funder? That decides which branch of Step 1 you're on.