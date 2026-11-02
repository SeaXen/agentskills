# Open-Source Fund Rules — [Company]

Two problems in the brief need fixing before this goes to a vote, not after: a staff engineer's own project is on the ballot, and one candidate has no way to receive a donation at all — it only sells support contracts. Both are exactly the failure modes the reference model for this kind of fund (the FOSS Contributor Fund, O'Brien & Grover, O'Reilly 2021 — Ambrose's "$8,000/month, one project a month" design is a close variant of that model's own $10,000/month reference implementation) was written to prevent. The rules below build the fixes in as standing policy, not one-time exceptions, and are meant to be published internally before the first ballot opens.

Mandate: this is an **internal engagement** fund — it's judged on participation and contribution, not on brand reach or dependency coverage. Say that plainly in the announcement so nobody benchmarks it against a supply-chain or PR program later.

---

## 1. Why we fund

We give engineers a direct, visible say in supporting the open-source projects our work depends on, and we back that support with real money every month.

## 2. What we fund — eligibility (checked before a project reaches the ballot, never after)

A project qualifies only if **all four** are true:

- We actually use it (someone can point to it in a lockfile, SBOM, or a service's dependency list).
- It carries an OSI-approved license.
- It has a working mechanism to *receive a sponsorship or donation* — a GitHub Sponsors / Open Collective / equivalent link that resolves, checked live, not from memory.
- It is **not maintained by a current employee.**

A project failing any filter doesn't go to a vote. It's dropped from that cycle's ballot and the reason is recorded.

Applied to your two named candidates:

- **ferrite-queue is disqualified.** It fails the fourth filter, and that filter isn't optional colour on top of the model — the published reference implementation lists "not maintained by an employee" as one of its four *required* criteria, and every existing rule about employee-owned projects in this org points the same way. Beyond the rule itself: a company-wide Slack poll paying a monthly stipend into a staff engineer's own repo reads as self-dealing whether or not it's earned, and it wouldn't count as real open-source giving under the closest published reporting standard (the Open Source Pledge explicitly excludes "a maintainer the company already employs" from what counts). Keep the engineer's work recognized some other way — an internal shout-out, a conference talk slot — just not through this fund.
- **The support-subscription-only candidate is disqualified**, on the third filter. A paid support contract is a commercial services purchase with deliverables attached (an SLA, a vendor relationship) — not a sponsorship. Funding it through this program would also fail the same non-incidental-benefit test the pledge standard uses to reject "strategic sponsorships" that are really services contracts in disguise. If the company genuinely wants that support contract, buy it — through normal procurement, on its own budget line, not this fund's.

## 3. How much, how often

- **$8,000 per month, one project per month.** $96,000/year committed through a single recurring line, in line with the reference model's monthly cadence.
- Recurring by default: a project that wins isn't a one-off gesture, it's this cycle's answer to "who did the company back this month."
- Flag the operational cost up front: because the winner changes monthly, up to 12 different maintainers a year go through vendor onboarding — tax forms, sanctions screening, invoicing setup. Start that paperwork the moment a winner is announced, not when the first payment is due.

## 4. Getting onto the ballot

- **Anyone can nominate**, no prerequisite. Restricting nominations to people with linked accounts measurably suppresses turnout — don't do it.
- Run the eligibility filters (§2) on every nomination before it's added to the ballot.
- **Don't let the ballot be famous-frameworks-only.** Ten big-name projects sourced from a survey is exactly the failure mode this model warns about by name: open voting drifts toward whatever's already well-funded, and a famous framework with a foundation behind it needs your $8,000 far less than a small library holding up a critical path with one maintainer. Before the first ballot goes live:
  - Verify each of the ten survey picks is actually in use in our stack (pull the lockfile/SBOM — don't take "everyone's heard of it" as evidence of dependency).
  - Add at least 2–3 candidates sourced from the dependency graph itself, favoring ones with thin maintainer counts or no existing sponsor — not from the survey.
- Reuse the ballot as a standing menu: post it somewhere permanent so employees who want to start contributing know where to look.

## 5. How the winner is chosen

- **One Slack poll, single-select, one vote per person.** Restrict it to real employee accounts (exclude guests/bots) — a company-wide poll with no gate on who can vote is easy to game with duplicate or automated entries.
- Poll stays open a fixed window — 3 business days — announced in advance.
- Winner is the option with the most votes at close.
- **Tie-break, decided in advance, never improvised after the fact:** a 24-hour runoff poll between the tied options; if still tied, a coin flip, logged publicly with the result.
- **Cooldown rule:** a project that wins is ineligible for the next 6 months. Without this, the same 2–3 famous frameworks will win every month indefinitely — the fund exists to spread engagement, not to repeatedly re-fund whoever has the most name recognition in a poll.

One open call for Ambrose: this design puts the vote to the *whole company*, which is simpler to run and more inclusive than the reference model's version — where only employees who made an open-source contribution that cycle earn a vote, specifically to make the fund double as a contribution incentive. Whole-company voting is a legitimate choice; just know it trades away that incentive effect and makes the poll closer to a popularity contest. If that matters later, the fix is cheap: gate voting to anyone who logged one qualifying contribution that cycle, nothing more.

## 6. What sponsorship does not buy

No roadmap input. No priority handling on our issues. No obligation to mention us, thank us, or answer us faster than anyone else. State this to the winning maintainer before the first payment, every month.

## 7. Conflicts of interest

Projects maintained by a current employee are ineligible (§2). If a close call comes up that isn't a clean employee-maintainer case — an employee is a significant *contributor* but not the maintainer, for instance — the fund owner decides and records the reasoning; don't leave it to the poll.

## 8. Disclosure

Employees who publicly advocate for a project this fund has sponsored disclose the relationship (e.g., in a blog post or conference talk).

## 9. Payment path

- $8,000/month clears the $5,000-per-invoice minimum on invoiced corporate billing comfortably, so set the company org up on invoiced billing once, up front.
- **Do this before the first cycle's winner is announced** — switching an org to invoiced billing cancels any sponsorships already live on that platform, and a winner announced first, then cancelled by a billing-mode switch, reads as a withdrawal.
- If a monthly winner isn't on that platform (no incorporated entity, individual maintainer), route through a fiscal host instead — expect a 3–10% cut and a public ledger.

## 10. Measurement

Track engagement, not dollars:

| Metric | Why it matters |
|---|---|
| Employees contributing per cycle | This is what the fund exists to grow |
| Nominations submitted per cycle | Signals whether the ballot stays fresh or goes stale |
| Participation rate in the vote | Whether it's read as real or ignored |
| Policy breaches raised | Should be zero, every cycle |

Ignore "total dollars given" as a success metric — it's fixed by design ($8,000 × 12), so it tells you nothing about whether the program is working.

## 11. Reporting

Publish once a year, internally at minimum: the year, total paid, the twelve winners and amounts, participation numbers, and one honest paragraph on what didn't work. That last paragraph is what keeps this a program instead of an announcement.

## 12. Contact

Name one owner (not "OSPO" or "the fund") who runs the monthly cycle, checks eligibility before each ballot, and answers questions about why a project was or wasn't included.