Do these three first. Total about 1.5 hours.

1. Drop the banner and the daily ping (below). 5 min.
2. Do not merge the audit-log PR yet. Post the reply below. 10 min.
3. Email the logistics company and the bank with the quote below, to validate the boundary before you write Pro code. 30 min each.

I did not see the repo or the PR. I only had your message. The interview answers I lack are marked **DRAFT**.

# Monetization plan - Brasswick - 2026-10-23

## Goal - DRAFT
- Goal, monthly net target, date and weekly hours are unknown. Send them and I will fill this in.
- The 8 named companies cap the revenue you can see. At the Business band ($6k/yr), all 8 buying would be about $48k/yr, roughly $4k/month. None of the 8 has committed to buy.
- Plan size: side income plus a co-maintainer's hours. A salary needs more organizations than you can name today.
- Baseline check: compare the first-year revenue per hour with a paid maintenance job at a company that depends on Brasswick.

## Gates
| Gate | Result | Evidence |
|---|---|---|
| Buyer | Pass | 8 named production users, 2 of them (a bank and a logistics firm) asked for SSO. They asked for a feature, not yet to pay. |
| Audience | n/a | Paid content is not the chosen option. |
| Ownership | Pass | MIT core. Pro is new code you write alone, so it is yours to sell. No license change is needed. |
| Shape | Pass for the add-on | It is a self-hosted server. Hosting is deferred unless one of the three of you wants to run production. |
| Capacity | DRAFT | My estimate, not a benchmark: 6 to 10 h/week standing. That covers module upkeep, 2 capped contracts, buyer email and renewals. Compare it with your budget. |

## Chosen offer
- Primary: a paid add-on on the MIT core, the **Pro** package.
- Secondary: 2 capped support contracts with the logistics firm and the bank, sold first. They bring revenue in weeks and show what they would pay for before you build.
- Rejected: relicensing and a commercial license on a next major (no need, and fork risk), and hosting (deferred).

## Paid boundary
The test is whether an organization needs it and a solo developer does not, and whether a competent user could build it in a weekend.

**Pro v1**
- SSO (OIDC and SAML, one IdP). Both named buyers asked for it, so it stays paid.
- Advanced audit: retention, tamper-evident storage, export or streaming to a SIEM, attribution to SSO identity, and a query UI.

**Candidates, not yet validated.** Keep them out of v1 until a named company asks.
- Change approvals (four-eyes) and per-environment RBAC. Banks plausibly pay for these.
- Per-environment rate limiting on the evaluation API. This is the weakest candidate: a reverse proxy does it in an hour, which fails the weekend test.

**Percentage rollouts and targeting rules: keep them free.**
- Rollouts are a core flag primitive, so everyone needs them (Perham's rule).
- If the free server already ships them, paywalling them is retroactive gating, which is the move that produces forks.
- Sell org-scale governance (approvals, promotion between environments) instead.

**Always-free list.** Publish it before you ship Pro.
- Everything in the current release, including rollouts, targeting, the evaluation API and the existing auth.
- Security fixes for the free server for the current major plus a stated window. You choose the length.
- Docs needed to use the free server.
- Data export.
- Community contributions.
- No banner, no phone-home and no license check in the free server.

**Design.** The free core gets small interfaces (`AuthProvider`, `AuditSink`) with defaults: the standard auth and a structured log line. The Pro module implements them. Deliver it privately as a separate image or module with a per-customer token.

**Pull-request rule.** Written now, so the first one is not improvised. A PR that adds a paid-list feature to the free core is declined with a written reason, unless the feature is something everyone needs. Then it moves to the free list and stays there.

## The audit-log PR
**Do not merge it as is.**
- Merged code is community-contributed. You may never paywall it later.
- If you merge it before the always-free list is published, you cannot move that feature to Pro.
- It also gives away most of the audit value your bank buyer would pay for.

Reply:
> Thanks. Audit logging is on our roadmap. Before it lands I need to publish what stays free. Could you narrow this to structured audit events emitted through an `AuditSink` interface, with a default log writer? That stays free and ships. Storage, retention, export and a query UI will be a separate paid module. If you'd rather keep the full scope, I'll decline with thanks.

- Review the PR for what it does first. If it already matches the narrow shape, merge it after the always-free list is published.
- Never copy its code into Pro.
- Resolve this within days. Do not leave it open for months.

## Banner and daily ping: cut both
**Never** put telemetry, phone-home or license checks in the free code (Moq, 2023: a sponsorship check that sent hashed developer git emails drew a public backlash and was removed within a day).

- The ping hurts the exact buyers you want. Banks and logistics firms often run air-gapped, and an outbound call fails their security review.
- Counting users is data collection, which is GDPR-sensitive.
- A banner changes free behavior, which breaks the always-free list.

Do this instead:
- Pro uses an **offline signed key**, verified locally inside the Pro module only. Say so in the FAQ.
- The Pro module sends no data either.
- Nudge upgrades with the docs, the README, release notes, and a reply with the Pro link on every SSO or audit issue.
- Reach the 8 named companies directly.

## Price shape
- **$19 per developer per month: drop it.**
  - It has no sourced basis.
  - It is the pattern the skill says to avoid: per-developer with no organization band (FluentAssertions drew the strongest recent fork).
  - It needs a developer count. You cannot verify one without the phone-home you are giving up.
  - Adding a developer raises the bill, which pushes customers to hide seats.
- **Draft bands, per organization, annual only.** These are my starting point for the quote conversations (self-set, not sourced).

| Tier | Developers | Price | Purchase |
|---|---|---|---|
| Team | up to 20 | $1,500/yr | card checkout |
| Business | up to 100 | $6,000/yr | invoice or PO |
| Enterprise | over 100 | quote, opening at $15,000/yr | PO, security pack, custom terms, SCIM later |

- Sourced anchors (River Pro, Sidekiq Pro and Enterprise, Faktory) are in `references/case-evidence.md`:
  - River Pro is $125/month for up to 20 developers, about $1,500/yr, the source of the Team figure.
  - Sidekiq Pro was $1,000/yr and Enterprise $2,000/yr in 2017, later $99/month and from $269/month.
  - Faktory Enterprise is $299/month for its first pack.
- No sourced figure supports my Business and Enterprise numbers. Test them on the bank, which is the one buyer able to pay the top band.
- Ceiling to check: what the bank would spend to build SSO and audit itself. A senior developer's month costs more than a year of Pro.
- Run a price review at two quarters after GA, and raise prices for new accounts only.
- **Who invoices:** a merchant-of-record service, or your own entity. Tell me your country and I will narrow it. Ask an accountant.

## Rights - DRAFT
Check these before selling anything.
- Register the Brasswick name as a trademark. Counsel picks the jurisdictions.
- Do you hold the name, domain and registry accounts? Have you written "free forever" or "never commercial" anywhere? If so, the always-free list is the fix, and the edit must be announced.
- Does your employer own part of the code or forbid side income? If yes, stop until it is cleared in writing.
- The two reviewers' code in the core stays MIT. A CLA is not needed for this plan.
- Run the EU Cyber Resilience Act role test before launch. Charging for software can make you a manufacturer with reporting duties. The skill points to `oss-security-disclosure`, which I did not run.
- Continuity clause for buyers: deployed versions keep working, with source access or escrow if you stop.

## Announcement
Ship it the same day Pro is available. Add-ons need no notice period.

1. Always-free list in the README, with the "what changes, what never changes" post.
2. Say plainly: MIT stays, existing releases are untouched, free security fixes continue, no banner or phone-home.
3. FAQ: fewer free features? (No.) Keep using the current version forever? (Yes.) Can anyone fork it? (Yes.) Does Pro collect data? (No.) Does Pro check a key? (Yes, offline.) What if you stop? (The continuity clause.) How do I buy with a PO?
4. Templates are in `references/launch-kit.md`.

## Hours and obligations
- Standing load is my estimate (6 to 10 h/week), against your budget, which is unknown.
- Paying customers' support outranks the free queue. Write response terms for them and keep the free queue's terms unchanged.
- Cap the support contracts at 2 or 3 customers.
- If the budget is already spent on the free project, take this to `oss-maintainer-sustainability`.

## Signals
- **Leading indicator:** companies asking to pay (quotes, invoices, security reviews) per month, before and after launch.
- **Goal threshold:** orgs needed = monthly net target ÷ (monthly price per org × (1 − fee)).
  - Illustration only, with an assumed $5k/month net target, $6k/yr average contract and an assumed 3% fee: 5,000 ÷ (500 × 0.97) ≈ **11 orgs**.
  - Replace the target and fee with your real ones.
- **Demand test:** 10 paying organizations within two quarters of GA. Below that, revisit the boundary before adding features. No free-to-paid conversion rate has been published for a library, so do not plan on one.
- **Trust signals:** outside PRs per month, and activity on any fork.
- **Kill or pivot:** fewer than 3 paying orgs after two quarters means rework the boundary with the 8 companies before any new feature.

## What I need from you
1. Monthly net target, date, and hours per week (on top of a job?).
2. Does the free server already ship percentage rollouts and any rate limiting? Is there a CLA or a trademark? Any "free forever" wording anywhere?

Reply with answer 1 and I will turn the DRAFT sections into final ones.