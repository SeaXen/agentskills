# Overnight auto-off vs Hermes cron

Use this when Dr. Sagar says the laptop/server running Hermes "auto turned off" around a specific overnight window and you need to decide whether Hermes caused it.

## Fast triage order

1. **Check timezone first**
   - Confirm the live machine timezone before interpreting 1–3 AM reports.
   - If the host is not on `Asia/Dhaka`, all later time comparisons can be wrong.

2. **Check whether Hermes even had work scheduled then**
   - List Hermes cron jobs and compare their next/last run times against the reported outage window.
   - If there is no cron in that window, say so explicitly. Do not keep implying Hermes cron is still the prime suspect.

3. **Check reboot evidence, not just current service state**
   - Current boot time / service uptime tells you whether the machine came back after the event.
   - A gateway that restarted at ~01:02 does not prove it caused the shutdown; it often only proves the machine rebooted.

4. **Check for abrupt-loss evidence that survives reboot**
   - `dmesg` / kernel lines such as `EXT4-fs ... recovery complete` are strong evidence that the filesystem was not cleanly unmounted.
   - That points toward sudden power loss / hard-off, not a clean planned shutdown.

5. **Check battery health from sysfs**
   - Read `/sys/class/power_supply/*` and compare `energy_full` vs `energy_full_design` (or charge equivalents).
   - If the real full capacity is a small fraction of design capacity, the battery is effectively dead even if it still shows `100%`.
   - A degraded battery + AC briefly dropping is enough to explain instant power-off.

6. **Check for explicit thermal/panic evidence before mentioning it**
   - Only call thermal shutdown, kernel panic, watchdog, or OOM if the logs actually show it.
   - Absence of those lines matters.

7. **Then separately assess Hermes load**
   - Measure gateway memory footprint and inspect lingering browser/MCP child processes.
   - Frame this as a contributing stressor, not the root cause, unless there is direct evidence.

## Strong pattern from this session

Observed pattern:
- No Hermes cron jobs in the reported 1–3 AM window
- Battery telemetry showed severe degradation (`energy_full` far below `energy_full_design`)
- Filesystem recovery happened on boot (`EXT4-fs ... recovery complete`)
- Current Hermes gateway was heavy (~2.4G RSS, ~2.9G peak) with MCP/browser children

Best interpretation:
- **Primary cause:** abrupt power loss / AC interruption with no battery buffer
- **Secondary factor:** Hermes load may raise power draw or stress, but did not itself prove a shutdown trigger

## Good answer shape

Use three buckets:

1. **What Hermes likely did not do**
   - No matching cron jobs in the outage window
   - No evidence of a clean Hermes-triggered shutdown

2. **What the host evidence suggests**
   - Abrupt power loss / hard-off
   - Degraded battery made the host unable to survive even a brief AC drop
   - ext4 recovery supports unclean shutdown

3. **What to do next**
   - Check charger / DC jack / power strip
   - Treat battery as unreliable
   - Clean lingering browser/OAuth processes from Hermes
   - Add power-loss / battery logging for the overnight window

## Pitfalls

- Do not blame Hermes just because Hermes was running.
- Do not confuse service restart time with shutdown cause.
- Do not call a battery healthy because `capacity=100`; compare against design capacity.
- Do not jump to thermal explanations without explicit critical thermal log lines.
- Do not stop at root cause; recommend instrumentation for the next incident.
