# Session agenda, reconciliations, handover

How the session runs, the four checks against documents that already exist, and what leaves the room.

## Session agenda

Timings are for the default single-session rung. MLH schedules "a 1-hour event reflection with your team a few days after the event" and opens it with three questions about attendee feedback, planning challenges, and useful resources.

The segment breakdown below sits inside that hour. Scale these timings to your team's pace; they are a pacing guide, not measured intervals.

| Segment          | Roughly | What happens                                                                         |
| ---------------- | ------- | ------------------------------------------------------------------------------------ |
| Frame            | 5 min   | The blameless statement, out loud. Who is here, what leaves the room, what does not. |
| Timeline         | 20 min  | Chronological reconstruction. No judgment yet.                                       |
| What went well   | 15 min  | First, and not as a formality.                                                       |
| What went poorly | 25 min  | Observations, not verdicts.                                                          |
| Reconciliations  | 20 min  | The four checks below, against the documents in the room.                            |
| Team health      | 10 min  | Explicitly on the agenda, so it is not left to whoever is brave.                     |
| Owners and dates | 15 min  | Every entry gets a name and a date, or an explicit no-action.                        |
| Publication      | 10 min  | Decided here, by the team, not taken away as homework.                               |

## The blameless opening, said out loud

Adapt the wording; keep all four moves. Read it rather than paraphrasing it - the point is that everyone hears the same sentence at the same time.

> We are reconstructing what happened, not deciding who is at fault. The question this session asks is what conditions allowed something, never who caused it. Everything that went wrong here went wrong inside a system we all built, mostly at the end of a long day. Nothing said in this room becomes a performance judgment, and nothing leaves it except the findings we agree to write down.

Two additions by team type:

- **Volunteer team** - add that nobody is here on work time and that saying "I could not keep up with this" is a finding about the workload, not about them.
- **Staffed or mixed team** - whoever holds the reporting line says the frame themselves; coming from anyone else it does not bind, and a manager silently present is read as an evaluator by default.

Enforce it the first time it slips, immediately and lightly: restate the observation without the name. One uncorrected "you dropped this" costs the rest of the session.

## Timeline reconstruction

Walking the sequence before analysing it is what stops the loudest memory from becoming the record.

1. Two granularities, in order: the planning cycle at whatever resolution matters (usually milestone by milestone), then the event days hour by hour.
2. Build it from artifacts first - the run of show, the comms channel history, the ticketing timeline, photo timestamps - and from memory second. Memory fills gaps; artifacts set the spine.
3. Mark anything the room disagrees on as disputed rather than resolving it. A disputed step is itself a finding: nobody knew what was happening at that moment.
4. Mark the gaps too. "Nobody in this room knows what happened at the sponsor tables between 14:00 and 16:00" tells you who was missing from the debrief.
5. Only once the sequence stands does anyone say whether a step was good or bad.

## The four reconciliations

Each is a check against a document that already exists, owned by a sibling skill. Each produces a handback, not a rewrite. If a document does not exist, say so and skip the check rather than reconstructing it from memory.

**Against the risk register.** Three questions:

- which scored risks actually materialised
- whether each treatment held
- what fired that nobody had scored

Hand back a list in three buckets: fired-and-treatment-held, fired-and-treatment-failed, fired-and-unscored. The third bucket is the valuable one - it is a new risk category, not a fix. Re-scoring the register is `samber/dev-event-organizer-skills@event-risk-management`'s job, not yours.

**Against the planned budget.** Line-by-line actual versus planned, largest absolute variance first. For each material variance, one sentence on cause:

- a price move
- a volume miss
- an unplanned line
- an estimate that was always wrong

Hand back the variance table with those causes. Do not propose next edition's numbers.

**Against the run of show.** Where did the real day diverge from the written one:

- segments that ran long
- a role that was never actually staffed
- an escalation that went to the wrong person
- a transition that ate a talk's time

Hand back the divergences as observations. The cue sheet's revision belongs to `samber/dev-event-organizer-skills@event-run-of-show`.

**Against the goals the team set.** Whatever was written down before the event:

- attendance
- financial outcome
- satisfaction
- incident count
- a diversity or first-time-speaker target

Hit, missed, or unmeasurable - and be willing to write unmeasurable, since a goal nobody instrumented is itself a finding. If no goals were written down, reconstruct what they would have been and label the whole section reconstructed, not measured. Keep this strictly internal: it answers whether this edition hit its own targets, never whether the event still has a market.

## Why surface team health at finding severity, not shutdown severity

Two of this field's best-known events published this kind of self-assessment only at shutdown.

- **JSConf EU, 2019 closing statement** - itemised what became unmanageable: "over 1600 attendees in total, 60+ flights and 100+ hotel stays to book, 120 scholarships... the cost of all this exceeds one million Euro."
- **!!Con, co-founder statement, June 2024** - "after !!Con 2022, the team was burned out and needed to take a year off."

Both examples appeared at shutdown. A debrief is where the same assessment should surface years earlier, while the finding is still small enough to route rather than absorb.

## Handover packet

One dated document leaves the debrief, plus four routed items. Name each recipient explicitly so nothing sits unclaimed.

- **The dated lessons-learned log** - every entry in three parts, each carrying an owner and a date or an explicit no-action, each tagged with its category. Goes to `samber/dev-event-organizer-skills@event-continuous-improvement`, which owns every trend claim across editions.
- **The three risk buckets** → `samber/dev-event-organizer-skills@event-risk-management`.
- **The variance table** → `samber/dev-event-organizer-skills@event-budget`.
- **The run-of-show divergences** → `samber/dev-event-organizer-skills@event-run-of-show`.
- **The team-health findings, phrased structurally** → `samber/dev-event-organizer-skills@event-team-structure`. "One person held three roles with no backup", never "they took on too much".
- **Any signal the demand verdict should weigh** - a sponsor renewal below goal, a return rate below goal - → `samber/dev-event-organizer-skills@event-market-fit`, as a signal and not as a conclusion.
- **Open action items**, once next edition's plan opens → `samber/dev-event-organizer-skills@event-planning-timeline`, as real tasks with slots rather than log lines.

If your harness has persistent memory, store:

- the log
- the goals it was measured against
- the open items with owners and dates
- the routing list

Next edition's debrief then opens on last edition's unfinished items, which is the one input nobody can reconstruct a year later.
