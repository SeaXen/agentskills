Read skill + all five reference files. Verdict first: **your ranking method broke, and it flipped the answer. Don't lock hobbyists as primary yet.**

## What's wrong, in order of size

1. **Raw sum instead of value ÷ effort.** Skill step 5.3: *"Rank by value per unit of effort, not by total score... show the division, so a reader can see which segment lost on the denominator rather than on merit."* Summing all seven lets three cheap-to-score criteria (size, reach, low effort) outvote weak value and fit. That's the exact trap named in the skill — automotive tier-one didn't lose on merit, it lost on one denominator (effort=3) getting added instead of divided.

2. **Funded driver never weighted the score.** Step 5.1: *"Weight before scoring."* You said the program is funded "explicitly to help sales close bigger deals" — that's the sales-enablement driver, and the skill states plainly: *"a program funded for sales enablement weights value and competitive position."* Your scorecard weighted all seven equally. Reweighted toward value and competitive position, automotive tier-one — the segment that actually produces "bigger deals" — gets heavier, not lighter.

3. **Hobbyists structurally can't satisfy the funding driver.** Independent hardware hobbyists are individual adoption, no purchase (decision-unit.md). There is no "sale" for a sales-enablement program to close there. A segment can carry no purchase only if justified by a named non-revenue driver — talent brand, contributor supply, future buyers, ecosystem gravity (decision-unit.md, "Segments with no purchase"). None of those was stated. Per that same section: *"Without one of these written down, the segment belongs in the anti-segment."* Right now, on the evidence given, hobbyists default to the anti-segment, not primary.

4. **Effort likely got double-counted against reach.** "Costs us nothing" reads like a reach/GTM-cost argument, but effort in this skill means something else: *"what must exist before this segment can succeed: SDK, docs track, compliance pack, integration."* Automotive tier-one's effort=3 is probably real — functional-safety qualification (ISO 26262-class), long OEM integration cycles. Hobbyists' effort score likely borrowed the same "cheap to reach" logic reach already captures, inflating the total a second time.

5. **1–10 is false precision.** Skill step 5.2: *"Score coarsely... 1-3 or high/medium/low. False precision invites arguing about a 6 versus a 7 instead of about the segment."* A whole primary-segment call is currently resting on one 3-out-of-10 effort score.

6. **No sizes, no decision units, given at all.** The scorecard has seven criteria scores but no size range+method+date+confidence, and no evaluator/approver/buyer per segment — both mandatory map fields, independent of the 1–10 scores.

None of this says hobbyists are wrong forever — it says the method that put them on top is the one the skill warns against by name, and the number it downgraded on (automotive tier-one's effort) is precisely the "promote anyway" case: *"The big, high-value, high-effort segment... loses every round it is ranked in [by ratio alone]... Promote it anyway when... the funded driver is sales enablement and no cheaper segment carries revenue at all."*

Below is the write-up, built on what you gave me. It's marked wherever your scorecard didn't supply data — I'm not inventing segments, sizes, or scores you didn't give me.

---

```
# Developer segment map — Vantablack Systems, H2 2026 (DRAFT — pending full scorecard)

## Cut
Dimensions: not confirmed. "Independent hardware hobbyists" and "automotive
tier-one suppliers" read as one firmographic/involvement axis (who the buyer
is). The second, reach-changing axis is not stated — confirm what it is
(workload? compliance regime? deployment scale?) before treating this as a
real two-dimension cut rather than a single labelled list.

## Segments

| Segment | Definition | Size + confidence | Decision unit | Needs | Evidence |
|---|---|---|---|---|---|
| Automotive tier-one suppliers | company adoption, functional-safety-qualified HIL test programs | NOT GIVEN | not stated — almost certainly: test/validation engineer evaluates, functional-safety/quality approver signs off, procurement is the economic buyer | qualification/compliance pack, long integration runway, named production references | NOT GIVEN — count data points before trusting the row |
| Independent hardware hobbyists | individual adoption, no purchase or near-zero-ticket purchase | NOT GIVEN | user = buyer, or no purchase at all | low-cost/entry hardware, community reach, near-zero support cost | NOT GIVEN |
| [3rd–5th segment] | — | — | — | — | PENDING: send the rest of the scorecard. Map needs 3-5 rows to clear the quality gate; two is not a map. |

## Primary — provisional, pending full scorecard
Automotive tier-one suppliers, on the funded driver (sales enablement — "help
sales close bigger deals"). Reasoning:
- Weighted for this driver, value and competitive position dominate the
  score, not size/reach/effort equally.
- Effort=3 is a real, known cost (compliance qualification, OEM integration),
  not a reason to drop a segment defined by exactly the kind of large,
  complex deal the program exists to close.
- Hobbyists cannot be "closed" by sales in the funded sense — no purchase,
  no deal size, no decision unit for a rep to work.
This is provisional: no size, decision-unit confirmation, or evidence count
was supplied for this segment. Confirm those before funding artefacts.

## Secondary
Not determined — depends on the missing rows 3-5.

## Anti-segment
Independent hardware hobbyists, unless a non-revenue driver is named and
written down (talent brand, contributor supply, future buyers, ecosystem
gravity — decision-unit.md). On a program funded explicitly for revenue
sales enablement, an unjustified free segment is the textbook case that
"quietly consumes the whole content budget" (skill step 4). If there IS a
real non-revenue reason to fund hobbyists this horizon, say it in one line
and this segment moves to secondary or its own tracked line — it does not
move to primary on a sales-enablement budget either way.

## Hypotheses
Both rows above are below the evidence floor until you confirm data-point
counts (5-10 independent points from a consistent group — interviews,
tickets, sales notes, telemetry). Until then, treat both as hypotheses, not
funded conclusions.

## Implications
Stop: building toward "hobbyists primary" as a funded decision — it doesn't
touch the metric the program is funded against.
Needed before this map is final: sizes (range + method + date + confidence)
for every segment, decision unit per segment, the second cut dimension, the
remaining 3+ segment rows, and coarse (not /10) re-scoring weighted toward
value and competitive position.

## Review
Not set — re-run once the gaps above are closed.

## Quality gate — reported as required by the skill
FAILS: segment count (2 of 3-5), size fields (none given), decision-unit
fields (none given), scoring scale (10-point, not coarse), driver weighting
(not documented), evidence floor (unknown). PASSES: funded driver is named
and specific.
```

---

Next: send the full scorecard (all segments, not just top/bottom) plus size ranges and decision units — I'll re-run the ranking properly and confirm whether automotive tier-one actually holds as primary or something else in the middle wins on value ÷ effort.