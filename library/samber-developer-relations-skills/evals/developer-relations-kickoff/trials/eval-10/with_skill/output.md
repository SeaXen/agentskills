Using the **developer-relations-kickoff** skill to route this and produce the actual kickoff deliverable for Plimsoll.

---

## Detection

No `devrel-context.md` in the described project → **cold start**. I have no filesystem/git access to the real Plimsoll repo (this session only has your description), so detection is limited to what you stated — no guessing beyond it.

## Interview — answered from your message, capped at 7

Cold start normally asks up to 7 questions. Your message already answers all but one, so I'm not going to re-ask what you told me — flagging each as detected vs. inferred:

- **Surface (Q1):** open-source project is the dominant one this session — release cadence, tag events, and the issue backlog are the load-bearing facts. Community and events are secondary facets, not the primary fork. *(Detected — this changes where the release-tag routine ranks; see Routines.)*
- **Session goal (Q2):** stop releases, CFP deadlines, and the backlog from falling through — matches the project's standing goal, nothing here is already decided-and-closed.
- **Who adopts/pays (Q3):** MIT, no revenue or company mentioned → non-commercial OSS, no buyer. *(Inferred — correct me if Plimsoll has a commercial arm.)*
- **Funded driver (Q4):** contributor community — the entire ask is about maintainer capacity and an unowned backlog, not adoption or sales. *(Inferred.)*
- **Stage (Q5):** one person doing it part-time — three maintainers, only you touch anything non-code.
- **Constraints/date (Q6):** maintainer hours only; hard date = CFP season opens **~2026-10-10** (three weeks from today, 2026-09-19).
- **Horizon/ceiling (Q7):** standing, a few hours a week — you explicitly asked for recurring automation, not a one-off fix. Sign-off: you.

Only real open question, not answerable from your message: **who, if anyone, is willing to own issue-triage follow-through.** Your own phrasing — "nobody wants to be [assigned]" — reads as nobody, including you, which I'm treating as the answer rather than asking it as a question. It changes the routines below.

## Route

The immediate ask — "set up whatever recurring automation you can" — doesn't hand off to one sibling skill. It's what this kickoff's own **§7 Routines** step exists for, so that's what's running below, not a stretch-fit onto a sibling.

If you also want the backlog's underlying *system* designed today (not just automated later), that's a one-off session with `samber/developer-relations-skills@oss-issue-triage` — separate from, and a prerequisite to, ever automating a queue review.

## Short-list

Non-commercial OSS (Q3) deletes `devtools-pricing-strategy`, `devtools-business-model`, `developer-first-gtm` entirely — not parked at the bottom, removed. Same deletion is reinforced by the contributor-community driver (Q4).

1. **`samber/developer-relations-skills@oss-issue-triage`** — 340 unassigned issues nobody wants is the single biggest named cost. Cost: one design session for labels/staleness policy; note the *recurring review* stays unautomated until someone owns it (see Routines).
2. **`samber/developer-relations-skills@changelog-writing`** — lines up exactly with the Thursday tag cadence and your tag-push trigger. Cost: near-zero once wired; one glance per release.
3. **`samber/developer-relations-skills@conference-cfp-submission`** — promoted for the season: three weeks to opening, and a missed CFP window is gone for a year. Cost: one focused session against a fixed external clock.
4. **`samber/developer-relations-skills@oss-governance`** — promoted for non-commercial OSS. "Three maintainers, only I do anything non-code" is a bus-factor problem the automation below doesn't fix, only papers over. Cost: a negotiation among all three of you, undone only by another negotiation.
5. **`samber/developer-relations-skills@oss-sponsors-fundraising`** — promoted for non-commercial OSS. 11k stars and a live Discord are real fundraising leverage; money is the actual fix for "only I do non-code work." Cost: a program-design session plus a standing invoice/rewards cadence.
6. **`samber/developer-relations-skills@developer-champions`** — 900 Discord members is unused capacity that could absorb community and light triage load. Cost: months of lead time before a first cohort is productive — a bet, not this month's win.

## Chain

One genuine dependency, not a fabricated sequence: **`oss-issue-triage` → `oss-governance`**. The triage design hands over exactly who (or what policy) has decision rights over an unassigned issue — that's the input `oss-governance`'s contributor-absence-factor and role definitions need; it can't be decided before the triage system names the problem precisely.

## Not now

- **`samber/developer-relations-skills@developer-live-demo-design`** — once a CFP is actually accepted. Designing a demo runbook for a talk that doesn't exist yet is premature, even though the season is opening.
- **`samber/developer-relations-skills@developer-community-health`** — once the Discord has a measured baseline (the day-90 convention `developer-community-launch` sets). Nothing you described suggests one exists for the 900-member server.
- **`samber/developer-relations-skills@devrel-team-structure`** — once `oss-governance` produces an actual decision to formalize roles. Premature before that conversation happens.

## Gap

⚠️ **Maintainer burnout as a subject of its own is not covered by this collection.** `oss-governance` covers succession and bus-factor *insurance* (who takes over if you stop), but nothing here addresses the workload itself — one person carrying all non-code work across release comms, community, and a 340-issue backlog is a burnout risk today, not just a continuity risk later.

## Context artifact

No real Plimsoll repo exists in this environment, so I can't commit `devrel-context.md` — here's its content to drop at your project root yourself:

```markdown
# DevRel context

_Last updated: 2026-09-19_

## Product and audience

- Product: Plimsoll, an open-source observability agent.
- Adoption motion: non-commercial open-source, no buyer.
- License: MIT. ~11k stars.

## Program

- Funded driver: contributor community.
- Stage and team: three maintainers; one (you) does all non-code work — docs, community, release comms, triage.

## Surfaces owned

- Repository: tags a release most Thursdays.
- Community: Discord, ~900 members.

## Measurement

- None reported yet. Blind spot: no Discord activity baseline, no backlog-trend tracking.

## State

- In flight: setting up recurring automation for releases, CFP, and backlog visibility (this session).
- Decided: automation should be standing, not one-off; a few hours a week is the ceiling.
- Open: who (if anyone) owns issue-triage follow-through; whether to formalize maintainer roles via oss-governance.
- Constraints: maintainer hours only; CFP season opens ~2026-10-10.

## Stakeholders

- You — sole non-code maintainer, sign-off on anything non-code.
- Two other maintainers — code only; decision rights on code changes.

## Session log

- 2026-09-19 - "set up recurring automation so releases/CFP/backlog stop falling through" → this kickoff's §7 routines (release-tag pass, CFP sweep, kickoff re-invocation) + short-listed oss-issue-triage, changelog-writing, conference-cfp-submission, oss-governance, oss-sponsors-fundraising, developer-champions.
```

## Routines — dry-run, nothing created yet

No routines exist yet for Plimsoll (first kickoff run), so there's nothing to retire. Ranked by **value per unit of standing effort**, not by cheapness:

```
Routine: release-tag documentation pass
Trigger: on push of a tag matching v* to the Plimsoll repo
Runs: samber/developer-relations-skills@changelog-writing
Output channel: drafted GitHub Release body attached to the tag, held for one maintainer glance before publishing
Cost: one short review pass per release
First fire: next tag push (likely 2026-09-24, this Thursday)
```

```
Routine: CFP deadline sweep
Trigger: weekly schedule, for the duration of the season (no repo event fires on "a CFP window opening")
Runs: samber/developer-relations-skills@conference-cfp-submission
Output channel: weekly message to you listing that week's open CFP deadlines against Plimsoll's talk angles
Cost: a short read every week during the season, plus one drafting session per event pursued
First fire: 2026-10-06 (ahead of the ~2026-10-10 opening — review lead times run longer than they feel)
```

```
Routine: kickoff re-invocation
Trigger: monthly schedule (matches Plimsoll's weekly-release pace better than quarterly)
Runs: samber/developer-relations-skills@developer-relations-kickoff
Output channel: short state-summary message to you, plus an appended session-log line in devrel-context.md
Cost: near-zero — a five-line read and a re-rank, not a new interview
First fire: 2026-10-19
```

**Ranking, stated out loud:** release-tag pass leads — it's the only one of the three whose output reaches users *before* the next Thursday's release ships rather than after someone hits breakage, at near-zero marginal cost since the tag already fires weekly. CFP sweep is promoted above its usual third slot because the three-week runway is a hard, non-recoverable deadline — miss it and that stage is gone for a year — which outweighs the kickoff re-invocation's lower cost. The kickoff re-invocation stays in, third, *not* first: it's the cheapest of the three, but cheap and first-in-line are different orderings, and its job is to keep the other two calibrated, not to replace them.

**Withheld, not proposed:** an issue/PR **queue review** routine. It would normally sit here too, but installing a recurring review against a backlog nobody has agreed to own doesn't fix anything — it just adds a fourth thing that quietly stops getting read. Design the triage system first (`oss-issue-triage`, one-off, above) — a staleness policy and label taxonomy can shrink 340 issues without needing a human assignee on each one — then add this routine once someone, even you part-time, explicitly claims the follow-through.

## Memory

Nothing here falls in the excluded categories (no PII, no embargoed news, no NDA figures) — but I'm not writing this to your actual persistent memory store, since Plimsoll isn't the real project this session's memory is scoped to (that's `example-org/example-repo`). Treat the `devrel-context.md` block above as the source of truth; if Plimsoll is a real project you want tracked across sessions, say so and I'll persist the durable facts from it properly.