# Dashboard Watchdog Cron Pattern (2026-06-17)

## Problem

Systemd auto-restart catches hard crashes (the dashboard process exits
non-zero → restart). It does **not** catch:
- The service is up but `/api/recall` returns empty
- The service is up but recall quality has silently degraded
- The FTS5 index is corrupted
- A scoring regression shipped silently
- The dashboard is serving stale data because the recall DB rebuild failed

In all these cases, the agent's auto-injected context degrades silently
and the user doesn't know.

## Pattern: script-only cron with health threshold

A `no_agent: true` script that periodically pings `/api/memory-health` and
alerts on threshold breach. Runs every 4 hours by default.

### Cron registration

```bash
hermes cron create \
  --name obsidian-dashboard-watchdog \
  --schedule "every 4h" \
  --no-agent \
  --script obsidian_dashboard_watchdog.py \
  --deliver local
```

The script is the dashboard watchdog. Use `no_agent: true` so the script
itself produces the message — no LLM cost, no LLM hallucination, no LLM
quota. Exit code 0 = healthy, 1 = degraded, 2 = unreachable.

### Script skeleton

```python
#!/usr/bin/env python3
"""Watchdog for the Obsidian vault dashboard service."""
from __future__ import annotations
import json
import sys
import time
import urllib.error
import urllib.request

HEALTH_URL = "http://127.0.0.1:6065/api/memory-health"
THRESHOLD_RECALL = 95.0
THRESHOLD_HIT_AT_K = 0.85
THRESHOLD_MRR = 0.80
STATE_PATH = "/tmp/obsidian-dashboard-watchdog.state"


def fetch_health() -> dict | None:
    try:
        with urllib.request.urlopen(HEALTH_URL, timeout=5) as r:
            return json.loads(r.read())
    except (urllib.error.URLError, json.JSONDecodeError, OSError):
        return None


def send_alert(message: str) -> None:
    # 1. Log to a file the agent can grep later
    with open("/tmp/obsidian-dashboard-watchdog.log", "a") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")
    # 2. Best-effort Discord delivery via hermes CLI
    try:
        import subprocess
        subprocess.run(
            ["hermes", "send", "--target", "discord", "--message", message],
            timeout=8, check=False, capture_output=True,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass


def main() -> int:
    health = fetch_health()
    if health is None:
        send_alert("❌ Obsidian dashboard unreachable")
        return 2

    recall = health["scores"]["recall"]
    hit_at_k = health["recall_eval"]["hit_at_k"]
    mrr = health["recall_eval"]["mrr"]
    broken = health["counts"]["broken_links"]

    if recall < THRESHOLD_RECALL or hit_at_k < THRESHOLD_HIT_AT_K or mrr < THRESHOLD_MRR:
        # Dedupe: don't re-alert if the same state was already alerted
        alert_key = f"{recall}|{hit_at_k}|{mrr}|{broken}"
        prev = ""
        try:
            with open(STATE_PATH) as f:
                prev = json.load(f).get("last_alert", "")
        except (OSError, json.JSONDecodeError):
            pass
        if prev != alert_key:
            send_alert(
                f"⚠️ Dashboard degraded:\n"
                f"  recall={recall}, hit@5={hit_at_k}, mrr={mrr:.3f}\n"
                f"  broken_links={broken}"
            )
            with open(STATE_PATH, "w") as f:
                json.dump({"last_alert": alert_key, "at": time.time()}, f)
        return 1

    print(f"healthy: recall={recall}, hit@5={hit_at_k}, mrr={mrr:.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

### Why dedupe

Without dedupe, a 4-hour cron with a persistent regression would alert
**every 4 hours forever**. The user learns to ignore the alerts. With
dedupe, the alert fires once when the threshold is first crossed, and
silently thereafter until the state changes. Subsequent changes
(recall went from 95 → 80 → 90) trigger fresh alerts.

### Why thresholds, not zero-tolerance

Setting thresholds to "alert on any degradation" is noisy. A 0.5-point MRR
swing from one query being added to the eval is not worth waking the user.
The thresholds here (recall <95, hit@5 <0.85, MRR <0.80) are tuned to the
vault's normal operating range. Adjust if your vault has different
baselines.

## What this catches, what it doesn't

| Failure mode | Watchdog catches? |
|---|---|
| Dashboard process crashed | ✓ (unreachable) |
| Dashboard up, recall empty | ✓ (recall drops below 95) |
| Dashboard up, recall degraded | ✓ (hit_at_k / mrr drop) |
| FTS5 index corruption | ✓ (recall collapses) |
| Scoring regression | ✓ (recall drops) |
| Single query goes wrong | ✗ (need stress test for this) |
| Recency-only wins dominate | partial (recall drops eventually) |
| Broken links accumulate silently | ✓ if broken > 0 set a threshold |

The stress test (see `recall-stress-testing-2026-06.md`) is the complement —
it catches per-query regressions. The watchdog catches fleet-level
regressions.

## Companion: live health check before declaring victory

The watchdog is a fleet check. Before declaring a recall pass "done" in a
session, also run a one-shot:

```bash
curl -s 'http://localhost:6065/api/memory-health' | python3 -c "
import json, sys
d = json.load(sys.stdin)
assert d['scores']['recall'] >= 95, d
assert d['recall_eval']['hit_at_k'] == 1.0, d
assert d['counts']['broken_links'] == 0, d
print('OK')
"
```

This is the per-session acceptance bar. The cron is the per-day fleet
bar. Both are needed.
