# Lightweight operator dashboard patterns

Session-derived patterns for low-CPU self-hosted dashboards like Systor.

## 1) Secret settings fields: mask in HTML, never reuse masks as real values
- Render saved Telegram bot tokens / Discord webhooks as blank password inputs with helper text like `saved — leave blank to keep`.
- Never put the real secret value back into the HTML.
- On save, ignore masked placeholder strings such as `123456:***` or other sentinel values; do not persist them as real credentials.
- Test buttons should serialize the current form values, not only the already-saved config, so a user can paste a new token/webhook and test before save.
- If a saved token is only a masked placeholder, surface that exact error in the UI instead of forwarding a vague upstream API failure.

## 2) Telegram formatting pitfall
- Telegram HTML parse mode rejects some markup patterns that look harmless in other channels.
- In this session, replacing escaped newlines with `<br>` broke delivery with `Unsupported start tag "br"`.
- Safer default for compact alert messages: bold subject line plus literal newline-separated body text.

## 3) Post-restart verification rule for self-hosted dashboards
- Old tracked web processes may emit delayed `exit -9` / `SIGTERM` notices after being replaced.
- Treat those notices as untrusted until the current listener and health endpoint are checked.
- Verify the live port owner, current PID, and `/health` before reporting a fresh outage.

## 4) Hide virtual interfaces by default on operator network pages
- For network tables, default-hide noisy interfaces such as `docker*`, `veth*`, `br-*`, and loopback.
- Add a visible checkbox toggle so the user can expand to all interfaces without losing access to the raw data.
- Show visible-vs-total counts in the table heading so the filter state is obvious.

## 5) Uniform dense chart headers
- For tight telemetry pages, use the same header geometry everywhere:
  - chart name on the left
  - bold live values / latest+peak meta on the right
  - no extra stacked subtitle row unless the user explicitly asks
- Keep RX/TX color semantics consistent across cards, chart headers, tooltips, and tables.

## 6) Lightweight self-monitoring card
- A cheap self-monitor card can be built from:
  - web PID `%CPU` / RSS via `ps`
  - collector PID `%CPU` / RSS via `ps`
  - dashboard storage footprint from DB + log file sizes
- Mini canvases are enough; do not add a heavy charting dependency just for internal service health.

## 7) Lightweight Apps page scope
- Host app CPU/RAM can be sourced cheaply from `/proc`/`ps`.
- Docker app CPU/RAM/network/block I/O can be sourced from `docker stats --no-stream`.
- Be explicit that per-host-process network/disk attribution is limited unless a heavier accounting path is introduced.
- It is acceptable to ship a first pass where host per-process CPU/RAM are real, Docker per-container net/disk are real, and host per-process net/disk remain zero/unknown.
