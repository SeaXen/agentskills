I don't have live web access approved in this session, so I can't independently pull the source report. I'll flag that as a verification item rather than assume it either way. Here's the full sanity check and write-up.

---

# DevRel Program Budget — Sanity Check & Revised Plan
**Tesserine | FY1 DevRel Budget | Prepared for January Board Meeting**

## 0. Bottom line

⚠️ **Don't bring this plan to the board as drafted.** The benchmark you're mirroring is being misapplied in three separate ways, and the two-booth allocation actively works against what your sponsor (VP Eng) asked for: developer adoption. Below is why, and a revised structure that still fits inside $440k.

---

## 1. Check the benchmark itself before designing around it

**Arithmetic problem:** 41 + 31 + 19.5 + 13 = **104.5%**, not 100%. Either you've mistyped one of the numbers, the source uses overlapping/non-exclusive categories (e.g., "marketing" partially double-counts spend also tagged "content" or "events"), or the figure was misremembered. This isn't pedantry — you're about to allocate real dollars against it. Pull the original source and confirm:

- Is this "% of *program* budget" or "% of *total* DevRel budget including headcount"? Those are structurally different denominators, and it changes what "31% salaries" even means.
- What stage/size companies are in the sample? A benchmark aggregated across Series A through public companies will be dominated by larger, later-stage programs that sponsor re:Invent-scale events — that skews "events" spend upward in a way that has nothing to do with what a 1-person, first-year program at 22 employees should do.
- Is it even DevRel-specific, or a general marketing-spend survey being relabeled?

ℹ️ **Why this matters beyond accuracy:** an average describes what programs *currently spend*, not what *works*. It's descriptive, not prescriptive. A mature 15-person DevRel org spending 41% on events is diversifying across many events with a proven playbook and existing brand pull. You are none of those things yet — you're a first hire, one person, with zero track record to date. Mirroring their allocation without mirroring their maturity is a category error.

## 2. The team-size mismatch nobody's naming

You are the entire DevRel function. $440k is a **large program budget to execute solo in year one** — for comparison, that's typically enough opex to support a team of 3–5, not one person's first year. Two things to resolve before the board meeting:

- **Does $440k include your own salary/benefits?** If yes, and "31% salaries" ($136k) is meant to be *your* comp, then the "program" money you actually have to spend is closer to $300k, not $440k — which changes the two-booth math substantially (that'd make $180k of booths ~60% of your real discretionary budget, not 41%).
- If $440k is program-only (your salary sits elsewhere in the org chart), then a first-year, unproven function asking a Series A board for $440k in pure program spend — on top of headcount — is a big ask that will draw scrutiny. Boards fund unproven functions incrementally, not at steady-state benchmark levels.

Get this denominator question answered before you build anything else — it's upstream of every other number in the plan.

## 3. The two-booth allocation, specifically

This is the part most worth stopping. Per the events playbook:

**Concentration risk.** $180k in two events is two shots on goal for 41% of your entire annual budget. If either venue underdelivers — bad hall placement, a competing announcement that week, wrong attendee mix — you have no portfolio to fall back on and no year-one data to justify a second attempt. Compare: niche/regional developer events (50–200 attendees) routinely deliver *more* qualified conversations per dollar than mega-conferences, because mega-conferences dilute your booth traffic with students, press, and vendors who aren't your ICP. Bigger is not better; it's noisier and more expensive per qualified conversation.

**Audience-fit is unverified.** You build a payments-reconciliation API. Your ICP is narrow: backend/platform engineers at companies with real reconciliation pain (marketplaces, fintechs, high-volume SaaS billing teams). "Two big conference booths" only works if those specific engineers are disproportionately in that hall — a huge, general-purpose developer conference is exactly the wrong shape for a narrow, technical B2B infra product. Before committing money, name the two events and check: who actually attends, and does that list look like your ICP or like a broad audience you're paying to reach 5% of?

**Timing versus your actual deadline.** You need a story for the January board meeting. Sponsorship deals, booth builds, and staffing typically lock in months ahead, and the *payback* on a booth (qualified conversations → pipeline → any signal of "developer adoption") takes months after the event itself. If these two events land anywhere in Q1–Q2, you will have **spent 41% of the annual budget and have nothing to show the board in January** except a signed sponsorship contract. That's a bad story to walk in with as the newly-hired function.

**Metric mismatch with your sponsor's actual ask.** Your VP of Eng wants *developer adoption* — activation, integration, usage. A booth's native output is badge scans and hallway conversations, which the events playbook explicitly calls a vanity metric: "a scan is a person who walked slowly." Booths are a brand/pipeline-influence play at best; they don't directly move activation or time-to-first-API-call, which is what actually proves developer adoption. If you show up in January with "2,400 badge scans," that will not read as adoption to an engineering-minded sponsor — it'll read as spend with no adoption signal, which is the exact trap several DevRel teams I've reviewed before have fallen into (reporting downloads/impressions/sessions as "users" and getting challenged on it by technical leadership).

## 4. What's missing from the plan entirely

For an API product, developer adoption is won or lost on the parts of the journey a benchmark percentage split doesn't even name: quickstart time-to-first-call, docs quality, SDKs/sample code, and a self-serve integration path. None of that shows up as a line item in "events / salaries / content / marketing." If two booths consume 41% of the budget and there's no allocation for making the actual integration experience good, you'll be paying to drive interested engineers to a mediocre onboarding funnel — the highest-leverage, lowest-cost part of "developer adoption" is arguably not events at all, it's docs and time-to-first-call, and it's currently unbudgeted.

## 5. Revised structure

Don't port a mature-org percentage split onto a first-year solo function. Build bottom-up from the VP Eng's actual mandate (adoption) and your actual constraints (one person, no track record, board checkpoint in ~3.5 months). Suggested reallocation of program dollars (excludes the salary question in §2 — resolve that first, then apply these ratios to whatever the real discretionary number is):

| Category | Old plan | Revised | Why |
|---|---|---|---|
| Foundational adoption assets (docs, quickstarts, sample integrations, SDK polish) | $0 named | ~15–20% | Directly moves the metric your sponsor cares about; cheapest lever you have; currently unbudgeted |
| Events | $180k (2 big booths) | ~15–20%, spread across 4–6 smaller/niche events + speaking slots, not booths | Portfolio over concentration; speaking is cheaper than a booth and converts better for a technical audience; niche fintech/API events likely beat generalist mega-conferences for your ICP |
| Content (technical blog, tutorials, docs-as-marketing) | 19.5% | ~25–30% | Compounding asset, works while you sleep, doesn't need a headcount team to scale, directly supports SEO/AI-answer discovery for a narrow technical buyer |
| Community (Slack/Discord, forum, office hours) | Not named | ~10% | Cheap, scales support without you doing 1:1 white-glove for every developer |
| Marketing/tooling/ops (analytics, swag, misc) | 13% | ~10% | Keep lean in year one |

Directionally: shift weight *out* of large one-off events and *into* compounding, cheap-to-produce assets (docs, content, community) that a solo hire can actually execute without burning out, and that produce adoption signal faster than a conference booth's multi-month payback cycle.

## 6. If you keep any conference presence

- Prefer **speaking slots over booths** at 1–2 well-targeted events. Cheaper, and a technical talk converts a skeptical engineering audience better than a booth ever will.
- If you do sponsor, require: a named target list of ICP attendees built *before* the event, a meetings-booked target (not a badge-scan target), and 24–48 hour follow-up discipline — most sponsorship ROI is lost in the follow-up gap, not the floor time.
- Pick events by checking who *actually* attends against your ICP, not by size or brand recognition of the conference.

## 7. What to report to the board instead of badge scans

Tie every line item to something adoption-shaped:
- Time to first API call (quickstart effectiveness)
- % of signups reaching a production integration
- Qualified developer conversations / meetings from any event activity (not scans)
- Docs/content-driven signups (source-tagged)
- Community-reported issues resolved without your direct intervention (scalability signal)

This also gives you a defensible story in January even if it's early: "here's the funnel we're instrumenting and the first-quarter baseline," rather than a spend recap with no adoption tie-back.

## 8. Before you finalize anything

1. Confirm the actual source and exact numbers behind 41/31/19.5/13 — get the sample's company stage/size, and fix the >100% total.
2. Confirm whether $440k includes your salary. This changes every other number.
3. Name the two candidate conferences and pull their actual attendee composition — don't assume ICP fit.
4. Decide, with the VP of Eng explicitly, what "developer adoption" means as a measurable metric (activation rate? time-to-first-call? production deployments?) before allocating a dollar — right now the plan is optimizing for a benchmark's shape, not for his stated goal.