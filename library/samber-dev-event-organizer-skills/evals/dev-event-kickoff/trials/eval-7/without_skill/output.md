I haven't created any check-ins yet. Two things block that, and I need one date from you.

## What I found

- ✅ **Claude Code scheduler:** it has no jobs, so last year's reminders aren't there.
- ⚠️ **Other schedulers:** I couldn't check them. My attempt to list system cron and launchd agents wasn't approved, so I haven't looked. Last year's reminders are probably in one of these places:
  - user crontab (`crontab -l`)
  - `~/Library/LaunchAgents`
  - GitHub Actions `schedule:` triggers
  - calendar recurring events
  - the ticketing platform's own alerts
  - a Slack or Notion reminder bot
- ⚠️ **Don't delete them blindly.** Some may still be useful. A job that still points at edition 2 dates, or at a stale channel, is worse than none, because it sends false alarms. List them and decide per job: retarget, then delete the rest.
- ❌ **Claude Code cron is the wrong tool for a nine-month horizon.** Recurring jobs expire after 7 days and only fire while a session is open. Durable mode survives restarts, but the 7-day limit still applies. I'd use a calendar or CI schedule and use Claude only for the weekly review prompt.

## Needed from you

The exact **event start date**. "About nine months out" isn't enough, because every deadline below is computed from it.

For a rough guide: the event lands around mid-July 2027. That puts the fee steps near mid-March (T-120), mid-April (T-90) and late May (T-45). The CFP closes around mid-February 2027. Treat these as placeholders until you give me the date.

## Proposed check-ins

You asked for as many as it takes. I'd cap this at about 10, tiered. At 30 alerts, the one that matters gets ignored.

**Hard deadlines (one-shot, each with an escalation ladder)**

| # | Check-in | Fires | Question it asks |
|---|---|---|---|
| 1 | Fee step T-120 | T-150, T-135, T-121 | Is the go/no-go made? What do we owe if we cancel tomorrow? |
| 2 | Fee step T-90 | T-120, T-105, T-91 | Same, with the new fee. Are ticket sales on track against the break-even? |
| 3 | Fee step T-45 | T-75, T-60, T-46 | Last cheap exit. Is the attendance and sponsor commitment locked? |
| 4 | CFP close | T-30d, T-14d, T-3d, close day | Submission count against target? Is there a speaker-outreach push? |
| 5 | Doors announce date | T-14d, T-3d | Are the announcement assets, site and press list ready? |

Pull the fee dates from the **signed contract**, not from my arithmetic. Check whether "120 days before" counts from the first or last day of the event.

**Recurring pulses**

| # | Check-in | Cadence | Question it asks |
|---|---|---|---|
| 6 | Ticket sales | Weekly now, daily in the last 3 weeks before each fee step | Sales against the curve? Any refunds or fee anomalies on the platform? |
| 7 | CFP funnel | Weekly until close | Submissions, quality, diversity of topics and speakers |
| 8 | Budget and contract | Monthly | Spend against plan, open vendor items, sponsor payments |
| 9 | Open-loop sweep | Weekly (Monday) | What's owed to whom, and what has no owner? |
| 10 | Edition-2 retro carryover | One-off, next week | Which lessons from last year are still unaddressed? |

## Next steps

1. Send me the event start date and tell me where the reminders should go: email, Slack, calendar, or all three.
2. Run `crontab -l`, `ls ~/Library/LaunchAgents` and a search of your CI workflows for last year's reminders. Paste the output, or approve my running those commands. I'll then sort each job into keep, retarget or delete.
3. I'll generate the 10 jobs with exact dates, with the three fee-step ladders first, since they carry real money.