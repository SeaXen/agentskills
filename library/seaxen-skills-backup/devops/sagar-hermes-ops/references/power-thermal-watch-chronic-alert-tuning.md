# Power/Thermal Watch Chronic Alert Tuning

Use this when a Hermes `no_agent=True` watchdog runs frequently for logging/forensics, but one alert class is based on a chronic condition that will stay true for days or weeks.

## Problem shape
- Cron job schedule is frequent, often `* * * * *`
- CSV/system snapshot logging is useful every run
- One condition is permanently bad, not transient
- Current alert logic repeats on cooldown forever, so the user gets spammed

Concrete example from this host:
- `power-thermal-watch`
- battery health threshold: `<= 15%`
- actual battery health: `8.0%`
- alert cooldown: `1800s`
- result: a warning every 30 minutes forever, despite no state change

## Preferred fix order
1. Keep the logger cadence if the forensic data is useful.
2. Suppress only the chronic alert class instead of pausing the whole job.
3. Preserve acute alerts: AC offline, critical temp, hot+loaded, sustained CPU/RAM pressure.
4. If the user still wants a reminder, degrade the chronic alert to daily/fixed-time instead of cooldown-based repeats.

## Good implementation shape
Add an explicit constant near the thresholds, for example:

```python
ENABLE_BATTERY_HEALTH_ALERT = False
```

Then gate only that alert block:

```python
if ENABLE_BATTERY_HEALTH_ALERT and should_emit(...):
    ...
```

Why this is better than changing the main schedule:
- logging remains minute-level
- real transient danger alerts still fire quickly
- the chronic hardware fact stops spamming the user
- future re-enable is one obvious edit

## When not to disable the chronic alert
Keep it if the user explicitly wants repetitive reminders or if the condition is expected to change rapidly rather than staying true for weeks.

## Verification
- Run the watcher script directly after patching.
- Expect no output when only the chronic condition is present.
- Confirm the CSV/log file still gets a new row.
- Do not call it fixed until both are true.

## Pitfall
Do not conflate "this condition is always bad" with "the whole watcher is useless". Often the right answer is to keep the recorder and suppress only the noisy notification class.
