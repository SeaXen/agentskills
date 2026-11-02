Using the `oss-governance` skill (steps 1–8, its interview inference rule, and its own output template) to produce the governance review below.

---

# Governance review — Thornfield

## As-is — who decides today, by what implicit rule, where it has failed

- One monorepo, six top-level components (core runtime, CLI, web dashboard, Terraform provider, Helm charts, VS Code extension), six maintainers.
- Inferred, confirm before finalizing: all six hold merge rights repo-wide, since all six work across all six directories — no per-directory routing exists today.
- The implicit rule filling that vacuum: nothing is delegated, so every change defaults to needing broad buy-in. That's a maintainer council missing the two things a council needs — a lazy-consensus default and named area delegation — not a law anyone wrote down.
- Missing: a deadlock rule, a promotion path for the ~4 regular outside contributors, per-component release ownership.
- Unconfirmed, ask directly: employer spread across the six; who holds release-signing/publish credentials per component (npm, Terraform Registry, Helm repo, VS Code Marketplace, container registry, domains).

## Concentration — absence factor, employer spread, credential holders

- Contributor absence factor: not computed from real history here — run it from `git shortlog`/CHAOSS before committing this document. Six active maintainers sharing six directories roughly evenly would land comfortably above 1 project-wide, but check per directory too; "we all work everywhere" is a self-report, not a measurement.
- Outside contributors: ~4 regular, **project-wide**, not per directory — this number decides the federation question below more than the absence factor does.
- Credential inventory: not available — open action item (see Enforcement).
- Gate 1 (absence factor of 1 blocks every shared model): likely not triggered, pending measurement.
- Gate 2 (components without their own contributor communities block federation): **triggered.** Six directories, one shared maintainer pool, one shared 4-person outside-contributor pool. Nobody described a CLI community distinct from a Helm-charts community.

## Recommendation — model chosen, alternative considered, monthly hours and what they buy

Federation, as asked for, fails gate 2 before it reaches the efficiency ranking. Kubernetes' SIG model works because each SIG already has its own contributor base that doesn't need the others to ship. Thornfield has one team spread across six directories and four outside contributors not described as clustering by directory either. Federating here means writing six charters for six communities that don't exist yet — "wrong as a starting point, because it multiplies process before there is anyone to govern." By Eghbal's taxonomy, Thornfield is a **stadium at best, more likely a club** (few contributors, however many users) — federation is the quadrant for many contributors split into several stakeholder groups, which this isn't.

**✅ Recommended — maintainer council + delegated area owners.**
Matches the model catalogue's own fit row: "3-8 maintainers, one shared area → maintainer council." Thornfield has one shared area in practice, despite six folders, because all six maintainers work across all six. Add delegation, not a second governance layer: name 1-2 area owners per directory (rotating among the same six — nobody new to find) who route reviews and decide routine changes inside their area, reporting back rather than deciding in isolation forever. This is the actual fix for "every change needs everyone" — the problem is nothing's delegated, not that there are too few governance bodies.
Cost: about an hour a month of council process, no standing meeting, reversed by one vote if it doesn't work — fits the 2-hours-a-week ceiling with room left for real review. Buys: a deadlock rule, a promotion path for the 4 outside contributors, area-routed reviews.

**Alternative considered, not recommended now — federated subprojects (the original ask).**
Cost: about a week per charter to install — six charters, ~6 person-weeks one-off — then a standing job per SIG afterward (cadence, charter upkeep, SIG leads), on top of the top-level council itself. That recurring load alone likely exceeds 2 hours/week/person once six SIGs are running, before counting normal review time. Buys: cross-component deadlock resolution and nothing else — a problem nobody reported. The reported problem is a review bottleneck; federation doesn't fix that, it federates the bottleneck six ways.
Revisit trigger, not a rejection forever: charter exactly one subproject, as an experiment with a review date, the day a specific directory (most plausibly Terraform provider or Helm charts — furthest in skill set from the other four) grows outside contributors who don't touch the other five. If the council still makes all the decisions for that component, the split was premature — undo it.

Q10 (2-hour/week ceiling) is what moves this ranking — it's the answer that deletes federation outright rather than just demoting it. No hard deadline was given (Q11), so nothing pulls the other way. Q12 (compounding structure vs. one-off patch) argues for writing council-plus-delegation properly now, not for the heavier model — gate 2 rules that out on structural grounds regardless of ambition.

## Decision rules — per class: who decides, threshold, timer, escalation

| Class | Decider | Mechanism | Timer | Escalation |
|---|---|---|---|---|
| Routine change (single directory) | area owner(s) for that directory | lazy consensus, 1 approval | none beyond normal review | — |
| Cross-cutting / breaking change (shared code, public API, 2+ directories) | affected area owners, written proposal | consensus-seeking, 2 approvals, justified objections only | 10-day comment window | unresolved after 14 days → full council, simple majority |
| New maintainer | any maintainer nominates | no-objection window, else vote | 7 days | majority vote of current maintainers |
| Maintainer removal | maintainer council | supermajority vote | — | two-thirds of remaining maintainers |
| Scope change (add/drop/rename a component) | full council | consensus-seeking, written proposal | 10 days | explicit vote if unresolved |
| Release (per component) | that component's release owner | majority approval, no veto | — | — |
| Security response | 2 named responders spanning core runtime + provider/charts | private, delegated authority | per SECURITY.md | disclose per policy |
| Amendment to this document | maintainer council | supermajority (two-thirds) | 14-day window | — |

Promotion numbers (6 months, 10 merged PRs, 20 reviews) are the reference skill's baseline for a well-trafficked project; at ~4 regular outside contributors that bar excludes everyone. Scale down — e.g., 3 months, 5 non-trivial merged PRs, meaningful review activity — and let the six set the real number against actual PR volume.

Escalation: keep it flat. With six people and no election history, don't invent a tiebreaker role nobody asked for. Unresolved disagreement after the stated window goes to a council vote; a tie or a vote not reaching threshold is declined/held, not force-closed — the one rule shared by all six published ladders.

## Neutrality — trademark, affiliation ratio, contribution agreement, minutes

Not urgent — no adopter has asked who controls Thornfield, and this is a blocker only once one signal is confirmed:

- ⚠️ Employer spread unconfirmed. Ask directly. If one company already or later holds a maintainer majority, add organization-balanced voting (one vote per employer, independents count as their own) to the council before it's contested — it's "uncontroversial" only while the seat count is still small.
- Trademark, domains, registry accounts (npm, Terraform Registry namespace, Helm repo, VS Code Marketplace publisher, container registry): ownership unconfirmed. Inventory now regardless of employer spread — this is the step 7 credential list either way.
- No contribution agreement mentioned. If a CLA exists, check whether it concentrates relicensing rights in one company; a DCO model carries no such risk.

## GOVERNANCE.md — ready to commit

```markdown
# Thornfield governance

## Scope

Thornfield is maintained as one repository covering six components: core
runtime, CLI, web dashboard, Terraform provider, Helm charts, and VS Code
extension. It stays one project with one release cadence per component,
not six independently-governed subprojects — see "Area ownership" below
for how work is routed without splitting governance.

## Roles

- **Maintainers**: [name six]. Merge rights across the repository, a vote
  in governance decisions.
- **Area owners**: one or two maintainers named per component in
  CODEOWNERS, first reviewer and first decider for routine changes inside
  that component. Rotates among the six maintainers; not a separate role
  with its own promotion path.
- **Release keys**: [fill in per component — npm, Terraform Registry,
  Helm repo, VS Code Marketplace, container registry]. At least two
  maintainers hold each.
- **Contributors**: anyone with a merged change.

## Becoming a maintainer

Three months of sustained participation, including at least five
non-trivial merged pull requests and meaningful review activity. Any
maintainer may nominate. The nomination passes if no maintainer objects
within 7 days, otherwise it goes to a simple-majority vote.

## Removing a maintainer

Resignation, or inactivity of six months with no stated return date, or a
two-thirds vote of the remaining maintainers for cause. Writing this
before it's needed is what makes it survivable.

## Emeritus

An inactive or resigned maintainer moves to emeritus: credit retained in
MAINTAINERS.md, merge rights and credentials removed, listed separately.
Reinstatement by simple majority of current maintainers.

## Meetings and communication

No standing meeting. Decisions happen asynchronously in issues and pull
requests. Area owners may hold ad-hoc syncs within their component; notes
go in the relevant issue, not a private channel.

## Decision-making and voting

[the decision-rules table above, pasted in as the authoritative version]

Abstentions do not count toward a threshold. Quorum for any vote is a
simple majority of current maintainers.

## Area ownership

Each of the six components has one or two named area owners in
CODEOWNERS. An area owner decides routine changes to their component
without returning to the full council. Anything crossing component
boundaries, changing public API behaviour, or changing project scope
follows the cross-cutting rule above instead.

This document does not create a subproject, charter, or maintainer list
per component. Revisit only if a component grows contributors who don't
touch the other five — see "Review" below.

## Code-of-conduct enforcement

See CODE_OF_CONDUCT.md. If the subject of a report is a maintainer, they
are excluded from deliberation; two other maintainers handle it. If the
whole maintainer group is implicated, escalate outside the project.

## Security response

See SECURITY.md. [Name 2] handle reports privately and act with
delegated authority to patch and coordinate disclosure without a public
vote. Reviewed every [interval].

## Appeals and escalation

Open an issue tagged `governance-appeal`. The relevant decider (area
owner or council) responds within 14 days. If denied, any maintainer may
bring it to a full council vote.

## Trademarks and project assets

[Fill in once confirmed: who holds the Thornfield name, domains, npm
org, Terraform Registry namespace, Helm repo, VS Code Marketplace
publisher, container registry. Route any transfer or licensing question
to counsel.]

## Amendments

Any maintainer may propose a change to this document. Requires a
two-thirds vote of current maintainers, open for at least 14 days.
Expected to change as the project grows — amending it is normal, not a
crisis.

## Review

Re-examined annually and after any maintainer change. Re-open the
federation question specifically if one component's outside contributor
base stops overlapping with the other five, or if decisions keep
stalling despite area ownership — in that order, since the second means
this document's mechanism, not its model, is wrong.
```

## Enforcement — repo settings and credential changes needed to match it

- Repo permissions: keep merge rights repo-wide for all six — matches reality, don't fake a restriction nobody has. Add a CODEOWNERS file mapping each of the six directories to its named area owner(s); this is the actual fix for the reported bottleneck and requires zero new people.
- Branch protection: 1 required approval for changes scoped to one directory, 2 for anything touching more than one directory or public API/shared code — matches the table above, not today's undocumented "everyone" default.
- Credential inventory (unconfirmed today, do regardless of the governance choice): npm org, Terraform Registry namespace, Helm chart repo index, VS Code Marketplace publisher account, container/image registry, domains/DNS for the dashboard, CI secrets and deploy tokens, security-report inbox. Target ≥2 current holders per row; flag any row with exactly one.
- MAINTAINERS.md: list the six with current affiliations, plus an emeritus section (empty today, ready for when needed).

## Succession — trust ladder, inactivity rule, emeritus, end state

- Trust ladder: Contributor → Triager → Reviewer (named component) → Maintainer → Key holder. Merge/triage rights are cheap to grant and revoke — grant them generously to the 4 regular outside contributors. Grant signing/publish rights only after a supervised release cycle, never in the same act as merge rights.
- Inactivity: six months low activity → emeritus, credentials rotated within 30 days.
- Named end state per component: if a component's maintainers all step back with no successor, mark it maintenance-mode publicly (last supported version, security policy) rather than let it silently rot — the one-component version of an archive announcement.
- Absence factor target: ≥2, project-wide and per directory — measure from real history before the next review; today's number is a self-report.

## Foundation — needed or not, and the gap list if yes

Not needed now. No money to handle, no adopter asking who controls Thornfield — say so and stop, per the skill: a host adds only obligations with neither need present. Revisit on a real trigger: the first sponsorship offer, the first adopter procurement review, or a maintainer personally paying for infrastructure.

## Review date — when it is re-examined, and what triggers it sooner

- Recompute the absence factor and confirm employer spread from real data before treating this document as final — everything above used the numbers given in the request, not measured ones.
- Re-rank federation the day one component's outside-contributor base stops overlapping with the other five — that's the actual trigger this design is waiting on, not a calendar date.
- Otherwise: re-run annually and after any maintainer change. Sooner if: decisions keep stalling despite area ownership (wrong mechanism, not wrong model), one employer reaches a maintainer majority (step 6, now a blocker), or money/an adopter's control question shows up (step 8).
- Health check before committing: rule coverage (every hard decision of the last 12 months maps to a rule above — confirm with the six), concentration (absence factor ≥2, ≥2 credential holders — pending measurement), alignment (CODEOWNERS/branch protection match the table), timers (every class above has one — yes). Schedule the fifth check — evidence the rules ran once — two quarters out.