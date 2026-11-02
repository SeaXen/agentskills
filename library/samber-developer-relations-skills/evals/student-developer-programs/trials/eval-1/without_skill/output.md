**Next action (10 min):** export your signups by email domain (`.edu`, `.ac.uk`) from the last 90 days. That list picks your 25 schools. Build the school list from it before recruiting anyone.

The program below is built to hit "25 schools by March" at about 5 hours a week. Six parts of the brief need a decision first, so they come first.

## Six brief items to settle before launch

1. **".edu gets 12 months Pro" misses UK students.** The UK uses `.ac.uk`, and `.edu` is US-only. Use an academic-domain allowlist (the open-source Swot list is a start) and a manual fallback for everyone else. Pro costs you runner minutes, so set a compute cap, and expect crypto-mining abuse on free hosted CI.
2. **"$15 per verified signup" is gameable.** The free tier needs no card, so fake signups cost nothing. Pay on activation, not signup (defined below), and cap the bounty.
3. **Final-year students leave in May.** Your program starts in March, so they'd serve about 10 weeks and then vanish. Recruit 2nd- and 3rd-year students as leads. Take final-years only as paid-for-one-term leads who name a successor by April.
4. **One ambassador per school is a single point of failure.** Keep one paid lead per school. Add an unpaid deputy with perks only (swag, Pro, a reference letter). A lead who goes quiet then doesn't kill the school.
5. **You can't run 25 schools at 5 hours a week.** 25 schools means 50 events a month, 50 event reports and 25 payouts. That is about 22 hours a month of pure admin, before recruiting and support. The plan below gets you to 25 signed by March and runs it at about 5 hours a week only with automation. If you don't automate, you need 8 hours a week, or a part-time coordinator.
6. **Paying students needs legal review before anything else.** I'm not a lawyer, so check these with one:
   - Many US international students (F-1) and UK Student-visa holders can't take contractor income.
   - Some universities ban paid commercial promotion on campus.
   - US (FTC) and UK (ASA) rules require ambassadors to disclose that they're paid.
   - Fallback payout: club funding or credits instead of cash.

## Program design

**Roles**
- **Lead:** one per school. Paid. Runs events and answers questions from students.
- **Deputy:** optional and unpaid. Takes over the lead role the following year.
- **You:** own the playbook, the kit, the monthly call and the payouts.

**Stipend: $300/month, conditional**
- Paid only if the lead holds 2 events and files a report within 5 days of each.
- Pay in full only for months the school is in term. Pause during exams and breaks.
- Miss a month: no stipend. Miss two months: offboard.

**Activation bounty: $15 per activated student**
- **Activated** means a verified academic email, a first successful pipeline run within 14 days, and 3 or more builds.
- The referred student must be a different person from the ambassador and from other ambassadors.
- Cap at 30 per ambassador per month, so $450 maximum.
- Track attribution with a referral link or code. Ambassadors never see signup lists (GDPR).

**Student Pro: 12 months free**
- Open to all verified students, not only ambassadors' referrals.
- Get finance sign-off on the cost per student and a compute cap.
- At month 12 the student drops to the free tier, so there's no cliff. Send an email at month 11.

**Events (2 a month per lead)**
- *CI clinic* (45 min): bring your repo, get a pipeline running.
- *Hack night:* part of a club's existing meeting (ACM, GDSC, hackathon teams). This is the cheapest option.
- *Workshop:* "Ship your class project with CI".
- Budget $75 per event for food, reimbursed with a receipt.
- Pipewright provides a slide deck, a lab repo, a sign-up QR code and a report form.
- Pause events in finals (Dec, late April to May) and school breaks. US and UK term dates differ, so keep a calendar per school.

**Selection (application form, 6 questions)**
- Year and expected graduation date.
- A club or community role they already hold.
- Describe a CI problem they've solved.
- Audience size they can reach (club lists, courses).
- Hours a week they can commit.
- Disclosure and visa-status check (routes to the legal fallback).

Score each answer 1 to 5. Take the top candidate per school. Prefer students who already lead a club over students with the best GitHub profile.

**School selection (25: aim for about 15 US, 10 UK)**
- Rank schools by existing signups from their domain.
- Prefer schools with an active CS or ACM club.
- Skip schools whose policy bans paid promotion.

## Timeline (today is 2026-10-31)

| When | What | Hours |
|---|---|---|
| Nov 2–29 | Pull the data, get legal and finance sign-off, build the kit and the application form | ~20 |
| Dec 1–18 | Applications open through clubs and professors. Interview 10 for the pilot | ~25 |
| Dec 19 – Jan 4 | Pause | 0 |
| Jan 5–31 | Onboard 10 pilot schools (kickoff call, kit, referral links) | ~20 |
| Feb | Pilot runs its first events. Open recruiting for the other 15 | ~25 |
| Mar | Onboard wave 2. **25 signed.** Gate review | ~25 |

That's about 115 hours across 17 weeks. It exceeds your 85, so Nov–Dec design must stay lean, and the 15-school wave in Feb–Mar is where you'll need help.

## Your weekly time budget (steady state, 5h/wk)

- Reports: use a form that auto-fills a sheet. Review exceptions only (1h).
- Payouts: batch monthly through one payment tool (0.5h).
- Support: one shared channel for all ambassadors, answered twice a week (1.5h).
- Monthly group call (1h a month, so about 0.25h a week).
- Recruiting and school relations (1.75h).

If a task takes more than 5 minutes per ambassador, change the process.

## Budget (estimate, excludes Pro cost)

| Month | Active schools | Stipend | Bounty + events | Total |
|---|---|---|---|---|
| Jan | 10 | $3.0k | ~$2.5k | ~$5.5k |
| Feb | 17 | $5.1k | ~$4.5k | ~$9.6k |
| Mar | 25 | $7.5k | ~$7.5k | ~$15k |
| Apr | 25 | $7.5k | ~$7.5k | ~$15k |
| May | 25 | $7.5k | ~$7.5k | ~$15k |

That's about $60k for Jan–May. Bounty plus event cost is an assumption of about 10 activated students and 2 events per school. The bounty cap bounds the worst case at roughly $11k a month in bounties alone. At full run, each event costs about $225 (half a stipend plus food), so 20 attendees is about $11 each.

## Scorecard (review monthly)

- **Primary:** activated students per school, measured at 30 days.
- **Support:** events held versus 2 per month, attendees per event, activation rate per event, and the share of ambassadors who are active.
- **Cost:** spend per activated student.
- **Check, not target:** repeat usage at day 30 and day 90. A signup that goes silent isn't worth $15.

**Gate (end of March):**
- A school with fewer than 1 event in 2 months is paused.
- If spend per activated student is above what a paying Pro customer returns in lifetime value, cut the bounty or the stipend before adding schools. You'll need LTV from finance for this.
- Don't add schools 26 and up until the first 25 pass this gate.

## Risks

- **Fraud and abuse:** fake accounts for bounties, and free runners used for mining. Mitigate with the activation definition, a per-account compute cap and a manual review of any school above 3x the average.
- **Leads going quiet:** mitigate with the deputy and the 2-month rule.
- **University conflict:** one school objects to paid promotion. Mitigate by pre-checking policies and keeping the club-funding payout option.
- **Your time:** 25 schools is the stretch. Raise it with the CEO now, as in item 5.

## Open items for you

1. What does a Pro student cost you per month? (Sets the compute cap.)
2. Is the $60k approved?
3. Is "25 by March" fixed, or would "10 active in Jan, 25 signed by March" satisfy the CEO?

**Next:** run the signup export by email domain, then send me the top 30 domains and I'll draft the school shortlist and the application form.