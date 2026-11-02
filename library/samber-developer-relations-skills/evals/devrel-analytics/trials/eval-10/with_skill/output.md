# Cinderbank DevRel tracking plan

Version: 0.1 (draft) · Owner: you · Last verified: not yet — ships this cycle · Review trigger: after the board meeting, after any product-analytics access decision, quarterly otherwise

Applying `samber/developer-relations-skills@devrel-analytics`. Skipping the interview's full ten questions — your brief already answers most of them. Where it didn't, I made an explicit assumption and flagged it (ℹ️). Fix any wrong assumption and the rest of the plan barely moves; it was built around your constraints, not around a guess at your decisions.

**Inferred interview answers:**
- Surfaces owned: docs, blog, two repos, Discord, npm. Signup/app is product's, not yours.
- Instrumented today: nothing.
- Effort ceiling: solo, no data team, one web-team ticket per month, best case.
- Hard date: board meeting in 3 weeks — **2026-10-11**. Per the skill, a hard date promotes near-zero-cost rungs and defers the identity spine; that shapes everything below.
- ℹ️ Adoption motion (self-serve vs company-buying): assumed **both** — typical Series A devtool shape. If it's purely self-serve, drop `account_id` from the identity spine; nothing else changes.
- ℹ️ Consent regime: unstated. Assumed you may have EU/UK visitors and no consent banner yet. Confirm with legal before shipping any client-side script — this gates rung 4 below, not the rest.
- ℹ️ Decisions this data should change: not stated. I propose four below — the whole plan hangs off these, so edit this table first, not last.

## Decisions this plan serves

| # | Decision | Question that settles it | Funnel view |
|---|---|---|---|
| 1 | Continue/grow DevRel budget or headcount next cycle | Is there a real, trending signal that content produces movement toward signup — not a target, a direction | Docs quickstart funnel, Blog-to-outbound-signup funnel |
| 2 | Where the one monthly web-team ticket goes next | Which surface loses more people per step: docs quickstart or blog→signup handoff | Same two views, compared |
| 3 | Keep, cut, or double down on a content format | Which surface (docs guide, blog post, sample repo) produces outbound clicks and repo engagement relative to effort spent producing it | Per-artifact link-tag report |
| 4 | Escalate product-analytics access to leadership | Is "we cannot prove content → revenue" acceptable permanently, or does the org mandate a minimal shared identifier | N/A — this is a resourcing decision, not a funnel |

If these aren't your real decisions, replace them — but replace them before you build the next section, not after. An event with no decision behind it gets deleted later anyway.

## What ships before the board meeting (3-week plan)

Everything here is zero-engineering or fits inside one ticket. Nothing here waits on anyone's permission except the two items marked ⚠️.

**This week (days 1–3) — start today, backfill is impossible:**
- ✅ **Capture today's baselines** before touching anything: current npm download figures, GitHub stars, whatever the last 14 days of repo traffic endpoints currently show, Discord member count and recent message volume. Write them into the Baselines table below with today's date. This is the only irreversible step in the whole plan — every day you wait is a day of repo-traffic history gone for good.
- ✅ **Write the tagging vocabulary and link registry** (below) — an hour, no engineering. Every link you publish from this week forward uses it.
- ✅ **Build the snapshot jobs** — a small script, e.g. a scheduled **GitHub Actions cron job** in one of your two repos, hitting the GitHub traffic API daily, the npm download API weekly, and a Discord export monthly, appending each pull to a CSV or a Google Sheet. This is entirely inside your own repos — no ticket, no data team, no product team. It's the single highest-leverage thing you build this week: it buys the only history that's otherwise unrecoverable.

**Week 2:**
- ⚠️ **Ask product for one form field, not analytics access.** You've been refused dashboard/data access twice — stop asking for that. Ask instead for a single closed-list dropdown ("How did you hear about us?") on the signup form, answer list fixed for the quarter, no access to their systems required on your end. It's a much smaller ask than the one that's been declined twice, and it's the only signal you'll have for talks, podcasts, and anything off-web.
- ✅ **Spend the one ticket** on first-party-proxied analytics for docs + blog only — a tool you own (Plausible via reverse proxy, or a PostHog project scoped to just those two domains), not the product team's system. This recovers the roughly 58% of developer traffic a third-party script never sees (Plausible, Aug 2021), and it's the only rung that gets you page-level docs behavior at all. If your docs platform lets you drop an analytics snippet via its own config (Docusaurus, Mintlify, GitBook all support this without a full sprint), this may not even need the ticket — check before spending it.

**Week 3:**
- Trace one real event end to end on docs and on blog (recipe below). Anything unverified goes into the deck labeled "unverified," not "done."
- Pull 2–3 weeks of data from the snapshot jobs and the new docs/blog collector. Build the board narrative from what actually exists — see "What to say at the board meeting" below.

**What doesn't ship this cycle, and why:**
- ⚠️ **Identity spine to signup/activation — structurally blocked.** Not an effort problem, a permissions one: product owns signup and has declined access twice. The spine stops at docs+blog. `anonymous_id` lives there; `user_id` and `account_id` don't exist in this plan until product cooperates.
- Log analysis, CLI/SDK telemetry, product-side events: deleted outright, not deferred quietly. Your effort ceiling (solo, no data team, refused product access) is below what any of these need. If they come back as "unbudgeted scope" next quarter, this is the paper trail for why they were cut.

## Surface register

| Surface | Owner | Data source | Retention | Known bias | Snapshot schedule |
|---|---|---|---|---|---|
| Docs site | you | new first-party-proxied collector (week 2) | yours | pre–week 2: nothing; post: client-side still under-counts developers | continuous once live |
| Blog | you | same collector as docs | yours | same | continuous once live |
| Repo A | you | GitHub traffic API + issue/PR API | **14 days** on traffic endpoints | clones include CI; stars only go up | daily via GH Actions cron |
| Repo B | you | same | 14 days | same | daily via GH Actions cron |
| npm | you (package) | npm download-counts API | 18 months, 7 days per version | counts CI/mirrors/bots; <50/day mostly automation | weekly |
| Discord | you | server insights / export | free-tier caps message history | bots and staff inflate raw counts | monthly |
| Signup / product | **not you** | product's own event stream | unknown | ⚠️ access declined twice — see Known gaps | none — blocked |

## Build order

| Rank | What gets built | Effort | What it buys | Deleted / deferred, and why |
|---|---|---|---|---|
| 1 | Tagging vocabulary + link registry | ~1 hour | every future link readable and mergeable | — |
| 2 | Snapshot jobs (GH Actions cron: repo, npm, Discord) | ~1 hour build, standing job | the only history that can't be bought back later | — |
| 3 | Self-reported source field (small ask, reframed) | near-zero, pending a yes | the only signal for off-web and blocked traffic | — |
| 4 | Docs+blog first-party-proxied collector | the one monthly ticket, or a config-only change | recovers the blocked developer half; page-level docs behavior | — |
| 5 | Identity spine → signup/activation | a week if you owned both domains — you don't | strongest evidence in the plan | **deferred, not deleted** — blocked on product access, escalate via decision #4 |
| 6 | Server/CDN log analysis | ~a week of data work | unblockable reach, no behavior | **deleted** — below your effort ceiling this cycle |
| 7 | Product-side events | a quarter, mostly negotiation | settles activation/behavior claims | **deleted** — access already refused twice, not an effort question |
| 8 | CLI/SDK telemetry | standing job + trust cost | real-usage signal | **not applicable** — no CLI/SDK named in scope; revisit if Cinderbank ships one |

## Identity spine

- `anonymous_id`: set by the week-2 collector, first-party, shared across the docs and blog subdomains only (confirm they sit under one apex domain, e.g. `docs.cinderbank.com` / `blog.cinderbank.com` under `cinderbank.com` — cookie sharing needs that).
- `user_id`: **not available.** Would be assigned at signup, but signup is product's surface and product has declined the access needed to emit it alongside `anonymous_id`.
- `account_id`: **not applicable this cycle** — depends on `user_id` existing first.
- Unresolvable surfaces: repos, npm, Discord, off-web (talks/podcasts if any exist), and — until decision #4 resolves — signup and everything past it. Substitute signal for all of them: the tagged-link registry, the self-reported field, and `outbound_click` events (below), read as a floor, never a total.

## Events

| Event | Surface | Trigger | Properties | Decision # | Verified |
|---|---|---|---|---|---|
| `docs_page_viewed` | docs | page render | `section`, `path`, `version`, `language` | 1, 2, 3 | pending — week 3 trace |
| `quickstart_step_completed` | docs | step checkpoint reached (evidence the step worked, not scroll depth) | `step_number`, `step_name`, `language` | 1, 2 | pending |
| `sample_copied` | docs | copy control used on a code block | `path`, `block_id`, `language` | 3 | pending |
| `docs_search_performed` | docs | search submitted | `query_length`, `results_count`, `zero_results` | 1 | pending |
| `blog_post_viewed` | blog | page render | `path`, `author`, `topic` | 1, 3 | pending |
| `outbound_click` | docs, blog | click on a link leaving the surface | `target` (`signup`, `repo_a`, `repo_b`, `npm`, `discord`), `source_path` | 1, 2, 4 | pending |
| `signup_form_source_selected` | signup (product-owned; contingent on the week-2 ask landing) | dropdown submitted | `self_reported_source` (closed list, matches link-tagging `source`) | 4 | blocked — pending product's yes |

That's the whole list — small enough to read on one screen, which is the point. `signup_completed` and anything past it (`first_api_call_succeeded`, activation, retention) do **not** appear here: you cannot fire, receive, or verify an event you have no access to. Adding it anyway would misrepresent what this plan actually measures.

## Property registry

| Property | Type | Allowed values | Notes |
|---|---|---|---|
| `section` | enum | `docs`, `reference`, `blog` | |
| `path` | string | URL path, no query string | |
| `version` | string | doc version tag, or `latest` | |
| `language` | enum | closed list matching your docs' language variants | |
| `step_number` | int | 1..n | |
| `step_name` | enum | closed list per quickstart | |
| `target` | enum | `signup`, `repo_a`, `repo_b`, `npm`, `discord` | never free text |
| `self_reported_source` | enum | closed list, stable across quarters (see link-tagging `source` below) | |
| `zero_results` | bool | | |

## Link tagging vocabulary

| Parameter | Allowed values / pattern |
|---|---|
| `source` | `x`, `linkedin`, `hn`, `reddit`, `newsletter`, `discord`, `npm-readme`, `partner` — closed list, additions need a version bump |
| `medium` | `social`, `email`, `referral`, `talk`, `sponsorship` — closed list |
| `campaign` | `<yyyy-mm>-<artifact-slug>`, lowercase, hyphen-separated |

Lowercase everything, one separator, no spaces. Never tag an internal docs→docs or docs→blog link — that restarts the session and overwrites the real source with your own, the most common self-inflicted wound on a docs site. Register every published tagged link in one table with owner and publish date; an unregistered tag is unreadable in six months.

## Funnel views

| View | Entry event | Steps | Success event | Segment |
|---|---|---|---|---|
| Quickstart funnel | `docs_page_viewed {path: /quickstart}` | `quickstart_step_completed {1..n}` | `outbound_click {target: signup}` | by `language`, by inbound `source` |
| Blog-to-signup-click | `blog_post_viewed` | — | `outbound_click {target: signup}` | by `source`, by `campaign` |

Both funnels terminate at a **click toward signup, not a signup.** Say this explicitly every time these numbers appear anywhere — it's a floor on interest, not a conversion rate, and treating it as one is exactly the borrowed-benchmark mistake this plan is built to avoid.

## Baselines captured

| Metric | Value | Date | Source |
|---|---|---|---|
| npm downloads (trailing period) | *fill today* | 2026-09-20 | npm download-counts API |
| GitHub stars, repo A / repo B | *fill today* | 2026-09-20 | GitHub API |
| Repo traffic, last 14 days (views/clones), repo A / repo B | *fill today* | 2026-09-20 | GitHub traffic endpoints — capture now, this window never comes back |
| Discord members / recent message volume | *fill today* | 2026-09-20 | Discord server insights / export |
| Docs/blog traffic | none exists pre-collector | — | starts week 2 |

Fill this table today, literally — before reading further. It's the one step in this whole plan with no do-over.

## Quality gate

| Check | Threshold | Current | Status |
|---|---|---|---|
| Decision coverage | 100% of events trace to a decision | 7/7 events trace to decisions 1–4 | pass |
| Verified traces | 100% of primary conversion events traced end to end | 0/2 (`outbound_click` on docs and blog) | fail — scheduled week 3 |
| Join coverage | ≥80% of primary conversions resolve to a first touch | **not computable this cycle** | n/a — identity spine doesn't reach a conversion event yet (see Known gaps) |
| Tag well-formedness | 100% of published external links validate | 0 links published yet under the new vocabulary | pass by default, re-check at first publish |

Below ~30 events in the reporting window (true for nearly everything you'll have after 3 weeks), report the raw dated list at the board meeting, not a percentage. A "14% click-through" built on 9 clicks will not survive the first follow-up question, and it shouldn't.

## Known gaps

| Gap | Impact on which number | Owner | Decision |
|---|---|---|---|
| No path from `outbound_click{target:signup}` to an actual signup or to activation | Every number in this plan is top-of-funnel only; content→revenue is unmeasurable | Product team / leadership | **This is decision #4.** Product has declined access twice; the org now has to choose between funding a minimal shared identifier or accepting permanent opacity on "does content work." |
| Client-side docs/blog collection still under-counts developers even after week 2 | Absolute traffic numbers are a floor, not a total | you | trust step-to-step ratios inside one funnel, never cross-tool totals |
| Only ~3 weeks of data by board day | Everything is small-N; no rate is stable | you | present raw counts with dates, set real targets after 2 months |
| Self-reported source field depends on product saying yes to a much smaller ask | Off-web and blocked-traffic attribution has no signal until this lands | product team | track as open ask, don't build a funnel view around it yet |

## Privacy gate

- Aggregate everything person-level before it reaches a slide — no per-member Discord leaderboard, no named-account funnel view.
- Confirm consent posture with legal before the week-2 collector goes live if EU/UK traffic is plausible (unconfirmed — flagged above).
- No PII in any property above; `self_reported_source` is a closed enum, not free text, specifically so it can never become one.

## What to say at the board meeting

State plainly: three weeks ago there was no instrumentation anywhere. What exists now:

1. A durable baseline for repo, npm and Discord activity that didn't exist before and would have been unrecoverable in another 14 days.
2. First-party docs and blog analytics, live for roughly [N] days, showing [raw counts, not rates] of engagement and outbound clicks toward signup, broken down by source.
3. One number this plan cannot produce, and structurally cannot produce without a decision from this room: whether that engagement turns into signups, activation, or revenue. Product analytics owns that answer and has twice declined DevRel access to it. Closing that gap costs one shared identifier field, not a new team or a new tool.

That's a true statement backed by a real trace, not a target borrowed from someone else's funnel — and it turns your resourcing problem into a decision the board is actually positioned to make.