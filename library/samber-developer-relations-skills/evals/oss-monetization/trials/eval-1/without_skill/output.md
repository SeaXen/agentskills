**Next action (20 min):** in the Quillfeed repo, run `git ls-files | xargs -n1 git blame --line-porcelain | sed -n 's/^author-mail //p' | sort | uniq -c | sort -rn`. It counts surviving lines per author, and everything below depends on that list.

This is not legal advice. Steps 2, 3 and 6 need a lawyer who knows open-source licensing. Prices and revenue targets below are my working assumptions, not market benchmarks. Check them against your own customer calls.

## Three facts that change the plan

1. **DCO does not give you relicensing rights.** DCO sign-off certifies that a contributor may submit under GPL-3.0. It does not let you sell their code under other terms. About 14 people hold copyright in their lines, and two of them wrote the compression layer and the Kafka sink. You cannot sell a commercial license to the whole codebase without their consent.
2. **Most of your users probably have no GPL problem.** Copyleft triggers on distribution. A company running Quillfeed inside its own backend services usually distributes nothing. They have little reason to buy a license. The invoice request for "a license" is a signal that someone wants to pay. It does not show they need dual licensing.
3. **What you can sell today needs no license change.** Support, SLA, security-patch backports and priority fixes need nobody's consent. Two of your dozen known users already asked for this.

## Recommended model

- **Primary: support and LTS subscription, starting now.** It needs no contributor consent. It is the model the evidence shows buyers asking for.
- **Secondary: commercial license, only after the consent campaign succeeds.** Sell it to the few companies that do distribute Quillfeed (embedded in a product, appliance or on-prem agent) or whose legal team bans GPL. Don't plan revenue around it until step 3 passes.
- **Rejected:**
  - Relicensing to source-available. It is irreversible, forks historically follow, and you have no hyperscaler threat to justify it.
  - AGPL. Some enterprises ban it outright, and it adds nothing for your revenue.
  - Open core with a closed module. You'd have to carve out the contributor-written parts first.
  - Sponsorship as the main income. It won't reach 4,000 EUR a month.

## The math

- 4,000 EUR a month is 48,000 EUR a year.
- At 8,000 EUR a year per customer, that's 6 customers.
- At 12,000 EUR a year per customer, that's 4 customers.
- You know about 12 companies. Landing 4 to 6 means converting a third to a half of them. That's ambitious, so expect to need adjacent leads from the repo and from conference talks.
- 12 hours a week is about 600 hours a year. If each customer takes 2 to 3 hours a week of support and fixes, 6 customers would take all your time. Write a support hours cap into every contract.

## The plan

**Phase 0 — Week 1 (about 6 hours)**
1. Run the blame count above and save the output. List every author with surviving lines.
2. Mark the authors who matter: the two substantial ones, plus anyone above roughly 2% of lines.
3. Check each author's contribution date and employer. Employer-owned code needs the employer's sign-off too, so flag any contributor who worked on it during a job.
4. Email the 3 inbound leads (the two support requests and the invoice request). Ask 5 questions each: what they run it for, what they'd pay for, who signs, what budget, and what deadline. Ten minutes each is enough.

**Phase 1 — Weeks 2–6 (about 10 hours a week): start revenue before the license question is solved**
1. Write a one-page support offer with two tiers:
   - **Standard:** email support, 2-business-day response, security-fix notification, 4-hour monthly cap.
   - **Priority:** 1-business-day response, a backported fix for your last two minor versions, a quarterly call.
2. Pilot price: pick one number per tier from the three calls, not from a benchmark. Offer the first 3 customers a discounted annual rate in exchange for a named reference or testimonial.
3. Set up the business side: a legal entity or freelance status, an accountant, an invoice template, and VAT handling. Ask your accountant first, because the right status for EU invoicing depends on your country.
4. Success check at week 6: at least 1 signed support contract, or a written reason from each lead why not.

**Phase 2 — Weeks 4–12 (parallel, about 3 hours a week): contributor consent campaign**
1. Hire a lawyer for a fixed-fee job. They draft two documents:
   - A short relicensing grant for past contributions. It lets you distribute their existing code under GPL-3.0 and a commercial license.
   - A CLA for future contributions.
2. Contact the two substantial authors first, personally and before anyone else. Explain the plan openly:
   - Say what you'll sell and what stays GPL.
   - Offer a credit, and consider offering them a share. Ask your lawyer how to structure a share.
   - Treat this as a negotiation. They can say no.
3. Then email the rest by value (most surviving lines first). Allow 3 reminders over 4 weeks.
4. **Go/no-go at week 12:** you need grants covering roughly 95% or more of surviving lines. This number is my threshold, not a legal one, so ask your lawyer where the line is.

**If the go/no-go fails (an author refuses or can't be reached):**
- Rewrite their files, clean-room, in someone else's hands. Estimate the hours before you commit. A rewrite of the compression layer or Kafka sink could cost weeks.
- Or exclude those modules from the commercial offer.
- Or stay on support only. That still reaches the revenue target if you land 4 to 6 customers.

**Phase 3 — Months 4–6: commercial license, if the go/no-go passed**
1. Publish a `COMMERCIAL-LICENSE.md` and a pricing page. Say plainly: the code stays GPL-3.0, and the commercial license is for companies that can't or won't accept copyleft.
2. Keep the commercial license text lawyer-drafted. Don't write it yourself.
3. Price it per company per year, not per seat, and let the lawyer tie it to distribution rights (embedding, shipping to customers).
4. Switch new contributions to a CLA. Keep the DCO check too. It costs you some drive-by contributors, but you need the rights going forward. Say so in the contributing guide.
5. Register the Quillfeed name and logo as a trademark, or at least publish a trademark policy. The license covers code, not the name.

**Phase 4 — Months 6–12: reach 4,000 EUR a month**
1. Convert the leads you know, then widen. Search GitHub issues and dependents for companies you haven't contacted.
2. Add a "Used in production? Support options" link to the README, the docs and issue templates. Doing this once costs little and captures the next asker.
3. Track one leading indicator monthly: qualified conversations held. Revenue lags by one to three months.
4. Revisit at month 6 and month 12 (below).

## Rough targets (my assumptions)

| By | Milestone |
|---|---|
| Week 6 | 1 signed support contract, or written reasons for no |
| Month 3 | 2 customers, about 1,000 EUR a month |
| Month 6 | 3–4 customers and the consent decision made, about 2,000 EUR a month |
| Month 12 | 4–6 customers, about 4,000 EUR a month |

## Risks and the signal for each

1. **A key contributor refuses.** Signal: no reply after 3 reminders, or a no from either of the two substantial authors. Response: the fallback options above.
2. **Nobody pays for support.** Signal: zero contracts by week 6 and a "we're fine without" reason from every lead. Response: reconsider the model before spending on lawyers.
3. **Support eats your 12 hours.** Signal: more than 8 hours a week on support before you have 3 customers. Response: lower the cap, raise the price, or write more docs.
4. **A contributor feels exploited.** Signal: public complaints or a withdrawn PR. Response: talk first, be transparent about plans, and credit them.
5. **Cash runs out before month 12.** Signal: you can't cover living costs by month 6. Response: consider part-time contracting or a funded fallback now. A 4,000 EUR target in 12 months assumes you can live on savings until then.

## Reopen the decision if

- Week 6 passes with no signed support contract.
- Either substantial author refuses and the rewrite costs more than the revenue it unlocks.
- A hyperscaler or competitor starts reselling Quillfeed as a managed service. Only then is a license change worth the fork risk.
- Support demand exceeds your capacity and a second maintainer or a contractor becomes necessary.

## Questions I need answered

1. **Runway:** how many months can you live without income? This decides whether 12 months is feasible.
2. **Distribution:** do any of the dozen companies ship Quillfeed inside a product they sell or deploy on customer premises? Those are your commercial-license buyers.
3. **Contributors:** are you on good terms with the two substantial authors, and do you know whether they wrote the code on an employer's time?

**Next:** run the blame command from the top and paste the author list. I'll help you rank who to contact first.