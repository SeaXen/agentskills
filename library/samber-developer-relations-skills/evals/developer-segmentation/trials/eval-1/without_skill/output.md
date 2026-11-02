## Verdict

**Indie developers, next quarter. Not enterprise platform teams.**

This isn't close, and it's not because indie devs are "nicer" — it's because you have no monetization engine, and that fact changes which audience is actually valuable to chase.

## Why this debate exists but shouldn't

The indie-vs-enterprise fight is usually a revenue question: which segment converts to paid seats faster, which has higher ACV, which churns less. **That question doesn't apply to you.** No paid tier, no hosted version, founders on record ruling it out forever. So "enterprise platform teams" isn't a revenue bet here — it's a prestige bet (bigger logos, "used at Fortune 500" cred) dressed up as a growth strategy. Worth naming that plainly before the team spends a quarter on it.

**Steelman for the enterprise camp, because it's not crazy:** enterprise platform teams write bigger PRs, fund edge cases indie users never hit (multi-tenant migrations, huge tables, zero-downtime constraints), and occasionally show up with an engineer whose employer lets them contribute during work hours — real subsidized maintenance capacity. That's a legitimate reason to *want* them. It's not a reason to *target* them.

## Why indie wins anyway

1. **You don't have a channel to enterprise — you have a channel through indies.** Nobody's platform team discovers a schema-migration CLI via a sales deck; they discover it because an engineer already used it on a side project or snuck it into a work repo, then it survives contact with a real team. Enterprise adoption of tools like this is *always* downstream of individual engineers vouching for it. Skip the indie stage and you don't get a shortcut to enterprise — you get silence.

2. **Reach compounds, targeting doesn't.** At 11k stars / 60k installs you're still in the phase where mental availability — "the migration CLI you reach for by reflex" — is worth more than deepening relationships with a handful of platform teams. Narrowing to enterprise now trades a compounding, broad-reach asset for a narrow, linear one.

3. **Repositioning tax you can't afford.** Your current brand equity — dev-loved, simple, fast to adopt — is the exact opposite of what "built for enterprise platform teams" requires (governance workflows, approval chains, RBAC-flavored ceremony). You'd be competing against Liquibase/Bytebase on their turf, on a feature set you don't have, while diluting the DX reputation that got you 11k stars in the first place. That's not a quarter of work, that's a different product.

4. **Zero revenue capture makes the labor math brutal.** Winning an enterprise platform team typically costs you: security questionnaires, SOC2-flavored answers you can't fully give as a bare CLI, support SLA expectations, a "talk to us" motion. All real maintainer/devrel hours. With no paid tier, none of that converts to anything — not revenue, not even a support contract, since the founders have foreclosed that too. You'd be paying enterprise-sales-shaped costs for open-source-shaped returns.

## What "focus on indie" actually means this quarter

- **Cut time-to-first-migration.** Audit the quickstart — if it's not a working migration in under 5 minutes on a fresh project, that's the highest-leverage fix available, full stop.
- **Meet them where they already are.** Ship first-class integration guides/templates for the ORMs and stacks your installs are coming from (check your install telemetry by language/framework if you have it — that's your real ICP, not a guess). Get into starter templates and boilerplates where migrations get chosen once and never revisited.
- **Turn comparison searches into installs.** "X vs Flyway," "X vs golang-migrate," "migrating from Liquibase to X" — indie devs search this exact phrasing when evaluating. Enterprise platform teams don't search, they inherit whatever their engineer already picked.
- **Invest in the contributor funnel, not a sales funnel.** Good-first-issue pipeline, fast PR review, public thanks. This is literally how you buy the "subsidized maintenance capacity" the enterprise camp wants — via contributors, not procurement.
- **Content that spreads by itself.** Blog posts, conference talks, YouTube walkthroughs aimed at the individual engineer's problem ("my migrations broke prod at 2am") — this is what gets shared, not a whitepaper aimed at a platform team lead.

## Don't ignore enterprise — just don't build a motion for them

A few things are cheap, dual-purpose, and worth doing regardless of who you're "targeting": signed releases, an SBOM, a real semver/changelog discipline, a documented security-report process. Indie devs benefit from this too (nobody wants supply-chain risk in their weekend project either), and it quietly derisks enterprise adoption as a side effect — without you spending a single hour on enterprise outreach, case studies, or a "contact us" flow that leads nowhere.

If a platform team shows up on their own — via an engineer who already loved the tool — welcome them, take their PRs, and if they want to sponsor maintenance through GitHub Sponsors/Open Collective, take the money. That's upside capture, not a strategy to build a quarter around.

## ⚠️ Tripwire

If maintainer bandwidth — not adoption — becomes the binding constraint (issue/PR backlog growing faster than you can triage), that's the signal to invest in co-maintainers and contributor experience, not the signal to pivot toward enterprise. Chasing bigger logos when your actual bottleneck is throughput just adds obligation without adding hands.