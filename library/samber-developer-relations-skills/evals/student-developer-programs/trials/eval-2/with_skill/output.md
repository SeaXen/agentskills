# Vectrix × TU Delft: sanity check and plan

## Direct answer

Don't do it as planned. Three of your four moves break the skill's rules, and the fourth, v3, needs a decision before you commit.

| Your plan | Verdict | Replace with |
|---|---|---|
| Build a full 12-week course | ❌ Never a full vendor course. It can't be built in 4 weeks, and her syllabus is hers. | 2–3 course-sized modules (assignment, auto-check, slides) that slot into her existing weeks |
| Shared Pro API key for 180 students | ❌ Not a no-card path. It's a leaked-key and abuse risk, with no per-student revocation, quota or usage read. | Instructor-managed classroom accounts, or per-student no-card signup with credits capped per student |
| Ask for the roster for lifecycle onboarding | ❌ Refused. Classroom rosters and usage never feed marketing. | Aggregate course usage only. Marketing consent is collected outside the classroom. |
| Ship v3 mid-term with breaking changes | ⚠️ Breaks the per-term freeze and stalls the class mid-term. | Pin the course to v2 for the term. Ship v3 changes to the kit between terms. |

The root problem is that the free tier needs a card above 1 GB. The shared key is a workaround for that, so fix the free path and the key becomes unnecessary.

## Refused asks

1. **Shared Pro key.** It is not a refused ask in the skill's table, but it violates the kit and offer rules (credits "capped per student, never resellable licence keys"). It also gives you no way to cut off one student.
2. **Roster for marketing.**
   - The skill's basis is US FERPA, plus trust everywhere. TU Delft is in the Netherlands, so GDPR purpose limitation and the university's own privacy office apply instead. This isn't legal advice, so route it to TU Delft's privacy office and your counsel.
   - Offer her aggregate course usage (activity per week, assignment completion). Offer students an optional marketing opt-in on a page outside the course.
3. **Full 12-week course.** This is a component-rule violation, not a legal one.

## Job (assumed)

**Adoption after graduation.** You didn't say what the program should change, so this is an assumption (see the table below). It fits a professor-led course. If you actually want hires, the shape changes.

| Assumption | If wrong |
|---|---|
| Job = adoption | Hires: internship funnel moves up, needs headcount evidence. Visibility only: ask which job it serves. |
| Course-sized datasets fit the free path or a no-card classroom path | Free path fails, so no kit until it's fixed. |
| You can spend about 4 weeks of an owner's time | The kit shrinks to the student offer only. |
| One course, one term, 180 students | A multi-course ask means re-run the interview. |

## Gate result

| Condition | Evidence | Result |
|---|---|---|
| Free path | Free tier needs a card above 1 GB. Unknown whether IR course corpora and 180 indexes fit under 1 GB each. | **Blocked.** Owner: professor (dataset sizes) and your pricing owner. If it doesn't fit, it **fails**, and no kit ships until a no-card classroom path exists. |
| Headcount | Not applicable to the adoption job | Internship funnel removed, no hiring promise |
| Owner | No named owner or weekly hours given | **Blocked.** Owner: you. Needs one name and a standing weekly slot. |
| Horizon | No sponsor sign-off on a one-year indicator | **Blocked.** Owner: your sponsor. |

## Program shapes

1. **Classroom-first (recommended).**
   - Contents: a thin kit for her course, a student offer with graduation bridge, and no champions.
   - Effort: about 4 weeks, one owner.
   - First result: the first month of the term, as an early read.
   - Trade-off: one course is a small sample.
2. **Campus-network-first.**
   - Contents: champions at TU Delft plus the offer.
   - Effort: a standing job.
   - First result: a term or more.
   - Trade-off: nothing is ready in 4 weeks, and no club has asked for it.
3. **Talent-first.**
   - Contents: an internship funnel.
   - Why not: deleted by the gate (no headcount evidence).

You asked for a final answer, so I proceeded with shape 1. Confirm or change it.

## Components (adoption order: offer > kit > champions > internship)

The 4-week deadline promotes the offer. The existing professor tie moves the kit up a rung. Both depend on the same missing thing, a no-card classroom path, so build that first.

1. **No-card classroom path, then student offer with bridge.**
   - Instructor-managed accounts, or individual no-card signup.
   - Credits capped per student, with abuse watching and revocation.
   - Expiry at the term end, with a prompt to add a personal or work email beforehand.
   - Post-graduation discount for a fixed window. The level is **blocked**: pricing owner to confirm.
2. **Faculty classroom kit.**
   - 2–3 modules mapped to her syllabus weeks, which you ask her for. Candidates are an ANN indexing lab, a hybrid search and evaluation lab, and retrieval for RAG.
   - Distributed through her LMS or Git.
   - Solutions and graders go to verified instructors only, in an access-gated place.
   - **Frozen to v2 for the term.**
   - Expect a TU Delft IT, privacy and accessibility review. A data processing agreement is likely required because it's the EU. Start now, because this is the schedule risk.
3. **Campus champions:** deferred. Promote only if a TU Delft club asks for help.
4. **Internship funnel:** deleted by the gate.

No student-facing roles exist in this plan, so there is no age, pay or visa rule to set. If TAs help, they are university staff, and any pay goes through the university.

## The v3 decision

1. Ask engineering for a date: does v2 stay fully supported through the end of the term plus a grace period?
2. If yes, pin classroom accounts to v2 and ship v3 changes to the kit afterwards.
3. If v2 sunsets before the term ends, that is a blocker. Either extend v2 for classroom accounts or delay the start.
4. Write a migration guide for v3 anyway, using `version-migration-guide`.
5. Don't make the v3 migration a mid-course exercise. A class stalls when the product changes under it.

## 4-week calendar

I don't know TU Delft's term structure, and a 12-week course may not fit a teaching period there. Ask her.

| Week | Action |
|---|---|
| 0 (this week) | Reply to her. Confirm term dates, materials deadline, privacy and IT review process, dataset sizes. Get the v2 support date. |
| 1 | Decide the no-card classroom path. Start the DPA and privacy review. Name the owner and weekly hours. |
| 2–3 | Build the modules against v2. Run a cold test of each module as a student would, with no card. |
| 4 | Freeze the kit. Hand it to her. Set up the aggregate usage view. |
| Term start | Early read after the first month. |

Pitching a term ahead is the rule, so this term is already late. If the review can't clear in 4 weeks, ship the student offer only and make the kit next term's job.

## Metrics and kill rules

| Kind | Metric | Baseline | Target |
|---|---|---|---|
| Early read | First-month activity of the course's students | none | not set |
| Leading indicator | Share of course students still active 6 and 12 months after the benefit ends | none | self-set once the baseline exists |
| Leading indicator | Her course re-adopting the kit for a second term | 0 | self-set: yes |
| Long-term (hypothesis) | Graduates bringing Vectrix into employers | none | not set |
| Activity log | Students, modules shipped | | |

- **Kill rules.**
  - No second-term re-adoption: stop authoring modules.
  - Bridge retention no better than other free signups after two cohorts: stop spending above the offer.
- With 180 students in one course, read results case by case, not as rates.

## Pass thresholds

- ✅ One job, every component traces to it.
- ✅ Every refused ask names its basis.
- ⚠️ **Blocked.**
  - Free path: dataset sizes and pricing owner.
  - Owner and weekly hours: you.
  - Horizon sign-off: your sponsor.
  - Bridge discount level: pricing owner.
  - TU Delft deadlines and review: the professor.
  - v2 support date: engineering.

## Reply to the professor

- Yes to Vectrix in the course, with a kit of a few modules that fit her syllabus.
- Students use their own no-card accounts, or accounts she manages.
- You'll share aggregate usage with her. You won't ask for a roster.
- Ask her for: term dates, the materials and privacy-review deadline, the assignment slot, and the dataset sizes.

## Questions I couldn't ask

Answer these in order, because they change the plan:

1. What should the program change: adoption, hires, projects, or visibility?
2. Do the course datasets fit the free tier per student, and what does a no-card classroom path cost you?
3. Who owns this, for how many hours a week?
4. Which date does v2 sunset?
5. Is this a one-off for her course, or a standing asset for more courses?
6. What budget exists for credits?