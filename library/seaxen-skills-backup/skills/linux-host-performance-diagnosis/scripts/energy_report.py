#!/usr/bin/env python3
"""
Compute daily CPU+DRAM energy consumption from power_watch.log.
Handles RAPL resets (reboots) via boot_id tracking.
Usage: energy_report.py [YYYY-MM-DD]  (default: yesterday)
"""
import sys
import re
from datetime import datetime, timedelta

LOG = "/root/diag/power_watch.log"

LINE_RE = re.compile(
    r'\[(\d{4}-\d{2}-\d{2}) \d{2}:\d{2}:\d{2} [+-]\d{4}\] '
    r'boot_id=([0-9a-f-]+) uptime_s=([\d.]+)'
    r'.*?rapl_pkg_uj=(\d+|na).*?rapl_core_uj=(\d+|na).*?rapl_dram_uj=(\d+|na)'
)

MAX_ENERGY_UJ = 262143328850  # RAPL counter wraparound point


def parse_log(target_date):
    samples = []
    try:
        with open(LOG) as f:
            for line in f:
                m = LINE_RE.search(line)
                if not m:
                    continue
                date_str, boot_id, uptime, pkg, core, dram = m.groups()
                if date_str != target_date:
                    continue
                if pkg == "na" or dram == "na":
                    continue
                samples.append({
                    "boot_id": boot_id,
                    "uptime_s": float(uptime),
                    "pkg_uj": int(pkg),
                    "core_uj": int(core),
                    "dram_uj": int(dram),
                })
    except FileNotFoundError:
        pass
    return samples


def compute_energy_uj(samples):
    if len(samples) < 2:
        return 0, 0, 0
    total_pkg, total_core, total_dram = 0, 0, 0
    prev = samples[0]
    for s in samples[1:]:
        if s["boot_id"] != prev["boot_id"] or s["uptime_s"] < prev["uptime_s"]:
            prev = s
            continue
        d_pkg = s["pkg_uj"] - prev["pkg_uj"]
        d_core = s["core_uj"] - prev["core_uj"]
        d_dram = s["dram_uj"] - prev["dram_uj"]
        if d_pkg < 0: d_pkg += MAX_ENERGY_UJ
        if d_core < 0: d_core += MAX_ENERGY_UJ
        if d_dram < 0: d_dram += MAX_ENERGY_UJ
        total_pkg += d_pkg
        total_core += d_core
        total_dram += d_dram
        prev = s
    return total_pkg, total_core, total_dram


def main():
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

    samples = parse_log(target)
    if not samples:
        print(f"No RAPL data found for {target}")
        print("(Note: RAPL logging started 2026-06-27. Earlier dates have no energy data.)")
        return

    pkg_uj, core_uj, dram_uj = compute_energy_uj(samples)
    pkg_wh = pkg_uj / 3.6e9
    core_wh = core_uj / 3.6e9
    dram_wh = dram_uj / 3.6e9
    total_wh = pkg_wh + dram_wh

    first_uptime = samples[0]["uptime_s"]
    last_uptime = samples[-1]["uptime_s"]
    boot_ids = set(s["boot_id"] for s in samples)

    total_j = (pkg_uj + dram_uj) / 1e6
    duration_h = (last_uptime - first_uptime) / 3600
    avg_w = total_j / (duration_h * 3600) if duration_h > 0 else 0

    peak_w = 0
    prev = samples[0]
    for s in samples[1:]:
        if s["boot_id"] != prev["boot_id"] or s["uptime_s"] < prev["uptime_s"]:
            prev = s
            continue
        d_pkg = s["pkg_uj"] - prev["pkg_uj"]
        d_dram = s["dram_uj"] - prev["dram_uj"]
        if d_pkg < 0: d_pkg += MAX_ENERGY_UJ
        if d_dram < 0: d_dram += MAX_ENERGY_UJ
        interval_j = (d_pkg + d_dram) / 1e6
        interval_w = interval_j / 300
        if interval_w > peak_w:
            peak_w = interval_w
        prev = s

    print(f"════════════════════════════════════════════")
    print(f"  Energy Report: {target}")
    print(f"════════════════════════════════════════════")
    print(f"  Samples: {len(samples)}")
    print(f"  Boot sessions: {len(boot_ids)}")
    print(f"  Duration covered: {duration_h:.2f} hours")
    print(f"  Reboots during day: {len(boot_ids) - 1}")
    print(f"")
    print(f"  CPU Package:   {pkg_wh:7.2f} Wh")
    print(f"  ├─ Cores:       {core_wh:7.2f} Wh")
    print(f"  DRAM:          {dram_wh:7.2f} Wh")
    print(f"  ────────────────────────")
    print(f"  Total (CPU+DRAM): {total_wh:7.2f} Wh  ({total_wh/1000:.3f} kWh)")
    print(f"")
    print(f"  Avg power:     {avg_w:6.2f} W")
    print(f"  Peak 5-min:    {peak_w:6.2f} W")
    print(f"")
    print(f"  ⚠ RAPL = CPU+DRAM only. Whole-system draw")
    print(f"  at the wall is typically 30-50% higher.")
    print(f"════════════════════════════════════════════")


if __name__ == "__main__":
    main()
