**Next action (20 min, today):** find out who owns the package and the `@brindlewood` scope on npm. Run `npm owner ls @brindlewood/ledgerkit` and `npm org ls brindlewood`. Everything below depends on that answer.

I didn't have repo access, and the skill's six-question interview wasn't possible in a one-shot answer. So I inferred the answers from what you wrote and marked every number as an estimate. Replace the estimates with your real counts before you commit the plan.

---

# Sustainability plan: @brindlewood/ledgerkit, 2026-10-23

## Destination

**Same project, about 8 h/week (20% of a 40 h week) instead of about 24 h, by 2026-12-04 (6 weeks).** I picked this from your "I don't want to leave" and your 20% target. Sharing the load (a second maintainer) is the lever that keeps it there.

## Why your manager's advice isn't enough

"Timebox it and let the backlog be" is half right. Cap your hours, but that alone fails here:

- **Escalations are not backlog.** They come from about 40 customer integrations, and each one is a company waiting. If you timebox without telling anyone, those customers see silence and escalate harder.
- **There is no published contract.** Nobody outside knows your hours, your reply window or your scope. Your 60% is inflow times unstated expectation.
- **This is a staffing decision.** The company adopted the repo, so a 20% budget with 60% demand needs a second maintainer or a scope cut. Both are your manager's calls. Your manager can only make them if you show data.

## Ledger

Fill the blanks from the repo's Insights and issue search. The 30-minute pull is step 2 below.

| Item | Value |
|---|---|
| Inflow | ___ issues/PRs per month (estimate until pulled) |
| Backlog split | ___ waiting on reporter / ___ waiting on you / ___ confirmed bugs / ___ feature requests |
| Hours now vs budget | ~24 h/week vs 8 h/week |
| Top drain (inferred) | Customer escalations arriving as issues, so support work on the tracker |
| Transition hours | About 30 h over 6 weeks, ending 2026-12-04. See Moves for the breakdown. |
| Concentration | **Critical.** You hold the publish rights, from a personal npm account. |

The ledger also shows the shape. About 60k weekly downloads with probably one or two real contributors is Eghbal's "stadium". Contributors won't appear on request, so cut the contract and the intake first and recruit second.

## Moves

The order is re-ranked from the default using your answers:

- **Employer-paid maintainer** moves the credentials fix to first. Do it before any role change.
- **Escalation drain** adds a new move, "route escalations", straight after the contract.
- **Co-maintainer** moves up because the company can give you one.
- **Funding** is dropped. You are already paid, and donations don't reduce inflow.

| # | Move | Effort | Buys | Ships |
|---|---|---|---|---|
| 0 | **Move publish rights to company ownership** | 2 h | Ends the single-key risk | 2026-10-30 |
| 1 | **Publish the contract** | 1 h | Every customer and user calibrated at once | 2026-10-30 |
| 2 | **Route escalations off the tracker** | 3 h plus one meeting | Customer pressure stops landing on you | 2026-11-06 |
| 3 | **Declare maintenance tier and scope** | 3 h | Feature requests close by pointer | 2026-11-06 |
| 4 | **Cut intake** (issue forms, questions to Discussions) | 4 h | Fewer items arrive | 2026-11-13 |
| 5 | **Automate release chores** | 8 h | Releases stop costing evenings | 2026-11-20 |
| 6 | **Announced backlog reset** | 8 h | The guilt pile is gone | 2026-12-04 |
| 7 | **Ask the manager for a co-maintainer**, then mentor them | Ask now; mentoring runs for months | The only move that compounds | Ask by 2026-11-06 |

The transition total is about 29 h plus the mentoring. That is above your 8 h/week steady state, so treat it as a dated bridge. Ask your manager to approve about 5 extra hours a week until 2026-12-04, then the budget drops to 8 h.

**Move 0: credentials.**

1. If you are the only owner, run `npm owner add <second-company-maintainer> @brindlewood/ledgerkit`. Do this even before the scope question is settled.
2. If the package sits under your personal account rather than a company-owned `@brindlewood` npm org, transfer it to the org. You must stay reachable while this happens.
3. Move publishing to CI with npm trusted publishing (OIDC from GitHub Actions) and provenance. After that no personal token publishes anything.
4. Revoke your personal automation tokens. Keep your own account alive with 2FA.
5. Also check the GitHub org: at least two owners, and your personal fork or admin rights are not the only path.

This is not a trust problem. It is the "repo transferred, package not" failure mode, and it also means you can't take a holiday or leave your job without stranding 40 customers.

**Move 2: route escalations.** Make this the main change.

1. Agree with support/CS that customer problems enter through a support ticket, not a GitHub issue.
2. Support triages first. Only a confirmed SDK bug reaches the repo, as an issue with a minimal reproduction, linked to the ticket.
3. Give the 40 integrators one named escalation path for true emergencies (a production outage). Write down who answers and what counts.
4. Agree on what the company promises customers (support SLA) versus what the open-source project promises (the contract below). They must be different documents.

**Move 5: automation.** Do grouped dependency updates, release tooling (changesets or release-please) and publishing from CI. Review the bots' output; that is the cost.

**Move 6: backlog reset.** Run it once, announced a week ahead, labelled `backlog-reset`. Close old items without a reproduction and without activity. Keep confirmed bugs and any issue linked to a customer ticket. Expect some angry replies and answer only through the reopen rule. This overrides "let the backlog be" for one reason: an unannounced pile keeps generating guilt, and an announced sweep ends it.

## Contract

Commit this to the README after you edit the numbers:

```markdown
## Project status

**Maintenance-only for the 1.x line; new features are considered quarterly.**

- Maintained by Brindlewood Systems, about 8 hours a week across the team.
- Expect a first reply to issues within 10 business days; a reply is not a promise of a fix. Security reports: see SECURITY.md.
- In scope: bug fixes, security fixes, compatibility with supported Node.js and TypeScript versions. Not in scope: <your list, e.g. new transport layers, runtimes past end of life>.
- Questions go to GitHub Discussions, not the issue tracker.
- Brindlewood customers: contact support. Do not use GitHub issues for urgent production problems.
```

**Check the window against the formula.** Replies per week = 8 h × 60 × share on the tracker ÷ 15 min per reply. At half the time on the tracker that gives 16 first replies a week, or about 64 a month. Your 8 h also has to cover code, review and releases, so the real tracker share is probably smaller. If your pulled inflow exceeds about 60 a month, cut intake harder before you publish a 10-day window. These defaults (half the time, 15 minutes) are self-set, not measured.

Pick a window you can keep. A missed window means the window was wrong, so widen it publicly.

## People

1. **Ask your manager this week** for a named second maintainer with a defined number of hours (4 h a week is a sensible start). Bring the ledger, the contract and the escalation data. Ask for either a second person or an agreed scope cut.
2. **Candidates, in order:** a teammate who already reviews your PRs, a support engineer who knows customer cases, or an engineer at one of the 40 integrator companies who already contributes.
3. **Access stages, months apart:** triage and review first. Merge after a release made together. Publish rights last, only after a supervised release, and never in the same step as merge.
4. **Red flag:** anyone, especially a newcomer with little history, who pushes for publish rights early. Decline in writing and keep reviewing their PRs.

## Exit

Not applicable. You are staying. For the record, the single-key fix in move 0 is what makes any future exit safe.

## Review

- **Re-read the ledger on 2026-12-04**, at the end of the bridge. Compare actual hours with 8 h/week.
- **Look earlier if** hours stay above 12 h/week for two weeks, the 10-day window is missed for most new items, or a customer escalation bypasses the support route twice.

## Health check

| # | Check | Status now |
|---|---|---|
| 3 | Two holders per publish right | **Fails.** Fixed by move 0. |
| 4 | README states the end state | **Fails.** Fixed by move 1. |
| 5 | Someone is named for security reports | **Unknown.** Put a name in `SECURITY.md` and enable GitHub private vulnerability reporting. |
| 1 | Hours within budget four weeks after the plan | Check on 2026-12-04. |
| 2 | Published window met for most new items | Check on 2026-12-04. |

Checks 3, 4 and 5 must pass before the plan counts as done. Checks 1 and 2 are for the review date.

## Order of work, starting now

1. Today: run the two npm ownership commands above and write down what you find.
2. This week: pull the ledger numbers from the repo (30 min) and book 30 minutes with your manager.
3. This week: add a second npm owner, commit the contract, and send the manager the staffing ask with the ledger attached.
4. By 2026-11-06: agree the escalation route with support/CS.
5. By 2026-12-04: finish moves 3 to 6, then re-read the ledger.

**Estimate:** moves 0 to 2 take about 6 h in total and give the biggest drop in drain.