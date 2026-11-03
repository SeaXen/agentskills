# Lightweight monitor dashboard: notifications, logs, and metric migrations

Use for small self-hosted Python/stdlib/Flask-style monitoring dashboards that collect `/proc` metrics, persist to SQLite, and expose alert/log/settings pages.

## Durable patterns

### Compact settings/admin pages need explicit operator structure
If the settings page feels sprawling or the user says there is "no save button", fix structure, not just styling.

Good lightweight pattern:
- sticky top action bar with `Save`, `Save & apply`, and restart actions
- compact 2-column card layout instead of long full-width stacked forms
- explicit per-channel status chips (`enabled`, `saved`, `last sent/failed`)
- live access targets (`localhost`, `LAN`, `Tailscale`, tunnel/process status) directly inside Settings
- compact threshold table instead of verbose one-row-per-control prose
- on dark dashboards, explicitly restyle `input`, `select`, and `textarea` backgrounds/borders/placeholders; browser-default white inputs look broken even when the surrounding cards are fine

### Collector restart controls should not depend on pidfiles alone
A web "Restart collector" button should not fail just because `/tmp/...pid` is missing.

Use this pattern:
- check pidfile first
- if missing, discover the exact daemon via `ps -eo pid,args` and exact command matching
- do **not** use loose `pgrep -f` substring matching for restarts; it can accidentally match your own probe shell/wrapper process
- after SIGTERM, wait briefly for the old PID to disappear
- if no replacement came back, start a detached fallback collector so manual/non-systemd deployments still work

### Notification diagnosis split
Keep three separate truths clear:
1. Settings/UI wiring
2. backend delivery path
3. external credential validity

If Telegram still returns `HTTP 404: {"ok":false,"error_code":404,"description":"Not Found"}` from a direct backend test, treat it as an invalid or malformed bot token issue, not as a dashboard-delivery bug.

Before concluding the token is wrong, normalize user input:
- trim bot token
- trim chat ID
- trim Discord webhook URL

### Compact alert-message shape
For lightweight monitor alerts, prefer a short, scan-friendly body over raw metric dumps.

Good default body:
- `Host`
- `State`
- `Metric`
- `Detail`
- one current-context line (`CPU now`, `RAM avail`, `Disk mount/usage`, etc.)
- one likely-cause app line when useful

Cause line rule:
- CPU / temperature alerts → top CPU app only
- memory / swap alerts → top memory app only
- do not include both CPU and memory offender lists in the same compact alert

### One `0.0.0.0` listener can serve localhost, LAN, and Tailscale
When the app binds `0.0.0.0:<port>`, do not model that as separate dashboard copies. It is one listener reachable by multiple addresses.

A tiny `/api/access` endpoint is a good low-cost operator aid. It can return:
- localhost URLs
- preferred/private LAN URL
- Tailscale URL(s)
- simple Cloudflare-tunnel presence (`pgrep -af cloudflared`)

### Log clearing should be a real file operation
If the user asks for a clear button on the logs page, do not fake it with DOM clearing only. Add a backend route that truncates the configured log file and verify both:
- browser state changes to empty/no lines
- on-disk log size becomes `0`

### Restart verification: stale listener beats new code
If curl/browser still show old templates or new routes 404 after edits, check for a stale listener PID before assuming the patch failed.

Practical pattern:
- compare the PID holding the port with the PID of the process you just started
- if the new process exits with `address already in use`, the old one is still serving traffic
- kill the stale listener, restart once, then verify the new route/template again

### SQLite metric additions need additive migrations
If adding new metric columns to an existing SQLite `samples` table, `CREATE TABLE IF NOT EXISTS` is not enough. Existing DBs keep the old schema and inserts/series endpoints will fail with errors like `no column named <metric>`.

Minimum safe pattern:
```python
existing = {row[1] for row in c.execute("PRAGMA table_info(samples)").fetchall()}
for col, typ in {"disk_read_mbps": "REAL", "disk_write_mbps": "REAL"}.items():
    if col not in existing:
        c.execute(f"ALTER TABLE samples ADD COLUMN {col} {typ}")
```
Verify:
- insert path succeeds
- `/api/series?metric=<new_metric>` returns 200
- no fresh collector errors after restart

### Canvas overlays must be multi-series, not redraw-over-redraw
For no-dependency canvas charts, do not draw read and then call a single-line chart function again for write; the second call clears the canvas and erases the first line. Use one renderer that accepts multiple series and computes shared bounds.

Also handle:
- `null` values
- constant values by padding bounds
- dynamic temperature bounds instead of fixed min that creates ugly flat bars
- resize redraw

### Secret settings: blank means keep saved
For tokens/webhooks in settings pages:
- render as password/empty input
- placeholder says `saved — leave blank to keep`
- never echo raw webhook/token into HTML
- API config should mask secrets
- test buttons should send the current form values, so a newly pasted webhook can be tested before/while saving

Backend test routes should accept override fields from JSON body:
```python
url = body.get("webhook_url") or body.get("discord_webhook_url") or cfg["discord"].get("webhook_url", "")
```

### Discord webhook via Python urllib may need User-Agent
Discord/Cloudflare can reject bare `urllib` POSTs with `HTTP 403: error code: 1010`. Add a reasonable `User-Agent` header to webhook requests:
```python
headers={
  "Content-Type": "application/json",
  "User-Agent": "<app>/<version> (+<repo-or-url>)",
}
```
Then verify with a real test message and a delivery-log row.

### Telegram 404 is usually token, not dashboard code
If Telegram `sendMessage` returns:
```text
HTTP 404: {"ok":false,"error_code":404,"description":"Not Found"}
```
that usually means the bot token / bot endpoint is wrong. Surface the exact API error in the UI and delivery log instead of treating it as a generic dashboard failure.

### Logs page should be operator-oriented
A log page that technically fetches text can still feel broken if it opens on stale traceback noise. Better defaults:
- newest lines first
- line-count selector
- all / warn+ / errors filter
- manual refresh
- copy button
- status chip: `N lines · M fresh errors / 10m · time`
- fresh-error count based on recent timestamps, not old historical tracebacks

### Alerts page should include delivery operations
For alert/notification dashboards, include:
- alert history
- notification delivery log
- refresh button
- per-channel test buttons
- visible `sent` / `failed` badges
- exact error text for failed deliveries

## Verification checklist

- [ ] Raw API pages return 200: `/logs/raw`, `/api/alerts`, `/api/notifications`, `/api/config`
- [ ] Settings page masks saved secrets in HTML
- [ ] Save preserves secrets when password fields are blank
- [ ] Test button uses typed-but-unsaved values when present
- [ ] Discord test sends a real message and writes a `sent` delivery row
- [ ] Telegram failure, if any, shows exact API error
- [ ] Browser console has no JS errors on Dashboard, Alerts, Logs, Settings
- [ ] Live process on the port is the freshly restarted process, not a stale survivor
