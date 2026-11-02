Next action: publish a 5-question survey to your newsletter and YouTube community tab today. Don't build SSO or the admin panel yet. You have no evidence that companies want this.

## Diagnosis

- **Math.** $5k net needs about $6k MRR gross, minus the $180 from sponsors, so about $5.8k from Pro. At $12/seat that is about 480 seats, or about 32 teams of 15. The tax rate on your net is a guess I can't pin down, so this may need adjusting.
- **Demand risk.** In three years, 300k installs have produced zero company contact. That means either companies don't use Tidewrack, or they use it and never needed to talk to you. You can't tell which from where you stand, and the whole plan depends on the answer.
- **Stargazer emails are weak.** Stars come from individuals, not companies. Cold emails to EMs found that way carry no signal that the company has any use for the tool. Keep it as a small side channel, not the main one.
- **Free alternative.** Teams already share config by committing a file to a git repo. That is your price ceiling. "Shared config" alone won't sell. Governance will: enforced policy, audit, SSO. That is also what has a long sales cycle.
- **Runway.** 8 months ends about June 23, 2027. A first paid launch in February leaves about 4 months of revenue ramp. The base case probably misses $5k MRR by June, so plan a bridge now.

## Model

- **Model:** open core. MIT stays MIT. Never move an existing free feature behind the paywall. Publish a short "always free" list.
- **Paid boundary:** features only an organization needs, with a trigger you can see (a second user, a policy file, an audit request).
- **Metric:** per seat, $12/month. Cost to serve is near zero if you avoid a hosted backend. Annual billing at 10 months for 12. Treat $12 as an experiment, not a fact.
- **Deployment:** v1 has no hosted service. Use a license key and a policy file synced from the customer's own git repo. A hosted backend means on-call duty, which a solo founder can't carry.
- **Team rung, v1:** signed shared config and policy, license key, seat billing through a merchant of record (handles VAT), email support.
- **Enterprise rung, later:** SSO, SCIM, audit log, admin panel. Build only when at least two paying or signed teams say its absence blocks purchase.
- **Don't price SSO as a luxury.** Basic SSO at the team rung. Only custom IdP, SCIM and audit go at the top.

## Plan

1. **Oct 26 – Nov 6: demand test.**
   - Ask five questions: do you use it at work, employer size, does your team share a setup, would you pay for X, can you intro your manager.
   - Add a one-time, opt-in first-run prompt in the CLI asking for a work email. Opt-in keeps you clean on GDPR.
   - Put a waitlist page on the site.
2. **Nov 9 – Dec 4: sell before building.**
   - Hold 15–20 calls with people who use it at work.
   - Offer 3–5 founding design partners a prepaid discount on the first year.
   - **Gate 1 (Dec 4):** go only if you get at least 3 prepaid teams and at least 200 work-domain signups. These thresholds are my baselines, not industry benchmarks.
   - **If the gate fails:** don't build team features. Run the individual-Pro fallback below.
3. **Dec 7 – Feb 12: build v1** with the design partners. Ship small, weekly, and film it as devlogs. Skip the admin panel and SSO.
4. **Mid-Feb: public launch.**
   - A pricing page with real numbers.
   - A devlog video.
   - A newsletter issue.
   - A Show HN.
   - Self-serve checkout with no sales call.
   - Founding customers get a public thank-you.
5. **Mar 31, Gate 2:** if MRR is under about $1.5k and you have fewer than 10 paying teams, switch to bridge mode. Take contract work at about 15 hours a week and keep Pro running on the rest. Set this threshold yourself; it is a trigger, not a forecast.
6. **Apr–Jun:** build enterprise features only against signed demand. Review again on May 15, with 6 weeks of runway left to decide.

## Hours (45/week)

- 40% customer conversations and selling.
- 40% build.
- 20% content: devlog, newsletter, docs.

During the demand test, flip it to 70% conversations.

## Bridge income, start now

- Sell newsletter sponsor slots. Price them from your own open rate.
- Sell YouTube sponsor slots.
- Keep GitHub Sponsors running, and add a "used at work" tier.

None of these is a business model on its own. They buy months.

## Fallback if companies don't show up

Sell Pro to individuals as a convenience upgrade (themes, sync, advanced UI). Expect small amounts and fast churn, so treat it as a runway extender, not the $5k plan. Then reconsider the whole bet at Gate 1 instead of in June.

## Risks and signals

- **Few companies use it.** Signal: under 100 work-domain signups at Gate 1.
- **Shared config is too easy to DIY.** Signal: calls say "we'd just use a git repo."
- **Community backlash.** Signal: forks or "rug pull" threads. Pre-empt it with the always-free list.
- **Long enterprise cycles.** Signal: deals stall at security review. Stay self-serve until revenue per account justifies sales effort.
- **Cold-email compliance.** If you email people scraped from GitHub, check GDPR and ePrivacy rules first. I haven't researched them for your case.

## Questions that would sharpen this

- What do installs look like by OS and channel? Linux and Homebrew-on-Mac skew toward company laptops.
- Do you have any telemetry or a download-by-domain signal at all?
- Which team feature do you think sells, and why?