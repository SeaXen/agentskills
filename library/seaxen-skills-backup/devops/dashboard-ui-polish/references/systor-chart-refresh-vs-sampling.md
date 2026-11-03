# Systor chart refresh vs collector sampling regression

Use this when a lightweight monitor dashboard appears frozen even though chart refresh is set to 1s/5s.

## Symptom
- User sets chart refresh to 1s or 5s.
- Canvas redraws, but visible line does not move for 10+ seconds.
- Status text says `idle`, reinforcing the impression that refresh is broken.
- Previously charts looked OK.

## Root-cause pattern
There are two independent cadences:
1. **Collector sample interval** — writes new rows to storage.
2. **Chart refresh/redraw interval** — fetches and redraws chart data.

If collector writes every 30s and chart redraws every 1s/5s, the UI correctly redraws the same latest sample until the next collector row exists. It looks frozen but the frontend timer is not necessarily broken.

## Verification probes
Check backend sample cadence directly before patching JS timers:

```bash
python3 - <<'PY'
import json, time, urllib.request
url='http://127.0.0.1:6677/api/series?metric=cpu_pct&hours=1'
for i in range(4):
    with urllib.request.urlopen(url) as r:
        j=json.load(r)
    data=j.get('data', [])
    print(i, 'count', len(data), 'tail_ts', [p[0] for p in data[-5:]])
    time.sleep(5)
PY
```

Expected fixed shape for 5s sampling:

```text
tail_ts [..., 1781807545, 1781807550, 1781807555, 1781807560, 1781807565]
tail_ts [..., 1781807550, 1781807555, 1781807560, 1781807565, 1781807570]
```

Check frontend redraw separately:

```js
new Promise(resolve => {
  const get = () => ({
    status: document.querySelector('#load-state')?.textContent,
    chartVal: document.querySelector('#chart-sec')?.value,
    canvasData: [...document.querySelectorAll('canvas')].map(c => c.toDataURL().length),
    avgExists: [...document.body.querySelectorAll('*')].some(x => x.textContent === 'avg')
  });
  const before = get();
  document.querySelector('#chart-sec').value='1000';
  document.querySelector('#chart-sec').dispatchEvent(new Event('change', {bubbles:true}));
  document.querySelector('#manual-refresh-btn').click();
  setTimeout(() => resolve({before, after:get()}), 6500);
})
```

Canvas `toDataURL().length > 10000` usually proves the chart is drawing, not blank.

## Fix pattern
- Expose collector `poll_interval_sec` in Settings as **Sample interval**.
- Keep default sample interval at 5s for responsive charts without too much write load.
- Keep chart redraw at 5s by default; 1s redraw can be offered as a temporary page override.
- Make Settings the saved-default source of truth; page controls are temporary live overrides.
- Remove localStorage page persistence unless UI explicitly labels it as saved.
- Replace post-success `idle` with visible timestamps:
  - `snapshot HH:MM:SS`
  - `charts HH:MM:SS`
- Remove ambiguous labels like `avg` from CPU load cards; use `1m · 5m · 15m`.

## Live-deployed app rule
For `/opt/systor` or similar deployed copies:
1. Patch repo.
2. Run installer/sync step.
3. Restart systemd services.
4. Verify the live deployed DOM and API, not just repo files.

## Tradeoff
Do not default collector sampling to 1s unless the user accepts higher CPU/disk writes. A 5s collector interval plus 1s optional chart redraw is the safer lightweight default.