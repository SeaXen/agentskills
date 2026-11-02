# Cleaning up the PolyglotDays learning log (41 entries, 5 editions)

**Don't delete everything resolved or outdated.** The skill reserves Delete for entries that were never findings, such as copy-paste duplicates. Resolved or outdated findings get closed with a reason. A deleted finding gets re-filed as "new" in two editions by someone who wasn't there, which is what the log exists to prevent. You can still get a short log. Keep closed entries in a separate section so the live part stays short enough to re-read.

I haven't seen the log. Only the 8 entries you described are classified below, and the other ~33 need the same pass.

## Classification of the entries you named

Each entry gets exactly one of Keep, Update, Consolidate, Replace or Delete.

| Entry | Verdict | Action |
|---|---|---|
| 7 and 23 | **Delete 23** (keep 7) | A verbatim paste is a duplicate, not a finding. Keep 7 because it holds the earliest date. Don't count 23 as a second occurrence. |
| 12 | **Update**, status closed | Harbour Hall is no longer the venue, so the entry fails the "current" test. Close it with the reason "venue changed after ed. 3". Do not delete it. |
| 15 + 31 (+ 18) | **Consolidate** | Merge into one theme, "check-in throughput". Recount by edition (details below). |
| 18 | **Update** (or merged into the theme above) | The condition changed: the queue went from about 60 to about 25 minutes. The theme stays live with a smaller condition line. |
| 9 → 33 | **Replace** | Point 9 at 33 and close 9. Keep 9 visible as a record of what was tried and misdiagnosed. |

### Entries 7 and 23
- **Check the edition dates first.** If 23 was added in a later edition, the finding may have really recurred and been logged by pasting. In that case it is a Consolidate, not a Delete. Ask whoever added it.
- **Leave a one-line pointer** such as "23 removed, duplicate of 7". That way any document citing #23 doesn't break. This is my suggestion, not part of the skill.

### Entry 12
- **Re-check the new venue.** The specific cause is gone, but ask whether the new venue has its own hard teardown cutoff. If it does, that is a new live entry.
- **The skill has no named verdict for "closed".** I classed it as Update, with status changed to closed. That is my reading.

### Entries 15, 31 and 18
- **Check that they share a fix.** Cluster by what would have to change to prevent the problem, not by wording or workstream. "Desk understaffed" and "queue backed up" are one theme only if the same fix addresses both. Capacity and fallback is one fix and rota size is another, so confirm which it is.
- **Recount by editions, not entries.** Entry 15 appears in editions 2 and 4. Entry 31 appears in editions 3 and 4. The union is editions 2, 3 and 4. Edition 4 counts once, so adding the two counts to get 4 would be double-counting.
  - Separately, each is a **candidate** (2 occurrences). Merged, it is a **pattern** at 3 of 5 editions, if records exist for all five.
  - Keep the earliest first-seen edition, which is 2.
- **Entry 18 is probably the same theme.** If it also covers edition 5, the count becomes 4 of 5. If 18 and 31 describe the same event, count it once.
- **Partial fix, not resolved.** The 60 → 25 minute drop is a closure-pass outcome: did it improve? Yes, partially. The theme stays live. Don't move it to "Improvements achieved".
- **The two-edition rule.** If the theme sat in "Persistent problems" for two consecutive editions, it is the first item the kickoff pass opens with.

### Entries 9 and 33
- **Don't leave both live.** A reader will find whichever one they hit first.
- **Check whether 33 already counts the editions 9 recorded.** The underlying problem (people missing sessions) is the same. This is my judgment call. If you merge the histories, recount by edition.
- **The printed schedule being wrong is a process or vendor fault.**
  - If it is a printer or supplier fault, route it to `event-vendor-sourcing` and file it on that vendor's record.
  - If it is a missing proofing step, it becomes a task for `event-planning-timeline`.
- **Keep the entry de-personalised.** Describe conditions, not people. This applies to all 41 entries.

## Proposed deliberate change for the check-in theme

This is a draft. It needs your answers to the questions below before it can be filled in. The skill allows one deliberate change per edition, so nothing else gets bundled with it.

```
CR-n  <change to check-in capacity or fallback — which one depends on the cause>
Evidence:   check-in throughput, pattern, 3 of 5 editions (ed. 2, 3, 4)
Change:     <what exactly>
Because:    <capacity/fallback vs staffing — decide from the 15/31/18 text>
Check:      peak queue length at the door in ed. 6, observed not surveyed,
            at or below <number you set>
Outcome:    <filled at closure pass after ed. 6>
```

Pick the target yourself. The 30-minute figure in the skill is only an example. Write the Check line before the change ships.

## Routing hand-offs

- **`event-planning-timeline`:** the change as a task on the ed. 6 plan.
- **`event-team-structure`:** only if the volunteer-rota size is the structural cause. Send the recurrence count as evidence.
- **`event-growth-strategy`:** only if the queue breaks past a specific attendee count. Hand over the ceiling as evidence and no recommendation.
- **`event-vendor-sourcing`:** the printed-schedule issue, if a supplier caused it.

## Settings for the pass

Planning opens next month, so run the kickoff pass now.

- **Persistence:** you hold four or more editions of records, so use the structured entry record. Give each live entry these fields: theme, first-seen edition, occurrences as "x of y", status, condition, disposition, owner, audit result.
- **Audit cadence:** run a kickoff pass now, then a closure pass after edition 6 ships. At the closure pass, reopen each change record and add two columns: did it improve (yes or no), and why.
- **Pass threshold:** the only target the skill sets is zero unclassified entries after the pass. Each live entry must also carry a theme and an occurrence count.
- **Time:** roughly 1.5 hours for 41 entries, done in one sitting. A half-audited log is worse than an unaudited one.
- **Make the log short by splitting it.** Keep a live section and a closed section. The theme list should fit on one page. Twenty or more themes for five editions usually means the clustering followed wording.

## What I need from you

1. Paste the log, or at least the dates and text of entries 7, 23, 15, 31, 18, 9 and 33, so I can finish all 41.
2. Do written records exist for all five editions? That sets the denominator on every count.
3. In which edition did the partial check-in fix land, and what was it?
4. Who opens the log before planning starts? Name a person, not "the team".
5. How much of the team is new for edition 6, and how many hours do you have between editions? These two answers could change the persistence and audit choices above.

## Sourcing

None of the formats, counts, menus or thresholds above are published organizer practice. The skill built them itself. Two things are borrowed from software practice: the filing gate and the Keep/Update/Consolidate/Replace/Delete classification. The "twice is a coincidence, three times is a pattern" rule is an older general heuristic, not an event-industry standard.