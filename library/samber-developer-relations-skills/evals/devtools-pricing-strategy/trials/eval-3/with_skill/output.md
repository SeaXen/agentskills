## What price hits 75% margin — and why that number alone doesn't solve the problem

### The floor

Marginal cost per document: $0.017 (GPU inference) + $0.004 (support) = **$0.021/doc**.

Floor formula (this skill's baseline): `price = marginal cost ÷ (1 − target margin)`

```
$0.021 ÷ (1 − 0.75) = $0.021 ÷ 0.25 = $0.084/document
```

**$0.084/document is what closes the loop to 75% gross margin on your current cost base** — a 4.2x increase over the $0.02 you charge today.

Worth flagging before anything else: at today's $0.02 price against $0.021 cost, you're not at some-margin-below-target — you're at **−5% gross margin right now**. This isn't a "raise it a bit" conversation, it's "the current price doesn't cover COGS."

One caveat on the floor itself: it should be modeled on the **90th-percentile account**, not the blended average — if messier scans, more OCR retries, or heavier support tickets push some accounts' cost meaningfully above $0.021/doc, the real floor sits above $0.084. The two costs you gave read as blended figures; confirm whether they already reflect your heavy accounts or a fleet average before locking the number.

### The ceiling — and why it breaks this

The four ceilings are self-host, build, next-best-vendor, do-nothing; you take the **lowest**. Prospects are already telling you theirs: **$0.006/doc** to run the open-weights model on spot instances.

$0.006 is below your $0.084 floor by 14x. It's below your **raw GPU cost alone** ($0.017) by nearly 3x. Per the method: *"If the lowest ceiling sits below the floor, the problem is the cost structure or the model, not the price. Say so instead of picking a number in between."*

That's the honest answer here: **no price gets you to 75% margin while a prospect's cited alternative costs less than your compute bill alone.** Pushing to $0.084 doesn't buy margin — it buys a much sharper demonstration that self-hosting is 14x cheaper, and accelerates the churn to it.

### The one thing worth checking before believing that number

$0.006 is compute only. It's what a prospect pays AWS/Lambda/etc. for spot GPU time — it is *not* their fully-loaded cost to replace Parchmill, which the method requires you to price against: operator time to build and maintain an OCR + structured-extraction pipeline (not just "run a model"), on-call, spot-instance preemption handling, and the accuracy/liability gap between a tuned production pipeline and a self-assembled one. Prospects citing $0.006 are quoting their own floor, not their ceiling — the real self-host ceiling is very likely higher than $0.006, but you don't have that number yet, and it would be a guess to assume it's anywhere near $0.084.

This is also the classic failure mode named in the skill: *"Pricing against the wrong ceiling — benchmarking only against other vendors while the real alternative is the customer running your own open-source edition for the cost of a VM."* You're not making that mistake — you're already hearing the real ceiling from prospects — but don't let the incomplete version of it (compute-only) stand in for the full number either.

### What actually moves you toward 75%, in order

1. **Get the real ceiling.** Ask a prospect who chose self-host (or one seriously evaluating it) for their fully-loaded estimate — engineering time to build the pipeline, ongoing maintenance, on-call, spot-interruption handling, and what they do about accuracy drift. That number, not $0.006, is what bounds your price.
2. **Attack the cost side.** GPU inference is 81% of your unit cost. Reserved/committed GPU capacity instead of on-demand, quantization or a smaller specialized model, and batching to amortize fixed overhead are the levers that move the floor down instead of the price up.
3. **Differentiate past the commodity comparison.** A raw open-weights model on spot instances doesn't ship an accuracy SLA, a support line, audit trail, or uptime guarantee. If those are real and valued, they widen the gap between your price and the self-host ceiling without you owning the operational burden the prospect is pricing against — that's a packaging move (Step 3), not just a number.
4. **Re-run the floor once 1–2 land.** $0.084 is correct math against today's $0.021 cost — it's the target to re-check against, not the number to ship, until the ceiling and the cost base both move.

**Labeling, as the skill requires:** the $0.084 floor and the −5%-today figure are arithmetic on the numbers you gave, not sourced benchmarks. The 62% median gross margin for usage-only pricing models (vs. 80% software median) is sourced — Aleph x Benchmarkit 2026, 342 companies — and it's the context for why 75% is an aggressive ask for an inference-heavy product, not an unusual one to hold. The 90th-percentile-account modeling rule and the "ceiling below floor → cost problem, not price problem" call are this skill's own baselines, not industry-measured figures.