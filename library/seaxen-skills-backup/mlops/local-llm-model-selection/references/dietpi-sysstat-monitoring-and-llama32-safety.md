# DietPi 8 GB laptop: sysstat monitoring + llama3.2:3b safety notes

Applies to the user's Asus X455L running DietPi with 8 GB RAM, CPU-only, weak battery, and Ollama/Open WebUI.

## Why this note exists

A request to inspect the *last 24 hours* of CPU/RAM usage could not be answered from history because the machine did not have a metrics collector installed. `sar`/`sysstat` was missing, no Glances history logs were present, and no `atop`/`netdata` history files were found.

## Lightweight fix: enable sysstat for future 24h analysis

Install and enable:

```bash
apt-get update
apt-get install -y sysstat
sed -i 's/^ENABLED=.*/ENABLED="true"/' /etc/default/sysstat
systemctl enable --now sysstat
systemctl enable --now sysstat-collect.timer sysstat-summary.timer
```

Verify:

```bash
systemctl is-active sysstat
systemctl is-active sysstat-collect.timer
systemctl is-active sysstat-summary.timer
ls -l /var/log/sysstat
sar -u 1 1
sar -r 1 1
```

Expected history location:

- `/var/log/sysstat/saDD` for daily binary activity files

Useful follow-up commands after data accumulates:

```bash
sar -u
sar -r
sar -u -f /var/log/sysstat/sa11
sar -r -f /var/log/sysstat/sa11
sar -u -s 00:00:00
sar -r -s 00:00:00
```

## Crash interpretation caution

On this machine, absence of OOM/thermal log messages plus a severely degraded battery means sudden power-off during local inference may be caused by unstable power rather than Linux memory kill events.

Battery state observed earlier in session:

- `energy-full`: `3.093 Wh`
- `energy-full-design`: `37.331 Wh`
- `capacity`: `8.28534%`

So even if a model technically fits in RAM, long/high-CPU runs are still risky if charger connection is unstable.

## `llama3.2:3b` 2-prompt safety test on this hardware

A live Ollama test with 2 prompts completed successfully without system crash.

### Baseline
- available RAM: `5548.7 MB`
- free swap: `4810.5 MB`

### Prompt 1
- wall: `129.0 s`
- first token: `16.5 s`
- load: `10.6 s`
- generation: `4.09 tok/s`

### Prompt 2
- wall: `61.4 s`
- first token: `3.47 s`
- load: `0.50 s`
- generation: `4.55 tok/s`

### Peak pressure during test
- minimum available RAM: `2954.0 MB`
- RAM drop from baseline: `2594.6 MB`
- additional swap used: about `17 MB`

### After test
- model unloaded successfully (`/api/ps` empty)
- system remained alive
- current available RAM returned above `5 GiB` on later live check

## Practical conclusion

`llama3.2:3b` looks *usable* and relatively safe among the tested local models on this 8 GB CPU-only DietPi laptop, but:

- it is still slow
- sustained CPU load is expected while generating
- power/battery condition remains the larger real-world risk

Recommended framing for future sessions:

- safer local picks: `llama3.2:3b`, `qwen3.5:2b`
- borderline / use selectively: `qwen2.5-coder:3b`, `phi4-mini:latest`
- avoid locally on this machine: `gemma4:e2b`, `gemma4:e4b`
