**Sound right? No, two parts are wrong.**

1. AGPL will probably not stop the reseller.
2. "License now, revenue later" runs backwards. The license change is the most trust-costly option, and you don't need it to sell hosting.

**Do this week, in order:**

1. Do not relicense yet.
2. Ask a trademark lawyer about registering "Lanternbrook" and sending the reseller a written notice about the logo and name.
3. Write down the names of the 6 or 7 companies that asked about hosting.

I had no repo access, so everything below rests on your message. Sections marked *draft* wait on the open inputs at the end.

---

# Monetization plan - Lanternbrook - 2026-10-23

## Goal (draft)

- **Money pays for:** two modest salaries, Dario and you.
- **Target:** 9,000 EUR/month combined, within 18 months, so by about April 2028.
- **Hours:** two people full time, about 80 hours a week, until the grant ends in March 2027.
- **Unclear:** whether 9,000 is take-home, pre-tax, or company revenue. Social charges, taxes and hosting costs sit between revenue and take-home, so the revenue needed could be 1.3 to 1.6 times higher. Confirm this first.

## Gates

| Gate | Result | Evidence |
|---|---|---|
| Buyer | **Pass, thin** | 6–7 companies asked to pay for hosting this year, and the reseller has paying customers. Both are real signals, but the companies are unnamed. The 40 Docker pulls an hour are not buyer evidence. They include CI and auto-updates. |
| Audience | **Not tested** | No newsletter, courses or talks mentioned. Paid content and sponsorware stay off the list. |
| Ownership | **Pass for AGPL, with conditions** | Assuming outside contributions arrived under MIT: MIT lets you ship the code inside a work under other terms, with notices kept. Counsel should confirm. If any contributor code arrived under GPL or AGPL, this gate fails. After the switch, new contributions arrive under AGPL. You then need a CLA first, or you can never sell a commercial license. |
| Shape | **Hosting passes** | Self-hosted server with Postgres, migrations every release and a worker fleet. That is real operational pain. The "Managed" Docker-and-Postgres story is what a buyer would pay to skip. |
| Capacity | **Pass if tenants stay under about 20 and provisioning is scripted** | These are my estimates, not a benchmark. Fixed upkeep is about 10–15 h/week: billing, backups, upgrade runbook, a monitor of the monitor. Each customer takes about 2–4 h/month. The hard limit is 24/7 on-call for two people running an uptime monitor. If the monitor is down, customers feel it immediately. |

**Drop for now:**

- Commercial license on a next major, because it needs months and has no buyers yet.
- Relicensing the current version, which ranks last.
- Donations as a salary. Plausible's self-hosters gave about $300 a month in total while subscribers paid the team.

## Chosen offer

**Primary: a hosted offering, opened by 2–3 capped pilot contracts.**

- **Why hosted ranks first.** The skill ranks it near last by default, but moves it up when two or more people work on the project, one of them wants to run production, and the server is hard to self-host. That is your situation. Dario runs it and you write code.
- **Why open with pilots.** A company already asked to pay, so a capped contract is the first sale. Sell it to those companies now. It brings revenue in weeks and shows which paid features they want.
- **Pilot shape.** Offer a managed single-tenant instance per customer, flat monthly price, 6-month term, capped at 3 customers. Use it to validate before building multi-tenant billing.

**Secondary (Q2 2027 and later): a closed paid add-on.**

- Candidates: SSO, audit log, RBAC, compliance and SLA reports.
- Validate each candidate with the pilot companies before writing code.
- The add-on works for self-hosters and for your hosted tier. It also gives you something to code, which suits your preference.

**Rejected, in plain terms:**

- **Relicense to AGPL next week.** It fails the announcement rules in step 4. It does not fix the reseller (see Rights). It could also hurt the 6–7 inbound companies, since many corporate policies ban AGPL.
- **Paid content, sponsorware, donations.** No audience evidence, and donations rarely reach a salary.
- **Marketplace listings.** No indie project has shown material revenue from them.

## Paid boundary (draft)

**Always free, published before the paid tier ships:**

- Everything in Lanternbrook today, including migrations and the worker fleet. Nothing leaves the core to make hosting look better.
- Security fixes for the free edition for the current major and a stated window after the next.
- Documentation, and data export in a documented format.
- Community-contributed code.

**Paid, a hosted service, not withheld features:**

- Running it for the customer: upgrades, backups, scaling, on-call, SLA.

**Paid add-on candidates, none confirmed:**

- SSO/SAML, audit trail, RBAC, compliance reports, priority support.
- Perham's rule: if everyone needs it, it belongs in the free core.
- A feature stays a candidate until a named company says it would pay, and at what unit.

**Contribution rule, decide before the first pull request:** outside pull requests that add a paid feature to the free core are declined with a written reason, or the feature moves to free if everyone needs it.

**Never:** telemetry, phone-home or license checks in the free code. Moq lost a day of trust over one.

## Price shape (draft)

- **Unit:** per organization for hosted. Band it by monitor count or probe frequency as the usage proxy. Do not price per developer.
- **Tiers:** a card-paid self-serve tier and a custom tier with quote, purchase order and invoice. Bill the custom tier annually.
- **Invoicing:** a registered business of your own, or a merchant-of-record service that handles sales tax. Which one depends on your country, and an accountant decides.
- **Price levels:** go to `devtools-pricing-strategy`. The prices below only show the arithmetic.

**Paying organizations needed** = 9,000 / (monthly price × (1 − fee)). I assumed a 3% fee, before sales tax, and **before hosting costs and taxes**:

| Illustrative price | Orgs for 9,000 EUR |
|---|---|
| 300 EUR/mo | 31 |
| 600 EUR/mo | 16 |
| 1,000 EUR/mo | 10 |

**Pace.** Say you launch publicly in March 2027. Reaching 16 orgs by April 2028 means about 1.1 net new orgs a month. Your current inbound is about 0.5 asks a month, with unknown conversion. No free-to-paid rate has been published for any library, so I will not plan on one. You need a "Managed" button in the docs, README and install page, because that is where self-host pain shows up.

**Honest verdict on 9,000 within 18 months.** It is possible, but only at a price of 600 EUR/mo or more with a working funnel. Salary-level cases took years: Sidekiq launched in 2012 and reported about $80,000 a month in 2017. The current evidence supports a few pilots by March, not 9,000.

**Bridge to March and after.** Revenue by March of roughly 1,000–1,500 EUR/month is a realistic guess, not a forecast. It does not replace two salaries. Plan a bridge now:

- Another grant or fellowship (hand to `oss-sponsors-fundraising`).
- Contract work for a company that depends on Lanternbrook.
- A part-time job for one of you.

Compare revenue per maintainer hour against the baseline each quarter. If a job at a company that depends on Lanternbrook pays better per hour, say so.

## Rights

| Item | Position |
|---|---|
| Inbound license | MIT assumed. Confirm with a contributor list. |
| CLA/DCO | Unknown. Decide before any license change. A DCO alone does not give relicensing rights. |
| Trademark | **Biggest lever against the reseller.** Register the name before selling anything. Registration protects against resellers in most countries, and first use alone rarely does outside the US and UK. |
| Logo | Check whether the logo file sits in the repo under MIT. If it does, the reseller may have a license to use it. Counsel decides. |
| Reseller and AGPL | AGPL's network clause targets modified versions offered as a service. An unmodified resale may have nothing to release. They can also keep running the last MIT release forever, or fork it. Plausible moved MIT to AGPL in 2020 to stop resale, and resellers still used its name and logo until it renamed its self-hosted edition in 2024. Trademark mattered as much as the license. |

**If you still want AGPL after the offer is running**, the earliest sound path is:

1. Collect a CLA from active contributors.
2. Announce 3–6 months ahead, so late 2026 for a release in 2027.
3. Apply it to a new major only. Keep MIT on the old major with a stated security window.
4. Never switch inside the final pull request of an open-source release.

AGPL could then support a commercial exception for hosting competitors who modify the code. That needs the CLA.

Not legal advice. License wording, contracts and tax go to professionals.

## Announcement (draft)

- **Changes:** from <date>, an official managed Lanternbrook is available for organizations that don't want to run Postgres, migrations and workers.
- **Does not change:** the license, the existing releases, the always-free list, and the free support window. Publish the always-free list with the announcement. No "protect the community" wording.
- **Who pays:** organizations buying hosting or the add-on. Self-hosters pay nothing.
- **Timeline:** pilots now, public launch around March 2027. No license change in this announcement.
- A new add-on can ship the same day as its announcement. A license change cannot.

## Hours and obligations

| Option | Standing load (my estimate) |
|---|---|
| Hosted, up to ~20 tenants | 10–15 h/week fixed, plus 2–4 h/month per tenant, plus 24/7 on-call |
| Pilot support, 3 customers | 6–12 h/month |
| Add-on, once built | 3–5 h/week and two codebases |

- Paid customers' queue outranks the community queue. State their response terms, and keep the free queue's terms unchanged.
- **EU Cyber Resilience Act:** charging for software or support can make you a manufacturer with vulnerability-reporting duties. Run the role test in `oss-security-disclosure` before launch. I did not read that skill.
- **Continuity:** buyers will ask what happens if one of you stops. Answer in the contract: deployed versions keep working, with source access or escrow on exit.
- **Data:** customer probes may reach private endpoints and credentials. Expect refusals in regulated sectors, and get a data-processing agreement ready.

## Signals

All of these are self-set baselines.

- **Leading indicator:** companies asking to pay per month. Today it is about 0.5. Log each ask with its date.
- **Demand test:** 10 paying organizations within two quarters of public launch. That proves demand, not the 9,000 goal. Below it, revisit the boundary before adding features.
- **Goal threshold:** from the table above, with the date it implies at the current net new customers per month.
- **Review date:** 2027-02-28, before the grant ends.
- **Kill or pivot:** fewer than 3 paying orgs by 2027-03-31 means no hosted launch. Switch to support contracts and an add-on, and take the bridge job or grant seriously.
- **Trust signals:** outside pull requests per month, and any fork activity.

---

## Open inputs

Reply to any of these. Answer the first one if you answer only one.

1. **Names and exact asks of the 6–7 companies.** Did they offer a price? Is it hosting only, or also support?
2. **What does 9,000 mean?** Take-home, pre-tax, or company revenue? In which country?
3. **Contributors.** How many outside contributors are still in the code, and under which license? Is there a CLA or DCO?
4. **Promises.** Have you written "free forever", "always open source" or "never commercial" anywhere?
5. **Selling appetite.** Who sends quotes and takes calls? Dario runs infrastructure and you write code, but nobody has said they want to sell. A "no" here removes custom quotes, so the plan would be card-only and self-serve.

**Next step, under 2 minutes:** paste the company names from Discord into one line each, with the date they asked.