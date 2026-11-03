# RAPL Energy Logging & Daily Reporting

Extension to `/root/diag/power_watch.sh` (the per-minute cron logger) that adds
Intel RAPL energy counters, plus a Python report script that computes daily
watt-hours from the logged data.

## What was added to power_watch.sh

Three new fields appended to each log line:

```
rapl_pkg_uj=  rapl_core_uj=  rapl_dram_uj=
```

Sources (Intel RAPL via powercap sysfs):

| Domain | Sysfs path | Covers |
|---|---|---|
| Package | `/sys/class/powercap/intel-rapl:0/energy_uj` | Cores + cache + integrated GPU |
| Core | `/sys/class/powercap/intel-rapl:0:0/energy_uj` | Cores only (subset of package) |
| DRAM | `/sys/class/powercap/intel-rapl:0:2/energy_uj` | Memory |

Values are **cumulative microjoules since boot**, reset to zero on every reboot.

## The report script

`/root/diag/energy_report.py` — parses `power_watch.log`, computes daily energy.

Usage:
```bash
python3 /root/diag/energy_report.py              # yesterday
python3 /root/diag/energy_report.py 2026-06-27    # specific date
```

Output: total Wh (CPU package + DRAM), average power, peak 5-min power,
duration covered, reboot count.

## Key implementation details

### Reboot handling (critical)

RAPL counters reset on reboot. The script detects resets via **boot_id**
(already logged by `power_watch.sh`) and **uptime decreasing**. When a reset
is detected, the delta for that interval is skipped (not summed negatively).

### Counter wraparound

RAPL counters wrap at `max_energy_range_uj` (~262 TJ on this Intel chip).
The script handles wraparound by adding the max range if a delta is negative
(and it's not a reboot reset).

### Unit conversion

- RAPL reports microjoules (µJ)
- 1 watt-hour = 3,600,000,000 µJ (3.6×10⁹)
- Average power (W) = total joules ÷ duration in seconds

## What RAPL does NOT capture

This is the most important caveat to communicate to the user:

- Screen / backlight (2–5 W)
- SSD / NVMe
- Wi-Fi / Bluetooth radio
- USB devices
- Voltage regulator losses
- Discrete GPU (if present)

**Rule of thumb:** RAPL undercounts whole-system wall draw by ~30–50%.
If RAPL reads 5 W average, real wall draw is likely 8–15 W idle, 30–60 W
under sustained load.

For true whole-system wattage, a smart plug (Sonoff S31, Tapo, ~$10–15) on
the charger is the only accurate option. RAPL is for trend tracking and
anomaly detection, not billing-grade measurement.

## Daily notification cron

A Hermes cron job (`acb77bf61649`, "Daily Energy Report") runs at midnight
`0 0 * * *`, executes `~/.hermes/scripts/daily_energy.sh` (which calls
`energy_report.py` for yesterday's date), and delivers the output to the
origin Discord channel.

- `no_agent: true` — zero token cost, script output delivered verbatim
- Script path: `~/.hermes/scripts/daily_energy.sh` (must be relative to
  `~/.hermes/scripts/` for the cron `script` field)

## Resource cost

- Reading RAPL files: one `cat` of a few bytes, microseconds of CPU
- Per-minute cron: 288 reads/day, ~17 KB/day of log data
- Negligible CPU/RAM impact — far below the existing power_watch.sh overhead

## Verification

After patching `power_watch.sh`:
```bash
bash /root/diag/power_watch.sh
tail -1 /root/diag/power_watch.log  # confirm rapl_*_uj fields present
python3 /root/diag/energy_report.py 2026-06-27  # should produce a report
```

Minimum 2 samples needed for any delta computation. Wait ~2 min after
patching before testing the report.
