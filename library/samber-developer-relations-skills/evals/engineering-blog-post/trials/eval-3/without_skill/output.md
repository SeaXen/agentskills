# Deliverable: blog post draft for Vantage Metrics

**Recommendation: don't publish this as "3x faster ingest than Northlake".** That headline claims a head-to-head result, but the test compared our tuned production profile against Northlake's untuned defaults, with one run each. Northlake's users or engineers can rerun it with a tuned config and publicly contradict the claim. The post below keeps the 3x figure and states the setup in the headline, which makes it defensible.

## Headline options

1. **3x faster ingest than Northlake's default configuration** (recommended: true as stated)
2. How Vantage Metrics ingests 3x faster than a default Northlake install
3. Ingest benchmark: Vantage Metrics (tuned) vs. Northlake (defaults)

---

# 3x faster ingest than Northlake's default configuration

*Draft. Items in [brackets] are details I don't have. Fill them in from your test logs before publishing.*

We benchmarked ingest throughput on Vantage Metrics against Northlake TSDB. In our test, Vantage Metrics running its production tuning profile ingested **about 3x faster** than Northlake on its default install settings.

This post explains what we compared, why we chose that setup, and what the result does and doesn't tell you.

## What we compared

| | Vantage Metrics | Northlake TSDB |
|---|---|---|
| Version | [version] | [version] |
| Configuration | The tuning profile we run in production | Install defaults |
| Instance | AWS m6i.2xlarge (8 vCPU, 32 GiB) | AWS m6i.2xlarge (8 vCPU, 32 GiB) |
| Runs | 1 | 1 |

**Workload:** [number of series, cardinality, points per second or batch size, payload format, client count, test duration, storage type and volume]

**Result:** [Vantage Metrics: X points/s] vs. [Northlake: Y points/s], a ratio of about 3x.

## Why Northlake on defaults

We ran Northlake on its install defaults because that is how most people run it. Many users never tune a database, so defaults show what you get out of the box.

We ran Vantage Metrics with the profile we use in production, not its defaults. This is **not an equal-effort comparison**. It compares our best-known configuration with their untouched one. It shows what you get running each product the way we run ours and the way most people run theirs.

## What this result does not show

- **It is not a tuned-vs-tuned comparison.** A Northlake deployment tuned by someone experienced may close part or all of the gap. We haven't measured that. [If you do: "We plan to publish a tuned-vs-tuned follow-up."]
- **It is one run on one instance type.** We have no variance data, so treat 3x as indicative, not as a precise figure.
- **It measures ingest only.** Query latency, compression, resource usage, and durability settings are out of scope. [State whether durability and fsync settings were equivalent on both sides.]
- **It is our own internal test.** We built the workload and ran it ourselves.

## Reproduce it

[Link to scripts, configs for both systems, and the exact Northlake version. Publishing both configs is the most effective way to make this credible.]

If you run Northlake with a different configuration and get different results, we'd like to hear about it: [contact].

---

## Before you publish

Ordered by value, with rough effort:

1. **Rerun 5 or more times per system** (about 1 hour). Report the median and range. One run can't separate a real 3x from noise, and a "3x" that turns out to be 2.2x on rerun is worse than a modest number up front.
2. **Check Northlake's docs for a recommended production profile** (about 30 minutes). If one exists, run it as a third arm. Even if the gap shrinks, "Nx faster than a tuned Northlake" is a much stronger headline. If the gap holds, you can upgrade the headline.
3. **Confirm the durability and consistency settings are comparable**, such as fsync, WAL, replication, and acknowledgment mode. Mismatches here are the most common reason ingest benchmarks get challenged.
4. **Have Northlake's docs or community checked against your setup.** Vendors often respond to benchmark posts, so make sure nothing in the defaults is a misconfiguration on your side.
5. **Check any Northlake license terms** that restrict publishing benchmarks (DeWitt-style clauses). Some commercial products have them.

Decision for you: if you can't do 1 and 2 before next week, publish the draft above with the "defaults" headline. If you can, wait and publish the stronger version.