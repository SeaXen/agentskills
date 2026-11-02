Next action: run the afternoon-1 query below — it's the one thing that unblocks the rest.

# Developer segment map — Nimbus Relay, H1 roadmap decision

## Cut

**Dimensions: primary client language × deployment runtime** (both technographic — signup data already carries both, no new instrumentation needed).

Why this pair: your product must sit *inside* a runtime to be used at all (a message-queue client is a library someone imports into a Go service, a Lambda, a Java monolith). That makes technographic the dominant family here — it decides which SDK ships, which docs track gets written, which integration shape (sidecar, operator, extension) gets built. That is exactly the question the SDK team is asking.

**Rejected — workload/job-to-be-done cut** (what they're actually building on top of the queue: event sourcing, task queue, log pipeline, IoT ingest). This is normally the highest-leverage cut for a product that solves different problems per domain, but it requires ticket coding or interviews you don't have and can't get in 9 days. Deleted outright, not demoted — don't let it get re-proposed next quarter as if it were free.

**Rejected — seniority.** A junior and a staff engineer both integrating a Go client onto Kubernetes need the same SDK and the same docs.

**Not a separate cut — buying mode.** Self-serve-$29 vs enterprise-contract is real and matters, but you don't have enough evidence to make it its own 3-5-row grid (200 notes, unclustered, not designed for this question). Instead it gets folded in as the **decision unit inside each ecosystem segment** (step 4) — cheaper, and it answers "who signs" without needing a second full grid.

## The 2-afternoon runbook

**Afternoon 1 — size the grid (signup data, ~1-2 hrs):**
1. Pull last 24 months of signups, grouped by (`primary_language`, `runtime`). Use whatever's actually recorded per row — don't collapse "runtime" categories yet, collapse *after* you see the distribution.
2. Weight by activation or paid conversion, not raw signup count — raw signups overweight tire-kickers. If you only have signup volume, say so and mark the row `estimated`, not `measured`.
3. Keep only cells with a substantial share (skip anything under ~3-5%) — that's your candidate segment list, capped at 5.

**Afternoon 2 — decision unit per cell (sales notes, ~1-2 hrs):**
4. Sample ~30-40 of the 200 notes, spread across your biggest 3-4 language/runtime cells if the notes mention stack.
5. For each note, tag three things: who first evaluated, who else had to say yes, self-serve or contract. (This is the skill's exact question set for revealing a decision unit — five real deals beat an assumed org chart.)
6. Where a cell shows both self-serve-only deals and contract deals with an approver, that's your split signal (step below).

That's the whole research budget. Everything past this is filling in the template below with what you find.

## Segments (template — replace size/decision-unit cells with your query output)

| Segment | Definition | Size + confidence | Decision unit | Needs | Evidence |
|---|---|---|---|---|---|
| [Top language] × containers/K8s | Backend teams running the client inside containerized services | pending — from step 1 | pending — from step 5 | idiomatic client, sane retry/backoff defaults, quickstart | signup telemetry — measured once pulled |
| [Top language] × serverless | Teams calling the queue from functions (Lambda/Cloud Functions) | pending | pending | cold-start-light client, no persistent connection pooling assumption | signup telemetry |
| [2nd language] × VM/on-prem, contract-heavy | Platform teams running at scale, longer sales cycles | pending | likely: user evaluates, platform lead approves, someone signs | throughput guarantees, self-host or VPC-peering story, SLA doc | sales notes |
| [3rd cell if it clears ~5%] | — | pending | pending | — | — |

Cap at 5 rows. If a language/runtime cell shows up in signups but never in a closed sales note, that's a real finding — it means the segment self-serves and never needs anything beyond the SDK.

**Split rule:** if one language×runtime cell contains both pure self-serve deals (dev = buyer, card payment) and contract deals with an approver, split it into two rows — they need different artefacts (quickstart + free tier vs SLA doc + reference architecture), and folding them into one row hides that.

## Scoring weights (set now, apply once sizes land)

Driver = SDK roadmap investment, so weight the denominator hard:

- **Effort** (SDK/runtime-integration build cost) — heaviest weight. This is literally what the SDK team is trading against.
- **Size** and **Value** — high. A cell needs enough volume, or enough contract weight, to justify a new SDK surface.
- **Compounding** — high. A segment where the same SDK work also unlocks the enterprise cell (e.g., the language your biggest self-serve base already uses is also the language enterprise deals ask for) outranks one where you'd build twice.
- **Reachability**, **Fit**, **Competitive position** — medium. Useful for the secondary GTM decision, not the primary build decision.

Rank by value ÷ effort, not sum. Say the division out loud when you present it — "cell X wins by volume, cell Y wins on the ratio because it needs no new integration shape" is the sentence that survives the roadmap meeting.

**Check before finalizing:** if the largest, highest-value cell is also the highest-effort one (new runtime integration, e.g., a K8s operator you don't have), don't let the ratio auto-kill it. Promote it anyway if no cheaper cell carries real contract revenue — that's the exact override condition this method calls out, and it's common in infra tooling.

## Primary / Secondary / Anti-segment (decision rule — apply after step 1-2 above)

- **Primary:** the cell with the largest weighted signup share that also shows nonzero presence in closed enterprise deals. That overlap is what makes one SDK investment pay both self-serve and enterprise at once — the compounding case.
- **Secondary:** the next-largest cell, served only by what the primary already funds (same client library, no dedicated new integration).
- **Anti-segment, provisional:** any language/runtime cell under ~3-5% share with zero appearance in sales notes. Name it explicitly in the roadmap doc — "we are not building a [language] SDK this half, revisit if its signup share crosses X%" — so it stops being re-argued every planning cycle. Also route trial signups with zero send volume here unless you can name a non-revenue reason to serve them (talent brand, future buyers) — undirected free usage quietly eats support capacity.

## Hypotheses

Until the two-afternoon pull runs, every row above is a hypothesis (this is inherent — you've never surveyed or interviewed, so nothing clears the evidence floor yet). The test that clears each: the signup query (quantitative floor) plus 5+ sales notes per cell showing a consistent decision pattern (qualitative floor). Don't present any row as "measured" to the roadmap meeting until both have run.

## Implications

- **Build:** SDK/runtime work for the primary cell only, this horizon.
- **Stop:** any in-flight SDK work for a cell that lands in the anti-segment — say which, by name, in the roadmap doc.
- **Don't build yet:** a workload-based reference architecture — you have no evidence for which workload dominates. If the team keeps arguing "but what are they actually building," that argument is the signal to fund a cheap workload test next quarter (10 support tickets read end to end, tagged), not to guess now.

## Review

Re-read this map at the next planning cycle. Force an early re-read if: pricing/packaging changes, a new runtime gets a launch commitment, or the primary cell's signup share moves more than ~10 points in either direction.

---
Next: run step 1 of the runbook (group signups by language × runtime, weighted by activation) — that single query decides which row becomes primary.