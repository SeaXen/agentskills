# Trellisway: the move

**Core read:** you don't have a marketing problem. You have 9,400 installs and zero revenue — that's a *monetization design* problem. Distribution already exists. Nobody has to discover Trellisway; you have to give the ~5,450 companies already running it a reason to pay. That's a much shorter, cheaper problem than the one most OSS-to-business stories start with.

## The one decision that shapes everything else

**Don't touch the Apache-2.0 license on the core.** Don't relicense to BSL/SSPL, don't retroactively restrict it. You have 9,400 installs' worth of trust; a HashiCorp-style relicense is how you turn your own users into a fork (see Terraform → OpenTofu). You have no leverage to survive that fight — no sales org, no brand moat, 14 months of runway.

Monetize *around* the core instead: open-core features + a hosted Cloud, both closed-source add-ons, core untouched. This is the Grafana/GitLab/dbt/Temporal playbook, and it's the only one compatible with keeping the goodwill that's your actual asset.

## Why Cloud, not enterprise features, not support contracts

Three monetization paths exist for an OSS infra project. Rank them against your actual constraints (5 people, 14 months, two SREs, zero sales reps):

| Path | Fit for you |
|---|---|
| **Hosted Cloud** (managed control plane, self-serve, usage/seat priced) | ✅ Best fit. Plays to what SREs are actually good at — running reliable infra — and sells itself through the product, not a sales team. |
| **Open-core enterprise features** (SSO, RBAC, audit log, multi-tenancy) | Real, but sales-led — security reviews, procurement, MSAs. Layer in later, don't lead with it. |
| **Support/SLA contracts** | Lowest leverage, most relationship-selling, worst match for a team that has "never sold anything." Fine as an opportunistic side-deal, not a strategy. |

Lead with Cloud. It converts existing self-hosting *pain* (running your own scheduler, metadata DB, HA, upgrades) directly into a subscription, and the sale is "stop doing this yourself" — a technical argument to a technical buyer, which is the only kind of selling your team can currently do credibly.

**Build it BYO-compute**: you host the control plane (scheduler, UI, run history), customers' workers run in their own VPC/cluster. This keeps your infra bill from ballooning on a 14-month runway and matches how Temporal Cloud and Astronomer are architected.

## Sanity check on the market

Workflow orchestration is a **large, high-frequency** problem — teams hit it every day, not once a quarter. That's the best quadrant for marketing to compound in. The fundamentals justify building a real GTM motion here; this isn't a niche tool you're overinvesting in.

## First move: you don't actually know your buyer yet

"58% inside companies" is a telemetry ping, not a validated willingness to pay. It could mean production dependency or a dev's laptop. Before building anything, find out:

1. **Instrument better signal.** Add an opt-in "tell us about your deployment" prompt in the web UI/docs. You need identified accounts, not anonymous pings.
2. **Interview 20–30 power users** — longest-running installs, highest DAG counts from telemetry. Ask JTBD-style: what are they hiring Trellisway to do, what's the worst part of self-hosting it, what would make them pay to not run it themselves, what's the one missing feature that blocks them today (SSO? multi-tenancy? alerting? cost visibility?).
3. Use this to sharpen positioning against Airflow (ops-heavy incumbent), Prefect and Dagster (direct open-core comps). Right now you don't have a stated reason someone picks you over them — get one from the interviews, don't guess it.

This is 2–3 weeks of work for whichever founder is best at talking to people. Do not skip it to start building Cloud sooner — you'll price and package blind otherwise.

## Pricing: pick a number, don't research it for months

You're a B2B infra tool sold to engineering teams — that's the **~$100–$1,000/mo bucket**, not the $9-prosumer trap. Don't run Van Westendorp studies on day one; you don't have a price to optimize yet, you have a bet to place.

- Ship a **Starter** tier: self-serve, credit card, seat- or run-volume priced, something like $200–$400/mo to start.
- Keep price **public**. Your buyers are engineers — "Contact Sales" gating is a bounce, not a qualifier, for this audience.
- Gate SSO/RBAC/audit log behind a **Business** tier — this is where the "58% inside companies" segment actually pays, once they self-identify by asking for it.
- If nobody flinches at the price in the first month, raise it. That's a real signal; a spreadsheet isn't.

## GTM: product-led, not sales-led

You have no sales muscle — don't fake it. Use the channel you already have: the product itself, running inside 5,450 companies right now.

- **In-product nudge**: when self-hosted users hit the pain points your interviews surface (scheduler bottleneck, metadata DB growth, retry pileups), surface Cloud right there. Timeliness beats any outbound email you could write.
- **Technical content, not marketing content**: reliability/SRE-grade writeups ("how we run our own scheduler at the scale our Cloud customers need") — this is content your team can write *authentically*, unlike generic thought-leadership copy.
- **Founder-led, not team-led sales**: when a company inbounds asking for SSO or a contract, handle it personally. Don't hire a VP Sales or an SDR yet — that's the wrong first hire for a PLG motion, and it burns runway on a skill you can't yet evaluate candidates for.

## 90-day plan

| When | Do |
|---|---|
| **Now – Oct 7** | Ship the deployment-survey prompt. Identify 30 power users from telemetry. |
| **Oct 7–21** | Run the interviews. Write down, verbatim, why they'd pay and what blocks them. |
| **Oct 21 – Nov 4** | Scope the smallest viable Cloud: control plane only, BYO workers. Pick one price. |
| **Nov 4 – Dec 15** | Build it. Launch as a beta to the installed base via in-product nudge + one honest "why we built Cloud" post. Target: 10–20 paying beta customers. |
| **Dec 15 – Mar 2027** | Iterate price and packaging on real signups. Start layering SSO/RBAC behind Business tier for inbound requests. |
| **Month 6 checkpoint** | Look at MRR and beta retention. With ~8 months of runway left, decide: raise on this traction, or cut burn and go for ramen-profitable. Don't defer this decision past month 6 — you won't have runway left to recover from deferring it. |

## Tripwires

- ⚠️ If 30 outreach attempts can't get you 20 interviews, that's itself the finding — it means "58% inside companies" is dev/test noise, and the whole plan above needs re-anchoring on a different segment.
- ⚠️ Don't let Cloud compute costs creep onto your books — BYO-workers is the fence against that, keep it.
- ⚠️ Don't build a sales org before 10 self-serve paying customers exist. Premature sales-led motion is the single most common way teams like yours burn the last 6 months of runway on a skill they don't have yet.
- ⚠️ Don't touch the Apache-2.0 core license, ever, no matter how tempting it looks at month 10 when revenue is still thin. It's the one asset you can't rebuild if you lose it.