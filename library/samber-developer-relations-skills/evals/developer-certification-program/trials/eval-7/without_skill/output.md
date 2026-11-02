**Next action (2 min):** send the owner-gate message in section 2 to your manager and the CEO today. Everything else depends on the answer.

# Pellmont Certified Associate: 9-week plan

## 1. Verdict

- ✅ Doable: a 100-question exam, proctored on conference day, with a documented cut score. The score comes from a formal standard-setting method (modified Angoff) run by subject-matter experts (SMEs).
- ❌ Not doable in 9 weeks on a few thousand dollars: a statistically validated exam. That takes pilot data from 100 or more candidates, and you will not have it before launch.
- Ship **provisional** on day one, then finalize from real answers. "Proper cut score" here means a defensible, documented process with a written review date. It does not mean validated.
- ⚠️ I priced nothing. Every dollar figure below is a planning estimate to confirm with quotes.

## 2. Gate: name an owner (week 1–2)

Exams decay. Product versions change, items leak, candidates appeal, retakes arrive. You leave in 3 months, and about 4 of those weeks come after the conference. Without an owner, the exam dies the day you walk out.

Send this to your manager and the CEO:

> I can deliver Pellmont Certified Associate at the conference: 100 questions, proctored, documented cut score. It needs a named owner for item maintenance, candidate support, and annual review (~4 h/week after launch). I leave in 3 months. I need a name by end of week 2. Without one, I ship it as "Founding Cohort / Beta" with a published expiry and no promise of future exam forms.

Fallback if no owner appears by week 2 (needs CEO sign-off):

- Brand it "Pellmont Certified Associate (Founding Cohort)".
- Credentials are valid 12 months.
- Publish one line: no further forms are guaranteed.
- This still keeps the stage promise: it is available at the conference.

Likely owners: training, support, customer success, or the docs lead.

## 3. Exam design

- Format: 100 single-best-answer items, 4 options, scenario-based, associate level.
- Time limit: 120 minutes.
- Blueprint (illustrative, confirm in week 1). Domains and weights:
  - pipeline authoring, 30%
  - secrets, permissions, security, 15%
  - runners and scaling, 15%
  - caching, artifacts, performance, 15%
  - deployments and rollbacks, 15%
  - troubleshooting, 10%
- Interview the 2 hiring-manager customers. Ask what an associate must do on day 1. Use their answers to set the weights. This is your job-task analysis, and it is also your best marketing proof.
- Write about 160 items. Expect 30–35% to die in review and leave ~105. Keep any spare as the seed of a second form.

## 4. Timeline

1. **Weeks 1–2: blueprint and owner.**
   - Interview the 2 customers (~3 h).
   - Lock the blueprint.
   - Get the owner decision.
   - Recruit 6–8 SMEs (engineers, support, solutions) and 1 reviewer.
   - Choose the platform.
2. **Weeks 2–5: item writing.**
   - Each SME writes ~25 items against the blueprint.
   - Estimate: ~45 min per item including review, so ~120 h total. You carry ~40 h, each SME ~10–12 h.
   - Peer review for accuracy, then an editorial pass for clarity and for answers that give themselves away.
   - Front-load this. Week 9 ends around 25 Dec, so holidays will shrink SME time late in the plan.
3. **Week 6: cut-score workshop (3 h).**
   - Modified Angoff, 6–8 SMEs.
   - Define the "minimally qualified candidate" in writing first.
   - Each SME estimates the probability that this candidate answers each item correctly.
   - Round 1 is independent. Discuss outliers. Round 2 is revised.
   - Cut score = mean of the SME sums, rounded.
   - Sanity check: the pass rate for the minimally qualified profile should look plausible, ~60–75% for an associate exam.
   - Worth ~$1–2k to have a psychometrician review the method and facilitate. If the budget holds, do it.
4. **Weeks 7–8: dry run and platform build.**
   - Load the items and shuffle the item and option order.
   - Have 8–10 internal staff outside the SME group take it under timed conditions. This catches broken items and timing issues. Do not use their scores to set the cut.
   - Fix items.
   - Write candidate rules: ID check, no devices, no notes, a retake policy, an appeal path.
5. **Week 9: conference day.**
   - Run 2 to 3 closed-room sittings with 2 proctors each.
   - Candidates use a locked-down browser. Safe Exam Browser is free, or the platform's own.
   - Items never leave the room.

## 5. After the conference (your last 4 weeks)

1. Within 30 days, run item analysis on real answers:
   - Reliability: KR-20 of 0.80 or higher is the target.
   - Per item: difficulty and point-biserial correlation.
   - Flag items that almost everyone gets right or wrong, and items with correlation under ~0.15.
2. Remove flagged items from scoring. Publish the rule up front: a removal can only help a candidate. Nobody who passed on the day loses the credential.
3. Announce results as "provisional, confirmed within 30 days".
4. Confirm or adjust the cut at the next Angoff pass once ~100 or more candidates have sat.
5. Hand over the owner pack:
   - item bank, with a metadata field for each item's product version
   - blueprint and SME roster
   - cut-score report
   - runbook
   - appeals log template
   - one-year maintenance calendar

## 6. Proctoring options

- **Recommended: onsite proctoring at the conference.** Cost is mostly staff time, and security is strong. It also makes a good stage moment.
- Remote proctored sittings later: usually per-exam fees, roughly $10–30 each (verify). Also ask about video retention and GDPR.
- Test-center networks (Pearson VUE, PSI): onboarding takes months and the contracts are large. Out of scope for 9 weeks.

## 7. Budget (planning ranges, not quotes)

- Exam platform or quiz tool: $0–1.5k. Free options are Moodle quiz with Safe Exam Browser. Hosted certification platforms may fit, but only if the quote is under ~$1.5k.
- Psychometrician review and workshop facilitation: $1–2k.
- Proctor staffing and room: $0–300, mostly internal.
- Badge issuing (Open Badges or Credly): $0–500 for launch. Credly's enterprise pricing may exceed that, so check.
- Reserve: ~$500 for printing, loaner laptops, and incidents.

## 8. Claims and risks

- ⚠️ Hiring managers will screen on this, so what you claim matters. Say "verifies working knowledge of the Pellmont platform, developed by SMEs against a published blueprint." Do not say "industry-recognized", "validated", or "accredited".
- Tell the two customers what it measures, what it does not, and that it is a founding-cohort exam if the fallback applies. Advise them not to use it as a sole filter.
- Item leaks are the big security risk. Use one closed-room sitting per cohort, shuffle, and keep reserve items for a refresh.
- Product drift: the owner retires or updates items each major release. Put the version tag on every item now.
- Regulatory and data protection: publish a short candidate agreement and a retention policy for scores, ID checks, and any recordings.
- Open question: how many attendees will want to sit? That sets the number of sittings and proctors. Estimate it from last year's registration.

## 9. Decisions I need from you

1. Exact budget figure.
2. Expected exam takers at the conference.
3. Whether you have 6–8 SMEs who will commit ~10–12 h each.

**Next:** send the section 2 message, then block 3 h this week to interview the 2 customer hiring managers.