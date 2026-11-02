# Governance review — Quillrope

## As-is

No written governance exists today; the real rule lives in three heads. Reconstructed from what you've given me:

- **Decides today:** you, Dara, Sasha — all three hold merge rights. Unstated: whether all three also hold crates.io publish rights, or just some of you.
- **Affected:** ~41,000 crates depending directly or transitively — mostly other maintainers and companies via `Cargo.lock`, not end users you interact with directly.
- **Contribution funnel:** effectively closed. 9 external contributors last year, 6 of them a single typo-fix PR. Everything of substance is written by the three of you.
- **Load:** ~120 issues/month across three people, with no stated triage role beneath "maintainer."
- **Gaps a documented model would close:** no deadlock rule, no promotion criteria, no inactivity/emeritus definition, no named security-response process for a crate this widely depended on.

This is Eghbal's **Stadium** shape — many users, almost no contributors — not the Federation shape that elected committees exist to serve. That mismatch drives the recommendation below.

## Concentration

I can't compute the actual absence factor without your commit history — run this yourselves before locking any threshold into the document:

```
git log --since=12.months --no-merges --pretty=format:'%aN' | sort | uniq -c | sort -rn
```

Sum contributions, take 50% of the total, accumulate top contributors until you cross it — that count is the absence factor (CHAOSS metric). Given how rare outside patches are, I'd expect the project-wide number to already collapse to 1–2 among the three of you; confirm it, because it determines whether "any two of three" quorum rules are actually safe or whether one of you is silently load-bearing for more than half the project.

Open items I need from you, not inferable:

- **Employer spread** — do you, Dara and Sasha work for the same company, different companies, or is anyone unaffiliated? This gates step 6 and whether "organization-balanced voting" needs to exist at all.
- **Credential inventory** — who holds the crates.io publish token(s) for `quillrope`, GitHub org/repo ownership, the security-report inbox, CI secrets? List each row and how many people hold it. Any row with exactly one holder is your actual emergency, ahead of any council design.

## Recommendation

**Not the five-seat elected council, not yet — install a maintainer council now, revisit the elected model on a named trigger.** Two options, trade-offs first:

| Option | Effort | What it buys |
|---|---|---|
| **1. Maintainer council** (you, Dara, Sasha as the council) | ~1 hour/month, no standing meeting, reversible by one vote | The two things you're actually missing: a deadlock rule and promotion criteria. Installs in an afternoon — compatible with a March deadline. |
| **2. Elected 5-seat steering committee**, PEP 13 / Kubernetes-style | A quarter to install (define electorate, run election, seat officers), then a standing job, hardest of the two to undo | Legitimacy a self-selecting group can't claim — but you have no electorate to claim it from yet. |

Why option 2 is wrong for Quillrope *right now*, not wrong in principle:

- **No electorate.** PEP 13's council was elected by 96 eligible core-team voters (62 voted). Kubernetes' committee is elected by a contribution-based community. You have 9 external contributors, 6 of them one-off typo fixes. There's no pool to elect 5 people from — you'd end up appointing 2 non-maintainers to titles with no decision history behind them, which is the exact "titles instead of authority" failure mode this process warns about.
- **The date argument cuts against you, not for you.** A hard deadline promotes models that install in an afternoon and demotes an elected body, because electoral legitimacy is the one thing that can't be compressed to fit a schedule. Wanting this settled before March is a reason to pick the council, not the committee.
- **This is close to a documented anti-pattern.** The reference case for "over-engineered" is, almost line for line, a five-seat committee with staggered two-year terms and election officers, on a project with a handful of maintainers that has never held an election. Lapsed terms and a visibly false governance file are worse than having written nothing.
- **The scarce resource is maintainer attention, not decision legitimacy.** With 41k dependents and near-zero contributor throughput, the work is curation and scope defense. A council seat doesn't create a sixth pair of hands.

**What would flip this recommendation:** any of — decisions actually stalling under the council; the only path to influence becoming "become a maintainer" as your contributor base grows; one employer holding a majority of the three seats; or a foundation application with a stated governance bar. None of those are true yet from what you've told me. Write the trigger into the document (below) so the next review argues against a stated bar, not a vibe.

**Keep from your PEP 13 / Kubernetes reading, for later:** staggered terms, an impartial election officer, and contribution-based eligibility are all correct designs — they're just designs for a body with an electorate. Build the electorate first via the trust ladder in Succession, below; the committee shape is ready to reuse once it exists.

## Decision rules

| Class | Decider | Mechanism | Threshold / timer |
|---|---|---|---|
| Routine change | any maintainer | lazy consensus | 1 approval to merge; drops from 2→1 after a change has sat 7 days with no objection (Node.js's aging rule — useful for a 3-person team where someone is often away) |
| Breaking change / 2.0 scope | maintainers | written proposal + consensus-seeking | 10-day comment window; objection must state a technical reason; unresolved after 30 days → simple-majority vote among the three |
| New maintainer | maintainers | nomination + no-objection window | any current maintainer nominates; passes if none object within 7 days, else majority vote |
| Maintainer removal | maintainers | vote | 2 of 3 (supermajority at this size); written reason recorded |
| Release | release owner(s) | majority approval, no veto | whoever holds the crates.io token for that release |
| Security response | maintainers | private, delegated | named inbox, ≥2 people with access; public disclosure timeline stated in SECURITY.md |
| Money / brand | maintainers (none currently apply) | — | revisit if sponsorship money starts arriving |
| Governance amendment | maintainers | vote, longer window | 2 of 3, minimum 14-day open PR |

## Neutrality

Not urgent at your current scale, but cheap to fix now versus later — do it in this order per the skill, before it's a live dispute:

- Confirm the `quillrope` crate name is owned by ≥2 of you on crates.io, not one personal account.
- Move repo ownership to a GitHub organization if it isn't already, with ≥2 owners.
- If any domain (`quillrope.dev` or similar) exists, confirm who holds the registrar account.
- Answer the employer-spread question above — if two of three of you share an employer, say so explicitly in the document rather than letting it surface later as a surprise. Stating a reserved interest up front is what avoids the "invisible control" failure mode; drift after the fact is what triggers revolt.

## GOVERNANCE.md

```markdown
# Governance

## Scope

<You>, Dara <Last>, and Sasha <Last> maintain Quillrope. It stays a
streaming CSV parser; format auto-detection, non-CSV delimited formats,
and a plugin system are out of scope unless a maintainer vote changes this.

## Roles

- Maintainers: <You>, Dara, Sasha. Merge, release, and decide direction.
- Release keys: crates.io publish rights held by [name at least two].
  GitHub organization ownership held by [name at least two].
- Triagers: contributors granted label/close/reopen rights without merge
  rights (see Becoming a maintainer).
- Contributors: anyone with a merged change.

## Decisions

Routine changes: one maintainer approves; any maintainer may merge.
A change open 7+ days with no objection needs only one approval regardless
of size.

Breaking changes, scope changes, and the 2.0 release plan: a written
proposal, a 10-day comment period, and agreement from at least two of
three maintainers with no unresolved technical objection. An objection
must state a technical reason to block.

Disagreement surviving 30 days after a proposal: decided by a vote among
the three maintainers, simple majority, recorded in the issue.

## Becoming a maintainer

Six months of sustained triage or review activity, judged on judgment
shown rather than volume — this project's contributor pipeline is thin,
so a merged-PR count would exclude nearly everyone. Any maintainer may
nominate; passes if no maintainer objects within 7 days, otherwise a
majority vote. New maintainers get merge rights immediately and release
(crates.io) rights after one supervised release cycle.

## Removing a maintainer

Resignation, six months of inactivity with no stated return date, or a
conduct violation. Threshold: agreement of the two other maintainers.
Recused if the removal concerns them.

## Emeritus

A maintainer who steps back keeps credit in MAINTAINERS.md and loses
rights; credentials are rotated within 30 days. Reinstatement by
agreement of the remaining maintainers.

## Meetings and communication

No standing meeting. Decisions happen in public issues and PRs. Security
reports are the only category handled privately, and are disclosed on a
stated timeline once fixed.

## Decision-making and voting

See Decisions above for thresholds by class. Any maintainer may call a
vote on a stalled proposal. Quorum is all active (non-emeritus)
maintainers; abstentions do not count toward the threshold.

## Security response

Reports go to [security contact / inbox]. At least two maintainers have
access at all times. See SECURITY.md for the disclosure process.

## Appeals and escalation

Reopen a closed decision by opening a new issue tagged `governance`,
stating what changed. The maintainers respond within 14 days.

## Trademarks and project assets

The Quillrope name and crates.io listing are held under the project's
GitHub organization, with at least two maintainers as owners on every
account and registry. No maintainer holds a project credential alone.

## Amendments

Any maintainer may propose a change to this document. Requires agreement
from two of three maintainers and a comment period of at least 14 days.

## Revisiting this document

This project runs a 3-seat maintainer council by design, not a smaller
version of a steering committee. Revisit the model — including an elected,
staggered-term steering council — when any of the following hold:
merge rights extend past three people, one employer holds a majority of
maintainer seats, decisions are stalling under this process, or a
foundation application requires elected governance. Next scheduled
review: before the 2.0 release, and annually after.
```

## Enforcement

Align these before treating the document as real:

- Branch protection on `main`: require the review count stated above (1, dropping from 2 after 7 days), from a CODEOWNERS list matching the three names.
- crates.io: confirm current owners with `cargo owner --list quillrope`; add any maintainer missing, remove anyone no longer active.
- GitHub org (not a personal account) owns the repo, with ≥2 org owners.
- Security advisory / private vulnerability reporting enabled on the repo, routed to the ≥2 people named in SECURITY.md.
- MAINTAINERS.md lists current affiliations and an emeritus section, even if empty today.

## Succession

Your real exposure isn't the three of you — it's that nothing exists beneath you. At 120 issues/month with a near-zero contributor funnel, build the ladder now; it's also the prerequisite for ever making the elected-committee model real:

1. **Contributor** — merged changes. You have this.
2. **Triager** — label, close, reopen; no merge rights. Cheapest grant available and directly cuts your 120/month load. Grant this liberally — it's revocable at no cost.
3. **Reviewer** — approvals count toward merge in a named area (parsing core, serde integration, CLI, etc. — whatever Quillrope's areas actually are).
4. **Maintainer** — merge rights, a vote in governance.
5. **Key holder** — crates.io publish, granted only after one supervised release cycle, never in the same act as merge rights.

Be generous with steps 2–3, slow with 4–5 — that split is what would have slowed the xz-utils takeover, and it's the mechanism that eventually produces an electorate worth holding an election for. Treat any external pressure to fast-track someone into a key-holder role as a reason to pause, not a reason to move faster.

## Foundation

Not triggered. Per the join-or-not test: you haven't mentioned needing to hold donations, pay contributors, or prove vendor-neutrality to an adopter, and with three independent maintainers there's no single-vendor-control question yet. Revisit if: sponsorship money starts arriving, an enterprise adopter's procurement review asks who controls Quillrope, or the ecosystem fit (Rust Foundation, given this is a crates.io-published crate) becomes relevant once you have adopters willing to be named publicly.

## Review date

Adopt the council model now — it's the piece compatible with your March deadline. Re-examine on:

- **Before the 2.0 release ships** — confirm the breaking-change process in Decisions actually governed the 2.0 scope decisions, not just existed on paper.
- **Two quarters after adoption** — confirm the rules were exercised at least once (a triager promoted, an objection resolved under the written path, not just the happy case).
- **Annually, and after any maintainer change** — standard cadence.
- **Immediately, out of cycle** — if any of the elected-committee triggers in the "Revisiting this document" clause fire early.

One thing worth doing in parallel, outside this document: with 120 issues/month and a triage gap, `samber/developer-relations-skills@oss-issue-triage` covers the queue this governance model assumes exists, and `@oss-contributor-onboarding` covers turning single-typo-fix drive-bys into the reviewer pipeline step 7 depends on.