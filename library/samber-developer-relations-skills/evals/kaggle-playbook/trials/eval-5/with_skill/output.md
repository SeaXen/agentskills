# Kaggle plan for Gatekeep: don't run one this quarter

**Verdict: Skip.** Don't build a Kaggle notebook or hackathon program. Spend the 4 hours a week on channels where people who own CI/CD pipelines already are.

I applied the kaggle-playbook and its references (`limits.md`, `templates.md`). I didn't check any Kaggle page live, so figures below that come from the playbook are unconfirmed.

## Why

- **The test fails.** The playbook asks whether a stranger can fork a notebook and run your product in it with internet off. Gatekeep scans GitHub Actions and GitLab pipelines, and no data or ML workflow touches the product. The playbook names CI as a Skip case.
- **The 20M+ figure is the wrong number.** It's a count of Kaggle accounts, which are mostly students and data scientists. It says nothing about platform engineers, DevSecOps staff or the security buyers of a pipeline scanner. I haven't confirmed the figure either.
- **A hackathon is the weakest option.** A Community Hackathon runs about a $10k prize pool, needs a judging panel (reportedly 3+), and has you paying and handling tax on prizes yourself. Its competition-style rules also expect free, equally accessible tools. You would pay real money and 4 hours a week to reach the wrong people.
- **Kaggle punishes the usual vendor behavior.** Linking your own work outside the Accomplishments forum is treated as spam. Vote requests and colleague forks (which count as votes) can get content removed or accounts banned. A security vendor with a ban on record carries a trust cost.

## What would change the verdict

Tell me which of these are true, and I'll re-rank:

1. **Does any part of Gatekeep run inside a Python notebook?** For example a local scanner library, or scanning of ML or model-training pipelines. If it installs and runs offline, Kaggle becomes "notebooks and datasets only."
2. **Do you own data worth publishing?** An example is a dataset of public, anonymized workflow misconfigurations that researchers could model. Even then it supports a research reputation and doesn't drive signups. It's a side experiment, not the strategy.
3. **Is the CMO's real goal reaching ML or data-science buyers?** If so, the target is an ML-supply-chain pitch, which is a different product decision.

If all three are no, the verdict stands.

## What to tell the CMO

Three sentences you can paste:

- "Kaggle's 20M is total accounts, mostly data scientists, and Gatekeep's buyers are platform and security engineers."
- "Our product can't run in a Kaggle notebook, which is the thing that makes Kaggle work as a channel."
- "I'll spend the same hours on channels where pipeline owners already are, and report numbers at week 6."

## Replacement plan: 4 hours a week, 12 weeks

The channels below are my judgment, not playbook facts. I haven't validated them for Gatekeep. Week 1 picks the two best.

**Week 1 (4h): pick two channels.**
- Ask 5 existing customers or trial users where they learned about pipeline security.
- Check where Gatekeep signups come from now.
- Choose two channels from this shortlist: GitHub (Actions Marketplace listing, advisories), GitLab CI/CD Catalog, Hacker News, Reddit r/devops and r/netsec, conferences such as DevOpsDays and BSides, OWASP CI/CD security material.

**Weeks 2-4 (4h/wk): one research-style asset.**
- Publish a data-backed post, for example "what we found scanning N public workflows".
- Use only public repos, anonymized, with no customer data.
- Run it past security and legal first.

**Weeks 5-8 (4h/wk): distribute and answer.**
- Post it in your two chosen channels.
- Spend about 1.5 hours a week answering questions in full, without leading with links.
- Submit one conference talk (CFP) that fits the research.

**Weeks 9-12 (4h/wk): double down or drop.**
- Keep whichever channel produced tagged signups or replies from real pipeline owners.
- Drop the other.

If you later want to sponsor events, the `developer-event-sponsorship` and `hackathon-sponsorship` skills cover it. A security-focused hackathon on GitHub or GitLab would fit your audience far better than Kaggle, but it's a budget decision, not a 4-hour-a-week one.

## Metrics

Targets are self-set, since no vendor benchmark exists.

- Tagged-link signups per channel.
- Replies or DMs from people who own a pipeline.
- Qualified conversations started per month.
- Stars, followers and impressions only as secondary signals.
- Zero removed posts or moderator warnings.

## If you still want a Kaggle experiment

Only do this if the CMO insists and the three questions above come back yes. Cap it at 1 hour a week, with no hackathon.

1. Put 2-3 named staff on Kaggle, with no shared company account.
2. Get each to Contributor level in week 1: complete profile, verified phone, one notebook run, one comment, one vote.
3. Have them answer 2-3 forum questions a week in full, with no links.
4. In week 3, publish one standalone notebook on a public dataset. A colleague forks it once and runs all cells with internet off. Pin package versions.
5. After the notebook is live, request an organization profile.
6. Never ask anyone for votes, in any channel.

The question I'd answer first is the first one above: does any part of Gatekeep run in a notebook?