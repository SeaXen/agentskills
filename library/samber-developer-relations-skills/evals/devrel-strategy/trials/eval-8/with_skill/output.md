Using **devrel-team-structure** for the org chart and **devrel-strategy** (Step 6, leverage programs) for the contributor-program call. One flag up front: your ask ("org chart... roles, reporting lines, ratios") is explicitly routed by devrel-strategy's own scope note to devrel-team-structure — that's the skill actually driving this, not the one you named.

Both skills refuse to draw a chart before an interview and a work inventory exist. I don't have either from you, so this draft runs on stated assumptions instead — flagged with ℹ️ everywhere they carry real risk if wrong. Validate the ℹ️ list before this goes in front of your VP; everything else is derived and should hold regardless.

---

# DevRel org design brief — Perrix, 12-month horizon

## Assumptions this brief runs on (confirm before Friday)

ℹ️ **Current 6-person roster** — you didn't give me the breakdown, so I've inferred a typical shape for a devtool that grew DevRel 1→6 via content/advocacy: Head of DevRel, 2 Developer Advocates, 1 Technical Writer, 1 DX Engineer, 1 DevRel Ops/Analytics generalist. If this is wrong, the sequencing below changes — the whole argument hinges on advocacy already being your best-covered pillar.

ℹ️ **Funded driver** — not stated. I've assumed *developer adoption* (awareness + activation among individually-signing-up engineers), because that's what a community manager + 2 advocates + educator hiring plan optimizes for. If the VP's real answer is *product input* or *enablement for an enterprise motion*, the reporting-line recommendation below flips — see the decision rule.

ℹ️ **Audience path** — assumed primary = individual-developer adoption (self-serve branching, PLG-shaped). If company/platform-team evaluation is actually the growth engine (likely once branching touches production data, security review), the Q3–Q4 hires should shift toward enablement/DX-engineering, not a third advocate.

ℹ️ **CLI license status** — unconfirmed whether Perrix's CLI is open source today. This blocks the contributor program entirely, not just delays it — see Leverage Programs below.

---

## Reporting line — recommend staying in marketing, not moving to product

Your instinct is to move the whole team to product. Running it against the decision rule (name the driver → name the leader who owns it):

- The four hires you're planning — community manager, 2 advocates, developer educator — are awareness, retention and enablement roles. That's exactly what the **marketing** line optimizes for (reach, distribution, campaign integration) and exactly what the **product** line starves (awareness spend, distribution muscle — product orgs rarely hold a promotion budget).
- Product's upside — feedback loop, roadmap proximity — isn't what this hiring plan buys. If proximity to roadmap were the real goal, the plan would be embedding a DX engineer per squad, not hiring a community manager.

**Recommendation: keep the line in marketing this horizon.** Marketing's characteristic failure is advocates getting absorbed into pipeline support (webinars, gated assets, lead targets) — the counter-move, not a change of parent:

- Written product interlock with a standing roadmap slot (owner: Head of DevRel + a named product counterpart).
- Hard rule: no DevRel surface carries a lead-gen gate.

**Trigger to revisit product as the line:** the funded driver shifts to product input, or the CLI contributor program (once launched) becomes a named primary bet feeding the roadmap directly. Don't move the org to chase a program that doesn't exist yet.

⚠️ If the VP's actual stated reason for funding this team next year is "we need product feedback from developers," override this and go with product — the rule above says to follow the driver's owner, not my guess at it.

## Shape — stay centralized all 12 months

At 10 people by Q4, Perrix sits exactly at this skill's own threshold ("under roughly ten full-time people, centralized only — every other shape spends headcount on coordination"). Split, embedded and hub-and-spoke all require staffing floors you won't clear until well past this horizon (hub-and-spoke needs a hub of 2–3 *plus* two spokes; split needs ~8 per side).

**Don't pre-design a shape change for this chart.** Schedule the next devrel-team-structure review for the start of next year — crossing 10 is itself one of this skill's standing re-org triggers, and you'll hit it right as this plan ends.

## Work inventory — build this before the chart is final

I can't populate the real version (owner, hours/week, what breaks if it stops, per surface) without your data. Minimum surfaces to run through it: docs set, CLI, quickstart, blog, community venue (if any exists today), changelog, SDKs/client libraries, event calendar, champions cohort. Any surface that comes back "unowned" or "informally absorbed by someone with a different title" changes the hiring order below — that's the actual justification a re-org needs, not a template.

## The chart

```
Head of DevRel  (reports to: CMO — see reporting-line decision above)
├─ Senior Developer Advocate — Team Lead     [existing Advocate, promoted Q3]
│   ├─ Developer Advocate                    [existing]
│   └─ Developer Advocate                    [new hire, Q3]
├─ Community Manager                         [new hire, Q1]
├─ Developer Educator                        [new hire, Q2]
├─ Developer Experience Engineer             [existing]
├─ DX Engineer / CLI Maintainer              [new hire, Q4 — dotted line to Engineering]
├─ Technical Writer                          [existing]
└─ DevRel Ops & Analytics                    [existing]
```

10 people at Q4. Head of DevRel has 7 direct reports.

### Hiring sequence, and where it departs from your instinct

| Quarter | Hire | Reports to | Why this slot, not another |
|---|---|---|---|
| Q1 | Community Manager | Head of DevRel | Matches your instinct. Community management is your most cleanly *unowned* function today (0 of 6 FTE vs. 52.7% of surveyed teams staffing it at all) — the clearest gap on the coverage map, no argument needed. |
| Q2 | Developer Educator | Head of DevRel | Matches your instinct, but moved ahead of the 2nd advocate. Developer education is your other clean gap (35.6% industry baseline vs. 0 today), and it's a cheap, reversible, compounding bet (enablement-first archetype: quarter of one person's writing time, near-zero maintenance). It also directly de-risks the contributor program — a real CLI onboarding path is a precondition for external contributors, not a nice-to-have. |
| Q3 | Developer Advocate #3, + promote existing Advocate #1 to Senior Advocate / Team Lead | Team Lead | **Diverges from your plan of "two advocates."** ℹ️ Under the assumed current roster, advocacy is already your best-staffed pillar (2 of 6 people, above the 82.2%-of-teams-have-any-presence baseline in *depth*, not just presence). A 2nd new advocate hire (your plan's 4th and 5th people, both advocates) would concentrate 40% of a 10-person team in the one function least short of coverage. One additional advocate extends reach capacity; the promotion adds a lead so Head of DevRel isn't managing every IC directly. |
| Q4 | DX Engineer / CLI Maintainer, dotted line to Engineering | Head of DevRel | **Not in your original plan — added because the contributor program requires it.** See below: a contributor program with no named maintainer and no review bandwidth is "the one investment worse than not starting." This seat is that precondition, sequenced to land the same quarter you'd otherwise launch the program. |

**If your assumed current roster is wrong** (e.g., you actually have 1 advocate, not 2, or the "6" already includes a community role), re-run this table — the whole argument is "don't add headcount to the pillar you're already deepest in," and that only holds if advocacy really is your deepest pillar today.

## Coverage map (Q4 state)

| Function | State | Owner | Backup |
|---|---|---|---|
| Advocacy | Owned | Sr. Advocate Lead + 2 Advocates | — |
| Community management | Owned | Community Manager | ⚠️ none named — bus factor of 1, assign now |
| Technical writing | Owned | Technical Writer | ⚠️ none named — same risk |
| Developer marketing | Shared, X-as-a-service | Central Marketing owns channels/campaigns; DevRel Ops feeds content | — |
| Developer education | Owned | Developer Educator | ⚠️ none named |
| DX engineering | Owned | 2 DX Engineers (one dual-hatted as CLI Maintainer) | mutual backup between the two |

Three functions land at bus factor 1 the day their sole owner is hired. Name backups (even partial, cross-trained ones) in the same hiring cycle — don't wait for the quarterly review the skill would otherwise force this to surface at.

## Ratios

I'm refusing an advocate-per-developer or advocate-per-signup ratio — every version of that number in circulation is a single-company anecdote, not a standard, and it'll collapse the first time a finance partner asks for the source. Two ratios I'll actually stand behind, both derived, both labeled:

- **Pillar mix at Q4** (from the work inventory above, not a benchmark): Advocacy 30% (3/10), DX engineering 20% (2/10), Community 10%, Education 10%, Technical writing 10%, Ops/analytics 10%, unallocated to central marketing interlock 10%.
- **Span of control**: Head of DevRel → 7 direct reports at Q4. General-management convention (not DevRel-specific — labeled as a sanity check only) puts 5–8 as typical; you're at the top of that band. The Q3 Team Lead promotion exists specifically to keep this number from hitting 9.

## Interlocks

`<team> — <mode> — <what crosses> — <arbiter>`

- Product — collaboration during launches, X-as-a-service otherwise — feedback in, roadmap/dates out — Head of DevRel + named product counterpart.
- Engineering — facilitation, thicker than default because the CLI Maintainer carries a dotted line here — technical review in, writing/demo coaching out — Head of DevRel + Eng manager who takes the dotted-line report.
- Central/growth marketing — collaboration on campaigns, X-as-a-service on distribution — content in, channels/audience data out — Head of DevRel.
- Support — X-as-a-service — failure signals in, troubleshooting content out — Developer Educator.
- Sales — X-as-a-service, strictly — evaluation material out, field objections in — Sr. Advocate Lead.
- Customer success — X-as-a-service — adoption blockers in, enablement material out — Developer Educator.

## Ladder & budget

- Put the team on a DevRel-specific ladder, not borrowed from engineering or marketing — you're crossing from "flat generalist" to a specialized cluster this year, which is exactly when a borrowed ladder starts promoting people against criteria that don't describe their work.
- "Head of DevRel" managing 10 people against company-level goals reads as Director scope, not "Head of" — resolve the title before it becomes a retention problem (Maida's check).
- ⚠️ Open question, ask the VP directly: who owns headcount budget vs. program budget? 60% of surveyed programs exclude salaries from the program budget — don't assume the same person signs both.

## Refused this horizon

- A second community venue beyond the one the Community Manager stands up first.
- An agency-run content pipeline — six-month setup latency doesn't fit a 12-month plan that's already fully committed.
- Embedding any advocate into a product squad — premature below the ~10-person floor that shape needs.
- **Launching the CLI contributor program before Q4** — this is the direct answer to your proposal. See below.

## Re-org triggers for next year

- Funded driver changes, or the VP sponsoring this changes.
- A second team (e.g. growth marketing) starts doing DevRel-shaped work with no declared interlock.
- Community Manager or Technical Writer stays at bus factor 1 for a full quarter after Q1/existing.
- The team declines the same category of request three times for lack of coverage.
- **Headcount crosses 10 — already true at the end of this chart.** Schedule the next devrel-team-structure pass for Q1 of next year, not mid-cycle.

---

# Leverage programs

Scale-stage leverage order (devrel-strategy, Step 6): **champion/ambassador programs > community-run events > paid write-for-us pipelines > contributor programs.** Contributor programs sit last on purpose — they spend maintainer hours nobody can backfill, and they're the least reversible bet on this list once a CLA/DCO is in place and PRs start landing.

Perrix is at the Grow→Scale boundary, not fully into it — one centralized team with emerging specialization, not yet "several specialized teams." Leverage programs belong on the roadmap now, staffed to launch once the specialists exist, not before.

**Recommended sequence:**

1. **Champion/ambassador program — Q2/Q3, owned by Community Manager + Sr. Advocate Lead.** Cheapest leverage bet: it recognizes people already advocating for Perrix, so it multiplies an asset you own rather than building one from zero. Precondition: the Community Manager needs a few months to seed a founding cohort first — you can't recognize champions in a venue that doesn't have density yet.
2. **Community-run events — Q4, once champions exist to run them.** Natural extension of (1); don't staff this as a separate program.
3. **Paid write-for-us pipeline — not this horizon.** Six-month pipeline setup latency (per this skill's build-vs-buy table) doesn't fit inside a 12-month plan that's already fully committed to four hires. Park it for next year's charter.
4. **Contributor program for the CLI — earliest Q4, and only if every precondition below is met.**

## On the contributor program specifically

Your instinct to lead with this is the one place I'd stop you. Ranked last for a reason that applies directly here: "recruiting contributors into a review backlog damages the project's reputation" — and today you have no named maintainer with review bandwidth. Launching before the DX Engineer/CLI Maintainer seat exists (Q4 in the chart above) means external PRs land with nobody accountable for reviewing them.

**Preconditions, in order:**

- ⚠️ **Confirm the CLI is actually open source, under a real license, today.** If it isn't, this isn't a "launch a program" decision, it's an OSS licensing/governance decision first — hand off to oss-license-strategy and oss-governance before staffing anything.
- A CLA or DCO decision, documented, before the first external PR lands — this is the least reversible commitment in the whole build-vs-buy menu; a merged contribution can't be un-licensed.
- The Q4 CLI Maintainer seat filled and actually has review bandwidth, not review time squeezed out of an already-full DX engineer.
- First-contribution path: curated starter issues with real mentoring, a reproducible dev environment, published triage/response-time targets.

**Signal to track once live:** first-response time on issues and PRs, repeat contributors in the following quarter. Not stars, not raw PR count — those measure hits, not the behavior the program is actually for.

**Bet card for the charter:**

| Bet | Goal served | Owner | Signal | Review date |
|---|---|---|---|---|
| Champion program | Retention, referral | Community Manager | Champions active per quarter | End of Q3 |
| Contributor program (CLI) | Product, referral | DX Eng/CLI Maintainer | First-response time on PRs; repeat contributors next quarter | End of Q1 next year |

---

## Quality-gate self-check

Structural, per devrel-team-structure: reporting line names a driver/leader/starved-pillar/coverage (✅, with the driver itself flagged ℹ️ assumed); shape justified by coordination bought, not company-size mimicry (✅); all six functions have a coverage state (✅); three surfaces flagged bus-factor-1 rather than hidden (✅); one interlock mode per adjacent team with a named arbiter (✅); no headcount ratio quoted as benchmark, none refused-but-invented (✅); re-org triggers non-empty (✅).

Per devrel-strategy Step 6/quality gate: refused list is non-empty and includes something you wanted to do now (✅ — the contributor program, deliberately delayed); every bet has one owner, one signal, one review date (✅).

Numeric baselines moved from this skill's defaults: none — span-of-control and pillar-mix are used as sanity checks only, labeled as general-management convention, not DevRel data.

**Biggest single risk to this chart:** the current-roster and funded-driver assumptions. If either is wrong, re-run the sequencing table — the structure (centralized, marketing line, 10 people) is fairly robust to both; the *hiring order* is not.