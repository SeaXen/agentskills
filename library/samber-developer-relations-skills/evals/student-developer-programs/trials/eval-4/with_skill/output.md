# Codemint high-school program plan

**Direct answer:** I can't plan this as written. I declined four parts of the request and replaced them (below). The replacement is a separate, adult-led school-club program that is not an extension of the university one. Three gate facts are still unknown, so the plan is conditional until you confirm them.

I read the skill and its three references in full. Two inputs were missing: the interview answers and Codemint's own context. The skill's fallback is an assumptions table, and I used it.

## Refused asks

| Your ask | Declined because | Replacement |
|---|---|---|
| 14-17 year-old club **leaders** | Under-18 leadership roles are refused. The floor is 18+, based on safeguarding (a house rule) and consent law. GDPR Art. 8 requires parental consent where consent is the basis, below 16 by default and 13 to 16 by member state. COPPA covers under-13s. US state teen-privacy laws also apply to 13-17s. | Adult-led clubs (teacher or mentor). Students are members. Leadership goes to 18+ students only. |
| **Public leaderboard with names and photos** | Public profiles for under-18s are refused. A ranking also works as a quota renamed. Milestones may reward what students learn and ship, never reach or signup counts. Outcomes are counted per campus, never per ambassador. | A project showcase credited to the club or school. Individual credit appears only for 18+ students or with documented guardian consent, and photos are off by default. |
| **Top 5 flown to Berlin** | Travel for under-18s is refused. It would also be a prize attached to the leaderboard, which has the same quota problem. | Teachers and 18+ students attend. Minors take part online in a judged showcase. |
| **Reuse the university application form** | The university design cannot be reused for high schools. The form was built for 18+ applicants with no parental consent, and it presumably collects photos and public handles. | A new form with school and guardian consent. See "Form" below. |

**Mismatch for you to resolve:** the plan runs a high-school program, but the existing form and ambassador design are university-only. Your call: do you accept the separate high-school design? The alternative is to keep this at 18+ inside the university program.

## Assumptions

I have no interview answers, so these assumptions carry the plan. Each row says what changes if it is wrong.

| # | Assumption | If wrong |
|---|---|---|
| 1 | **Job:** ecosystem. Students build projects that keep running after the club's first term. This is the closest fit for a platform whose users are kids. Visibility alone is not a job. | If the job is adoption, the student offer and kit move up. The graduation bridge doesn't fit under-18s, so the plan would need rework. |
| 2 | **Free path:** a learner can use Codemint for a full school term with no card. | If false, the kit and the adoption job are removed until it is fixed. |
| 3 | **Intern headcount:** none. Interns would be minors, so the funnel is deleted regardless. | No change. |
| 4 | **Owner:** one person, hours unknown. | See the gate. |
| 5 | **Audience:** high schools in Germany and the US. Beyond that, only the Berlin conference is known. | The calendar changes. |

## Job

**Primary job: ecosystem.** The skill allows a second job only when the same components serve both.

## Gate result

| Condition | Evidence | Result |
|---|---|---|
| Free path | None supplied | **Blocked.** Owner: Codemint product or pricing. The kit is pending, not committed. |
| Headcount | None, and interns would be minors | Fails. No internship funnel, and no hiring promise to students. |
| Owner | None named | **Blocked.** Owner: you. Without a named person with a weekly slot, only the offer, piggybacked on an existing verification, survives. |
| Horizon | Unknown | **Blocked.** Owner: sponsor. Needs sign-off on the one-year indicator below. |

## Program shapes

1. **Teacher-led club kit.** Components: a teacher kit and a project showcase. Effort is medium. First result is the next school term. The trade-off is slow reach and dependence on teacher uptake. **Recommended.**
2. **18+ champions.** Components: 18+ champions at schools or youth programs, which is the university design with a high-school feeder. Effort is higher and first results are slower. It can't meet the "14-17 year-old leaders" ask.
3. **Talent-first.** Deleted by the gate.

Pick one before I go further. This plan assumes shape 1.

## Components

Ranked for the ecosystem job (efficiency: champions > offer > kit > funnel). The gate and the age rules reorder this.

| Rank | Component | Decision |
|---|---|---|
| 1 | **Teacher club kit** (faculty-kit analog) | **Kept**, pending the free-path fact. |
| 2 | **Project showcase** (replaces leaderboard and Berlin trip) | **Kept.** It is judged on what students built, not on counts. |
| 3 | **18+ champions** | **Deferred.** Only students 18+ with more than a year before graduating qualify, which is rare in high school. Seniors who turn 18 go to alumni status or the university program. |
| 4 | **Internship funnel** | **Deleted.** Minors, and no approved headcount. |
| 5 | **Student offer** | **Skipped.** Verification and credits are designed for post-secondary students. Under-18s use the separate minors design. |

## Component rules applied

**Teacher club kit**
- No-card path for the whole club: teacher-managed classroom accounts.
- Course-sized modules (assignment, automatic check, slides) delivered through the school's LMS or Git. Never a full Codemint course.
- Solutions and graders go to verified teachers only, in an access-gated place.
- Freeze the kit per term. Ship breaking product changes between terms.
- Expect an IT and privacy review before any school adopts it:
  - **Germany:** a data processing agreement (GDPR).
  - **US:** FERPA terms, since a vendor handling rosters or grades must act as a "school official".
- Roster and usage data never feed marketing. Collect marketing consent outside the classroom.
- The skill requires an accessibility conformance report for public institutions.

**Form (replaces the university form)**
- Collect only what the program needs. Collect no photo.
- Guardian consent captured in the form and documented.
- A school-official sign-off from someone above the teacher. Not every school allows a club to run an external program.
- Per the skill, GDPR consent age varies by member state (13 to 16). Counsel must confirm the German age and US state teen-privacy rules. I can't verify them from the skill alone.

**Roles**

| Role | Age floor | Pay rule | Visa rule |
|---|---|---|---|
| Club sponsor (teacher or adult mentor) | Adult | No payment. Credits and training only. The role is not assigned company work. | Not applicable for the adult's own status. Check the school's rules on outside sponsorship. |
| Student member (13-17) | 13+, with guardian consent | No payment and no cash-value prizes. | Any non-citizen student: no payment or work without clearing with the school's designated official. |
| 18+ champion | 18+, more than a year before graduation | Access perks only. No signup bounties or quotas. | Any payment or travel benefit for an international student must be cleared first (F-1 rules in the legal reference). |

## Calendar

- Pitch the kit a term ahead of the school's materials deadline. US universities lock required materials 45 days to about five months ahead. The skill gives no figures for high schools, so ask each school.
- Germany's school year varies by Land. **Ask.** Don't assume one calendar.
- Club intake at term start, a first showcase at term end.
- Berlin conference date is unknown. **Ask.** Teachers and 18+ students attend. Minors present online.

## Metrics and kill rules

Outputs (schools, clubs, students registered, events) go in an activity log, never in the headline.

| Kind | Metric | Baseline | Target |
|---|---|---|---|
| Leading indicator | Club projects still maintained 3 months after the showcase | None yet | Self-set, to be agreed with the sponsor |
| Leading indicator | Teachers re-adopting the kit for a second term | 0 | Self-set |
| Long-term outcome (hypothesis) | A student content base outside Codemint | None | Not set |

Until the 3-month reading exists, report first-month activity of club members labelled as an "early read".

**Kill rules**
- Fewer than one maintained project per active school after a year → retire that school.
- No teacher re-adopts the kit for a second term → stop authoring new modules.
- A club with no named adult sponsor at term end → retire it.

## Pass thresholds

| Threshold | Result |
|---|---|
| One primary job, every kept component traces to it | Pass |
| Gate shows evidence per condition | Pass, with three **blocked** |
| Every component has an owner and weekly hours | **Blocked.** Owner and hours unknown. |
| Each job has a leading indicator measurable within a year | Pass |
| Student-facing roles state age floor, pay rule and visa rule | Pass |
| Calendar set against the target institutions' own deadlines | **Blocked.** Dates are marked "ask". |
| Every refused ask names its basis | Pass |

## Next actions (answer in this order)

1. Confirm the separate high-school design (see the mismatch above).
2. Confirm the free path: can a learner use Codemint for a whole term with no card?
3. Name the program owner and their weekly hours.
4. Confirm the sponsor accepts the one-year indicator.
5. Send Berlin conference dates and your target schools or Länder and states.
6. Run the guardian-consent form and the German age of consent past counsel. This plan is not legal advice.