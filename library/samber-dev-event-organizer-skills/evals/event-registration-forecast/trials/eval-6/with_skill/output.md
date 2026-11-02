# Signalhaus Conf: attendance numbers

I read the skill and its attendance and lock-date references. I did not run the script, because you gave no registration pace curve. I took your band (420 / 480 / 560, net of comps) as given. The method is booking-curve pickup forecasting borrowed from hotel and airline revenue management. It is not an established event-specific method.

## Assumptions

- ⚠️ **Show rate: 79.8% for every sold type.** This is own-data: last year 455 scanned − 52 comps = 403, and 403 / 505 = 79.8%. It is blended because you have no per-type split. Scans may miss some attendees, so treat it as a floor.
- ⚠️ **Speakers 95% and volunteers 90%.** Both are self-set. You gave no last-year speaker or volunteer counts, and no published rate exists for either type.
- ℹ️ **Sponsor staff: 31 of 60 allotted, own-data.** Last year 44 were claimed, and 31 of those 44 badges were collected. The count of 31 is 52% of the allotment, so I used 31, not 60 or 44.
- ⚠️ **Group tickets: treated as paid**, which is a hypothesis. No source measures show-up by who paid.
- ⚠️ **Walk-ins: unknown.** You gave no walk-in count from last year, and generic curves stop at doors. I include none.
- ⚠️ **Day two: unknown.** You did not scan it.
- ⚠️ **Catering lock date and flex were not given.** I assume no flex, so I divide by nothing.

## Attendance by ticket type, day one

| Type | Basis | Rate (label) | Low | Mid | High |
| --- | --- | --- | --- | --- | --- |
| Standard (70%) | 294 / 336 / 392 | 79.8% (own-data) | 235 | 268 | 313 |
| Student (20%) | 84 / 96 / 112 | 79.8% (own-data) | 67 | 77 | 89 |
| Group (10%) | 42 / 48 / 56 | 79.8% (own-data, hypothesis) | 34 | 38 | 45 |
| **Sold subtotal** | 420 / 480 / 560 | | **335** | **383** | **447** |
| Speakers | 45 | 95% (self-set) | 43 | 43 | 43 |
| Volunteers | 25 | 90% (self-set) | 23 | 23 | 23 |
| Sponsor staff | 60 allotted | 31 collected (own-data) | 31 | 31 | 31 |
| **Comps subtotal** | 130 | | **96** | **96** | **96** |
| **Day-one attendance** | | | **431** | **479** | **543** |

Comps make up 96 of the 479 mid attendees, so they matter.

Your 52 scanned comps last year compare with 96 expected this year. I can't check that gap without last year's speaker and volunteer counts. If you can send them, I will replace the self-set rates.

## Caterer

- **Day-one lunch: commit toward the high end, 543.**
  - One missing lunch leaves a person unfed, and one spare lunch costs one cover, so short is the more expensive mistake.
  - If the caterer allows a flex of x% after the lock, commit 543 / (1 + x) and keep the flex for a surge.
  - That figure is provisional. Re-run the forecast on the lock date and commit that run's figure.
  - If every claimed sponsor pass turned up (44 instead of 31), add 13.
- **Day-two lunch: unknown, so I give no forecast.** Reusing day one would be a guess, because day two can draw fewer people.
  - The only defensible number is an upper bound of 543, which means everyone returns. It is a ceiling, not an expectation.
  - Ask the caterer when day two locks and whether it can scale down.
  - If it locks after day one, set it from the day-one scan by ticket type.
  - Scan day two this year. That makes next year's day-two number your own data.
- ❌ **Do not give the caterer the same number for both days.**

## Your co-organizer's plan

| Proposal | Verdict |
| --- | --- |
| 85% across the board | ❌ Your own data says 79.8% for sold tickets. At 480 that is 408 against 383, an overstatement of about 25. It also applies a sold-ticket rate to comps, which have different rates (sponsor staff 52%, speakers about 95%). |
| 60% for last-two-weeks buyers | ❌ Within one event, late registrants show up at practically the same rate as early ones. The gap in pooled data comes from which events sell late. Apply one rate per ticket type. |
| Add 10% walk-ins | ❌ Walk-ins can be forecast only from your own prior count, and you have none. Measure them this year, and record the count by ticket type. |
| Same number for both days | ❌ Forecast each day separately. Day two is unknown today. |

## Next step

If the lock dates, the caterer's flex, last year's comp counts and the room capacity are available, I can finalise the commit figures. A capacity check needs the room limit. Hand the day-one attendance to `event-attendee-experience` for desk sizing.