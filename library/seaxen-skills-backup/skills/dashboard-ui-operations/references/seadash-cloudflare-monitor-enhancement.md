# SeaDash Cloudflare / Tunnel enhancement notes

Use for incremental upgrades that add Cloudflare awareness, public URL health, and alert plumbing to an existing SeaDash install.

## High-value implementation pattern

- Extend backend first with a monitor payload, commonly exposed as `/api/monitor` and merged into `/api/stats` or `/api/dashboard`.
- Surface three classes of state in UI:
  - local/internal
  - public
  - zero-trust / sensitive
- Add actions that operators actually use:
  - tunnel logs
  - tunnel restart
  - test alert

## Minimal verification targets

- `python3 -m py_compile server.py`
- service restart succeeds
- `/api/monitor` returns structured keys for alerts, apps, cloudflare, notifications, and timestamp
- browser shows app cards, not just header/widgets
- a notification test endpoint returns connector state clearly

## Important interpretation rules

- `cloudflare.urls: []` does **not** mean the feature failed. It can simply mean there are no mapped public routes yet.
- A cloudflared helper UI may only expose token-entry UX. Do not assume it has an API for route discovery.
- If the dashboard renders shell elements but no cards, suspect frontend scope breakage before blaming backend APIs.

## Example route mapping payload

```json
[
  {
    "section": "docker",
    "name": "open-webui",
    "public_url": "https://ai.example.com",
    "access": "zero_trust",
    "sensitive": false
  },
  {
    "section": "docker",
    "name": "portainer",
    "public_url": "https://portainer.example.com",
    "access": "zero_trust",
    "sensitive": true
  }
]
```

## Recovery tactic when frontend enhancement breaks rendering

If original inline JS has inconsistent scope and wrappers fail:

1. expose only the minimum required globals/state if possible
2. if that still fails, add a **small runtime repair layer** that:
   - fetches live API data
   - rebuilds card DOM
   - preserves core monitoring actions
3. leave a note to refactor the repair back into native page logic later
