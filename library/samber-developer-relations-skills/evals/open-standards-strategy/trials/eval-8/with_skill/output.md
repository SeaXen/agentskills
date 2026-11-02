# Standards decision: HarborLink — KPIs and kill rule

Date: 2026-09-24 · Owner: Samuel Berthe · v1 published: August 2026 · Review: August 2027 (12 months from v1 — same clock the thresholds below run on)

## KPIs and thresholds

| Metric | Threshold | Sourced or baseline | By when |
|---|---|---|---|
| Independent interoperating implementations (not controlled by us, not built by a customer under our direction) | ≥ 2 | **Sourced** — RFC 6410 §2.2, IETF's bar for Proposed → Internet Standard: "at least two independent interoperating implementations with widespread deployment and successful operational experience." | August 2027 |
| Of those, at least one implementer that is not a paying customer | ≥ 1 | **Baseline** — RFC 6410 sets no deadline and no customer test; this is this skill's proposed starting clock, not an industry norm. Flagging it as such so the review argues the right thing. | August 2027 |
| Of the 6 vendors who have expressed interest, count that have actually shipped an implementation | ≥ 2 of 6 | **Baseline** — this is our target integration surface, not counted demand yet. "Interested" is not "implemented"; track the conversion, not the headcount of 6. | Checked quarterly, reviewed August 2027 |
| Conformance pass rate: share of implementations claiming HarborLink compatibility that pass the current test suite version | 100% of implementations making the claim | **Baseline** — no suite exists yet if it wasn't shipped with v1; this threshold assumes Step 5's conformance plan (versioned mark, public registry) is in place before any vendor is allowed to claim support. | Ongoing from suite launch; checked at August 2027 review |

Note the first row is the only number in this table you can defend by citing a source — the second and third rows are ours, chosen from a 12-month horizon because that's roughly this market's own integration/release cadence, not because any body set it. Say so out loud if procurement or legal pushes back on "why 12 months."

## Kill rule

If, at the August 2027 review, fewer than two independent implementations exist, **or** the only implementations that exist are customer-built under our direction (i.e., the non-customer test also fails), we de-escalate from Drive:

- Stop funding roadmap control and stop actively recruiting new implementers.
- Either offer HarborLink to a neutral foundation (if any of the 6 interested vendors will co-fund and stay) or fold back to Contribute-level effort against whatever alternative spec has since filled the gap — whichever is cheaper at that point.
- Publish a note saying we're stopping, rather than letting the spec sit unmaintained while still claiming "v1" status.
- Anyone who shipped a HarborLink implementation before the kill date gets 6 months' notice, a maintained reference implementation for that window, and a documented successor or migration path. We caused the adoption; we own the exit cost, not them.

Separately — not a kill trigger, a revision trigger: if two or more independent implementations exist by August 2027 but conformance pass rate stays below 100%, that means the spec text is ambiguous, not that the spec failed. Response is a v1.1 clarification plus a test suite update, not withdrawal. Don't let a conformance gap and a real-implementations gap collapse into the same decision — they call for different fixes.

One thing to fix before this goes final: 6 vendors saying "interested" is not evidence toward either threshold above — it's a sales signal, not a counted implementation. Don't let it get cited in the review as if it were progress toward the 2-implementation bar; track it only as the denominator for row 3.