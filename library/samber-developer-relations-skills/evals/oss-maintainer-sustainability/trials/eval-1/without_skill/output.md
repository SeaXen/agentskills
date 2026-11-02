**Do not add the 48-hour badge.** At 3 hours a week you can't keep that promise, and a broken promise draws more complaints than silence does.

- Your inflow is about 45 issues a month plus 8 or more PRs.
- 3 hours a week is about 12 hours a month. Even 15 minutes per item uses all of it.
- The projects with that badge have paid staff or several maintainers.
- A badge that goes stale in week two reads as a lie. Visible silence at least doesn't claim anything.

The README section below states what you can deliver instead. It is a *schedule*, not a latency promise.

**Sponsor expectations.** Don't expect to replace the lost hours. Individual sponsorship for a library like this typically yields under $1,000 a month. Company tiers are where real money comes from, so the copy below targets companies first.

---

## 1. README section

```markdown
## Support and maintenance

Tessellate is maintained by one person, in about 3 hours a week.
That is the real capacity, so here is what to expect.

| What | What to expect |
|---|---|
| Security reports | Acknowledged within 7 days. Report privately via [SECURITY.md](SECURITY.md), never in a public issue. |
| Bug reports with a minimal reproduction and a sample file | Triaged in a weekly batch. Fixes ship as time allows. |
| Bug reports without a reproduction | Likely to get a single request for one, then close after 30 days. |
| Feature requests | Read, but rarely built by me. A PR is the fastest path. |
| Pull requests | Reviewed in the weekly batch. Small, tested PRs that follow [CONTRIBUTING.md](CONTRIBUTING.md) move fastest. |

Silence does not mean "no". It usually means the queue is longer than my week.

### How to get a faster answer

- Attach the smallest tile file that reproduces the problem, plus the Tessellate and Python versions.
- Search open issues first. About 410 are open and many are duplicates.
- Send a PR. I can merge a tested fix much faster than I can write one.
- Help triage. If you can reproduce or close stale issues, open an issue titled "triage help" and I'll add you.

### Funding changes this

Tessellate has about 1.1M downloads a month, and the maintenance behind it is unpaid.
Sponsor funding is what converts "3 hours a week" into more. See
[Sponsors](#sponsors) below.

## Sponsors

If your company builds on Tessellate, please consider sponsoring it.
It is the cheapest way to keep a dependency you rely on alive.

[**Sponsor on GitHub**](https://github.com/sponsors/<your-handle>) · [**Sponsor on Open Collective**](https://opencollective.com/<your-collective>)

<!-- sponsors:start -->
<!-- Logos go here. Generated from the sponsors list; do not edit by hand. -->
<!-- sponsors:end -->
```

Update the "weekly batch" row only after you've run two or three real batches. Never write a number you haven't yet met.

---

## 2. GitHub Sponsors page copy

**Headline:** Keep the tile-format parser your pipeline depends on maintained.

**Short bio (≤ 200 chars):**
Maintainer of Tessellate, the Python library that parses GIS tile formats. 1.1M monthly downloads, one maintainer, five years.

**About / long description:**

> Tessellate parses GIS tile formats for Python. It is installed about 1.1 million times a month, and for five years I've maintained it alone, on top of a full-time job.
>
> Each month about 45 new issues and several PRs arrive. I can give the project roughly 3 hours a week. Right now that covers security fixes and the most critical bugs. The backlog (410 open issues) keeps growing, and response times are slow. I don't think that's good enough for a library people build products on.
>
> **What your sponsorship does:** it pays for maintainer time. My target is to raise Tessellate from 3 hours a week to **[X] hours a week**, which would fund:
>
> - a regular triage pass, and a one-time cleanup of the 410-issue backlog
> - faster PR review
> - format-spec updates and new Python version support, shipped before they become your problem
> - security patches and release hygiene
>
> **What it does not buy:** roadmap control, guaranteed merges, or special treatment in the review queue. Sponsors can get faster *triage* (see tiers). Outcomes are decided on technical merit.
>
> If your company ships a product that depends on Tessellate, a sponsorship is a small insurance policy for your supply chain. If you're an individual, thank you. It makes a real difference to the hours I can give.

**Funding goal** (use a sponsor-count goal if you want to keep income private):
"First goal: $[X]/month, which buys [Y] extra hours a week. When it's reached, I will post a public update on what changed."

Set the first goal low enough to close this quarter.

**Tiers.** GitHub does not let you edit a published tier's price, so choose carefully before publishing.

| Tier | Price | What the sponsor gets |
|---|---|---|
| Thank you | $5/mo | Name in `SPONSORS.md`, my gratitude |
| Supporter | $15/mo | The above, plus a sponsor badge on your GitHub profile |
| **Team** | **$250/mo** | Logo and link in the README, plus your issues get **triaged in the weekly batch** (a label and a reply, not a fix) |
| **Company** | **$1,000/mo** | The above, plus logo on the docs homepage, a quarterly 30-minute office hour, and a heads-up before breaking changes |

Notes on this table:

- The two company tiers are placeholders. Price them against the real README and docs views you can measure. Check your PyPI stats and docs analytics before publishing.
- The Team tier carries the program. "Triaged" promises a reply, not a fix.
- Don't add a sub-$15 perk tier just under Team. People pick the cheaper one.
- Cap what each reward costs you. Monthly calls, priority support and bespoke work become a second job, so don't put them on the ladder.

**Boundaries to publish alongside the tiers:**

> - Sponsorship buys visibility and triage, not roadmap control or merged PRs.
> - Security fixes, the core library and the documentation stay free for everyone.
> - I may decline sponsors whose products conflict with the project's neutrality.

---

## 3. Open Collective page copy

**Tagline:** Fund the maintenance of Tessellate, the Python GIS tile-format parser.

**Description:**

> Tessellate parses GIS tile formats for Python, with about 1.1M downloads a month. It is maintained by one person, in about 3 hours a week.
>
> This collective exists so companies and individuals can pay for maintainer time **by invoice**. Funds go to:
>
> 1. Maintainer time (triage, review, releases): [X]% of income
> 2. Infrastructure and CI: [Y]%
> 3. Fiscal host fee: [Z]%
>
> Expenses are public on this page. Sponsors who need an invoice for procurement can pay here. Sponsors who prefer GitHub can use [GitHub Sponsors](https://github.com/sponsors/<your-handle>).

**Tiers:** mirror the GitHub company tiers: Team ($250/mo) and Company ($1,000/mo), plus a one-time "Invoice" option.

**Check before opening it:**

- Open Collective needs a **fiscal host** (a legal entity that holds the money). Pick one and read its current fee and wind-down terms first. The Open Collective Foundation dissolved in 2024 and gave its 600+ collectives seven months to move their funds.
- The public ledger shows what you pay yourself. Decide that you're fine with that.
- GitHub invoicing starts at $5,000 per invoice. Smaller company payments need Open Collective, which is why you want both.

---

## 4. `.github/FUNDING.yml`

```yaml
github: [<your-handle>]
open_collective: <your-collective>
```

Also add a `[project.urls] Funding = "..."` entry in `pyproject.toml`, so dependency-scanning funders find you.

---

## 5. Two things that will actually lower the complaint volume

Sponsor money arrives slowly, so these help sooner:

1. **A one-time backlog cleanup.** 410 open issues is the real source of the silence complaints. Ask for a stale-issue bot with a 60 to 90 day window and a reproduction-needed label, or close the oldest duplicates by hand.
2. **Issue templates that require a repro file and versions.** This cuts the 45 a month to those you can actually act on.

**Next action (2 minutes):** tell me the monthly dollar target and the hours-per-week you want to reach. I'll fill the `[X]` placeholders and price the two company tiers to match.