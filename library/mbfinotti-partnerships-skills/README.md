# Skills for Partnership teams

> Partner ecosystem operations, from channel program design to creator payouts.

A collection of agent skills covering the full **partnerships** surface: channel and alliance strategy, co-selling policy, affiliate program mechanics, referral incentives, and influencer deals.

Built for **partner managers, BD leads, affiliate managers, and ecosystem heads** who own partner revenue.

Every skill produces a **decision-ready artifact**: a scorecard, a policy, a rate card, a signed-off spec, not a generic checklist.

## Related Collections

Other skills repositories I built for my colleagues at **Nativa Labs**:

- [`advertising-skills`](https://github.com/mbfinotti/advertising-skills): Ad platform mastery: _for performance marketers, paid media managers, growth leads_
- [`revops-skills`](https://github.com/mbfinotti/revops-skills): Revenue operations: _for RevOps managers, sales ops, marketing ops, CRM admins_
- [`sales-skills`](https://github.com/mbfinotti/sales-skills): Sales execution: _for SDRs, AEs, sales managers, heads of sales_

## Install

Install every skill in this repo, not just one. Skills here are atomic by design and reference each other freely: picking a single skill leaves its sibling skills uninstalled, so cross-references and routed handoffs go nowhere.

**skills.sh (universal)**: works with any Agent Skills-compatible tool:

```bash
npx skills add mbfinotti/partnerships-skills
```

**Claude.ai**:

1. add as a plugin marketplace: open **Settings -> Capabilities -> Plugins**
2. click **Add -> Add marketplace -> Add from a repository**
3. enter `mbfinotti/partnerships-skills`
4. then **Sync**

**Claude Code**: install the plugin:

```bash
/plugin marketplace add mbfinotti/partnerships-skills
/plugin install partnerships-skills@partnerships-skills
```

**Codex (OpenAI)**: install via the Codex CLI:

```bash
codex plugin add github:mbfinotti/partnerships-skills
```

**Cursor**: copy into Cursor's skills directory:

```bash
git clone https://github.com/mbfinotti/partnerships-skills.git ~/.cursor/skills/partnerships-skills
```

Cursor auto-discovers skills from `.agents/skills/` and `.cursor/skills/`.

**Gemini CLI**: install as a Gemini extension:

```bash
gemini extensions install https://github.com/mbfinotti/partnerships-skills
```

Update with `gemini extensions update partnerships-skills`.

## Skills

This collection covers the full partnerships surface.

### Start here

[`partnerships-kickoff`](./skills/partnerships-kickoff): Routes a partnerships task to exactly one sibling skill and bootstraps the shared project context file so the next session starts warm.

### Meta

- [`partnerships-career`](./skills/partnerships-career): Plans a partnerships career from the candidate side: which of the four sub-disciplines to target, breaking in, interview prep, offer evaluation.
- [`partnerships-hiring`](./skills/partnerships-hiring): Plans partnerships hiring from the employer side: job posting and scorecard, interview loop, sourcing, compensation stance.

### Ecosystem strategy

- [`partner-ecosystem`](./skills/partner-ecosystem): Maps every partner type, account overlap, coverage gap, and conflict zone into a weighted scorecard and prioritization 2x2.
- [`alliance-prioritization`](./skills/alliance-prioritization): Ranks named candidate alliances by expected value, effort, and risk into a shortlist and a go/no-go recommendation memo.
- [`partner-economics`](./skills/partner-economics): Models one partner's P&L - margin, cost-to-serve, partner CAC, ramp, payback - to decide sign, scale, renegotiate, or exit.
- [`partner-ecosystem-expansion`](./skills/partner-ecosystem-expansion): Sequences which partner categories to launch next into a staged roadmap with readiness gates, capacity limits, and kill criteria.
- [`partner-marketplace-strategy`](./skills/partner-marketplace-strategy): Ranks candidate cloud, app store, and retail marketplaces by expected ROI, and sets the delist trigger for each.
- [`joint-gtm-planning`](./skills/joint-gtm-planning): Plans one joint go-to-market motion with a named partner: value proposition, campaign shape, budget, lead-sharing agreement.

### Channel program

- [`partner-channel-program`](./skills/partner-channel-program): Designs a partner program from scratch: readiness gate, partner value proposition, motions, tiers, benefits, economics envelope.
- [`partner-tiering`](./skills/partner-tiering): Designs the tier ladder inside an existing program: qualification criteria, benefit bundles, promotion and demotion rules, base migration.
- [`partner-enablement`](./skills/partner-enablement): Sequences the training, content, and certification roadmap that carries a partner to their first closed deal.
- [`co-selling-strategy`](./skills/co-selling-strategy): Defines how direct and partner sellers share deals: registration policy, deal credit splits, rules of engagement, comp neutrality.
- [`partner-channel-conflict`](./skills/partner-channel-conflict): Writes the channel conflict rules for contested deals: account segmentation, carve-outs, tie-breaks, escalation and adjudication ladders.
- [`partner-performance`](./skills/partner-performance): Builds the per-partner scorecard, QBR structure, and underperformance ladder from first trigger through de-tier or exit.

### Affiliate program

- [`affiliate-program-terms`](./skills/affiliate-program-terms): Drafts the clause-complete affiliate agreement: prohibited tactics, enforcement ladder, clawback mechanics, jurisdiction overlays.
- [`affiliate-commission-structure`](./skills/affiliate-commission-structure): Sets the commission rate model, tiers, recurring duration and caps, cookie window, and clawback terms from unit economics.
- [`affiliate-recruitment-outreach`](./skills/affiliate-recruitment-outreach): Drafts the recruitment pitch and follow-up sequence that brings content sites, newsletters, and communities into a program.
- [`affiliate-onboarding-sequence`](./skills/affiliate-onboarding-sequence): Designs the touch plan and asset kit that carry a newly approved affiliate from approval to first tracked conversion.
- [`affiliate-performance-dashboard`](./skills/affiliate-performance-dashboard): Specifies the affiliate dashboard: metric formulas, views per audience, refresh cadence, and alert thresholds.
- [`affiliate-payout-audit`](./skills/affiliate-payout-audit): Audits a commission payout run before disbursement and returns findings by severity with recommended holds.
- [`affiliate-fraud-detection`](./skills/affiliate-fraud-detection): Builds the rule set that flags cookie stuffing, fake leads, and self-referral rings, plus the investigation and escalation path.
- [`affiliate-disclosure-compliance`](./skills/affiliate-disclosure-compliance): Reviews a specific post, script, or live URL against FTC, UK, and EU disclosure rules and returns a pass/fail verdict with fixes.

### Referral

- [`referral-incentive-design`](./skills/referral-incentive-design): Sets who gets rewarded, reward type, amount against LTV and margin, payout trigger, and whether to build a tiered ladder.
- [`referral-abuse-guardrails`](./skills/referral-abuse-guardrails): Specifies the caps, velocity limits, hold windows, verification gates, and enforcement ladder that stop referral gaming.

### Influencer & creator

- [`influencer-discovery-brief`](./skills/influencer-discovery-brief): Defines weighted sourcing criteria and knockout screens, then produces a ranked creator shortlist with evidence per score.
- [`influencer-outreach`](./skills/influencer-outreach): Drafts the personalized first-touch pitch to one vetted creator, on the channel they list, with a bounded follow-up cadence.
- [`influencer-negotiation-playbook`](./skills/influencer-negotiation-playbook): Prepares term-by-term opening positions, a concession ladder, and walk-away thresholds for rates, usage rights, and exclusivity.
- [`influencer-campaign-brief`](./skills/influencer-campaign-brief): Writes the creative brief for a signed creator: deliverable specs, key messages, guardrails, disclosure, bounded review rounds.
- [`influencer-measurement-framework`](./skills/influencer-measurement-framework): Designs the pre-launch measurement plan: KPIs per objective, attribution method behind each, reporting cadence, declared blind spots.

## License

MIT © 2026 Maya-Beth Finotti
