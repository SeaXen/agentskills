# TradingX — settings alerts column, runtime prefs, perf polling, social MVP

Condensed from live work on `/mnt/tb/1Apps/Tradingx` (LAN `:8799`, Docker `network_mode: host`, host-built standalone).

## Settings layout (Discord / notifications visible)

**User signal:** right column felt empty; Discord hard to find; remove verbose header (“Personal preferences…”, “saved locally”).

**Layout (xl: 3 columns):**

| Col 1 | Col 2 | Col 3 (alerts — fill height) |
|-------|-------|------------------------------|
| Display + theme | Account + trading | **Alert channels** status strip |
| Refresh + risk | Notification event toggles | **Discord** (first), Telegram, Webhook |
| | | Signal listener, Shortcuts, Data |

- **Discord first** in column 3 — not buried under generic webhook.
- **ChannelStatusBar** at top: fetch `/api/notifications/discord`, `telegram`, `webhook` once; show chips (configured + on/off).
- Drop header clutter: title **Settings** only; optional “✓ Saved” — no “N keys · localStorage”.

## Two settings stores (do not conflate)

| Store | Keys | Examples |
|-------|------|----------|
| `lib/settings.ts` + localStorage | Client UX | `defaultRefreshSec`, `pauseAllRefresh`, `liveWidgetsRefreshSec`, demo toggle |
| SQLite `settings` table + `/api/settings/runtime` | Server behavior | `sync_interval_min`, `browser_notifications`, `daily_review_reminder` |

Browser/daily-review toggles that only flipped `checked={false}` in JSX were **bugs** — wire to `POST /api/settings/runtime`.

**Exchange sync interval:** `scheduler.ts` reads `getSetting("sync_interval_min")` then `SYNC_INTERVAL_MIN` env. UI saves via runtime API; **cron interval applies after container restart** (document in UI).

## Dashboard CPU/RAM

**`lib/useVisibilityPoll.ts`:** `setInterval` only runs when `!document.hidden`; refetch on `visibilitychange` when tab returns.

Wire dashboard widgets (`PortfolioWidget`, `LivePositionsWidget`, `OpenOrdersWidget`):

```ts
const pollMs = Math.max(5000, (settings.liveWidgetsRefreshSec || 15) * 1000);
useVisibilityPoll(load, pollMs, auto && !settings.pauseAllRefresh);
```

**Server:** position manager boot interval **10s** (was 5s) — `lib/crypto/boot.ts`.

Settings additions: `pauseAllRefresh`, `liveWidgetsRefreshSec` (default 15).

## Social trading MVP (honest scope)

**Shipped:** `/social` + `/api/social` + `lib/crypto/social.ts` tables `social_profiles`, `social_follows`.

- Opt-in leaderboard (30d WR/P&L from local trades).
- Follow handles on **same server instance** only.
- **Not** exchange copy-trading — point users to Signal listener + Discord/Telegram for alert mirroring.

## Verification (Dr. Sagar standard)

After changes:

```bash
cd /mnt/tb/1Apps/Tradingx
rm -rf .next && npm run build && docker compose build && docker compose up -d --force-recreate
npm test && npm run typecheck
curl -s http://127.0.0.1:8799/api/social | head -c 200
curl -s http://127.0.0.1:8799/api/settings/runtime
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:8799/settings
```

Browser: scroll settings — **DISCORD** section + “Alert channels” strip; `document.body.innerText.includes('DISCORD')`.

## Related

- `references/client-settings-and-prefs.md` — localStorage store pattern.
- `references/webhook-notifications.md` — Discord webhook + `notify()` fan-out.