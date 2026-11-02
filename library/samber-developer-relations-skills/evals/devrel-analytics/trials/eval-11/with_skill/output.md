Hold send. 261 vs 4 matches a known pattern exact: stitch ship, near-zero-before flips to real numbers same week. That flip is instrumentation resolving, not signups growing — skill's own failure-mode table names this row by name: "Attributed conversions jump the week the stitch ships → the spine only started resolving then → annotate the date; compare only within post-stitch period until a full cycle passed." Green debugger and firing tags confirm config, not measurement — playbook rule: "A green debugger is not evidence; the trace is."

**Check before you send (in order):**

1. **Pull total signups**, attributed + unattributed, same two weeks. This is the one that decides everything else. If total is flat, 261 is reclassification — signups that landed in "direct"/"unknown" before now resolve to a real source. Zero net new signups possible even with a 65x jump in the attributed count. If total also rose, you have two separate claims (stitch works + signups grew) and need to state them separately, not fused.
2. **Run one end-to-end trace**, not a debugger check: real browser, tagged link in, confirm the signup event payload carries `anonymous_id` + resolved source, confirm it lands in the actual report row the 261 comes from. Config green ≠ trace done.
3. **Check join coverage rate**, not the raw 261. 261 divided by total signups this week, against your 80% floor. A raw count with no denominator hides a broken stitch that only half-resolves.
4. **Check for double count.** Same signup landing once through the old path and once through the new stitched path inflates the 261 directly. Confirm one unique event ID per conversion, deduplicated on it.
5. **Check the backfill didn't overwrite populated rows.** Rule: backfill only fills blank `source`, never touches one already `journey_linked` or `self_reported`. If it touched populated rows, some of the 261 may be corrupted merges, not new resolutions.

Then, lower priority, before next month's number:
6. Confirm `source_basis`/`source_confidence` are populated per record, not just a bare channel name — you'll need this to defend the number later.
7. If any account rollup is in play, confirm free-mail domains are excluded from the match.

**Wrong framing** (don't send this):

> Cross-domain identity stitching drove a 65x increase in attributed signups this week.

That states a growth claim the data can't yet support — it's exactly the borrowed-benchmark mistake this field's practitioners warn against, just aimed at your own prior week instead of another company's number.

**Right framing**, once check #1 confirms total signups didn't just get relabeled:

> We shipped cross-domain identity stitching Monday, closing the gap between [domain A] and [domain B] that previously blinded source attribution. Attributed signups went from 4 to 261 — expected, not a signup surge: pre-stitch, almost nothing could resolve to a first touch, so last week's "4" undercounted, not underperformed. [If total signups flat: Total signup volume was unchanged (X both weeks); this is visibility, not growth.] [If total signups also rose: Total signups also rose from X to Y in the same window; we're treating that as a separate signal, still confirming causality against [other launch activity].] We'll report join coverage (currently Z%) as the standing health metric going forward, and re-baseline the target once a full post-stitch cycle of data exists.

Next: run check #1 (pull the total-signup number). Everything else in this update hinges on that one comparison.