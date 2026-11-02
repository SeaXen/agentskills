# Sponsorship program — mistral-gauge

Two assumptions I'm building on, correct me if wrong: "by March" means **March 2027** (~23 weeks from today), and you don't yet have a legal entity or GitHub Sponsors set up. Also confirm your country is on [GitHub Sponsors' supported list](https://github.com/sponsors) before anything below — if it isn't, swap the platform references for Open Collective and the rest of this plan still holds.

## Goal

$7,200/month, recurring, replacing your day-job income, arriving by March 2027.

That number has to come overwhelmingly from **companies**, not individual sponsors. Say why plainly: the typical income a widely-depended-on library earns through *individual* GitHub Sponsors is under $1,000/month (Filippo Valsorda's figure) — and mistral-gauge, at 190 stars and 4k downloads/month, is smaller than the libraries that figure was measured on. `ua-parser-js`, 6.5k stars, held $41.61 on Open Collective. Individual sponsors are not going to fund a salary here, and no ladder design changes that.

What can: the **~60 companies** already running mistral-gauge in production. That's your actual asset. The program below is built to extract salary-shaped money from a handful of them, with individual sponsorship as a gratitude layer underneath, not the engine.

## Instrument fit

Checked against the other four funding instruments before designing a ladder:

- **Employment** — the thing you're trying to leave. Not applicable.
- **Grants** — skipped. Grant programs fund infrastructure, security-critical, or research-adjacent projects (compilers, crypto libraries, package managers). A pressure-sensor log parser doesn't clear that bar unless it's embedded in a safety-critical pipeline somewhere — if one of your 60 companies uses it that way, that's a side bet worth ten minutes, not a load-bearing part of the March number.
- **Commercial revenue** (paid support/hosting) — this is where the retainer tier below effectively lives. I'm folding it into the corporate sponsorship lane rather than running it as a separate paid-support product, so you have one ask, one invoice trail, one thing to maintain.
- **Individual crowdfunding** — included as a base layer (see Ladder), capped low deliberately.

**Recommendation: sponsorship-as-retainer, aimed at named companies, not a bigger Patreon.** The only shape in this skill's own effort/value ranking that reaches salary-level income is the retainer — named commitments (response times, upgrade support, security triage) sold to companies who have a real budget line for "don't let our sensor-data pipeline break." That's what steps 7 (corporate lane) does the real work on. Visibility (logo placement) and gratitude (individual tiers) ride alongside it but won't carry the number alone.

**Deleted, not demoted: the access/sponsorware shape.** You're still working a day job until March. Sponsor-only content or early-access gating is a standing content-production job — it's the single most expensive shape to run, and you have no spare hours for it. Don't build it, don't promise it.

## Audience

- **Individuals**: unknown count, presumably some fraction of 190 stargazers. Treat as gratitude-tier only — a few hundred dollars a month, ceiling.
- **Companies**: ~60 estimated users. This is the number the whole plan depends on, and right now it's a guess. First real task, before pricing means anything: turn "maybe 60" into a scored list (see Corporate lane) — PyPI download telemetry won't tell you who they are, but issue trackers, PRs from company email domains, and job posts naming mistral-gauge will.
- No commercial product or employer claim on the work mentioned — nothing to route around there.

## Ladder

Five published tiers — within the 3–5 baseline, well under the platform's 10-tier ceiling. **Prices below are locked once published (GitHub Sponsors doesn't allow editing a live tier's price), so don't publish until you've sanity-checked the Business and Infrastructure numbers against your first real conversation with a company.**

| Tier | Price/month | Reward | Delivery cost at 10x sponsors |
|---|---|---|---|
| Backer | $5 | Name in `BACKERS.md` | ~0, scripted |
| Supporter | $25 | Name in `BACKERS.md` + thanks page + sponsor badge | ~0 |
| Team | $150 | Small logo in README + docs footer | ~10 min/quarter |
| Business | $750 | Larger logo in README + docs sidebar, quarterly written update on what shipped, "acknowledged within 48h" on issues you file | ~2h/quarter, capped |
| Infrastructure Partner | Custom, **minimum $2,000** | Everything in Business, plus a signed support agreement: named upgrade support when sensor-format/firmware changes break parsing, 48h security-issue acknowledgment, a direct contact channel | Bounded by the written scope, not the tier text |

Two things worth flagging on this ladder:

1. **No partial-perk trap.** Supporter ($25, individual, no logo) sits directly below Team ($150, company, logo) — different buyers, no overlap, so nobody rationally downgrades to dodge the price.
2. **Infrastructure Partner is deliberately not a fixed reward description.** Per this skill's own rule: named commitments big enough to be a real retainer shouldn't be published as tier copy — the price is locked forever once live, but the scope of "what I actually promise" needs to flex per company. Publish it as a **custom-amount tier** ("Infrastructure Partner — contact me, from $2,000/month") and negotiate the actual commitments in a one-page agreement per company (template below). The tier button is just the payment rail.

**The math that gets you to $7,200/month:** one Infrastructure Partner deal with your most dependent account at ~$3,600/month, plus five Business-tier companies at $750/month ($3,750) = **$7,350/month** from six companies — a 10% conversion rate on your 60 known users. Team, Supporter, and Backer tiers are upside buffer, not part of the plan. Six corporate deals in ~5 months, while still holding a day job, is the actual project — the tier ladder is just the pricing sheet for it.

## Platform

**GitHub Sponsors, personal account** — 0% fee (vs. up to 6% on an org account), and you have no entity yet, so this is the simplest receiving rail for Backer/Supporter/Team.

For Business and Infrastructure Partner: invoiced sponsorships have a **$5,000-per-invoice minimum**. Bill these **annually**, not monthly — $750/month becomes a $9,000 annual invoice, $2,000+/month becomes $24,000+/year, both clear the floor. Confirm with GitHub Sponsors support whether invoiced billing is available on a personal (non-org) account before you pitch anyone at that tier — this is a real unknown, not a formality, and it blocks the whole corporate lane if the answer is no. If it turns out invoicing requires an org account or a fiscal host, Open Collective is the fallback (3–10% fee, typically 10%) — don't set both up preemptively, only if the direct route fails.

`.github/FUNDING.yml` on the default branch (enable the Sponsors button in repo settings too):

```yaml
github: [your-github-username]
custom: ["https://github.com/sponsors/your-github-username"]
```

Also fill the funding URL in `pyproject.toml`'s `[project.urls]` — PyPI surfaces it, and it's one more place a company's automated dependency-funding tooling (thanks.dev-style) can find you without you pitching anyone:

```toml
[project.urls]
Funding = "https://github.com/sponsors/your-github-username"
```

## Ask

**Goal type: sponsor-count, not amount.** An amount goal publicly and permanently displays your monthly sponsorship income — while you're still employed, that's a needless disclosure with no upside. Set the public goal as something like "12 sponsoring companies and individuals" and track the real dollar number privately.

Page copy, short, your voice, not a pitch deck:

> I maintain mistral-gauge, a Python library for parsing pressure-sensor logs. About 60 companies run it in production as far as I can tell. I'm doing this on evenings and weekends right now, on top of a full-time job — sponsorship is what lets me change that. Sponsorship funds: keeping parsing correct as sensor formats change, triaging issues and security reports on a real timeline, and eventually doing this full-time. It doesn't buy roadmap control or a merged PR — see Boundaries.

Put the funding link within two clicks of everywhere a user already is: repo Sponsor button (enabled via FUNDING.yml above), README top, docs footer. A page nobody reaches converts nobody — this is often the actual reason "nobody sponsors a widely-used project," not the ladder.

## Corporate lane

This is the part that decides whether you hit $7,200. Sequence:

1. **Turn "maybe 60" into a scored list.** Pull evidence in this order of signal strength: who's filed issues/PRs from a company email domain (they already have an engineer paying attention — start here), public repos/lockfiles naming mistral-gauge, job posts mentioning it, any conference talk or blog post describing a pipeline built on it. Twenty well-qualified companies beats all sixty loosely guessed.
2. **Identify one flagship account** — whichever company looks most operationally dependent (sensor data feeding something safety- or compliance-relevant is your strongest "this breaking costs you real money" story). That's your Infrastructure Partner target; budget a week of outreach effort on that one account specifically.
3. **Address a named person with budget and exposure** — a platform lead or staff engineer, never a generic contact address.
4. **Send the ask this shape, not the "please support my work" shape:**

   > Subject: mistral-gauge maintenance — support tier for &lt;Company&gt;
   >
   > Hi &lt;Name&gt;, I maintain mistral-gauge. I can see &lt;their service/repo&gt; parses pressure-sensor logs through it, and &lt;N&gt; of your engineers have filed issues this year, so this is likely load-bearing for you.
   >
   > I currently maintain it on evenings and weekends. I'm setting up company support tiers so the teams actually running this in production get a defined level of service: security issues acknowledged within 48 hours, named support when sensor formats change, and a direct line to me instead of the public issue queue. $750/month, invoiced annually, logo in the README and docs.
   >
   > If removing maintenance risk on this dependency is worth it, I'll send a one-page summary and an invoice this week. If sponsorship isn't the right budget line, is platform engineering or supply-chain security the better door to knock on?

5. **Have the payable checklist answered *before* the first email goes out**: a way to receive money (personal GitHub Sponsors account is enough to start), a tax form ready for your country, the ability to send a numbered invoice, bank details beyond a card-donation link. Companies pay whoever their finance department can process without an exception — not whoever's most deserving.
6. **Plan the renewal before the first invoice.** Corporate budgets are annual; a short quarterly note on what shipped and what was triaged is what gets you renewed, not remembered fondly.

## Boundaries

Publish this alongside the tiers, before the first sponsor lands:

- Sponsorship buys visibility, gratitude, and named service commitments — never roadmap control or a merged PR. Contributions are judged on merit regardless of who pays.
- "Acknowledged within 48 hours" (a triage promise) is sellable. "Your issue gets fixed first" (an outcome promise) is not — don't sell it, even informally, to your biggest account.
- If a conflict of interest ever comes up (a sponsor's competitor also wants in, a sponsor pressuring a technical decision), you decide, and you say so publicly now rather than improvising later.

## Measurement

Check at 90 days (~2026-12-22) and again at the March 2027 deadline:

| Question | Metric | Ignore |
|---|---|---|
| Growing? | Recurring monthly total, trend | Cumulative lifetime total |
| Who's paying? | Sponsor count, individual vs. company split | Stars, downloads |
| Durable? | Churn, whether one sponsor is >50% of income | One-time spikes |
| Ask working? | Conversion per surface (README vs. docs vs. direct outreach) | Page views alone |
| Promise kept? | Every published/agreed commitment actually delivered on time | Thank-you replies |

Pass bar at 90 days: at least one Business-tier or Infrastructure Partner deal signed. If zero corporate deals have closed by then with real outreach behind it, the ladder isn't the problem — the corporate lane never actually opened, and $7,200/month by March is off the table; that's the moment to renegotiate the date, not the pricing.

## Before you publish — four things to confirm first

1. Is your country on GitHub Sponsors' supported list? Blocks everything else if not.
2. Can a personal (non-org) GitHub Sponsors account take invoiced billing? Ask GitHub Sponsors support directly — determines whether Business/Infrastructure tiers need a fiscal host instead.
3. Pull your real docs/README traffic numbers (Google Analytics, or whatever you have) — the Team/Business logo prices above are placeholders sized off your download count, not measured placement traffic.
4. Pick the flagship account for the Infrastructure Partner pitch and send that one email first — it's the highest-value, highest-uncertainty part of the whole plan, so it shouldn't wait behind the other five.