Run this first — five minutes — before touching the allocation below:

```
# Node
npm ls --all --omit=dev --json > deps.json
# Go
go list -m all > deps.txt
# Python
pip list --format=json > deps.json
```

That's your real dependency graph. Everything below is a template built on real, well-known OSS funding recipients — swap in whatever your SBOM actually shows once you have it. Don't skip this step: the whole point of the exercise is that the money goes to what you actually run, not what a generic list assumes you run.

## Split the $4,000: $2,000 automated, $2,000 hand-picked

**$2,000/mo → thanks.dev or Tidelift, pointed at your real manifest.**
Both scan your actual lockfiles and split payment across every maintainer in your dependency tree, weighted by usage. This is the fix for "we don't know our whole stack" — you don't have to know it, the tool reads it. It also self-updates: add a dependency next quarter, it's covered next quarter, no manual re-allocation. Tidelift additionally gives you licensing/security assurances you can cite directly in the board report.

**$2,000/mo → 6-8 hand-picked flagship sponsorships**, for the projects where a direct relationship and public recognition matter more than diffuse coverage. Automated splitting is fair but invisible — nobody screenshots a thanks.dev dashboard for the board. A named sponsorship with your logo on a project's site is the actual proof artifact.

Starter portfolio (real projects, real sponsor pages, genuinely small/single-maintainer critical infra — replace any row that isn't in your actual SBOM):

| Project | Maintainer | Platform | Monthly | Why this one |
|---|---|---|---|---|
| core-js | Denis Pushkarev | Open Collective | $400 | Embedded in nearly every JS build chain, historically and publicly underfunded relative to usage |
| Vite / Vitest | Anthony Fu / VoidZero | GitHub Sponsors | $300 | Build-tool bus factor; funds documented in their own transparency reports |
| pnpm | Zoltan Kochan | GitHub Sponsors | $250 | Single maintainer, used in nearly every JS CI pipeline |
| Caddy | Matt Holt | GitHub Sponsors | $250 | Solo-founder-led, if you run it as ingress/reverse proxy |
| pytest | pytest-dev | Open Collective | $250 | If Python is in your stack, this is close to unavoidable |
| ripgrep / BurntSushi tools | Andrew Gallant | GitHub Sponsors | $250 | Widely embedded in dev tooling and CI images |
| Zod | Colin McDonnell | GitHub Sponsors | $150 | Common validation dependency, small team |
| pgx | Jack Christensen | GitHub Sponsors | $150 | If Postgres-from-Go is in your stack |

Sums to $2,000. Drop any row that isn't a real dependency; redistribute its amount toward whichever real dependency in your SBOM has the fewest maintainers and the highest usage — that combination (small team, high blast radius if it stalls) is the actual selection criterion, not project fame.

## Picking the tier on each sponsor page

Don't chase the cheapest or the most expensive tier. Rule of thumb:

1. Take the highest tier that still gets you **name/logo placement** on the project's README or site. That placement is your board evidence — screenshot it each quarter.
2. If a tier includes **private security advisory access** or a **support/triage channel**, take it — that's operational value, not goodwill.
3. Skip "contact us / enterprise" tiers without talking to the maintainer first; those often assume a much larger check or an actual call, not worth it at $150-400/mo.
4. Most individual-maintainer GitHub Sponsors and Open Collective pages accept a **custom recurring amount** — you don't have to match a preset tier exactly. Verify the live tier names/prices before committing; they change and I'm not going to state stale numbers as current fact.

## What to show the board

A one-page quarterly scorecard, not a narrative. Four blocks:

1. **Coverage** — dollars deployed, number of projects funded, % of your critical dependency graph (bus-factor ≤2 projects) that now has funding.
2. **Risk mitigated** — name the specific bus-factor-1 projects you funded and what "unmaintained" would have cost you (engineering hours to fork/patch internally — put a number on it, even a rough one).
3. **Direct return** — security advisories received early, PRs from your engineers that got merged faster post-sponsorship, any support SLA actually used.
4. **Visibility** — screenshots of your logo/name on sponsor pages, plus any recruiting or press mention that cited it.

Frame this as insurance and engineering-brand spend, not marketing ROI — $4,000/mo funding maintainers doesn't move a revenue number, and claiming it does will read as dishonest to a board that can do the math. "We removed single-points-of-failure in infrastructure we run in production, for less than one engineer-day of fully-loaded cost per month" is the honest and strong version of this pitch.

Next action: run the three SBOM commands above, and tell me which languages actually came back non-empty — I'll rebuild the flagship table against your real list instead of the placeholder one.

Parked, not solved here: funding inbound for your own CLI (3k stars) is a separate problem — different mechanism (you're the recipient, not the payer) — pick it up next month.