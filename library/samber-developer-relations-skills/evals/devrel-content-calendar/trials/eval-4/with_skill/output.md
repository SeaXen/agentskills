# Cindershift — Q3 DevRel Content Calendar

One page of decisions before the tables: the skill's interview is normally run one question at a time, but you asked for the quarter laid out in one pass. Below, every answer I would have interviewed for is either taken from what you locked, or stated as a named assumption in the next block. Correct any assumption and the affected sections re-plan, not the whole document.

## Quarter shape (decided, provisional)

The three candidate shapes, ranked as the skill ranks them:

- **Efficiency:** evergreen-compounding > launch-dominated > event-led
- **Value inside the quarter:** launch-dominated > event-led > evergreen-compounding
- **Value a year out:** evergreen-compounding > event-led > launch-dominated

**Recommendation: launch-anchored hybrid — a bounded launch cluster in W1-W5, an evergreen core, a bounded event spike W7-W10.** Not a pure shape, and the reasoning is the skill's own re-ranking rules:

- Pure launch-dominated is *cheaper than usual here* because the agency writes the headline launch post — but a GA that slips must not take the quarter with it, so anchor-bound capacity stays bounded and the evergreen slots carry no v5 dependency.
- Pure event-led is unjustified: one accepted talk is a bounded spike, not a quarter. The talk being *accepted* (not pending CFP) is what makes even the spike safe to plan around.
- Nothing is deleted outright — all three shapes are technically viable — but event-led is demoted, and the evergreen core gets hard dates and named reviewers exactly as if a launch depended on them, because calendar gravity will otherwise starve it.

**Q7 (one-off win vs. asset base), answered for you:** when week 8 goes wrong, the asset base yields. The un-dated benchmark post is the designated shock absorber — first piece cut or slipped. The launch and talk beats never yield.

## Assumptions substituted for the interview

| Question | Assumed answer | If wrong |
| --- | --- | --- |
| Team | Raoul (advocate, ~6 h/wk outside events), 1 writer (~12 h/wk), 1 engineer reviewer ("E", 4 h/wk), support lead ("S", cheap reviewer), agency (external) | Capacity model and slot count re-scale |
| Funding driver | Developer adoption, existing-user enablement second | Mix ratios re-derive |
| Audiences | Individual devs adopting solo + platform teams introducing it at work | Audience split changes |
| Judgment date | Quarter judged at its end — no board date mid-quarter | Promotes launch-dominated |
| Last quarter | No numbers given — skill baselines used as stand-ins | Replace all throughput figures |
| Off-limits | v5 embargo until W5; benchmark compares **architectures, not named vendors** | ⚠️ Confirm the second half — it shapes the benchmark post |

## Section 1 — Anchors

Anchors are consumed capacity, not opportunities.

| Week | Anchor | Class | Owner | Consumes |
| --- | --- | --- | --- | --- |
| W2 | Agency starts | external capacity | writer (internal owner) | briefs, outline lock, 2 review rounds × 2 pieces |
| ~W4 | Office hours #1 (last Thursday) | community | Raoul | promo, session, digest |
| **W5** | **v5 GA** | launch | product/eng | launch post (agency), release notes, migration guide, reply load |
| ~W8 | Office hours #2 | community | Raoul | promo, session, digest |
| **W9** | **ObserveCon (talk accepted)** | conference | Raoul | prep W7-W8, travel, companion post, recording follow-up |
| ~W13 | Office hours #3 | community | Raoul | promo, session, digest → Q4 |

- **Freeze: W5** — launch week, no unrelated publishing. W9 ships only the talk companion.
- ⚠️ Confirm office-hours weeks against the real calendar. If session #2 lands in talk week (W9) instead of W8, the writer hosts; Raoul attends from the venue if possible. Decide at the W7 check-in.
- The agency's measured latency in the one published case study is 8-9 weeks conception-to-publication. Brief was last week (~W0), live W5 — **~5 weeks, under the measured figure even though the brief work is done.** This is the plan's largest single risk; the two agency gates below exist because of it.

## Section 2 — Mix ratios

Percentages of slots (hours hide that one talk costs six blog posts). 12 committed + 3 slack = 15.

| Axis | Target | Rationale |
| --- | --- | --- |
| Surface | docs 40%, blog 30%, changelog 10%, community 10%, video+talk 10% | Adoption driver puts docs first; docs also carry the launch's enablement weight |
| Pillar | enablement 50%, advocacy 25%, marketing 25% | v5 migration + post-launch debt |
| Stage | discover 25%, try 15%, adopt 50%, contribute 10% | Existing users must survive v5 while new ones arrive |
| Shelf life | evergreen 60%, timely 40% | Launch + accepted talk; timely share is the accepted trade-off of this shape |
| Audience | individual 60%, platform/approver 40% | Approver audience is thin (see cuts) — first Q4 slot is theirs |

**Announcement cap: 3 slots** (launch post, release notes, benchmark). At cap, deliberately.

## Section 3 — Capacity model (in passes, not drafting hours)

- **Writer:** ~1 substantial piece per 2 weeks + small pieces. From W2, ~2-3 h/wk goes to agency management — briefs, outline, two review rounds per piece. The agency adds writer capacity only net of this tax; it does **not** add reviewer capacity.
- **Raoul:** 6 h/wk; fully absorbed W7-W9 by the talk; hosts office hours.
- **E — the binding constraint.** 4 h/wk, max ~2 review-heavy pieces per month. Heavy reviews land: agency draft (W3), migration guide (W3-W4) → month 1 full; benchmark methodology + draft (W9, W11) → month 3 full. Month 2 has **no** heavy E reviews by design — that is when the benchmark harness runs.
- **Benchmark harness:** working code that must run on GA bits — needs real engineering project time W6-W8, *outside* the 4 h/wk review budget. If that time is not granted, the benchmark is cut (kill rule below).
- **Slack (3 slots, named):** W3 — held for agency round-trips, default use is advancing the deferred approver page; W8 — advocate absorbed by talk; W11 — reactive room while E reviews the benchmark draft.
- **Compliance:** launch post carries product/legal veto in W4-W5. Pre-book it now; a veto exercised late is how outsourced launch pieces die.

**Decision gates:**
- **G1 — end W2:** agency outline for the launch post locked, E and product review booked. Else escalate that week.
- **G2 — end W3:** launch-post draft ready for review. Else in-house takeover: writer rewrites from agency research in W4 (migration guide is reviewed by then). The post goes live W5 regardless — that date is locked.
- **G3 — W9:** benchmark harness reproducible on GA bits. Else the benchmark slips to Q4 whole. It is the shock absorber; nothing else moves for it.

## Section 4 — Slot table

| Week | Working title | Surface | Pillar | Stage | Shelf | Anchor | Owner | Reviewer | Evidence / hypothesis |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W1 | Agent CPU/memory overhead: tuning page | docs | enablement | adopt | evergreen | — | writer | S | ⚠️ placeholder: recurring agent-resource tickets — pull real count before W1 |
| W2 | v5 launch post — agency outline lock (prep, not published; **gate G1**) | blog | marketing | discover | — | agency start | writer (owns agency) | E + product | 8-9 wk measured agency latency vs ~5 wk available → gates |
| W3 | *slack* — agency round-trips; default use: draft approver security page for Q4 | — | — | — | — | — | — | — | — |
| W4 | v4→v5 migration guide: what breaks and how to move | docs | enablement | adopt | evergreen | v5 GA | writer | E | ⚠️ placeholder: RC-program upgrade failures — pull count |
| W4 | Office hours #1 (~last Thu): v5 RC Q&A | community | community | contribute | timely | office hours | Raoul | — | standing ritual |
| W5 | **v5 launch post** (**gate G2** was end W3) | blog | marketing | discover | timely | v5 GA | agency / writer | E + product | agency piece #1; canonical v5 URL |
| W5 | v5.0 release notes | changelog | enablement | adopt | timely | v5 GA | E | writer | release |
| W6 | Top v5 upgrade errors (post-launch triage) | docs | enablement | adopt | evergreen | v5 GA follow-up | writer | S | W5 launch-week tickets, live count |
| W6 | Office hours #1 digest | community | community | try | evergreen | office hours | writer | Raoul | questions asked ≥3× feed Q4 pages |
| W7 | ObserveCon prep: demo + 2 dry runs (not published) | talk | advocacy | discover | — | ObserveCon | Raoul | writer | talk accepted; E runs benchmark harness W6-W8 |
| W8 | *slack* — advocate in final prep; office hours #2 (~last Thu) stands | — | — | — | — | — | — | — | host falls back to writer on collision |
| W9 | Talk companion post (canonical ObserveCon URL) | blog | advocacy | discover | timely | ObserveCon | Raoul | writer | lands talk week |
| W10 | Recording write-up + 3 clips + office hours #2 digest | video + community | advocacy | discover | timely + evergreen | ObserveCon | Raoul / writer | writer | follow-up window |
| W11 | *slack* — benchmark draft in E review; reactive room | — | — | — | — | — | — | — | — |
| W12 | Benchmark: v5 agent overhead vs sidecar / daemon-set setups | blog | marketing | adopt | evergreen | none, by design | agency / writer | E | **Bet:** platform teams choosing collector architecture search for this comparison and nobody credible publishes reproducible numbers — architecture-level, no named vendors |
| W13 | Quickstart cold-run refresh on v5 + office hours #3 (~last Thu) | docs + community | enablement / community | try | evergreen | v5 GA | writer / Raoul | E | quickstart drifts at every major; cold-run on clean machine |

**Repurposing trees** (every derivative is a slot above; one canonical URL per topic):

- **v5 GA:** launch post → migration guide (canonical for upgrade) → top-errors page (canonical for error strings) → quickstart refresh. Release notes link the guide, never duplicate it.
- **ObserveCon:** talk → companion post (canonical) → recording → 3 clips → a Q4 troubleshooting page mined from audience questions.
- **Benchmark:** post (canonical) → methodology section reusable as a docs page → OH #3 demo of the harness.

## Section 5 — Review ritual, kill rules, metrics

Monthly, 30 minutes, the Friday after each office-hours session (W4, W8, W13) — the sessions already gather the material. Three questions: shipped versus slotted; mix drift per axis; which pieces earned a follow-up.

- **Kill:** a piece whose anchor has passed, or re-drafted twice without converging, is cut out loud. Benchmark dies at G3 if the harness is not reproducible.
- **Defer:** one deferral maximum, then cut. The benchmark is the designated first sacrifice whenever W6-W8 overruns.
- **Metrics:** publish rate ≥ 80% (published ÷ slotted); mix drift; anchor coverage (share of anchors with both prep and follow-up — target 100%); lead time from "ready for review" to published, which is where E's bottleneck will show first.

## Validation result

| Threshold | Result |
| --- | --- |
| Every slot owned + named reviewer | ✅ 12/12 (ritual office-hours sessions exempt — standing anchor) |
| Surface / pillar / stage / shelf on every slot | ✅ |
| Evidence per demand slot, hypothesis per bet | ⚠️ structure ✅, but two evidence cells are named placeholders — pull real ticket counts before W1 or those slots are guesses |
| Committed ≤ 80% of capacity | ✅ 12 of 15 |
| Every anchor has prep + follow-up | ✅ v5: outline W2 + guide W4 → top-errors W6; talk: prep W7-W8 → companion W9 + recording W10; office hours: promo → digest each |
| ≥ 3 surfaces, ≥ 2 journey stages | ✅ 6 surfaces, 4 stages |
| Evergreen majority | ✅ 6-7 of 10 content slots (~60%), the accepted trade-off of this shape |
| Announcements under cap | 🟠 at cap: 3 of 12 (launch post, release notes, benchmark) |

**What was cut, and why (so it stays cut):**

1. **Approver security/data-flow page (was W3)** — E reviews the agency draft and the migration guide in the same fortnight. First slot of Q4.
2. **Benchmark at launch week** — needs GA bits to exist and E is saturated through W5. W12 is the earliest slot where both hold; being un-dated, it costs nothing to place late.
3. **"v5 is coming" teaser post** — announcement cap. The GA is close enough that a teaser splits the attention week.
4. **Second Raoul byline pre-launch** — talk prep owns him from W7; before that, office hours do.
5. **Office hours #3 digest** — folds into Q4's first slot rather than competing with quarter close.

The plan's two watch-items, ranked: the **agency timeline** (gates G1/G2 exist for it — a missed G2 triggers in-house takeover with zero schedule slack), and **E's month-1 load** (two heavy reviews plus launch-week support is the tightest fortnight in the plan; if it breaks, the migration guide moves to W5's launch cluster before anything else moves).