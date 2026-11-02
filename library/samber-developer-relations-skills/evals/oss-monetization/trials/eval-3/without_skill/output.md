**Next action (10 min): reply to Oakhaven today. Ask what they want to pay for, and offer a monthly support subscription. Do not form an LLC yet.**

## Verdict

- **Do not build the hosted SaaS now.** Your three inbound leads are not SaaS buyers, and the SaaS cannot reach $2,500/month by December.
- **Sell a support subscription plus one paid feature.** Oakhaven, the fintech, and the dry-run company each already ask for one of these.
- **Skip the LLC for now. Check your employment contract first.**

## Why not the SaaS

1. **Time.** You have about 100 hours before Dec 31 (10 h × 10 weeks). My estimate for a multi-tenant runner, dashboard, auth, secrets handling, billing and on-call is 300–600 hours. That is 7–15 months at your pace.
2. **Customers.** At a guessed $99–199/month, $2,500 needs 13–25 paying customers. You have zero SaaS leads.
3. **Trust.** A hosted runner holds credentials to customers' production ClickHouse. The fintech sent a security questionnaire. It will not hand a solo maintainer those credentials.
4. **The free alternative.** Your Apache-2.0 CLI in a CI job costs almost nothing. A hosted runner must beat that on features, not convenience.
5. **Signals.** All three inbound requests are customer-side: invoice, assurance, feature. Nobody asked for hosting.

## The plan

| Lead | What they asked | Offer | My starting price (unvalidated) |
|---|---|---|---|
| Oakhaven Analytics | Pay for something | Supported subscription | $750/month |
| Fintech | Security questionnaire | Supported tier plus security documentation | $1,500/month |
| Dry-run company | Dry-run mode | Fixed-price feature, 50% upfront | $4,500 one-off |

**Supported subscription contents:**
- Email answers within 2 business days, best effort.
- Priority triage of their issues.
- Security questionnaire answers once per year.
- A written vulnerability-handling policy.
- Input on the roadmap.

**What the numbers do:**
- Two subscriptions give $2,250/month recurring.
- The dry-run fee adds about $4,500 in cash across Nov–Dec.
- You reach roughly $2,500/month in average cash by December even if one subscription slips.

**Where the prices come from:**
- They are my judgment, not sourced benchmarks.
- $2,500 ÷ about 43 hours a month is roughly $58/hour gross.
- The dry-run fee assumes about 35–40 hours at a contractor-like rate.
- Quote them, then adjust to the reaction.

**Dry-run terms:**
- The feature merges into the Apache-2.0 main branch, so it cannot be exclusive.
- Their payment buys priority and a delivery date.
- Write acceptance criteria and the supported ClickHouse versions into the quote.

**Hour budget (100 h):**
- 40 h dry-run.
- 20 h support and admin.
- 20 h security documentation.
- 20 h buffer.
- If subscriptions eat the buffer, stop selling.

**Do not do:**
- Fill the questionnaire for free. It is part of the paid tier.
- Relicense or split the code into an open core. Published Apache-2.0 releases stay Apache-2.0, and a relicensing move would cost you trust.
- Promise an SLA with penalties. Keep it best-effort.

## Timeline

1. **By Oct 30:** reply to all three leads and ask discovery questions. For example, what exactly will they pay for, who signs, and by when?
2. **By Nov 6:** send one-page quotes.
3. **By Nov 20:** at least two signed. If not, reprice or reconsider.
4. **Dec 1:** first invoices go out.
5. **Dec:** deliver dry-run. Collect testimonials with permission.

## LLC question

1. **Entity.** No LLC first. The first invoice is the bottleneck, not the entity. Form one after a signed quote exists.
2. **Where you live.** My notes say you live in France. A US LLC does not change French tax residency.
   - The fast French route is likely micro-entrepreneur registration, which is online and cheap.
   - Check the current revenue ceiling and VAT rules with an accountant. One hour is enough.
   - If you are US-based, an LLC is days of work and a modest fee. Do it after the first signed deal.
3. **Employment contract.** Check this before you invoice anyone.
   - Look for exclusivity, moonlighting, and IP clauses.
   - Check whether your employer could claim Marrowline, since it relates to your job.
   - Notify or get written consent if needed. This is the real blocker, more than the entity.
4. **Contract.** Use a one-page agreement with a liability cap and no warranty. The fintech will expect one. Have a lawyer review the template once.

I am not a lawyer.

## SaaS pricing, parked

Revisit only after 2+ customers have paid and ask for a dashboard. If you ever build it:
- **Architecture.** Customer-run agent, with the SaaS holding only metadata. Fintechs will not share credentials otherwise.
- **Metric.** Per connected cluster per month. Seats fail because CI does the work.
- **Paid boundary.** Org-only features: approvals, audit log, drift detection, RBAC. Never paywall the runner itself or security fixes.
- **Placeholder price.** About $99–199/month for a team. This is an untested hypothesis. Test it on a landing page plus 10 customer calls first.
- **Cap.** Bound by the free CLI in CI, which costs nearly nothing.

## Risks and signals

- **Leads go cold.** Signal: no reply in 7 days.
- **The fintech wants a SOC 2 report.** Signal: the questionnaire asks for certifications. Then drop that offer.
- **Support eats the hours.** Signal: more than 4 h/week on tickets.
- **Employer objection.** Signal: contract clause found.

**Reopen the SaaS decision if:**
- Two customers ask for hosting unprompted.
- Recurring revenue passes $2,500/month.
- Your time budget grows past 10 h/week.

## Next step

Tell me where you are tax resident and whether your contract has a side-work clause. I will then draft the three reply emails and the one-page quote.