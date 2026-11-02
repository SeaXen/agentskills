# Quarrystone Immersion Day: program redesign

## Verdict for leadership

**Don't keep the program as it runs today, and don't kill it yet.** Pause open booking. Run a 90-day pilot of the redesigned version below, with a pre-agreed keep/kill gate.

Your current data can't support either decision.

## What the data does and doesn't show

| Claim | Problem |
|---|---|
| "Only 2 of 31 started a POC" | A 6.5% rate with n=31 has a 95% interval of roughly 2–21%. You also have no baseline: what share of comparable accounts started a POC *without* an immersion day? Without that, you can't tell whether the days help, hurt, or do nothing. |
| "4.6/5 survey" | It measures how much attendees enjoyed the day. It doesn't measure buying intent. A free day off with a good lab scores 4.6 and ends in no POC. Keep it as a quality signal only. |
| "Lab platforms say 40% start a trial, up from 14%" | This is vendor marketing, and it doesn't transfer. It counts self-serve users starting a low-commitment *trial*. You're measuring *sales-assisted POCs* at accounts you visited in person. The "up from 14%" comparison is also unspecified. It says nothing about your lab. |
| "Our labs are the issue" | No evidence yet, and the design points elsewhere (below). A lab can be fine while the program fails upstream. |

**More likely causes**, all visible in how the program runs:
1. **No qualification.** AEs book a day whenever a prospect asks. Some of those prospects are tire-kickers, have no project, or have no budget or timeline.
2. **No pre-work.** The agenda is the same standard 2 hours of slides plus a lab for everyone. It isn't tied to the prospect's use case, data, or decision criteria.
3. **No defined exit.** Nothing in the agenda ends with a commitment such as a scoped POC, a named owner, or a date.
4. **Success measured by satisfaction**, so nobody is accountable for the outcome.

## Step 0: diagnose the 31 before redesigning (about 1 week)

Pull these fields per account from the CRM and the SE and AE notes:
- Deal stage and opportunity existence *before* the day
- Whether the prospect had a named use case, budget, and timeline
- Attendee roles (engineers only, or also a decision-maker)
- Who requested the day (prospect or AE) and why
- Follow-up: what happened in the 14 days after, and by whom
- Outcome: POC started, POC pending, stalled, or lost to a competitor
- Cost: SE and DevRel hours, travel

Then ask two questions:
- **What distinguishes the 2 that started POCs?** Look at the pre-existing use case, attendee mix, and follow-up speed.
- **Where do the other 29 stall?** Is it before the day (they never had a project), at the day (the content missed), or after (no follow-up)?

If the 29 mostly lacked a live project, qualification is the fix. If they had projects and the lab didn't convince them, then the lab is the issue. Test your hypothesis against this data instead of against the vendor stat.

## The redesigned program

### 1. Purpose

An immersion day exists to **move a qualified account from "interested" to a scoped, resourced POC**. It's not education and it's not goodwill.

### 2. Entry gate (replaces "book on request")

An AE can request a day only if the account meets all of these:
- A named project with a use case (RAG, semantic or hybrid search, recommendations, and so on)
- A named technical owner who will attend
- A named business sponsor or decision-maker who commits at least 30 minutes of attendance (the scoping segment)
- A rough decision timeline, such as a decision within about 1–2 quarters
- Sample data, or the ability to share a de-identified subset, before the day

Accounts that don't qualify get the self-serve path (docs, sandbox, office hours). Those paths cost far less than a site visit.

Treat the gate thresholds as a starting point. Adjust after the first 90 days.

### 3. Pre-work (2 weeks before)

Run a **60-minute discovery call** led by the SE. It covers:
- Current stack (existing search or DB, embedding model, scale: vectors, dimensions, QPS)
- Success criteria in their words: target recall, p95 latency, filtering needs, cost ceiling, security and compliance constraints
- Who decides, and what blocks a POC today (security review, procurement, data access)
- Who else needs to be in the room

Output: a **one-page Day Brief** shared with the prospect and the AE. It states the use case, the 2–3 questions the day must answer, and the proposed POC hypothesis.

Also: get the sample data and load it into a prepared environment before the day.

### 4. Agenda (full day or half day; the 2-hour format is too short for real data work)

| Block | Time | Content |
|---|---|---|
| Frame | 15 min | Restate the Day Brief and the questions to answer. No product pitch. |
| Architecture fit | 30–45 min | Their use case on Quarrystone: indexing choices, filtering, hybrid search, scaling, cost at their volume. Slides are capped here and tailored. |
| **Hands-on on their data** | 90–120 min | They work with their own sample data and queries. Build an eval set (queries with expected results), measure recall and latency, and test filtered search and updates. |
| Findings readout | 20 min | Show what they measured, honestly, including where Quarrystone falls short or needs tuning. |
| **POC scoping** | 30–45 min | Write the POC plan with them: success criteria (numbers), data, timeline, owners, resources, blockers and who clears them. The business sponsor attends this segment. |

The standard generic lab can remain as a fallback for accounts that can't share data. Mark those days as lower-confidence.

### 5. Roles

- **AE:** owns qualification and the post-day commercial path. They are accountable for the follow-up, not only the booking.
- **SE:** runs discovery, the lab, and the POC plan.
- **DevRel:** supplies content, the reusable lab, and facilitation for larger groups. They aren't the owner of the outcome.
- **Sponsor (prospect):** attends scoping and signs off on success criteria.

### 6. Follow-up (the part that is missing today)

- Same day: the POC plan and the findings go to all attendees.
- Within 48 hours: AE and SE hold a call with the champion to confirm the POC start date.
- Day 14: if no POC has started, a recorded reason is logged (no budget, security review, lost priority, competitor), and the account is either re-queued or closed.

### 7. Measurement

Replace the satisfaction survey with commitment signals. Keep the survey as a quality check.

**Leading indicators (at the end of the day):**
- Written POC plan with numeric success criteria: yes or no
- Named owner and named sponsor on that plan
- Kickoff date set before the team leaves
- Data access granted

**Outcome metrics (the ones leadership decides on):**
- **POC start within 45 days of the day** (primary)
- POC-to-win rate
- Cost per POC started (SE, DevRel, and travel hours)
- Sales-cycle length versus comparable accounts

**Comparison group.** Track a matched cohort of qualified accounts that get the standard path (discovery call, docs, self-serve sandbox) and no immersion day. Without it, you can't separate "the day works" from "qualified accounts start POCs anyway". Even 10–15 accounts is informative, though not statistically strong.

### 8. Pilot and keep/kill gate

- **Scope:** 12–15 qualified days over 90 days, plus the comparison cohort.
- **Review at day 90.** Proposed gate, to be set with leadership *before* the pilot starts and not after seeing results:
  - **Keep and scale** if POC start rate within 45 days is clearly above the comparison cohort's and at least about 30–40% of qualified days.
  - **Fix and rerun** if the rate is above baseline but below target and the stall reasons point to something fixable.
  - **Kill or shrink to an on-demand add-on** if the rate is no better than the comparison cohort.
- The numbers above are proposals, not benchmarks. I don't have a source for a "good" immersion-day POC rate, so calibrate them against your own funnel, using your current POC rate from qualified opportunities.

## On the lab question

Don't re-platform the lab yet. Improve it only in ways the redesign already implies: run it on the prospect's data, with an eval set and a measured readout. Revisit the lab platform if the pilot's stall reasons show prospects can't get through the hands-on block. If you do evaluate lab platforms, ask vendors for the denominator, the definition of "trial", the customer type, and the time window behind that 40%.

## What I need from you

1. Can you pull the Step 0 fields for the 31 accounts? I can then tell you which cause dominates.
2. What is your normal POC start rate for qualified opportunities that didn't have an immersion day?
3. What does one immersion day cost in SE and DevRel hours, plus travel?
4. Are AEs compensated or measured on days booked or on POCs started? If it's days booked, the incentive undermines the entry gate.