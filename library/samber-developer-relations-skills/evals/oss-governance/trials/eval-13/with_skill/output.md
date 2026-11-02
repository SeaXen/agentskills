# Governance review — Sablewire

## As-is — who decides today, by what implicit rule, where it has failed

The implicit rule right now is: **Kestrel Data decides; the other maintainers review code.** Nothing wrong has happened yet, but two things already show the rule has no floor under it:

- **Roadmap** is set in a Kestrel-internal planning meeting. It isn't published, and there's no path for a non-Kestrel maintainer to get a say before it's decided.
- **Release timing** is controlled by Kestrel, tied to Sablewire Cloud rollout schedules. That's a real operational need, not an overreach — but it's currently undocumented, so from outside it reads identically to "Kestrel controls everything," including things it doesn't need to control.
- **Trademark and the Cloud product** sit with Kestrel, the founding company.
- Seven maintainers: five at Kestrel, one at Munro Freight, one at Alto Health. The two external seats are new — each company put a full-time engineer on the project.

There's no written rule for deadlock, for adding or removing a maintainer, or for what's reserved to Kestrel versus what the group decides together. The wariness you're describing isn't a symptom of a specific bad decision — it's what happens when new maintainers can't yet tell which of those two buckets any given decision falls into.

*Confirm before treating the rest of this as final: exactly who holds merge rights and release-signing/publish credentials today, and whether Sablewire currently has a CLA or DCO on contributions.*

## Concentration — absence factor, employer spread, credential holders

- **Employer spread:** 5 of 7 maintainers (71%) work for Kestrel; 2 of 7 (29%) are external, one each at Munro Freight and Alto Health.
- **Sourced comparison:** "Only two of Redis's five maintainers worked outside the controlling company" before its 2024 relicense (Valkey co-founder, press interviews) — that 2-of-5 (40% external) ratio is what got Redis classified as single-vendor ahead of its fork. Sablewire's external share, at 29%, is lower than that.
- **Absence factor:** not computed — no commit-history pass has been run. Self-set target, per this skill's baseline: at least 2, computed per governed area as well as project-wide (a workflow engine commonly has one person alone on the execution core even when the whole-project number looks fine). Run this before the next review.
- **Credential holders:** assumed Kestrel alone holds the trademark, domain, registry publish rights, and release signing (confirm the actual list — see Enforcement). A row with one holder, or one company as the only holder, is the finding regardless of what voting model gets adopted.

## Recommendation — model chosen, alternative considered, monthly hours and what they buy

**Chosen: maintainer council with organization-balanced voting (a vote cap plus a nomination cap).** This is the catalogue's own fit for "single vendor, external adopters" — a maintainer council is already the default shape at 3–8 maintainers, and the vote cap is the standard modifier for exactly your situation: one employer holds a seat majority.

- Cost: about an hour a month, no standing meeting, reversible by a single vote if it doesn't work.
- What the hours buy: the two things ad-hoc governance is missing — a deadlock rule and a promotion/removal rule — plus, specifically for your two new maintainers, a vote cap that makes Kestrel's five seats structurally unable to outvote them on anything that goes to a formal vote. That's a guarantee they can check themselves, not one they have to take on trust.

**Alternative considered, parked:** an elected steering committee. It buys legitimacy a self-selecting group can't claim, but costs a quarter to install and then a standing job. Nothing here calls for that yet — no foundation deadline, no contributor base bigger than the maintainer set. Revisit if either shows up.

**Also considered and rejected:** writing down today's arrangement as-is ("Kestrel decides"). Near-zero effort, but it buys no decision legitimacy at all — which is the exact thing making the two new maintainers wary. Not recommended.

## Decision rules — per class: who decides, threshold, timer, escalation

The vote-cap mechanism (self-set, not a published standard) is the load-bearing piece: **votes cast by maintainers employed by one organization count for at most 3 toward any threshold, no matter how many of that organization's people vote the same way.** With 7 maintainers, that produces two checkable facts:

- Simple majority is 4. Kestrel's capped 3 can never reach 4 alone — passing anything by vote needs at least one external maintainer on board.
- Two-thirds is 5. Kestrel's capped 3 plus one external maintainer is only 4 — reaching 5 needs *both* Munro Freight's and Alto Health's maintainers agreeing.

| Class | Decider | Threshold | Timer | Escalation |
|---|---|---|---|---|
| Routine change | any maintainer | 1 review + lazy consensus | — | none needed |
| Breaking / scope change | council | consensus-seeking; written proposal; objection must be technical | 10-day comment window (self-set, sized like Rust's final-comment-period practice, not copied from it) | unresolved after 30 days → council vote, simple majority (cap applies) |
| New maintainer | any maintainer nominates | no-objection window, else vote | 7 days | simple-majority vote (cap applies). **No new Kestrel-affiliated seat while Kestrel holds a seat majority, unless at least one external maintainer agrees** |
| Maintainer removal | council | two-thirds of all 7 (cap applies — requires both external maintainers) | 14-day open vote | none above council |
| Sablewire OSS release — **content** | council, via the breaking/scope-change track above | same as scope change | same | same |
| Sablewire release — **timing** | **reserved to the Kestrel-designated Release Owner** | no vote; not a council decision | published release calendar, minimum 5 business days' notice before a feature freeze | none — this is stated as Kestrel's operational right, not something that drifts into a promise later |
| Security response | named security team, ≥2 people, cross-company where possible | delegated, private | per SECURITY.md | escalates to council only after disclosure |
| Governance amendment | council | two-thirds of all 7 (cap applies) | 14-day open PR | none above council |

The split on releases is the important nuance: **what ships** goes through the normal scope-change track and the council; **when it ships** is Kestrel's, published in advance, because that's the actual operational need you described — Cloud rollouts tied to release cuts. Naming that split explicitly, rather than leaving "Kestrel controls releases" as one undifferentiated fact, is what keeps this from reading as broader control than it is.

## Neutrality — trademark, affiliation ratio, contribution agreement, minutes

You're not claiming Sablewire is vendor-neutral, and you don't need to — a company-backed project is a legitimate shape as long as it says so plainly instead of drifting ("neutrality by press release" is the failure mode, not company ownership itself). Run the four checks anyway, because your two new maintainers, and any future adopter, will:

| Signal | Finding | Read |
|---|---|---|
| Trademark, domain, registry | Kestrel-owned | Fine, if stated as a reserved right in the document (below) rather than left unstated |
| Maintainer affiliation | 2 of 7 (29%) outside Kestrel | Worse than the 2-of-5 (40%) ratio that flagged Redis as single-vendor pre-fork (sourced above). Worth knowing, not necessarily worth fixing by itself — the vote cap addresses the actual risk (outvoting), not the headcount ratio |
| Contribution agreement | not specified by you | Confirm whether Sablewire runs a CLA or a DCO. A broad-grant CLA is the lever that makes a future unilateral relicense possible; a DCO (inbound = outbound) doesn't concentrate that power. If a CLA already exists, this doesn't need reopening today, but say so in the document rather than staying silent. Route the actual text to counsel — not a governance question |
| Minutes | none published; decisions live in a closed Kestrel meeting | Recommend a short public decision log for the council's decision classes above. Kestrel's internal Sablewire Cloud product roadmap is a separate, legitimately private thing — it's a commercial plan, not an open-source governance decision, and shouldn't be conflated with it in either direction |

## GOVERNANCE.md — the document, ready to commit

```markdown
# Sablewire Governance

## Values and scope

Sablewire is a workflow engine. This document governs the open-source project:
what ships in it, who decides, and how maintainers are added or removed.
It does not govern Sablewire Cloud, Kestrel Data's hosted commercial product,
which is Kestrel's own to build and price.

## Roles

- **Maintainer**: merge rights, a vote in council decisions, listed in MAINTAINERS.md
  with current employer.
- **Release Owner**: designated by Kestrel Data. Sets and publishes the release
  calendar and cuts releases. Does not decide what code ships — see "Decisions" below.
- **Security team**: at least two maintainers, cross-company where possible, holding
  the security-report inbox. See SECURITY.md.

Merge rights and privileged credentials (release signing, registry publishing,
GitHub organization ownership) are granted separately. A new maintainer receives
merge rights on approval; credentials follow at least one supervised release cycle.

## Becoming a maintainer

Any maintainer may nominate a contributor after three months of sustained
contribution, including reviews given, not only pull requests merged. The
nomination passes if no maintainer objects within 7 days; an objection sends it
to a council vote (see Decisions).

No maintainer seat may be added for a Kestrel Data employee while Kestrel already
holds a majority of seats, unless at least one external (non-Kestrel) maintainer
agrees to the nomination.

## Removing a maintainer

Triggered by resignation, six months of inactivity with no stated leave, or a
conduct violation. Requires a two-thirds vote of all current maintainers (see the
vote cap in Decisions). Written down now so it is procedural, not personal, if it
is ever needed.

## Emeritus

A maintainer stepping back keeps credit in MAINTAINERS.md under an emeritus
section and loses merge rights and credentials. Reinstatement is a simple-majority
council vote.

## Meetings and communication

No standing meeting. Proposals and votes happen in public GitHub issues, labeled
`governance`. Kestrel Data's internal Sablewire Cloud roadmap discussions are not
part of this process and are not expected to be public.

## Decision-making and voting

- **Routine changes**: one maintainer approves, any maintainer merges.
- **Breaking or scope changes**: written proposal, 10-day public comment window,
  objections must state a technical reason. Unresolved after 30 days: any
  maintainer may call a council vote, simple majority.
- **Release content** follows the breaking/scope-change rule above.
- **Release timing** is set and published by the Release Owner, on behalf of
  Kestrel Data, to coordinate with Sablewire Cloud rollout schedules. It is not
  put to a vote. Minimum 5 business days' notice before a feature freeze.
- **New maintainers, removals, and amendments to this document** go to a formal
  vote when triggered by the rules above.

**Vote cap.** In any formal council vote, the votes of maintainers employed by a
single organization count for at most 3, regardless of how many of that
organization's maintainers vote the same way. With 7 maintainers: a simple
majority (4) always requires at least one vote from outside the capped
organization; a two-thirds vote (5) requires agreement from every maintainer
outside it. This applies to all classes above except release timing.

Abstentions do not count toward either the numerator or the denominator.

## Code of conduct enforcement

Handled under CODE_OF_CONDUCT.md. A maintainer who is the subject of a report is
excluded from deliberating it; if the whole maintainer group is implicated, it
escalates outside the project.

## Security response

Handled by the named security team under SECURITY.md, privately, until
disclosure. Team membership is reviewed every 6 months.

## Appeals and escalation

Any maintainer may ask for a decision to be reconsidered by opening an issue
labeled `governance-appeal`. The council responds in writing within 14 days.
A proposal that cannot reach agreement is explicitly declined or held — never
left open indefinitely.

## Trademarks and project assets

Kestrel Data owns the "Sablewire" trademark, the project domain, and the
package-registry account, and operates Sablewire Cloud as a commercial product
built on the open-source project. This is stated here so it is a known,
reserved position rather than an assumption anyone has to guess at. Any change
to this arrangement — including a future transfer to a neutral foundation —
is itself a governance amendment (below), not a unilateral Kestrel decision.

## Amendments

Two-thirds vote of all maintainers (vote cap applies), open for public comment
at least 14 days. This document is expected to change as the project and its
maintainer base grow; amending it is normal, not a crisis.
```

## Enforcement — repo settings and credential changes needed to match it

Written roles the repository contradicts are fiction, and it's cheap to check now while the group is small:

- Confirm branch protection and merge permissions on the default branch match the "maintainer" list in MAINTAINERS.md — no wider, no narrower.
- Confirm CODEOWNERS routing matches who actually reviews each area in recent commit history, not who used to.
- Confirm the GitHub organization has at least two owners, not one — and that at least one is not the sole Kestrel signatory on release signing and package-registry publish rights, so a single departure doesn't strand the release process.
- Confirm the security-report inbox has at least two current holders.
- Write down who currently holds the domain registration — this is usually the one nobody checks.

## Succession — trust ladder, inactivity rule, emeritus, end state

Both new maintainers already got merge rights immediately, which is the right move — merge rights are cheap to grant and cheap to revoke. Keep the next rung, privileged credentials (signing, publishing, org ownership), staged behind at least one supervised release cycle for any *future* maintainer, regardless of employer; that pause is policy, not distrust, and it's worth saying so in the document if it ever comes up.

- **Inactivity**: propose 6 months with no stated leave triggers emeritus.
- **Emeritus**: credit retained, rights removed, reinstatement by simple-majority vote.
- **End state**: if Kestrel ever deprioritizes the open-source project relative to Sablewire Cloud, that's a governance act to announce — archive or handover — not something to let go quiet. Worth naming now, precisely because Kestrel's commercial incentives and the OSS project's health won't always point the same direction.

## Foundation — needed or not, and the gap list if yes

**Not needed now.** You haven't described a need to receive outside donations, and the actual problem — two maintainers who need a checkable reason to trust the structure — is solved by the vote cap above, which costs almost nothing and is fully reversible. A foundation trade (giving up the trademark, the release process, and a reporting cadence for a neutrality credential) isn't warranted by anything in this brief.

Revisit if: an adopter beyond Munro Freight or Alto Health asks who controls Sablewire and won't accept "Kestrel Data, with a published vote cap" as an answer, or if outside sponsorship money starts arriving and needs a home.

## Review date

Before committing this document, confirm the three open items flagged above: actual credential holders, CLA/DCO status, and a real absence-factor computation from commit history.

- **6 months out (2027-03-24):** check whether the rules have actually run once — has a vote been called, has a nomination gone through the objection window, is the decision log populated. If nothing has run, that's the finding, not a pass.
- **Annual review (2027-09-24), and immediately if:** a maintainer is added or leaves, a third external company puts an engineer on the project, or a release-timing decision draws an objection that the reserved-right split doesn't actually settle.