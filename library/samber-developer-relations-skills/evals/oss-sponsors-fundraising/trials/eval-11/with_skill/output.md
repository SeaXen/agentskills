# Sponsorship program — quillstream

## Goal

**First target: 25 total sponsors within this quarter — a sponsor-*count* goal, not an amount goal.**

GitHub Sponsors only lets you run one goal, and it has two shapes: a count (private income) or an amount (permanently public income, since it can't be un-published). Personal-account income with no entity behind it means an amount goal exposes your personal earnings forever with no corporate buffer in front of it. Default to the count goal unless you already run a build-in-public practice that makes that disclosure a feature, not a leak. **Confirm this — I don't know if you do.**

Frame the goal in a unit a reader recognizes, not "support my work": *"quillstream's CI minutes, docs hosting and a code-signing cert run about $X/month — 25 sponsors covers it."* Plug in your real number; I don't have it. An unreachable first goal reads as "nobody supports this" — a goal that closes this quarter beats an ambitious one stuck at 4% for a year.

## Instrument fit

You didn't give me a monthly dollar target or say this should replace a salary — you gave me a durability goal ("still paying me in two years"). That's a different instrument question than "how much," and it's the one this skill answers well.

- **Sponsorship fits.** No stated income floor, real measurable audience (docs, README, newsletter), goal is durability not speed.
- **Employment, commercial revenue** — out of scope here (`oss-sponsors-brand-strategy` is the other side of the table; `devtools-business-model` covers whether a paid Pro/commercial build could substitute for or sit alongside sponsorship — audio DSP libraries commonly dual-track this, worth a look separately, not now).
- **Grants — deferred, not built.** NLnet's Open Internet Stack funds pay individuals directly, no entity, €5k–€50k first grant — genuinely fits your "no entity" constraint better than sponsorship does. But every grant carries a reporting duty tied to a fixed schedule, and your bad-month ceiling is two hours for anything sponsor-facing. Don't add a milestone-and-report obligation on top of that ceiling until the sponsorship program is running on autopilot. Revisit in six months if the ceiling loosens.

## Audience

You didn't name who uses quillstream — individual devs, companies shipping it in products, or both — or name three dependent companies. I'm assuming both, since an audio DSP library's realistic buyer mix is indie/hobbyist developers (gratitude tier) plus companies shipping audio product on top of it — game studios, plugin vendors, audio-software companies (visibility tier). **Confirm this, and name the companies if you can — it changes nothing about the ladder below but it changes whether Step 7's outreach has a target list on day one or needs a research pass first.**

Surfaces, with the numbers that price the ladder:

| Surface | Reach |
|---|---|
| Docs site | 41,000 views/month |
| README | 12,000 views/month |
| Newsletter | 9,200 subscribers |

That's real, countable placement traffic — enough to price a company tier honestly, not enough (and not the right shape anyway) to run an access/content program.

## Shape decision

Two of the four shapes are deleted outright, by your own constraints, not by preference:

- **Retainer — deleted.** "No entity and no willingness to use a fiscal host deletes the retainer" is the rule as written. Retainer money requires invoicing, tax handling, and a written commitment expensive to break — none of which survives "money hits my personal bank account, I won't incorporate."
- **Access — deleted.** Sponsor-only content, early access, sponsorware — all standing jobs. Two hours in a bad month can't sustain a program that ships whether or not anyone asked.

What's left is **gratitude + visibility**, which is also the documented default combination ("most working programs are a gratitude base plus one of the other shapes"). Visibility is the right second shape specifically because your goal is durability: a published logo placement keeps paying without new work every renewal, which is exactly what a content/access program can't do. Your traffic (41k + 12k, well into "tens of thousands") is also the stated threshold where visibility's value overtakes access's — you're not settling for the cheaper option, you're in the range where it's the *better* one.

## Ladder

Two buyers, two price bands, split near the $100/month baseline:

| Tier | Price/mo | Reward | Delivery cost at 10× sponsors |
|---|---|---|---|
| **Backer** | $5 | Name in `BACKERS.md`, GitHub sponsor badge | Near-zero — script appends from the Sponsors API |
| **Supporter** | $25 | Name in `BACKERS.md` "Top Supporters" + listed on a `/sponsors` page | Near-zero |
| **Team** | $100 | Small logo on README (12,000 views/mo) | ~10 min, one-time commit |
| **Studio** | $400 | Logo on README + docs site footer (53,000 combined views/mo) | Same commit, templated docs include |
| **Partner** | $900 | Logo on README + docs + credit line in every newsletter issue (9,200 subscribers) | One template edit; auto-repeats every send |

- **Expected converting tier: Studio.** Priced under most companies' no-PO card limit, clearest ROI (a logo on the actual product's docs, not a generic "gold" badge), no invoicing needed.
- **No partial-perk tier sits below a converting tier.** Team and Studio aren't a cheap/expensive version of the same reward — Team is README-only, Studio adds docs — so nobody is offered a discount route to the same perk.
- **Everything on this ladder is in the "near-zero, safe" reward bucket on purpose** — logo commits and templated credit lines, nothing bounded (office hours, private repos) and nothing that becomes a second job. That's what makes it survive your two-hour ceiling at 10× today's sponsor count, not just today.
- **Logos are logos only** — no ad copy, no UTM parameters. Keeps the README from turning into an ad unit and keeps the boundary in Step 8 honest.
- **These prices are effectively permanent** once published — GitHub Sponsors doesn't let you edit a live tier's price, only retire and replace it. Treat $100/$400/$900 as a real proposal, not a placeholder — argue with the numbers now, not in month four.

## Platform

**GitHub Sponsors, personal account. Nothing else.**

- 0% fee on personal accounts — the entire sponsorship reaches your bank account, no entity, no fiscal host.
- Every tier above tops out at $900/month, nowhere near the $5,000 invoiced-sponsorship floor, so you never need organization/invoiced billing (which would force the entity question you've already ruled out).
- Confirm your country is on GitHub Sponsors' supported list before publishing anything (it's region-gated with a waitlist for unsupported regions).
- Add **thanks.dev** alongside it — pure dependency-graph money, zero outreach, zero standing effort once your `FUNDING.yml` and manifest are filled in. It's the one channel that pays without you doing anything monthly, which is the entire point given your ceiling.
- Skip Open Collective / fiscal hosting entirely — that's the multi-maintainer, public-ledger, has-to-incorporate-adjacent path, and you've already said no to it.

## Ask

Page copy, answering the five questions every funder asks:

> **quillstream** is an audio DSP library [name what it does in one line — filters, effects chain, resampling, whatever the actual scope is]. It gets 41,000 docs views and 12,000 README views a month, and the newsletter that ships alongside it has 9,200 subscribers — people actively building on it, not just browsing.
>
> I maintain it solo, outside a day job, with no company or association behind it. Sponsorship money is the only thing standing between "maintained" and "maintained until I run out of evenings for it."
>
> **What it funds:** [name the real unit — CI minutes, docs hosting, a code-signing cert, a release cadence you're trying to protect]. Not "more development" — that number, specifically.
>
> **What sponsorship doesn't buy:** roadmap influence, merged pull requests, or priority outcomes on issues. Every contribution is judged on merit whether or not the author sponsors.
>
> Money goes to me personally via GitHub Sponsors — no entity, no invoicing, no fiscal host in the way.

`.github/FUNDING.yml`:

```yaml
github: [your-username]
custom: ["https://quillstream.example/sponsors"]
```

Add the org-level fallback check too (`{owner}/.github/FUNDING.yml`) if quillstream lives under an org rather than your personal namespace — a stale one there silently overrides nothing.

Surfaces carrying the link, in order of effort: README badge near the top, docs site footer, newsletter footer, one line in release notes ("If quillstream saves you time, sponsor it →"). Fill the package-manifest funding field too, in whichever registry you publish to (npm's `funding` key, or the equivalent for your ecosystem — tell me the language and I'll give you the exact field). Verify every link resolves before you publish the ladder; a dead link silently kills the dependency-graph channel too.

## Corporate lane

- **Dependency-share (do now, near-zero):** `FUNDING.yml` + manifest metadata + thanks.dev, done above. This is the channel that pays without you pitching anyone — Sentry's program hit 95%+ coverage of its dependency tree at $4–$10 each and was "likely the first and sole sponsor" for most of them. Being findable is the whole ask.
- **Employee-nominated funds (no action, free upside):** programs like Indeed's FOSS Contributor Fund ($10,000/month, one project per cycle) require only an OSI license and a funding mechanism — both now true. The nomination comes from an engineer at a company who already files your issues; you don't pitch this one, you just don't disqualify yourself from it.
- **Strategic outreach (one-time, not recurring — do it in a good month, not the two-hour ceiling):** identify 3–5 companies actually shipping quillstream in production — reverse-dependency search, issues filed from company email domains, job posts naming it. You didn't name any yet, so this is a research pass before it's an outreach pass. Send the Studio/Partner tier directly, not a generic ask:

> Subject: quillstream maintenance — support tier for \<Company>
>
> Hi \<Name>, I maintain quillstream. \<Their repo/product> depends on it \[cite the evidence], so this is likely load-bearing for you.
>
> I maintain it solo, evenings. I've set up a Studio tier ($400/mo) — logo on the README and docs (53k combined monthly views) — for companies running it in production. If that's useful, I can send an invoice-free sign-up link this week.

- **Foundation/pledge membership — skip for now.** Open Source Pledge and similar are won by being noticed at scale, not by applying. Nothing to build yet.

## Boundaries

Publish these before the first sponsor, not after the first awkward ask:

- Sponsorship buys visibility and gratitude — never roadmap control or merged pull requests. Contributions are judged on merit regardless of sponsor status.
- No priority *outcomes* are sold on this ladder (there's no triage-speed tier here at all — that's an Access/Retainer reward and both are deleted).
- Sponsor list, roadmap and review queue stay three separate artifacts.
- Logos are logos — no copy, no UTM parameters, no "featured partner" language implying endorsement.
- **Refusal rule (default, confirm or edit):** decline sponsors whose product competes directly with quillstream, or where the sponsorship would read as an endorsement you don't intend. You didn't answer "what would you refuse to sell at any price" — this is a placeholder, not your answer.

## Measurement

Review at 90 days, then quarterly:

| Question | Metric | Ignore |
|---|---|---|
| Growing? | Recurring monthly amount, 6-month trend | Cumulative total raised |
| Who's paying? | Sponsor count, individual vs. company split | Stars, followers |
| Durable? | Churn, median tier, top-sponsor share of income | One-time spikes |
| Ask working? | Conversion per surface carrying the link | Page views alone |
| Promise kept? | Every published reward delivered on time | Thank-you replies |

Pass bar at 90 days: recurring income grew quarter over quarter, every reward shipped on time, no single sponsor is more than 50% of income, and at least one company tier is occupied. That last one is the real test of whether this became a two-year asset or just a nicer donate button — if Studio/Partner sit empty at 90 days while Backer/Supporter fill up, the ladder isn't the problem, the corporate-lane research pass above never happened.

## Open items to confirm

Filled in with defaults above so this ships as a complete plan, not a stalled interview — but these are the interview answers I didn't have:

- Sole maintainer, or a team? (Changes Step 8's split-authority question.)
- Real monthly cost the goal should name (CI, hosting, certs — whatever it actually is).
- Names of companies you know depend on quillstream, if any — shortcuts the research pass in the corporate lane.
- quillstream's language/package ecosystem — needed for the exact manifest funding-metadata field.
- Whether you run a build-in-public practice — decides sponsor-count vs. amount goal.
- Anything you'd refuse to sell regardless of price, beyond the default refusal rule above.