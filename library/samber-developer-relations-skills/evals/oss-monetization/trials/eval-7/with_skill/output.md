**No, this isn't the right sequence.** Two of your moves are on the skill's "Never" list, and the sequence skips the cheapest first sale. Below is the order I'd use, then the draft plan.

## What's wrong with the sequence

1. **Cutting free support to current-major-only is the one thing the skill says never to do.** It says never "shorten that window to sell extended support". Both insurers are on 4.x, so the cut would be aimed at two named customers. That's the surprise switch, and the evidence file shows how it goes. FluentAssertions made a sudden, badly timed change and got the strongest fork of its wave. MassTransit pre-announced and got a muted reaction.
2. **Paywalling the 4.x→5.x guide and the performance docs is also on the "Never" list.** The list includes "documentation needed to use the core". It also makes the free-versus-paid gap look like withholding rather than a service. Both moves together read as coercion of your two warmest buyers.
3. **ESS has nothing to sell yet for 4.x.** While 4.x is inside the free window, there are no backports past the window to charge for. You'd be pricing the same patches you give away today.
4. **The sequence skips the first sale.** The skill's rule for a company that already asked to pay is: sell a capped support contract now. It bills in weeks, and the conversation tells you what an add-on should contain.
5. **"Free forever, no enterprise edition" needs a visible edit.** You can keep the offer, since ESS is a service and touches no promised code. But the line must become a published always-free list, and the edit must be announced, never made silently.

## Better sequence (about 8 h/week)

1. **Weeks 1-2 (about 16 h): rights and promise.**
   - Check which contributors' code is present. Apache-2.0 inbound is permissive, so no consent blocker.
   - Run a trademark search on "Hollowmere" and register the name before selling.
   - Confirm your employer doesn't own or restrict any of this.
   - Draft the always-free list and the README rewrite.
2. **Weeks 2-3 (about 16 h): publish the support policy with dates.**
   - Keep "last two majors" exactly as it is, and write it down.
   - Announce it together with the README edit.
   - Say what stays free: all current code, security fixes inside the window, all docs including the upgrade and tuning guides, and data export.
3. **Weeks 3-6 (about 32 h): sell to the two insurers.** Offer one capped support contract each:
   - a written response window, an invoice and purchase-order path, a security-questionnaire answer pack, and paid migration help for 4.x→5.x;
   - an ESS option that starts automatically the day 4.x leaves the free window, which is when 6.0 ships;
   - a continuity clause for "what if the solo maintainer stops": deployed versions keep working, plus source access or escrow;
   - a cap of three customers in total.

   Have counsel review the contract. Take price levels to `devtools-pricing-strategy`.
4. **Weeks 6-12: ESS for anything already out of the window.** If any company runs 3.x or older, sell ESS to them now. Otherwise ESS waits for 6.0.
5. **Month 3 onward: draw the add-on boundary from what the insurers ask for.** Validate each feature with named buyers before writing code. Build only after at least one contract has paid for the hours.
6. **Performance tuning becomes a new paid product, not a paywall.** Keep the existing docs free. Sell a workshop or a "Hollowmere in production" workbook if you want to teach. This depends on the audience gate, which I couldn't check.
7. **When 6.0 is planned:** announce 3-6 months ahead that 4.x moves to ESS-only on that date. That's the legitimate version of your idea.

## Draft monetization plan: Hollowmere, 2026-10-23

*Draft: I couldn't ask the interview questions, so inputs marked "needed" are open.*

**Goal**
- Income target, net per month, and date: **needed**.
- Purpose of the money: **needed** (salary, side income or co-maintainer).
- Hours: 8 per week. Whether that's on top of a job: **needed**.
- Your appetite for quoting and selling versus writing: **needed**.
- If the real goal is fewer hours, stop and route to `oss-maintainer-sustainability`. Monetization adds load.

**Gates**

| Gate | Result | Evidence |
|---|---|---|
| Buyer | Pass | Two insurers asked for paid support; a dozen production users |
| Audience | Unknown | Needed only for paid content |
| Ownership | Pass | Apache-2.0 inbound, and ESS ships no new terms. Verify contributors and CLA. |
| Shape | Pass for support and ESS; hosting fails | An embedded ORM has nothing to host |
| Capacity | Pass on my estimate | Two contracts at about 4 h/month each is about 2 h/week. The skill publishes no benchmark, so this is my number. |

The add-on is deferred on capacity. Weeks of code at 8 h/week is a quarter or more.

**Chosen offer**
- Primary: capped support contracts for the insurers, sold now.
- Secondary: ESS for 4.x, starting when 4.x leaves the free window.
- Next: a paid add-on, boundary drawn from buyer requests.
- Rejected: shortening the free window, paywalling docs, relicensing, hosting.

**Paid boundary**
- Always free: all current code, security fixes inside the published window, all docs, data export, community contributions.
- Paid: response terms, backports past the window, security answers, invoice path, migration help.
- Contribution rule: decide before the first PR arrives. Decline paid-feature PRs with a written reason, or move the feature to free if everyone needs it.

**Price shape**
- Unit: per organization, annual.
- Tiers: a custom tier with purchase order and invoice.
- Who invoices: needed. Ask your country; a merchant-of-record is an option.
- Levels go to `devtools-pricing-strategy`.

**Rights**
- Inbound Apache-2.0, no license move planned.
- Trademark registration before launch.
- CLA and employer check pending.

**Announcement**
- What changes: paid support and ESS exist, and the README promise becomes the always-free list.
- What never changes: the code stays Apache-2.0, free support covers the last two majors, and docs stay free.
- Date: before the first contract is signed.
- Use the launch-kit template.

**Hours and obligations**
- Standing load is about 2 h/week for two contracts.
- Paid customers' queue outranks community issues. Keep the free queue's terms unchanged.
- Charging for support may make you a manufacturer under the EU Cyber Resilience Act. Run the role test in `oss-security-disclosure`. I couldn't confirm that skill is installed.

**Signals**
- Leading indicator: payment requests per month.
- Demand test: ten paying organizations within two quarters. This is a self-set baseline.
- Goal threshold: paying organizations = monthly net target ÷ (monthly price × (1 − payment fee rate)). It needs your target and price, so I haven't computed it.
- Trust signals: outside PRs per month and fork activity.
- Review at month 6. Pivot if no contract is signed in the first quarter.
- Compare revenue per hour with an employment baseline. A job at an insurer that depends on Hollowmere may beat this plan's first-year revenue.
- Expect years, not months. Sidekiq took five.

## Questions I need answered

1. What's the net monthly target, and by when?
2. Is the 8 hours on top of a job?
3. Is the current "last two majors" policy written down anywhere with dates, and is anyone on 3.x or older?
4. Do you hold the trademark, domain and registry account, and does any employer own or restrict the code?
5. Do you prefer talking to companies, or writing and teaching?