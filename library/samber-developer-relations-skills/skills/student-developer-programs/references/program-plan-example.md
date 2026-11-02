# Worked plan and negative example

## Situation

Ledgerline sells a managed event-streaming service. The head of DevRel was asked by the CEO to "launch a student ambassador program in 30 universities this year, $25 per signup". Interview answers:

1. Job: the CEO wants "more developers knowing us when they join companies". Adoption.
2. Free tier exists, no card, but capped at a load a class project fits inside. No student offer yet.
3. No intern headcount this year.
4. Customers mostly in Germany, France and the Netherlands. One professor in Lyon already uses the product in a distributed-systems course.
5. Universities only.
6. Owner: one developer advocate, 6 hours a week. Small credits budget.
7. A result before the next annual budget review, about 11 months away; the CEO wants a standing asset.
8. Nothing tried.

## Plan

**Refused asks**

- $25 per signup: bounty buys fake signups and makes the role look like work. Replaced by access perks.
- "30 universities" as the target: an output. Replaced by the leading indicator below, with campuses kept in the activity log.

**Job:** adoption after graduation.

**Gate**

| Condition | Evidence                                 | Result                                         |
| --------- | ---------------------------------------- | ---------------------------------------------- |
| Free path | Free tier, no card, fits a class project | Holds                                          |
| Headcount | None this year                           | Fails: no internship funnel, no hiring promise |
| Owner     | One advocate, 6 h/week                   | Holds for two components, not a campus network |
| Horizon   | CEO signs off a one-year indicator       | Holds                                          |

**Chosen shape:** classroom-first (offered: classroom-first, campus-network-first; talent-first deleted by the gate).

**Components**, adoption efficiency order:

1. Student offer with graduation bridge: student credits on top of the free tier through an existing verified-student service; expiry at the verified end date; 12 months at a discount after graduation (self-set); a prompt to add a work email before expiry.
2. Faculty kit: three modules (producer, consumer group, exactly-once lab) for the Lyon course first, then two more courses. Pitched in October for the spring term, frozen per term.
3. Campus champions: deferred. The re-rank promotes them only if a club asks for help; none has.
4. Internship funnel: deleted by the gate.

**Calendar:** Lyon course spring term; kit modules ready a month before that school's materials deadline (ask the professor for the exact date). Next pitches go out before the autumn deadlines.

**Metrics**

| Kind                           | Metric                                              | Baseline | Target                                                     |
| ------------------------------ | --------------------------------------------------- | -------- | ---------------------------------------------------------- |
| Leading indicator              | Verified students active 6 months after benefit end | none yet | self-set: above the 6-month activity of other free signups |
| Leading indicator              | Courses re-adopting the kit for a second term       | 0        | self-set: 2 of 3                                           |
| Long-term outcome (hypothesis) | Accounts adding an employer email within 2 years    | none     | not set                                                    |
| Activity log                   | Campuses, students verified, modules shipped        |          |                                                            |

**Kill rules:** no course re-adopts the kit for a second term → stop authoring modules. Bridge retention no better than other free signups after two cohorts → keep the offer, stop spending above it.

**Pass thresholds:** all pass except the bridge discount level, **blocked**: pricing owner to confirm the discount.

## Negative example

```
✗ Bad
Student Ambassador Program
- Recruit 30 ambassadors (one per university), pay $25 per verified signup
- Ambassadors host 2 events a month and post weekly on LinkedIn
- Give every .edu email 12 months free
- KPIs: universities reached, ambassadors enrolled, events held, signups
- Rationale: students become enterprise buyers in 5-10 years
```

What is wrong with it:

- Bounty plus monthly quotas: fake signups, and the role looks like unpaid work.
- One ambassador per campus with no term or successor: each chapter dies at graduation.
- `.edu` only: excludes the target countries, where student addresses use other domains or none, and invites resale abuse.
- No bridge: every account ends at the moment the student starts working.
- Every KPI is an output. The rationale cites a lag nobody has measured.
- No age, pay or visa rule for any role.
