**Work on 1, 4 and 5. Drop 2 and 3. Only item 5 is a certification-program task, and it can't be designed yet.**

Next action: send the 3 gate questions under item 5 to whoever proposed the badge (about 10 minutes).

## Triage

| # | Ask | Verdict | Where it goes |
|---|---|---|---|
| 1 | Nimbletide connector "Veldora Certified" | Work on it, different skill | `samber/developer-platform-skills@app-marketplace-review` |
| 4 | Build a Veldora Academy? | Work on it, first | `samber/developer-relations-skills@developer-education-strategy` |
| 5 | Badge for consultants who build on you | Work on it, gated | This skill: gate first, no build yet |
| 2 | HR skills matrix, 40 engineers | Drop | HR or L&D owns it |
| 3 | Your Terraform Associate exam | Drop | Personal prep, out of scope |

## Why each verdict

**1. Nimbletide connector.**
- A certification program credentials a person. Your connector is an app, so this is a marketplace review.
- It is the only item with a named partner waiting, so start it first.
- "Veldora Certified" on a connector will collide with any later person credential. Pick distinct names now: for example "Veldora Verified" for apps and a skill-badge name for people. This is my judgment, not a sourced rule.
- Review criteria, and the answer to "what does Nimbletide get": the app-marketplace-review skill. Install it from the sibling repo if it is missing.

**2. HR skills matrix.**
- It is an internal employee tool. No outside reader relies on it, so it is out of scope for credentialing.
- Tell HR it belongs to their L&D owner. The platform team can supply the task list of what a Veldora engineer does.
- Do not reuse it as a blueprint for the consultant badge. Different readers, different stakes.

**3. Your Terraform Associate.**
- The exam is someone else's, and a candidate preparing for another vendor's exam is out of scope here. I stopped.
- If you want a study plan, ask separately. I haven't checked HashiCorp's current exam details.

**4. Veldora Academy.**
- This decides items 5 and (partly) 2, so run it first.
- It answers whether structured education is worth funding at all. A credential question only comes back here once it says yes.
- Do not let leadership's question turn into "build the exam". An academy and a credential are separate spends.

**5. Consultant badge.** The gate result is "undetermined", and without a named consumer it fails.
- "Someone suggested it" names no outside consumer and no action.
- A badge nobody outside Veldora acts on becomes a vanity badge. The right substitute is a public learning path or a showcase.
- Hard rule from the skill: a requirement your own company writes (for example, partner tier) does not count as outside demand without buyer evidence.

## Item 5 gate: 3 questions to answer

1. **Who outside Veldora acts on it?** Clients choosing a consultant, tenders counting certified people, hiring managers, or only the holders?
2. **Who are the candidates, and how many per year?** How do their clients find and shortlist them today: referrals, a partner directory, tenders, CVs?
3. **What effort ceiling?** Owner hours per week, a named successor, budget, and whether you can carry a commitment you cannot withdraw once holders exist.

The full interview has 7 more questions (deadline, role, existing courses, release cadence, break-even, privacy). Ask them only if the gate passes.

## If the gate passes: the expected design

This is the default for consultants whose clients shortlist them. It assumes answers I don't have, so treat every figure as self-set.

- **Tier ceiling: skill badge.** Role certification needs all three of these. None is visible yet:
  - a buyer contract or job posts that name certified people;
  - two years of funded re-alignment;
  - a standing owner for the item bank.
- **Level: one.** An "Associate"-style name carries the skill-badge tier.
- **Format:** auto-graded hands-on tasks in disposable tenants. Add a 15-minute live explanation on a sample of passes, because an AI agent can reach the same end state unattended.
- **AI policy:** allowed, worded as "competence with your own tools".
- **Identity:** account login. Skip face matching, so no biometric privacy review is needed.
- **Renewal:** stamped with the Veldora major or API version, no expiry. A short delta task on each new major version.
- **Verification:** Open Badges 3.0 plus an opt-in "find a certified consultant" directory. For consultants, client leads from that directory are the return on the exam fee.
- **Fee:** break-even per attempt from your own costs, small enough that one engagement repays it. Seat bundles for services firms.
- **Prep:** a free practice quiz plus a course on a MOOC or edtech platform. Keep the assessed exam off that platform.
- **Expert level, later:** human-reviewed client project plus live defence, never an exam. It needs a named client asking for the distinction.
- **Kill rule:** set a number and a date before launch, for example no client-driven engagements citing the badge within 18 months. Self-set.
- **Upgrade trigger:** the first tender or buyer contract that names certified people, plus two years of funded re-alignment.

## Order and time

1. Today: send the item 5 gate questions (10 min) and hand item 1 to the marketplace review skill (30 min to scope).
2. This week: run developer-education-strategy for item 4 (about 2 hours with leadership input).
3. After 1 and 2: if the gate passes, draft the charter section by section, about 150 owner hours over about 4 months (self-set, from the skill's worked example).

HR and your Terraform exam need nothing from the platform team this week.

Next: ask the proposer of the badge question 1, "who outside Veldora will act on it, and how?"