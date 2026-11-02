Using the **oss-governance** skill (`skill-wip/samber/developer-relations-skills/skills/oss-governance/`) and its six references (neutrality-and-assets, governance-models, decision-rules, succession-playbook, governance-doc-template, foundation-options, published-findings) to produce the review this triggers, then answer the actual ask.

**Headline, before anything else:** the announcement as scoped ("Vantablock is now a vendor-neutral open project") will not survive the exact check a bank's procurement team runs. Publishing it now is the skill's named failure mode — **neutrality by press release** — and it lands on the one audience already looking. Here's the audit, then the governance work that makes a *true* version of that claim possible, then two announcement drafts: one you can run next month, one to hold for later.

---

## Why the claim fails today

The four checkable signals adopters, procurement teams and foundations use, applied to Vantablock as described:

| Signal | Vantablock today | Verdict |
|---|---|---|
| Trademark, domain, registry accounts | held by Corvid | ❌ fails |
| Maintainer affiliation | 5 of 5 employed by Corvid | ❌ fails — worse than the 2-of-5 ratio that classified Redis as single-vendor before its fork |
| Contribution agreement | CLA assigning broad rights to Corvid | ❌ fails — this is the exact lever that made Redis's later relicense possible; fork contributors called this out by name |
| Published minutes | weekly sync, internal, no minutes | ❌ fails |
| License | Apache-2.0, OSI-approved | ✅ passes, and is irrelevant to the other four |

Four of four governance signals fail. License openness and governance openness are separately audited — a permissive license does not offset any of this. This is a stronger single-vendor signature than the project (Redis) whose affiliation ratio is the field's standard example. A procurement analyst who already asked the question will find this within a day of the announcement running, not eventually.

The Istio case is the direct precedent for what happens when a company announces neutrality without transferring the asset: partners judged where the trademark actually landed, not the sincerity of the announcement, and the dispute only closed when Google donated the mark to CNCF two years later. Vantablock has not yet moved anything.

---

## As-is — who decides today

- Merge/release authority: unconfirmed — name who can merge to main and who can publish a release; often not the same people. **Confirm before publishing anything.**
- All five maintainers are Corvid employees. No maintainer, trademark holder, domain registrant, or CLA assignee sits outside Corvid.
- Decisions happen in a weekly internal sync with no minutes — an implicit "whoever's in the room" rule, invisible to anyone outside Corvid, including the two evaluating banks.
- No documented rule exists for: deadlock, adding/removing a maintainer, security response ownership, or what happens if a maintainer leaves.
- Credential inventory (trademark, domain, CLA counterparty, package registry, signing keys, security inbox): all presumed Corvid-held. Confirm the registry/CI/security-inbox rows specifically — not mentioned, likely the same pattern.

## Concentration

- Employer spread: **1**. This is the number to move, and it's more urgent than the internal absence factor — a project can have five well-distributed internal contributors and still fail the neutrality check on this one row alone.
- Internal absence factor: not computed — needs `git shortlog`/CHAOSS-style analysis over 12 months, per governed area, if you want the number. Doesn't change the recommendation below; single-employer-affiliation already gates the neutrality claim regardless of how contributions split among the five.
- Trend: unknown — flag if the maintainer count or affiliation mix has moved in the last year.

## Recommendation

**Maintainer council, with an organization-balanced voting module pre-written and ready to trigger.** Top two considered:

| Model | Monthly hours | What it buys |
|---|---|---|
| **Maintainer council (recommended)** | ~1 hour/month beyond the sync you already run; reversible by one vote | The two rules Vantablock visibly lacks — deadlock and promotion — installable in an afternoon, which fits the conference date |
| Elected steering committee | a quarter to install, then standing overhead | Legitimacy a self-selecting group can't claim — not yet earned here: no election history, no second employer, no outgrown-maintainer-set signal |

None of the four triggers that would promote the committee are crossed yet (no second payroll, no founder departure, no contributor base outgrowing the maintainers, no foundation application with a stated bar). Adopting a committee now, days before a conference, with zero election history, is the named anti-pattern in the template reference — don't do it for the announcement's sake.

Write the org-balanced voting and per-org seat-cap clause into the document *now*, dormant, so it activates the moment a non-Corvid maintainer is seated instead of being negotiated under pressure later.

## Decision rules

| Class | Decider | Mechanism |
|---|---|---|
| Routine change | any maintainer | lazy consensus + review |
| Breaking/scope change | council | consensus-seeking, written proposal, 10-day comment window |
| New maintainer | council | staged criteria (below), no-objection window, judged without prejudice to employer |
| Removal | council | two-thirds vote |
| Release | release owner(s) | majority approval, no veto |
| Security response | named 2-person team | delegated, private |
| Money, brand, trademark | council | vote, minutes published — this row currently has no rule at all and is the one a bank will ask about first |
| Amendment | council | supermajority, 7-day window |

Escalation ladder (Node.js's shape, adapted — attributed, not claimed as standard): consensus-seeking first; unresolved after 30 days, any maintainer may call a vote; simple majority decides; a proposal nobody agrees on is explicitly declined or held, never left open.

## Neutrality — the actual sequence

Per the skill: *neutrality is transferred, not announced*, and the order is maintainer diversity first, then seat/vote caps, then the asset transfer. Announcing the asset move before the maintainer pool changes reads as marketing because it is marketing.

1. **Now, cheap:** publish minutes from the Tuesday sync going forward. Free, immediate, closes one of the four failing signals this week.
2. **Now, cheap:** write the council + org-balanced-voting governance document (below) and state Corvid's reserved rights explicitly — brand usage, hosted product, release timing, whatever you intend to keep. Say it up front; a stated limit is fine, a drifting assurance is what triggers revolt later.
3. **Start now, takes months:** recruit a maintainer from outside Corvid — one of the evaluating banks' engineers is a plausible candidate if they're contributing. Use the staged trust ladder (contributor → triager → reviewer → maintainer → key holder), not a fast-tracked grant; the xz-utils incident is the reason urgency here is treated as suspicious, not helpful.
4. **Legal review, not yours to draft:** the CLA's broad-rights grant is precisely the relicensing lever that made Redis's move possible later, and re-opening the license without touching the CLA wouldn't restore trust. Send the CLA-vs-DCO question to counsel now so it's not the last blocker before a future real announcement.
5. **Last, and only after 1-4 are real:** move the trademark and domain — into a neutral host if you pursue one (see below), never announced as complete while still Corvid-registered.

## GOVERNANCE.md — ready to commit

```markdown
# Governance

## Scope

Vantablock is a stream-processing engine. This document covers who decides what;
it does not cover contribution mechanics (CONTRIBUTING.md) or conduct (CODE_OF_CONDUCT.md).

## Roles

- Maintainers: [name all five], employed by Corvid Systems. Merge rights, release rights,
  a vote in council decisions. Affiliation is disclosed here and in MAINTAINERS.md, not hidden.
- Release keys and registry publishing rights: [confirm current holders].
- Contributors: anyone with a merged change.

Employer affiliation is listed for every maintainer and updated within 30 days of a change.

## Becoming a maintainer

Nomination after six months of sustained participation, including at least ten
non-trivial merged changes and twenty substantive reviews. Any maintainer may nominate;
the council decides by no-objection window (7 days) or, on objection, a simple-majority vote.
Nominations are judged without prejudice to employer. No more than [N] of [total] maintainer
seats may be held by employees of one organization once a second organization is represented —
this cap is dormant until that day and binding from it.

## Removing a maintainer

Resignation, six months' inactivity with no stated return date, or a conduct violation.
Threshold: two-thirds of remaining maintainers.

## Emeritus

Recognition retained, rights removed, listed separately in MAINTAINERS.md.
Reinstatement by simple majority.

## Meetings and communication

The council meets weekly. Minutes are published within 3 business days to [location],
with exceptions only for security reports, conduct cases, and matters under confidentiality —
each withheld item marked as withheld, never silently omitted.

## Decision-making

- Routine changes: any maintainer, lazy consensus.
- Breaking or scope changes: written proposal, 10-day comment window, consensus-seeking.
  Unresolved after 30 days, any maintainer may call a vote; simple majority decides.
- New maintainer / removal / amendment / money / brand / trademark: council vote per the
  thresholds above; minutes published regardless of outcome.
- A proposal that cannot reach agreement is explicitly declined or held — never left open indefinitely.

## Security response

[Name two maintainers.] Reporting process: SECURITY.md. Membership reviewed every 6 months.

## Appeals

Open an issue tagged `governance-appeal`; the council responds in writing within 14 days.

## Trademarks and project assets

The Vantablock name, vantablock.io domain, and package registry accounts are currently
held by Corvid Systems. This is disclosed, not concealed. Any transfer to a neutral
foundation or fiscal host will be announced when executed, not before. Legal review
governs the transfer itself; this document records the decision, not the contract.

## Amendments

Council supermajority (two-thirds), 7-day open window. This document is expected to
change as the project's maintainer base grows — amending it is normal, not a crisis.
```

## Enforcement

- Audit branch protection and code-owner files against the roles above — confirm merge rights match who's named, before publishing anything.
- Confirm who holds registry publish rights and signing keys today; add a second holder per credential if only one person holds it.
- Publish MAINTAINERS.md with current Corvid affiliation stated plainly — disclosure here is a credibility asset, not a liability, given what's coming next.

## Succession

- Target: employer spread of 2+ before any neutrality claim; internal absence factor of 2+ as the standard baseline once measured.
- Credential inventory: trademark, domain, CLA counterparty, registry, signing keys, security inbox — confirm each row's holder; today they're presumed single-organization (Corvid), which is coherent internally but is exactly what an external audit flags.
- Staged ladder for the first outside maintainer: contributor → triager → reviewer → maintainer → key holder, key holder only after one supervised release cycle.

## Foundation — real question, not yet the next step

Money need: none stated. Neutrality need: yes — this is the actual driver, given procurement's question and the conference ambition. Given Apache-2.0 is already the license, a level-gated technical foundation (Apache Incubator or a CNCF-style host, depending on your ecosystem fit) is the plausible destination for the trademark once the readiness gaps close. Fix order, per the readiness list: single-organization maintainer pool (in progress above), governance never exercised (closes once the council runs its first real vote), repository-permission alignment, registry/domain ownership clarity. These take quarters. Applying — or announcing a target foundation — before closing them is the same anti-pattern as the elected-committee mistake above. Trademark assignment, CLA terms, and any sponsorship agreement go to counsel; this document only prepares the decision.

## Review date

Re-examine this quarterly, and immediately on either trigger: a non-Corvid maintainer is seated, or a bank's procurement team formally responds to what ships next month.

---

## The announcement

### Draft A — publish this next month

> **Vantablock is opening its governance.**
> Vantablock has been Apache-2.0 licensed since day one. Today we're publishing our governance model: decision rules for every class of change, from routine fixes to maintainer changes to release approval, and a public commitment to weekly meeting minutes starting now. We're also opening a path for maintainers from outside Corvid Systems, with clear, self-assessable criteria anyone can work toward. Corvid founded and currently stewards Vantablock — that's disclosed in our new MAINTAINERS.md, not hidden — and our public roadmap toward broader maintainer representation and neutral trademark stewardship is now part of the project's own governance document, reviewed quarterly.

This is true today, it's a real story for the conference (open governance, public rules, a stated roadmap), and it survives the exact check procurement already ran — because it doesn't claim anything that isn't yet the case.

### Draft B — hold for later, do not publish now

> **Vantablock is now a vendor-neutral open project.**
> [Use only once the trademark and domain have actually moved to a neutral host, at least one maintainer from an organization other than Corvid has been seated for real, and the CLA question has been resolved with counsel. At that point this sentence is a fact, not a claim, and it's a considerably stronger announcement than the one you were about to make — it'll survive procurement rather than triggering it.]

---

## Open items I inferred rather than confirmed — check these before shipping

- Names and employer of whoever actually holds merge and release rights.
- Registry, CI-secrets, and security-inbox ownership (assumed Corvid-only; confirm).
- 90-day merge/contributor counts, to compute a real absence factor if you want one.
- What Corvid wants to explicitly reserve going forward (hosted product, release timing, brand usage) — name it in the document rather than leaving it implicit.
- Whether a specific foundation target (Apache Incubator vs. a CNCF-style host vs. staying independent) is even on the table — this determines how far Step 8 goes.

Everything above the license question is governance work, not legal work. The CLA rewrite, trademark transfer mechanics, and any foundation membership agreement go to counsel — this document prepares that conversation, it doesn't replace it.