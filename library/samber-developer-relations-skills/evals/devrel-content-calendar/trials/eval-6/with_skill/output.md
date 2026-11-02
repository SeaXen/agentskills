Read the skill and all three of its references (mix-and-capacity model, published findings, worked example). Here's the complete answer, per the skill.

---

# 1. The 80/20 evergreen/trending ratio

**No — it's not a devtools benchmark, and quoting it as one is a documented trap.**

- That split is creator-economy folklore. The material carrying it describes "the widely-reported baseline among solo creators" — short-form video accounts, with none of the review cost technical content carries.
- The same material adjusts to roughly **60/40–70/30 for fast-moving technical niches**. A CI runner qualifies.
- A *different* 80/20 is defensible: **80% committed capacity / 20% open slack** for reactive work — two independent planning conventions converge on it. Even that counts hours or slots, not reviewer passes; tighten downward if review is your bottleneck.

What to actually target:

- **Evergreen majority as a floor, not 80%.** It's a working baseline, not a measured optimum.
- A launch-dominated quarter legitimately runs ~60/40 — the skill's own worked example does.
- Replace the baseline with Ferrite's own decay data: how long a post keeps earning search and support deflection. One quarter of data and the ratio sets itself.

Cite the mechanism, never the number: evergreen keeps earning search traffic and support deflection after the release that prompted it — that's what makes next quarter cheaper, and it's the only mix that survives a slipped launch.

One warning: evergreen needs protection, not just a ratio. Promotional work arrives with deadlines and sponsors; evergreen arrives with neither, so it's what gets dropped when week 8 goes wrong. Give evergreen slots hard dates and a named reviewer, same as a launch piece.

# 2. The idea pile

| Idea | Verdict | Why |
|---|---|---|
| Agent handshake timeout (34 tickets) | ✅ Keep — **reroute to docs** | Cleanest demand signal in the pile, but it's a troubleshooting page, not a blog post |
| Scheduler rewrite in Rust | ✅ Keep | Strongest blog bet; flagship, with two caveats |
| 7 tips for faster builds | ❌ Cut as pitched | No evidence, no novelty; rescue path exists |
| Why we love open source | ❌ Cut | No evidence, no novelty, no anchor |

Note: the two rejects appear verbatim in the skill's *negative example* of a quarter planned badly.

**Agent handshake timeout — top priority, wrong surface as a blog post.** 34 tickets on one error string trips the volume rule: asked 3× = missing page; ~30× = a docs **or product** defect — and the slot must say which. If the handshake flow is genuinely broken, the fix is product and the page documents the workaround until it ships. Routing: specific error string → troubleshooting page, canonical URL, built from the resolution notes on those 34 tickets. Publishing it as a blog post is the exact "blog as dumping ground" failure the routing table exists to prevent. Value: evergreen, measurable support deflection.

**Rust scheduler rewrite — the quarter's flagship.** Trade-off story → engineering blog post. Write the bet's hypothesis down: *a real perf war story with reproducible numbers reaches senior platform engineers better than any tips content.* Two caveats:

- Benchmark-shaped content **fails late**. Before/after p99 needs reproducible measurements and honest limitations. Name the technical reviewer at planning time — someone who can dispute the claims — and don't schedule it against an anchor date.
- It earns a repurposing tree: talk pitch, recording, clips, a scheduler-tuning docs page. Schedule each derivative as its own slot.

**7 tips for faster builds.** Fails both gates: no observed demand behind it, and it passes no novelty filter (not counter-intuitive, counter-narrative, surprising, or an elegant articulation of something readers already feel) — ideas passing none produce accurate, unread pieces. Rescue path: check docs searches and community threads for build-speed questions. Demand exists → it's a performance-tuning guide in docs, not a listicle. Unproven → test in the cheapest format first (community post), promote winners up the cost ladder.

**Why we love open source.** Cut outright. If OSS presence matters at Ferrite, give it a job — contributor onboarding, governance, roadmap transparency — and bring it back with evidence. (Employer-branding value is already better served by the Rust deep dive.)

The keepers as slots:

| Working title | Surface | Pillar | Stage | Shelf life | Evidence / hypothesis | Reviewer |
| --- | --- | --- | --- | --- | --- | --- |
| "Agent handshake timeout": causes and fixes | docs (troubleshooting) | enablement | adopt | evergreen | 34 tickets, same error string + docs-vs-product-defect call | support lead |
| p99 queue latency: rewriting the scheduler in Rust | engineering blog | advocacy | discover | evergreen | bet: reproducible perf war story reaches senior platform eng | named engineer who can dispute claims |

Coverage check: two keepers = 2 surfaces, 2 stages. A full plan needs ≥3 surfaces and ≥2 stages — a third surface (changelog, community digest, video) has to come from elsewhere in the quarter.

# 3. Hero / Hub / Help

**No — evaluated and rejected in the source material.** Google's 3H model is built for a brand's *video channel*, not docs and release notes. As a year structure it lacks the three things that actually break devtools content plans: anchors (releases, CFPs, conferences), capacity in reviewer passes, and surfaces.

If the vocabulary helps, the mapping is: Hero ≈ anchor-bound launches + flagship bets (the Rust post), Hub ≈ evergreen enablement, Help ≈ demand-sourced slots (the handshake page). You already have all three as slot columns. What H³ adds is a label; what it costs you is the capacity model and demand pipeline — and Help-type content is precisely where those 34 tickets live, which a brand-video model structurally starves. Spend the consultant's framing fee on a technical reviewer's hours instead.

# What's missing before this becomes a calendar

To turn the two keepers into a dated quarterly slot table I'd need: the quarter and its fixed anchors (releases, conferences, CFP deadlines), the funding driver (adoption vs. existing-user enablement vs. sales support), writer weeks plus reviewer passes available, and last quarter's shipped-vs-planned. Say the word and I'll run the full interview.