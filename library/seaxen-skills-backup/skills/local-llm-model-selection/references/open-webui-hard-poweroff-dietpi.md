# Open WebUI + Ollama hard power-off notes on 8 GB DietPi laptop

Session pattern observed on an Asus X455L-class machine:
- user reported that after a local model answer in Open WebUI, the **entire laptop turned off**
- model in use was `llama3.2:3b`, not one of the heavier Gemma models
- current boot inspection showed `open-webui` healthy and `ollama.service` active with **restart count 0**
- current boot logs showed no OOM-killer, segfault, or service-crash evidence
- therefore the symptom was better classified as **hard power loss / thermal or power instability**, not a normal application crash

## Useful differentiator

If the machine fully powers off:
- do not stop at "Open WebUI crashed"
- check whether the app or service actually restarted
- absence of service restarts plus absence of OOM logs strongly suggests hardware/power/thermal trouble

## High-value checks used

- `docker inspect open-webui --format '{{.RestartCount}}'`
- `systemctl show ollama -p NRestarts,ActiveState,SubState`
- `journalctl -k | egrep -i 'oom|killed process|segfault|thermal|critical|power'`
- `grep -H . /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor`
- `for f in /sys/class/thermal/thermal_zone*/temp; do ...; done`
- confirm whether persistent journal exists: `/var/log/journal`

## Important findings from this machine

- CPU governor was `performance`
- thermal zones were already around 59-62 C at modest load
- RAM pressure existed but did not by itself explain a hard power-off
- no persistent journald was enabled initially, so previous-boot evidence was being lost after sudden shutdowns

## Mitigation set that was applied

### Ollama drop-in
Created:
- `/etc/systemd/system/ollama.service.d/override.conf`

Contents:
```ini
[Service]
Environment="OLLAMA_CONTEXT_LENGTH=2048"
Environment="OLLAMA_KEEP_ALIVE=30s"
```

### Persistent CPU governor service
Created:
- `/etc/systemd/system/cpu-governor-schedutil.service`

Behavior:
- writes `schedutil` to each `/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor`
- enabled under `multi-user.target`

### Persistent journald
Created:
- `/etc/systemd/journald.conf.d/persistent.conf`
- `/var/log/journal`

Suggested contents:
```ini
[Journal]
Storage=persistent
SystemMaxUse=200M
RuntimeMaxUse=100M
```

## Verification after changes

- governors became `schedutil` on all CPUs
- Ollama environment showed:
  - `OLLAMA_CONTEXT_LENGTH=2048`
  - `OLLAMA_KEEP_ALIVE=30s`
- live model test with `llama3.2:3b` showed:
  - `llama_context: n_ctx = 2048`
  - `CPU KV buffer size = 224.00 MiB`
- `journalctl --list-boots` started working after persistent journald was enabled

## Practical takeaway

For old 8 GB CPU-only laptops, even `llama3.2:3b` can trigger a full-machine shutdown if the platform is thermally marginal or the governor is too aggressive.

If the next shutdown still happens after these mitigations, prioritize:
- fan / dust / heatsink inspection
- charger and battery stability checks
- previous-boot review with:
  - `journalctl -b -1 -e`
  - `journalctl -k -b -1 -e`
