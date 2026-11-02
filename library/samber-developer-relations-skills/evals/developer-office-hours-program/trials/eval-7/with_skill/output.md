**Next action, 15 minutes:** message Dario's manager and thank them. Say Dario has covered 3 of the last 4 sessions, and ask them to confirm a cap of one session per month for him. Do this before anything else.

**Don't do any of your three ideas as stated.** The cause is not money or pressure. It is a rotation with no written cap, no manager agreement and no backup.

## Open decisions (need your answer)

1. **Why did four engineers stop?** Nobody has asked them. Spend 5 minutes with each: sprint conflict, no manager cover, no idea what would be asked, or the slot hits their focus time.
2. **Did their managers agree to this in writing?** I assume not. A kickoff meeting is not a commitment.
3. **Where are your users?** Region split decides the slot. The skill says to put the slot in the users' working day.
4. **How many real outside askers have come in five weeks?** I don't know. Charter bar below assumes you don't have a bar yet.
5. **What must never be recorded** (customer data, unreleased features)?

## Verdict on your three ideas

| Idea | Verdict | Why |
|---|---|---|
| $50 gift card per session | No | It pays for goodwill but fixes none of the causes: manager sign-off, cap, prep. Judgment call, not from the skill. The only sourced precedent, Kubernetes, kept the load to 1 hour/month per volunteer and thanked donating employers by name. |
| Fully optional | No | It is already optional in practice. That is why only Dario shows up. |
| Run solo, call "ask the engineers" aspirational | Only as a fallback | You are already a support desk that escalates afterwards. Engineers never see the questions, so they have no reason to come. |

## What I'd do instead

1. **Stop leaning on Dario.** Three sessions in about four weeks is three times the cap of one per month. He is your single point of failure. Kubernetes paused an edition when its panel pool ran dry.
2. **Go biweekly, announced publicly.** Weekly needs about six engineers (sessions per month plus one spare). You have five, so you are short. Biweekly needs three or four. Announce it as a cadence change, never a silent gap.
3. **Get written manager sign-off** for each engineer: cap of one session per month, and the session counts as work in their review.
4. **Book a quarter ahead with a backup per session.** Send the prep brief 48 hours before so the engineer reads real questions first.
5. **Keep your Slack escalation, but make it the async intake.** Engineers answer in a pinned thread, credited by name. For an engineer who can't do a live slot, owning an area of the thread keeps them in the rotation. This is my adaptation, not a skill rule.

## Charter changes

```
Job:            [pick one: unblock users | docs gaps | product signal | contributor growth]
Format:         drop-in call + async intake thread
Slot:           biweekly, in the largest user region's time zone [open decision 3]
Staffing:       Host you, backup host [name]; engineers A-E + Dario, cap 1 session/month each
Pilot:          6 sessions from the new start date. Announced pauses don't count.
Demand bar:     median ≥ 3 distinct non-staff askers per cycle (live or async), and
                ≥ 1 merged docs fix or feedback record per 2 sessions.
                Below it: async thread only for a quarter, then re-test.
Operating bar:  no silent cancellation, no engineer over cap,
                write-ups within 2 business days in all but one session
Recording:      notice at the start; publish the write-up instead of the recording
```

No organization publishes attendance benchmarks for office hours, so the bar of 3 is a self-set baseline. Replace it with your own after the pilot. Write the bar into the charter before session 1 so the review can't be fitted to the result.

## Rotation, one quarter (biweekly, 6 sessions)

Engineer names are placeholders except Dario. Each person has at most one session per month. Backup is the spare for that month.

| Session | Week | Engineer | Backup |
|---|---|---|---|
| 1 | 1 | B | Dario |
| 2 | 3 | C | A |
| 3 | 5 | E | B |
| 4 | 7 | A | C |
| 5 | 9 | Dario | E |
| 6 | 11 | B | A |

Dario hosts no session until week 9. He is the backup in session 1, which spreads the load without cancelling anything.

## Scope card (publish before session 1)

- **In scope:** product how-to, API errors, pipeline design questions.
- **Account, billing, contract:** support.
- **Pricing, licensing, paid tiers:** sales contact. Answer only what the public docs say.
- **Suspected vulnerability:** private security channel, never a public thread or recording.
- **Reproducible bug:** issue tracker; we help write it.
- **Feature request:** logged live in the feedback record; the product team decides.
- **Your own environment:** no live debugging. Send a minimal reproduction with secrets removed.

## Per-cycle timeline

- T-72h: nudge the intake thread with the engineer's name and area.
- T-48h: triage the queue; send the engineer the prep brief and scope card.
- T+2 business days: publish the write-up.

## Write-up skeleton (empty)

```
## [Program] - [date], with [engineer], [area]
### Answered / ### Answered here, not live / ### Redirected
### Logged for the product team / ### Docs we are fixing
Next session: [date, time, calendar link]. Submit questions: [link].
```

Credit the engineer and their team by name in the write-up. Open a docs ticket the second time a question family appears.

## Measurement (not measured yet)

| Signal | Target | Current |
|---|---|---|
| Sessions held / planned | all held, none silent | not measured yet |
| Distinct non-staff askers per cycle | median ≥ 3 | not measured yet |
| Merged docs fixes + feedback records | ≥ 1 per 2 sessions | not measured yet |
| Write-up within 2 business days | all but one | not measured yet |
| Engineer sessions per month | none over 1 | Dario over cap |

## If this fails

If the demand bar fails at session 6, stop the live call. Run the async thread for a quarter with the same rotation. Publish your repeat answers as docs, then re-test demand. Running solo is that fallback done openly, not a launch plan. Everything past the pilot is provisional.

## Time estimates

- Manager messages: 30 minutes.
- Five engineer conversations: 25 minutes.
- Rotation and public announcement: about 1 hour.

**Next:** send the Dario's-manager message now, then book the five 5-minute conversations.