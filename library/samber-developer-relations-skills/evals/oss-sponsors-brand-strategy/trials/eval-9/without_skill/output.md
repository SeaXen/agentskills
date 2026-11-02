# Open Source Sustainability Fund — Program Rules

## 1. Purpose and budget

- Fund $8,000 per month to exactly one open-source project, chosen by company-wide vote.
- Renew the ballot every month. A project can win more than once, subject to the cooldown in §4.
- Owner of this program: CTO office, operationally run by [designate a program admin — do not leave this unowned].

## 2. Eligibility screen (runs before anything reaches a ballot)

Every candidate — seed-ballot or later nomination — passes this screen before a vote, not after.

1. **Genuine open-source project.** OSI-approved (or equivalent) license, public repository, governance not controlled by a single company's product roadmap.
2. **Real donation channel.** Money must reach the project's maintainers or fiscal host (GitHub Sponsors, Open Collective, Tidelift, Software Freedom Conservancy, Apache/Linux Foundation, etc.) as a donation — not as payment for a commercial product.
3. **Not a disguised vendor purchase.** If a candidate's only monetization is a paid support subscription — no independent donation path, the "project" is effectively a company's product — reject it from the fund. Paying for that subscription is a legitimate business expense, but it is procurement, not a donation, and must go through normal vendor approval (security review, contract, budget owner sign-off), never through this poll. Do not let it appear on the ballot dressed as open-source funding.
4. **Dependency or need, not just fame.** Require that at least half of each month's ballot be projects the company actually depends on (check the dependency graph) or that show real funding need (small maintainer count, no major foundation backing) — not exclusively "big frameworks everyone has heard of." A mega-project with existing corporate sponsorship from ten other companies needs your $8,000 less than a two-maintainer library holding up your build. Popularity earns a nomination; it does not exempt a project from this balance requirement.

Anything that fails screen items 1–3 is removed from the ballot before the poll opens, full stop — it does not go up for a vote and then get explained away afterward.

## 3. Conflicts of interest — mandatory disclosure

Any candidate maintained, founded, or meaningfully monetized by a current employee (this includes ferrite-queue) stays eligible, but only under these conditions:

1. **Flag it on the ballot itself.** The Slack poll entry for that project must state, in plain text, "Maintained by [employee], [team]" — visible to every voter before they vote, not footnoted after.
2. **Maintainer recuses.** The employee does not vote in that month's poll and does not campaign for it (no Slack posts, no DMs asking for votes) while it's an active candidate.
3. **Second sign-off before payout.** If an employee-linked project wins, the program admin and Finance approve the disbursement explicitly, in writing, before money moves — separate from the vote itself. This isn't about blocking the payout; it's about making sure company funds flowing toward a staff member's own project were never rubber-stamped by a poll alone.
4. **No personal accounts.** If the maintainer's donation channel is a personal GitHub Sponsors/Patreon rather than a project-level or foundation fiscal host, do not send funds there. Ask the maintainer to route it through a neutral fiscal host, or treat it as a bonus/compensation matter and take it out of this program entirely.

Apply the same three steps to any future candidate with an employee tie — this rule is general, not a one-off carve-out for ferrite-queue.

## 4. Ballot composition and rotation

- **Seed ballot (month 1):** the 10 projects from the engineer survey, after they clear §2 and are flagged per §3 where applicable. If more than half are "big frameworks everyone has heard of," pull in survey runner-up candidates so the dependency/need balance in §2.4 is actually met — don't launch a ballot that's 9 famous frameworks and 1 outlier.
- **Later months:** open a standing nomination channel (Slack form or similar). Any employee can nominate; the program admin runs the eligibility screen before adding it.
- **Cooldown:** a project that wins sits out the following 6 months before it can return to a ballot, so the fund doesn't default to the same winner every month once one project builds a Slack voting bloc.

## 5. Voting

1. Poll runs in a company-wide Slack channel, open to every employee, one vote per person, visible for [set a window — e.g., 5 business days].
2. Highest vote count wins. Tie: run a 24-hour run-off poll between the tied projects; if still tied, the program admin casts the deciding vote.
3. Publish vote counts after the poll closes. No anonymous late changes to tallies.

## 6. Disbursement

1. Pay through the project's official fiscal host, not an individual's personal account, whenever one exists (see §3.4 for the employee-maintainer case).
2. If the winning project has no channel that can receive $8,000 in one donation (common for indie maintainers on $5–50 sponsor tiers), the program admin finds the closest equivalent — a foundation umbrella, Open Collective, a one-time invoice arrangement with the maintainer — rather than silently sending less than $8,000 to a tier cap.
3. Keep a paper trail: recipient, amount, channel, date, and the §3 sign-off if applicable. Finance needs this for books and tax treatment regardless of program size.
4. If a project can't accept funds within 30 days for any reason, reallocate that month's $8,000 to the runner-up, don't let it roll over silently.

## 7. Review

- Revisit this document every 6 months: is the ballot still balanced per §2.4, is the cooldown working, has any conflict-of-interest case come up that these rules didn't anticipate.
- Any change to budget, cadence, or eligibility criteria needs CTO sign-off, not just program-admin discretion.