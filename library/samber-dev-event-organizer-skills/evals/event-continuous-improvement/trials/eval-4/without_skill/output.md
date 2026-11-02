# PolyglotDays learning log cleanup, edition 6 prep

## Short answer

⚠️ Don't delete everything resolved or outdated. The log is institutional memory, and "resolved" often means the fix still has to be repeated each edition. Make the log short by changing what people see by default. Only delete exact duplicates.

41 entries is not long. The real problem is that nothing tells you which entries are open. Fix that with a status field and an archive section.

## Do first (5 min)

1. **Copy the log** to a dated backup before you edit anything.
2. Keep entry numbers stable and don't renumber. Other documents probably cite "entry 31". A merged entry keeps one line saying `merged into #N`.

## Add four fields to every entry (once, then reuse)

| Field | Values |
|---|---|
| Status | Open, Mitigated, Resolved, Superseded, Retired |
| Scope | General, or venue-specific (name the venue) |
| Editions seen | List each edition once |
| Owner | One person or workstream |

Default view: Open and Mitigated only. Everything else goes in an Archive section below it.

## Your specific entries

| Entry | Action | Why |
|---|---|---|
| 7 and 23 | **Delete 23**, keep 7 | Exact duplicates are the only real deletion. First check that 23 has no different edition tag or date. If it does, it may be a real recurrence that was logged twice, so merge the metadata into 7. Also check that nothing links to 23. |
| 12 (Harbour Hall loading dock, 17:00) | Mark Retired, scope = Harbour Hall, move to Archive | The constraint is gone, but the lesson isn't. Add one general line to the venue site-visit checklist: "Get hard cutoffs for load-in and load-out at every new venue." Also check that the new venue has no similar constraint. |
| 15, 31 and 18 | **Merge into one record** (see below) | You listed 18 separately, but it is the same check-in queue issue as 31. It is probably the same problem as 15 too. |
| 9 and 33 | Fold 9 into 33, mark 9 Superseded, with a redirect | Keep a "Ruled out: the app causes missed sessions" note inside 33. It stops someone from proposing that theory again in edition 7. Delete 9 only if 33 already says this. |

### The merged check-in record (15 + 31 + 18)

1. Keep the earliest ID (15) as the survivor. Give 31 and 18 redirect stubs.
2. **Editions seen: 2, 3, 4, plus 5 if the queue was measured then.** 15 gives you 2 and 4. 31 gives you 3 and 4. Edition 4 appears in both, so count it once.
3. Status: **Mitigated, not resolved.** The queue dropped from about 60 to about 25 minutes. 25 minutes is still a long wait. Don't archive this one.
4. Record **what the fix actually was**. That is the most valuable thing in the three entries combined.
5. Set an explicit edition 6 target, such as "under 10 minutes". Say how the wait is measured, because "about 25" is an estimate.
6. Assign one owner. Volunteers and front-of-house each logged half of this, which probably helped it survive four editions.

⚠️ You said you were "pretty sure" these are the same problem. Check before you merge. Look at the edition 4 notes and the fix described in 18.
- If the fix was staffing, the merge is clearly right.
- If the fix was process (pre-registration, scanning, badge printing), then "desk understaffed" and "queue backed up" may be separate causes of one symptom.
- If you can't tell, merge into one record and list the causes as sub-bullets.

## Why not delete resolved or outdated entries

- **Resolved entries hold the fix.** Move the fix into a "keep doing" checklist, then archive the entry.
- **Resolved issues regress.** Venues, vendors, and volunteers change between editions.
- **Superseded theories protect you.** Entry 9 was a wrong diagnosis. Without a record, the app theory comes back.
- **Venue-specific entries still teach general lessons.** Entry 12 is one example.

## Expected result

41 − 1 (dup) − 2 (merge of 15, 31, 18) − 1 (9 folded into 33) = **37 entries**. Entry 12 stays but moves to the archive. I can't tell you the final Open count, because you haven't shown me the other 33 entries.

## Remaining work (about 1 hour)

1. Give each of the other 33 entries a status, about 2 minutes each. Ask one question per entry: "Would edition 6 planners be worse off without this?"
2. Pull every Resolved entry's fix into a short "keep doing" checklist.
3. Review the Open and Mitigated list in the first planning meeting, with an owner on every line.

The 8 entries above take about 20 minutes. Do those first.

❓ **One question:** was entry 18's partial fix applied in edition 5 or edition 4? That decides whether 25 minutes is the edition 5 baseline or still untested.