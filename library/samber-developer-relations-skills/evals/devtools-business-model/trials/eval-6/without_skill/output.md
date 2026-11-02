## Bottom line

The plan describes three *nice-to-have* revenue streams, not a business. As written, it can't reliably fund two full-time salaries — the gaps aren't details to polish, they're missing revenue lanes.

## Math check first

400k monthly downloads tells you reach, not willingness to pay. Individual-developer sponsorship (GitHub Sponsors + a $6 badge) converts at fractions of a percent, even for beloved projects. Calibrate against the best-documented case: Sindre Sorhus, arguably the highest-earning individual OSS sponsor on GitHub, needed a decade and hundreds of packages to reach six figures a year — and that's one person's income, not two. A single library, however popular, sponsored mostly by individuals at $5–$100, realistically nets low hundreds to low thousands per month, not the ~$13–20k/month two founders need to live on. If you need real numbers, run a Van Westendorp-style gut check against your actual GitHub star/dependent graph rather than downloads — but go in assuming individual sponsorship is a *supplement*, not the engine.

## What's actually missing

**1. Company-tier sponsorship — this is the big one.** Companies with Pipesmith in production, not individual devs, are your real payers. $5/$25/$100 tiers are sized for individuals. Add a tier ($500–$5,000+/mo) explicitly aimed at organizations, with a real quid pro quo procurement can justify: logo placement, priority issue triage, roadmap input, a direct Slack channel. "Support the maintainers" doesn't get approved by finance; "priority support contract" does.

**2. No way to actually take corporate money.** GitHub Sponsors charges by card with no invoices, no PO numbers, no NET-30 — most companies' procurement can't pay that way at any meaningful amount. You need either Open Collective (fiscal sponsorship, transparent books, real invoices) or your own entity issuing invoices, or you'll lose every company that wants to pay you $2k/mo but whose AP department needs a PDF.

**3. No enterprise support/SLA product.** The standard open-core lever for infra/data tooling is a paid support contract: guaranteed response times, security patch commitments, migration help. This is usually the single largest line item for OSS-funded companies (see GitLab, Sourcegraph, most DB/infra projects) and it's absent from your plan entirely.

**4. Consulting has no engine.** "Take gigs when they come in" is passive — no packaging, no rate card, no inbound pipeline. It also has real downside risk you haven't priced in:
   - Reactive/lumpy revenue is a bad fit for "we just went full-time" — you need a floor, not a lottery ticket.
   - No legal entity/invoicing/liability coverage mentioned — if a client's data pipeline breaks in production, what's your exposure?
   - Scope creep with no fixed engagement shape (retainer vs. fixed-scope vs. time-and-materials).
   - Conflict of interest: a client will eventually want a feature built privately or prioritized for them — decide now what gets upstreamed vs. stays proprietary, before a contract forces the answer.
   - Time cannibalization: hours spent consulting are hours not spent on the project that drives downloads → sponsorship → more consulting leads. Cap it (e.g., ≤30–40% of capacity) or the flywheel stalls.

**5. The $6/mo "Pro badge" is thin and possibly redundant.** What does it actually give an individual beyond what a $5 GitHub Sponsor tier already gives (recognition)? Running a second payment surface (your own billing vs. GitHub's) for marginal differentiated value is extra infrastructure and support burden for a revenue line that was never going to move the needle. Either fold it into the Sponsors tiers or give it real functional value (private Discord, early builds, vote on roadmap) — right now it reads like a vanity SKU.

**6. No hosted/managed offering considered.** If Pipesmith's use case supports it (scheduling, monitoring, a UI, managed connectors), a paid cloud layer on top of the free self-hosted core is the standard way OSS data tools actually reach real ARR (see Supabase, Plausible, Metabase). Worth explicitly deciding "not doing this" rather than never considering it.

**7. Grants/foundations unexplored.** Depending on how critical Pipesmith is as infrastructure, things like Sovereign Tech Fund, NLnet, or GitHub's own OSS funding programs can be real non-dilutive money — worth a week of application-writing, not a core plan.

**8. No trademark/brand policy.** "Pipesmith Pro" as a paid product name needs basic trademark hygiene once money changes hands — otherwise nothing stops a fork from shipping its own "Pipesmith Pro."

## What I'd change

- Add a company/org sponsorship tier with real deliverables, priced for procurement (not goodwill).
- Set up Open Collective or a proper invoicing entity — you cannot capture corporate money through GitHub Sponsors alone.
- Package a paid support/SLA tier — this is probably your actual path to sustainable recurring revenue, not sponsorship.
- Turn consulting into a product: fixed-scope packages, a public rate card, a lightweight intake form, and an explicit cap on hours/month so it doesn't eat the project.
- Cut or re-scope the $6 badge — low effort either way, but decide deliberately rather than letting it linger as clutter.
- Treat GitHub Sponsors + badge as a goodwill/community signal, not the income plan. The income plan is support contracts + consulting + (maybe) a hosted layer.