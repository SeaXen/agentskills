# Does the measurement plan hold up?

**Mostly no.** Two of the three KPIs are mis-specified, the third costs far more than your team has, and the best signal for your situation is missing. The restore page is not "clearly fine".

I applied the KPI section of the `developer-how-to-guide` skill. Its wiring costs are estimates, not measurements, so check them against your own stack.

## Verdict per item

| Proposal | Verdict | Why |
| --- | --- | --- |
| Page views as headline KPI | ❌ Demote | Views measure demand, not quality. A how-to that works can produce fewer views, because fewer people come back or search again. Use views to rank where to spend effort, not as the goal. |
| Thumbs-up with a 70% target | ⚠️ Keep the widget, drop the target | Votes are triage only. They aren't validated against whether the reader finished the task. A docs-tooling vendor's blog isn't your baseline, and a different audience, page type and widget wording shift the number. Collect a quarter of your own data, then set per-page targets from it. Read the free-text comments, because they point at the broken steps. |
| Moderated task test on all 40 pages, quarterly | ❌ Not affordable | The task test is the highest-value signal and the most expensive, at about a day per round. If a round is one page, 40 pages is about 40 person-days a quarter, against one engineer-day. Each run also needs a disposable Postgres environment seeded to the reader's starting point, and restore and credential rotation are destructive. Scope it to the few pages that carry the traffic. |
| (missing) Executable steps in CI | 🥇 Add this first | It is the only signal that catches drift before readers do. Your product deploys continuously, so pages break when the product changes, not when the docs change. Setup is about half a day, then near zero upkeep. |
| (missing) Tickets citing the page or task | ✅ Add | It costs almost nothing to collect, and each ticket points at a wrong, ambiguous or missing step. |
| (missing) Search refinements and returns to results | ✅ Add if search analytics exist | About an hour of work. It shows when a title or goal line promises something the page doesn't deliver. A plain exit is often success. |

## The restore page: don't conclude it's fine

Your skill's rule is that when tickets fall with no other change, **silence can also mean readers gave up**. A drop from about 12 a month to exactly zero, on a page nobody touched, is a signal to check. It is not a result to report to the VP.

"We changed nothing on it" is the weak point. You deploy continuously, so the product under the page may have changed even though the page didn't.

These explanations all produce zero tickets:

- The page is now wrong and readers give up without writing in.
- Ticket routing or tagging changed, so restore tickets no longer carry the page mention.
- A support macro, a new channel or a product-side fix absorbed the demand.
- Traffic to the page fell, for example after a search ranking change.

Checks, cheapest first:

1. Compare restore-page views for the same months. If views held steady, readers are still arriving and not writing in.
2. Ask support whether tagging, forms or macros changed last month.
3. Read the page's thumbs-down comments and search refinements for the same period.
4. Have someone other than the author do a cold run of the page on a disposable instance. Restore is destructive and carries a lot of traffic, so it goes first in the task-test rotation.

If steps 1–3 show nothing changed on the reader side, and the cold run passes, then you can call it fine.

## Plan to take to your VP

**Headline:** share of top-traffic how-tos whose steps pass in CI against the live product. Report tickets citing each page next to it.

1. **Spend the platform engineer's day on CI for the three big pages.**
   - Cover restore, add a read replica and rotate credentials. Together they carry about 60% of traffic.
   - Run them against a disposable instance with fixture data and tear it down afterwards. Assert the documented output, not just the exit code.
   - Run it on a schedule, not only on docs commits.
   - Expect this to take longer than half a day, because each page creates billable Postgres resources. If it doesn't fit, do restore first.
2. **Collect cited tickets for all 40 pages.** Add a page tag to the ticket form if there isn't one. Read the tagged tickets monthly.
3. **Keep the thumbs widget with free text and no target.** Use it to triage and to prioritise edits. Set targets after one quarter, per page, from your own baseline.
4. **Run the moderated task test on the top three pages**, scored per subtask. Do restore this quarter, then rotate. Add one or two more pages a quarter from the ticket and search signals if the writers have time.
5. **Stamp all 40 pages** with `owner` (a team), `tested_with` (a run date, since you have no version numbers) and `last_verified`. Flag any page whose `last_verified` is older than one quarter. This is a cheap drift signal for the 37 pages without tests.
6. **Use page views to rank, not to judge.** They show which pages deserve the tests, and they're free.

## Open questions

These could change the ranking:

- Does a docs-test job already run in CI? If so, executable steps cost almost nothing.
- Does search analytics exist on the docs site?
- Can support tag tickets by page?
- Do you have a disposable Postgres environment that the platform engineer can provision quickly?

Answer these and I'll re-rank the plan.