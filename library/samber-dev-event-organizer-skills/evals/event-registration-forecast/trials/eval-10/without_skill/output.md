# Tidewater Cloud Summit: where we stand

I can't give you a number yet. The weekly rows didn't come through in your message, only the description. Below is the cleanup and the verdict logic, so the answer is a few subtractions once you paste the rows. The "12% behind" is wrong in two ways, and they push in opposite directions.

## 1. The 12% compares two different points in the sales cycle

- This year's event is 2026-12-10, so October 1 is **70 days out**.
- Last year's event was 2025-12-03, so October 1 was **63 days out**.
- The like-for-like point last year is **2025-09-24** (also 70 days out).

Last year's October 1 sits a week later in the cycle. Registrations usually speed up near the event, so last year's October 1 is probably higher than its 70-days-out value. **Aligning by days-to-event makes this year look better than 12% behind.**

## 2. This year's numbers are gross, last year's are net

You're comparing this year's gross figure with last year's net figure. That overstates this year.

| Adjustment | Amount | Caveat |
|---|---|---|
| Speaker and sponsor codes | −28 | Subtract only those redeemed on or before the comparison date. A code redeemed in November doesn't belong in the October 1 number. |
| Cancellations | −14, but probably −11 | The holiday week already shows 161 → 158, so at least 3 refunds are already netted out. Subtracting all 14 would double-count them. Confirm how many cancellations are still in the gross series. |

**Total adjustment: −28 and between −11 and −14, so about −39 to −42** for a date after all of them have occurred.

Check one more thing: whether any of the 14 cancellations were speaker or sponsor codes. If so, the two adjustments overlap and you'd subtract too much.

## 3. What the gap really is

Let L be last year's net count at 70 days out (2025-09-24), and T this year's gross count at 70 days out (2026-10-01).

```
net_this_year = T − (codes redeemed by 10/01) − (cancellations not yet netted by 10/01)
gap % = (net_this_year / L − 1) × 100
```

If you simply keep the 12% (T = 0.88 × L), the cleanup alone worsens the gap by about **(39 to 42) ÷ L** points.

Illustrative only, since I don't have your L:

| L (last year, net) | Cleanup alone | Gap |
|---|---|---|
| 250 | −39 to −42 | about 28–29% behind |
| 400 | −39 to −42 | about 22% behind |
| 600 | −39 to −42 | about 19% behind |

The date alignment from section 1 then pulls the gap back toward zero. Which effect wins depends on how steeply last year's curve rose between September 24 and October 1.

## 4. Fixing the date mismatch

1. Convert every row to days-to-event: `event_date − week_date`.
2. Interpolate each year's cumulative count linearly to 70 days out, since the weekly rows won't land on October 1 exactly.
3. Apply the adjustments, using the date each code was redeemed and each refund was issued. Don't subtract the totals wholesale.
4. Repeat at 63, 56, 49 and 45 days out. Today (2026-10-26) is **45 days out**, which is more informative than October 1.

The 45-days-out comparison matters most. Last year's value at that point is about 2025-10-19, and you have this year's actual data for it.

## 5. What to tell your co-organizer

- "12% behind" mixes gross with net, and mixes 70 days out with 63 days out.
- On a net, like-for-like basis the true gap is **not 12%**. I expect it to be smaller after date alignment and larger after the net adjustment.
- Use the 45-days-out comparison as the headline. It's current, and it's the only one with no extrapolation.

## What I need from you

1. Both weekly series, with date and cumulative count.
2. The date of the holiday week, to confirm which refunds it already reflects.
3. The redemption dates of the 28 codes and the dates of the 14 cancellations, even if approximate by week.
4. Whether any cancellations were code-holders.

With those I'll return the exact net gap at 70, 63 and 45 days out, plus a projection to 2026-12-10 using last year's final-weeks curve.