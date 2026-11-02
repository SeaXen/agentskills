# Q4 devrel competitive read — the 4-hour version

## The conflict, stated plainly

"Everything, across three rivals" and "four hours, solo, no engineer" don't fit together. Costed against this skill's own estimates:

| Surface | Real cost (3 competitors) | Why it can't compress |
|---|---|---|
| Timed quickstart | ~3h | One person, one run each, no shortcut |
| Docs mode coverage | ~3-6h | Per major feature, ×3 companies |
| Repo/forge health | ~1-2h manual (no API pull without an engineer) | Manual glance replaces the 10-min API pull |
| Q&A tags | ~1.5h | Cheap but still per-company |
| Content cadence | ~3 days | Needs a full 12-month sample — a 30-day look "reports the opposite of the truth" |
| Community | 1 day + calendar time | Requires 4 *separated* weeks of sampling — literally can't fit between Wednesday and Friday regardless of hours |
| Hiring | ~1.5h | Cheap, capped at one pass |
| Events | ~3 days | Least finding per hour on the list |

Minimum for "everything" is several days plus a multi-week community sample. You have 4 hours. So the plan below cuts hard, on purpose, and names what got cut instead of quietly shrinking it.

## Step 0 — before the clock starts (do this now, ~10 min)

I still need two things named, not derived:

1. **Product/project** this benchmarks (name + URL).
2. **The three rivals** — if you don't have them locked, tell me and I'll propose a category leader / closest substitute / adjacent-category outlier, plus the "what would a developer use if we vanished" fourth option, for you to confirm.

One more quick call, doesn't block starting: **individual developers or an org buyer signing off** — changes whether security/compliance pages matter. Default to individual-developer if you don't know; it's the more common OSS/dev-tool motion.

The moment you give me the three names, I run the plan below live.

## What 4 hours actually buys

Rungs 1-2 (timed quickstart, docs mode coverage) for all three, plus a manual repo glance standing in for rung 3 (no engineer to script the API pull). That's it — rungs 4-8 are cut, not shrunk. Schedule:

| Time | Activity |
|---|---|
| 0:00–0:15 | Lock product + 3 names, freeze the 12-field scorecard (below) |
| 0:15–1:10 | Competitor A — 20 min timed quickstart (hard stop, even mid-flow) → 15 min docs-mode check on 1-2 flagship features only → 10 min repo glance (releases page, CONTRIBUTING file, good-first-issue count, last 3 issues' response time by eye) → 10 min log into scorecard |
| 1:10–2:05 | Competitor B, same 55 min |
| 2:05–3:00 | Competitor C, same 55 min |
| 3:00–3:20 | Consolidate scorecard, write the per-surface read (bullets, not prose) |
| 3:20–3:50 | Gap plan: score impact/cost per gap, sort by ratio, assign verdict — close / ignore / counter — owner, date |
| 3:50–4:00 | Write the 3 findings that change what you do Friday, plus method-and-limits |

**Frozen scorecard fields** (same 12 for your product too):
1. Quickstart exists · 2. Steps to first result · 3. Timed minutes to first success · 4. Blocking step (paid wall / sales call / none) · 5. Doc modes present on the checked features · 6. Public changelog with feed · 7. Migration guide for latest major · 8. Last release date · 9. Releases visible in last 90 days *(partial-year count, not an annualized rate — say so)* · 10. CONTRIBUTING/code-of-conduct present · 11. Good-first-issue label + open count · 12. Eyeballed response time on 3 recent issues *(rough, not a median — label it as such)*.

## What you walk out with by Friday morning

- A symmetric scorecard, ours-first, 12 rows × 4 companies, every cell sourced with a URL and today's date.
- A timed-quickstart table: minutes, blocking step, where you stand — this is the finding evaluators feel most directly and the one no scraped number gives you.
- A short docs/DX read: what they do that you don't, what structural difference sits behind it (not a page-count comparison).
- A gap plan, sorted by impact-per-cost, every row verdicted close/ignore/counter with owner and date — this is the actual Q4-planning artifact, not the scorecard.
- The 3 findings that change what the team does next quarter, stated up front.
- An explicit "not covered" list (next section) so nobody mistakes the 4-hour pass for the full picture.

## What's cut — named, not buried

| Cut | Reason | Promotes when |
|---|---|---|
| Community | Needs sampling across 4 separated calendar weeks — a structural time problem, not an effort one | The Q4 question becomes "why do people adopt then leave" |
| Content cadence (12-month) | A short window reads a launch burst as a trend, or a rival's steady baseline as a slump — exactly backwards either way | Before a board/budget moment, or the moment a rival's content spike becomes part of someone's argument |
| Events/sponsorships | Lowest finding-per-hour on the whole list | Only if the actual decision in the room is a sponsorship call |
| Hiring signals | Cheapest of the cut surfaces (~90 min for 3 careers pages) — first thing to add back if the quickstarts run under time | Anytime; capped at one pass regardless |
| Q&A tags | Cheapest surface overall, and the only one where developers describe a rival in their own words | Second thing to add back if time remains |

If you want a 10-minute, clearly-labeled bolt-on: a glance at each rival's blog archive for the last 2-3 months' post count. Not a cadence read — can't separate burst from trend on that window — usable only as "they're posting / they've gone quiet," nothing stronger.

## After Friday

Save the dated scorecard to `research/devrel-competitor-benchmark-2026-Q4.md` (per your usual research-report convention) so the next pass is a diff, not a fresh opinion. That's also where the ignored gaps live, so "no community venue" doesn't get rediscovered as a surprise next quarter. If Q4 planning surfaces a real decision that needs community, content, or events, that's a separate half-day-to-multi-day pass — worth scoping once you know which of the three findings actually drove the room.

Send me the product and the three names and I'll start the 4-hour clock for real.