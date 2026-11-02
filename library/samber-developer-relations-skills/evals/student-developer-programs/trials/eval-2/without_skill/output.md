**Next action (15 min):** Email her the 6 questions in step 1 below. Don't build anything until she answers.

## Verdict

| Your plan | Verdict | Why |
|---|---|---|
| Build a full 12-week course | ❌ Cut down | She owns the syllabus. 4 weeks is too short to build and test 12 weeks. v3 would break it mid-term. |
| One shared Pro key for 180 students | ❌ Replace | One leak or runaway loop hits everyone, and you can't tell who did it. |
| Ask for the student roster for lifecycle emails | ❌ Drop | GDPR and Dutch consent rules. Details below. |
| v3 breaking changes mid-term | ⚠️ Fixable | Freeze v2 for the term. Offer v3 as an optional end-of-term module. |
| Free tier needs a card above 1 GB | ⚠️ Fixable | Students can't be asked for cards. Use a sponsored org. |

## 1. Questions to ask her first

1. Which weeks or labs should use a vector DB? Likely 3 to 4 of 12.
2. Which datasets? MS MARCO and BEIR corpora exceed 1 GB, so size them.
3. Does she want a vendor-neutral comparison (BM25, FAISS, pgvector, Vectrix)? IR courses usually do.
4. Which weeks are graded, and which are deadline weeks?
5. Do students work solo or in groups?
6. Does TU Delft have a privacy or procurement process for third-party tools?

## 2. What to build

Build a lab pack of 3 to 4 labs, not a course. She teaches and you supply the material.

- Lab 1: first index and query. Target under 10 minutes to the first call.
- Lab 2: dense vs BM25 retrieval, evaluated with nDCG.
- Lab 3: hybrid search and filtering.
- Optional Lab 4: v3 migration, used as a graded or extra-credit exercise.
- Ship a starter repo and a pinned dataset that fits the quota.
- Cost: about 2 to 3 weeks of work, instead of 12 weeks of content.

## 3. Access, not a shared key

Replace the shared key with one of these, in this order:

1. **Sponsored org.** Create a "TU Delft IR" org with per-student scoped keys and a quota per student. Students join through an invite link or class code. No card is needed. Each key is revocable on its own. Every call is attributable to a student.
2. **Credit code.** Students redeem a code on a normal account. This is simpler, but it is less controllable.
3. **Fallback.** One shared key held by the instructor, used only for live demos. It is never given to students.

Before you promise anything, get the cost per student. Estimate storage, queries and rate limits for 180 students, and add 3x headroom for the deadline week.

Metrics: count activated students (first query made) and labs completed. Do not count paid conversions. Students are future buyers, not revenue now.

## 4. The roster

Don't ask for it. She probably can't legally hand it over, and marketing emails need opt-in under Dutch and EU rules.

- Students sign up themselves through the join link.
- Onboarding emails stay transactional: key issued, quota warning, v3 notice.
- Product marketing gets a separate, unticked opt-in checkbox at signup.
- If she wants to share a roster for support, TU Delft needs to approve it. That likely means a data processing agreement and her privacy office, and it covers support use only.
- The lifecycle team can build the onboarding sequence on signup events, not on a roster.

## 5. v3 mid-term

1. Tell her now, before she commits.
2. Pin the course to v2 through the end of term plus 4 weeks. Use the API version pin. Don't remove v2 inside that window.
3. Test every lab against the v3 beta, so you know the delta before v3 ships.
4. Publish a migration guide with before/after code for each breaking change. Run it cold on a lab repo before release.
5. Offer v3 migration as an optional last-week module, only if v3 is stable by then.
6. Don't let v3 changes reach the course repo or the sponsored org mid-term.

## 6. Timeline (4 weeks)

| Week | Do |
|---|---|
| 1 | Send questions. Agree scope. Size cost per student. Start the privacy check. |
| 2 | Build the sponsored org and the join flow. Draft Labs 1 and 2. |
| 3 | Draft Labs 3 and 4. Cold-test all labs on a clean machine. Set the v2 pin. |
| 4 | Give her the lab pack and run a TA walkthrough. Load-test at 180 users. Set up support. |

Work is roughly 6 to 8 person-days. Have a named owner for support during the term.

## Draft email to her

> Thank you, we would be glad to support your course. We can provide a lab pack for the weeks that use a vector database, plus free access for every student without a credit card. To set this up, could you tell us: (1) which weeks and datasets, (2) whether you want a vendor-neutral comparison, (3) the graded deadlines, and (4) whether TU Delft needs a privacy or procurement check for third-party tools? Students will join through an invite link, so we don't need a roster. One heads-up: we ship a major API version this term. We will keep the current version available through the end of your course so nothing changes under you.

## Decisions for you

1. Who owns support during the term: you, a DevRel person, or her TAs?
2. Is the sponsored org feasible in your billing system in 2 weeks? If not, use the credit-code route.