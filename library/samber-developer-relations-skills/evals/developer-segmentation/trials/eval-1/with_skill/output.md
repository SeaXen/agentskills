# Verdict: build for solo & small-team builders this quarter. Enterprise platform teams are the explicit anti-segment.

The team's framing — "indie vs. enterprise" — hides the fact that Harbinger Labs removed the usual reason to chase enterprise: there is no purchase anywhere in this picture, for anyone, ever. That single fact (Apache 2.0, no paid tier, no hosted version, publicly permanent) changes the whole argument. "Enterprise platform teams" can only be justified on non-revenue grounds — reference logos, contributor supply, category ownership — never on deal value, because there is no deal. Below is the full segment map, run through `developer-segmentation`.

## Working assumptions (stated explicitly, since this ran as a single pass, not the interview)

I don't have your telemetry, so I built this from what you gave me (11k stars, 60k monthly installs, Apache 2.0, no monetization, ever) plus published population data, and marked everything else **inferred**. Two things I assumed that you should confirm with your founders before treating this as final:

- **Funded driver**: since revenue and sales enablement are structurally impossible, I scored against *developer adoption + category ownership* (the metrics you led with — stars, installs — are usually the tell for what leadership actually tracks). If the real funded driver is talent brand or contributor supply instead, re-weight step 5 below; the ranking arithmetic is shown so you can redo it.
- **No install-channel data**: I don't know your Homebrew/curl vs. Docker/Terraform/K8s-operator split. That single number is the cheapest test that would upgrade this map from *estimated* to *measured* — see Hypotheses.

## Cuts considered (step 1–2)

Three candidate cuts of the same audience, ranked on evidence cost given your "next quarter" deadline:

1. **Buying-mode cut (deleted, not ranked)** — no purchase exists for anyone, at any size. The skill deletes this cut outright when question 4 answers "no purchase at all," and it does here.
2. **Sector/workload cut (rejected)** — fintech backend vs. e-commerce vs. general SaaS. Schema-migration pain is shaped by database engine and deploy topology, not industry vertical; a regulated-industry backend and an e-commerce backend hit the identical migration problem. This returns one dominant, non-discriminating cell — rejected in brainstorming, not scored.
3. **Firmographic (team/infra scale) × role-in-decision (evaluator-only vs. evaluator+approver)** — a real cut, but the approver-side evidence lives in sales notes and interviews you don't have (no sales function exists here), pushing it into weeks of research you don't have time for this horizon.
4. **Firmographic (team/infra scale) × technographic (install/integration context: local CLI vs. CI-embedded vs. infra-as-code-embedded) — chosen.** Same firmographic axis as #3, but the second axis is something you can query from your own release/package-registry analytics today — Homebrew/curl pulls cluster with solo devs, Docker/Terraform-registry/K8s-operator pulls cluster with platform teams. Near-zero incremental research cost, which is what a near deadline should select for.

**Discarded explicitly:**
- **Seniority** — a junior and a staff engineer running the same DB stack need the same CLI and the same docs. Only relevant here if it maps to org-wide tool-standardization authority, which is already captured by the firmographic axis instead.
- **Language/runtime ecosystem** as a standalone axis — the tool acts on the database, not the host language, so it doesn't discriminate the artefact the way it would for an SDK.

## The map

```
# Developer segment map — Harbinger Labs [migration CLI], Q4 2026

## Cut
Dimensions: firmographic (team / infra scale: solo → platform-scale) × technographic
(install & integration context: local CLI → CI-embedded → infra-as-code-embedded).
Rejected: buying-mode — no purchase exists at any size, so it cannot discriminate.
Rejected: sector/workload — the same DB-engine pain hits every vertical identically.
Rejected: seniority — same stack, same CLI, same docs, regardless of level.

## Segments

| Segment | Definition | Size + confidence | Decision unit | Needs | Where they gather | Evidence |
|---|---|---|---|---|---|---|
| Solo & small-team builders | 1-5 engineers, install via Homebrew/curl/binary, run migrations from a laptop or a single CI job | ~5M-9M developers, estimated (SlashData Q1 2026 cloud-native population implies ~51M global developers; Stack Overflow 2025 back-end+architect role share ~20% ≈ ~10M schema-migration-relevant developers; solo/small-team share of that inferred at ~50-65% from typical company-size shape) | user = buyer, or no purchase at all — nobody to veto | 10-minute quickstart, zero-config defaults, docs that don't assume a platform team behind them | GitHub, HN, r/programming, dev.to, package-manager pages, awesome-lists | 11k stars, 60k monthly installs — measured (aggregate, no channel split yet) |
| Growth-stage product & backend teams | 6-40 engineers, install embedded in CI (GitHub Actions/GitLab CI), a few services sharing one DB-ops workflow | ~2M-4M developers / order of ~150k-400k companies globally in this band, inferred (same population method, company-size split not directly sourced — firm up via job-posting counts for backend/platform roles at 20-200-engineer companies) | developer evaluates and champions; a tech lead occasionally approves standardizing org-wide; still no economic buyer | CI-native packaging (official Action/image), migration-from-Flyway/golang-migrate content, comparison docs | eng blogs, framework-specific Slack/Discord, conference lightning talks | none collected yet — hypothesis-adjacent, see Hypotheses |
| Enterprise platform teams | 50+ engineers, many services/DBs, install via Terraform provider / Kubernetes operator / GitOps pipeline | order of ~15k-40k companies globally, inferred (analogous to job-posting-based sizing in comparable maps; no live lookup run this pass — treat as a rough shape, not a count) | developer evaluates; platform lead approves; security/license reviewer can still veto a free dependency (SBOM, supply-chain review) — but **no economic buyer exists**, because there is nothing to buy | Terraform provider, K8s operator, audit-log/dry-run story, security questionnaire answers, an SLA-shaped support promise the project cannot structurally offer | analyst content, LinkedIn, infra conferences, CNCF-adjacent channels | 0 data points — hypothesis |
| OSS driver/integration contributors | people extending DB-engine or CI-platform support for the CLI itself | order of hundreds to low thousands, inferred | no purchase; justified only via contributor-supply, not adoption | stable plugin/driver API, contribution guide, predictable release cadence | the project's own issue tracker | 0 data points collected deliberately — hypothesis |

## Primary
Solo & small-team builders. Score (driver = adoption + category ownership, 1-3 scale):
size 3, reachability 3, fit 3, value 2, effort 1, competitive position 2, compounding 3.
Ratio = (3+3+3+2+2+3) / effort 1 = **16**. Wins by a wide margin on the only axis that
matters given a no-revenue product: cost to reach and serve them is lowest, and they are
the actual source of the stars/installs you're already tracking as success. They are also
the pipeline — today's solo user is next year's growth-stage champion and, occasionally,
the platform-team engineer who introduces it at their next job.

## Secondary
Growth-stage product & backend teams. Ratio = (2+2+3+3+2+3) / effort 2 = **7.5**. Served
almost entirely by artefacts the primary already funds (quickstart quality, CLI ergonomics,
docs), plus one cheap addition: official CI packaging and one migration-from-incumbent
guide. No dedicated event budget, no dedicated headcount this horizon.

## Anti-segment
Enterprise platform teams. Ratio = (2+1+2+2+1+2) / effort 3 = **3.3** — lowest of the three,
and not by a close margin. Reachability and competitive position both fail: your devrel
team cannot afford analyst/LinkedIn/enterprise-conference presence at the volume this
segment expects, and Flyway/Liquibase/Atlas already sell what this segment actually wants
(a support contract) — something structurally unbuildable without a commercial entity
behind the product. None of the three promote-anyway conditions apply: the artefact list
(Terraform provider, K8s operator, security review paperwork) isn't funded elsewhere, no
single reference is known to unlock the rest of the segment yet, and sales enablement
cannot be the funded driver because there is nothing to sell. Not served with dedicated
artefacts this horizon. Still say yes, and quote them, when they show up unprompted — that
costs nothing and is pure upside.

## Hypotheses
- Growth-stage product & backend teams: 0 collected data points, below the evidence floor
  despite being scored above. Test: pull 15-20 recent GitHub issues/star-history referrers
  and tag them by apparent team size; five DM/interview requests to recent adopters who
  starred from a company GitHub org. Drop the "team" framing if most activity turns out to
  be solo accounts using it at work.
- OSS driver/integration contributors: justified only via contributor-supply, not adoption.
  Test: read the last 10-15 issues/PRs tagged integration or driver, and ask who's asking.
  Drop if it's the same 3-4 people who already contribute for other reasons.
- Enterprise platform teams' size: order-of-magnitude only, no job-posting or LinkedIn
  lookup run. Not worth doing this quarter given the anti-segment call — revisit only if
  the anti-segment status is challenged.

## Implications
Build: quickstart/onboarding polish, an official CI Action/Docker image, one
migration-from-Flyway/golang-migrate comparison guide, community content in the channels
solo builders already read (HN, r/programming, dev.to, awesome-lists).
Publish: nothing enterprise-specific — no analyst content, no compliance one-pager, no
enterprise conference booth this horizon.
Prove: install-channel breakdown from your own release/registry analytics — the cheapest
lookup available, and the one that would move this whole map from estimated to measured.
Stop: any in-progress compliance-pack, SOC2-style questionnaire doc, or enterprise-targeted
sales-enablement content — it serves a segment this map just deprioritised, and would be
the exact "next steps contradict the ranking" failure this skill flags.

## Review
Re-read ~2026-12-18 (90 days). Early re-read if: the founders' no-monetization stance
changes; an enterprise platform team offers to fund a specific artefact (grant/sponsorship)
directly, which removes the "unfunded effort" objection; a competitor ships a free tier
that erodes the solo/small-team differentiation; or install-channel data shows platform-
scale (Terraform/K8s-operator) installs are a bigger share than assumed here.
```

## Quality gate

- Segments: 4 — within the 3-5 range. ✓
- Every segment names a differing artefact/channel/proof point from its siblings. ✓
- Every size carries a range, method, date (this pass, 2026-09-19) and confidence tier — mostly *estimated*/*inferred*, one *measured* aggregate (stars/installs). Weakest point in this map: no first-party channel split yet — flagged as the top hypothesis test.
- Every segment names its decision unit, including the structurally unusual "approver but no buyer" case for enterprise. ✓
- Evidence floor: only 1 of 4 funded/scored segments (solo builders, via your aggregate stars/installs) approaches the floor; growth-stage and enterprise are correctly labelled hypotheses. This map is lighter on evidence than the gate wants — commission the install-channel and issue-tagging tests before treating the ranking as locked in, not just as directional.
- Anti-segment is non-empty and names an audience the team visibly wanted to keep (enterprise platform teams) — the point of the exercise. ✓
- Two-page length and review date: met. ✓

## What would actually flip this

Not "enterprise is bigger" — it may well be, in raw headcount. What would flip it: the funded driver turning out to be something other than adoption (e.g., a named grant/sponsor specifically wants platform-team logos), or someone external agreeing to fund the Terraform-provider/K8s-operator artefact so the effort score for enterprise drops from 3 to 1-2. Absent either, this is a bottom-up OSS devtool, and bottom-up OSS devtools win by being trusted first by the people who have the least friction to try them — not by being sold to the people with the most process to get past.