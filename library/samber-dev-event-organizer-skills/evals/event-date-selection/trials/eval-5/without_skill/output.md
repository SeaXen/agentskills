# CompilerCamp: dates and the cost of picking the wrong days

## Short answer

- **Nobody can give you a real percentage yet.** It depends on three numbers you haven't measured: the audience mix, how many professionals will attend on a weekend day, and how many students will skip Friday classes.
- **Friday + Saturday is a sensible default, but it isn't "obvious".** Each audience gives up one day. Professionals lose Saturday, which is unpaid personal time. Students lose Friday, which is a teaching day.
- **Under my illustrative guesses, the gap between best and worst day choice is about 5 to 6 points of attendance.** It would not be 30%. Those inputs are guesses, so treat the result as a template to fill in.
- **Settle it with a 2-minute survey, not a committee vote.** Details below.

## The model

Attendance is the share of intended person-days that actually show up:

```
retention = ( P × avg(p_day1, p_day2) + S × avg(s_day1, s_day2) ) / (P + S)
```

- `P`, `S`: professionals and students you hope to attract.
- `p_day`, `s_day`: probability that a person who wants to come attends that day.

Loss from a wrong choice = best option's retention minus the option you picked.

## Illustrative numbers (my assumptions, not data)

Assumptions:
- 100 professionals and 200 students.
- Professionals: 85% on a weekday, because it's company time and still needs manager sign-off. 45% on Saturday, 35% on Sunday.
- Students: 85% on Saturday, 80% on Sunday. 65 to 70% on weekdays, since they skip lectures.

| Option | Professionals | Students | Total retention |
|---|---|---|---|
| Thu + Fri | 85% | 67.5% | ~73% |
| **Fri + Sat** | 65% | 77.5% | **~74%** |
| Sat + Sun | 40% | 82.5% | ~68% |
| Tue + Wed (typical industry days) | 85% | ~60% | ~68% |

**What the numbers show**
- Fri+Sat and Thu+Fri land within a point of each other. The compromise costs you almost nothing relative to the best case.
- Sat+Sun is the clear loser if professionals matter to you, and that is the "wrong choice" case. It loses roughly 5 to 6 points overall and about 45 points among professionals.
- The result is most sensitive to the Saturday professional rate. If it is 25% instead of 45%, Fri+Sat drops to about 70%. If it is 65%, Fri+Sat wins clearly.
- Retention may matter less than composition. If sponsors fund the event because of the professionals, weight `P` higher. The ranking can then flip toward Thu+Fri.

## Settle it with real data

1. **Survey the two groups before fixing the date.** Use the committee's contacts, the employers' DevRel or recruiting teams, and the two universities' CS societies. Ask each person:
   - "Could you attend on Thu+Fri, Fri+Sat, or Sat+Sun?" Give three options and allow multiple answers.
   - Professionals: "Would your employer let you attend on a work day? Would you give up a Saturday?"
   - Students: "Would you skip Friday teaching?"
2. **Aim for about 30 responses per group.** That is enough to show whether the Saturday professional rate is near 25% or near 65%.
3. **Plug the answers into the formula** and pick the highest-scoring option. If Fri+Sat is within about 3 points of the best option, keep it, because the difference is inside the noise.
4. **Check calendar conflicts before locking dates:**
   - Both universities' term dates, exam periods and reading weeks. A Friday during exams cuts student attendance far more than 65%.
   - Manchester home-match days and large concerts, which push up hotel prices and cause travel disruption.
   - Competing compiler and systems conferences.
   - Venue availability and price. Weekend rates are often cheaper.

## Mitigations if you keep Fri + Sat

- **Put the professional-focused content on Friday** (industry talks, hiring, sponsor sessions) and the student-friendly content on Saturday (workshops, hands-on labs, career panels).
- **Offer a one-day professional ticket and a one-day student ticket.** Most of the loss comes from people who can only make one day.
- **Ask employers to let staff attend the Friday as a work day.** Give them a short letter justifying the event as training or recruiting.
- **Record talks.** This recovers some of the people who miss a day.

## Bottom line

Fri+Sat is a defensible choice, and the downside of getting it slightly wrong looks small. The real risk is choosing Sat+Sun or a pure midweek format. Run the survey, fill in the formula, and keep Fri+Sat unless the data shows professionals won't give up a Saturday.