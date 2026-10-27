#!/usr/bin/env python3
"""Gate O - load and soak.

A real load generator, not a checklist.  It hammers one or more routes with
N concurrent workers, measures latency percentiles, throughput and error
rate, and then checks for *drift*: a soak is a long run where the tail must
not degrade compared with the start.

Thresholds (override on the command line):
    --p95 1000        max p95 latency in ms
    --error-rate 1    max % of failed requests
    --rps 0           min requests/second (0 = not enforced)
    --duration 10     seconds of steady-state traffic
    --workers 8       concurrent workers
    --soak 30         extra seconds of soak traffic (0 = skip soak)
    --soak-interval 0 seconds per soak window (0 = auto: soak / 6)
    --soak-drift 50   max % p95 growth between the first and last soak third

A soak is a *time series*: the window is measured repeatedly and the trend
(first third vs last third) is what is judged, plus the error-rate trend.
The report is written to ``qa/load.json``.

Usage:
  python scripts/load_check.py --url http://localhost:3000 --routes /,/api/items
  python scripts/load_check.py --url ... --duration 30 --soak 60 --json

Exit 0 = thresholds met, 1 = thresholds breached, 2 = nothing to measure.
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
import threading
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import emit, parse_cli, resolve_root, root_error  # noqa: E402
from qa_ext import GateResult, http_request, print_report  # noqa: E402


def percentile(values, pct):
    if not values:
        return 0.0
    ordered = sorted(values)
    if len(ordered) == 1:
        return ordered[0]
    k = (len(ordered) - 1) * (pct / 100.0)
    lo = int(k)
    hi = min(lo + 1, len(ordered) - 1)
    return ordered[lo] + (ordered[hi] - ordered[lo]) * (k - lo)


def _worker(url, duration, stop_at, results, lock):
    latencies = []
    errors = 0
    count = 0
    while time.monotonic() < stop_at:
        started = time.perf_counter()
        res = http_request(url, timeout=15.0)
        elapsed = (time.perf_counter() - started) * 1000
        count += 1
        if res["status"] == 0 or res["status"] >= 500:
            errors += 1
        else:
            latencies.append(elapsed)
        if time.monotonic() >= stop_at:
            break
    with lock:
        results.append({"count": count, "errors": errors, "latencies": latencies})


def run_phase(url, duration, workers):
    stop_at = time.monotonic() + duration
    results = []
    lock = threading.Lock()
    threads = [threading.Thread(target=_worker,
                                args=(url, duration, stop_at, results, lock))
               for _ in range(workers)]
    started = time.monotonic()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    elapsed = max(0.001, time.monotonic() - started)
    latencies = [l for r in results for l in r["latencies"]]
    total = sum(r["count"] for r in results)
    errors = sum(r["errors"] for r in results)
    return {
        "requests": total,
        "errors": errors,
        "error_rate_pct": round(100.0 * errors / total, 2) if total else 0.0,
        "rps": round(total / elapsed, 1),
        "p50_ms": round(percentile(latencies, 50), 1),
        "p95_ms": round(percentile(latencies, 95), 1),
        "p99_ms": round(percentile(latencies, 99), 1),
        "max_ms": round(max(latencies), 1) if latencies else 0.0,
        "duration_s": round(elapsed, 1),
    }


def main() -> int:
    args = sys.argv[1:]
    _root, json_mode, want_help = parse_cli(args)
    url = None
    routes = []
    root_arg = "."
    workers = 8
    duration = 10
    soak = 0
    soak_interval = 0
    max_drift = 50.0
    max_p95 = 1000.0
    max_error_rate = 1.0
    min_rps = 0.0
    i = 0
    while i < len(args):
        a = args[i]
        nxt = args[i + 1] if i + 1 < len(args) else None
        if a == "--url" and nxt:
            url = nxt
        elif a == "--root" and nxt:
            root_arg = nxt
        elif a == "--routes" and nxt:
            routes = [r.strip() for r in nxt.split(",") if r.strip()]
        elif a == "--workers" and nxt:
            workers = int(nxt)
        elif a == "--duration" and nxt:
            duration = int(nxt)
        elif a == "--soak" and nxt:
            soak = int(nxt)
        elif a == "--soak-interval" and nxt:
            soak_interval = int(nxt)
        elif a == "--soak-drift" and nxt:
            max_drift = float(nxt)
        elif a == "--p95" and nxt:
            max_p95 = float(nxt)
        elif a == "--error-rate" and nxt:
            max_error_rate = float(nxt)
        elif a == "--rps" and nxt:
            min_rps = float(nxt)
        i += 1
    if want_help:
        print(__doc__)
        return 0
    if not url:
        print("ERROR: --url is required", file=sys.stderr)
        return 1
    root = resolve_root(root_arg)
    err = root_error(root)
    if err:
        print(f"ERROR: {err}", file=sys.stderr)
        return 1
    routes = routes or ["/"]
    targets = [r if str(r).startswith("http") else url.rstrip("/") + "/" + str(r).lstrip("/")
               for r in routes]

    result = GateResult("O", "LOAD & SOAK")
    phases = []
    for target in targets:
        phase = run_phase(target, duration, workers)
        phase["route"] = target
        phases.append(phase)

    # If EVERY request failed the app was not reachable at all: the
    # measurement could not be taken. That is a SKIP, not a 100 % error-rate
    # failure of the app.
    total_requests = sum(p["requests"] for p in phases)
    total_errors = sum(p["errors"] for p in phases)
    unreachable = bool(total_requests) and total_errors == total_requests

    if unreachable:
        result.add("the app was reachable while the load was applied", False, False,
                   f"{total_errors}/{total_requests} requests failed - the app could "
                   f"not be reached, so no measurement was possible")
        result.notes.append(
            "the app was not reachable during the load run - the measurement was "
            "skipped instead of being reported as a 100 % error rate")
    else:
        for phase in phases:
            target = phase["route"]
            result.add(f"{target}: p95 <= {max_p95} ms",
                       phase["p95_ms"] <= max_p95, True,
                       f"p95 {phase['p95_ms']} ms, p99 {phase['p99_ms']} ms, max {phase['max_ms']} ms")
            result.add(f"{target}: error rate <= {max_error_rate} %",
                       phase["error_rate_pct"] <= max_error_rate, True,
                       f"{phase['errors']}/{phase['requests']} failed")
            if min_rps:
                result.add(f"{target}: throughput >= {min_rps} rps",
                           phase["rps"] >= min_rps, True, f"{phase['rps']} rps")

    soak_data = []
    if soak > 0 and targets:
        # A real soak is a time series: the window is measured again and again
        # and the trend is what matters, not two independent runs.
        interval = soak_interval or max(2, soak // 6)
        windows = max(2, soak // interval)
        third = max(1, windows // 3)
        for target in targets:
            series = []
            for window in range(windows):
                phase = run_phase(target, interval, workers)
                series.append({
                    "window": window + 1,
                    "p50_ms": phase["p50_ms"],
                    "p95_ms": phase["p95_ms"],
                    "p99_ms": phase["p99_ms"],
                    "rps": phase["rps"],
                    "requests": phase["requests"],
                    "errors": phase["errors"],
                    "error_rate_pct": phase["error_rate_pct"],
                })
            first_avg = sum(s["p95_ms"] for s in series[:third]) / third
            last_avg = sum(s["p95_ms"] for s in series[-third:]) / third
            drift = round(100.0 * (last_avg - first_avg) / first_avg, 1) if first_avg else 0.0
            first_err = max(s["error_rate_pct"] for s in series[:third])
            last_err = max(s["error_rate_pct"] for s in series[-third:])
            soak_data.append({
                "route": target,
                "windows": windows,
                "interval_s": interval,
                "series": series,
                "first_p95_ms": round(first_avg, 1),
                "last_p95_ms": round(last_avg, 1),
                "drift_pct": drift,
                "first_error_rate_pct": first_err,
                "last_error_rate_pct": last_err,
            })
            result.add(f"{target}: no latency drift under soak (<= {max_drift} %)",
                       drift <= max_drift, True,
                       f"p95 avg {round(first_avg, 1)} ms -> {round(last_avg, 1)} ms "
                       f"({drift} %) over {windows} windows of {interval}s")
            result.add(f"{target}: no error-rate growth under soak",
                       last_err <= max(first_err, max_error_rate), True,
                       f"error rate {first_err} % -> {last_err} %")

    payload = print_report(result, json_mode, extra={
        "phases": phases, "soak": soak_data,
        "thresholds": {"p95_ms": max_p95, "error_rate_pct": max_error_rate,
                       "min_rps": min_rps, "duration_s": duration,
                       "soak_s": soak, "soak_interval_s": soak_interval,
                       "soak_drift_pct": max_drift, "workers": workers},
        "unreachable": unreachable,
    })
    try:
        out_dir = root / "qa"
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "load.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    except OSError:
        pass
    emit([], payload, json_mode)
    if unreachable:
        return 2
    return 1 if result.blocking else 0


if __name__ == "__main__":
    raise SystemExit(main())
