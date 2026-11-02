**Using devrel-metrics to build this. I made no edits and read nothing under skill-wip/.**

## 1. Site one-liner

> **Between Editions: a conversation every other Thursday, from the people who make [conference name], until the next edition.**

Alternative that leads with the benefit:

> **Between Editions keeps the conference conversation going, one episode every two weeks.**

Fill in the bracket and the audience. I don't know either one.

## 2. Public commitment

Commit only to what Tomas controls: the schedule.

> **One new episode every other Thursday, from [month] to [month]. We pause for the [conference] run-up and say so on this page.**

- Tomas has about 3 hours a week, so each episode gets about 6 hours. Booking, recording, editing and publishing must fit in that.
- Record 3 episodes before you announce. That gives a buffer.
- Don't publish the subscriber targets or the drop rule. A public number you can't control becomes a public miss.

## 3. KPI sheet

**Driver:** the show exists to keep the audience warm between editions and sell tickets for the next one.
**Spine:** driver-anchored. Seven metrics, and the first six each have one owner and one action.

| # | Metric | Definition and source | Baseline | Threshold | Owner | Action |
|---|---|---|---|---|---|---|
| 1 | **Schedule kept** | Episodes published on the announced date ÷ episodes scheduled. Announced pauses are excluded. Source: publish log. | n/a | 100% in season (`baseline`) | Tomas | Three misses in a row triggers the drop rule below. |
| 2 | **Hours per episode** | Tomas's logged hours per episode. | baselining (first 3 episodes) | median ≤ 6 h (`baseline`, from 3 h/wk × 2 weeks) | Tomas | If the median exceeds 6 h, move to monthly before the public announcement. |
| 3 | **Unique listeners per episode at 30 days** | Host analytics. | baselining | direction: flat or rising; set the range after 3 periods (`baseline`) | Tomas | A drop of more than 2 SD below the trailing mean triggers a format or guest review. |
| 4 | **Net subscriber change per quarter** | Subscribers at quarter end minus subscribers at quarter start. This is a period delta, never the total. | baselining | positive; set the range after 3 quarters (`baseline`) | Co-founder | If it is flat for two quarters, change distribution (guest cross-posting, clips). |
| 5 | **Return rate (counter-metric to #4)** | 30-day plays per episode ÷ subscribers. | baselining | no falling trend while #4 rises (`baseline`) | Co-founder | If #4 rises while #5 falls, the growth is thin. Stop paying for or pushing volume. |
| 6 | **Ticket buyers who name the show** | Buyers who pick the show at checkout ("How did you hear about us?") or use a show promo code, per edition. Report as a raw count. | baselining (first edition) | direction: up edition over edition (`baseline`) | Co-founder | If the count is flat after 2 editions, add a ticket call-to-action to every episode or reconsider the show's role. |
| 7 | **Listener-to-ticket rate** | Metric 6 ÷ unique 30-day listeners in the sales window. | baselining | none yet | Co-founder | Report only once metric 6 is at least 30. Below 30, show the raw list with dates, not a percentage. |

Metric 7 is a rough rate, not a conversion in the funnel sense. Listeners are anonymous, so the denominator is an estimate.

**Why the thresholds are all `baseline`:** I have no history for the show, so I set no growth percentages. Any round number I gave you would be folklore. Set the real ranges after 3 periods.

## 4. Your co-founder's three asks

1. **Subscriber growth targets.** I kept the metric as a quarterly change and paired it with metric 5. A total only goes up, so it can't tell you the show is failing. A growth target without a quality pair gets hit with thin audience.
2. **Listener-to-ticket conversion.** I kept it but demoted it to a rate reported only when there are 30 or more attributed buyers. A conference with fewer attributed buyers than that gets swung by single purchases. The count (metric 6) is the primary.
3. **Drop the show after three missed episodes in a row.** I kept it with a tighter definition:
   - A "miss" is a scheduled episode, not an announced pause. Without that, the conference run-up triggers it automatically.
   - Three consecutive misses means about 6 weeks of silence on a biweekly schedule.
   - On the third miss, hold a go/no-go review within 2 weeks. Drop the show unless Tomas gets more hours or the cadence changes.
   - Keep this rule internal.

## 5. Attribution rule

Write this down before the first edition's sales window opens.

- **Method.** One self-reported checkout question plus one show-specific promo code, mentioned in every episode. The promo code is valid for the whole sales window.
- **Wording.** Call the result "influenced by the show", never "sourced". Other channels share credit.
- **Direct and unlabeled traffic.** A large "direct" bucket is normal. Podcast apps strip referrers, so don't treat it as a bug.
- **Lag.** Ticket sales lag listening. Metrics 1 to 5 carry the interim.

## 6. Known blind spots

- Podcast hosts report downloads, not people. Metric 3 depends on how your host counts.
- Word-of-mouth listeners who buy a ticket without picking the show are missed.
- No history exists for any metric. Everything is "baselining" until 3 periods have passed.
- Tomas's hours outside the pause window are a stated estimate, not measured. Metric 2 tests it.

## 7. Review

- **Monthly:** metrics 1 and 2.
- **Quarterly:** metrics 3 to 5.
- **Per edition:** metrics 6 and 7.
- **Kill rule:** remove any metric that hasn't changed a decision in 2 review cycles.

**Next, under 2 minutes:** pick the real conference name and fill the brackets in the one-liner and the commitment line.