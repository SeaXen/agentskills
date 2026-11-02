**Venue: owned real-time chat, on Slack. Not Discord, not GitHub Discussions, not a forum.**

# Community Launch Brief — Duneshift

## 1. Verdict

Launch. 4-5 gates pass, one assumed.

- Demand: weak/assumed. No evidence given that partners already flag breakage to each other vs just to support. 30 partners hitting the same weekly breaking changes makes peer chatter likely, but confirm before/at launch — don't treat as proven.
- Owner: pass. Ines in the room all day + named 3-person rota (Berlin, São Paulo, Singapore) = near round-the-clock staffed presence. Strongest gate here.
- Purpose: pass. SPACES letter = Product. Claim: "hear about a shipped regression within hours, from the partners hitting it." One outcome, stated, measurable.
- Venue vacuum: pass. Pre-1.0, hand-picked 30-partner cohort — no existing space already serves this relationship.
- Seed supply: pass. 30 named partners (range is 20-50), all on GitHub, rota gives 3-timezone coverage matching a global partner base.

## 2. Audience and outcome

Audience: ~30 design partners, hands-on integrators of a pre-1.0 edge-function runtime. B2B, design-partner stage — buyer and user are likely the same person here, not split.

Primary outcome (SPACES: Product) — "surface breaking-change fallout within hours of each weekly release, direct from partners running it in production." No secondary outcome named; don't add one.

## 3. Venue — with rejected alternatives

Chosen: **owned real-time chat (Slack)**. Reasoning, not habit:

- Purpose = Product, and continuous presence is genuinely staffed (founder + 3-zone rota) → this is the named condition in the skill for promoting real-time chat above its normal rank.
- Real-time chat's usual weakness — no durable, indexed archive — is not a cost here. Answers go stale in weeks, and you want zero search/index footprint. The thing that normally kills this venue class doesn't apply to Duneshift; it's a rare match.
- Owner can be present most days (deletes the usual reason to rule real-time chat out).

Rejected:

- **Forge-native discussions (GitHub Discussions)** — an-hour-a-week, batched pace. Can't deliver "within hours." Its main edge, indexed/exportable durable answers, is worth nothing to you (no search interest, content decays in weeks). Reopens if latency need relaxes to days, or search visibility becomes wanted.
- **Owned async forum (Discourse)** — same latency mismatch, worse: adds a daily standing job and you host member data for a durability payoff you don't want. Reopens if answer half-life grows and search becomes a wanted acquisition channel.
- **Rented public space** — no owned relationship over a hand-picked 30-partner cohort, no control over pre-1.0 breaking-change chatter being public. No existing space to join anyway (vacuum gate already passed). Reopens only if the audience broadens past named partners into the general public.

Vendor — Slack over Discord: Slack's named best fit is "a bounded B2B customer community where the archive matters less than immediacy" — exact match. Discord's named best fit is a large, informal, hobbyist audience — mismatch for 30 named B2B partners. Slack free tier's 90-day history cap is a non-issue since answers are stale in weeks anyway.

Mechanics not independently re-verified live this session (WebFetch blocked). Last captured figures in this skill's own reference file: Slack Pro ≈ €8.25/user/month (annual). Re-check slack.com/pricing before buying 30 seats.

One-venue rule: Slack is the single primary venue. Keep GitHub issues as the bug system-of-record after triage — that's normal issue tracking, not a second community surface.

## 4. Community model and member mix

Model: founder-led, product-development flavor — Ines's presence carries trust, partners' feedback shapes the roadmap.

Target mix: with only 30 people, aim near all-active, not the web-scale 90-9-1 lurker ratio. At minimum, want most of the 30 posting when something breaks for them, not just DMing support privately.

## 5. Seeding plan

1. Personally invite all 30 by name. Ask: "flag anything broken within a day of upgrading, in #breaking-changes."
2. Open 3 channels max on day one: #general, #breaking-changes, #support. Add more only once one gets noisy.
3. Seed 5-10 messages: Ines/rota post an upcoming known breaking change ahead of a release, modeling the heads-up format partners should use back.
4. Ritual from week one: weekly pinned "what shipped, what might break" post from Ines or rota.
5. Publish a response-time commitment matching the rota: answers within 2 hours during business hours across the 3 covered zones.

## 6. First 90 days

Audience quirk: the 30 partners already are the whole addressable audience, so the usual founding-cohort → invited-beta → public-announcement sequence collapses — there's no wider public to open to, and you don't want one.

1. Weeks 1-2: invite all 30 directly. No public announcement phase — stays closed permanently.
2. Weeks 3-6: normal operation. Watch day-30 leading indicators: any post from someone outside Ines/rota, any question answered by a peer, first-response median under a few hours.
3. Weeks 7-12: keep closed. Do not expand past the 30 — matches the zero-search-visibility stance.

## 7. Thresholds and measurement

Room is small (30) and B2B — use absolute counts, not percentages (skill explicitly allows this adjustment for small B2B rooms):

- Regressions acknowledged within 2h: target 90%+ of reports.
- 15+ of 30 partners post at least once in first 30 days.
- 3+ of 30 act as peer-first responders (answer before rota does) by day 60.

Basis: the 24h-response and non-staff-share metrics are published baselines (Mozilla/GitHub Open Source Guides, community-marketing practice); the 2-hour bar and absolute-count adjustment are set here for this room's size and latency need.

Two or more of these missing at day 90 → don't add promotion (there's no wider audience to add anyway) → re-run seeding on the specific gap, or fold back.

## 8. Fold-back criteria

Standard fold-back order (archive read-only > merge > convert to support channel) mostly doesn't apply here: archiving buys search-value you don't want, and there's no existing space to merge into. So the only real exit is: if response-within-2h stays under 50% at day 90, or partners never answer each other (all traffic is Ines/rota-only), convert to a plain support channel and drop the community framing. Decision owner: Ines.

## 9. Open risks

- Demand gate is assumed, not evidenced — confirm partners already flag issues peer-to-peer (not just to support) before or right after launch.
- Staff-dominated risk: Ines + rota both being highly present can crowd out peer answers. Deliberately hold back and let partners answer each other first when possible.
- Competitive exposure: 30 partners posting bugs in view of 29 other companies may deter candor. Ask Ines whether that's acceptable or needs a private-per-partner override for sensitive cases (gate any such private channel on real need, not default-open — private channels fragment fast).
- Slack pricing/limits not independently re-verified live this session — confirm on slack.com/pricing before purchasing seats.

**Next:** confirm the demand-gate assumption with Ines (ask her directly: do partners already DM each other or forward each other's workarounds?), then create the Slack workspace and send the 30 invites.