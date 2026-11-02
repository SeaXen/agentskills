Next: email the three companies that asked about support or an invoice, this week (about 1 hour). Offer a capped support contract. Ask each one what they want from "a license". The plan below explains why.

I read the `oss-monetization` skill and both references. I did not run the live interview, so unknown inputs are labeled and listed at the end. Not legal or tax advice. Counsel must review the license, contract and CRA points.

# Monetization plan: Quillfeed, 2026-10-23 (draft)

## Verdict on dual licensing

Dual licensing fails two gates. Drop it for now.

1. **Ownership gate fails.** Strong-copyleft code (GPL-3.0) from about 14 contributors arrived under DCO only. DCO grants no right to relicense. Selling the whole library under commercial terms needs one of three things:
   - every remaining contributor's consent;
   - a CLA from each of them;
   - a rewrite of their code.
   Two of them wrote the compression layer and the Kafka sink.
2. **Shape gate fails.** Quillfeed runs inside backend services. Running GPL code on your own servers is not distribution, so GPL imposes nothing on those companies. They have no reason to buy an exemption. Copyleft pressure exists only for software shipped inside distributed products. Only AGPL pressures server use, and it also needs the same consent.
3. **What the three companies asked for is not a GPL exemption.** Support contract and invoice are procurement needs. Sell those. Never sell "a license" to the GPL code. You do not hold all the copyrights, and the invoice request is a paper-trail need, not a copyleft fear.

## Goal

- Purpose: replace a salary, so about 4,000 EUR net per month. The skill's own cases took years: Sidekiq launched in 2012 and reported about $80k a month in 2017.
- Date asked: within 12 months (2027-10).
- Hours: 12 per week, about 52 per month. This count includes selling, invoicing and support, with no job alongside.
- ⚠️ My expectation, labeled as my judgment because no published benchmark exists: 1,000 to 2,500 EUR per month at month 12. 4,000 EUR is more likely year 2 or later.
- Baseline check: 4,000 EUR over 52 hours is about 77 EUR per hour net. A contract or part-time job at a company that depends on Quillfeed may beat the plan's first-year revenue per hour. Keep that option open as a bridge.

## Gates

| Gate | Result | Evidence |
|---|---|---|
| Buyer | ✅ pass | About 12 production companies known from issues. 3 asked to pay (2 for support, 1 for an invoice). |
| Audience | ❓ not assessed | Unknown whether you have a following. This only matters for paid content or sponsorware, so it blocks nothing. |
| Ownership | ❌ for relicensing, ✅ for new add-on code | Strong copyleft inbound, no CLA. Code you write alone is yours to sell. |
| Shape | ❌ for dual license, ✅ for support and add-on | Embedded Go library on servers. Hosting has nothing to host. |
| Capacity | ✅ for support and add-on, ❌ for license change | License change takes months plus counsel. Support takes days. Add-on takes weeks of code. |

## Chosen offer

**Primary: the capped support contract.** It is the first sale to the companies that already asked. It brings revenue in weeks and shows which add-on features they would pay for.

**Secondary: a paid add-on.** This is a closed module behind a clean seam, wrapping the free GPL core and delivered privately. The skill puts it first in efficiency, and it needs no license change.

**Later, only if you have old majors:** extended security support, meaning paid backports past the free window.

**Rejected:**
- Dual license or relicensing: ownership and shape gates. Relicensing also risks a fork of the last free version.
- Hosting: nothing to host.
- Paid content or sponsorware: audience gate unverified. Revisit if you have a following.

⚠️ **Open risk, not covered by the skill: a closed add-on that wraps a GPL core.**
- You hold copyright in your own add-on. You ship only your add-on, and customers combine it with the core privately. That is likely defensible.
- The FSF treats a program linked to a GPL library as one combined work. Counsel must confirm the add-on's shape before you build. Ask about a process or plugin boundary versus a Go import.
- Optional track that removes the risk and also reopens relicensing: ask all 14 contributors for relicensing consent, starting with the two big authors. It costs a few emails. If any refuse, nothing changes. Do not make the plan depend on it.

## Paid boundary

**Always-free list (draft, publish before launch):**
- Everything in Quillfeed today, including the compression layer and the Kafka sink.
- Security fixes for the free edition for the current major, plus a stated window after any new major.
- The documentation needed to use the free edition.
- Your data, and the ability to export it.
- Community contributions, which ship in the free edition.

**Candidate paid features.** These are guesses, since I do not know the codebase. Validate each with the three companies before coding:
- fleet-wide coordination or backpressure across nodes;
- audit trail and compliance evidence;
- encrypted at-rest buffering;
- PII redaction;
- SSO or access control for any admin surface.

**Rules:**
1. Never paywall the compression layer, the Kafka sink or any other community-contributed code. Other people wrote it under GPL.
2. A feature nobody names stays a candidate and is not built.
3. Perham's rule: if everyone needs it, it belongs in the free core.
4. Outside PRs that add a paid-tier feature: decline with a written reason, or move the feature to free if everyone needs it. Decide this before the first one arrives.
5. No telemetry, phone-home or license check in the free library. Enforce the paid package through the contract and private delivery only.

## Price shape

I do not know your country. Prices below are my labeled scenario, not benchmarks. Hand final numbers to `devtools-pricing-strategy`.

- **Support contract.** Cap at 3 or 4 customers. Cap hours per customer, for example 4 hours per month. Set a written response window and scope. Price flat per organization per month, billed annually or quarterly, with an invoice and purchase-order path.
- **Add-on.** Price per organization, banded by developer count. Offer a card-paid tier and a custom tier with invoice and security answers. Avoid pure per-developer pricing.
- **Invoicing.** Your own registered business, or a merchant of record that handles sales tax. An accountant decides; tell me your country.

**Goal threshold.** Paying organizations needed = 4,000 / (monthly price × (1 − fee rate)). Assumed fee 5%, to be replaced with your actual rate:

| Price per org per month | Orgs needed |
|---|---|
| 125 EUR | 34 |
| 300 EUR | 15 |
| 600 EUR | 8 |
| 1,000 EUR | 5 |

Example mix (a scenario, not a forecast): 4 support contracts at 600 EUR plus 8 add-on orgs at 300 EUR gives about 4,560 EUR net. That is 12 paying organizations, which is every company you know about. So the known list is too small for the target. Growth must come from unseen users and referrals, and the add-on has to reach them.

## Rights

- **Inbound license:** GPL-3.0, DCO only, no CLA. Check whether files say "GPL-3.0-only" or "or later". That matters for counsel.
- **Contributors:** list all 14 and what each still has in the code. The compression and Kafka authors are the two that matter.
- **Trademark:** search and register "Quillfeed" before selling. Counsel picks jurisdictions.
- **Project assets:** confirm you hold the domain and registry accounts.
- **Prior employer:** you have no job now. Confirm no past employer claims any of the code.
- **Promises:** confirm you never wrote "free forever" or "never commercial". A "free forever" line stays valid for the add-on, but it must become the always-free list above.
- **License moves:** none. This is an optional consent drive, as above.

## Announcement (draft)

An add-on can ship the same day as its announcement, so no three-month notice is needed. There is no license change to announce.

> **Quillfeed Pro and support contracts: what changes and what does not**
>
> **What changes:** from [launch date], organizations that need [validated paid features] can buy a separate Pro add-on and a capped support contract.
> **What does not change:** Quillfeed stays GPL-3.0. Every current release and feature stays free. See the always-free list.
> **Who pays:** organizations running Quillfeed in production that want support or the add-on. Individuals and open-source projects use the free edition.
> **Price and timeline:** [from the pricing step].

Fill the bracketed items once the buyer calls and pricing are done. Answer the launch-kit FAQ before launch, especially these: can I keep using the current version, can someone fork the free edition, does the paid package collect any data, and what happens if you stop maintaining it.

## Hours and obligations

Standing load, estimated by me:
- **Support:** 4 customers at 4 hours per month is about 16 hours per month.
- **Add-on upkeep, billing and sales:** about 15 hours per month once live.
- **Left for building:** about 20 hours per month, around 5 per week.

⚠️ This is tight. Paying customers outrank the free issue queue, so state response terms in the contract and leave the free queue's terms unchanged. Do not take a fifth customer before the add-on exists.

**Obligations:**
- **EU Cyber Resilience Act:** charging for software or support can make you a manufacturer with vulnerability-reporting duties. Run the role test in `oss-security-disclosure` before launch. I did not run it.
- **Contract:** a lawyer drafts the support terms and the add-on end-user license. Include a perpetual right to keep running deployed versions, plus source access or escrow if you stop maintaining it.
- **Delivery:** private delivery of the add-on through a per-customer credential on a private Go module proxy or private repository, with rotation on cancellation.

## Signals

- **Leading indicator:** invoice, quote and security-review requests per month, now versus after launch.
- **Demand test:** the skill's default is 10 paying organizations within two quarters. That is nearly your whole known list, so use 3 paying organizations by 2027-04-23 (month 6). This number is mine. At 3, continue. Below it, revisit the paid boundary before adding features.
- **Goal review:** 2027-10-23. Check revenue against the threshold table, and compare revenue per hour with the employment baseline.
- **Kill or pivot condition:** under 3 paying organizations at month 6. Then take the contract or part-time baseline and keep the free project running.
- **Trust signals:** outside PRs per month, and any fork activity.

## Timeline

1. **Week of 2026-10-26 (about 8 hours):**
   - Email the three companies. Ask what they would pay for, and what they mean by "a license".
   - Check the GPL-3.0 "only" or "or later" wording.
   - Run the trademark search.
2. **Weeks 2 to 4 (about 10 hours per week):**
   - Counsel reviews the support terms, the add-on boundary and the CRA test.
   - Sign the first one or two capped support contracts.
3. **Weeks 5 to 12:** build the first add-on feature that the companies named. Optionally send the consent emails to the 14 contributors.
4. **Around 2027-01-22 (month 3):** publish the always-free list, the announcement and the pricing page, and ship the add-on.
5. **2027-04-23 and 2027-10-23:** run the demand test and the goal review.

## Open inputs, answer in this order

1. Why do the three companies want a paid relationship? Their answers decide the first offer.
2. What country and business entity do you have?
3. Do you have an audience, such as a newsletter, talks or followers? That would open paid content.
4. Has Quillfeed shipped old majors that companies are stuck on?
5. Is the code "GPL-3.0-only" or "or later"? Did you ever write "free forever"?

Not on this list but still needed:
- your payment-fee rate;
- whether you want to talk to companies every week;
- whether you will run production infrastructure (assumed no).

Once I have answers 1 and 2, I will fill the price and announcement sections.