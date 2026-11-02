## The number

COGS per document = $0.017 (GPU) + $0.004 (support) = **$0.021**

Price for 75% gross margin: P such that (P − 0.021) / P = 0.75 → P = 0.021 / 0.25 = **$0.084 per document**

That's roughly **4.2x your current $0.02 price**.

## The number you need to see first

At today's $0.02 price, gross margin is **−5%**. You're not below the 75% target — you're already losing $0.001 on every document before touching R&D, sales, or overhead. The ask isn't "improve margin," it's "stop the bleed and then some."

## The problem with just charging $0.084

Cost-plus is the wrong anchor here, and your prospects are already telling you why: they can self-host the open-weights model on spot instances for **$0.006/doc** — less than a third of what *your own* GPU inference costs you ($0.017), and 14x cheaper than the $0.084 you'd need to charge. Price should sit between the next-best alternative and perceived value, not fall out of your cost structure. $0.084 against a $0.006 anchor is a hard sell unless the gap is visibly justified.

Two levers, not one:

**1. Attack the cost side, not just the price side.** If prospects can hit $0.006/doc on spot instances, your $0.017 GPU cost has real headroom — spot pricing, batching, quantization, better utilization. If you got inference down to ~$0.007 (still a premium over pure DIY, presumably for reliability), total COGS = $0.011, and 75% margin only requires **~$0.044/doc** — a 2.2x increase instead of 4.2x, and a much smaller gap over the $0.006 floor to defend.

**2. Justify whatever premium remains with what $0.006 doesn't include.** The self-host number is raw compute only — it omits MLOps engineering time, uptime/monitoring, model updates, accuracy tuning, and the support you're already budgeting $0.004/doc for. That delta is your pitch: turnkey accuracy + zero ops burden vs. DIY infrastructure risk. Make that comparison explicit on the pricing page, not implicit.

## Recommendation

Don't jump straight to $0.084. Sequence it:
- Fix the cost structure first (target GPU cost toward $0.007–0.010/doc) — cheapest lever, no customer-facing risk.
- Re-run the math on updated COGS; land likely in the **$0.04–0.05/doc** range for 75% margin, a much more defensible multiple over the $0.006 DIY floor.
- Test the new price on new customers first, not existing ones — you have no pricing signal yet, only a cost target. A Van Westendorp pass with a few active prospects (especially the ones citing $0.006) would tell you whether $0.04–0.05 clears their willingness-to-pay before you commit the whole base to it.
- If cost reduction stalls and $0.084 is genuinely required to hit 75% this year, say so to investors as a pricing-power question, not an arithmetic one — that price only holds if you can articulate 14x of differentiation over self-hosting.