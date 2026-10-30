# Advertising agent skills

> A bunch of skills for spending paid media budget on purpose.

A collection of **agent skills for paid advertising**: channel selection, budget policy, audience design, creative development, and measurement, across search, paid social, video, native, and AI-answer surfaces.

Built for **media buyers, performance marketers, PPC specialists, and growth leads** running real budgets in B2B and B2C.

## Related Collections

Other skills repositories I built for my colleagues at **Nativa Labs**:

- [`partnerships-skills`](https://github.com/mbfinotti/partnerships-skills): Partner ecosystem operations: _for partner managers, BD leads, ecosystem heads_
- [`revops-skills`](https://github.com/mbfinotti/revops-skills): Revenue operations: _for RevOps managers, sales ops, marketing ops, CRM admins_
- [`sales-skills`](https://github.com/mbfinotti/sales-skills): Sales execution: _for SDRs, AEs, sales managers, heads of sales_

## Install

Install every skill in this repo, not just one. Skills here are atomic by design and reference each other freely: picking a single skill leaves its sibling skills uninstalled, so cross-references and routed handoffs go nowhere.

**skills.sh (universal)**: works with any Agent Skills-compatible tool:

```bash
npx skills add mbfinotti/advertising-skills
```

**Claude.ai**:

1. add as a plugin marketplace: open **Settings -> Capabilities -> Plugins**
2. click **Add -> Add marketplace -> Add from a repository**
3. enter `mbfinotti/advertising-skills`
4. then **Sync**

**Claude Code**: install the plugin:

```bash
/plugin marketplace add mbfinotti/advertising-skills
/plugin install advertising-skills@advertising-skills
```

**Codex (OpenAI)**: install via the Codex CLI:

```bash
codex plugin add github:mbfinotti/advertising-skills
```

**Cursor**: copy into Cursor's skills directory:

```bash
git clone https://github.com/mbfinotti/advertising-skills.git ~/.cursor/skills/advertising-skills
```

Cursor auto-discovers skills from `.agents/skills/` and `.cursor/skills/`.

**Gemini CLI**: install as a Gemini extension:

```bash
gemini extensions install https://github.com/mbfinotti/advertising-skills
```

Update with `gemini extensions update advertising-skills`.

## Skills

This collection covers the full advertising surface.

### Start here

[`advertising-kickoff`](./skills/advertising-kickoff): Routes a paid advertising task to the right skill in this collection and bootstraps a shared project context artifact reused across sessions.

### Meta

- [`advertising-career`](./skills/advertising-career): Plans a paid media career from the candidate side: the junior-to-lead ladder, interview formats, an NDA-safe portfolio, and pay conversations.
- [`advertising-hiring`](./skills/advertising-hiring): Builds the employer-side hiring packet for a paid advertising role: outcome scorecard, interview loop, work sample, and a 30-60-90 ramp.
- [`advertising-radar`](./skills/advertising-radar): Assembles a time-budgeted watch list of newsletters, podcasts, platform release notes, communities, and people, with a method for keeping it fresh.

### Strategy & planning

- [`ad-platform-selection`](./skills/ad-platform-selection): Decides which paid channel families fit the business's economics, audience, funnel stage, and budget before any campaign gets built.
- [`ad-spend-allocation`](./skills/ad-spend-allocation): Splits a fixed paid media budget across campaigns, platforms, funnel stages, and audiences based on expected marginal return.
- [`ad-format-fit`](./skills/ad-format-fit): Flags ad formats mismatched to the objective, funnel stage, or production capacity, then separates a format problem from a creative one post-launch.
- [`paid-media-scaling`](./skills/paid-media-scaling): Decides when a proven campaign has earned a budget increase, how large each step should be, and what triggers a rollback.
- [`cac-roas-benchmark`](./skills/cac-roas-benchmark): Computes CAC and ROAS from real spend data and returns a healthy, watch, or unhealthy verdict against break-even, history, and external benchmarks.

### Audience & targeting

- [`ad-audience-targeting`](./skills/ad-audience-targeting): Turns an ICP and buying signals into layered audience tiers sized against platform floors, budgeted to the learning threshold, with exclusion rules.
- [`lookalike-audience-seeds`](./skills/lookalike-audience-seeds): Selects and sizes the seed customer list behind a lookalike audience, with a consent gate and a fallback ladder when the match floor is missed.
- [`ad-negative-keywords`](./skills/ad-negative-keywords): Mines search term reports into negative keyword lists, choosing match types, exclusion levels, and a review cadence that avoids overblocking converters.
- [`ad-buyer-group-mapper`](./skills/ad-buyer-group-mapper): Maps the buying committee for an offer and gives each role a messaging angle plus the targeting proxy that actually reaches them.
- [`retargeting-funnel`](./skills/retargeting-funnel): Designs a staged retargeting sequence with recency windows, behavioural depth tiers, a message and offer ladder, and per-stage frequency caps.

### Creative

- [`ad-creative-brief`](./skills/ad-creative-brief): Turns a campaign goal and an audience insight into a brief a designer, editor, or creator can execute, with specs and a revision loop.
- [`ad-copy-variants`](./skills/ad-copy-variants): Produces genuinely distinct copy variants from one value proposition, each labelled by angle, awareness stage, and formula so results stay attributable.
- [`ad-hook-analyzer`](./skills/ad-hook-analyzer): Scores and force-ranks candidate video ad openings to decide which hooks deserve test budget, returning a shortlist rather than a performance prediction.
- [`ad-creative-test-plan`](./skills/ad-creative-test-plan): Designs a pre-launch creative test with a falsifiable hypothesis, per-cell budgets, required sample, and kill or scale rules registered in advance.
- [`ad-creative-fatigue`](./skills/ad-creative-fatigue): Decides whether a creative is genuinely wearing out or a confounder explains the decline, returning a verdict with confidence and the highest-return remedy.
- [`ugc-ad-scripts`](./skills/ugc-ad-scripts): Writes UGC-style short-form video scripts a creator can film - hook, body, CTA - with hook variants, delivery notes, and disclosure lines.
- [`conversational-ad-copy`](./skills/conversational-ad-copy): Adapts messaging for one-shot ad slots inside AI assistant answers, covering recommendation register, situation targeting, grounding, and disclosure.
- [`thought-leadership-ads`](./skills/thought-leadership-ads): Plans a campaign promoting an executive's existing organic posts as paid person-fronted ads: selection, exclusions, permission, budget, and measurement.
- [`ad-swipe-file`](./skills/ad-swipe-file): Builds a queryable library of competitors' running ads classified by format, hook, offer, and funnel stage, then converts it into ranked test hypotheses.

### Campaign operations

- [`ad-bidding-strategy`](./skills/ad-bidding-strategy): Chooses the bidding policy per platform and goal, written up with an evaluation window, change discipline, and a rollback trigger.
- [`ad-budget-pacing`](./skills/ad-budget-pacing): Tracks spend against budget and flags under-pacing or over-pacing early, reporting the pacing ratio, projected spend, and the corrective daily spend.
- [`ad-spend-guardrails`](./skills/ad-spend-guardrails): Sets top-level spend policy - allowable CAC, ROAS floor, kill-switch thresholds, owners, overrides - derived from margin, payback, and runway.
- [`ad-campaign-consolidation`](./skills/ad-campaign-consolidation): Recommends which campaigns and ad sets to merge, which splits to preserve, and how to migrate without resetting learning across the account.

### Measurement & diagnostics

- [`ad-conversion-tracking`](./skills/ad-conversion-tracking): Verifies conversion events fire once and deduplicate correctly before launch, then turns the evidence into a GO or NO-GO decision.
- [`ad-attribution-gap`](./skills/ad-attribution-gap): Quantifies the discrepancy between platform, analytics, and CRM numbers, classifying every unit of the gap as timing, definitional, or unexplained residual.
- [`ad-account-diagnostic`](./skills/ad-account-diagnostic): Diagnoses the root cause of an underperforming ad account and returns a prioritised verdict with evidence and confidence, not a budget increase.
- [`paid-landing-page-audit`](./skills/paid-landing-page-audit): Audits a landing page taking paid traffic and returns a prioritised fix list covering message match, form friction, trust, speed, and mobile.

## License

MIT © 2026 Maya-Beth Finotti
