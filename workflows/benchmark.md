---
description: Empirical benchmark and telemetry protocol (synthesizes test harnesses, executes headlessly, and validates with hardware telemetry).
---

# /benchmark - Empirical Telemetry & Stress Benchmark

$ARGUMENTS

---

## Purpose

Enforces empirical hardware verification. Constructs executable test harnesses, runs them headlessly, and measures real performance metrics (latency, throughput, RSS memory, failure rate).

---

## Workflow Steps

1. **Harness Synthesis:**
   - Synthesizes an ad-hoc micro-benchmark or stress-test harness in `scratch/`.
   - Warms up runtime and runs multiple iterations (p50, p90, p99).

2. **Execution & Telemetry:**
   - Executes via headless command and captures wall-clock time, ops/sec, and peak memory.

3. **Empirical Comparison Matrix:**
   - Reports side-by-side Baseline vs. Candidate performance matrix with p-value confidence.
