# Governance review — Cinderpath

## As-is — what I know, what I'm inferring, what I still need from you

Known: 3 maintainers, 2 employed by the same consultancy, BUSL-1.1 license, no legal entity yet, sponsorship money currently has nowhere to land but a personal account, and someone (a board member, an adopter, SFC itself?) has told you to apply to Software Freedom Conservancy.

Inferred, confirm before you act on it: no written governance today (money defaulting to a personal account is what a project with no entity and no rule looks like); the third maintainer's employer is unknown to me; who currently holds the domain, trademark, and package-registry account is unknown; the contributor absence factor is unmeasured.

Get these three facts before your first conversation with SFC — they change the answer:

1. **Run the absence factor** off real commit/review/issue history (method in the succession playbook) — project-wide and per module. Three named maintainers doesn't tell you whether one of the three is actually irreplaceable in one subsystem.
2. **Who holds the domain, GitHub org, and trademark today** — a person's personal account is a bigger neutrality problem than anything else here, and it's a five-minute fix versus everything else on this list.
3. **What "two features" actually means contractually** — is the bank buying a services contract with named deliverables, or donating toward the roadmap? These need different homes (see Foundation, below).

## Concentration — the number that already trips a trigger

2 of 3 maintainers (a majority) share one employer. That is a worse ratio than the one that flagged Redis as single-vendor before its 2024 fork — there it was 2 of 5 (a minority) and that alone was enough for researchers and the eventual forkers to call it. A majority at one consultancy, on a project two commercial adopters are about to pay into, is already crossed, independent of anything you do next: *"One company employs a majority of maintainers → step 6 as a blocker: the affiliation ratio classifies a project as single-vendor, and no messaging changes it."*

This isn't a reason to panic, it's a reason to fix it now while it's cheap: recruit a maintainer or an active reviewer with no tie to the consultancy, or at minimum write a vote-cap clause treating the consultancy as one voting bloc (below). Foundation reviewers check this specific ratio before anything else — it's their #1 cause of delay.

## Recommendation — Maintainer council, with a seat cap

**Model: maintainer council** — the default at 3+ maintainers, an hour a month, reversible by one vote, and it buys exactly what an ad-hoc 3-person project is missing: a rule for deadlock and a rule for promotion.

**Modifier: organization-balanced voting**, because of the concentration above — the two consultancy maintainers vote as a single bloc (one vote, not two) on money, brand, license, and maintainer-roster decisions. Day-to-day merges stay on lazy consensus, unaffected.

Alternative considered and rejected: solo authority. You have three active people already; the actual open question is a money and neutrality rule, not who has final say on code.

## Decision rules — the classes this situation actually needs

| Decision | Who decides | Threshold | Note |
|---|---|---|---|
| Accept the $48k/yr sponsorship | All 3, consultancy pair as one vote | Unanimous-of-blocs | Record in a public note, not a private thread |
| Accept the bank's paid-feature contract | All 3, consultancy pair as one vote | Unanimous-of-blocs | Recuse if the contract routes through the consultancy itself (see below) |
| Fiscal host / SFC application | All 3 | Two-thirds | Long window (10+ days), written proposal |
| Adding/removing a maintainer, license, trademark | All 3 | Two-thirds | Same |
| Routine code | Any maintainer | Lazy consensus | Unchanged |

**Write a conflict-of-interest clause now**, not later: if the bank's payment for "two features" is actually a services contract with the consultancy (rather than money into the project), the third maintainer signs off independently and it's disclosed in the public note. This is the exact pattern a bank's own procurement/legal review is trained to look for in a shared dependency — don't let it default into place silently.

## Neutrality — four checks, run today

1. **Trademark/domain/registry**: confirm and consolidate off any single personal account — cheapest, highest-leverage fix available to you this week.
2. **Affiliation ratio**: 2/3, majority-single-employer — already tripped; fix by recruiting or by the vote-cap above.
3. **Contribution agreement**: if none exists, that's neutral by default (no CLA means no concentrated relicensing lever) — don't add one casually while a licensing question is already open; that's a question for counsel, not this review.
4. **Minutes**: none evident. Start a public log now — it costs almost nothing and is exactly what a foundation reviewer checks for "governance documented but never exercised."

## GOVERNANCE.md — right-sized draft, ready to edit

```markdown
# Governance

## Scope
[Maintainer A], [Maintainer B], and [Maintainer C] maintain Cinderpath.
[Maintainer A] and [Maintainer B] are both employed by [Consultancy]; this is
disclosed here, not hidden, and is the reason for the voting rule below.

## Roles
- Maintainers: A, B, C. Merge, release, and decide direction.
- Release keys / registry publish rights: [name current holders; add a second
  holder for any row held by only one person].
- Contributors: anyone with a merged change.

## Decisions
Routine changes: one maintainer approves; any maintainer may merge.
Money (sponsorships, paid contracts), license, trademark, or maintainer
roster: all three must agree. [Maintainer A] and [Maintainer B], as employees
of the same consultancy, vote as a single bloc on these classes. A proposal
sits in a public issue for at least 10 days before it is decided.
Any decision that would pay [Consultancy] directly, or route adopter money
to it instead of the project, requires [Maintainer C]'s independent
sign-off, recorded in the same issue.

## Adding a maintainer
Three months of sustained review activity, then all three current
maintainers agree; the consultancy affiliation of a nominee is disclosed,
never a bar to nomination, but does not get a second vote if it duplicates
an existing employer already on the council.

## Stepping back
A maintainer inactive for six months with no return date moves to emeritus,
credit kept in MAINTAINERS.md; credentials rotated within 30 days. If all
three step back, we will name a successor or archive the repository
publicly rather than leave it silently unmaintained.

## Changing this document
Two of three maintainers agree, open for at least 10 days, consultancy pair
counted as one vote as above.
```

Fill in names and actual credential holders before committing it.

## Enforcement

- Match repo settings to the roles above: who can merge, who can publish, who owns the GitHub org — once you know the real current state (open item above).
- Get the money out of a personal account before you accept either offer. That's not a foundation question, it's a "your accountant is right" question — you need *some* legal receiving entity (a fiscal host is the cheapest form of one) before either check clears, independent of whether SFC works out.

## Succession

- Target absence factor of at least 2 now, raise to 3+ once the sponsorship and bank contract are both live — you now have paying adopters, which is exactly the trigger the baseline says to raise it on.
- Inventory credentials (repo/org ownership, signing keys, registry publish, domain/DNS, security inbox, the new funding account) and get two current holders on each row — right now the money-in-personal-account fact suggests several of these rows have exactly one holder.
- Write the inactivity definition and emeritus path now, while nothing is on fire; it's nearly free today and expensive to improvise later.

## Foundation — this is the actual crux, and it splits into two separate questions

**1. Does Cinderpath even clear SFC's door?**
Software Freedom Conservancy's own published fiscal-sponsorship terms require a license that is both OSI-approved and DFSG-free. BUSL-1.1, as generally written, is not OSI-approved — it restricts competitive/commercial use during the embargo period, which is exactly what the Open Source Definition excludes. That's a fact about SFC's stated intake bar, not legal advice about your license — and it's a **gate, not a ranking**: it can block the application outright rather than just cost you a step.

Two things worth doing before assuming it's a dead end, neither of which is a decision I can make for you:
- **Ask SFC directly.** If Cinderpath's BUSL text already has a Change Date that converts it to an OSI-approved license (Apache 2.0 is the common choice — this is the same shape as CockroachDB, Sentry, and others), tell them that; it may change their read. This is a question for SFC and for counsel, not for this review.
- **Consider a lightweight fiscal host as a stopgap for the $48k specifically** — no license gate stated for that tier, just donation plumbing, at the cost of the legal/licensing services SFC would otherwise provide.

**2. Where does the bank's money for "two features" actually go?**
That reads like a services contract with deliverables, not a donation — a different instrument from fiscal sponsorship, and it may not need a foundation at all. It may just need an entity to invoice through. If that entity ends up being the consultancy, say so in the governance doc (the conflict-of-interest clause above), rather than let a bank's procurement review discover it on their own.

**On the 15–20% archival figure**: don't use it. It's explicitly flagged as an unverified, commonly-repeated number with no foundation's own data behind it — not a planning input. It also doesn't map to what you're doing: that stat describes CNCF-style sandbox→graduation maturity tiers, not a fiscal-sponsorship arrangement like SFC's. The real, sourced risk to plan around instead is **exit friction** — a fiscal sponsor holding assigned assets typically can't transfer them back to an individual or a for-profit, and a fiscal host can itself dissolve (a charitable host affiliated with Open Collective gave ~600 collectives roughly seven months to move funds in 2024). Ask SFC what happens to Cinderpath's assets and unspent funds if either side ever wants to leave, and get that answer before signing, not after.

**Readiness gaps, in fix order:**
1. Resolve the OSI-license question with SFC and counsel — blocker, not a queue position.
2. Fix the 2-of-3 consultancy concentration — recruit, or ship the vote-cap clause now.
3. Decide and disclose where the bank's contract money goes.
4. Move domain/trademark/registry off any personal holder.
5. Commit the GOVERNANCE.md above and exercise it once (even a small real vote) before or shortly after applying.

## Review date

Re-run this once you have SFC's answer on the license, once the bank contract is signed or declined, and in any case within two quarters or on any maintainer-roster change.