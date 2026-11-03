# iCalendar (.ics) Export

Generate standards-compliant RFC 5545 calendar feeds that import cleanly into Apple Calendar, Google Calendar, Outlook, Thunderbird, and phone calendars. Useful for: economic calendars, event reminders, scheduled jobs (DCA buys, expiry dates), billing cycles.

## File shape

A complete `.ics` file:

```
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//YourApp//Feature Name//EN
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:YourApp Calendar Name
X-WR-CALDESC:Description shown in clients
X-WR-TIMEZONE:America/New_York
BEGIN:VEVENT
UID:2026-06-15-FOMC@yourapp.local
DTSTAMP:20260623T040400Z
DTSTART:20260615T180000Z
DTEND:20260615T183000Z
SUMMARY:FOMC rate decision
DESCRIPTION:Press conference 30 min after. Watch dot plot.
CATEGORIES:FED
URL:https://www.federalreserve.gov/
END:VEVENT
END:VCALENDAR
```

Critical formatting rules:
- **CRLF line endings** (`\r\n`), not just `\n`
- **Fold lines** longer than 75 octets with `\r\n ` (CRLF + space) — most modern clients tolerate longer, but stay safe
- **Escape** commas, semicolons, backslashes, and newlines in TEXT properties: `\,`, `\;`, `\\`, `\n`

## Response headers

```ts
return new Response(ics, {
  headers: {
    "Content-Type": "text/calendar; charset=utf-8",
    "Content-Disposition": `attachment; filename="yourapp-2026-06-12mo.ics"`,
    "Cache-Control": "public, s-maxage=3600, stale-while-revalidate=7200",
  },
});
```

The `Content-Disposition: attachment` makes the browser download; `inline` makes it open in a subscribed calendar. For "Export to my phone calendar" UX, `attachment` is what users expect.

## Date format helpers

```ts
function pad(n: number): string { return String(n).padStart(2, "0"); }

// UTC timestamp: YYYYMMDDTHHMMSSZ
function fmtIcsTime(d: Date): string {
  return `${d.getUTCFullYear()}${pad(d.getUTCMonth() + 1)}${pad(d.getUTCDate())}T${pad(d.getUTCHours())}${pad(d.getUTCMinutes())}00Z`;
}
```

## ET → UTC conversion with DST

Most US macro events (FOMC, CPI, NFP) are scheduled in US Eastern. Convert ET to UTC before emitting. Coarse DST table is enough for calendar export — clients will display the local time correctly if you tag with `TZID`, but the Z-suffix UTC form is the most portable and the least surprising.

```ts
function isEasternDst(year: number, month: number, day: number): boolean {
  // US DST: 2nd Sunday of March (>= 02:00) to 1st Sunday of November
  if (month < 2 || month > 10) return false;
  if (month > 2 && month < 10) return true;
  // Edge months
  const first = new Date(year, month, 1);
  const firstSunday = 1 + ((7 - first.getDay()) % 7);
  const secondSunday = firstSunday + 7;
  if (month === 2) return day >= secondSunday;
  // November: DST ends at the FIRST Sunday
  return !(month === 10 && day < secondSunday);
}

function eventToUtc(date: string, time: string): Date {
  // date = "YYYY-MM-DD", time = "HH:MM" (in ET) or "" for all-day
  const [y, mo, d] = date.split("-").map(Number);
  if (!time) {
    // All-day: noon UTC as stable marker
    return new Date(Date.UTC(y, mo - 1, d, 12, 0, 0));
  }
  const [h, mi] = time.split(":").map(Number);
  const offsetHours = isEasternDst(y, mo - 1, d) ? 4 : 5;
  return new Date(Date.UTC(y, mo - 1, d, h + offsetHours, mi, 0));
}
```

For all-day events (no time), the spec says to use a DATE-only `DTSTART;VALUE=DATE:YYYYMMDD` form, but `YYYYMMDDTHHMMSSZ` with noon UTC is widely accepted and works in all major clients. Pick one and be consistent.

## Required vs optional VEVENT fields

Required (clients warn if missing):
- `UID` — must be globally unique and stable across regenerations
- `DTSTAMP` — when the iCal object was created (UTC, Z-suffix)
- `DTSTART` — when the event starts
- `SUMMARY` — short title shown in list view

Optional but useful:
- `DTEND` — for timed events, 30 min default is sensible; for all-day, set to 24h after start
- `DESCRIPTION` — long text, supports `\n` for line breaks
- `LOCATION` — venue / address
- `URL` — link to more info (great for "view source" links)
- `CATEGORIES` — comma-separated, used by clients for filtering
- `RRULE` — for recurring events (FREQ=DAILY|WEEKLY|MONTHLY etc.)

## UID pattern

Make UIDs deterministic so re-importing doesn't create duplicates:

```ts
const uid = `${date}-${title.replace(/[^A-Za-z0-9]/g, "")}@yourapp.local`;
```

The `@yourapp.local` suffix is a valid email-shape namespace. Use a real domain you own if you have one.

## DTEND for timed events

Default to 30 min for typical event-style items (announcements, briefings) and 1h for all-day markers. Adjust per event type. A `DTEND` that equals `DTSTART` is technically valid but some clients hide zero-duration events.

## Common pitfalls

- **No CRLF** — Mac calendar apps silently break with LF-only
- **Unescaped commas in SUMMARY** — "CPI release, all day" breaks Apple Calendar parsing
- **Floating local time without TZID** — emits `DTSTART:20260615T140000` (no Z). Different clients in different timezones show different things. Either use Z (UTC) or `DTSTART;TZID=America/New_York:20260615T140000`.
- **Missing DTSTAMP** — Outlook rejects the event
- **Re-using the same UID** — re-import creates a single event but the client updates the description/times silently. If you regenerate the feed (e.g. adding new events), keep UIDs stable for old events.

## Verify

```bash
curl -s "http://localhost:PORT/api/your-feature/export.ics" | head -c 400
```

Look for:
- Starts with `BEGIN:VCALENDAR`, ends with `END:VCALENDAR`
- Each event has UID, DTSTAMP, DTSTART, SUMMARY
- CRLF between lines (visible in `head -c 400 | xxd | head`)

Online validators:
- https://icalendar.org/validator.html — paste the .ics content
- Google Calendar: Settings → Import & export → Select file → Import. Failed imports tell you which line broke.
