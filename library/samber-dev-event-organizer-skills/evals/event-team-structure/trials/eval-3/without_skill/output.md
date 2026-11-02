# VantiqCon structure: org design brief

**Recommendation: don't spin up the non-profit yet.** Fix decision rights inside Vantiq first. Run VantiqCon as a named internal program with a charter, a program owner, and a split between who decides the agenda and who decides spend. Revisit the association against the triggers in section 6.

I didn't interview you, so I've labelled my assumptions. Correct any that are wrong, because several change the answer.

## 1. Situation

- **The pain is decision rights.** Nobody knows who decides the agenda versus who decides spend. That is a governance gap, and a legal entity doesn't close it.
- **A non-profit would inherit the same confusion.** It would add a board, a bylaws fight, and a trademark negotiation on top. You'd be arguing over who decides things, with lawyers present.
- **What I assumed.**
  - Marketing owns the budget and the headcount.
  - The conference exists to serve users and produce pipeline and retention for Vantiq.
  - "Community money" means sponsorships, ticket revenue and possibly grants or donations.
  - You haven't picked a jurisdiction. The details of a US 501(c) versus a French loi 1901 association differ a lot, and counsel would settle them.
- **The funded driver.** I assumed adoption and retention of existing users, with some pipeline. If the real driver is neutrality (competitors and partners co-owning the event) or a standards effort, my answer changes. See the triggers.

## 2. What a non-profit buys and costs

| Buys | Costs |
|---|---|
| Perceived neutrality, so competitors and partners sponsor more easily | Vantiq loses unilateral control of agenda, brand and money |
| Eligibility for grants and tax-deductible donations (jurisdiction-dependent) | A board, bylaws, annual filings, audit or accounting, and separate insurance and banking |
| A separate identity | A trademark and brand licence from Vantiq, which needs negotiating and can be revoked or contested |
| Legitimacy for volunteer organizers | Private-benefit limits: staff time, speaking slots and leads can't flow back to Vantiq freely |
| | A quarter or more to stand up and a long time to unwind |
| | You, as a DevRel lead, becoming an unpaid association officer |

Most of the benefits don't apply to you yet:

- **Sponsors already pay companies.** Vendor-run user conferences take sponsor money routinely. Vantiq can sell sponsorships from its own books today.
- **Neutrality is a real gap only if** you want rival vendors on stage and in the sponsor hall. If you don't, it's irrelevant.
- **Grants and donations** are marginal for a B2B user conference at this scale.
- **Funding is not your problem.** Marketing already funds the event in full. The problem is who decides.
- **The costs are mostly irreversible.** You'd lose control and take on a board, in exchange for benefits you can't yet name.

## 3. Candidate structures

All three need the decision-rights charter in section 4. They differ only in where the conference sits.

**A. Internal program with a charter (recommended).**
- VantiqCon becomes a named program inside DevRel, with one accountable program owner.
- An Agenda Committee holds a community seat, and a sponsor policy is written down.
- *Makes easy:* clarity within weeks, no legal work, reversible.
- *Makes hard:* sponsors who want neutrality will still see a vendor event.
- *Assumes:* the staffing in section 5, with no new headcount.
- *First thing to break:* engineering loans each year. The Agenda Committee needs engineering seats.
- *Wrong pick if:* you need competitor participation to make the event work.

**B. Internal program plus an external Community Advisory Board.**
- This is A, plus a board of customers, partners and maintainers. It advises on agenda and sponsor policy and has no spending authority.
- *Makes easy:* it delivers most of the "community identity" benefit without a legal entity.
- *Makes hard:* it adds a standing meeting and an expectation that Vantiq acts on its advice.
- *Wrong pick if:* the board would be ignored. An advisory body nobody listens to costs trust.

**C. Separate non-profit association.**
- *Makes easy:* neutrality, grant access, independent brand.
- *Makes hard:* everything in the cost column above.
- *First thing to break:* the trademark licence and the cost sharing with Vantiq.
- *Wrong pick if:* you haven't settled A first. Today that is the case.

**Order by efficiency: A > B > C. Recommend A now, with B added once A is stable.**

## 4. Decision rights charter (draft for you to approve)

Write this as one page and have the budget owner sign it.

| Decision | Decides | Consulted | Informed |
|---|---|---|---|
| Strategy: goals, audience, budget ceiling | Marketing VP (budget owner) | DevRel lead, engineering sponsor | Exec team |
| Agenda: themes, tracks, speaker selection | Agenda Committee, chaired by the DevRel lead. Includes an engineering lead, a customer or community member, and the program owner. | CAB (once it exists), product | Marketing |
| Spend within the approved budget | Program owner | DevRel lead | Marketing finance |
| Spend above a threshold or off-plan | Marketing VP | Program owner | |
| Sponsor policy: who may sponsor, what they get, no speaking slots for sale | DevRel lead, approved by Marketing VP | Legal | Sales |
| Engineering contributors: scope and time | Engineering sponsor commits capacity in writing each year | DevRel lead | |
| Tie-break between agenda and spend | Marketing VP | | |

Rules that make it work:
- **One program owner.** Name a person, not a team. They run the plan, the timeline and the vendors.
- **A hard line between agenda and spend.** The committee chooses what is on stage but can't commit money. The owner commits money within budget but can't change the agenda. This split fixes the confusion you described.
- **Sponsors never buy agenda.** Sponsor-bought slots are labelled and capped, or not offered. Write this down; it protects the event's credibility with attendees.
- **The engineering loan is a commitment.** The engineering sponsor allocates named people and hours each year, in writing, before the agenda opens. "Whoever we can pull in" becomes a plan.
- **A year-round calendar.** Fixed milestones for CFP open, close, notifications, sponsor sales, and a go/no-go gate. Dates don't move without the owner and the Marketing VP agreeing.

## 5. Team and capacity

- **Today:** you, two marketing people, and engineering loaners.
- **Suggested split.**
  - *Marketing person 1:* registration, attendee marketing, sponsor sales operations.
  - *Marketing person 2:* logistics, venue, vendors, budget tracking.
  - *You:* agenda chair and speaker quality.
  - *Program owner:* one of the above. It should be whoever you can free from other work. If that is you, you can't also chair the agenda.
- **Bus factor.** Every surface needs a named backup: venue, sponsors, CFP, A/V. Flag any that depend on one person.
- **Capacity.** Plan to roughly 70% of declared capacity (a planning baseline, adjustable, not a benchmark), because launches and support will eat the rest. A 1,100-person event with this team probably already exceeds that. If so, cut a surface, don't add a legal entity: fewer tracks, fewer side events, or an outsourced logistics vendor.
- **Contracting.** Event logistics is a good candidate. A contracted surface still needs one internal accountable owner.

## 6. When to revisit the association

Reopen the non-profit question when you can observe any of these:

- Competitors or partners tell you they won't sponsor or speak because Vantiq controls it.
- Community members want a governing say in the agenda or the money, beyond advising.
- Sponsor or donation revenue is large enough that keeping it inside Vantiq's books creates a real tax or accounting problem. Legal and finance would confirm this.
- The event grows into something Vantiq wants to run as a neutral industry standard, not a user conference.
- Marketing funding is cut and external money becomes necessary to survive.

If you reach that point, compare the association with a lighter alternative before choosing it: a fiscal sponsor or an existing foundation or trade body that hosts the event under its umbrella. That gives neutrality and tax status without you forming and governing an entity.

## 7. Transition

- **Week 1:** Get the Marketing VP's agreement to the charter in principle. Name the program owner and the engineering sponsor.
- **Month 1:** Publish the one-page charter. Form the Agenda Committee. Write the sponsor policy.
- **Quarter 1:** Run next year's planning on the new calendar. Commit engineering capacity in writing. Track the budget against the plan.
- **Before the next event:** Decide on the CAB (structure B). Measure with the numbers below.

## 8. Success measures

Report these quarterly:
- Cost per qualified conversation, and pipeline or expansion influenced, with the event tagged in the CRM. Treat registrations and badge scans as vanity metrics.
- Whether the agenda and spend decisions were made on the calendar's dates.
- Engineering hours committed versus delivered.

## 9. Open questions that could change my answer

1. Is Vantiq's goal for VantiqCon pipeline, retention or community? I assumed retention and community.
2. Do you want competitors or neutral third parties on stage?
3. How large is sponsor revenue, and does marketing keep it or does it offset cost?
4. Which jurisdiction would the entity sit in?
5. Who are the people who proposed the non-profit, and what problem do they want it to solve? If the answer is "its own identity", structure B delivers that without the entity.