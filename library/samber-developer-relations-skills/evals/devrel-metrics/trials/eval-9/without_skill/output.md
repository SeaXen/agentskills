# Saltmarsh Data — DevRel Measurement Framework v1

## 1. Design rules

These five invariants hold the whole thing together. Every later decision derives from them.

1. **One event stream, two views.** The AAARRRP panel and the drop-off map read the same instrumented events. Never build separate tracking for each — that is how unit mismatches get in.
2. **Stages are events, not feelings.** A developer is in a stage when a specific, machine-observable event has fired. Definitions below are the contract; rename events to match the product, never the reverse.
3. **Unit integrity.** Every rate's numerator and denominator share the same unit, same cohort, same window. "Talk attendees who activated within 14 days ÷ talk attendees" — never "activations ÷ attendees" across mismatched periods.
4. **No percentages on small bases.** Report the absolute n alongside every rate. No trend claim when n < 30.
5. **Kill rule.** Every metric names the decision it informs and the person who would act on it. Anything nobody would act on gets cut at the quarterly review. Activity counts (posts shipped, events held) are inputs, never goals.

## 2. Wiring the two charter goals

The charter goals are the two things the team is funded to move. Each gets one **primary** (an outcome metric from the stage model) and one **input** (something the team controls weekly). Fill in your exact charter wording; the worked defaults below show the pattern.

| Slot | Charter goal (your wording) | Primary metric | Input metric | Lead |
|---|---|---|---|---|
| A | *e.g. "1,000 net-new activated developers by Dec 31"* | Cumulative activated developers (cohort-verified) | Activation rate (Acq→Act) | Docs |
| B | *e.g. "$2M DevRel-influenced pipeline at ≥15% win rate"* | Influenced pipeline $ (attribution rule, §9) | ICP-account touch coverage | Advocate |

Rules: primaries must be stage outcomes (§3), never activity counts. Inputs must be movable by one person in one week. If a goal's primary isn't a stage outcome, the goal is either miswritten or not a DevRel goal — surface that now, not in Q3.

## 3. View 1 — AAARRRP stage model

| Stage | Developer has... | Entry event (the definition) | Primary metric | Owner |
|---|---|---|---|---|
| **Awareness** | Learned Saltmarsh exists | Reached via a channel we tag | Unique developers reached, by channel | Advocate |
| **Acquisition** | Made first countable contact | First touch on our property (`content_viewed`) | New developers / week | Docs |
| **Activation** | Experienced first value | `first_success` — first successful query / pipeline / API 200 in sandbox or own data | Activation rate; median TTFV | Docs |
| **Retention** | Repeated use | Active ≥3 of 4 consecutive weeks post-activation | W4 retention of activated cohort | Advocate |
| **Referral** | Told someone | `referral_action` — shared link, invited teammate, second seat | Referral rate of retained devs | Community |
| **Revenue** | Become a commercial contact | `commercial_signal` — trial, plan change, sales contact | Influenced pipeline $ | Advocate |
| **Participation** | Contributes back | Asks/answers in community, issue/PR, speaks, writes integration | Participation rate (90d) | Community |

Participation is a **loop, not a ladder top**: participants regenerate Awareness and are the cheapest Acquisition channel. The flywheel is the point — P feeds the first A.

Ownership is deliberate, one cluster per person, matching the three roles:

- **Docs** owns the front (Awareness→Acquisition→Activation). Activation *is* the docs product.
- **Advocate** owns the middle (Activation→Retention→Revenue influence).
- **Community** owns the loops (Referral + Participation).

Each person also owns instrumentation for their stage boundaries, so no boundary is orphaned.

## 4. View 2 — Journey drop-off map

Canonical path with instrumented checkpoints. Referral and Participation are annotated loops off the path, not forced into the line.

```
Awareness ─→ Acquisition ─→ Activation ─→ Retention ─→ Revenue
                                  │  ▲          │
                                  │  └──────────┤ Referral loop ↺ feeds Awareness
                                  └─────────────┤ Participation loop ↺ feeds Awareness
```

**Checkpoints (rename 3–5 to your real product moments):**

| # | Checkpoint event | Gap owner |
|---|---|---|
| 1 | First touch (UTM-tagged) | Advocate |
| 2 | Quickstart opened | Docs |
| 3 | Environment step: sandbox created / SDK installed / API key created | Docs |
| 4 | `first_success` | Docs |
| 5 | Second session within 14 days | Advocate |
| 6 | Active 3-of-4 weeks | Advocate |
| 7 | Second seat / shared workspace | Community |
| 8 | `commercial_signal` | Advocate |

**The six tracked conversions** (adjacent-pair rates, cohort- and window-matched):

| Conversion | Read it as | Diagnostic question when it drops |
|---|---|---|
| 1→2 | Content findability | Are we discoverable for the problem we solve? |
| 2→3 | Intent capture | Does the quickstart look worth 10 minutes? |
| 3→4 | Time-to-first-value | Where in setup do developers stall or error out? |
| 4→5 | Value validation | Did "first success" actually feel like success? |
| 5→6 | Habit formation | Is there a recurring job needing us? |
| 6→8 | Commercial path | Do retained users ever hit a reason to pay? |

**Exit-event taxonomy** — every drop gets classified, because each class has a different fix owner:

| Exit class | Signature | Fix owner |
|---|---|---|
| Never-returned | No session 2 | Docs |
| Failed first value | Errors / abandonment mid-quickstart | Docs |
| Value-not-validated | Succeeded once, no return | Advocate |
| Tool-fit | Returned, usage decayed | Advocate |
| Chose competitor | Win/loss signal from community or sales | Advocate + Community |

**Diagnosis loop (the operating rhythm of this view):** for any conversion flagged red (baseline rule in §7), run one gap per week: classify exits → one fix hypothesis → one instrumented experiment → owner + review date. Prioritize gaps by absolute developer volume × proximity to Goal A/B — biggest leak nearest the money first.

## 5. The metric sheet

Thirteen rows. This is the whole dashboard; everything else lives in a monthly appendix.

| # | Metric | Unit / definition | Source | Owner | Cadence |
|---|---|---|---|---|---|
| 1 | New developers | Unique stitched devs, first touch | Product analytics | Docs | Weekly |
| 2 | Activation rate | `first_success` within 7d ÷ cohort acquisitions | Cohort table | Docs | Weekly |
| 3 | Median TTFV | First-touch → `first_success`, minutes | Product analytics | Docs | Weekly |
| 4 | W4 retention | Active 3-of-4 wks ÷ activated cohort | Cohort table | Advocate | Monthly |
| 5 | Docs-assisted activation % | Activations with docs-session in path | Warehouse join | Docs | Monthly |
| 6 | Event/content-assisted activation lift | Cohort activation w/ touch vs without | Cohort table | Advocate | Monthly |
| 7 | Influenced pipeline $ | Per §9 attribution rule | CRM + touch log | Advocate | Monthly |
| 8 | ICP touch coverage | % target accounts with ≥1 touch / quarter | Touch log | Advocate | Monthly |
| 9 | Referral rate | Retained devs with `referral_action` ÷ retained | Cohort table | Community | Monthly |
| 10 | Participation rate | Activated devs active in community ≤90d | Community platform | Community | Monthly |
| 11 | Community responsiveness | Median first-answer time | Community platform | Community | Weekly |
| 12 | Contributors | New + returning, issues/PRs/content | GitHub + log | Community | Monthly |
| 13 | Goal A + B primaries | Per §2 slots | — | Leads | Monthly vs pace |

Social followers, per-post engagement, event RSVP counts: monthly appendix only. They never enter the weekly room — nobody changes behavior on them.

## 6. Instrumentation

- **Event naming:** `<object>_<action>`, snake_case. One events glossary file in the repo is the single source of truth; the dashboard is generated from it, never hand-built.
- **Checkpoint events:** `content_viewed`, `docs_quickstart_opened`, `sandbox_created`, `first_success`, `session_started`, `team_invite_sent`, `referral_action`, `commercial_signal`, `community_join`, `community_post`, `contribution`.
- **Required properties on all:** anonymous ID, UTM/source, SDK language, docs version, elapsed-since-previous-checkpoint (this is what makes TTFV and drop-off timing computable, not just counts).
- **Identity stitching:** anonymous → known at `api_key_created` or community join. A "developer" is a stitched identity, deduped at the workspace member level.
- **UTM discipline:** every link the team ships anywhere carries UTMs. This is non-negotiable and free.
- **Plumbing:** events → warehouse (you are a data company; use your own stack) + one dashboard layer on top. Two queries power both views: the stage panel and the weekly cohort table (cohort of `first_success`, columns: size, W1–W4 active %, referral %, participation %, commercial n). No new tool sprawl.

## 7. Operating cadence

- **Weekly, 30 min, all three:** funnel deltas, then one drop-off gap through the diagnosis loop. 15 minutes dashboard, 15 minutes one gap.
- **Monthly:** cohort read, goal primaries vs. pace-to-target, attribution refresh.
- **Quarterly:** re-baseline, run the kill rule on every metric, re-state goal primaries if the charter moved.
- **Flags:** for the first quarter, flag any conversion moving >±20% relative MoM with n ≥ 30. After one quarter of baseline, set RAG thresholds from your own data. Do not adopt industry benchmark numbers without a verifiable primary source — most circulating figures ("median response time", "standard conversion") are folklore that nobody can source.

Upkeep budget: ~2h/person/week, including instrumentation maintenance. If it exceeds that, cut metrics, not effort — a 3-person team drowning in tracking is a dropped-retention metric waiting to happen.

## 8. Build plan — this week

| Day | Deliverable | Who |
|---|---|---|
| Mon | 2h, all three: lock stage definitions, the 6 conversions, events glossary v1 | All |
| Tue | Instrument checkpoint events in product + docs; UTM discipline live | Docs (lead) |
| Wed | Community + referral events; CRM touch-log fields for attribution | Community (lead) |
| Wed PM | Cohort table + both dashboard views built from the glossary | Advocate (lead) |
| Thu | Backfill 90 days where data exists; else start the baseline clock. Backfill gaps are marked as gaps — never estimated | All |
| Fri | First weekly review on real data; publish glossary v1 + dashboard links | All |

## 9. Attribution rule (pin this before the first report)

**Influenced** = opportunity with ≥1 logged DevRel touch (event attendance, docs-account session, community activity, OSS interaction) in the 365 days before opportunity creation, logged at touch time. Retroactive touches added after close don't count. **Sourced** = DevRel initiated the contact; tracked separately, never merged. Influenced-pipeline claims always carry the touch count and lookback window in the footnote.

---

The framework is deliberately complete at thirteen metrics: enough to see both views clearly, small enough that three people actually run it. Week one priority order if time runs short: the events glossary and checkpoints 3–5 — TTFV and the session-2 gap are where a data platform's developers live or die, and everything else can baseline a week later.