# One-page exec template and worked example

## Contents

- [Template](#template)
- [Worked quarterly example](#worked-quarterly-example)
- [Weak versus strong](#weak-versus-strong)

## Template

```markdown
# DevRel - <period> - for <reader>

<Headline: what the program moved for <reader goal>, in one sentence.>
Decision asked: <one decision>, by <date>.

## Results table

| Spine unit (goal, stage or bet) | Metric (framework) | This period | Baseline / threshold | Status | Label |
| ------------------------------- | ------------------ | ----------- | -------------------- | ------ | ----- |

## Leading indicators carrying slow outcomes

| Lagging outcome | Leading indicator | Expected lag | Pull-through so far | Label |
| --------------- | ----------------- | ------------ | ------------------- | ----- |

## What did not work

| Metric or bet                                                   | What happened | Likely cause | What changes | Next read |
| --------------------------------------------------------------- | ------------- | ------------ | ------------ | --------- |
| Dropped since last time: <metric - kill-rule reason, or "none"> |

## Cost per outcome

Program cost <amount> (salaries <in / out>). Cost per <outcome>: <amount> (<label>),
against <the funder's alternative>: <amount> (<source>).

## Decision asked

<Decision>. Options: <A>, <B>. Recommendation: <A>, because <one reason>. Needed by <date>.

---

Appendix: metric definitions · attribution rule as written in the framework · blind spots ·
activity: <one line of counts>
```

## Worked quarterly example

Fictional: a Series B observability API, self-serve plus an enterprise tier, three-person DevRel team reporting to the CMO. The framework already exists; its primary is first-success rate, with influenced pipeline as the business-impact row.

```markdown
# DevRel - Q3 - for the CMO

First-success rate in the cohort that used DevRel's rewritten quickstart rose from 31% to 38%,
the step that feeds the activation goal you own; enterprise pipeline influenced by DevRel is still two quarters from reading.
Decision asked: keep the docs engineer funded through Q1 instead of moving the role to
campaigns, by 15 November.

## Results table

| Reader goal                | Metric (framework)                    | This period | Baseline / threshold | Status            | Label                         |
| -------------------------- | ------------------------------------- | ----------- | -------------------- | ----------------- | ----------------------------- |
| Self-serve activation +20% | first-success rate, quickstart cohort | 38%         | 31% / 33-36% band    | green             | influenced (touched cohort)   |
| Enterprise pipeline        | pipeline influenced, 180-day rule     | $410k       | baselining           | none (baselining) | influenced, shared with sales |
| Lower support load         | tickets per 100 new signups           | 9.1         | 11.4 / under 10      | green             | measured                      |

## Leading indicators carrying slow outcomes

| Lagging outcome     | Leading indicator                      | Expected lag | Pull-through so far               | Label      |
| ------------------- | -------------------------------------- | ------------ | --------------------------------- | ---------- |
| Enterprise pipeline | DevRel qualified leads routed to sales | 1-2 quarters | 6 of Q1's 40 now opportunities    | influenced |
| 90-day retention    | first-success rate                     | 1 quarter    | link unproven, first read January | measured   |

## What did not work

| Metric or bet  | What happened                                    | Likely cause                       | What changes                               | Next read |
| -------------- | ------------------------------------------------ | ---------------------------------- | ------------------------------------------ | --------- |
| Webinar series | 3 sessions, 41 live attendees, 2 qualified leads | topic chosen by us, not by tickets | next 3 topics taken from top ticket themes | December  |

Dropped since last time: blog sessions - no decision changed in two cycles (kill rule).

## Cost per outcome

Program cost $96k this quarter (salaries out). Cost per developer in the quickstart cohort
reaching first success: $41 (influenced, touched cohort), against $118 per developer
reaching first success from paid search last quarter (growth team's figure, media cost
only, salaries out on both sides).

## Decision asked

Keep the docs engineer on DevRel through Q1. Options: keep, or move to campaign support.
Recommendation: keep - the first-success gain is the only activation lever moving this
year. Needed by 15 November.

---

Appendix: definitions · 180-day influenced rule, touch must precede opportunity creation ·
blind spots: hallway and podcast touches visible only through the signup question ·
activity: 4 talks, 11 posts, 3 webinars, 2 docs rewrites.
```

## Weak versus strong

```
// ✗ Weak headline - activity, no reader goal, no ask
This quarter the team gave 4 talks, published 11 posts and grew Discord to 3,200 members.

// ✓ Strong headline - outcome on the reader's goal, then the decision
First-success rate in the quickstart cohort DevRel rebuilt rose from 31% to 38%, the step
feeding your activation goal.
Decision asked: keep the docs engineer through Q1, by 15 November.
```

```
// ✗ Weak - shared credit renamed, multiple from modeled value
DevRel drove $410k pipeline, a 4.3x ROI on program cost.

// ✓ Strong - label, rule, shared credit, no multiple
$410k pipeline influenced (180-day rule, shared with sales); first read on closed revenue in Q1.
```

```
// ✗ Weak - the falling metric vanished since last quarter
(blog sessions no longer appear; no explanation)

// ✓ Strong - named, with the rule that removed it
Dropped since last time: blog sessions - no decision changed in two cycles (kill rule).
```
