# DevRel org design brief: Corvid Freight, 2026-10-03

**Verdict.** Do not ship the layer as drawn. The two-lead layer is fine at this size if the leads are player-coaches. The 2 and 6 split is wrong for your audience, so rebalance it. Staff documentation and technical-evaluation work first, and events last.

**Not done:** I did not run the 13-question interview, and the work inventory is blank. I have no names, hours or current owners. Everything below rests on your message plus the assumptions marked ⚠️. Fill the inventory before you announce anything.

## Situation

- Funded driver (⚠️ assumed): enterprise adoption. A developer integrates, but the VP of Operations signs the contract after a security review.
- Sponsor (⚠️ assumed): you, inside marketing.
- Trigger: you want a management layer for nine people.
- The headcount does not reconcile.
  - Your plan is 1 content lead + 2 reports + 1 events lead + 6 reports = **10 people**. You said nine.
  - Either one seat is a hire, or one lead is promoted and counts twice, or the numbers are off by one.
  - Does the nine include you? Please confirm.
- Shape threshold: 69% of surveyed teams are under ten people (State of Developer Relations 2024, DevRel.Agency, 310 respondents). The ten-person line below which only centralized fits is this skill's own baseline, adjustable. You sit on it.

## Work inventory (⚠️ blank: fill before approval)

Inventory has no names. Fill all four columns for every surface. Skip this and the chart reassigns work someone invisible already does.

| Surface | Owner today | Manager | Hours/week | If it stops |
|---|---|---|---|---|
| API docs and reference | ? | ? | ? | ? |
| Quickstart, sandbox, sample integrations | ? | ? | ? | ? |
| Security-review pack (data flow, auth, compliance answers) | ? probably nobody, or sales engineering | ? | ? | The VP's review stalls the deal |
| Blog and case studies | ? | ? | ? | ? |
| Community venue | ? | ? | ? | ? |
| Events calendar (meetups, conferences, field) | ? | ? | ? | ? |
| SDKs and changelog | ? | ? | ? | ? |
| Support presence | ? | ? | ? | ? |

Check the security-review pack first. It is not one of the six standard functions. It is the artefact your approver reads, and it is the likeliest unowned surface.

## Reporting line

DevRel reports to marketing, because the funded driver is enterprise adoption and the marketing leader owns it. This line starves the product-feedback loop and technical credibility.
- **Cover:** a standing roadmap slot with the head of product, owned by the content lead.
- **Cover:** a rule that no DevRel surface carries a lead-gen gate.
- **Review:** 2027-04, or immediately if the sponsor changes.

Marketing is the plurality line at 33.1%. No line holds a majority (2024 survey), so this is a trade-off, not a best practice. If the real driver turns out to be sales enablement, the line stays in marketing and sales gets a service interlock. Reporting to sales is the 3.2% outlier.

## Shape: three candidate structures

I use "layer" for a management layer inside one team and one budget. That is still centralized. A split would be two teams under different parents.

**A. Flat centralized, nine direct reports to you, two informal surface owners.**
- Easy: one calendar, one voice, nothing to undo.
- Hard: your span is nine. The general-management sanity check is 5 to 8. That figure is convention, not DevRel data.
- Breaks first: your attention. Every escalation lands on you.
- Wrong when: you also run other work.

**B. Your plan: content lead + 2, events and field lead + 6.**
- Easy: clear spans and two accountable owners.
- Hard: the split is by channel.
  - Conway's Law (Hoopy/Common Room, May 2023) says a team split by channel produces channel metrics and no journey.
  - Your approver reads documents, not talks, so six of ten heads on events puts the weight where your buyer is not.
- Adds: two managers (20% of headcount) and weekly coordination between leads.
- Breaks first: nobody owns documentation, the security pack or the sandbox, because neither lead's remit covers them.
- Wrong when: the VP of Operations is actually reached at field events. Prove that with evidence, not by assumption.

**C. Same layer, split by what the audience needs. Recommended.**
- Lead 1, **Evaluate and integrate**: technical writing, quickstart and sandbox, sample integrations, security-review pack, case studies. About 4 to 5 heads.
- Lead 2, **Reach and community**: advocacy, community, events and field. About 4 heads.
- Easy: every surface the approver or integrator touches has one owner. The journey stays whole inside each lead's half.
- Hard: the awareness-to-enablement handoff between the two leads.
- Breaks first: the handoff. Fix with one shared planning ritual and you as the arbiter.
- Wrong when: the inventory shows events are genuinely the main route to the VP. Then B's weight is right and only B's remit needs fixing.
- Adds the same two managers as B.

**Recommendation: C.** A fails on span, B fails on audience fit. Which numbers fit under which lead depends on the inventory, so treat 4 to 5 and 4 as placeholders derived from audience reasoning, not a benchmark.

Embedded and hub-and-spoke are deleted. At nine to ten people, neither has the staffing floor, and no product line pays for an embedded advocate (⚠️ assumed).

**Leggetter's scaling test** (leggetter.co.uk, 2021): "You're only really scaling a team if further investment increases output more than the increase in input." A lead who only manages two people adds coordination and no output. Make both leads player-coaches. The baseline is at least 50% hands-on work, our number, adjustable.

## Coverage: the six functions

| Function | State | Note |
|---|---|---|
| Technical writing | **owned by this team, staff first** | Approvers read documents. Staffed on 42.7% of teams (2024). If it sits under engineering today, write down the arbiter. |
| Developer-experience engineering | **shared with platform engineering, staff 1 if possible** | Sandbox, SDK samples, webhook and tracking examples. 27.4% of teams (2024). |
| Advocacy | owned, small | 82.2% of teams (2024). Aim at integration walkthroughs and technical credibility with the security reviewer, not conference volume. |
| Community | owned, one person plus a named backup | 52.7% (2024). A hat held by a part-time owner. |
| Developer marketing | shared: DevRel writes, marketing distributes | 37.7% (2024). Do not staff a separate team. |
| Developer education | deliberately refused this year | 35.6% (2024). Fold onboarding paths into docs. No academy or certification. |

Gap outside the six: the **security-review pack**. Owner is Lead 1, with the security team as X-as-a-service. Resolution is to re-scope existing writers, not to hire.

**Events.** I cannot derive a number for events without your inventory. I refuse a ratio. My read: six heads is the most likely over-allocation. Derive the number from events-surface hours, and move any surplus to documentation and DX engineering.

## Roles

| Seat | Surfaces owned | Backup | Capacity |
|---|---|---|---|
| Lead 1, Evaluate and integrate | docs, security pack, roadmap slot | named senior writer | 70% planned |
| Lead 2, Reach and community | advocacy, events, community | named senior advocate | 70% planned |
| ICs (⚠️ names needed) | one named surface each | one named backup each | 70% planned |

- **70% ceiling** is our baseline, adjustable.
- **Bus factor:** any surface with one owner and no backup is a flagged risk. Likely candidates are the security pack and the sandbox.

## Interlocks

Each adjacent team gets one mode. Arbiter names are blanks for you to fill.

- Product: collaboration during launches, X-as-a-service otherwise. Developer feedback in, roadmap and dates out. Arbiter: head of product.
- Platform engineering: facilitation. Technical review in, writing coaching out. Arbiter: engineering manager.
- Support: X-as-a-service. Failure signals in, troubleshooting pages out. Arbiter: support lead.
- Sales and sales engineering: X-as-a-service, capped in hours per week (cap is yours to set). Security-review pack out, field objections in. Arbiter: you.
- Security or compliance: X-as-a-service. Approved answers in, pack out. Arbiter: CISO or equivalent.
- Marketing: collaboration on campaigns, X-as-a-service on distribution. Arbiter: marketing head.
- Customer success: X-as-a-service. Adoption blockers in, reusable guides out. Arbiter: CS lead.

## Ladder and titles

- Which ladder: ⚠️ unknown. A marketing ladder levels on campaign ownership, which does not describe docs or DX work. Adopt a DevRel-specific or engineering-based ladder before the two leads are levelled.
- "Lead" maps to a manager of two. Keep the title at manager level until the team passes the ten-person line.
- Span check: two leads for you, and two or six reports under each. General-management practice says 5 to 8. Check B's six-report lead against this, and expect Lead 1 and Lead 2 in C to land in range.

## Budget

- Headcount owner: ⚠️ confirm.
- Program owner: ⚠️ confirm.
- Staff salaries sit outside the DevRel program budget in 60% of surveyed programs (2024), so the person who approves an event is often not the person who approves a hire.

## Re-org triggers

- The funded driver changes, or the sponsor leaves.
- A second team starts running developer work without an interlock.
- Any surface sits at bus factor one for a quarter.
- The team declines the same request category three times for lack of coverage.
- The security-review pack becomes the bottleneck on three consecutive deals.
- An interlock stays in collaboration mode past its launch.

## Transition

- **Week 1:** fill the inventory and confirm headcount. Publish the surface owners.
- **Month 1:** name the leads. Write ladder criteria. Start the roadmap slot and the security-pack interlock.
- **Quarter 1:** move events surplus into docs and DX engineering. Review backups.
- **Unchanged:** reporting line, refused education scope.

## Quality gate

- ❌ Inventory has no named owners. Needs your data.
- ✅ Reporting line names driver, leader, starved pillar and cover.
- ✅ Shape justified by coordination bought. Embedded and hub-and-spoke deleted.
- ✅ Six functions each carry a coverage state.
- ⚠️ Bus factor and 70% capacity cannot be checked until the inventory exists.
- ✅ Every interlock has one mode and an arbiter slot. Arbiter names are blank.
- ✅ Numbers carry a source and year, or "our baseline, adjustable". No ratios, no pay bands.
- ✅ Re-org trigger list is observable without a survey.
- Survey figures are 2024. I did not re-check for a newer edition today.

**Next, five minutes:** reply with the count (nine including you or not) and which function each of the nine does today. I then fill the inventory and fix the Lead 1 and Lead 2 head counts.