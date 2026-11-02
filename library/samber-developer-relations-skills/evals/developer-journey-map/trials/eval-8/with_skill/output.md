Two calls up front, since you asked directly:

- **Labels:** don't drop difficulty tiers to zero, but they're not the lever. Santos et al. (74-participant study, arXiv:2103.12653) found newcomers pick tasks by which API/component they already know, not by a maintainer's difficulty guess. Relabel by area (`area:postgres-driver`, `area:cli`, `area:migration-runner`, `area:docs`), keep `easy/medium/hard` as a secondary filter.
- **Buyer lane:** none. Thistlewrap is self-serve MIT, nobody pays — the map says so explicitly below, per this skill's own rule for that case, rather than leaving it blank.

Full map follows. It's a single-shot draft — no interview round-trip, since you asked for the deliverable direct. Assumptions are named in Scope; correct any and I'll re-cut.

---

# Developer journey map — Thistlewrap external contributors, 2026-09-19

## Scope

**Segment:** developers already running Thistlewrap in production who could become external contributors. Not the discovery/adoption audience — that funnel is already working (3,800 stars, production use at multiple companies) and is out of scope here.

**End state:** sustained outside contribution — a first-time contributor returns for a second one.

**Stage model:** OSS contributor funnel (Land → find work → set up → change → submit → survive review → return). Chosen by deletion, not preference:

- Revell six-stage (terminal: standardization) — dropped, no enterprise-standardization question in play.
- AAARRRP (terminal: revenue) — dropped, nothing is sold.
- API five-stage arc (terminal: production) — dropped, production adoption is the solved part, not the problem.
- Unsourced discover→advocate default — dropped, too coarse to name an exit event inside "contribute."
- OSS contributor funnel (terminal: return) survives — it's the only model whose tail is "sustained outside contribution," and it costs about a week to stand up because the repo already holds first-PR, review-latency and return data (GitHub's own guides + `stage-models.md`).

**Assumptions made without an interview** (confirm or correct):

1. You are the sole maintainer reviewing PRs — no separate triage/review team.
2. "Two outside PRs a quarter" means PRs that reach submission and are largely merged, not a mix of opened-and-abandoned. Unconfirmed — see Gaps.
3. No friction log, no exit interviews, no issue-view analytics exist yet. Every early-stage cell below is inferred or not instrumented as a result.

## Journey

| Stage | Developer's job | Entry trigger | Exit event | Touchpoints | Owner | Friction evidence | Signal |
|---|---|---|---|---|---|---|---|
| Land | "See if this project actually wants outside help, and whether I could plausibly do it" | Opens the Issues tab, already a production user | Opens or comments claiming an issue | README, CONTRIBUTING.md, issue tracker | Maintainer (solo) | No evidence yet | Not instrumented — GitHub exposes no "issue viewed" event |
| Find work | "Pick a task I can finish without wasting the maintainer's time" | Browsing open issues/labels | Comments "I'll take this" or opens a draft PR against an issue | Issue labels (`easy/medium/hard`), issue templates | Maintainer (solo) | Santos et al., arXiv:2103.12653: newcomers select by required API domain, not a maintainer's difficulty tier — applied inference, not measured on this repo yet | Not instrumented — candidate: share of newcomer-claimed issues with zero follow-up in 14 days |
| Set up | "Get the repo and its test DB running locally" | Clones repo, runs test suite | Local build/tests pass | CONTRIBUTING.md, Makefile, test-DB fixtures, CI config | Maintainer (solo) | No evidence yet — recommend a friction log from the next first-timer | Not instrumented |
| Change | "Write the fix without breaking migration ordering or backward compat" | Local tests pass | Pushes a commit implementing the change | Code, existing tests, lint config | Contributor; maintainer owns whether guidance/design notes exist | No evidence yet | Not instrumented |
| Submit | "Get this in front of the maintainer" | Branch pushed | PR opened | PR template, CI checks | Contributor; maintainer owns CI | ~2 outside PRs/quarter (maintainer-reported; interpretation of "opened" vs "merged" unconfirmed — see Gaps) | Raw count, below the 30-event floor — track as dated list, not a rate |
| Survive review | "Get this merged without endless back-and-forth" | PR opened | PR merged | PR review thread, CI | Maintainer (solo) | GitHub Open Source Guides: contributors reviewed within 48h return at a much higher rate; "it only takes one negative experience to make someone not want to come back" — cited finding, not yet checked against this repo's own review latency | Not instrumented — pull median time-to-first-review from PR timestamps (available today via `gh pr list --json`, no new tooling needed) |
| Return | "Decide whether to do this again" | First PR merged | Opens a second PR (any time horizon) | Merge comment, changelog credit, any follow-up mention | Maintainer (solo) | Maintainer-reported: "almost every first-timer never comes back" — self-observed, not yet interview-verified | Raw list needed (name + date of anyone who returned) — currently ~0, well below the 30-event floor |

Every row's owner collapses to the same one person. That's itself the finding this map is supposed to surface: there is no differentiated ownership anywhere in this funnel, which is a bus-factor risk independent of the leak below.

## Buyer lane

None — self-serve, MIT-licensed, nobody pays. Stated explicitly per this skill's own rule, so a later reader knows it was decided, not forgotten.

If a production user's own company ever blocks adoption on license or dependency-policy grounds, that's friction inside the (separate, already-healthy) adoption funnel — not a lane in this map.

## Moments

- **First success** — first PR from an external contributor gets merged. No measured median time yet; only known input is ~2/quarter.
- **Moment of truth** — not the merge itself, but what happens in the two weeks after: does anything point the contributor at a next task, thank them by name, or invite them back. Evidenced by the GitHub Open Source Guides finding above, not yet confirmed on this repo.
- **Abandonment point** — maintainer-observed as after the first merge, before any second attempt. Flagged as inferred: because Land/Find work/Set up are completely dark, it's also possible worse abandonment is happening earlier and simply isn't visible yet.

## Leak

**Return.** It's the only stage with a concrete, if crude, observed conversion — everything upstream is unmeasured rather than confirmed-bad. Owner: the maintainer, who already controls the one lever the cited evidence points at (review speed and tone).

This wins the earliest-and-owned test only because the upstream stages aren't measured well enough to compete for it — not because they're known to be healthy. That gap is the real finding; see Gaps.

## Handoff

- Owner: maintainer (solo)
- Signal to watch: count of external contributors reaching a second merged PR (dated raw list, not a rate — volume is too low for one)
- Re-read: 2026-12-18 (90 days out), or sooner if a docs rewrite or CONTRIBUTING.md change ships first

## Gaps

Signal coverage: 2 of 7 stages carry a real value (29%) — below this skill's own 60% target. Shipping anyway, per the skill's own rule: an honest map with holes beats a complete one with invented numbers.

What would close each gap, cheapest first, all readable from data you already hold, no new instrumentation:

1. **Submit vs. Survive review** — split "2 outside PRs a quarter" into opened vs. merged. Pulls straight from `gh pr list --state all --json state,author,createdAt,mergedAt`.
2. **Survive review** — compute median time from PR open to first maintainer response from the same PR timestamps. This is the number the GitHub citation says predicts return.
3. **Find work** — tag currently-open issues by whether a newcomer claimed and then vanished; needs nothing but reading issue comment history.
4. **Return** — build the dated list of any contributor with ≥2 merged PRs, all-time, from `git shortlog` or the contributors API.
5. **Land / Set up / Change** — stay dark until a friction log exists. Cheapest fix: have the next first-time contributor (or you, pretending to be one, on a clean machine) keep one, per the protocol in this skill's evidence reference.

Next: run item 2 above — it's one `gh pr list` command and it's the single number the leak diagnosis leans on hardest.