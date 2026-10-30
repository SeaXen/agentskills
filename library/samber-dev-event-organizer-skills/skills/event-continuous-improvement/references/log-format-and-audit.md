# Log format, the audit classification, and the handover packets

## What the log has to be, and why an organizing guide is not a template

DevOpsDays' `organizing.md` is the clearest inspectable case of institutional memory surviving organizer turnover: 58 commits, 20+ named contributors, 2015-11-22 to 2026-06-02, accreting through small targeted edits rather than periodic rewrites. It proves that **a persisted, collectively-edited document survives a decade of turnover without a standing entity enforcing it**.

It is not a template for this log. `organizing.md` is timeless how-to guidance edited in place - no dated entries, no per-edition structure, no trend annotations. Borrow the survival property (one shared document, small edits, many hands, no scheduled rewrite ritual) and build the format yourself.

MLH's `Organizer-Resources/keeping-records.md` covers the log's raw material: keep "a document for your team to dump feedback and challenges during the event and event planning process, so you don't forget them", then organise it afterwards and hand it to next year's team. That gives you the capture habit and the single handover. The dated entry, the occurrence count and the audit classification below are conventions you adopt rather than published practice.

## What one organizer guide covers, and where it stops

MLH's guide supplies:

- A cadence: "Schedule a 1-hour event reflection with your team a few days after the event".
- An audience: "Review this document with next year's organizing team".
- Two artifacts: a shared Drive folder, plus the running document above.
- Three forward-looking reflection questions.
- A worked example of a finding crossing an edition: "if you went over budget because snacks for hackers cost more than you expected then you should note that for next year's team to help them avoid making the same mistake."

DevOpsDays' `organizing.md` carries nothing but one code-of-conduct line about "insights for future events". The guidance stops at that first handover. MLH describes one conversation between two consecutive teams, not a persisted trend, and nothing there follows a finding from edition one to edition three or four. Everything past that handover in this skill is its own construction, not established organizer practice.

## Entry shape

Whatever the persistence rung, an entry has to answer four questions a stranger will ask: what is this, how often, is it still live, and who has it. At the appended-document rung these are a sentence each under a dated heading; at the structured-record rung they are fields.

The block below is this skill's own construction. Every value in it is illustrative, drawn from no real event.

```
Theme:        check-in throughput
First seen:   edition 2
Occurrences:  3 of 4 editions (ed. 2, 3, 4)
Status:       pattern
Condition:    single check-in station, no offline fallback, venue wifi unreliable
Disposition:  deliberate change proposed for ed. 5 - see change record CR-2
Routed to:    samber/dev-event-organizer-skills@event-planning-timeline (task), samber/dev-event-organizer-skills@event-growth-strategy (evidence only)
Owner:        <named person>
Audit:        Keep (ed. 5 kickoff pass)
```

Two rules that matter more than the fields:

- **Never a name in the condition line.** Conditions, not people. The blameless frame has to survive into a document read by people who never met the person.
- **Never delete a resolved entry.** Close it with the reason. A deleted entry is re-filed as a new finding three editions later by someone who was not there, and the log's whole purpose is to prevent exactly that.

## The deliberate-change record

One record per change, and one change at a time per edition. Bundling makes the next closure pass unable to attribute any outcome. The record below is this skill's own construction, filled with illustrative values.

```
CR-2  Second check-in station with an offline attendee list
Evidence:   check-in throughput, pattern, 3 of 4 editions
Change:     add a second station and print the attendee list the morning of
Because:    the condition is capacity plus fallback, not staffing
Check:      peak queue length at ed. 5, observed at the door, not surveyed
Routed to:  samber/dev-event-organizer-skills@event-planning-timeline as a task on the work-back plan
Outcome:    <filled at the closure pass, after ed. 5>
```

The **Check** line is the part teams skip, and it is what separates a deliberate change from a preference. Write it before the change ships, in terms someone can observe rather than infer.

Give it a number wherever the underlying quantity is genuinely measurable at this event's own scale: a stated threshold on peak queue length, not just "shorter". Direction alone invites a motivated reading next edition. When more changes are proposed than the team can carry, let a rough urgency call, need-now against nice-to-have, decide which ones earn that stricter numbered form.

The objective-plus-measurable-check shape is loosely borrowed from goal-setting practice. Do not let it grow into a full objectives framework, which assumes a quarterly cadence an annual event does not have.

## An alternative layout: two tables

The field-block entry above and the two-table layout below hold the same information; pick whichever the team will actually keep updating. Split the log into **Improvements achieved** (theme, first-seen edition, most recent edition, status) and **Persistent problems** (theme, first-seen edition, most recent edition, action required). Both tables are this skill's own construction, and every figure in them is illustrative:

```
Improvements achieved
| Theme                | Ed. 2 state        | Ed. 4 state       | Status      |
| --------------------- | ------------------- | ------------------ | ----------- |
| Check-in throughput   | 90-minute queue     | Under 30 minutes   | Resolved    |

Persistent problems
| Theme                 | Ed. 2 state         | Ed. 4 state        | Action required        |
| --------------------- | ------------------- | ------------------ | ---------------------- |
| Volunteer no-shows    | 3 of 12 no-show     | 4 of 14 no-show    | See CR-5, escalated    |
```

A theme still sitting in the persistent table across two consecutive editions escalates: it moves from an ordinary entry on next cycle's list to the one the kickoff pass opens with, ahead of anything new. That two-edition bar is self-set, not a measured threshold.

Two tables read faster than a field block when the audience is the whole team rather than one person maintaining the record. The cost is the per-entry detail the field-block form carries natively: condition, routing, owner. Keep those fields in a linked per-theme note if the team needs both.

## The audit classification

**Borrowed** from `everyinc/compound-engineering-plugin`'s `ce-compound-refresh`, which periodically audits a persisted learnings store against ground truth and classifies every entry into exactly one of five outcomes, so nothing sits forever unexamined.

One honest amendment: `ce-compound-refresh` checks its store against a codebase, which can be inspected at any moment. Your ground truth is **next edition's own outcome**, which only exists after the fact. The audit here is therefore retrospective and periodic, never continuous - that is a real limitation of the domain, not a shortcut.

Every entry gets exactly one:

- **Keep** - still true, still live, count unchanged. The common outcome, and it still has to be stated rather than assumed.
- **Update** - still live but its condition has changed. Rewrite the condition line and keep the occurrence history. Most often after a partial fix: the queue halved, so the theme survives with a smaller condition.
- **Consolidate** - two or more entries turn out to be one theme seen from different workstreams. Merge them, keep the **earliest** first-seen edition, and recount occurrences by edition rather than adding the two counts together. Double-counting a merge is the fastest way to manufacture a pattern.
- **Replace** - the finding was superseded by a better-understood one. Point the old entry at the new one and close it; do not leave both live, because a reader will find whichever one they hit first.
- **Delete** - reserved for entries that were never findings: duplicates from a copy-paste, or something misfiled from another event entirely. A real finding that is no longer live gets closed, not deleted.

Run the pass entry by entry and finish it in one sitting. A half-audited log is worse than an unaudited one, because part of it now carries a fresh timestamp that implies the rest was checked.

## Handover packets

Say what you are handing over, hand over evidence rather than conclusions, and stop there. Each recipient owns the decision inside its own scope.

- **To `samber/dev-event-organizer-skills@event-planning-timeline`** - each deliberate change as a task: the change, the edition it lands in, its owner, and the point in the work-back plan by which the decision has to be made. Not the evidence trail; it does not need it to schedule.
- **To `samber/dev-event-organizer-skills@event-market-fit`** - any theme shaped like demand rather than operations, with its occurrence count and the editions involved. Frame it as an observation feeding their read. In the illustrative form _"attendee return fell in both editions where check-in exceeded 30 minutes"_, that is a signal for them to weigh, not a causal claim you have established.
- **To `samber/dev-event-organizer-skills@event-growth-strategy`** - any theme that names a ceiling: a number of attendees, tracks, rooms or volunteers past which something reliably breaks. Hand over the ceiling and the evidence; never the recommendation about size.
- **To `samber/dev-event-organizer-skills@event-vendor-sourcing`** - a rebook-or-not verdict on one named supplier, plus what to change in the brief or the ordered quantity if the verdict is yes. File it on that vendor's own record the same edition it happens, as a first-class post-event task rather than an aside someone half-remembers when sourcing reopens.
- **To `samber/dev-event-organizer-skills@event-team-structure`** - any structural theme that recurs: a role only one person can do, a workload nobody sized, a handover that failed the same way twice. The recurrence count is the whole point of the hand-off: a single debrief can report exhaustion, but only a cross-edition count shows it is the structure rather than the year. Say explicitly that the persisted log is itself one of the bus-factor mitigations that skill is choosing among. It is the artifact that carries what the team learned across the people who leave.
- **To an incoming team, on a full rotation** - the theme list with occurrence counts, every live entry, the deliberate-change records with their outcomes, and an explicit list of what was tried and did not work. That last list is the part nobody writes and every incoming team needs, because a failed fix is invisible in a log that only records findings.
