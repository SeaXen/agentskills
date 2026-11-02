# Does the Oakhaven docs measurement plan hold up?

**No, not as written.** The plan has three problems: the headline KPI measures the wrong thing, the 70% target has no basis, and the testing is too big for your team. The restore-page conclusion is unsafe. I've kept the parts worth keeping and added a revised plan you can take to your VP.

I haven't seen your analytics, so the reasoning below rests on what you described.

## 1. Page views as the headline KPI

**Verdict: demote it to context.**

- **A view isn't a success.** Someone restoring a backup is often mid-incident. A rise in views can mean the product got harder or had more incidents, and a fall can mean the product got better.
- **Three pages carry about 60% of traffic.** The other 37 pages split the remaining 40%, so each gets roughly 1% of total traffic. A per-page KPI across all 40 is mostly noise on 37 of them.
- **Views can't show whether a page worked.** Your VP will ask whether the docs helped. Views can't answer that.

**Use instead, per page:**
- **Headline:** tickets mentioning the page, per 1,000 views.
- **Better, if your platform engineer can pull it:** the product's own completion rate for the task. Examples are restores completed versus started, replicas created, and credential rotations finished.

Keep views as the denominator and as a traffic alert.

## 2. 70% "helpful" target from a vendor blog

**Verdict: keep the widget, drop the target.**

- **The benchmark isn't yours.** A docs-tooling vendor's blog doesn't tell you what your audience, widget wording or placement produces.
- **Thumbs measure sentiment, not task success.** People also vote down when the product lacks a feature, and the page can't fix that.
- **Response rates are low and self-selected.** On a long-tail page with 200 views a month and a 3% response rate, you get about 6 votes. At that size 70% and 50% are indistinguishable.
- **A fixed target invites gaming.** Teams end up tuning the widget instead of fixing the page.

**Do this:**
1. Collect a 6-week baseline and record the response rate beside the helpful rate.
2. Set the target as improvement on your own baseline, for the top 3 pages only.
3. Add a reason picker on thumbs-down: "steps didn't work", "something's missing", "product can't do what I need". This turns the widget into a work queue.
4. On the long tail, pool votes into a rolling quarter and read the comments. Don't compute rates on single pages.

## 3. Quarterly moderated task test on all 40 pages

**Verdict: not feasible, and not the best use of testing.**

- **The volume is too big.** Forty pages at 5 participants each is about 200 sessions a quarter. A small writing team plus one engineer for one day can't run that.
- **The pages need real infrastructure.** Restore, replica and credential rotation need live instances with backups and a primary. The test environment is the expensive part.
- **A quarterly snapshot goes stale.** You deploy continuously and have no version numbers. A page tested in January can be wrong by February.

**Do this:**
- **Top 3 pages:** run a moderated test each quarter with about 5 participants per page, so about 15 sessions. Five users usually surface most major usability problems.
- **Long tail:** test 3–4 pages a quarter, chosen by risk. Prioritize destructive or irreversible tasks such as failover, delete and downgrade. A lighter engineer walk-through that follows the steps verbatim works here.
- **Drift:** put a "last verified" date on every page. Re-verify when the underlying service ships a change, not on a calendar. Without version numbers, that trigger is how you catch drift.

**The platform engineer's day:**
- Spend most of it on a disposable, scripted test environment with a seeded backup and a primary. Every future test reuses it.
- Spend the rest on a query that joins page views to product completion events. That one query is your headline metric.

## 4. "Restore tickets went from 12/month to zero, so it's fine"

**Verdict: don't conclude that yet.**

- **Something changed.** If the true rate were still about 12, a month of zero would be vanishingly unlikely, around 1 in 160,000. A drop to zero is a real change, but it isn't necessarily an improvement.
- **"We changed nothing on the page" is weak evidence.** You deploy continuously, so the product, the console, the error messages and the support setup around the page can all change.

**Plausible causes other than a better page:**
- **Product change.** A UI or automation change made restore easier or removed the failure mode.
- **Ticket classification or routing change.** A new tag, form, macro or deflection flow, a tool migration, or a staffing change.
- **One-off cause.** One customer or incident was generating most of the 12.
- **Users stopped asking.** They gave up, or went to a community, search or an AI assistant instead.
- **Users can't find the page.** A search ranking or navigation change may have buried it.

**Check this first (about an hour):**
1. Compare restore-page views, thumbs and comments, month over month.
2. Pull product events for restore started, succeeded and failed.
3. Look at total ticket volume and the backup and PITR tickets (point-in-time recovery) for the same month.
4. Check what changed in ticket tagging, support tooling and the console that month.

The restore page is also one of your three highest-stakes pages. It stays in the top-3 test rotation either way.

## Revised plan for your VP

| Layer | What | Cadence |
|---|---|---|
| Headline (top 3 pages) | Tickets per 1,000 views, plus product task completion if available | Monthly |
| Context | Page views, with product and incident annotations | Monthly |
| Sentiment | Thumbs widget with reason picker, baseline first, target set against your own baseline | 6-week baseline, then quarterly |
| Task test | Moderated test on the top 3 (about 15 sessions), plus 3–4 risk-chosen long-tail pages | Quarterly |
| Freshness (all 40) | "Last verified" date, re-verified when the underlying service changes | Event-driven |
| Long tail | Pooled quarterly thumbs and comments, ticket tagging by page | Quarterly |

## Questions that would sharpen this

- Do tickets carry a page or topic tag, or only free text?
- Does the product emit start and completion events for restore, replica creation and credential rotation?
- Where would you recruit task-test participants: customers, or internal engineers who don't know Oakhaven?