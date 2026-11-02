**Fix cron job now: add API token to poller.** Hub rate-limits per 5-minute window, anonymous callers get a fraction of authenticated quota. Unauthed daily/weekly poll risks silent 429s → flat line reads as "adoption died" when it's just rate-limiting. This breaks before anything else does.

Below: full read on your 4 asks, in tracking-plan shape (single-surface: artifact hub).

## Decisions this plan serves

| # | Decision | Question that settles it |
|---|----------|---------------------------|
| 1 | Board slide download number | Is "1.2M downloads" one honest number or two incompatible ones summed? |
| 2 | "Breakout" model narrative | Does like-count support a usage claim? |
| 3 | Trending rank tracking | Snapshot it how, and can it carry a target? |
| 4 | Unique downloaders per model | Answerable from current setup or not? |

## Finding 1 — the 1.2M figure is not a valid sum

Model downloads and dataset downloads on this hub are **two different counting regimes**, not two rows of the same metric:

- **Model download** = every `GET`/`HEAD` on a per-library query file (`config.json` by default). CI hitting your repo on every build counts every time. Self-contained formats (GGUF) double-count a whole-repo clone as one download.
- **Dataset download** = every file one IP pulls from one repo inside a 5-minute window collapses to **one** download.

These are not summable and not comparable to each other — direct from the hub's own published counting docs. "1.2M downloads" (models + datasets combined) mixes an inflate-prone request count with a dedup'd-by-IP count and reports it as one clean number. **Kill that line.** Report two numbers: "X model downloads" and "Y dataset downloads," each labeled with what it counts. Neither is a user count.

## Finding 2 — the "breakout" call is unsupported

| Model | Downloads | Likes |
|---|---|---|
| A | 40,000 | 12 |
| B (called "breakout") | 900 | 310 |

Likes and downloads are two different signals, not two views of one thing: **likes concentrate on new releases (recency), downloads concentrate on adoption (usage over time).** The hub's own analysis names treating one as a proxy for the other "the most common mistake we see in coverage of the Hub."

Model B has 44x fewer downloads than A. High likes says people are noticing it — not using it. Calling B the "breakout" on a like-count is exactly the named mistake. Correct framing: "B is getting attention, adoption hasn't followed yet" — track B's downloads over the next few weekly snapshots before repeating "breakout" externally. If downloads stay flat while likes plateau, the honest read is "well-received, low-adopted," not breakout.

## Finding 3 — trending rank: track it, don't target it

Trending score is an opaque API sort key — no published formula, no stability guarantee. **Snapshot weekly, never set a threshold or goal on it.** Public API returns current state only, no history — the moment you start saving is the earliest data point you'll ever have; nothing before today is recoverable.

## Finding 4 — unique downloaders: not answerable today

Per-request dedup (hashed user/IP, country, agent) is a **paid enterprise add-on** on this hub, not part of the default API. Default org dashboard is explicitly "not deduplicated by user." Until that tier is bought, "how many distinct people pulled model X" has no answer — only "how many requests." Don't publish a people-count derived from raw downloads; it will be wrong and undefendable.

Options, ranked:
1. Buy the enterprise per-request-log add-on if this number matters enough to pay for.
2. Otherwise, report request-count only, labeled as such, and drop the "distinct people" framing everywhere internally too — it primes the board to expect a number this setup can't produce.

## Build order (do in this sequence)

| Rank | What | Effort | Buys |
|---|---|---|---|
| 1 | Add API token to the cron poller | minutes | stops silent 429-flatline risk before any snapshot job runs |
| 2 | Daily snapshot job: per-model downloads, per-model likes, per-dataset downloads, trending rank | ~1 hour to write, then standing | the only history you'll ever have — API has no time series |
| 3 | Split board metric into two labeled series (model / dataset) | ~1 hour, decision only | kills the false 1.2M composite |
| 4 | Weekly trending-rank report, framed as observation not KPI | none — reuse snapshot | visibility without inventing a fake target |
| 5 | Decide on unique-downloader paid tier | budget call | only route to a real people-count |

## Snapshot store — fields to save daily (public API gives no history, so this is your only source)

| Field | Type | Notes |
|---|---|---|
| `artifact_id` | string | model or dataset slug |
| `artifact_type` | enum: `model`, `dataset` | never merge these two series |
| `downloads_total` | int | cumulative counter as returned; report deltas, not the raw cumulative, for a "this week" number |
| `likes_total` | int | separate series from downloads, never blended |
| `trending_rank` | int, nullable | opaque; log for trend-watching only |
| `snapshot_date` | date | dedup key |

## Known gaps (say these out loud on the slide, not just in this doc)

| Gap | Impact | Fix |
|---|---|---|
| Model downloads include CI/bot traffic | model number likely overstates real adoption | none available without paid logs; caveat the number instead |
| No dedup by user | can't claim "distinct people" | buy add-on, or drop the claim |
| No history before today's snapshot | can't backfill trending or past download curve | starts now, unrecoverable for the past |
| Anonymous polling | risk of rate-limit-induced false flatline | fixed by adding token (step 1 above) |

Next: add the token to the cron job — that's the one open item that actively risks corrupting every number above it.