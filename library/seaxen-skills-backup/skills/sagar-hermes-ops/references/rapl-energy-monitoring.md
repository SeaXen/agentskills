# RAPL Energy Monitoring (CPU + DRAM)

## Context

Linux doesn't keep historical power records. RAPL counters (`/sys/class/powercap/intel-rapl:0/energy_uj`) are cumulative since boot and reset on every reboot. Battery only reports real-time. So "how much power did I use yesterday" is impossible unless a logger was already running.

## What RAPL Captures

| Domain | Path | What |
|--------|------|------|
| `intel-rapl:0` | `package-0` | CPU package (cores + integrated GPU + cache) |
| `intel-rapl:0:0` | `core` | CPU cores only |
| `intel-rapl:0:1` | `uncore` | Uncore (memory controller, PCIe) |
| `intel-rapl:0:2` | `dram` | DRAM |

**Does NOT capture:** screen/backlight, SSD/NVMe, Wi-Fi/BT, USB devices, voltage regulator losses, dGPU. Whole-system wall draw is typically 30-50% higher than RAPL CPU+DRAM.

## Setup on This Host

The existing per-minute logger `/root/diag/power_watch.sh` was extended with RAPL energy counters:

```bash
RAPL_PKG=$(cat /sys/class/powercap/intel-rapl:0/energy_uj 2>/dev/null || echo na)
RAPL_CORE=$(cat /sys/class/powercap/intel-rapl:0:0/energy_uj 2>/dev/null || echo na)
RAPL_DRAM=$(cat /sys/class/powercap/intel-rapl:0:2/energy_uj 2>/dev/null || echo na)
```

Cron: `* * * * * /bin/bash /root/diag/power_watch.sh` (every 1 min, already existed).

## Daily Report

`/root/diag/energy_report.py [YYYY-MM-DD]` (default: yesterday) computes:
- Total watt-hours (CPU package + DRAM)
- Average and peak 5-min power
- Handles RAPL resets via `boot_id` tracking (reboots detected, forward-deltas only)
- Handles counter wraparound at max_energy_range_uj (~262 TJ)

```bash
python3 /root/diag/energy_report.py              # yesterday
python3 /root/diag/energy_report.py 2026-06-27    # specific date
```

## Daily Discord Notification

Cron job `acb77bf61649` ("Daily Energy Report") runs at midnight `0 0 * * *`:
- `no_agent=True` (zero token cost, just runs the script)
- Script: `~/.hermes/scripts/daily_energy.sh` → runs `energy_report.py` for yesterday
- Delivers to Discord channel `1510847768896208986`
- Output: compact text with Wh, avg W, peak W, reboots count

## Resource Cost

- Reading RAPL files: microseconds of CPU, a few KB of RAM
- 1-min cron = 1440 reads/day, ~288 rows with RAPL data
- Storage: ~17 KB/day in `power_watch.log`, ~6 MB/year
- Negligible — no CPU/RAM/thermal concern

## Key Design Decisions

1. **Full time-series, not just averages.** Raw counter values stored every minute. Totals, averages, peaks, and curves all computed from raw data after the fact.
2. **boot_id tracking.** RAPL resets on reboot. The logger records `boot_id` (from `/proc/sys/kernel/random/boot_id`) so the report script can detect resets and sum only forward-deltas.
3. **Integrated into existing logger.** No separate cron job — RAPL fields appended to the already-running `power_watch.sh` which also logs thermals, battery, load, memory.

## For True Whole-System Power

RAPL undercounts by 30-50%. For exact wall draw:
- Smart plug (Sonoff S31, Tapo) on the charger — $10-15, exact
- USB-PD meter inline with charger — $10, exact at charger
- These are hardware solutions; software-only cannot measure wall draw
