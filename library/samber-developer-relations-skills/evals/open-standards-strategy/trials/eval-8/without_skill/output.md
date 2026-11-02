## KPIs

**Primary KPI — independent interoperating implementations.** Two independent implementations of HarborLink v1 interoperate, at least one built by an organization that is not our customer, by August 2027 (12 months from v1's publication in August 2026).

"Interoperate" means: the two implementations exchange HarborLink messages with each other, not just with our reference implementation.

**Secondary KPI — conformance pass rate.** Each of the two implementations passes at least 95% of the HarborLink conformance suite. An implementation that interoperates informally but fails a meaningful share of the suite does not count toward the primary KPI — publish the pass rate per implementation, not just a combined average, since one strong implementer can otherwise mask a weak one.

**Tracked separately, not counted as a KPI — vendor interest.** Six vendors have told us they're interested as of September 2026. Log each as a pipeline stage (interested → building → conformance-testing → interoperating) with a date at each stage. Interest is a leading indicator; it becomes a KPI contribution only when an implementation exists and clears the conformance threshold. Do not report the six as progress toward the primary KPI in any status update.

## Stop condition

Review is set for September 2027, one month after the 12-month window closes — so the review works from actual results, not a projection.

At review, if fewer than two independent implementations meet both the interoperability and 95% conformance thresholds:

- Do not extend the 12-month window by default. Extending it requires a separate, explicit decision with its own new deadline.
- Withdraw v1's "published" status and revert it to draft, pending the blockers found in the vendors that stalled.
- Write down, for each vendor that expressed interest but didn't ship, the reason they stalled (spec gap, resourcing, priority). Fix the spec gaps in a v1.1 before reopening the window; don't reopen on an unchanged spec.
- I hold the call on whether to extend, revise, or withdraw, since I own this spec.