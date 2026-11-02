# Monetization plan: Tidewrack (DRAFT, 2026-10-23)

**Next action:** post one question in your newsletter this week: "Do you use Tidewrack at work? Does your team share config?" That starts the buyer evidence you lack. It costs 15 minutes.

**Verdict:** your Pro plan, as written, fails the buyer gate. Do not build SSO and an admin panel first. Lead with what your 37k-follower audience can buy, and test Pro cheaply in parallel.

I could not run the interview, so some inputs are assumed. Open questions are at the end.

## Goal
- Money replaces your salary. Target: $5k a month net, within the 8-month runway. I assume that means by ~2027-06-23.
- Hours: 45 a week, about 193 a month. $5k a month is about $26 per hour before tax. Hours cover building, selling, invoicing and support.
- Honest expectation: the cited salary-level cases took years. Sidekiq launched in 2012 and reported ~$80k a month in 2017. You earn $180 a month today. This plan may not reach $5k inside the runway. It maximizes early revenue and information, and it fixes the fallback in advance (see Signals).

## Gates
- **Buyer: FAIL on current evidence.**
  - Zero companies have contacted you in 3 years, and almost all users are individuals.
  - Stars and installs are not buyers. Only a company asking to pay counts.
  - Interview rule 4b (mostly individual developers) deletes the organization-priced options: add-on, support, extended security support, commercial license, hosting.
  - This gate can reopen if the evidence below turns up named companies.
- **Audience: PASS.** 28k YouTube subscribers and a 9k newsletter already follow the project, and your devlogs show you like to teach and ship new tools.
- **Ownership: PASS.**
  - You write the Pro code alone, so it is yours to sell.
  - Inbound MIT contributions are permissive. Unverified: check for a CLA and for any employer claim.
- **Shape: PARTIAL.**
  - Tidewrack is a CLI, so there is nothing to host.
  - SSO and an admin panel need a server that touches customer credentials. That is operations work, and regulated buyers refuse it.
  - Defer both.
- **Capacity: FAIL for SSO plus admin panel plus billing plus selling.** It likely takes months, which is my estimate. Pro is deferred until named companies pay for the hours.

## Chosen offer
Rule applied: an existing audience promotes paid content above the add-on.

1. **Primary: paid content and companion product.**
   - Build "Tidewrack Mastery": a video course on terminal git workflows (rebase, bisect, worktrees, monorepos), plus a config and theme pack.
   - Sell individual licenses and a team license for companies.
   - Sell through your owned newsletter and YouTube, not docs traffic alone. Tailwind's one-funnel, one-time-purchase revenue fell close to 80%.
   - Presell before you build: open a founders' price to the newsletter. Build only if presales prove demand.
2. **Secondary: sponsorware companion.**
   - Build a new small tool, with its building filmed as devlogs.
   - Release it to sponsors first and publish an opening threshold. Pest opened at 75 sponsors, as promised.
   - Raise your 60 sponsors with this, not a plain donation ask.
3. **Experiment, not a launch: Pro for organizations.**
   - Validate first (below). Build nothing until 3 named companies commit to pay.
4. **Rejected:**
   - Hosting and a commercial license on a next major: no buyers, and long lead times.
   - Relicensing the current version: no buyers and a likely fork.
   - Marketplaces: no indie revenue evidence.

## Paid boundary (Pro, draft)
- **Always free:**
  - Everything Tidewrack does today.
  - Shared config through plain files in a repo (everyone needs it, so Perham's rule keeps it free).
  - Security fixes, docs, and data export.
  - Community contributions.
- **Paid candidates, organization-only:**
  - Enforced policy bundles (lock settings across a team).
  - Audit-log export.
  - Signed-commit enforcement.
  - Priority response and an invoice or purchase-order path.
  - SSO and an admin panel come last, only after 10 or more paying organizations ask.
- **Delivery:** a separate closed crate that wraps the open one, served through a private registry with a per-customer credential. An offline license key is acceptable if the FAQ says so.
- **Never:** telemetry or license checks in the free client. Moq was removed in a day after backlash.
- **Contribution rule:** decide it now. Outside PRs that add a paid feature to the core are either declined with a written reason or moved to free if everyone needs the feature.
- **Validation test before any code:**
  - Count stargazers by employer. Companies with 5 or more stargazers are candidates.
  - Read issues for "at work" or "our team".
  - Run the newsletter question, and a 5-line YouTube pinned comment.
  - Hold 10 to 15 research calls, not pitches, asking how their team shares config today.
  - Offer the 3 to 5 warmest companies a paid pilot: a capped support contract, which brings first revenue and shapes the add-on.
- **Cold email:** stargazers are mostly individuals. Harvested GitHub emails raise GDPR/ePrivacy and GitHub terms issues, so ask counsel and prefer public contact channels. This is not legal advice.

## Price shape
- Your $12 per seat is per-developer pricing with no organization band. That drew the strongest fork reaction (FluentAssertions). Use organization bands billed annually, like AutoMapper's developer-count bands.
- Content: a card-paid individual license and a team license.
- Pro: a card tier plus a custom tier with purchase orders, invoices and a security answer pack.
- Exact levels go to `devtools-pricing-strategy`.
- **Who invoices:** your own registered business, or a merchant-of-record service. I need your country; tax and entity questions go to an accountant.

## Rights
- Inbound: MIT, assumed. Verify the contributor list and any CLA.
- Secure the "Tidewrack" trademark before selling. Counsel picks the jurisdictions.
- No license move is planned, so there is nothing to date.
- Employer: you quit, but confirm in writing that nothing you built belongs to your old employer.

## Announcement (draft)
- Publish the always-free list before any paid thing ships. Use the `launch-kit.md` template.
- Content ships the same day as the announcement. Pro ships with its own announcement, and any future license change needs at least 3 months' notice.
- If you ever wrote "free forever" anywhere, the promise becomes the published list. Announce the edit, never make it silently.

## Hours and obligations
Rough estimates, mine, not benchmarks:
- Weeks 1–2: validation and rights checks, about 30 hours of the 90 available.
- Weeks 3–8: course build, about 25 hours a week. Sales and audience work take about 10. The rest goes to maintaining the free project and to calls.
- Pro, if it goes ahead: 15 to 20 hours a week to build, then standing support. Paid customers' queue outranks the free one, and you keep the free queue's terms unchanged.
- Obligations:
  - The EU Cyber Resilience Act may make you a manufacturer once you charge. Run the role test in `oss-security-disclosure` before launch.
  - Continuity: buyers will ask what happens if you stop. Answer: deployed versions keep working, with source access or escrow on exit.

## Signals
Self-set baselines.
- **Leading indicator:** companies asking to pay per month. Today it is 0.
- **Goal threshold for Pro alone**, assuming $12 per seat per month and a 5% payment fee:
  - 5,000 / (12 × 0.95) ≈ 439 seats, which is about 44 organizations of 10 developers or 18 of 25.
  - The demand test of 10 paying organizations (about 100 seats) gives roughly $1,140 a month. Pro alone cannot reach $5k inside the runway.
- **Goal threshold for content**, at a $149 individual price (illustrative): 5,000 × 12 / (149 × 0.95) ≈ 424 sales a year, about 35 a month. I do not use a conversion rate, because none is published.
- **Illustrative stack (my estimate):** content $2.5k + Pro pilots and support contracts $1.5k + sponsors and sponsorware $1k.
- **Review dates and pivots:**
  - **2027-01-31:** presale result, plus named organizations willing to pay. If fewer than 3 named organizations, do not build Pro, and sell only capped support and training.
  - **2027-03-31:** if recurring revenue is under $2k a month, start a contract or job search in parallel. A company that depends on Tidewrack paying for maintenance time is the baseline.
  - **2027-05-31:** the hard stop on runway.
- **Trust signals:** outside PRs per month, and activity on any fork.
- Compare revenue per hour to the job baseline each quarter.

## Open questions (answer in any order)
1. Which country, and do you have a business entity?
2. Have you ever written "free forever" or "never commercial"?
3. Which would you do weekly: teaching and writing, talking to companies, or running servers?
4. Is the $12 per seat per month or per year?
5. Do you have a CLA, outside contributors, or a registered trademark?

**Next:** do the newsletter question first, then answer the five questions above.