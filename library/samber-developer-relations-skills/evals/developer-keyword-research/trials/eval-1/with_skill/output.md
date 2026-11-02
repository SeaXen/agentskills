# Keyword map: Hookline — webhook delivery API

## Scope

**Product:** Hookline, webhook delivery API, ~900 paying teams.

**Axes** (inferred from the seven terms handed over — confirm before I expand further): HMAC signature verification, rate limiting (429), retry/backoff, manual replay of failed deliveries. No language/framework/SDK axis was stated; ask before generating `<task> in <language>` cells.

**Adoption mode:** both. Individual adoption dominates the three branded error queries (a developer mid-integration, pasting a string). Company adoption shows up once in the seven ("webhook delivery service" — a build-vs-buy evaluation, typed by a champion, not the eventual signer).

**Owned surfaces:** docs site (has search logs), support desk (Zendesk). Blog/changelog existence unconfirmed — ask.

**Sources named as available:** Search Console (tier 1), Zendesk export, 12 months (tier 3), docs-site search logs, 6 months (tier 2).

**Sources not exercised in this pass:** I was not handed the actual exports or a live API connection for any of the three — this session has no Search Console, Zendesk, or docs-search connector wired up, and no CSVs were attached. Every tier 1–3 cell below is `N/A — pull pending`, not a guess. Tier 4 (error telemetry), tier 5 (Q&A), tier 6 (ecosystem) are not mentioned as available and are marked unavailable.

**Tier 8 (keyword tool):** the seven rows supplied by the growth lead. No pull date given — get one before trusting the counts (Ahrefs/Semrush-class tools reindex monthly, and reported dates matter for the version-rot check).

Given the floor below fails as-is, treat this as a **corrected screening pass**, not a finished map: it fixes the growth lead's ranking logic and hands back the exact pulls needed to promote it to a fully evidenced one.

## Ranked clusters

Sorted by outcome per page-hour, **not** by tool volume — that's the actual defect in the growth lead's plan, not a stylistic choice. The three branded queries were dropped because a vendor tool rounds unique, product-specific strings to 0; that's a statement about the tool's index (Ahrefs' own numbers: ~93% of its database sits below 10 monthly searches, and Keyword Planner merges and rounds close variants), never a statement about whether a Hookline customer is stuck right now. Reversing that drop is the single highest-value move in this map.

| Cluster | Primary query | Variants (candidates — verify against docs search log) | Family | Evidence | Incumbent | Target surface | Existing URL or new | Priority |
|---|---|---|---|---|---|---|---|---|
| Signature verification failure | `hookline WEBHOOK_SIGNATURE_MISMATCH` | "hmac verification failed webhook", "webhook signature invalid hookline", "X-Hookline-Signature does not match" | Error string | Tier 8: 0/mo (tool, undated — index floor, not demand). Tiers 1–3: N/A, pull pending | None known — check if any existing Hookline page already ranks | Error entry | new (confirm no existing page first) | **P1** |
| Rate limit / 429 on delivery | `hookline 429 too many requests webhook` | "hookline rate limit error", "too many webhook deliveries 429" | Error string | Tier 8: 0/mo (same index-floor caveat). Tiers 1–3: N/A, pull pending | None known | Error entry (distinct from a rate-limits evaluation page — see intent-collision note below) | new | **P1** |
| Manual replay of a failed delivery | `hookline replay failed webhook` | "resend failed webhook hookline", "how to redeliver webhook hookline" | Task how-to / reference (documents an existing dashboard/API action) | Tier 8: 0/mo. Tiers 1–3: N/A, pull pending | None known | Reference/how-to page for the replay feature | new | **P1** |
| Retry/backoff behavior | `webhook retry best practices` | "webhook exponential backoff", "webhook retry schedule" | Task how-to | Tier 8: 390/mo, KD 34 (tool, undated) | Generic engineering blog posts, competitor devrel content — beatable on completeness (Hookline's actual backoff schedule, jitter, max-attempt count) | How-to guide, documents Hookline's real retry config | new (or update if a retries page already exists) | **P2** |
| Webhook testing capability | `webhook testing tool` | — | Reference/tool page **if** Hookline ships a real testing feature (local tunnel, event simulator, sandbox replay); otherwise refuse | Tier 8: 1,300/mo, KD 55 | ngrok, webhook.site, RequestBin, Beeceptor — high-authority incumbents, hard to out-rank on the generic term | Reference page for the specific feature, narrow long-tail angle only | new, **conditional** — confirm feature exists first | **P3, conditional** |
| Build-vs-buy category term | `webhook delivery service` | — | Evaluation (company adoption) | Tier 8: 2,400/mo, KD 62 | Svix, Hookdeck, Convoy — direct competitors already running devrel-grade category pages | Evaluation/trust page, attacked from the flank (see Company-adoption set) rather than head-on | new | **P2, demoted** — see note |
| Definitional term | `what is a webhook` | — | Concept | Tier 8: 18,000/mo, KD 71 | MDN-adjacent explainers, Zapier, Svix/Hookdeck glossary pages — actively maintained, high-authority, evergreen | — | — | **Do not target as a flagship page** |

**High-value cluster the ratio demoted, and what promotes it:** `webhook delivery service` carries the highest legitimate business proximity of the four generic terms — it's closest to Hookline's actual product — but KD 62 against three funded direct competitors makes a head-on category page an expensive, low-odds bet at 900 paying teams. It's demoted to P2 under the ratio. Promote it to P1 only if a real SERP check shows a stale or thin incumbent result (run the winnability check before committing budget), or fold it into the company-adoption evaluation set below, which converts the same champion more cheaply.

## Company-adoption set

| Cluster | Primary query | Family | Evidence | Incumbent | Target surface | Priority |
|---|---|---|---|---|---|---|
| Build-vs-buy category term | `webhook delivery service` | Evaluation | Tier 8: 2,400/mo, KD 62 | Svix, Hookdeck, Convoy | Evaluation/trust page (rate limits, retries, delivery guarantees stated in numbers) | **P1 for this set** |

This set has exactly one entry because only one of the seven supplied keywords is company-adoption-shaped. That's a gap, not a finding — evaluation-family demand (rate limits, self-hosting, SOC 2, SLA, data residency) rarely surfaces in public search or docs logs at all; it lives in sales and solution-engineer question lists, which weren't among the three sources described. **Action: ask whoever runs Hookline sales calls what a prospect asks before signing** — that's the actual tier for this family, and it's the fastest, cheapest evidence pull available (an afternoon, not an export).

## Fix first

Not run — requires the actual Search Console pull, which I don't have in this session. Before writing anything new, run the striking-distance check yourself:

1. Export the Search Console query report for the full available window, row limit raised to max (25,000 if using the API directly).
2. Cut to average position 5–20 client-side (position isn't filterable server-side).
3. Filter for `signature`, `hmac`, `429`, `rate limit`, `replay`, `resend`, `retry`, `backoff`.
4. Join each surviving query to its landing page.

Any hit here is an update-existing-page case, not a new-page case, and jumps to P1 regardless of where it lands above — a page already at position 12 for "hookline signature verification" outranks writing from zero every time.

## Do not target

- **`what is a webhook`** — owned by incumbents with years of accumulated authority on a term that gets no more specific with your product; per Stack Overflow's 2025 survey, 84% of developers now use or plan to use AI tools for exactly this kind of lookup, and JetBrains' 2025 survey ranks "searching for information" as the #2 task developers delegate to AI — this is precisely the one-line-answer query an assistant now answers without sending anyone to a page. Not winnable at 900-team scale; at most a short glossary stub for citability, never the page the growth lead is picturing spending a KD-71 budget on.
- **`webhook testing tool`** — refuse *unless* Hookline ships a real testing feature. If the growth lead's ask is "rank for this because it's high volume" and there's no actual capability behind it, this is the "real fix is a product change, not a page" refusal category — writing it anyway produces a page promising something that doesn't exist.

## Backlog

Not populated — no shipping-capacity figure (pages/quarter) was given. Provide that number and I'll cut this list to what two quarters of real capacity covers and date-stamp the rest.

## Pass threshold

1. ✅ Every ranked cluster carries at least one dated, sourced, labeled evidence item — tier 8 for all seven (label: Estimated, tool-vendor figures; get the missing pull date from the growth lead).
2. ❌ **70% tier 1–4 floor: fails.** 0 of 7 clusters currently draw top evidence from tiers 1–4 — none of the three named sources were actually pulled in this pass. This map is a corrected ranking logic, not yet a fully evidenced one. Lower this floor explicitly if you want to ship on tier-8-plus-domain-reasoning alone; I'd instead run the four pulls above first (an afternoon of work) and re-rank.
3. ✅ No cluster is ranked on tool volume alone — the three zero-volume branded errors outrank the 18,000/mo definitional term on family and intent, not the reverse.
4. ✅ One canonical surface per cluster — the 429 error entry and the rate-limits evaluation page are kept deliberately separate (same root cause, two different searchers: one mid-failure, one pre-purchase).
5. ✅ Do-not-target list is non-empty (two refusals above).
6. ✅ Sort is stated, the demoted high-value cluster is named with its promotion condition, and the company-adoption set has its own (thin, flagged) target count rather than inheriting the ratio's order.

**Bottom line: keep the three branded error pages, don't drop them — they're the cheapest, highest-intent pages on this list and the tool simply can't see them. Build `webhook retry best practices` from the growth lead's four. Treat `webhook delivery service` and `webhook testing tool` as conditional, not automatic. Drop `what is a webhook` as a flagship target entirely.** Run the four data pulls above before locking a final priority order — that's what moves this from a screening pass to a map that clears its own threshold.