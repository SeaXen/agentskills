**Pick none of the three this month. Cut your hours first, and check whether any company would pay.**

Charging does not fix what you described. Your goal is closest to "fewer hours, not more money" (the skill's goal (e)), and the skill says to stop there. Monetization adds standing work: invoices, renewals, and a paid-customer queue that outranks your free queue. Rude users stay rude. Porzio's line fits: "The work is what justifies the money". It does not work the other way around.

## Why each option fails now

- **Pro tier (paid add-on).**
  - It ranks highest long-term. The one solo case I have evidence for is Sidekiq, which launched in 2012 and reported about $80k a month in 2017.
  - It needs weeks of new code, plus selling and support. That comes on top of your 20 hours a week and your job.
  - Nothing shows that anyone would buy it. 12k stars are not buyers.
- **Support contract.**
  - It is the fastest to revenue and the cheapest to try. It also costs hours per customer every month.
  - It only makes sense for a company that has already asked to pay you.
- **Dual license.**
  - Apache-2.0 inbound code passes the ownership gate. Counsel should still review it.
  - It ranks near last. A Kotlin HTTP client mostly runs inside apps and servers, so GPL creates no pressure on anyone. Only AGPL does, and AGPL is on many corporate ban lists.
  - Revenue is unproven. The FluentAssertions relicensing produced a strong fork, so it risks the trust that makes up your 12k stars.

## This month (about 3 to 4 hours a week, 2026-10-23 to 2026-11-23)

1. **Today, 10 minutes:** turn off GitHub notification email and push. Check issues twice a week at fixed times.
2. **Week 1, about 2 hours:**
   - Add issue and PR templates.
   - Add a `CODE_OF_CONDUCT.md` and a short `SUPPORT.md` saying that questions go to Discussions.
   - Add a stale-issue bot.
   - Write one canned reply for rude or duplicate issues. Lock or close on the first rudeness.
3. **Week 2, about 1 hour:** set a hard cap of 8 hours a week for the project, and post a short README or Discussions note with your response expectations. Say that responses are best-effort and not tied to a deadline.
4. **Weeks 2 to 3, about 3 hours:** ask your three or four most active contributors if one wants triage rights or co-maintainership. The skills `oss-issue-triage` and `oss-governance` cover this.
5. **Week 3, about 1 hour:** list every company that appears in your issues asking for support, features, invoices or security answers. This is the only buyer evidence that counts.
6. **Week 4:** re-check your weekly hours and how you feel about the notifications. Then decide on money.

## What to do about money after that

- **Companies on your list and your hours at or below 8 a week:**
  - Offer one or two capped support contracts to the companies that asked.
  - Sell them first, and use those conversations to find out which Pro features anyone would pay for.
  - Build nothing before a company names a feature and a price.
- **No companies on the list:**
  - Do not monetize. Companies do not pay when nobody has asked them to.
  - Keep the hours cap and the co-maintainer search going.
- **Still resentful at 8 hours a week:** that points to handing the project over, not to charging. Releasing it to co-maintainers is a valid ending.

## Before you sell anything

- **Employer:** your day job may own your code or forbid side income. Get written clearance first.
- **Trademark:** register the name `Sablecastle` before any sale. Counsel picks the jurisdictions.
- **Promises:** if the README says "free forever", turn that into a published always-free list. Announce any paid tier. Never add it silently.
- **EU law:** charging can make you a manufacturer under the EU Cyber Resilience Act, with vulnerability-reporting duties. I have not checked whether that applies to you.

Everything above rests on what you told me. I have not looked at the repo: contributors, CLA, FUNDING files and dependents are unchecked.

**Next, under 2 minutes:** turn off GitHub notification email and push now, then answer this: does your employer allow side income, and has any company ever asked you to pay?