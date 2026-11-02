Assuming "public model hub" = Hugging Face Hub (the mechanics below — rolling download counts, one-like-per-account, `?sort=trending`, unauthenticated rate limits — are specific to it; flag if it's actually Kaggle/Civitai/Ollama/etc. and I'll adjust).

## 1. The "1.2M downloads" board number is a mixed metric and should not be reported as one figure

Model downloads and dataset downloads aren't the same kind of event — datasets get pulled once per training run and cached, models get re-resolved on every cold start, CI job, container rebuild, or autoscaled inference replica. Adding them together produces a number that's bigger but means nothing: it can't be compared period-over-period (the mix shifts), and a reader assumes "1.2M downloads" means model adoption when a large chunk could be dataset fetches from a handful of ML researchers.

Also check what window that number covers. The Hub's `downloads` field for models is a **rolling ~30-day count**, not a lifetime total. If someone took last month's snapshot and is presenting it as a cumulative "1.2M downloads ever," that's a second, separate error layered on top of the model+dataset mixing — worth confirming before the next board meeting, not after.

**Fix:** report model downloads (30-day) and dataset downloads (30-day) as two numbers, and if you want a cumulative "reach" figure, sum monthly snapshots you've actually stored yourself (see §4) rather than presenting one rolling window as if it were all-time.

## 2. The "breakout" model is very likely the wrong one

- Model A: 40,000 downloads / 12 likes → like ratio 0.03%
- Model B: 900 downloads / 310 likes → like ratio 34.4%

That's backwards from how organic engagement behaves. A "like" on the Hub requires a logged-in account and is capped at one per account — it's a genuine distinct-human signal. A "download" is a counted file-resolution event, not a distinct-human signal — the same person's CI pipeline, autoscaler, or notebook re-run can trigger dozens of counted downloads with zero additional humans involved.

So Model A's number (huge downloads, almost no likes) reads as **real, repeated production usage by people who don't bother to click a heart** — exactly what you'd expect from a model quietly embedded in someone's pipeline. Model B's number (tiny downloads, huge likes) reads as **a small number of people liking it without actually pulling it** — consistent with an internal team rallying likes, a social/Twitter callout, or coordinated/bot activity, not organic breakout adoption.

Calling B the breakout gets the story backwards. Recommend re-pulling both models' referrer/README-click data if the Hub exposes it for your org, and rebrief whoever you've been telling this to — model A is the one with actual traction.

## 3. You cannot get "distinct people who pulled each model" from the Hub API — full stop

The `downloads` count is an event counter (file-resolution requests through the tracked client libraries), not a unique-visitor or unique-IP count. There is no Hub API endpoint that returns per-model unique downloader counts — the Hub doesn't expose per-request identity data publicly, partly by design (privacy) and partly because it isn't tracked that way for public consumption. Any number you'd get from that field will overcount real humans, sometimes by a lot, for models that live inside automated pipelines.

If you genuinely need a "distinct people" number, the only real paths are:
- Self-host a mirror/proxy in front of the weights and log unique IPs/API keys yourself (you control the data, but you lose the Hub's organic discovery traffic for those pulls).
- Ask if the Hub offers an enterprise/org analytics tier — even then, expect aggregated estimates, not a literal distinct-person count, for the same privacy reasons.

Don't put "distinct downloaders" on a board slide sourced from the public API — there's no honest way to produce that number from it.

## 4. Tracking weekly trending rank

There's no historical trending-rank endpoint — trending is a live sort order (`GET /api/models?sort=trending&direction=-1&limit=N`), so "weekly rank" only exists if you snapshot it yourself.

Minimal approach:
1. Weekly cron hits `models?sort=trending&direction=-1&limit=100` (and the dataset equivalent), finds each of your 6 model IDs / 3 dataset IDs by index in the returned list → that index+1 is the week's rank.
2. If a model isn't in the top 100, store rank as `null`/unranked for that week — don't silently drop the row, a missing week and a real "fell out of top 100" look identical if you don't distinguish them.
3. Store `(entity_id, snapshot_date, rank, downloads, likes)` in an append-only table (SQLite/Postgres/CSV, whatever you're already running). This also gives you the real download-count time series to fix the "rolling 30-day presented as lifetime" problem in §1.

## 5. Fix the cron job before trusting any of this data

Unauthenticated requests share the Hub's anonymous, IP-based rate-limit pool with every other unauthenticated caller globally — not a per-org allowance. A weekly poll across 9 entities is small, but if it ever gets a 429 and the script doesn't handle that explicitly, a failed week silently looks like "no data" or, worse, like a real rank/download drop rather than an API failure. That's a correctness risk sitting directly underneath the trending-rank tracking you're about to build in §4.

Fix: create a **fine-grained, read-only** access token scoped to nothing but public read, add `Authorization: Bearer <token>` to the cron job's requests, and store it as a secret (env var / secrets manager, not in the script). Also add explicit 429/5xx handling that records "poll failed" as its own state rather than writing a null or zero into the same column you use for "not in top 100" — those are different facts and conflating them will produce another misleading board slide six months from now.