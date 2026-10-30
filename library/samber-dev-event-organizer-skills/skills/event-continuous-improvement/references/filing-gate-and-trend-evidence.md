# Filing gate, theme grouping, and the evidence bar for a trend

## The filing gate

**Borrowed** from `mvanhorn/cli-printing-press`'s `printing-press-retro`, which files an issue against its generator only when a defect is _"current, reproducible, generalizing"_, and explicitly refuses to file for _"manual iteration on one CLI"_, which it calls expected work rather than a finding. The discipline transfers; its per-run cadence and its issue-tracker mechanics do not.

An entry from a debrief log becomes a **candidate** only when all three hold:

1. **Current** - the condition that produced it still exists. A failure caused by a venue the event has left is history, not a candidate. File it as closed with the reason, so nobody re-files it next year.
2. **Reproducible in this event's own conditions** - it would happen again if the edition ran again unchanged. Ask what would have to be true for it not to recur. If the answer is "nothing, we got lucky", it is reproducible.
3. **Generalizing** - it points at something the team decides or builds, not at one person's one-off improvisation. A volunteer covering a gap by staying late is expected work; the gap that required it is the finding.

Everything failing the gate is **filed as expected work**: kept in the record with a one-line reason, never counted toward a recurrence. Deleting it instead guarantees someone re-files it in three editions and calls it new.

## De-personalisation, before anything is persisted

`samber/dev-event-organizer-skills@event-debrief` runs its session under a blameless frame stated out loud. That frame has to survive into a document that outlives everyone in the room, and it does not survive by itself - a sentence that read as candid feedback in a live session reads as a filed accusation when a new organizer opens it four years later.

Rewrite every entry so it describes a condition, not a person, before it enters the persisted log. Both pairs below are illustrative:

- Not "Sam forgot to order the second badge printer" → "one printer, no backup, and no one owned reordering after the first edition".
- Not "the volunteer lead was unreachable on the day" → "the volunteer rota had a single point of contact with no documented fallback".

The second form is also the only form that can be counted. "Sam forgot" happens once by definition; "no documented fallback" is a theme that recurs and can be routed to `samber/dev-event-organizer-skills@event-team-structure` with an occurrence count behind it.

## Worked filings

The check-in and badge theme running through the filings below is not invented from nothing. Tom Limoncelli, writing from three decades of organizing and attending conferences, names the identical failure at a real event of his own: "the fact that this was the third year in a row that badge pickup was a disaster." That is one named-organizer anecdote confirming the theme recurs unaddressed across editions in practice, not a structured multi-edition log. The specific numbers, occurrence counts and dispositions below remain this skill's own illustration.

- **Files as a candidate.** Edition 3's log: _"Check-in queue hit ~40 minutes at peak; two of four laptops couldn't reach the ticketing tool on venue wifi; we moved to paper lists at 09:20."_ Current (same venue, same tooling), reproducible (nothing changed about the network or the laptop count), generalizing (it is a capacity and fallback decision the team makes). Theme: check-in throughput. This is one occurrence, not a trend.
- **Files as expected work.** Edition 3's log: _"Speaker's laptop wouldn't output to the projector; swapped to the backup machine, lost four minutes."_ Reproducible in the sense that some laptop will always misbehave, but the backup machine is the treatment and it worked. Nothing about the event's design produced it. File with the reason; do not count it.
- **Files as closed, not deleted.** Edition 2's log: _"Loading dock closed at 17:00, teardown ran past it and we paid an overtime fee."_ The event moved venues after edition 2. Not current. Close it with "venue changed after ed. 2" so the next audit does not resurrect it as an unexplained old entry.
- **The tempting mis-filing.** Edition 3's log: _"Only 11 of last year's 40 attendees came back."_ This passes the gate and is still not yours - it is a demand signal owned by `samber/dev-event-organizer-skills@event-market-fit`. Route it, note the routing in the record, and keep going. What _is_ yours is any operational entry that plausibly explains it, such as the check-in theme above, and even then you hand over the observation rather than the conclusion.

## Theme grouping

Group before you count, because the same underlying failure is described differently by each organizer and in each edition. Counting raw entries under-detects exactly the recurring problems the log exists to surface.

Method:

1. Read every candidate across all editions in one sitting. Grouping across editions requires seeing them together; a per-edition pass reproduces the debrief's own single-edition view.
2. Cluster by **what would have to change to prevent it**, not by wording and not by the workstream that reported it. "Badge printer jammed", "queue out the door", and "laptops couldn't reach the ticketing tool" share one answer: check-in capacity and its fallbacks.
3. Name each theme in the team's own vocabulary, and keep the name stable across editions. A renamed theme resets its occurrence count and hides the trend.
4. Count the theme's occurrences as the number of **editions** it appears in, never the number of entries. Three entries in one edition is one occurrence - an intense edition, not a pattern.
5. Keep a theme list short enough to hold in a page. Twenty themes for a four-edition event means the clustering ran on wording.

## The evidence bar

A convention this skill sets rather than an industry standard, so present it to the team as something they adopt. The two-versus-three split tracks a much older cross-domain heuristic for the same judgment: "the first time is happenstance, the second time is coincidence, the third time is enemy action," genericized into troubleshooting and quality-management practice well beyond events. The number is therefore not arbitrary, even though no organizer guide sets it for this domain specifically.

- **One occurrence** - an entry. It stays filed. It changes nothing on its own.
- **Two occurrences** - a **candidate**. Say the word out loud every time. Two points draw a line through anything, and a candidate presented as a trend is how a coincidence acquires a budget. Act on a candidate only when the fix is cheap, reversible, and worth doing even if the pattern turns out to be noise.
- **Three occurrences** - a **pattern**. Strong enough to justify a deliberate change and to carry into a routing hand-off as evidence.
- **Any occurrence count, when the cost of recurrence is severe** - the bar drops, and say why in the entry. A safety, code-of-conduct, insurance or legal exposure does not get two more editions of confirmation. This is the one deliberate exception, and it should be rare enough to notice.

Always state the denominator with the count. "Three of four editions" and "three of eleven" are different claims, and only the first is a pattern.
