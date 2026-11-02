# Merge test results

Using the skill's shared-result bands (top-10 organic overlap):

| Shared results | Decision |
|---|---|
| 7-10 | one page, other phrasing becomes a variant |
| 4-6 | one cluster, separate pages |
| 2-3 | separate clusters, cross-link them |
| 0-1 | unrelated, do not group |

Applied to your four pairs:

**A) 'skiff websocket connection drops' / 'skiff socket disconnects randomly' — 8 shared → ONE PAGE.**
Same results already answer both. Merge into a single cluster, e.g. "WebSocket connection drops / disconnects unexpectedly." Family: Error/symptom (mid-failure query — highest-intent moment on the map). Target surface: one troubleshooting/error entry. Keep "socket disconnects randomly" as a variant phrasing on that page, not a second URL — two pages here would just cannibalize each other.

**B) 'skiff reconnect strategy' / 'skiff exponential backoff websocket' — 5 shared → ONE CLUSTER, SEPARATE PAGES.**
Related enough that Google treats them as the same neighborhood, distinct enough that one is the broader task ("how do I reconnect at all") and the other is the specific technique ("how do I back off exponentially"). Family: Task how-to for both. Route to two pages under one cluster — a reconnect-strategy how-to and a backoff-specific how-to (or a backoff section inside the how-to, linked from a dedicated backoff reference if that's where the specific query's incumbent lives) — and cross-link them both ways.

**C) 'skiff presence api' / 'skiff who is online' — 2 shared → SEPARATE CLUSTERS, CROSS-LINK.**
Low overlap despite reading like paraphrases of each other — a real example of the skill's warning that similar-looking wording can draw disjoint result sets. Likely different intents: "presence api" is a reference lookup (an evaluator/dev wants the API surface), "who is online" is a task how-to (someone building a presence-indicator feature and not yet thinking in API terms). Route to two target surfaces — a reference page for the API, a how-to for building an online/offline indicator — link each to the other.

**D) 'skiff message ordering' / 'skiff pricing per connection' — 1 shared → UNRELATED, DO NOT GROUP.**
Confirms what's obvious from reading them: one's a delivery-guarantee/concept question (individual-adoption, technical), the other's a cost question (company-adoption, evaluation). Don't let the shared "skiff" root or superficial "one query about the product" framing tempt you into a combined page. Two separate clusters, two separate families (Concept/Reference vs. Evaluation), no cross-link needed unless a pricing page later wants a "how ordering is billed" aside.

# Handling the other 60

Don't run the merge test on all of them — comparing every pair is quadratic (60 candidates → 1,770 possible pairs), and the skill flags this explicitly as the trap to avoid. Do this instead:

1. **Pre-group by family/topic first, no SERP pulls yet.** Sort the 60 into rough buckets by what they're actually asking (reliability/errors, reconnect/backoff, presence, ordering/delivery guarantees, pricing/limits, integration, etc.) and by adoption mode (individual vs. company). This is a five-minute read-through, not research — obvious non-matches (a pricing query next to a reconnect query) never need a SERP check at all.

2. **Only pull SERPs for boundary candidates.** Within each bucket, flag pairs whose wording is close enough that a merge is *plausible* — same bucket, overlapping vocabulary, or one reads like a rephrasing of the other. That's a small fraction of the 60, not all of them. Everything else either merges by obvious identity (near-identical phrasing, skip straight to "one page") or stays separate by obvious topic distance (skip the check entirely).

3. **Run the same mechanical test on that shortlist.** Pull top-10 organic for each flagged pair, count shared URLs, apply the same four-band table — no re-litigating band boundaries case by case, the table already made that call.

4. **Log every decision as you go**, even the "obviously don't group" ones you skipped SERPs for — one row per candidate: cluster name, paired-with (if any), shared count (or "skipped — no plausible overlap"), decision, target surface. This is what stops you from re-doing the same judgment call next quarter and becomes your "Fix first" cannibalization check input for free.

5. **Batch the SERP pulls.** Do all the flagged pairs' searches in one sitting, dump result URLs into a sheet, compute overlaps with a formula rather than eyeballing each pair — the mechanical counting is where people burn out, not the judgment.

If you want, hand me the 60 and I'll do the family pre-grouping pass with you — that's the step that kills most of the pairwise work before any SERP-checking starts.