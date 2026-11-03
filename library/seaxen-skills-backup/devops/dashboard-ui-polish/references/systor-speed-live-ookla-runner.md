# Systor Speed page — live Ookla runner pattern

Use this when the user wants the Speed page to feel more like a real speed-test surface **without inventing telemetry**.

## Key finding
Official Ookla CLI can expose a live textual stream when run through a PTY wrapper such as:

```bash
script -q -c 'speedtest --accept-license --accept-gdpr -s 33496' /dev/null
```

The stream includes lines like:
- `Server: MS Online - Dhaka (id: 33496)`
- `Idle Latency: 1.95 ms (jitter: 0.26ms, ...)`
- repeated `Download: ... Mbps ... 23% ...`
- repeated `Upload: ... Mbps ... 57% ...`
- `Packet Loss: 0.0%`
- `Result URL: https://...`

That means a live runner can use **real phase/value updates**, not a fake spinner.

## Recommended backend shape
Keep a shared run-state object guarded by a lock:
- `running`
- `phase`
- `progress`
- `target`
- `server_id`
- `ping_ms`
- `jitter_ms`
- `packet_loss`
- `dl_mbps`
- `ul_mbps`
- `ok`
- `status`
- `cancel_requested`
- `result_url`
- `run_type`
- `started_ts`
- `ended_ts`

Expose endpoints:
- `POST /api/speed/live/start`
- `GET /api/speed/live/status`
- `POST /api/speed/live/stop`

## Parsing hints
Useful regexes:
- server line: `Server:\s+(.+?)\s+\(id:\s*(\d+)\)`
- idle latency/jitter: `Idle Latency:\s*([0-9.]+)\s*ms\s*\(jitter:\s*([0-9.]+)ms`
- running download: `Download:\s+([0-9.]+)\s+Mbps.*?(\d+)%`
- running upload: `Upload:\s+([0-9.]+)\s+Mbps.*?(\d+)%`
- final download line: `Download:\s+([0-9.]+)\s+Mbps\s+\(data used:`
- final upload line: `Upload:\s+([0-9.]+)\s+Mbps\s+\(data used:`
- packet loss: `Packet Loss:\s*([0-9.]+)%`
- result URL: `Result URL:\s*(https?://\S+)`

## UI decisions that worked better here
- remove decorative spinner/ring if the user says stop spinning
- show the **selected server name** as the hero title
- keep the hero as:
  - server name
  - GO button
  - small Stop button
  - connected 4-step rail
  - one progress bar
  - compact status line
- update ping/jitter boxes as soon as those values are known
- update DL/UL boxes during real download/upload phases

## Progress semantics
For a calm professional UI, do **not** mirror every CLI percentage jump into the bar unless you are intentionally building a noisy live console feel.

A cleaner compromise:
- `ping = 25%`
- `jitter = 50%`
- `download = 75%`
- `upload = 75% while running`
- `complete = 100%`

This keeps the step rail truthful and avoids the user's complaint that upload looked like it went backward.

## Stop behavior
Implement a real stop by killing the tracked subprocess.
- if stopped mid-run: set live state to `stopped`
- do **not** log a success row to history
- keep the last completed history row unchanged

## Scheduler/UI lesson
This page is a **single saved schedule config**, not a multi-job scheduler table.
So if the user asks to see/edit/delete what was saved:
- keep the form
- add a saved-summary block below it
- add `Disable` and `Clear` actions
- do not invent a fake list of schedule rows

## Easy-to-miss bug
A duplicate DOM id on both the progress wrapper and the fill element made width writes hit the wrong node and produced erratic visuals. If the bar feels wrong, inspect the DOM ids before adjusting animation logic.