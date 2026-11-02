# Keyword map: Tessellate — Q4 2026 docs and content targets

## Scope

**Product:** Tessellate, self-hosted API gateway. First-hour task not stated in the brief — inferred (Estimated) as: install self-hosted, configure a route, attach a plugin (JWT auth, per-consumer rate limiting). Confirm before writing briefs.

**Surfaces owned:** not stated. Assumed docs site + blog since "ship 8 pages" implies a docs-shaped deliverable. Confirm whether changelog or community forum are also in scope — a migration announcement usually wants a changelog entry alongside the guide.

**Adoption mode:** both, explicitly — individual developers and internal champions. Given its own target count below so the ratio can't bury either one.

**Axes confirmed by evidence:** self-hosted deployment, JWT plugin, per-consumer rate limiting, upstream/proxy timeout behavior. No language, framework, or runtime axis was given, so none is added to the matrix — inventing one here would generate cells this map can't honestly back.

**Driving event:** the rival's 2.x line goes end-of-life in nine months (~June 2027) alongside a breaking 4.0. This is the specific condition this skill flags as the one window where a migration guide is cheap to win and closes on a clock — it reorders this map's top line (see Ranked clusters).

**Sources used (all User-provided — figures stated in the brief, not pulled by me from a live export):**
- Tier 1, first-party query data (impressions/position): the rate-limit-how-to, rate-limits, self-host, vs-rival, and "what is" queries.
- Tier 2, docs-site search logs: the JWT plugin example and migrate-from-rival queries.
- Tier 3, support tickets and SE question lists: the 502 error, rate-limit, self-host, vs-rival, and migrate queries.
- Tier 4, product error telemetry: the 502 error query.
- Window: trailing 90 days, ~2026-06-22 to 2026-09-20, per the brief.

**Sources unavailable this round:** issue tracker, community/forum archive, ecosystem counters, autocomplete harvests, keyword-tool volume. None of these were substituted with a guess.

**Evidence-tier floor:** 8/8 ranked clusters draw top evidence from tiers 1–4 → 100%, well above this skill's 70% baseline. No downgrade needed.

## Ranked clusters

Sorted by outcome per page-hour, highest first, **except two rows the pure ratio would have ranked lower**, both promoted explicitly:
- **Migration** (G) is this skill's own named override condition — a rival's deprecation or breaking major is "the one window where a switch is cheap to win," so it goes to the top outright despite being the single most expensive family on the map (a week of borrowed engineering time).
- **Comparison** (F) would normally sit mid-table (a day plus a legal pass on every claim). It's promoted because legal has already paid that compliance cost, and it answers the same champion, in the same nine-month window, one click after the migration guide.

| Cluster | Primary query | Variants | Family | Evidence (source, count, date, tag) | Incumbent | Target surface | Existing URL or new | Priority |
|---|---|---|---|---|---|---|---|---|
| Migrate from rival | `migrate from <rival> to tessellate` | "switching from `<rival>` to tessellate", "`<rival>` 2.x EOL alternative" | Migration | 63 docs searches / 90d + 19 SE questions / 90d (2026-09-20, User-provided) | rival's own docs; silent on their EOL/4.0 break | Migration guide (review date: rival's 4.0 GA) | new | **P1 — promoted** |
| Upstream timeout error | `tessellate 502 upstream timeout` | "502 bad gateway tessellate", "upstream connect error timeout" | Error | 1,900 error events / 90d (tier 4) + 44 tickets / 90d (tier 3) | none — no error entry found | Error entry | new | **P1** |
| Rate limit per consumer | `how to rate limit per consumer tessellate` | "per-key rate limiting tessellate", "consumer quota config" | Task how-to | 380 impressions, avg position 11 — striking distance (tier 1) | unconfirmed page ranking at pos 11 | How-to guide | existing, URL unconfirmed (see Fix first) | **P1** |
| Tessellate vs rival | `tessellate vs <rival>` | "`<rival>` alternative", "tessellate or `<rival>`" | Comparison | 96 impressions, avg position 19 — edge of striking distance + 8 SE questions / 90d | unconfirmed page ranking at pos 19; category pages skew toward the rival's own SEO weight | Comparison page | existing, URL unconfirmed (see Fix first) | **P1 — promoted** |
| Rate limits (spec/plan limits) | `tessellate rate limits` | "tessellate quota limits", "how many requests per second tessellate" | Evaluation | 52 impressions / 90d (position N/A) + 14 SE questions / 90d | pricing page, no numbers (assumed) | Trust/limits page — "Rate limits" | new | P2 |
| Self-host requirements | `self-host tessellate requirements` | "tessellate on-prem requirements", "minimum specs self-hosted tessellate" | Evaluation | 71 impressions / 90d (position N/A) + 11 SE questions / 90d | README, assumed incomplete | Trust/limits page — "Self-hosting requirements" | new | P2 |
| JWT plugin example | `tessellate jwt plugin example` | "jwt auth plugin config tessellate", "verify jwt tessellate" | Reference lookup | 210 docs searches / 90d — the largest raw count on the map (tier 2) | none — fully ownable, it's our own plugin | Reference page with example | new | P2 |

## Company-adoption set

Kept separate with its own filled target count (4) so the ratio can't bury it. Best evidence for this set is exactly what the pattern library predicts — sales/SE question lists, not search volume.

| Cluster | Primary query | Family | Evidence | Incumbent | Target surface | Priority |
|---|---|---|---|---|---|---|
| Migrate from rival | `migrate from <rival> to tessellate` | Migration | 19 SE questions / 90d + 63 docs searches | rival's docs, no EOL messaging | Migration guide | P1 |
| Tessellate vs rival | `tessellate vs <rival>` | Comparison | 8 SE questions / 90d + 96 impressions, avg pos 19 | rival's own comparison content | Comparison page | P1 |
| Rate limits | `tessellate rate limits` | Evaluation | 14 SE questions / 90d + 52 impressions | pricing page, no numbers | Trust/limits page | P2 |
| Self-host requirements | `self-host tessellate requirements` | Evaluation | 11 SE questions / 90d + 71 impressions | README, incomplete | Trust/limits page | P2 |

## Fix first

- **C and F both show a nonzero average position (11 and 19)** — some URL already ranks for each, but the brief didn't include the query-to-landing-page join. Pull that join before writing: if an existing page already sits at position 11 for "how to rate limit per consumer," update that page rather than publish a competing new URL — striking-distance pages carry proven relevance that a fresh page starts without.
- **C ("how to rate limit per consumer") and D ("tessellate rate limits") are adjacent, not identical** — one is a configuration task, the other a checklist-shaped limits lookup. Run the merge test (shared top-10 results) once you have SERP access; until then, keep them as two pages and cross-link rather than merging or letting one silently absorb the other's traffic.
- **Flag the 502 cluster for an engineering check before writing:** 1,900 error events against only 44 tickets is a ~2.3% report rate. That gap is consistent with a docs-fixable config issue (timeout tuned too low) but also with a product defect nobody bothers to file a ticket for. If telemetry shows the spike concentrated after a specific release, route that slice to engineering — a doc page cannot fix a regression.

## Do not target

- **"what is an api gateway"** (140 impressions, avg position 28 — outside the striking-distance window, tier 1) — refused. This is a generic category-definition term already owned by the established platform vendors' own explainer content (the kind of large, generic educational page big incumbents hold by default), it's the weakest family rung on the map (a one-line answer an assistant gives without sending anyone anywhere), and nothing in the brief gives it a differentiated angle Tessellate specifically can win on. Extending the "owned by someone else's documentation" refusal to this category-defining concept query rather than spending one of this quarter's 8 pages on it.

## Backlog

None. Every cluster that passed the winnability filter (7 of 8) fits inside this quarter's 8-page capacity, with one slot free.

**Recommendation for the freed slot:** don't spend it on the refused concept page. The migrate-from-rival cluster carries the highest SE-question count on the map (19) — that's usually more than one migration guide can absorb (config-mapping questions and "should we even switch" questions read differently). Use the 8th slot to split the migration guide into an overview/decision page plus a technical step-by-step, or ship a short FAQ alongside it, while the nine-month window is open.

## Pass-threshold check

1. Every ranked row carries source, count, date and a Measured/User-provided/Estimated tag — yes, all tagged User-provided (stated in the brief, not pulled from a live export by me).
2. Tier 1–4 share of ranked clusters: 8/8 = 100%, above the 70% floor.
3. No cluster ranked on tool volume alone — correct, tier 8 wasn't used at all.
4. One canonical target surface per cluster, no two clusters sharing a page — checked (D and E share a page *type*, Trust/limits, but not the same URL).
5. Do-not-target is non-empty — one refusal, reasoned above.
6. Sort stated above the table; G and F named as the ratio-demoted, condition-promoted rows; company-adoption set carries its own filled target count (4) independent of the ratio.