## Event check-in: DuckConf edition 3

**Do this first:** recruit reviewers for the CFP. Then run `samber/dev-event-organizer-skills@event-talk-selection`.

⚠️ I could not resolve two dates. The file stores "CFP closes in 11 weeks" and "doors about six months out" as relative dates, written 10 weeks ago.
- If they count from the file's last update, the CFP closes in about 1 week. Doors are about 16 weeks out.
- If they were already counted from today, the CFP closes in 11 weeks.
- Look up the real CFP close date and write it as an absolute date. Reviewer recruitment is urgent either way: the file records 41 submissions and no reviewers.

### State summary (from your file)
1. DuckConf edition 3: single-day, single-track, in-person conference. Edition 2 ran last spring. Volunteer-run.
2. Doors are announced and fixed, roughly 16 weeks out. The CFP close sits somewhere between about 1 and 11 weeks out (see above).
3. In flight: the CFP is running, with 41 submissions at last count. The grid is not published.
4. Top open decision: who reviews the submissions.
5. Constraint: standing project, a few hours a week, doors date immovable. Budget is committed, with break-even at 280 paid tickets (in `budget.md`).

Your file already answers the format, lifecycle and funding questions, so I asked none of them. For the gates I used:
- **Format gate:** fixed, so I applied it as written.
- **Lifecycle gate:** `recurring` is open (edition 3).
- **Funding gate:** the `company` gate is closed (volunteer-run).

### Route
**`event-talk-selection`**, for the committee, the rubric, the conflict-of-interest brief and the scoring process. The CFP close is the hard clock, so this goes first.

Its scope covers committee composition and sizing against your effort ceiling. It does not cover finding or inviting reviewers (see the gap below).

### Short-list, highest value per unit of effort first
1. **`event-talk-selection`**
   - Bottleneck: 41 or more submissions and nobody to score them.
   - Cost: a few hours to size the committee and write the rubric and conflict brief, plus reviewers' time.
2. **`event-planning-timeline`**
   - Bottleneck: ten quiet weeks. The doors date is fixed, so the work-back plan needs a replanning checkpoint that cuts scope rather than moves the date.
   - Cost: one session.
3. **`event-landing-page`**
   - Bottleneck: the public page's call to action must flip from "Propose" to "Register" when the CFP closes.
   - Cost: small, if the page already exists.
4. **`event-marketing-plan`**
   - Bottleneck: 280 paid tickets to break even, with a programme still to announce.
   - Cost: a campaign from announcement to doors, plus the list consent you then owe.
5. **`event-sponsor-value-proposition`**
   - Bottleneck: your file records no sponsor state at all, and break-even rests on tickets alone.
   - Cost: the first step of a months-long motion on sponsors' calendars.
6. **`event-code-of-conduct`**
   - Bottleneck: speakers should see the policy before acceptances go out.
   - Cost: policy and response-team drafting, which then binds you.

**Re-rank, stated out loud:**
- The CFP deadline (Q6b) puts programme intake above fill-the-room.
- Volunteer-run (Q4a) promotes sponsorship. A standing few hours a week (Q7c) promotes it to second place by default, but I placed it fifth. Your file records no sponsor state, and the CFP clock is shorter.
- Q4a also deletes `corporate-event-strategy` and `business-event-formats`.
- I dropped the existence check (market-fit, positioning): edition 3 is decided and the call is published.
- The committed budget makes the money model near-free, so `event-budget` is not listed.

### Chain (open-call talks lane)
1. `event-talk-selection` hands over an accepted list.
2. `event-speaker-experience` takes it from acceptance to the post-talk thank-you.
3. `event-schedule-design` lays the accepted talks into the grid.
4. `event-run-of-show` executes the published grid.

### Not now
- `event-schedule-design`: after `event-talk-selection` returns an accepted list.
- `event-speaker-experience`: after acceptances go out.
- `event-speaker-sourcing`: after review shows programme gaps worth filling by invitation.
- `event-production`: after the grid exists and you settle the livestream question below.
- `event-risk-management`: promotes to first place once a venue contract is signed. Your file does not say whether one is.
- Later sponsor skills (pricing, prospectus, outreach): after the value proposition.
- `event-continuous-improvement`: after edition 3's debrief, with edition 2's debrief to read alongside it.

### Gaps
- **Reviewer sourcing.** Nothing in the collection covers finding and onboarding reviewers beyond committee sizing and the conflict brief. Use your community's past speakers and attendees.
- **Livestream ambiguity.** "Free livestream of the recordings" could mean a live stream or posted recordings. Your file says in-person, so the hybrid gate stays closed and I did not reopen the format decision. If you stream live, `event-production` owns the signal path. Please fix the wording in the file.
- **Ticketing system operation.** The collection does not cover it.

### Routines (dry-run only, nothing created)
```
Routine: work-back checkpoint
Trigger: 2 weeks before CFP close, then at each replanning point on the plan
Runs: event-planning-timeline
Output channel: dated section in event-context.md + message to organizers
Cost: one short session per firing
First fire: 2 weeks before CFP close (absolute date to confirm)
Stops: doors-open date

Routine: kickoff re-invocation
Trigger: monthly, plus the day the CFP closes
Runs: dev-event-kickoff
Output channel: 5-line state summary appended to event-context.md
Cost: near zero
First fire: CFP close date
Stops: doors-open date
```
A third routine, the ticket-pace check, applies only if a ticketing source exists. Your file has no on-sale date, so I left it out.

Both routines need your approval before I create anything.

### Proposed patch to `event-context.md`
I can't reach your repo, so I did not write it. Replace the relative dates with absolute ones and add the log line:
```
_Last updated: 2026-10-12_
## Dates
- Doors: <YYYY-MM-DD>, announced. CFP closes <YYYY-MM-DD>.
## Programme
- CFP open: 41 submissions at last count (<date>). Reviewers: none recruited. Grid not published.
## State
- Constraints: doors <date> fixed; standing, a few hours weekly; effort ceiling: a few hours weekly.
- Open: who reviews submissions; whether the livestream is live or posted recordings; sponsor status unrecorded.
## Session log
- 2026-10-12 - check-in after 10 weeks -> routed to event-talk-selection -> dates re-anchored.
```

I wrote nothing to memory, and nothing has been committed.