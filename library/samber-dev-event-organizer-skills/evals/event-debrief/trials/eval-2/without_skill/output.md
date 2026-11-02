# TrailStack Conf lessons-learned log

**Event:** TrailStack Conf, 400 attendees, single day, last Saturday.
**Status:** Draft. Your notes hold four observations and a few conclusions. Anything not in your notes is marked **Hypothesis** and needs checking before it goes in the final log.

## Summary

| # | Issue | Impact | Root cause (confirmed) | Confidence | Top action |
|---|---|---|---|---|---|
| 1 | Registration queue | 🔴 First talk 10 min late | Staffing and flow design left no surge capacity. | Medium | Size check-in to peak arrivals and add a pre-agreed escalation trigger. |
| 2 | Track B mic handoffs | 🟠 Repeated talk disruption, all afternoon | Unknown. Your notes record a symptom and a person, not a cause. | Low | Run an AV debrief and add a mic-handoff runbook. |
| 3 | Gluten-free count | 🟢 Fixed by 1pm | Unknown. The count was wrong at the source or in transmission. | Low | Trace the count. Keep the early-flag habit. |
| 4 | Rain flooded sponsor tent | 🟠 Sponsor-facing damage | No weather contingency or drainage check. The rain was only the trigger. | Medium | Add a weather plan and a site-drainage check. |

## 1. Registration queue

**What happened (facts):** The queue went out the door. The first talk started 10 minutes late. Priya was overwhelmed. At 9:15 she pulled two floor volunteers to clear the queue.

**What worked:** Priya recovered it by improvising, and the queue was cleared.

**Root-cause analysis**
1. The queue grew because arrivals outpaced check-in throughput. *(Fact)*
2. Throughput was too low because one person was effectively running check-in. *(Inferred from "Priya was overwhelmed")*
3. Nobody was assigned to check-in surge capacity. The fix came from ad-hoc pulling at 9:15, not a plan. *(Inferred)*
4. **Hypothesis:** The plan assumed steady arrivals. In practice, 400 people mostly arrive in the 30 to 45 minutes before the first talk.
5. **Hypothesis:** No trigger such as "queue over N people means add staff" existed. The problem was spotted late, since volunteers arrived at 9:15, which is not early.

**Root cause:** Check-in was sized for average load, not the arrival peak. It had no escalation trigger and no reserve staff.

**Correcting the note "We need better volunteers":** The evidence doesn't support this. The volunteers solved the problem within minutes of being asked. The gap was how many were assigned to check-in, when they were assigned, and who decided to redeploy them. Better volunteers would not have fixed that. Don't carry this conclusion into the final log unless you have evidence of a volunteer-quality problem.

**Actions**
- Model the arrival curve (for example, 60% of attendees in the last 45 minutes) and size stations to it.
- Pre-assign 2 to 3 flex volunteers who move to check-in at a stated trigger, such as a queue past the door or a wait over 5 minutes.
- Use pre-printed badges, alphabetical lanes, and a separate "problem" lane.
- Send a pre-event email with a QR code to cut lookup time.
- Name a floor lead so Priya isn't deciding alone.

**Open questions:** How many people were on the desk? When did the doors open? Did anyone ask for help before 9:15? What was the badge-lookup method?

## 2. Track B mic handoffs

**What happened (facts):** Mic handoffs went wrong in track B all afternoon.

**Why the note isn't enough:** "The AV guy kept screwing up" names a person and gives no mechanism. A problem that repeats all afternoon points to something structural, because one person's mistake would normally be corrected after the first occurrence. Blaming the person would stop the investigation here.

**Hypotheses to test (not facts)**
- There was no handoff procedure between speakers, such as who hands over, when mics are swapped, and who is on stage.
- Track B had a single AV tech covering stage and booth, with no backup.
- Session changeovers were too short for a mic swap.
- Equipment issues (batteries, channel interference) were misread as operator error.
- Track B got less briefing or rehearsal than track A.
- Speakers weren't told how mics work (lavalier vs handheld, clip-on vs pass).
- Nobody owned feedback in real time, so the problem persisted instead of being fixed at the first failure.

**Root cause:** Not established.

**Actions**
1. Hold a 15-minute debrief with the AV person, in a blameless format. Ask: "What made handoffs hard in track B?"
2. Ask 2 or 3 track B speakers and the room host what they saw.
3. Check the changeover times in the schedule.
4. Write a one-page mic runbook (who, when, what) and brief speakers on it.
5. Require a changeover checklist and a mic test before each session.
6. Add a stage-manager role per track, separate from the AV tech.
7. Contract AV with a scope that includes rehearsal and a named backup.

## 3. Gluten-free lunch count

**What happened (facts):** The gluten-free lunch count was wrong. The team flagged it, and catering fixed it by 1pm.

**What worked:** The team caught the error and escalated it. Catering responded quickly. Dietary needs were met.

**Root cause:** Not established. The notes don't say whether the count was too low or too high, or how big the gap was.

**Hypotheses**
- The registration form captured dietary needs, but the numbers were copied to catering manually and went stale.
- Late registrations or walk-ins arrived after the catering count was sent.
- Catering miscounted the order.
- The form categories were ambiguous (gluten-free vs celiac vs "no wheat").

**Actions**
- Find out where the number went wrong: form, export, handoff, or caterer.
- Get a final dietary export 72 hours before the event, and confirm the count with the caterer in writing.
- Add a 10 to 15% buffer for dietary meals.
- Label food and confirm allergen handling (celiac needs differ from preference).
- Keep and repeat the early flag. Treat it as a pattern to keep.

## 4. Rain flooded the sponsor tent

**What happened (facts):** Rain flooded the sponsor tent mid-morning.

**Correcting the note "nothing anyone could do":** True only once the water was in. The rain was the trigger, not the cause. Flooding on the day means something earlier was missed, and "nothing could be done" closes off the lessons.

**Root-cause analysis**
1. The tent flooded because water pooled or ran into it. *(Fact)*
2. **Hypothesis:** The tent was on low or poorly draining ground, or the sides and floor weren't sealed.
3. **Hypothesis:** The site wasn't checked for drainage, or the setup crew wasn't briefed on it.
4. **Hypothesis:** The forecast wasn't monitored, or no rain plan existed.
5. **Hypothesis:** No fallback space was designated for sponsors, and no one had authority to move them.

**Root cause:** Probably a missing weather contingency and a skipped site-drainage check. Both are unverified.

**Actions**
- Check the forecast 72 hours and 24 hours out, and name an owner for the go/no-go call.
- Walk the site with the tent vendor and check the grade, drainage, and ground sheets.
- Raise floors and keep electrical gear off the ground.
- Designate an indoor fallback for sponsors, and write down who triggers the move.
- Check the vendor contract and event insurance for weather cover.
- Contact the affected sponsors: ask what was lost, and decide whether any goodwill gesture or credit is owed.

**Open questions:** Was rain forecast? What did sponsors lose (equipment, materials, lead-capture time)? Was the tent supplier's setup per spec?

## Cross-cutting patterns

- **No trigger-based escalation.** Registration and AV both ran on someone noticing. Define what a problem looks like and who acts.
- **Plans sized for the average case.** Check-in peaks, dietary counts, and weather are all about tails.
- **Notes recorded blame and fatalism ("better volunteers", "the AV guy", "nothing anyone could do") instead of mechanisms.** Keep the log blameless and ask "what made this possible?"
- **What worked:** Priya's quick redeployment, the gluten-free flag, and catering's response. Keep these as practices.

## Next steps (in order)

1. ⏳ Debrief the AV person and track B speakers (15 min each). This is the biggest gap.
2. Trace the gluten-free count (10 min).
3. Gather the check-in facts: desk staff count and the arrival curve from badge scans.
4. Collect the forecast, tent vendor spec, and sponsor impact for the rain item.
5. Assign an owner and a due date to each action. I left owners blank since I don't know your team.
6. Replace the **Hypothesis** items with findings and re-issue the log.

If you can answer the open questions above, I can turn this into a final version with confirmed root causes.