**Do not build the SaaS. Do not form an LLC first.** First action, 5 minutes: email your employer to ask for written clearance for paid side work on Marrowline. Without it, every other step is unsafe.

Marrowline is a draft plan. Employer, country, promises and CLA answers are open (see "Open questions" at the end).

# Monetization plan - Marrowline - 2026-10-23

## Goal
- Pay rent: +$2,500/month net by 2026-12-31 (about 10 weeks).
- Budget: 10 h/week on top of a full-time job, about 100 h total.
- Assumption: "net" means after payment fees, before income tax.
- ⚠️ Free-project upkeep also comes out of those 100 h. I assumed about 30 h.

## Gates
- ❌ Employer: unconfirmed. Stop until written clearance exists.
- ✅ Buyer: three companies asked this month. Oakhaven wants to pay, the fintech sent a security review, and the third wants dry-run. That is real buyer evidence.
- ✅ Ownership: Apache-2.0 inbound is permissive. You wrote 95%, and new add-on code is yours alone. No license move is needed, so step 4 is skipped.
- ❌ Hosted SaaS, shape: a runner needs credentials to customers' ClickHouse. The fintech's questionnaire shows how regulated buyers react.
- ❌ Hosted SaaS, capacity: on-call plus billing plus a dashboard does not fit 10 h/week beside a job.
- ❌ Hosted SaaS, date: it needs months, and you need money inside a quarter.
- ⏳ Add-on: passes the buyer gate. It fails the quarter date: weeks of code, then slow sales.
- ❓ Audience gate (paid content, sponsorware): unknown. Not needed this quarter.

## Chosen offer
- **Primary, now:** 2-3 capped support contracts with the companies already asking. These bill within weeks and show which features they would pay for.
- **Secondary, Q1 2027:** a paid add-on on the free core, only if the contract buyers name the same feature unprompted.
- **Rejected:** hosted runner and dashboard (gates above), relicensing (fork risk, no need), donations as salary (they rarely reach one).
- **Dry-run request:** sell it as fixed-fee feature development. Dry-run is something everyone needs, so it ships in the free core under Apache-2.0. They pay for priority delivery, not exclusivity. Ask for scope first.
- Your SaaS idea survives as a self-hosted add-on that runs in the customer's CI: audit trail, approval gates, drift reports. No credentials leave their network.

## Paid boundary (draft, validate with the 3 companies before coding)
- **Always free:** everything in Marrowline today, dry-run, security fixes for the current major, docs, migration-history export, and community PRs.
- **Candidate paid features** (fintech's questionnaire hints at the first two):
  - audit trail
  - compliance evidence reports
  - multi-cluster drift detection
  - approval gates
- Rule for outside PRs that add a paid feature to the free core: decline with a written reason, or move the feature to free if everyone needs it. Decide this before the first PR arrives.
- Paid code goes in a separate private package wrapping the free one. The free library never adds license checks or telemetry.

## Price shape
Numbers below are my estimates. No benchmark is published. Hand final levels to `devtools-pricing-strategy`.
- **Support contract:** flat monthly per organization, capped at about 4 h/month, 2-business-day response, security answer pack included once.
  - Quote the fintech about $1,000/month and Oakhaven about $750/month.
  - Dry-run: a fixed fee after you scope the hours.
- **Add-on, later:** per organization, banded by developer count, billed annually. Card tier plus a custom tier with PO and invoice.
  - Sidekiq Pro is $99/month. River Pro is $125/month.
  - At $125, hitting $2,500 needs 21 organizations. No free-to-paid conversion rate exists, so the add-on cannot fill this quarter.
- Goal math for contracts: $2,500 / ($833 × 0.97) = 3.1, so you need 3 organizations at about $833/month.
- A hosted SaaS has no price today. Pricing a product with no demand evidence is guessing.

## LLC question
- Do not block the first invoice on an LLC. Formation takes days to weeks.
- Invoice Oakhaven through the simplest vehicle your country allows, after employer clearance. An accountant can confirm in about 1 hour.
- Form the LLC before the fintech signs or before the add-on. Contracts with security promises and liability terms are the reason to want one.
- Card-paid sales later can use a merchant-of-record service that handles sales tax.
- I don't know your country. Entity and tax questions go to an accountant, and this is not legal or tax advice.
- Before selling anything, secure the Marrowline name (trademark, PyPI, domain).

## Rights
- Inbound license is Apache-2.0. Check for a CLA or DCO (unknown).
- No license move planned.
- Trademark registration is pending.

## Announcement
- No license change, so no 3-month notice is needed.
- Publish the always-free list in the README before the paid offer is public.
- Announce the add-on openly when it ships, never silently.
- Contracts need no announcement now.

## Hours and obligations
Draft split of about 100 h:

| Item | Hours |
|---|---|
| Free upkeep | ~30 |
| Dry-run build | ~30 |
| Sales, invoice, questionnaire pack | ~15 |
| Support (3 × 4 h × 2 months) | ~24 |

- No add-on code this quarter.
- Paid customers' queue outranks the free queue. Keep the free queue's terms unchanged.
- Contract must state what happens if you stop: deployed versions keep working, plus source access or escrow.
- EU Cyber Resilience Act: charging may make you a manufacturer. Run the role test with counsel. The `oss-security-disclosure` skill the SKILL.md cites is not installed here.
- Baseline: a freelance data-engineering contract may pay more per hour. At steady state, 3 contracts earn about $140/h on roughly 18 h/month of paid work. That excludes free upkeep.

## Signals
- **Leading indicator:** companies asking to pay per month. Now: 3 in October.
- **Goal threshold:** 3 signed contracts, about $2,500/month run-rate.
- **Review date:** 2026-12-15.
- **Kill or pivot:** fewer than 2 signed by 2026-12-15 means no add-on code. Fall back to freelance hours.
- **Add-on go signal:** the buyers name the same paid feature unprompted. The demand test for the add-on is 10 paying organizations within 2 quarters of launch.

## Next steps (all by 2026-11-06)
1. Email your employer for written clearance (5 min).
2. Reply to Oakhaven: "Yes, I can offer a capped support contract: priority response, up to 4 h/month, invoice. Price: $X. Call this week?" (15 min)
3. Reply to the fintech: offer the same contract with a one-time security answer pack, and ask for their questionnaire.
4. Ask the third company what "dry-run" must output, then quote a fixed fee.
5. Book 1 h with an accountant for the invoice vehicle and LLC timing.

## Open questions (answer in this order)
1. Does your employer allow paid side work, and who owns code you write on your own time?
2. What country are you in?
3. Have you written "free forever" or "never commercial" anywhere?
4. Is there a CLA or DCO on file?
5. Which would you do weekly: quotes and calls, writing and teaching, or running production?