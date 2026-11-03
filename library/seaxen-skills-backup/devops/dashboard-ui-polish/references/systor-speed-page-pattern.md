# Systor speed page pattern

Use when adding a "Speed" page to a lightweight self-hosted monitor dashboard.

## Scope split
Treat WAN and LAN as different products:
- WAN/public tests can run from the NAS/server alone.
- True LAN laptop↔NAS throughput cannot be measured from the NAS alone; expose an `iperf3` server on the NAS and give the user exact client commands.

## UI pattern
Page name:
- `Speed` (not `Speedtest`) when the page includes both WAN and LAN helpers.

Recommended sections:
1. top provider cards
   - `speedtest`
   - `librespeed`
   - `notion probe`
   - `cloudflare probe`
2. speed history chart
3. local LAN helper block
   - server status
   - NAS IPs
   - upload command: `iperf3 -c <nas-ip> -p 5201 -t 15`
   - reverse/download command: `iperf3 -c <nas-ip> -p 5201 -R -t 15`
4. auto-speed monitor summary
5. recent speed-tests table

## Backend pattern
Persist speed checks in SQLite so the page is not just a transient button:
- `speedtests(ts, provider, target, mode, ping_ms, dl_mbps, ul_mbps, note, ok, raw_json)`

Useful API shape:
- `/api/speedtests` → recent rows/history
- `/api/speed/status` → latest per provider + iperf status + local IPs + saved config
- `/api/speed/run` → run selected or all providers now
- `/api/speed/iperf/start` → start iperf3 server

## Provider honesty rules
- `speedtest-cli`/Ookla-style result is the primary WAN datapoint when available.
- Public LibreSpeed results can be region-wrong and misleading; label them honestly if the selected server is distant/unrepresentative.
- Small HTTP probes (Notion/Cloudflare) are quick reachability/latency sanity checks, **not** line-speed tests. Label them as probes, not full speed tests.

## Settings integration
Expose saved defaults if the page has controls:
- page refresh
- default provider
- auto-enabled
- auto provider
- auto interval
- notify enabled
- low DL threshold
- low UL threshold
- LibreSpeed server ID
- iperf port

## User-facing wording
For this user, prefer `DL` / `UL` over `RX` / `TX` across Dashboard, Apps, Network, and Speed pages unless the surface is explicitly low-level per-interface/kernel diagnostics.

## Verification
- live page route exists in deployed app nav
- speed run API stores rows in SQLite
- `iperf3` server status is visible in the page
- Settings page exposes all saved defaults for Speed
- browser verification must hit the deployed `/opt/...` app, not just the repo copy
