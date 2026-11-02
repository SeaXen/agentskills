Change the published time before you announce anything. "15:00 Lisbon time / 14:00 UTC" is wrong from the first call onward.

## 1. Fix the time label

Lisbon is UTC+0 in winter and UTC+1 in summer, and its clocks go back on Sun 25 Oct 2026. Your two labels agree only in summer.

| Period | 15:00 Lisbon equals |
|---|---|
| Until 25 Oct (summer) | 14:00 UTC |
| 25 Oct to 28 Mar 2027 (winter) | 15:00 UTC |

The first Wednesday call, 28 Oct, falls in winter. A reader who trusts "14:00 UTC" arrives an hour early, and one who trusts "15:00 Lisbon" is on time. The label contradicts itself for about five months.

Fix:
- Publish one anchor: "Wednesdays, 17:00 Lisbon time". Drop the UTC figure.
- Link a calendar invite whose timezone is `Europe/Lisbon`. It follows DST on its own.
- Add a "convert to your timezone" link.

## 2. The 15:00 slot does not work for the US West

15:00 Lisbon is 10:00 New York (5 hours behind) for most of the year. It is also 07:00 in San Francisco. You said the US is roughly even East and West, so about 31% of users are on the West Coast. Here is who the 15:00 slot reaches:

| Group | Share | Local time at 15:00 Lisbon |
|---|---|---|
| US East | ~31% | 10:00 (fine) |
| US West | ~31% | 07:00 (poor) |
| Europe | 22% | 16:00 CET (fine) |
| India | 9% | 19:30 (summer) / 20:30 (winter) IST (OK) |

"Suits everyone on the US side" holds for half of it.

## 3. Better main slot: Wednesday 17:00 Lisbon

| Group | Local time |
|---|---|
| US East | 12:00 |
| US West | 09:00 |
| Europe | 18:00 CET |
| India | 21:30 (summer) / 22:30 (winter) IST |

It reaches both US coasts (~63%) and Europe after work (22%). It costs you India, which the second slot covers. If 12:00 ET is too much of a lunch hour, use 16:00 Lisbon (11:00 ET / 08:00 PT). I would not go earlier than that.

## 4. The Europe-morning slot: right idea, wrong reason

The main slot already lands in the European afternoon, so Europe is not underserved. India is the group with no good time. A Wednesday 10:00 Lisbon slot gives:

| Group | Local time |
|---|---|
| Europe | 11:00 CET |
| India | 14:30 (summer) / 15:30 (winter) IST |
| US | 05:00 or earlier (nobody) |

That covers about 31% of users (Europe plus India) who are poorly served today. Pitch it as "Europe and India", since India is the real gap.

## 5. Make the alternate-week cadence predictable

- "Alternate weeks" drifts across months and is hard to publish. Use a calendar rule such as "1st and 3rd Wednesday of the month".
- With two hosts, the second slot doubles your call load. Run only the US slot for the first 4 to 6 weeks and track attendance by region.
- Add the morning slot only if Europe and India attendance shows demand. Drop-in calls split a small audience, so two thin calls can beat one healthy one only if demand is there.

## 6. DST shifts: tell attendees

If you anchor on Lisbon time, US attendees see a one-hour shift in the weeks when the US and EU clocks disagree. In 2026 and 2027 those Wednesdays are:
- 28 Oct 2026. 17:00 Lisbon is 13:00 ET / 10:00 PT that day.
- 11, 18 and 25 Mar 2027. Same shift (the US changes clocks on 14 Mar, the EU on 28 Mar), so confirm those dates against the calendar when you publish the schedule.

The 28 Oct call is your launch call. Note the shift on the announcement.

## 7. Check what "active users" means

For a connection pooler, "active users" may be deployed instances. Their IP location would then be the cloud region (us-east, us-west), not where the developer sits. If so, the US share is overstated and the Europe share understated. Check how that 63% is measured before you build the schedule on it. A short survey on the community page would settle it.

## Recommended plan

1. Publish "Wednesdays 17:00 Lisbon time (12:00 New York / 09:00 San Francisco)", with a `Europe/Lisbon` invite. No UTC figure.
2. Launch on 28 Oct and note the one-hour shift for that date.
3. Hold off on the second slot. After 4 to 6 weeks, add "1st and 3rd Wednesday 10:00 Lisbon" for Europe and India if the numbers support it.

Next action (2 minutes): confirm whether the 63% comes from user IPs or from deployed instances.