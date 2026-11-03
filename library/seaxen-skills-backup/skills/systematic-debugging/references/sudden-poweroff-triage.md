# Sudden Power-Off / Overnight Shutdown Triage

Use when a laptop or small always-on host dies between midnight and morning and the user is unsure whether it is config, OS policy, or unstable power.

## Fast triage order

1. **Rule out scheduled power actions**
   - `systemctl list-timers --all`
   - `crontab -l`
   - `crontab -l -u root`
2. **Rule out lid / idle / sleep policy**
   - `/etc/systemd/logind.conf`
   - `/etc/systemd/sleep.conf`
   - `/etc/UPower/UPower.conf`
3. **Check boot history**
   - `journalctl --list-boots`
   - `journalctl -b -1 -e`
   - warning slice around suspect window if available
4. **Check battery health, not just percentage**
   - `upower -i /org/freedesktop/UPower/devices/battery_BAT0`
   - compare `energy-full` vs `energy-full-design`
5. **Check your own periodic logs for timestamp gaps**
   - hard gaps are strong evidence of machine-off periods
6. **Check thermals and storage transport**
   - thermal zones / sensors
   - `smartctl -H` and key attributes

## Interpretation heuristics

- Battery at ~5–10% of design capacity can make even tiny AC interruptions fatal.
- `CriticalPowerAction=HybridSleep` explains policy, but not a sudden wall-power cut.
- Temperatures in the high 50s to high 60s C are not enough to call thermal shutdown without logs proving it.
- SSD SMART can pass while `CRC_Error_Count` is high; that points to SATA path instability more than flash-media failure.

## Lightweight instrumentation that helps next time

- `* * * * *` minute logger for battery/AC/thermals/uptime
- `@reboot` boot marker log entry
- persistent journald retention for prior-boot inspection
- daily SMART summary on internal disks

## Session example: ASUS X455LAB / DietPi

Observed pattern:
- No auto-off timer found
- Lid-close actions explicitly ignored
- Battery health ~8.3% of design (`3.093 Wh` full vs `37.331 Wh` design)
- Hourly log showed an 8-hour gap from `01:00:01` to `09:00:01`
- Root SSD `/dev/sdb` SMART passed, but `CRC_Error_Count=3364`

Most likely conclusion in that case:
1. degraded battery
2. brief AC drop / charger / DC jack issue
3. secondary check: SSD connector/path instability if broader crashes continue
