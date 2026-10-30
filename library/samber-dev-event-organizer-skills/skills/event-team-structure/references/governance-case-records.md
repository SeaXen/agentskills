# Governance case records

The case records behind the skill's entity, decision-rights, and paid-hire menus.

## The three decision-rights shapes, with named instances

Recurring tech events fall into one of three shapes. The board-plus-organizers split recurs at every scale from a 300-person conference to a 12,000+-person one, which is why the skill names it the default.

1. **Board-plus-organizers split** - a board/staff layer holds budget, contracts, legal and trademark authority; an operational team holds program and logistics decisions. Instances:
   - EuroPython Society board vs. workgroups.
   - DEFNA board vs. DjangoCon US conference committee.
   - Ruby Central board and Executive Director vs. conference operations.
   - PSF board/staff vs. PyCon US Chair and committee.
   - CNCF staff vs. program committee and co-chairs.

   In every case, code-of-conduct enforcement escalates to the board/staff layer or a dedicated CoC team, never staying at the operational level.

2. **Domain-lead federation** - named leads each hold real authority in their own lane. Purest instance: JSConf across events (below). Within a single event: FOSDEM devroom managers hold full content autonomy over their track; DjangoCon US splits authority across named chairs (Program, Sponsors, A/V, Opportunity Grants…), each with real decision rights in their lane.
3. **Consensus / committee** - the group decides, no single named leader. Instances: EuroPython workgroups (internal voting rights), FOSDEM devroom teams (own CFP, review, selection as a self-governing unit).

## PyCon US / PSF - staff-plus-volunteer hybrid

- Owned and run by the Python Software Foundation, a 501(c)(3). Paid staff:
  - A Program Director (hired August 2021) as "the lead planner" for PyCon US.
  - A Community Events Coordinator (hired January 2025) for onsite logistics, vendors, expo floor.
  - A Finance Manager and Controller for money.
- Volunteer leadership: the PyCon US Chair (formalized as a PSF officer position on March 14, 2008 - a documented formalization event) and a PyCon US Committee driving program and community decisions. On-site: named volunteer roles (Session Chairs, Session Runners, Green Room, Registration, Wayfinders) filling "over 300 on-site volunteer hours."
- The split is genuine: the volunteer Chair carries real program authority even though the event has paid staff - not a figurehead over a staffed operation.

## EuroPython Society - governance _as_ the succession mechanism

- A Swedish non-profit association, founded 2004, rebooted 2012, owning the EuroPython trademark. Board of up to 9 directors, elected annually at the General Assembly; the board "collectively takes up the fiscal and legal responsibility."
- Workgroups were introduced for the 2015 edition explicitly "to help implement the EuroPython organization without losing institutional knowledge every time the location changes" - governance redesigned to solve a succession problem, not to distribute workload. The board retains Finance and Conference Administration (contracts, venue, ticketing, insurance); workgroups own Sponsors, Communications, Program, CoC, etc., and are re-confirmed by board vote every year.
- Permanent workgroup members keep voting rights year to year, "allow[ing] non-voting members to become voting members in the following year" - a deliberate contributor-to-decision-maker pipeline.
- The structure was revised once already (2022) "to have a more balanced workload… and give more autonomy… while reducing the silos between teams" - evidence a governance design is a revisable artifact, not a founding constitution.
- Financial-continuity benchmark: a former chair reported a disaster-recovery reserve sized so the society could "lose the complete budget for a single in-person conference edition (around 600k EUR) without going bankrupt."

## DjangoCon US vs. DjangoCon Europe - the natural experiment

Both conferences share a parent (the Django Software Foundation) and a community, isolating the standing-team design choice as close to a controlled comparison as this domain offers.

- **DjangoCon US:** organized since 2015 by DEFNA (Django Events Foundation North America), a standing 501(c)(3). The board (President, VP, Treasurer, Secretary) carries legal and financial continuity; conference chairs (Conference, Program, A/V, Sponsors, Opportunity Grants, Volunteer, Website, Onsite, Visas, plus a CoC team most organizers are cross-listed onto) rotate beneath it. DEFNA stays volunteer-board-run and uses professional event-management vendors and hotel contracts instead of hiring employees.
- **DjangoCon Europe:** no standing organizer - a new volunteer host team in a new country bids for each edition, licensed by the DSF. Documented failure modes of the full-rotation design:
  - The pandemic left one team (Porto) "organizing DjangoCon Europe for the third time in a row" when no new host could be recruited.
  - Organizers named "challenges we faced in 2021 with finding new hosts."
  - A 2026 call getting "three viable proposals, a clear improvement over recent years" shows the host pipeline stayed fragile even for an established, well-supported event.

  The DSF layered patches on top: a support working group of previous organizers, and a "DSF Events Support" function from 2027.

- The conclusion the comparison forces: because DEFNA persists as the legal entity, DjangoCon US survives even as its volunteer chairs rotate - the opposite design choice from DjangoCon Europe, and demonstrably more stable. This is the strongest single piece of evidence for the standing-entity recommendation.

## KubeCon / CNCF - rotation over a standing continuity layer

- Three tiers:
  - CNCF/Linux Foundation staff own budget, logistics, and venue.
  - A volunteer Program Committee of subject-matter experts scores submissions (top-scored 30% advance to track chairs).
  - Co-chairs, "chosen by CNCF… on a rotating basis for each conference and are professionally contracted and compensated," finalize the schedule.
- Continuity comes entirely from the staff layer underneath - no volunteer or contracted role persists across editions. This is deliberate leadership rotation as a working design, and it only works because the standing body absorbs the institutional knowledge. Scale: 12,000+ attendees (EU 2024) run by staff plus a committee plus three named co-chairs - a strikingly small named leadership layer.

## FOSDEM - the all-volunteer outlier

- 8,000+ attendees, no paid staff at all. A small core team plus volunteer coordinators handle venue, network, video, and logistics; devrooms are self-organized tracks (2024: 948 speakers, 875 events, 67 tracks) running their own CFP, review, and moderation. The central team keeps authority over devroom acceptance and shared infrastructure.
- The bus-factor rule: FOSDEM "request[s] every devroom to have two people" as managers "to make sure there is a backup in case of issues" - an enforced operating rule, not a principle.
- Explicitly not replicable for most organizers: the model depends on a decentralized structure and an unusually large recurring volunteer pool, and still concentrates real risk on a small core team.

## JSConf - the franchise federation

- In the organizers' own words: "We essentially treat the JSConf event as a franchise model where the event is run entirely by the local individual or team. They handle all financial dealings, they arrange the schedule, they plan out the venue, the parties, and everything else." The only central guardrail: "You must have an existing JSConf organizer as oversight" - a brand check and a mentor, not a board. No shared entity, finances, or staff.
- When the flagship (JSConf EU) ended, the brand and logo were contributed to the OpenJS Foundation - what happens to a federation's central asset when its coordinating mentor-event disappears.

## Team-size benchmarks by event scale

| Scale                                                    | Standing team observed                                                                                                                                                                                                   |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ~100-person meetup                                       | 1 lead + 2-4 co-organizers; practitioner workload estimate "at least 4 to 8 hours a month." ~35% of surveyed meetup groups run on a single organizer (see the burnout evidence reference).                               |
| ~300-person conference (DjangoCon US)                    | 15-20 named chair roles beneath a small standing board, plus day-of volunteers.                                                                                                                                          |
| ~1,600-person conference (JSConf EU 2019, final edition) | 6 core organizers, 8 MCs, 17 volunteers - roughly one core organizer per ~270 attendees. The cleanest documented figure available, from the event's own closing statement - and the team size that proved unsustainable. |
| Multi-thousand (PyCon US)                                | PSF paid staff (Program Director, Community Events Coordinator, finance roles) + volunteer Chair/Committee + 300+ on-site volunteer hours.                                                                               |
| 8,000+ (FOSDEM)                                          | 60+ devrooms at two managers minimum each, a large day-of volunteer pool, a core "numbering in the dozens," zero paid staff.                                                                                             |
| 12,000+ (KubeCon EU 2024)                                | Foundation staff + volunteer program committee + 3 contracted rotating co-chairs.                                                                                                                                        |

**The honest limit:** the industry has no rigorous, generalizable organizer-to-attendee ratio. The JSConf EU figure is the best available real example, not a formula - and it comes from a team that concluded it had exceeded "what can be responsibly handled by our volunteer team."

Sanity check only, borrowed from generic corporate org design: one coordinating lead or board handles roughly 5-8 direct functional leads before the structure needs another layer. Use it to notice strain, never to enforce a number.

## First-paid-hire evidence

| Event                | What happened                                                                                                                                                                                                                                                                                                                                                   |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PyCon US / PSF       | Hired a Program Director (2021), then a Community Events Coordinator (2025). The paid role is event-planning execution; program and community leadership (the Chair) stays volunteer.                                                                                                                                                                           |
| EuroPython Society   | Moved from all-volunteer to part-time Event Managers - the board drafted its first Letter of Engagement in December 2024 and planned "hiring the second part-time Event Manager in the EP2026 location," framed as outsourcing administrative conference tasks. A live, dated first-hire example at ~1,000-1,500+ attendees and a ~€600k single-edition budget. |
| Ruby Central         | A paid Executive Director - a more senior first-hire pattern (four EDs since 2022), alongside a board expanded to six.                                                                                                                                                                                                                                          |
| DEFNA / DjangoCon US | Never hired staff - professional event-management vendors and hotel contracts instead. The documented middle path between all-volunteer and employment.                                                                                                                                                                                                         |
| FOSDEM               | Stays fully volunteer at 8,000+ attendees - the deliberate outlier, explicitly not a model for most organizers.                                                                                                                                                                                                                                                 |

**The threshold, across cases:** the first paid hire is consistently an operations role - an event coordinator/manager everywhere except Ruby Central, which hired a senior Executive Director - and never a community manager in any case. It appears when the event reaches roughly the low-thousands of attendees and/or a six-figure budget and organizing becomes a year-round burden. Sub-500-person events in the record stayed volunteer-run throughout.
