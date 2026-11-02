## Kestrelbase Cloud Pricing Recommendation

### Headline

**Team tier at $399/mo** (usage-inclusive, metered overage beyond allowance), with a free tier below it and a $1,200–1,500/mo Scale tier above it for the heavy-usage decile. Not a single flat price — the 4x cost skew in your own beta data rules that out.

### Why not just copy the competitor's $400 flat, or cost-plus off your $0.0009/$0.011 numbers

- **Cost-plus is irrelevant here.** At $0.0009/M points and $0.011/GB-month, even a heavy account (illustratively: 10B points/mo + 1TB stored ≈ $9 + $11 = $20/mo COGS; the top-decile 4x case ≈ $80/mo) costs almost nothing next to a $350–500 price. COGS is a rounding error, not a constraint. Don't let it anchor the number.
- **Matching the competitor's $400 copies their packaging risk, not their economics.** A flat, unlimited-usage price is exactly what lets a 4x-cost whale get subsidized by the median account — that's the mechanism you should price around, not imitate.
- **The real floor is self-host TCO, not the $260 infra line alone.** Buyers who quote "$260/mo" to themselves are underpricing their own alternative. Add the 5 eng-hours/mo: at a fully-loaded $75–150/hr, that's $375–750/mo of labor on top of the $260 infra, i.e. **true self-host TCO ≈ $635–1,010/mo.** That — not $260 — is the ceiling-side anchor for the persona you're actually selling to (a mid-sized team, not a solo hobbyist).

So the pricing band is bounded by:
- **Floor:** $400 (competitor's sticker price) and $260 (self-host cash-only, for price-anchoring skeptics)
- **Ceiling:** ~$635–1,010/mo (true self-host TCO once engineer time is counted)

$399/mo sits just inside that band on the low side — cheap enough to look like an obvious win against both the competitor and self-hosting, expensive enough not to leave the TCO gap on the table.

### Structure: hybrid flat-plus-usage, not pure metering and not pure flat

A pure per-unit usage price is hard for a buyer coming from "$260/mo" or "$400/mo flat" mental models to predict, and undersells the fact that you're replacing a fixed subscription, not a variable one. Pure flat-unlimited reproduces the competitor's whale problem. Do both:

| Tier | Price | What it's for |
|---|---|---|
| **Free / Hobby** | $0 | Small usage cap, community support. Converts the 1,400-deployment self-hosted base at the low end; COGS near-zero at these volumes, so it's cheap top-of-funnel, not a loss leader. |
| **Team** (anchor) | **$399/mo**, includes a generous ingest+storage allowance sized to cover a typical/median account comfortably | The mid-sized-team persona in your prompt. Below both competitor sticker and true self-host TCO. |
| **Scale** | **~$1,200–1,500/mo** (not a straight 4x — give volume discount per unit), much larger allowance, priority support/SLA | For the top usage decile. Also the upgrade path when Team-tier overage starts adding up. |
| **Enterprise** | Custom, usage + SSO/VPC/dedicated support/SLA | Sales-assisted, for regulated/largest accounts. |

**Overage beyond each tier's allowance:** price at roughly 3–4x marginal cost — around **$0.003–0.004/M points ingested** and **$0.04–0.05/GB-month stored**. Still trivial in absolute terms for a customer (an extra 10B points ≈ $35), but it means the heaviest 10% pay proportionally for the 4x they actually cost instead of being cross-subsidized by the median account, and it creates a natural, visible nudge to upgrade to Scale rather than a silent margin leak.

### On undercutting vs. premium-pricing the competitor

$399 is a deliberate wedge, not a rounding accident: it lets you say "cheaper than [competitor], and transparently metered instead of quietly averaging heavy users into everyone's bill" — a real differentiator you can only make because your OSS install base already trusts the project and your COGS gives you the margin room to do it. The alternative — pricing at a premium ($450–500+) on a TCO-savings story alone — is defensible too, but with no demand signal yet, the cheaper/faster-adoption play against a warm 1,400-deployment funnel is the higher-confidence bet for a first launch.

### Annual discount

Standard 17–20% off for annual commit on Team and Scale, framed as "2 months free" — gives you upfront cash and a churn-dampening lock-in with no new pricing logic.

### Treat this as a bet, not a final answer

You have zero live conversion signal yet. Ship $399/mo, instrument conversion rate against the free tier and against competitor-comparison traffic, and watch the overage/Scale-upgrade rate as your read on whether the allowance sizing and the 4x skew assumption hold up outside the beta cohort. Raising this number later (once demand is proven) is a far cheaper mistake to fix than launching too high and never finding out you scared off the self-host conversions you're actually positioned to win.