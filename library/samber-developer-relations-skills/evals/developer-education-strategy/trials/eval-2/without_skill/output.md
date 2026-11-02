## The problem, reframed

You don't have a content gap. You have 53 assets and zero structure. "Where do I start" isn't a documentation question, it's a navigation question — and it's the cheapest kind of problem to fix, because the fix is almost entirely rearrangement, not writing. That's good news given your constraints: one writer, 8 hrs/week, 8 weeks, $0.

Don't let this turn into "write more tutorials." More flat-list content makes the problem worse, not better. The deliverable is a **structure layered on top of what already exists**, plus the connective tissue between pieces.

---

## What to build: a "Start Here" hub with 4-5 role-based paths

Not a new tutorial. A single landing page that routes a developer to an ordered sequence of *existing* tutorials/videos based on what they're trying to do — built on the tutorial/how-to/reference/explanation split (Diátaxis), which is the standard model for exactly this problem.

**Hub page** — one screen, no scrolling required:
```
What are you trying to do?

→ Instrument my first service         (path: 5 steps, ~30 min)
→ Set up alerting & on-call            (path: 4 steps, ~20 min)
→ Migrate from Datadog / New Relic     (path: 3 steps, ~15 min)
→ Roll this out to my team             (path: 4 steps, SSO/RBAC)
→ Go deep on distributed tracing       (path: 6 steps, advanced)
```

**Each path page** is just: ordered links to existing tutorials/videos, one sentence per step on *why this step, what you'll have after it*. No new long-form content — you're writing connective sentences, not tutorials.

**Each existing tutorial** gets a small retrofit: a breadcrumb ("Part of: Set up alerting, step 2 of 4") and a "Next" link. That's a templated, mechanical edit across 53 pages — not a rewrite.

This is the same move ReadMe/Twilio/Stripe made when their docs sprawled: the fix wasn't more docs, it was a routing layer.

---

## 8-week plan, scoped to 8 hrs/week (64 hours total)

| Week | Hours | Work |
|---|---|---|
| **0 (this week)** | — | Start capturing baseline *before* touching anything — see Metrics below. Costs nothing, but you can't show delta without it. |
| **1** | 8h | Audit all 41 tutorials + 12 videos into a spreadsheet: title, product surface, use case, skill level, format, last-updated. Tag each against candidate personas/use cases. |
| **2** | 8h | From the audit, define 4-5 paths (use case clusters, not product-org clusters — org charts make bad navigation). Map existing assets into paths. Flag genuine gaps — expect 1-3 missing "bridge" pages, not 20. |
| **3-4** | 16h | Build the hub page + path pages. Retrofit existing tutorial pages with breadcrumb + "next step" links (templated, bulk edit). Set up redirects so old flat-list URLs still resolve (protects existing SEO/support links). |
| **5** | 8h | Add lightweight instrumentation (below). Soft-launch: swap the hub in as the default docs entry point. |
| **6-7** | 16h | Live for 2-3 weeks before the board meets — this is the window that produces real numbers, not projections. Fix friction points from real usage/support tickets. Write the 1-3 gap pages identified in week 2, if still needed. |
| **8** | 8h | Package the board narrative: before/after data, one screenshot of the hub, one quote or support-ticket trend line. |

Note the shape: build finishes by week 5, not week 8. A board wants evidence a change worked, not a demo of a change that shipped yesterday. Reserve weeks 6-7 as *live data collection*, not buffer.

---

## What's explicitly out of scope

Say this to the board too — it's a feature, not a gap:

- No new tutorials beyond 1-3 short bridge pages. 41 tutorials is not the bottleneck.
- No video re-recording or re-editing. Existing videos get linked into paths with a one-line description, as-is.
- No new hire, no contractor, no tooling purchase. The hub is a content page on your existing docs platform, not custom software.
- No CMS/platform migration. Whatever renders your docs today renders this.

---

## Metrics for the board (start this week)

You need a baseline captured *before* the rebuild, or the board story is "we built a thing" instead of "we fixed a measured problem."

**Capture now, this week:**
- Count of "where do I start" — style support emails/week (you said weekly; get an actual number and a source, e.g. a saved search or tag in your support tool).
- If you have any docs analytics: bounce rate / time-on-page on the current flat tutorial list.

**Capture during weeks 6-7 (post-launch, live):**
- Same email count, same tag, same time window — direct before/after.
- Hub → path click-through rate, and path completion rate (last step reached), via simple analytics events on the hub and each path page.
- Any support tickets that reference the new hub/paths directly ("found it in Start Here").

**Board slide is one chart**: onboarding-support-email volume, week-by-week, with a vertical line at the launch date. That's the whole pitch — you spent 64 hours of existing headcount and no budget, and the line moved.

---

## Risk to flag to the board proactively

Eight weeks is enough to ship and get 2-3 weeks of signal, but not enough for a fully mature answer — some paths will be thin, some assets will resist clean categorization, and the 1-3 gap pages might slip if the audit turns up more structural mess than expected. Frame week 8 honestly as "first working version, instrumented, already moving the number" rather than "finished." That's a stronger board story than a polished thing with no data behind it, and it sets up the next quarter's ask if you want to argue for more writer time later.