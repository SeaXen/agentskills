The doc isn't the problem — the doc describes a governance model your infrastructure doesn't enforce. An OSPO review will test controls, not prose, so treat every mismatch below as a finding to close, in priority order.

## 1. Revoke access for departed employees (do this today)

Two people who left in 2025 still hold repo admin. This is the single most damning finding a reviewer can surface — "former employee retains write/admin access" is a checklist-failing item on almost every vendor security questionnaire, independent of anything else in the repo.

- Remove them from the GitHub org entirely, not just the repo — check for lingering deploy keys, personal access tokens, SSH keys, and any CI/CD secrets tied to their accounts.
- Confirm this is now part of the offboarding checklist (HR/IT ticket includes "remove from GitHub org"), because the root cause isn't "we forgot" — it's that no process forces it.

## 2. Turn on branch protection on `main`

Currently anyone with push access can force-push or merge without review — the doc's "release authority rests with the maintainer group" is unenforceable without this.

- Require pull request review before merge (require review from CODEOWNERS, at minimum 1 maintainer approval).
- Require status checks to pass.
- Disallow force-push and branch deletion.
- Require signed commits/tags if you want release provenance to mean anything to a reviewer.

Low effort, highest signal-per-hour of any item here.

## 3. Fix the admin list to actually match the four named maintainers

Nine admins against four documented maintainers means the doc's authority model has no teeth. Reduce repo/org admin to Ash, Bo, Colm, Dee. Everyone else gets `write` or `triage`, not `admin`. If someone needs elevated access for a specific reason, document why in GOVERNANCE.md rather than granting it silently.

## 4. Make CODEOWNERS reflect the area-owner model the doc claims

Right now everything routes to `@ravenbrook/core`, which is a single blanket rule — it doesn't reflect "three area owners for collector, exporters, and docs" at all, and it gives approval authority to someone with no commits in 19 months.

- Split CODEOWNERS by path: `/collector/` → the collector owner, `/exporters/` → the exporters owner, `/docs/` → the docs owner. Keep a narrower core/fallback rule for everything else.
- Resolve the inactive member explicitly: either they're still an area owner (then they need to actually review something before the audit, or the doc is fiction), or they're emeritus (remove from the team, credit them in GOVERNANCE.md as emeritus). Don't leave it ambiguous — a reviewer who cross-references CODEOWNERS against commit history will find this in under five minutes.
- Add an inactivity rule to GOVERNANCE.md itself (e.g., "no review activity in 6 months → moved to emeritus, can be reinstated on request") so this doesn't silently drift again.

## 5. Fix the registry publish bus factor

Only Bo can publish. That's a single point of failure that also contradicts "release authority rests with the maintainer group" — if authority is collective, publish capability can't be sitting in one person's personal account.

- Move publishing off a personal credential onto a scoped automation identity (CI-triggered release gated by required PR approval + tag protection), or
- At minimum, get a second maintainer enrolled as a publisher, with the credential stored in a secrets manager, not a personal token nobody else can rotate if Bo is unavailable.

## 6. Add what an OSPO review checks that isn't in GOVERNANCE.md at all

- `SECURITY.md` with a vulnerability disclosure process and named contact — commonly a hard checklist item.
- Confirm org-wide 2FA (and SSO, if the customer's OSPO cares about identity assurance) is enforced, not just recommended.
- A one-line note in GOVERNANCE.md on how maintainer/area-owner status is granted and revoked — right now it's a static list of names with no process, which is exactly how you end up with an admin list, a CODEOWNERS routing, and a doc that all disagree with each other six months from now.

## 7. Sequence against the review date

- **This week:** revoke ex-employee access, enable branch protection on `main`.
- **Week 2:** trim admin list to the four maintainers, split CODEOWNERS by area, resolve the inactive owner.
- **Week 3:** fix the publish single-point-of-failure, add SECURITY.md.
- **Before the review:** write a short dated note (even in GOVERNANCE.md's changelog or a CONTRIBUTING section) showing when this access review happened and that it's now a recurring practice — not just that things happen to look clean the week they show up. Reviewers weight "we audit this quarterly" higher than a repo that's merely clean by accident on inspection day.

Get reality to match the doc, not the doc to match reality — rewriting GOVERNANCE.md to describe "nine admins and one publisher" would pass a proofreading pass but fail the actual review.