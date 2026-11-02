# Governance review — Ravenbrook

## As-is — who decides today, by what implicit rule, where it has failed

GOVERNANCE.md states: four maintainers (Ash, Bo, Colm, Dee), three area owners (collector, exporters, docs), release authority with the maintainer group. That's a **maintainer council** — the right-sized default at 3–8 maintainers. The model isn't the problem. The repository doesn't implement it:

- **Admin ≠ maintainer list.** 9 accounts hold repo admin; the doc names 4 people. Two admins left the company in 2025 — access wasn't revoked at offboarding.
- **No enforcement mechanism.** Branch protection is off on `main`. Nothing requires review, status checks, or blocks force-push. The written "maintainer group decides" rule has no technical backing — anyone with write access can bypass it today, admin or not.
- **Review routing contradicts the area-owner model.** CODEOWNERS sends everything to `@ravenbrook/core`, not per-area. That team contains Ash and one person inactive 19 months. The three named area owners for collector/exporters/docs aren't in the routing at all — either they were never added, or the doc describes a structure CODEOWNERS never implemented.
- **"Release authority rests with the maintainer group" is fiction at the credential layer.** Only Bo can publish to the registry. Whatever the group decides, one person executes it, and that person is a single point of failure regardless of what the vote says.

This is a **Step 5 (enforceability) failure**, not a model failure: written roles the repository contradicts read as theatre to a reviewer, and an OSS office checks repo settings before it reads prose.

## Concentration — absence factor, employer spread, credential holders

Can't compute a real contributor absence factor (CHAOSS metric: smallest number of contributors responsible for 50% of contributions) without commit history — pull it before the review, per area (collector, exporters, docs) and project-wide, not just overall. Project-level numbers routinely hide a subsystem one person owns, and CODEOWNERS already signals that's happening here: everything funnels through a team where only Ash looks active.

Credential inventory, from what's given — fill the blanks before the review:

| Credential | Holders | Verdict |
|---|---|---|
| Repo/org admin | 9, incl. 2 departed (2025) | 🔴 over-provisioned, includes ex-employees — a live security gap, not a governance nuance |
| Branch protection on `main` | nobody enforces it — it's off | 🔴 the "maintainer group" release rule has no mechanism behind it |
| Registry publish | Bo, alone | 🔴 absence factor of 1 on the one credential the doc claims is collective |
| Review routing (CODEOWNERS) | `@ravenbrook/core` = Ash + 1 inactive (19mo) | 🔴 effectively 1 active reviewer for the whole repo, despite 3 named area owners |
| Trademark / domain / registry account ownership | unknown | ⚠️ verify before the review — this is the highest-weighted neutrality signal |
| CI secrets, deploy tokens | unknown | ⚠️ verify — 9 admins is a proxy signal this is also over-exposed |
| Security report inbox | unknown | ⚠️ verify |

Target, self-set (not a published standard — the smallest value where no single departure stops a release, per the CHAOSS factor plus the "survives one withdrawal" test foundations use): **absence factor ≥2, two current holders per credential row.** Registry publish and admin both fail this today.

## Recommendation — model chosen, alternative considered, monthly hours

Keep the maintainer council. Four maintainers, one shared area, no election history, no visible founder-departure or multi-payroll pressure forcing an elected committee — nothing here promotes past row 1 of the model ranking. **Don't propose a governance model change for this review.** Adopting a heavier model (steering committee, federation) weeks before an external review, with zero history of using it, is the named anti-pattern in this skill's evidence base — it reads as staged for the reviewer, and reviewers check for exactly that.

What changes is enforcement, not shape: ~1 hour/month to run the council as written, reversible by one vote — the fix is making the repo match that hour, not buying a more expensive model.

## Decision rules — per class: who decides, threshold, timer, escalation

The one class actually broken: **release.** "Release authority rests with the maintainer group" doesn't name a mechanism — it's the unbounded-and-unenforceable shape this skill flags as bad ("consensus is reached" has no test; this has no decider either, at the credential layer). Split it into two clauses that can each be checked against the repo:

> **Release approval:** any two maintainers agree a release is ready; either may tag it. Disagreement blocks the release until resolved.
> **Release execution:** release-signing and registry-publish rights are held by at least two maintainers at all times, granted only after each has completed one supervised release cycle. No release ships from a credential held by one person alone.

Also write, since none of these exist yet:

- **New maintainer / area owner:** self-assessable criteria (time + non-trivial merges + reviews given), nomination + no-objection window or vote. Name who the three current area owners actually are — the doc references the role, not the people.
- **Removal / inactivity:** define inactivity in months (6–12 is the common range CNCF templates and GitHub's Minimum Viable Governance both use — self-set, not a law) and route to it. The 19-month CODEOWNERS holder clears any of those thresholds.
- **Admin/credential grant and revoke:** who can add/remove org admins, and a trigger tied to offboarding — this is what let two departed employees keep access into 2026.

## Neutrality — trademark, affiliation ratio, contribution agreement, minutes

An OSS office review checks these four signals, roughly in this order of weight, and none are addressed by the current document:

1. **Trademark, domains, registry account ownership** — not stated. Verify who legally holds "Ravenbrook" and the registry account itself, separate from who has publish *access*. A company-held mark next to a single-employee publish key is the cheapest way to fail this signal.
2. **Maintainer affiliation ratio** — verify how many of Ash/Bo/Colm/Dee are employed by the company behind Ravenbrook, versus external. If it's 4/4, that's not disqualifying by itself, but it must be disclosed, not discovered — the Redis case (2/5 outside the controlling company) is the pattern reviewers pattern-match to, and it was a leading indicator years before it mattered.
3. **Contribution agreement** — unknown; if there's a CLA, check whether it concentrates relicensing rights. Not urgent for this review unless asked.
4. **Published minutes** — unknown, likely absent. Not a blocker for a single-vendor stadium project, but its absence plus everything above reads as compounding evidence, not an isolated gap.

If Ravenbrook is in fact single-vendor (all four maintainers on one payroll), don't try to hide that before the review — state it and show the mitigations this skill recommends for company-backed projects: an explicit statement of what the company reserves (release timing, roadmap, hosted product), and public decision-making. What sinks a review is an assurance that drifts under questioning, not a disclosed limit.

## GOVERNANCE.md — additions, not a rewrite

The document's shape is right; it's missing the sections that would have caught this drift. Add:

- **Roles**, split explicitly: *merge rights* (who can merge) vs. *privileged credentials* (org admin, release signing, registry publish) — currently the doc implies these travel together ("release authority rests with the maintainer group"); the repo proves they don't.
- **Removing a maintainer / inactivity**, with a number in months and a named threshold (two-thirds of remaining maintainers is the common default).
- **Emeritus**, so the 19-month-inactive CODEOWNERS holder has somewhere to go that isn't silent removal.
- **Trademark and project assets**, factual statement of who holds the name/domain/registry account — this is the clause an OSS office reads first.
- **Amendments**, threshold and window, so this review's fixes are themselves made under a written rule rather than an ad hoc patch the week before an audit.

Everything else in the current doc passes the "has this project done this or will it plausibly do it this year" test — leave it.

## Enforcement — repo settings and credential changes needed to match it

In order, cheapest and most urgent first:

1. **Revoke the two departed employees' admin today.** This isn't a governance nice-to-have, it's an open incident — a credential held by someone no longer at the company is exactly the row the succession playbook calls "a security incident waiting to be discovered." Don't wait for the rest of this review to land.
2. **Turn on branch protection on `main`**: require review (matching the written maintainer-approval rule), require status checks, block force-push. This is the single change that makes "the maintainer group decides" true instead of aspirational.
3. **Cut repo admin from 9 to a justified list** — admin is for org/credential management, not for review rights; most of those 9 probably only need merge or triage access, not admin.
4. **Rewrite CODEOWNERS per area** — collector, exporters, docs routed to their named owners, `@ravenbrook/core` as fallback only, not blanket. Remove or replace the 19-month-inactive member.
5. **Add a second registry publisher** among the maintainer group, granted after one supervised release cycle (the minimum separation that would have slowed the xz-utils takeover — cite it as that, not as an arbitrary rule).

## Succession — trust ladder, inactivity rule, emeritus, end state

- **Inactivity definition:** adopt 6 months at minimum (matches the low end of the common CNCF/GitHub MVG range); the 19-month CODEOWNERS holder should already be emeritus under it.
- **Trust ladder:** separate what's currently conflated — reviewer/CODEOWNERS routing (area owners) from admin (org management) from key-holder (registry publish). Grant admin and publish rights on evidence measured in months, never in the same act as merge rights.
- **Emeritus path:** credit kept, rights removed, listed separately, reinstated by simple majority if they return.
- **End state:** not triggered here — four active maintainers, no departure in progress. Don't build a succession crisis narrative where there isn't one; just close the credential gap.

## Foundation — needed or not, and the gap list if yes

Run the three-question test: Money — not mentioned, no. Neutrality — yes, a prospective customer's OSS office is the trigger. Autonomy budget — unstated.

Only one of three is live, and it's answerable without a fiscal host: the customer wants evidence no single company can walk away and break the project, and that's what steps 5–7 above produce (working branch protection, correct CODEOWNERS, no orphaned credentials, disclosed affiliation ratio). **Don't pursue foundation membership for this review** — it's the anti-pattern this skill names explicitly (adopting a heavy structure right before a review it wasn't built for reads as staged). Hold it in reserve: if the customer's procurement process specifically *requires* foundation-backed neutrality (some do, contractually), that's a different, later conversation — ask them directly rather than pre-empting it.

## Review date — when this is re-examined, and what triggers it sooner

Target completion **2 weeks before the review** (so roughly by 2026-10-08, if the review is "next month" from 2026-09-24) — that leaves time to re-check before the customer looks, not to be still fixing things during it. Sequence:

1. Now: revoke departed-employee admin (today, not part of the scheduled work).
2. This week: branch protection on, admin list cut, CODEOWNERS rewritten.
3. Following week: registry publish shared to 2 holders, GOVERNANCE.md sections added, inactivity/emeritus applied to the 19-month CODEOWNERS holder.
4. Before the review: confirm affiliation ratio and trademark/registry ownership facts are known and, if single-vendor, stated plainly rather than left for the reviewer to discover.

Pass gate before calling this done — the skill's own health check: rule coverage (release + removal + inactivity now written), concentration (no credential row with one holder), alignment (zero contradictions between doc and repo settings, checked directly, not assumed), timers (every class has a clock). Re-run **after the review** regardless of outcome, and annually after that, or sooner if a fifth admin gets added, a maintainer leaves, or the company adds a second organization's maintainers (which would reopen the affiliation-ratio question in the other direction).