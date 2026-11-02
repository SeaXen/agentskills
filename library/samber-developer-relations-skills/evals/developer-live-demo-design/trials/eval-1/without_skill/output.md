Next action: **create local repo `riftline-demo/`**. Build order below kills wifi dependency and gets reused across all 5 events.

Root cause of last year: demo depended on network you don't control. Fix: demo depends on nothing but the laptop — zero wifi, zero staging cluster, zero cloud calls. Airplane mode ON before you walk out.

## 1. Architecture — build once, run local forever

5 pieces, all in `docker-compose.yml`, all offline:

1. **DB container** (assuming Postgres — swap if Riftline targets something else) — 2M-row table baked into image/volume snapshot. No live seed on stage.
2. **Write generator** — separate process, constant INSERT/UPDATE against table, prints live rows/sec + running total.
3. **Riftline itself** — real CLI, real reindex command, run live.
4. **Local dashboard** — one static HTML+JS page, Chart.js bundled locally (no CDN), polls a local metrics port every 250ms. 3 lines: write throughput, read p99 latency, reindex progress %. Flat latency line during reindex *is* the proof — sells harder than narration.
5. **Reset script** — one command, restores DB snapshot + restarts write generator, under 30 sec. Use between rehearsals and as on-stage recovery.

Why a dashboard beats raw terminal: room holds 300 people, scrolling text is unreadable past row 10, a chart line reads from the back.

## 2. Make 2M rows finish inside budget

1. Benchmark on the actual demo laptop, actual dataset, today. Log real time across 5 dry runs.
2. Tune DB: bump `maintenance_work_mem`, use `CREATE INDEX CONCURRENTLY` (or Riftline's equivalent), local NVMe, warm page cache before going on stage.
3. Start the reindex the moment you introduce it verbally — narrate over the run, don't sit silent waiting.
4. Budget 6 of the 8 minutes to run+narration, 2 min buffer. If tuned time still exceeds that, that's a signal to fix before the event, not on stage.

## 3. Failure tiers — this is what rebuilds trust after last year

Rehearse switching tiers, not just the happy path.

1. **Tier 0**: airplane mode ON before walking out. No wifi attempt at all on this segment.
2. **Tier 1** (primary): live local demo above.
3. **Tier 2** (fallback): screen capture of one clean full run, same terminal theme/timing, cued in the deck, one hotkey away.
4. **Tier 3** (last resort): static screenshots/GIF loop in slides — survives even a projector codec failure.
5. Hard trigger: 45 sec of visible trouble → cut to Tier 2. No live debugging in front of an audience. Rehearse the *cut* itself.

## 4. 2-day build

**Day 1 (~6-7h):**
1. Write `docker-compose.yml` + seed script, bake 2M-row snapshot into a volume.
2. Write the write-generator, confirm continuous writes are visible.
3. Tune DB, run first timing test, record real reindex time.
4. Wire Riftline into the stack, confirm reindex succeeds under concurrent writes.

**Day 2 (~6-7h):**
1. Build the dashboard (throughput + latency + progress lines).
2. Write the minute-by-minute script below, time it with a stopwatch.
3. Rehearse the full 8 min, 5+ times, airplane mode ON every time.
4. Record the Tier 2 fallback video from a clean run.
5. Package the repo, pin every Docker image tag — never `latest`, event 5 is 8 months out and drift will bite you.

## 5. Minute-by-minute script (8 min)

1. **0:00–0:30** — state the claim: "2 million rows, reindexing, writes never stop." Start write generator + Riftline reindex, both visible in terminal.
2. **0:30–1:00** — cut to dashboard, full screen. Point at the write line already climbing.
3. **1:00–5:30** — reindex runs, narrate the mechanism (whatever Riftline actually does). Eyes stay on the flat latency line — that's the proof beat.
4. **5:30–7:00** — reindex completes, cut back to terminal, show exit code 0, final write count, zero errors.
5. **7:00–8:00** — one live query against the new index, fast. Close on the number: "X writes landed during reindex, zero dropped."

## 6. Reuse across 5 events, 8 months

1. Keep `riftline-demo/` as its own versioned repo, not a throwaway.
2. Pin all image/dependency versions — no silent drift between event 1 and event 5.
3. Re-run **`./reset.sh && ./run-demo.sh`** the day before every event: fresh battery check, fresh airplane-mode test.
4. Consider a second laptop, preloaded identical, as a physical backup — cheap insurance amortized over 5 events.
5. After each event, log what broke or felt tight in `NOTES.md`. Fix before the next event, not day-of.

Next action: **create `riftline-demo/` now**, write the `docker-compose.yml` skeleton (DB + write-generator + Riftline containers), commit. That's step 1 of Day 1.