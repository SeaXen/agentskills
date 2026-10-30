#!/usr/bin/env python3
"""Project final registrations for an event from its pace curve, read against reference curves.

Usage:
    python3 forecast-registrations.py --actuals actuals.csv --reference ref.csv[@SHIFT] [--reference ...]
        [--event-date YYYY-MM-DD] [--as-of DAYS_OUT] [--target N] [--threshold N]
        [--capacity N] [--ceiling N] [--checkpoint NAME:DAYS_OUT ...]
        [--error-band FRACTION] [--types types.csv]

Inputs (CSV, header row required):
  --actuals     `days_out,cumulative` or `date,cumulative` (dates need --event-date).
                Cumulative registrations to date, net of comps. One row per reading.
  --reference   `days_out,cumulative`, repeatable. Either a prior edition's own counts
                (its doors-day value is its final) or a share curve with values in 0..1
                (for example assets/curve-pooled-lead-time.csv). Append `@N` to shift the
                reference N days: `@-7` when this year's milestone (early-bird close, speaker
                announcement) lands 7 days closer to doors than it did in the reference.
  --as-of       Project from the latest reading at or before this many days out, e.g. the
                last reading before a spike. Default: the latest reading.
  --types       `type,basis,amount,show_rate,label`. basis `share` = amount is a share of
                projected registrations (shares sum to 1); basis `count` = amount is a fixed
                count (comps, speakers). show_rate in 0..1. label says where the rate came from.
  --checkpoint  NAME:DAYS_OUT, repeatable (alias --lock): a lock date or a milestone.

Output: plain text. Per reference: expected share at the reading's days-out, pace index, the
multiplicative and additive projections, which one is used and why. Then the band
(low / mid / high), expected on-hand range at each checkpoint, the date the band crosses a
registration ceiling, threshold and capacity reads, and expected attendance by ticket type.
Read-only: the script writes nothing.
"""

import argparse
import csv
import datetime
import os
import statistics
import sys

# Below this share of the final already in, each registration of noise moves the
# multiplicative projection by more than 1/0.15 ~ 6.7 registrations, so early reads
# swing wildly. The additive projection is used instead when a count reference exists.
MIN_STABLE_SHARE = 0.15

# Additive pickup assumes the remaining volume matches the reference's. Once the event runs
# at under half or over double the reference's count at the same days-out, that assumption
# is visibly wrong, so the additive figure is flagged as a bound rather than a forecast.
ADDITIVE_TRUST_RANGE = (0.5, 2.0)

# A reference whose values never exceed this is read as a share curve (0..1), not counts.
SHARE_CURVE_MAX = 1.0

# A count curve ending at exactly 100 is more often a percent curve typed by hand.
PERCENT_CURVE_FINAL = 100.0

# Tolerance on ticket-type shares summing to 1, to absorb rounding in hand-written files.
SHARE_SUM_TOLERANCE = 0.01


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    sys.exit(2)


def read_rows(path):
    if not os.path.isfile(path):
        fail(f"file not found: {path}")
    with open(path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            fail(f"{path} is empty")
        rows = [{k.strip().lower(): (v or "").strip() for k, v in row.items() if k} for row in reader]
    if not rows:
        fail(f"{path} has a header but no rows")
    return rows


def to_float(value, path, column):
    try:
        return float(value)
    except ValueError:
        fail(f"{path}: column '{column}' holds a non-number: '{value}'")


def read_curve(path, event_date=None):
    """Return a list of (days_out, cumulative) sorted from far out to doors."""
    rows = read_rows(path)
    if "cumulative" not in rows[0]:
        fail(f"{path}: needs a 'cumulative' column")
    points = []
    for row in rows:
        if row.get("days_out", "") != "":
            days = to_float(row["days_out"], path, "days_out")
        elif row.get("date", "") != "":
            if event_date is None:
                fail(f"{path} uses dates; pass --event-date")
            try:
                day = datetime.date.fromisoformat(row["date"])
            except ValueError:
                fail(f"{path}: bad date '{row['date']}', expected YYYY-MM-DD")
            days = (event_date - day).days
        else:
            fail(f"{path}: each row needs 'days_out' or 'date'")
        if days < 0:
            fail(f"{path}: a reading after doors ({days:g} days out); drop post-event rows")
        points.append((days, to_float(row["cumulative"], path, "cumulative")))
    points.sort(key=lambda p: -p[0])
    for (d1, v1), (d2, v2) in zip(points, points[1:]):
        if v2 < v1:
            fail(f"{path}: cumulative falls from {v1:g} to {v2:g} between {d1:g} and {d2:g} days out; "
                 "net out refunds consistently or use gross counts throughout")
    return points


def value_at(points, days):
    """Linear interpolation on days-out. None when the curve does not cover that horizon."""
    if days > points[0][0] or days < points[-1][0]:
        return None
    for (d1, v1), (d2, v2) in zip(points, points[1:]):
        if d2 <= days <= d1:
            if d1 == d2:
                return v2
            return v1 + (v2 - v1) * (d1 - days) / (d1 - d2)
    return points[-1][1]


class Reference:
    def __init__(self, spec):
        path, _, shift_raw = spec.partition("@")
        self.shift = to_float(shift_raw, spec, "shift") if shift_raw else 0.0
        self.name = os.path.basename(path) + (f" shifted {self.shift:+g}d" if self.shift else "")
        raw = read_curve(path)
        if raw[-1][0] != 0:
            fail(f"{path}: the last row must be doors (days_out 0) so the final is known")
        self.final = raw[-1][1]
        if self.final <= 0:
            fail(f"{path}: final value is zero")
        self.is_share = max(v for _, v in raw) <= SHARE_CURVE_MAX
        self.suspect = not self.is_share and self.final == PERCENT_CURVE_FINAL
        if self.suspect:
            print(f"warning: {path} ends at exactly {PERCENT_CURVE_FINAL:g}; read as counts. "
                  "If it is a percent curve, divide it by 100.", file=sys.stderr)
        # Shift every point except doors, then clamp at doors: the final stays the final.
        shifted = [(max(d + self.shift, 0.0), v) for d, v in raw[:-1]]
        self.points = sorted(shifted + [raw[-1]], key=lambda p: -p[0])

    def count_at(self, days):
        return value_at(self.points, days)

    def share_at(self, days):
        value = self.count_at(days)
        return None if value is None else value / self.final


def project(reference, days, current, target):
    share = reference.share_at(days)
    if share is None:
        return None
    result = {"share": share, "bound": None}
    # Pace index = actual / curve-expected x 100, where curve-expected = target x share.
    result["pace"] = None if not target or share == 0 else 100.0 * current / (target * share)
    result["mult"] = None if share == 0 else current / share
    result["vs_ref"], result["additive"] = None, None
    if not reference.is_share:
        on_hand_then = reference.count_at(days)
        result["additive"] = current + (reference.final - on_hand_then)
        result["vs_ref"] = None if on_hand_then == 0 else current / on_hand_then
    if result["mult"] is not None and share >= MIN_STABLE_SHARE:
        result["used"], result["why"] = result["mult"], "multiplicative (enough of the curve is in)"
    elif result["additive"] is not None:
        result["used"], result["why"] = result["additive"], (
            f"additive (only {share:.0%} of the curve is in; multiplicative unstable)")
        ratio = result["vs_ref"]
        if ratio is not None and not ADDITIVE_TRUST_RANGE[0] <= ratio <= ADDITIVE_TRUST_RANGE[1]:
            bound = "upper" if ratio < 1 else "lower"
            article = "an" if bound == "upper" else "a"
            result["why"] += (f"; running at {ratio:.2f}x the reference, so additive is only {article} "
                              f"{bound} bound and stays out of the band")
            result["bound"] = f"{bound} bound"
    elif result["mult"] is not None:
        result["used"], result["why"] = result["mult"], (
            f"multiplicative, unstable (only {share:.0%} in, no count reference for additive); "
            "stays out of the band")
        result["bound"] = "unstable"
    else:
        result["used"], result["why"] = None, "reference expects zero by now; no projection"
    return result


def read_types(path):
    types = []
    for row in read_rows(path):
        for column in ("type", "basis", "amount", "show_rate"):
            if column not in row:
                fail(f"{path}: needs columns type,basis,amount,show_rate,label")
        basis = row["basis"].lower()
        if basis not in ("share", "count"):
            fail(f"{path}: basis for '{row['type']}' must be 'share' or 'count'")
        rate = to_float(row["show_rate"], path, "show_rate")
        if not 0 <= rate <= 1:
            fail(f"{path}: show_rate for '{row['type']}' must be between 0 and 1")
        types.append((row["type"], basis, to_float(row["amount"], path, "amount"), rate,
                      row.get("label", "") or "unlabelled"))
    share_total = sum(a for _, b, a, _, _ in types if b == "share")
    if share_total and abs(share_total - 1) > SHARE_SUM_TOLERANCE:
        fail(f"{path}: shares sum to {share_total:.2f}, expected 1.00 across the sold types")
    return types


def crossing_day(reference, final, ceiling):
    """Days out at which final x share first reaches the ceiling, None if never, inf if before the curve."""
    if final < ceiling:
        return None
    target_share = ceiling / final
    if reference.points[0][1] / reference.final >= target_share:
        return float("inf")
    for (d1, v1), (d2, v2) in zip(reference.points, reference.points[1:]):
        s1, s2 = v1 / reference.final, v2 / reference.final
        if s1 <= target_share <= s2:
            return d1 if s2 == s1 else d1 - (d1 - d2) * (target_share - s1) / (s2 - s1)
    return 0.0


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--actuals", required=True)
    parser.add_argument("--reference", action="append", required=True)
    parser.add_argument("--event-date")
    parser.add_argument("--as-of", type=float)
    parser.add_argument("--target", type=float, help="planned final registrations net of comps, for the pace index")
    parser.add_argument("--threshold", type=float, help="registrations the go/no-go criterion needs")
    parser.add_argument("--capacity", type=float, help="room limit in people, comps included")
    parser.add_argument("--ceiling", type=float, help="registration ceiling set by the no-show ratio")
    parser.add_argument("--checkpoint", "--lock", dest="checkpoint", action="append", default=[])
    parser.add_argument("--error-band", type=float, help="relative error from past forecasts, e.g. 0.2")
    parser.add_argument("--types")
    args = parser.parse_args()

    if args.error_band is not None and not 0 <= args.error_band < 1:
        fail("--error-band must be a fraction between 0 and 1, e.g. 0.2")

    event_date = None
    if args.event_date:
        try:
            event_date = datetime.date.fromisoformat(args.event_date)
        except ValueError:
            fail("--event-date must be YYYY-MM-DD")

    actuals = read_curve(args.actuals, event_date)
    if args.as_of is not None:
        usable = [p for p in actuals if p[0] >= args.as_of]
        if not usable:
            fail(f"no reading at or before {args.as_of:g} days out")
        days, current = usable[-1]
    else:
        days, current = actuals[-1]
    print(f"Projecting from: {current:g} registrations at {days:g} days out"
          + (f" (latest reading is {actuals[-1][1]:g} at {actuals[-1][0]:g} days out)" if (days, current) != actuals[-1] else ""))

    projections, bounds = [], []
    for spec in args.reference:
        ref = Reference(spec)
        res = project(ref, days, current, args.target)
        kind = "share curve" if ref.is_share else f"counts, final {ref.final:g}"
        if ref.suspect:
            kind += ", SUSPECT percent curve"
        if res is None:
            print(f"- {ref.name} ({kind}): does not cover {days:g} days out; skipped")
            continue
        if res["vs_ref"] is not None:
            kind += f", now at {res['vs_ref']:.2f}x its count at this days-out"
        fmt = lambda v: "n/a" if v is None else f"{v:.0f}"
        print(f"- {ref.name} ({kind}): expected share now {res['share']:.1%}, pace index {fmt(res['pace'])}, "
              f"multiplicative {fmt(res['mult'])}, additive {fmt(res['additive'])} -> uses {fmt(res['used'])}: {res['why']}")
        if res["used"] is not None and res["bound"] is None:
            projections.append((ref, res["used"]))
        elif res["bound"] is not None:
            bounds.append(f"{res['bound']} {res['used']:.0f} from {ref.name}")

    if bounds:
        print("Bounds only, not in the band: " + "; ".join(bounds))
    if not projections:
        fail("no usable projection: every reference is missing this horizon or gives only a bound; "
             "add a reference that covers it, or wait for more of the curve")

    values = sorted(v for _, v in projections)
    mid = statistics.median(values)
    no_band = False
    if len(values) > 1:
        low, high = values[0], values[-1]
        band_note = "spread across references (each end is one reference, never an average)"
        if args.error_band:
            low, high = low * (1 - args.error_band), high * (1 + args.error_band)
            band_note += f", widened by +/-{args.error_band:.0%} past forecast error"
    elif args.error_band:
        low, high = mid * (1 - args.error_band), mid * (1 + args.error_band)
        band_note = f"+/-{args.error_band:.0%} from past forecast error"
    else:
        low = high = mid
        no_band = True
        band_note = "NO BAND: one reference and no --error-band; every figure below is a point guess"
    print(f"\nProjected final registrations: low {low:.0f} / mid {mid:.0f} / high {high:.0f} ({band_note})")

    if args.checkpoint:
        print("\nCheckpoints (registrations expected on hand by then, if pace holds):")
    for spec in args.checkpoint:
        name, sep, raw = spec.rpartition(":")
        if not sep or not name:
            fail(f"--checkpoint '{spec}' must be NAME:DAYS_OUT")
        when = to_float(raw, "--checkpoint", name)
        if when > days:
            print(f"- {name} ({when:g} days out): before the reading projected from")
            continue
        expected = [final * ref.share_at(when) for ref, final in projections if ref.share_at(when) is not None]
        if expected and len(expected) == 1 and not args.error_band:
            print(f"- {name} ({when:g} days out): no range (one reference, no --error-band); point {expected[0]:.0f}")
        elif expected:
            band = args.error_band or 0.0
            print(f"- {name} ({when:g} days out): {min(expected) * (1 - band):.0f}-{max(expected) * (1 + band):.0f} on hand")
        else:
            print(f"- {name} ({when:g} days out): no reference covers this date")

    if args.ceiling:
        print(f"\nRegistration ceiling {args.ceiling:g}:")
        if current >= args.ceiling:
            print(f"- already reached: {current:g} on hand at {days:g} days out")
        else:
            for ref, final in projections:
                day = crossing_day(ref, final, args.ceiling)
                text = ("not reached" if day is None else "before the reference starts" if day == float("inf")
                        else f"reached about {day:.0f} days out")
                print(f"- {ref.name}: {text}")

    if args.threshold:
        verdict = ("low end clears" if low >= args.threshold else
                   "mid clears, low does not" if mid >= args.threshold else "mid misses")
        print(f"\nThreshold {args.threshold:g}: {verdict}")

    totals = None
    if args.types:
        print("\nExpected attendance by ticket type (low / mid / high):")
        totals = [0.0, 0.0, 0.0]
        for name, basis, amount, rate, label in read_types(args.types):
            regs = [amount] * 3 if basis == "count" else [low * amount, mid * amount, high * amount]
            att = [r * rate for r in regs]
            totals = [t + a for t, a in zip(totals, att)]
            print(f"- {name}: registrations {regs[0]:.0f} / {regs[1]:.0f} / {regs[2]:.0f}, "
                  f"show rate {rate:.0%} ({label}) -> attendance {att[0]:.0f} / {att[1]:.0f} / {att[2]:.0f}")
        print(f"Total expected attendance: {totals[0]:.0f} / {totals[1]:.0f} / {totals[2]:.0f}")

    if args.capacity:
        if totals:
            print(f"\nCapacity {args.capacity:g} (attendance incl. comps): low {totals[0] / args.capacity:.0%}, "
                  f"mid {totals[1] / args.capacity:.0%}, high {totals[2] / args.capacity:.0%}")
            if totals[2] > args.capacity:
                print("  High-end attendance exceeds the room: see the capacity steps.")
        else:
            print(f"\nCapacity {args.capacity:g}: pass --types to compare attendance; "
                  "registrations are not people in the room")
    if no_band and (args.capacity or args.ceiling or args.threshold):
        print("\nWARNING: the reads above rest on a point guess; add a second reference or --error-band "
              "before committing anything against them")


if __name__ == "__main__":
    main()
