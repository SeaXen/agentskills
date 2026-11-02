# KernelKamp, editions 2–4: patterns and what to change for edition 5

I followed `event-continuous-improvement` and its three references. I have not run its full interview. The assumptions I made are at the bottom, with the questions whose answers would change this output.

## Bottom line

- ✅ **One pattern: check-in throughput.** It appears in 3 of 4 editions. This is the only theme that justifies a deliberate change.
- ⚠️ **One candidate: Room B projector.** It appears in 2 of 4 editions. Do only cheap, reversible things.
- ℹ️ **Catering is one occurrence, not three.** Three complaints in one edition is one intense edition, so file it and change nothing yet.

Every count below is out of the editions you hold records for. You said you have four debrief docs, so the denominator is 4. I assumed edition 1's doc has no check-in or projector entry. If that is wrong, the counts change.

## Filed entries and themes

| Theme | Editions | Count | Label |
|---|---|---|---|
| Check-in throughput | 2, 3, 4 | 3 of 4 | **Pattern** |
| Room B projector failure | 3, 4 | 2 of 4 | **Candidate** |
| Catering delivery and layout | 4 | 1 of 4 | Entry (filed, not counted as a trend) |

### Check-in throughput (pattern)

- **Why these three entries are one theme.** The skill clusters by what would have to change to prevent a failure, not by wording.
  - Ed. 2: badge printer jammed for an hour.
  - Ed. 3: queue hit 45 minutes, and two laptops couldn't reach ticketing on venue wifi.
  - Ed. 4: queue spilled into the street.
  - All three share one answer: check-in has a single path with no capacity margin and no offline fallback.
- **Condition, written without names.** The condition is a single check-in path, no offline fallback, a dependency on venue wifi (ed. 3), a hardware single point of failure (ed. 2), and a queue that outgrows the space (ed. 4).
- **Gate.** It is current because it recurred in the latest edition. It is reproducible because nothing about the design changed between editions. It generalizes because it is a capacity and fallback decision the team makes.
- **Gap in the record.** Ed. 4's entry says "chaos again" and gives no cause. I have not reconstructed it.
  - ⚠️ I can't say whether wifi, printing, volume or staffing drove the ed. 4 failure.
  - Fix this in week 1, using the check-in volunteers and desk staff. Ask what failed first and how long the queue got.
- **Independent support.** Tom Limoncelli describes "the third year in a row that badge pickup was a disaster" at an event of his own. That is one anecdote showing this failure recurs in practice. It is not a multi-edition log.

### Room B projector (candidate)

- **Gate.** It passes. It failed in the same room in two consecutive editions, which suggests the same unit or the same venue AV arrangement.
- **Status.** It is a candidate, so don't present it as a trend.
- **Action.** The skill allows acting on a candidate only if the fix is cheap, reversible, and worth doing even if the pattern is noise. A spare projector and a pre-event test meet all three tests.
- **Routing.** The venue AV supplier or rental vendor owns this. Route it to `event-vendor-sourcing` and file it on that vendor's own record this cycle, not in the general log. It still needs a rebook-or-not call and a brief change, such as a spare unit and an on-site test.
- **Questions to answer.**
  - Was it the same unit both times?
  - Was it the same failure mode?
  - Is it venue-supplied or rented?

### Catering (one occurrence)

- **Cold lunches, the vegan option running out, and the coffee station placement** all appear in ed. 4 only. Three entries in one edition count as one occurrence.
- **Conditions to file, not names.** File them as holding and serving temperature, dietary quantity planning, and station layout. The coffee station is a layout issue, not a food one.
- **No deliberate change this cycle.** Check the ed. 2 and ed. 3 docs for any catering notes. If there are none, this stays at 1 of 4.
- **Severity exception.** If any dietary shortfall touches allergens or medical needs, the occurrence bar drops. A safety or legal exposure doesn't wait for a second confirmation.
- **Cheap, reversible ask.** Put a vegan and dietary quantity floor in the next catering order. That is vendor-brief work, so file it on the caterer's record in `event-vendor-sourcing`. It is not a theme change.
- **Individual complaints are not a recurrence.** If lunch and the vegan option fail again in ed. 5, that becomes a 2-of-5 candidate.

## What to change: one deliberate change

The skill's rule is one deliberate change per edition, so catering and the projector don't get one. A bundle can't be attributed at the closure pass. The change record below is drafted for you to confirm.

```
CR-1  Resilient check-in: second station plus an offline attendee list
Evidence:   check-in throughput, pattern, 3 of 4 editions (ed. 2, 3, 4)
Change:     add a second check-in station and run the morning
            with a printed attendee list so a venue-wifi failure
            doesn't stop the line
Because:    the condition is a single path with no fallback and
            no capacity margin, not a staffing failure
Check:      peak wait at the desk, observed at the door by timing
            sample arrivals at fixed intervals (not surveyed)
Threshold:  peak wait under 10 minutes and nobody queued outside
            the building. The 10 minutes is a proposal; set your own
Routed to:  event-planning-timeline, as a task on the edition 5 plan
Outcome:    <filled at the closure pass, after ed. 5>
```

- ⚠️ **Provisional on the ed. 4 cause.** This change targets capacity plus fallback, which fits ed. 2 and ed. 3 well. It fits ed. 4 only if the week-1 check confirms capacity or wifi. If ed. 4 was a printing or staffing problem, rewrite the change.
- **The Check line.** It is the part teams skip, and it turns a preference into a deliberate change. Fix the threshold before you ship the change. A direction alone ("shorter") invites a motivated reading next year.
- **Planning deadline.** Planning starts in six weeks, so the task must be on the work-back plan before that kickoff.

## Routing hand-offs

I hand over evidence and stop there. Each sibling owns its own decision.

| Sibling | What I hand over |
|---|---|
| `event-planning-timeline` | CR-1 as a real task: the change, the edition it lands in, its owner, and the decision date inside the six weeks |
| `event-vendor-sourcing` | Projector: 2 of 4, same room, ask about a spare and a pre-event test. Catering: ed. 4 holding temperature, vegan quantity floor and coffee layout. File each on that vendor's record |
| `event-growth-strategy` | Evidence only: at about 350 attendees, single-path check-in overflowed into the street in ed. 4. That may mark a ceiling for the current check-in design. No recommendation about size |
| `event-market-fit` | Nothing yet. If your ed. 4 return or sell-through numbers dropped, they weigh whether check-in plausibly contributed. I have not established a causal link, and I have no demand numbers |
| `event-team-structure` | Nothing yet. Route it if the week-1 check shows nobody owned check-in fallback or setup |

## Persistence and audit

- **Log rung: structured entry record.**
  - With four editions of records, the skill promotes it from the default (appended document) to first choice.
  - Use the field-block entry in one shared document. It stays cheap, and recurrence becomes countable instead of remembered.
  - If you have very few between-edition hours, fall back to the appended document, the default.
- **Audit cadence: kickoff pass.** Run it before the edition 5 planning kickoff.
  - This is the first log, so the pass is short. Classify every entry as Keep, Update, Consolidate, Replace or Delete.
  - After edition 5, add the cheap closure pass. Reopen CR-1 and add two columns: **did this actually improve, yes or no**, and **why**.
- **Pass threshold.** Every entry classified after the audit, and every live entry carrying a theme and an occurrence count.
- **Name the opener.** Name one person who opens the log before planning starts, and the day they do it. A log nobody re-reads is the most likely failure.

## Next steps, in order

1. **This week:** get the ed. 4 check-in cause from desk staff and volunteers. Fix the unanswered questions on the projector (same unit? venue or rental?).
2. **This week:** check the ed. 1–3 docs for catering notes and any ed. 1 check-in or projector entry.
3. **Before kickoff:** write the three themes into the log with the field-block entry. De-personalise first, with conditions and no names. Never delete a resolved entry. Close it with a reason.
4. **Before kickoff:** confirm CR-1 and its threshold. Send CR-1 to `event-planning-timeline`, and the projector and catering notes to `event-vendor-sourcing`.
5. **At kickoff:** the named person opens the log.
6. **After edition 5:** run the closure pass on CR-1.

## What is published practice and what is this skill's own judgment

- **Published practice:** MLH's `keeping-records.md` backs the habit of capturing feedback during the event and handing it to next year's team. Fraser and Mancl (2023) back running a post-event retrospective across a conference series, including trends year over year.
  - Neither follows one finding from edition 1 to edition 3 or 4.
  - Everything past the first handover is this skill's construction.
- **This skill's own judgment:**
  - The filing gate, borrowed from software practice (`printing-press-retro`).
  - The two-occurrence candidate and three-occurrence pattern bars.
  - The log format and change record.
  - The audit classification, borrowed from `ce-compound-refresh`.
  - The menus and their orderings.
- **Not established organizer practice:** the 10-minute threshold in CR-1 is a placeholder I proposed.

## Assumptions and open questions

I assumed a compounding event with several editions left, no full organizer rotation, and the same venue for ed. 3 and 4 (the projector entries suggest it). Each answer below changes the output:

1. Is ed. 1 silent on check-in and the projector? A yes keeps check-in at 3 of 4. A no changes the denominator or the count.
2. How much of the team has turned over, and is a handover planned this cycle? A big turnover promotes the written trend review and the standing audit owner.
3. How many hours do you have between editions? A low ceiling keeps the appended document.
4. Who is the named person who opens the log before planning?
5. Do ed. 2–4 entries carry an owner and date, and did any past edition change something deliberately because of a logged finding?