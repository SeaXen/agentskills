# Governance review — Kerrigold Mesh

## As-is

No written governance exists. By default, all four maintainers presumably hold equal merge and release rights (an unwritten council) — confirm this against actual repo permissions before submitting, since "presumably" is not something a foundation reviewer will accept either. Northgate Labs, by default, almost certainly also holds the GitHub org, the trademark/name, the domain, and the registry publish tokens, since nothing has ever separated them out. State that plainly rather than leaving it implied — see Neutrality below.

## Concentration

Maintainer-affiliation ratio: **4 of 4 at one employer — 100% single-vendor.** That's worse than the 2-of-5 ratio that flagged Redis as single-vendor before its 2024 fork (Valkey co-founder, press interviews). This is the first number a foundation reviewer computes, and no committee structure changes it.

Two numbers you haven't given me and need before submission, not estimated:

- **Contributor absence factor** (smallest number of people responsible for 50% of contributions, CHAOSS metric) — self-set target is ≥2. Compute it over the trailing 12 months, on commits *and* reviews *and* docs, per-area as well as project-wide.
- **Credential inventory** — release signing keys, registry publish rights, domain/DNS, org ownership, CI secrets, security inbox: list who holds each. Assume single points of failure on every row until you've confirmed ≥2 holders.

## Recommendation

**Your draft matches this skill's own documented failure case, clause for clause.** A five-seat committee, staggered two-year terms, an appointed election officer, a contribution-based electorate, and three working groups is the exact worked example of over-engineered governance for "four maintainers, all at one employer, that has never held an election." The three named costs apply directly: elections that never happen, working groups with one member, and a review that distrusts the whole document once one clause is provably false. A foundation reviewer reads your application the same way this skill reads a bad draft.

Two more reasons this instrument doesn't fit *this* milestone specifically:

- Sandbox-tier entry is typically satisfied by **documented** governance and a code of conduct. Exercised governance and organizational diversity are graduation-level tests. Installing graduation-grade machinery for a sandbox review spends effort the checklist doesn't yet ask for — confirm this against the actual foundation's published sandbox criteria, since I don't know which foundation and requirements diverge by host type.
- The electorate for this election is your four existing maintainers. A committee they elect from among themselves isn't more legitimate than the council they already are — it's the same body in an election costume. That's "titles instead of authority," a pattern reviewers are trained to spot, not solve for you.

**Two options, with trade-offs — pick one and say why in the doc:**

| | Maintainer council + delegated working groups (recommended) | Elected steering committee, fixed |
|---|---|---|
| Effort to install | ~1 hour/month, no standing meeting | A quarter, done honestly — electorate has to exist before seats do |
| Reversibility | One vote undoes it | Least reversible model in the catalogue — an elected body isn't quietly dissolved by the people it constrains |
| What it buys | The two rules an undocumented project most visibly lacks: deadlock and promotion | Legitimacy a self-selecting group can't claim — real only once a second employer is represented |
| Fits your 6 weeks? | Yes | Only if the target foundation's checklist *requires* an elected body, not merely prefers one |
| Honest about today? | Yes — states 4 maintainers, 1 employer, plainly | Only if you also state the seat math openly (see fixes below) |

Take the council. Keep your three working groups (security, docs, release) — they're good instincts — as **named, delegated scopes under the council**, not seats under an elected body. Delegation is how a council survives growth without needing a committee.

Write a revisit trigger instead of guessing at the future:

> Revisit this model when maintainer count exceeds eight, or a second employer holds two or more maintainer seats, or the foundation's next tier requires exercised governance.

### If you keep the committee anyway

Only if the foundation's own checklist names it as a requirement. If so, these five fixes are non-negotiable:

1. **Seat math.** Say where the fifth seat comes from. Filling it from Northgate Labs makes the committee 5-of-5 single-employer — cosmetically different, structurally identical to today. State a per-organization seat cap now (e.g., no employer holds more than 2 of 5 seats), adopted while the seat count is small enough to be uncontroversial — not after a second employer arrives and the cap looks aimed at them.
2. **Electorate.** Replace "contribution-based" with a number: e.g., 10 non-trivial merged PRs or 20 substantive reviews in the trailing 12 months. Publish the resulting eligible-voter list before the vote opens, so a reviewer can audit who could vote, not just that a vote happened.
3. **Election officer.** Name who appoints them, and bar sole appointment by the incumbent maintainer group. If the first officer is necessarily a Northgate Labs employee — nobody else exists yet — say so, and add a recusal rule for any cycle where they're also a candidate.
4. **Staggering.** Five seats elected the same day aren't staggered — they're five identical terms that desync only by luck. Assign initial terms by lot (two seats at one year, three at two years) so the *second* election is genuinely staggered.
5. **First-term length.** Don't lock in two years before the process has run once. Shorten the inaugural term to one year; start the two-year cycle at the second election. A long first term with zero evidence the rules work is exactly the "lapsed terms are worse than no election" failure.

## Decision rules — numbers, not descriptions

| Class | Decider | Mechanism, threshold, timer |
|---|---|---|
| Routine change | Any maintainer | One approval, lazy consensus, merge on approval |
| Breaking / scope change | Maintainers | Written proposal, 10-day comment window, 2 approvals, no unresolved technical objection; unresolved past 30 days escalates to full-council simple-majority vote |
| New maintainer | Maintainers | Nominate anytime; passes on no objection within 7 days, else simple-majority vote. Eligibility (self-set, tune to actual traffic): 6 months' sustained participation, ≥10 non-trivial merged PRs or ≥20 substantive reviews |
| Removal | Maintainers | Two-thirds of remaining maintainers; anyone employed by a party to the dispute recuses |
| Release | Named release owner(s), ≥2 | Majority approval, cannot be vetoed |
| Security response | Named group, ≥2 | Private channel, delegated authority on the timeline published in SECURITY.md — link it, don't restate it here |
| Money / brand / trademark | Full council | Vote, minutes published |
| Amendment | Full council | Agreement in a public PR open ≥7 days |

Every objection above must carry a technical reason to block — an unjustified veto carries no weight. Every class above has a clock; a decision not taken by its deadline defaults to the status quo, not to silence.

## Neutrality — say what Northgate Labs holds, today

- Confirm and write down, plainly: who holds the GitHub org, the trademark/name, the domain, the registry publish tokens. If it's Northgate Labs across the board — likely, given 4-of-4 — write it as a stated **Reserved rights** clause rather than leaving it implied. What triggers a later revolt is a neutrality claim that drifts, not a limit that was named up front.
- If incubation is a later goal, the sequence that actually earns neutrality is: maintainers from a second organization first, then seat/vote caps, then trademark and asset transfer — in that order. Claiming neutrality before the maintainer pool changes reads as marketing and gets checked as marketing (Istio's 2020 trademark dispute, the .NET Foundation's 2021 maintainer revolt).
- Contribution agreement (CLA vs. DCO) is out of scope for this review — route to counsel, and use `@oss-license-strategy` if you haven't settled it.

## GOVERNANCE.md — ready to commit

```markdown
# Governance

## Scope

Kerrigold Mesh is maintained by four maintainers, all currently employed by
Northgate Labs. It stays a <one-line scope statement>; <named
out-of-scope area> is out of scope.

## Roles

- **Maintainers**: <names>. Merge, release, and decide direction, equally,
  regardless of employer.
- **Release keys and registry publish rights**: held by <name>, <name> (at
  least two, confirmed against actual credentials before this document is
  committed).
- **Working groups** — delegated scope, reporting to the maintainers, no
  independent decision authority beyond what's named here:
  - *Security*: <names>, ≥2. Owns triage and disclosure on the timeline in
    SECURITY.md.
  - *Docs*: <names>. Owns docs review and structure.
  - *Release*: <names>, ≥2. Owns the release checklist and go/no-go call
    under the Decisions rule below.
- **Contributors**: anyone with a merged change.

## Reserved rights

Northgate Labs currently holds the project's trademark, domain, and GitHub
organization. This is stated here rather than left implicit. <State the
plan and timeline if diversification or transfer is intended; state "no
plan yet" if genuinely none, rather than omitting the line.>

## Decisions

Routine changes: one maintainer approves; either may merge.
Anything changing public API behaviour, scope, or licence: two maintainer
approvals, in a public issue, after a 10-day comment window. An objection
must state a technical reason. Unresolved after 30 days: any maintainer may
call a vote of the full maintainer group, decided by simple majority.
Releases: named release-group members approve by majority; a release
cannot be vetoed.
Security responses: the security working group acts under the timeline
published in SECURITY.md, without a full-council vote, and reports back
within 7 days of resolution.
Money, brand, and trademark decisions: full maintainer vote, minutes
published.

## Adding a maintainer

Eligible after 6 months of sustained participation, including at least 10
non-trivial merged pull requests or 20 substantive reviews. Any maintainer
may nominate. The nomination passes if no maintainer objects within 7 days,
otherwise it goes to a simple-majority vote. Nominations are judged without
regard to employer; if a single employer would come to hold more than half
of all maintainer seats, that nomination requires a public statement of
why before the vote.

## Removing a maintainer

Resignation, or inactivity of 6 months with no stated return date, moves a
maintainer to emeritus automatically. Conduct violations follow
CODE_OF_CONDUCT.md. Any other removal requires a two-thirds vote of the
remaining maintainers; a maintainer who is party to the dispute recuses.

## Emeritus

Emeritus maintainers keep credit in MAINTAINERS.md and lose merge, release,
and vote rights. Reinstatement is by simple majority of current
maintainers.

## Meetings and communication

<State actual cadence, or state there are no standing meetings and
decisions happen in public issues/PRs — don't invent a meeting that won't
happen.> Notes, where meetings occur, are published in <location>.

## Code of conduct enforcement

Enforcement follows CODE_OF_CONDUCT.md. A maintainer who is the subject of
a report is excluded from deliberation on it; the remaining maintainers
handle it, or refer it outside the project if the whole maintainer group
is implicated.

## Security response

Reports and embargo handling follow SECURITY.md. The security working
group (≥2 people, named above) is reviewed for currency every 6 months.

## Appeals and escalation

Any contributor may ask for reconsideration of a maintainer decision by
opening an issue tagged `governance-appeal`. The maintainers give a
written answer within 14 days. A decision not appealed within 30 days of
being made is final.

## Trademarks and project assets

The project name, domain, and registry accounts are held as stated in
Reserved rights, above. A departing maintainer retains no individual claim
on any of these. <Route any transfer or licensing question to counsel
before writing more here.>

## Amendments

Amending this document requires agreement of all current maintainers, in a
public pull request open for at least 7 days. This document is expected to
change as the project grows; amending it is a normal governance act, not
a crisis.

**Revisit trigger**: this model is re-evaluated when maintainer count
exceeds eight, when a second employer holds two or more maintainer seats,
or when the target foundation's next tier requires exercised, elected
governance — whichever comes first.
```

## Enforcement

- Confirm branch protection and merge rights match "4 maintainers, equal rights" exactly — no silent fifth admin, no maintainer missing a right the document grants them.
- Confirm CODEOWNERS (if present) routes to areas the commit history shows these four people actually touch, not aspirational areas.
- Confirm org ownership, release signing, and registry publish sit with ≥2 named people today — the document's "release" and "security" clauses are fiction until this is true.
- Ship MAINTAINERS.md today, listing current affiliations (all Northgate Labs, stated plainly) plus an emeritus section, even if empty.

## Succession

- Run the absence-factor calculation before submission and report the actual number in the review — don't estimate it in the document.
- Bring every credential row (signing, registry, domain, org, CI, security inbox) to ≥2 holders before relying on the release/security clauses above.
- The document above already carries the standard exit paths in miniature (inactivity → emeritus, resignation, removal). Add a one-line "if all four step back, we archive or name a successor publicly" clause — cheap now, and its absence is exactly the kind of gap a reviewer reads as an unmaintained-project risk.

## Foundation readiness — mapped to your 6 weeks

Fix order, per the standard readiness-gap list:

- **Maintainers from only one organization** — the slow gap; genuinely takes quarters, not six weeks. Don't paper over it with an election among the same four people. State it plainly, plus a real recruitment intent and rough timeline. A named gap with a plan reads far better to a reviewer than an undisclosed one.
- **Governance documented but never exercised** — six weeks is enough to run this document through one real cycle before you submit: process one actual nomination or one actual contested-change decision through the written rule, so "exercised" isn't purely theoretical on submission day.
- **Repository permissions contradicting documented roles** — fixable this week; do it first.
- **Unclear ownership of name, domain, registry** — fixable this week; do it first, and write the answer into Reserved rights above.
- **Missing community-health files or a stale maintainers list** — add CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md, and MAINTAINERS.md alongside this file if any are missing.
- **No adopters willing to be named publicly** — outside this review's scope, but reviewers ask; line this up in parallel with legal/counsel items.

**Open question I can't answer for you:** which foundation, and does its published sandbox checklist actually name an elected body as a requirement, versus documented governance plus a code of conduct? That single fact is what decides between the two models above — get the actual checklist before locking in either one.

## Review date

Re-run this review once the missing facts above (affiliation ratio is already known; absence factor, full credential inventory, and the target foundation's actual checklist are not) are filled in, and before the submission is finalized. Re-run again annually, after any maintainer change, or the moment a second employer holds a maintainer seat — whichever comes first.