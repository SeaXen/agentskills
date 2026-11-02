Ran the developer-relations-kickoff skill (`skill-wip/samber/developer-relations-skills/skills/developer-relations-kickoff`) against your brief. No `devrel-context.md` exists and there's no Halberd Metrics repo to detect against, so this is a cold start — I've extracted interview answers directly from what you gave me instead of asking them back one by one. Flagging that explicitly so you can correct anything I read wrong:

- **Surface (Q1):** company-wide kickoff, not one surface — matches the "first DevRel hire, no idea where to start" case, which routes to a chain, not one skill.
- **Who adopts, who pays (Q3):** both — individual engineers self-serve in, AEs close enterprise deals with VP Eng signing.
- **Funded driver (Q4):** ⚠️ your CEO named all seven — adoption, sales enablement, developer enablement, product feedback, ecosystem, contributor community, employer branding. Naming all seven is the same as naming none. This is the one answer that reorders everything below.
- **Stage (Q5):** solo, full-time, nothing formal built yet.
- **Constraints (Q6):** $60k/year, engineering available on ~1 week notice (not zero, not on-demand), no hard external date beyond starting Monday.
- **Horizon / sign-off (Q7):** standing role, not a one-off; CEO is the only named stakeholder with sign-off.

## Bottom line

🎯 Don't touch tactics in week one. Spend it forcing your CEO to cut seven drivers down to one or two, with the other five put in writing as refused-for-now. Everything else — docs, content, community, events — is a rounding error next to that decision, because right now nothing you ship can be judged a success or failure against anything.

## The chain (do these in order — each hands the next one something real)

1. **`developer-segmentation`** — Cut "developers" into the two audiences your brief already implies: self-serve individual engineers, and VP-Eng buyers the AEs sell to. Add an explicit anti-segment. Hands off: named, sized segments against your existing $2.4M ARR split.
2. **`devrel-strategy`** — Bring the segments and your CEO's seven-item list into one session with him. Force 1-2 funded drivers, write the other five down as refused, set the pillar mix (advocacy/marketing/enablement/community weights). Hands off: a charter you can hold him to.
3. **`devrel-budget-allocation`** — Split the $60k into line items against the chosen driver(s), with a threshold and a cut list. $60k split seven ways is $8.5k each — fun ds nothing. Split one or two ways it's a real program. Hands off: a spend plan.
4. **`devrel-metrics`** — Pick which numbers get a target, given the driver you just picked (self-serve trial-to-paid if it's adoption; AE-assisted cycle time or time-to-technical-win if it's enablement). Hands off: what your first quarterly review is judged on.
5. **`devrel-content-calendar`** — Plan the quarter's content against real anchors (a release, a conference, an AE ask) instead of whatever seems good that week.

## Short-list, ranked by value returned per hour spent

1. **`devrel-strategy`** — bottleneck: seven named drivers, zero prioritization; nothing downstream can be judged until this happens. Cost: one CEO working session, no budget, no engineering.
2. **`developer-segmentation`** — bottleneck: "developer" is being treated as one buyer when your own brief describes two. Cost: one session over existing signup/deal data, no engineering.
3. **`developer-journey-map`** — bottleneck: walks into the strategy conversation with evidence instead of the CEO's hunch — where the self-serve funnel actually leaks, where AE-assisted deals actually stall. Cost: one session over analytics plus a couple of AE interviews.
4. **`readme-optimization` + `developer-quickstart-guide`** — bottleneck: most of your signups are bottom-up; whatever they hit first decides if they bail before an AE ever sees them. Cost: an editing pass and one merged PR, no budget, no sign-off, reversible by another commit.
5. **`developer-case-study`** — bottleneck: your two AEs are already closing six-figure deals on something; a written technical case study turns one AE's war story into reusable proof for the other. Cost: one customer interview plus a write/review cycle, contingent on a customer willing to be named. Directly serves "sales enablement" if that survives as a chosen driver.
6. **`devrel-metrics`** — bottleneck: without an agreed number, every result this year gets re-litigated. Cost: one session, but it depends on the strategy session landing first.
7. **`devrel-budget-allocation`** — bottleneck: $60k unallocated across seven asks funds nothing. Cost: one session, same dependency.

## Not now

- **`tech-employer-branding`** — unblock: only if employer branding is one of the 1-2 drivers the CEO actually funds, or a recruiting budget exists outside this $60k.
- **`developer-community-launch` / `oss-contributor-onboarding`** — unblock: once you confirm there's a public repo or OSS surface (client libraries, exporters, a Grafana/Prometheus-style integration) worth building a community around. Your brief mentions "contributor community" as a CEO ask but never says anything is actually open source — check that this week.
- **`devrel-team-structure`** — unblock: once a second DevRel hire or the budget for one is on the table.
- **`developer-community-health`** — unblock: no community exists yet; there's no baseline to trend against.
- **`conference-cfp-submission` / `developer-event-sponsorship`** — unblock: once a specific event is named and a travel line survives budget-allocation. At $60k, this will compete hard with everything else.

## Gap — nothing in this collection covers

- **Sales collateral itself** (decks, one-pagers, objection handling for the AEs) — that's the separate `sales-enablement` skill, not part of this 55-skill collection. Run it after `devrel-strategy` and `developer-case-study` give it real material, not before.
- **Turning developer feedback into a roadmap input.** `developer-journey-map` surfaces friction and `developer-community-health` surfaces sentiment once a community exists, but neither is a mechanism for feeding engineer feedback into product decisions. If "product feedback" survives the strategy cut, tell your CEO this piece has to be built by hand.
- **The exec-facing DevRel report / budget defense narrative** — no skill in the collection writes that; you'll be improvising your first quarterly review.
- (Not a gap, but worth knowing it exists: `devrel-hiring` covers hiring a second DevRel person when that budget shows up.)

## `devrel-context.md` — save this at your project root once you have a repo to put it in

```markdown
# DevRel context

_Last updated: 2026-09-19_

## Product and audience

- Product: time-series database. 40 people, $2.4M ARR.
- Adoption motion: both — individual engineers self-serve in; two AEs close six-figure deals with VP Eng sign-off.
- Primary segment, secondary segment, anti-segment: not yet cut — first action item (`developer-segmentation`).

## Program

- Funded driver: not yet decided. CEO named all seven (adoption, sales enablement, developer enablement, product feedback, ecosystem, contributor community, employer branding) in the kickoff brief — forcing a choice is the first deliverable.
- Pillar mix: not yet set — depends on funded driver.
- Stage and team: one person (new hire), full-time, starting 2026-09-21 (Monday).

## Surfaces owned

- Docs: unknown — audit in week 1.
- Repositories: unknown whether anything is public/OSS — confirm in week 1, gates `developer-community-launch` and `oss-contributor-onboarding`.
- Community: none yet.
- Events: none committed.
- Content: none yet.

## Measurement

- Metrics currently reported: unknown — confirm what marketing/sales already track before assuming a blind spot.
- Known blind spots: none confirmed yet.

## State

- In flight: nothing.
- Decided: nothing yet — start date only.
- Open: which 1-2 of the CEO's seven drivers actually get funded; whether any product surface is or should be open source.
- Constraints: $60k/year budget; engineering time available with ~1 week notice; no team beyond this hire; no hard external date beyond start.

## Stakeholders

- CEO — sole sign-off on program driver and budget.
- Two AEs — own the enterprise deal motion; primary source for `developer-segmentation` and `developer-case-study` input.

## Session log

- 2026-09-19 - "first DevRel hire, where do I start" → `developer-relations-kickoff` → chain routed: segmentation → strategy → budget-allocation → metrics → content-calendar. Artifact created.
```

## Proposed routines (dry run — nothing created yet)

```
Routine: monthly kickoff re-invocation
Trigger: schedule, first Monday of each month
Runs: developer-relations-kickoff
Output channel: this devrel-context.md, updated in place
Cost: near-zero, keeps this plan from going stale
First fire: 2026-10-05
```

```
Routine: release-tag documentation pass
Trigger: on push of a tag matching v* — PENDING, confirm Halberd Metrics actually cuts versioned releases with a changelog surface before enabling
Runs: changelog-writing
Output channel: draft pull request on the release branch
Cost: one review pass per release
First fire: TBD once release cadence is confirmed
```

That's rungs 1-2 by default given solo stage — add a CFP sweep only once a specific conference is targeted, and a triage routine only once there's a repo with an issue queue to own.