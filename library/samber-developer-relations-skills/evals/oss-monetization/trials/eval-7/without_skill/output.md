**No. Three of the four pieces are in the wrong order or work against you.** ESS is a good idea. Your own scope is the problem.

**Next action (under 30 min):** email both insurers. Ask what they need from a support line. Details are in step 1.

## Verdict per piece

1. **ESS itself: keep.** The insurers already asked, so demand exists. This fits a support-and-LTS model, and your Apache code stays free.
2. **Cut support to the current major only: don't do it now.**
   - It makes the free tier worse so that paid looks better. Users read that as coercion, and they punish it publicly.
   - You don't need it. Both insurers are asking to pay today, with no pressure.
   - Change the window later, with a dated notice, once ESS exists and has customers.
3. **Paywall the 4.x→5.x guide and the performance docs: don't.**
   - Hidden upgrade docs keep people stuck on 4.x. More stuck users means more backport work for you alone.
   - Docs are your adoption funnel. Gating them costs stars and installs, and an insurer's engineers will share them anyway.
   - Sell people instead of pages. Examples: upgrade assistance, a performance review, office hours.
4. **README "free forever, no enterprise edition": fix first.** This is the real first step.
   - ESS is a service, not an edition. You can keep both promises if you reword honestly.
   - Silent drift is the trust risk. A public, dated rewrite is not.

## What the free/paid gap should be made of

Make the paid side things only a company needs and a solo developer does not:

- Security and bug backports on 4.x after community EOL, with a written response time.
- Early private security advisories.
- A named contact, plus a contract and invoicing.
- Vendor-risk paperwork: questionnaires, SBOM, signed artifacts.
- Upgrade help and performance review, billed as services.

Never put these on the paid side:

- Security patches for the supported free versions.
- Docs.
- Anything contributors built.

Contributors' code can be backported privately under Apache-2.0. Expect leakage. You sell response time and accountability, not secret code.

## Sequence (about 8 h/week)

1. **Week 1 (~8h): talk to the two insurers.** Ask what they need: response time, CVE handling, indemnity, vendor questionnaires, budget, 4.x lifespan. Ask 3 of your other ~10 production users too. Output: a one-page scope.
2. **Week 2 (~6h): fix the README and publish a short post.** Say Hollowmere stays Apache-2.0 and every feature stays free. Say optional paid support will cover versions past community support. Admit the 2019 line was written in anger.
3. **Weeks 2-3 (~8h): publish the support policy.** Keep two majors for now. Set a dated 4.x community EOL with at least 12 months' notice. ESS starts when that date passes.
4. **Weeks 3-6 (~24h): set up the business basics.**
   - Entity, support contract template, liability cap, invoicing.
   - A private security-report channel.
   - Backport process and an hours estimate per month.
   - A continuity answer. The insurers will ask what happens if you are sick. Candidates: a second maintainer or a paid backup.
5. **Weeks 6-12: sign paid pilots.** Offer 3-month ESS on 4.x with a defined scope. Success: 2 signed by the end of week 12. Price from their value and your measured backport hours, not from a copied number.
6. **Only after pilots:** reconsider shrinking the free window, and add services such as upgrade help.

## Risks, with the signal for each

- **Solo capacity.** Signal: backport hours above ~3 h/week. At that point, cap the number of customers or raise the price.
- **Key-person risk.** Signal: insurers ask about continuity and you have no answer.
- **Community backlash.** Signal: issue threads or forks around the README change. Pre-empt it by announcing before selling.
- **Insurers leave 4.x themselves.** Signal: they start 5.x migration. That is fine. Sell migration help instead.

## Revisit this plan if

- Fewer than 2 pilots are signed by week 12 (failure condition).
- A fork or vendor offers 4.x patches.
- Support hours cross your 8 h/week ceiling.

## Assumptions

I didn't ask these, so check them. You own the copyright or hold the contributors' agreement (needed only if you ever relicense, which this plan doesn't). 4.x is still receiving fixes today. You can invoice as a legal entity. If any of these is wrong, step 4 grows.

**Next:** send the two insurers a 5-line email asking for their support requirements and budget.