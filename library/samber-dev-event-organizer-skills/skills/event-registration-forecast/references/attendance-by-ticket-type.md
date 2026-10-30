# Attendance by ticket type

Show rates to put in the `--types` file, each with its scope. Overbooking ratios built from these figures belong to `samber/dev-event-organizer-skills@event-no-show-management`; this file only feeds the attendance forecast.

## Sourced by price posture

| Population | Show rate | Source and scope |
| --- | --- | --- |
| Paid events | 90-97% | Event Tech Live, attributed industry band |
| Paid events, median | ~83% (17% no-show) | PheedLoop check-in data, 860+ events narrowed to a 195-event follow-up |
| Free events | 40-60% | Event Tech Live, attributed industry band |
| Free events, median | ~72% (28% no-show) | PheedLoop, same dataset |
| Free hackathon registrants | ~50% | MLH organizer guide, trendline across 323 events |

- The two sources disagree for both postures: paid by more than ten points, free by more (~72% median against 40-60%). Quote the one whose population matches yours, or run both as the band ends.
- Most of the free-versus-paid gap sits between events, not within one: within a single event, payment moved an individual's odds by about 2-4 points.

## By registration timing

PheedLoop Report #09 (467 events): pooled no-show climbs from 18% for registrations six months out to 42% for same-week ones, but within one event the median early-versus-late gap is 0.6 points. Early registrants still edged ahead at most events (84.1% against 80.8% median attendance across 374 events; late ones did better at 44%). The gap is small enough to apply one show rate per type regardless of when its registrants signed up.

## Types with no published rate

| Type | What to use | Label |
| --- | --- | --- |
| Speakers | Your own prior count; otherwise a high self-set rate, since a no-show leaves a hole in the grid | self-set |
| Sponsor staff passes | Your own count of passes claimed, then of badges collected; claimed passes can fall short of the allotment | self-set |
| Volunteers | Your own shift sign-in record | self-set |
| Scholarship or sponsored seats | One data point: 22 of 47 sponsored student tickets attended at one 2024 regional Python conference (47%), inside the free band | single event |
| Group and employer-bought tickets | Treat as paid until measured; no source splits show-up by who paid | hypothesis |
| Walk-ins | Your own prior count only | own data, or "unknown" |

Measure every self-set type at this edition's check-in, by type, so next edition's file carries own-data rates.

## Day-one desk load

Hand day-one attendance to `samber/dev-event-organizer-skills@event-attendee-experience`, which sizes the desk on the busiest arrival hour.
