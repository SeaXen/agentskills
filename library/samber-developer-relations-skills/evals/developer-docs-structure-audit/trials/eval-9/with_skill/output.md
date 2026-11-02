# Almsley Robotics docs backlog — write order for the 14 missing pages

## The one thing blocking a literal 1–14 list

I don't have your actual grid — which of the 24 (surface × mode) cells are the 14 empty ones. I can't invent that and label it fact (that's the "silent inference" failure mode the audit skill explicitly warns against). What I can give you: a decision rule that ranks *any* cell in your matrix, applied to your six surfaces, so you sort your real 14 into it in about a minute. Paste the actual grid and I'll turn this into a literal numbered list with evidence per row.

Audience, flagged as inferred (you didn't state it): Fleet API, on-prem deployment, and Grafana integration read as enterprise/procurement surfaces; Python SDK, C++ SDK, and ROS 2 bridge read as self-serve developer-adoption surfaces. That split drives the ranking below — say if it's wrong.

## The rule

Primary key — mode damage, from the skill's heat map:

1. **Reference** empty on a surface someone configures — worst. Sends people to source or support.
2. **How-to** empty on a surface with real-world variability — repeat ticket generator.
3. **Tutorial** empty — only counts once per audience. If Python SDK already has a quickstart, a missing C++/ROS2/Fleet API tutorial is very likely *correctly* empty, not a gap. Don't queue a second tutorial per surface.
4. **Explanation** empty — slow-burn mistrust, except on procurement surfaces (Fleet API, on-prem), where it's a live sales blocker, not a someday item.

Secondary key — surface weight, given the inferred audience split:

| Surface | Why it ranks where it does |
|---|---|
| Fleet API | enterprise adoption path + the one live pain signal you have (78% exit) |
| On-prem deployment | procurement blocker: security/HA questions kill signed deals before a human reads page 2 |
| Python SDK | largest likely self-serve population, primary onboarding surface |
| ROS 2 bridge | ecosystem-critical integration, smaller population than core SDK |
| C++ SDK | self-serve but narrower (real-time/embedded) audience |
| Grafana integration | optional secondary integration, smallest blast radius by default |

## Generic ranked order (24 cells) — strike your 10 filled ones, keep the rest in order

| Rank | Surface | Mode | Why |
|---|---|---|---|
| 1 | Fleet API | Reference | configured surface, live pain signal — **verify it isn't already covered by /api/fleet/overview before writing new** |
| 2 | On-prem deployment | Reference | procurement blocker (config/sizing/ports) |
| 3 | ROS 2 bridge | Reference | integration surface, undocumented reference = readers hit source code |
| 4 | Python SDK | Reference | check this is genuinely empty — unlikely for a flagship SDK |
| 5 | C++ SDK | Reference | |
| 6 | Grafana integration | Reference | dashboard/metric schema |
| 7 | Fleet API | How-to | ops tasks: reassign a robot, handle an offline fleet member, bulk commands |
| 8 | On-prem deployment | How-to | upgrade in place, rotate certs, scale a node pool |
| 9 | ROS 2 bridge | How-to | common integration recipes |
| 10 | Python SDK | How-to | |
| 11 | C++ SDK | How-to | |
| 12 | Grafana integration | How-to | the one standard fleet-health dashboard recipe |
| 13 | Fleet API | Explanation | architecture/consistency/rate-limit model — this is the page that stops the 78% exit, not a rewritten overview |
| 14 | On-prem deployment | Explanation | security model, network architecture, HA story |
| 15+ | ROS 2 bridge / SDKs / Grafana | Explanation | promote only if a specific "surprising mental model" ticket exists — otherwise correctly stays empty |
| — | any surface | Tutorial | promote only the *one* cell that is the audience's actual missing first-run path; every other empty Tutorial cell is by design |

Your 14 will cluster somewhere in ranks 1–14ish once you strike the filled ones — read them off in the order they fall in this table.

## Before you lock rank 1–2 for Fleet API: check it isn't a split

/api/fleet/overview at 78% exit is your strongest signal, but the skill is explicit: a high-exit page isn't automatically a missing-page gap — it can mean the page is trying to do two jobs (Explanation + Reference on one URL, the classic "overview" symptom) and readers bounce because neither job is finished. If that's what's happening:

- The fix is a **split** (a day, ships Monday) — not one of your 14 missing-page writes (a week each).
- Splits jump the queue ahead of every missing-page write regardless of rank, because a split ships immediately with no dependency.

Open the page before committing a week of writer time to it.

## 15-minute check before you finalize Monday's order

You have three reachable signals — use them to confirm or cut candidates, per the skill: a gap without evidence is a question for the team, not a queued page.

- **Algolia**: pull zero-result queries and no-click queries for terms matching each of your 14 candidate surfaces/modes.
- **GitHub issues**: filter `question`/`support`/`docs` labels per surface — three+ repeats on one surface confirms a gap.
- **Page analytics**: corroborate the Fleet API exit rate with a ticket or search-query cluster before treating it as confirmed — an exit alone can also mean the reader got their answer and left satisfied.

Any of the 14 with zero hits across all three signals: park it as a question for the team, don't burn a writer-week on it speculatively.

## Queue format to fill in once you confirm the real 14

| # | Action | Page(s) | Mode outcome | Reader need fixed | Effort | Evidence |
|---|---|---|---|---|---|---|
| 1 | Split /api/fleet/overview (if confirmed mixed) | api/fleet/overview.md | explanation + reference → two pages | reader stops landing on a page doing two jobs | 1 day | 78% exit rate |
| 2 | Write Fleet API reference (if genuinely missing) | new: reference/fleet-api.md | reference | reader stops hitting source/support for config | 1 wk | [fill: Algolia/issues] |
| 3 | Write on-prem deployment reference | new: reference/on-prem-config.md | reference | procurement gets a real config answer | 1 wk | [fill] |
| ... | | | | | | |

Fill "Evidence" only with what your three signals actually show — leave `[confirm]` on any row you haven't checked rather than a guess, so the queue stays honest when someone re-scores it in three months.