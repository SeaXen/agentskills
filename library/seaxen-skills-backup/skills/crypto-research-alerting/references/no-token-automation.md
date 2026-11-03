# No-token automation pack

These features work without any extra LLM token or exchange API key.

## Scripts

- `scripts/sector_strength.py --text`
  - cross-sector summary for majors / AI / L1-L2 / RWA / memes
- `scripts/opportunity_digest.py --preset top50-trading --text`
  - Telegram-ready top-opportunity digest
- `scripts/daily_market_brief.py --preset majors --text`
  - no-model daily market brief
- `scripts/notification_digest.py --text --silent-if-none`
  - prints nothing when no price rules trigger; ideal for cron/no-agent watchdog jobs

## Dashboard UI

Added panels/buttons for:
- Sector Summary
- Daily Brief
- Auto-send Preview
- Telegram-ready Price Alert Digest

## Scheduling idea later

Good cron patterns when the user asks to enable delivery:
- `notification_digest.py --text --silent-if-none` every 10m
- `opportunity_digest.py --preset ai --text` every 2h
- `daily_market_brief.py --preset majors --text` at 09:00 daily

These are deliberately rule/script based, not model based.
