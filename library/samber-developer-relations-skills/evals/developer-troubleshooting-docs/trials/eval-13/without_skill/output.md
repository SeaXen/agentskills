Reject 30-entry plan as written. Fix 3 broken things first, size new writing off real demand data after.

## Real problem, not what writer diagnosed

- 22 entries, 3 months, ticket volume flat (-4%, noise) → docs had near-zero measurable effect on tickets.
- 190 zero-result searches for strings pages already cover → search broken, not content missing. If search can't surface existing pages, new pages fail same way.
- 6 known-issues entries describe bugs fixed in 5.0 (June) → stale 3+ months, actively misleads users into filing tickets on closed bugs.
- Every entry ends with dead link (#support-legacy, archived July) → every reader who needs escalation hits dead end.
- Writing 30 more entries into this pipeline repeats same failure at 1.4x volume. Fix pipes before pouring more water.

## Week 1 — fix now (~2-3 days)

1. Find/replace "#support-legacy" across all entries with live escalation path (ticket link or current channel).
2. Mark 6 stale known-issues entries "Resolved in 5.0" with date, or archive + redirect to changelog. Don't delete silently — redirect avoids adding more zero-result hits.

## Week 1-2 — diagnose search (~3-5 days)

3. Export the 190 zero-result queries. Bucket each:
   - phrasing mismatch (page exists, different words) → fix titles/synonyms, no new writing needed.
   - indexing bug (page exists, missing from index) → eng ticket, not writer task.
   - real gap (nothing covers it) → only this bucket justifies new entries.
4. Count bucket 3. That count replaces "30" as next quarter's target — could be lower, could be higher. Let data set it, not a round number.

## Week 3 onward — write, right-sized

5. Writer covers only confirmed-gap bucket. Test each new entry against docs search before publish: must return on the query that surfaced the gap.

## Swap the success metric

Drop "entries published" as the KPI. Track instead:
- zero-result search count, trending down monthly
- ticket volume on covered errors, trending down (not flat) 4-6 weeks after search fix ships
- broken links / dead channel refs in KB: 0, checked automatically
- known-issues entries cross-checked against changelog every release, not once a quarter

## Flag to writer

30 was a guess. The zero-result log was already sitting there as real demand signal — use it next time instead of picking a round number.

Next action: pull the 190 zero-result queries this week, before any new writing starts.