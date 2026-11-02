# Runnelgraph Commercial Model — Internal One-Pager

## The Model

Runnelgraph the project stays 100% Apache-2.0 — no dual license, no proprietary edition, no future relicense planned. We monetize entirely through a managed service (hosting, operations, support, SLAs) built around the open-source core. Anyone can self-host for free, forever. We charge for not having to.

## Why This Model

- **Trust compounds adoption.** A license that can't be revoked removes the single biggest objection enterprises raise before standardizing on an open-source dependency.
- **No bait-and-switch risk.** Elastic, MongoDB, and HashiCorp all relicensed after building on permissive licenses, and each took public trust damage plus forks (OpenSearch, Valkey, OpenTofu) as a result. We're pre-committing out of that path.
- **Community growth is the moat, not the license.** Contributions, integrations, and word-of-mouth compound while the code stays permissive; a restrictive license would blunt exactly the adoption we're relying on.
- **The service, not the code, is the product.** Ops maturity, uptime, and support are harder to copy than a repo.

## Scope: Free vs. Paid

| Free (Apache-2.0, self-hosted) | Paid (managed service) |
|---|---|
| Full source, full feature set | Hosting, upgrades, backups |
| Community support (GitHub issues, Discord/Slack) | Uptime SLA, on-call support |
| Self-managed scaling, security, upgrades | Managed scaling, security hardening, compliance support |

No feature gate. No "enterprise-only" fork of the code. If a customer wants to run it themselves, nothing in the repo stops them — the pitch has to win on convenience, not lock-in.

## What Each Function Does Differently

- **Engineering:** every PR lands in the public Apache-2.0 repo. No feature is built commercial-only. Managed-service-specific code (multi-tenancy, billing, provisioning) lives in a separate private repo, never in Runnelgraph itself.
- **DevRel / Marketing:** growth is community-led — docs, examples, integrations, conference presence. Message the license explicitly as a differentiator against competitors who've relicensed.
- **Sales / Success:** sell against "why pay when I can self-host" with ops burden, SLA, and time-to-value — never with "the free version is crippled," because it isn't.

## Metrics We Track (Monthly)

| Metric | What it tells us | Owner | Watch-out |
|---|---|---|---|
| **MRR** | Whether the service is monetizing | [Owner] | The only metric that proves the model is working — treat it as primary |
| **GitHub stars** | Awareness / top-of-funnel trend | [Owner] | Vanity signal — stars don't gate, don't convert, and can be bought or spiked by a single HN post. Track as a trendline, never present as "X developers use Runnelgraph" |

Neither metric alone tells the full story: stars can climb while MRR stalls (interest without conversion) or MRR can grow while stars flatten (expansion within an existing base). Read them together, monthly, same review.

## Risks

**Competition** — Apache-2.0 means any well-funded player, including a cloud provider, can host Runnelgraph itself and undercut us on price. This is the direct tradeoff of not relicensing.
*Mitigation:* win on operational quality and support responsiveness a generic hosted offering won't match; move faster on integrations than a third-party host would bother to.

**Execution** — the entire commercial case rests on our ops being visibly better than self-hosting. If uptime, support latency, or upgrade friction disappoint early customers, there's no license lock-in to fall back on.
*Mitigation:* treat SLA and support-response metrics as launch-blocking, not post-launch cleanup.

**Market timing** — committing to a pure hosted-service model assumes the market will pay for convenience now rather than waiting for demand to mature or for a cheaper host to appear first.
*Mitigation:* validate willingness-to-pay with design partners before scaling spend on the managed offering; treat early MRR trajectory as the go/no-go signal, not sentiment.

## Cadence

Review MRR + GitHub stars together on the same monthly cadence. Re-check the three risks above quarterly — flag to [Owner] immediately if a cloud provider announces a competing hosted offering, since that changes the competition risk from theoretical to active.