**Next action:** confirm that v4 ships before Thu 2026‑11‑05 and that the VP agrees to the AMA slot in §7. Everything else below stands on those two facts. Review time is about 20 minutes.

# Driftmark Office Hours Program: Nov 2026 to Oct 2027

## 0. Assumptions to fix first

I made these up. Fix whichever are wrong.

1. v4 ships on or before 2026‑11‑03. If it slips, the AMA slips with it, and the program start moves one week after.
2. I have no names, so people appear as roles (§3). Swap in names.
3. Users sit mostly in the Americas and Europe, with a real APAC minority. That drives two slots.
4. Sessions run on video with live chat. Recordings and written answers go in the community forum. I wrote `[platform]` where the tool matters.
5. I assume no budget and 3 to 5 people to staff it.
6. I publish no pricing, dates or roadmap commitments unless Product approves them.

## 1. Purpose and driver

- **Funded driver:** developer enablement. Developers get unblocked on the runtime faster, and the product team hears what breaks.
- **Primary outcome:** a first‑time attendee deploys to production sooner than a comparable non‑attendee.
- **Not a goal:** support queue, sales channel, or marketing reach.

## 2. Slots

| Slot | When | Length | Covers |
|---|---|---|---|
| **A, main** | Every Tuesday, 16:00 UTC (US East 11:00/12:00, Europe 17:00/18:00) | 45 min | Americas and Europe |
| **B, APAC‑friendly** | Every second Thursday, 08:00 UTC, starting 2026‑11‑12 | 45 min | APAC and Europe morning |
| **AMA (one‑off)** | Thu 2026‑11‑05, 16:00 UTC | 60 min | See §7 |

**Pause weeks:** Tue 12‑22, Tue 12‑29 and Thu 12‑24 (year‑end), plus Thu 11‑26 (US holiday). Everything else runs.

### Tuesday rhythm

| Week of month | Format | Content |
|---|---|---|
| W1 | **Themed deep dive** | 15 min talk by a specialist, then Q&A |
| W2 | **Open floor** | Bring your code or a failing deploy |
| W3 | **Clinic** | Triage of open GitHub issues and forum threads. In Feb, May and Aug this becomes the **Roadmap session**. |
| W4 | **Show‑and‑tell and open floor** | Community demos (10 min each, max 2), then Q&A |

### Thursday rhythm (slot B)

- Always open floor.
- A recap of that month's themed topic opens the session (5 min).

## 3. Who is on each session

| Role | Duty | Rotation |
|---|---|---|
| **Host** (DevRel) | Runs the clock, reads questions, enforces rules | DevRel lead plus one backup, alternating |
| **Runtime engineer** | Answers technical questions live | One of 3 to 4 engineers, rotating weekly. Max 1 session per engineer per month. |
| **Support engineer** | Triages the question queue, files follow‑ups | Fixed on slot A, rotating on slot B |
| **Product manager** | Handles "will you build X" | W3 clinics, all Roadmap sessions, and the AMA |
| **Docs lead** | Takes doc gaps live | W3 clinics and the Nov 10 migration clinic |
| **Scribe** (community manager) | Notes, recording, follow‑up post within 24 h | Fixed |
| **Guest specialist** | Themed talk (W1) | Per §5. Customer guests only with written consent. |

**Minimum staffing:** Host, one runtime engineer and a scribe. If an engineer is missing, find a swap 24 h ahead or cancel and post a notice. Never run without an engineer.

## 4. Rules

1. **Submit questions ahead.** Post them in the forum thread by 12:00 UTC the day before. Live questions are welcome, but pre‑submitted ones go first.
2. **Triage order:** pre‑submitted, then first‑time attendees, then everyone else.
3. **Time‑box.** 10 minutes per question. After that the question moves to a thread or GitHub issue.
4. **Bring a repro.** A minimal reproduction, a deploy ID or a code snippet. Without one, the answer is "post it in the thread".
5. **Out of scope:** billing, account access, security reports and legal terms. Route these to the support channel. Report security issues privately through the security contact, never live.
6. **No roadmap promises.** The Product manager may share direction and no dates unless approved. The Host says "not committed" when unsure.
7. **No pricing numbers** beyond what the public pricing page states.
8. **Customer names stay private.** Never name a customer or a customer's code unless they consented in writing.
9. **Everything is recorded and published,** with the chat log and a summary post within 24 h. Anyone may attend without being recorded on camera. Names appear only if volunteered.
10. **Code of conduct applies.** The Host may mute or remove anyone. Escalate to the community manager.
11. **Unanswered questions get a written answer within 2 business days,** or an explicit "we don't know yet, tracked in <issue>".
12. **Cancellation:** announce at least 4 hours ahead. Two cancellations in a quarter trigger a review of the staffing plan.
13. **Tag every follow‑up** (docs PR, GitHub issue, bug) `from-office-hours`, so metric 5 can count it.

## 5. Twelve‑month calendar

All Tuesday sessions at 16:00 UTC. Themed talks are on the first Tuesday of the month. W2, W3 and W4 sessions follow the rhythm in §2 (+7, +14, +21 days).

| Month | W1 themed deep dive (date, topic, guest) | Special sessions |
|---|---|---|
| **Nov 2026** | **Thu 11‑05: v4 Launch AMA** (see §7). **Tue 11‑10: v4 migration clinic** (Runtime eng, Docs lead, Support eng) | 11‑17 open floor, 11‑24 show‑and‑tell. Slot B starts 11‑12. |
| **Dec 2026** | 12‑01: **Cold starts and performance** (Runtime eng) | 12‑08 open floor, 12‑15 show‑and‑tell and year review. **Pause 12‑22 and 12‑29.** |
| **Jan 2027** | 01‑05: **Logs, tracing and debugging at the edge** (Observability eng) | 01‑12 open, 01‑19 clinic, 01‑26 show‑and‑tell |
| **Feb 2027** | 02‑02: **State and storage** (Storage eng) | 02‑09 open, **02‑16 Roadmap H1** (PM, Eng lead), 02‑23 show‑and‑tell |
| **Mar 2027** | 03‑02: **Security, isolation and secrets** (Security eng) | 03‑09 open, 03‑16 clinic, 03‑23 show‑and‑tell |
| **Apr 2027** | 04‑06: **Local dev, testing and CI** (Tooling eng) | 04‑13 open, 04‑20 clinic, 04‑27 show‑and‑tell |
| **May 2027** | 05‑04: **Networking: WebSockets, streaming, fetch limits** (Networking eng) | 05‑11 open, **05‑18 Roadmap Q2** (PM), 05‑25 show‑and‑tell |
| **Jun 2027** | 06‑01: **Web frameworks on Driftmark** (DevRel + framework maintainers) | 06‑08 open, 06‑15 clinic, 06‑22 show‑and‑tell, 06‑29 open |
| **Jul 2027** | 07‑06: **Limits, quotas and cost control** (Runtime eng, PM for published pricing only) | 07‑13 open, 07‑20 clinic, 07‑27 show‑and‑tell |
| **Aug 2027** | 08‑03: **Multi‑region, data locality, compliance** (Platform eng) | 08‑10 open, **08‑17 Roadmap H2** (PM), 08‑24 show‑and‑tell, 08‑31 open |
| **Sep 2027** | 09‑07: **Streaming and AI workloads** (Runtime eng, guest) | 09‑14 open, 09‑21 clinic, 09‑28 show‑and‑tell |
| **Oct 2027** | 10‑05: **Production readiness and postmortems** (SRE, customer guest with consent) | 10‑12 open, **10‑19 Program review and next‑year plan** (public), 10‑26 show‑and‑tell |

**Customer guests:** one per quarter at most (Mar, Jun, Sep, Oct), always with written consent and a Comms read of their slides.

**Topic changes:** the Roadmap session in Feb sets the Q2 and Q3 topics. Swap themes if the product team ships something bigger.

## 6. Metrics

Seven metrics. Months 1 to 3 are **baselining**: collect, don't judge. Thresholds are set at the Feb review from the first three periods. Until then, "hypothesis" means a target to test, not a standard.

| # | Metric | Definition and source | Baseline | Threshold | Owner | Action on breach |
|---|---|---|---|---|---|---|
| 1 | **Answer time on pre‑submitted questions** (median) | Hours from question post to first human answer. Forum timestamps; exclude bots. | baselining | Target 2 business days (`hypothesis`). From Feb: flag when above the trailing median by more than 30% (`baseline`). | Support eng | Add a triage owner for that week. Check engineer rotation. |
| 2 | **Resolution rate** | Questions resolved in session or within 5 business days of the written follow‑up, divided by questions raised. Paired with reopen rate. | baselining | Flag below the trailing 3‑period median (`baseline`). Flag if reopen rate rises. | Community manager | Review the unresolved list at the Friday sync. Escalate to engineering. |
| 3 | **Active attendees per month, new vs returning** | Unique people per month, split by first‑ever vs returning. Counted by event platform and forum login. | baselining | Flag a 25% drop vs the trailing median (`hypothesis`). | DevRel lead | Check slot timing, promotion, topic. Read the burst vs trend rule below. |
| 4 | **30‑day first‑deploy rate** (product impact) | Share of first‑time attendees with a production deploy within 30 days of first attendance, compared with a matched cohort of non‑attendee signups from the same month. Consent required. | pre‑period needed: pull 3 months of signup deploy rates before the first read | Attendee rate above matched cohort (`baseline`). Report as a range, not a point. | Product analytics | Redesign the onboarding path in sessions. Share the finding with Product. |
| 5 | **Fixes shipped from sessions** | Count of docs PRs and issues tagged `from-office-hours` that merged within 30 days, divided by the number opened. | baselining | Flag below the trailing median (`baseline`). | Docs lead | Block time in the next sprint for the tagged backlog. |
| 6 | **Tickets per 100 new users on session topics** (business impact) | Support tickets on a themed topic in the 60 days before vs after that month's talk, normalised per 100 new users. Support tool. Below ~30 tickets, report the raw list. | baselining, using the 3 months before each talk | Fall vs the prior period (`baseline`). State the confound with docs changes. | Support eng | Fold the winning answers into docs. Retire topics with no effect. |
| 7 | **"Did you get unblocked?" score** | 1 to 5 single item at session end, plus response rate. | baselining | Flag a mean under 4.0 or a response rate under 20% (`hypothesis`). | Host | Fix the format. Ask lapsed attendees why they left. |

**Counter‑metrics:** metric 2 is paired with reopen rate so nobody closes questions early to hit the number. Metric 3 is paired with the returning share so a promotion spike doesn't count as health.

**Reading rules:**

- Compare Driftmark only with its own past.
- Report burst weeks (launches, events) separately from the trend.
- Cohorts are by month, never by day.
- Under 30 events in a period, publish the list instead of a rate.
- Kill rule: drop any metric that changes no decision across two review cycles.

**Attribution rule:**

- Signup form gets the question "how did you hear about Driftmark?", with an "Office hours or AMA" option.
- Influence is claimed only through metric 4's matched cohort with a 90‑day lookback.
- The word **influenced** is mandatory wherever credit is shared.
- No revenue claim is made for this program.

**Blind spots:**

- Silent viewers who never register or log in.
- Recording views, which client‑side analytics undercount for developers.
- APAC users who rely on recordings.
- No CRM link, so enterprise impact is anecdotal.
- Private chat conversations, which I can't see.
- Metrics 4 and 6 cannot separate attendance from other docs and onboarding changes.

**Cadence:** weekly scribe post, monthly ops read (first Friday), quarterly decision review (Feb, May, Aug, Oct), and an annual framework reset at the Oct 19 session.

## 7. v4 launch AMA (one‑off, folded in)

**When:** Thu 2026‑11‑05, 16:00 UTC, 60 minutes. Placing it before the first regular session makes it "session 0".

**Who:**

- **VP:** opens for 5 minutes only, then listens.
- **Eng lead for v4:** answers architecture and breaking‑change questions.
- **Runtime engineer** and **PM:** the PM answers "what's next" and "why" questions within the §4 rule 6 limit.
- **Docs lead:** migration questions.
- **Host** (DevRel): runs the clock and reads questions.
- **Support engineer:** moderates the queue and flags duplicates.
- **Scribe:** captures notes and unanswered questions.

**Run of show:**

| Minute | Item |
|---|---|
| 0 to 5 | VP opening, Host sets rules |
| 5 to 15 | v4 in 3 slides: what changed, what breaks, what to do first |
| 15 to 50 | Q&A. Pre‑submitted first, then live. Eng lead and PM split by topic. |
| 50 to 57 | Unanswered questions: say when each gets a written answer |
| 57 to 60 | Link to the migration clinic (Nov 10) and the recording |

**Countdown (today is Fri 10‑23):**

1. **By Mon 10‑26:** VP confirms the slot. Name the 3 answerers and the Host.
2. **By Wed 10‑28:** publish the announcement and open a question thread. Pin it on the forum and in the release notes.
3. **Fri 10‑30:** Comms and Legal review the "do not say" list (pricing, dates, deprecation deadlines, named customers).
4. **Mon 11‑02:** close the pre‑submit queue and group questions by theme. The Eng lead drafts answers for the top 10.
5. **Tue 11‑03:** dry run (30 min) with the full panel.
6. **Thu 11‑05:** run it. Record it.
7. **By Fri 11‑06:** publish the recording, summary and written answers for every unanswered question.
8. **Nov 10:** the migration clinic works from the AMA's top unresolved questions.

**APAC coverage:** the 16:00 UTC slot is outside APAC working hours. Keep the question thread open 48 hours before and answer in writing within 24 hours after. Optionally add a 30‑minute APAC replay Q&A on Thu 11‑12 in slot B.

**AMA metrics (reported separately, never in the baseline):**

- Registrants
- Live attendees
- Questions submitted
- Percentage answered live
- Percentage answered in writing within 24 hours
- 7‑day replay views
- 14‑day first v4 deploy rate among attendees vs signups who did not attend

The AMA is a launch burst. Don't compare it with regular sessions.

## 8. Operating checklist

1. Weekly (Mon): scribe posts the thread, Host confirms the engineer, Support eng triages pre‑submits.
2. Per session: record, then publish within 24 h with a summary and links.
3. Monthly (first Friday): ops read of metrics 1 to 7, plus the burst vs trend check.
4. Quarterly: decision review and roadmap session.
5. Annually (Oct 19): reset topics, slots, metrics.

**Next:** confirm assumptions 1 and 2 in §0, then send the AMA invite to the VP today.