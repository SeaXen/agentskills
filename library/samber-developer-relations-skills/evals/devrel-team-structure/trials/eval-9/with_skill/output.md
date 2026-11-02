# DevRel org design brief — Vantor Mesh

## How to read this

This is a first-pass brief, not a live-interviewed one — I don't have named owners, real hours, or a stated funded driver, so several inputs below are marked **[confirm]**. Where a number is sourced, it's labeled with its source; where it's this skill's own baseline, it's labeled as adjustable; nothing here is an invented ratio.

**Bottom line up front:** the VP Product's proposal bundles two decisions that don't need to travel together. The reporting-line move (product → marketing) is plausible and probably right. The shape move (split into two pods with separate leads) is very likely wrong at this headcount, and the real cause of two missed quarters is almost certainly surface overload, not the parent org. Fix coverage first. Don't split until the team clears roughly eight people.

---

## Situation

DevRel is 5 people, has sat under product for 18 months, and has missed every goal two quarters running. A new VP Product, one month into the role, wants to (a) move the team to marketing and (b) split it into a content pod and a community pod, each under its own lead.

**Trigger:** new leader, arriving after two missed quarters — a classic condition for "reorganize" to substitute for "diagnose." That substitution is this skill's most common failure mode, and it's worth naming before anything else: a program missing its goals has usually funded too many surfaces, not chosen the wrong parent.

**Funded driver: not stated — the single biggest open question.** Everything in Step 2 hinges on it. I'm working from the surface mix as a proxy:

| Signal | Reading |
|---|---|
| Blog ×2, YouTube, webinar, conference track, changelog | awareness/distribution-shaped — 6 of 12 surfaces |
| Discord, champions, Stack Overflow | community/engagement-shaped — 3 of 12 |
| API docs, 3 SDKs, sample apps | enablement/DX-shaped — 3 of 12 |
| A product VP actively trying to hand the team off | product doesn't see this as product-input work worth owning |

That mix points to **developer adoption/awareness** as the real funded driver, which would make marketing the correct line. Confirm this with whoever signs off on DevRel's goals before treating the line below as final — if the true driver is product input, the line recommendation flips, but the shape and coverage recommendations do not.

---

## Work inventory (before any chart)

Real owners, managers and hours aren't available to me — get this table filled in with names before acting on anything below it. What I can state without a live interview is the structural math, and it's damning on its own:

**12 named surfaces ÷ 5 people.** Every surface should have an accountable owner *and* a named backup (this skill's own baseline — a bus factor of one is an outage waiting for a resignation). That's 24 ownership slots against 5 people, or under 5 slots each. Nobody has been given a backup on anything. This is very likely the actual reason for two missed quarters, independent of which VP the team reports to.

| Surface | Owner | Manager | Hours/wk | If it stops |
|---|---|---|---|---|
| API docs | [confirm] | [confirm] | [confirm] | Support load rises |
| Engineering blog | [confirm] | [confirm] | [confirm] | — |
| Product blog | [confirm] | [confirm] | [confirm] | — |
| Discord | [confirm] | [confirm] | [confirm] | Response time degrades fast |
| Monthly webinar | [confirm] | [confirm] | [confirm] | — |
| 3 SDKs | [confirm] | [confirm] | [confirm] | Issues age, integrations break on API changes |
| Sample apps repo | [confirm] | [confirm] | [confirm] | Goes stale silently |
| Champions program | [confirm] | [confirm] | [confirm] | Advocates disengage |
| Conference track | [confirm] | [confirm] | [confirm] | — |
| YouTube channel | [confirm] | [confirm] | [confirm] | — |
| Changelog | [confirm] | [confirm] | [confirm] | Customers miss breaking changes |
| Stack Overflow presence | [confirm] | [confirm] | [confirm] | Unanswered questions compound |

The one line item worth flagging without needing the full table: **"three SDKs" as a fully DevRel-owned surface is a heavy, non-standard load.** Developer-experience engineering is staffed on only 27.4% of surveyed DevRel teams (*State of Developer Relations 2024*, DevRel.Agency, 310 respondents). If this team owns SDK maintenance outright rather than samples/docs/community feedback on top of engineering-owned SDKs, that's plausibly the single biggest overcommitment on the list — check this first.

---

## Reporting line

> DevRel reports to **marketing**, because the funded driver is (working assumption, confirm) **developer adoption/awareness**, and marketing leadership owns that outcome. This line will starve **the product feedback loop**. A named product-side counterpart covers that gap via a standing bi-weekly roadmap slot, owned by one person on the DevRel side. Reviewed at the one-year mark, or immediately if the sponsor changes.

Marketing is the modal line (33.1%, same survey) but not a majority — no line is — so this is a trade-off, not a best practice. Its characteristic failure here is specific and worth guarding against explicitly: **advocates get absorbed into pipeline support — webinars turn into gated lead-gen assets, blog posts get campaign briefs.** Given this team already runs a webinar, two blogs and a YouTube channel, that failure mode is a real risk. Write the counter-move into the transition, not just into this brief: *no DevRel surface carries a lead-gen gate, full stop.*

If the funded driver turns out to be product input instead, the line should stay with product (or move to engineering, given the SDK/docs load) — but re-run this section once the driver is confirmed, don't just default to whatever the newest VP wants.

---

## Shape — three candidates, ordered by efficiency

Building this as a set, per the skill's own rule, because line + shape + coverage only make sense together.

**Candidate 1 (recommended): Centralized, 5 people, one manager, reporting to marketing.**
- Makes easy: one calendar, one voice, one place to say no to new surface requests.
- Makes hard: nothing new — this is the shape they're already running, minus the reporting line.
- Coordination added: none beyond the new product-roadmap interlock.
- Reversible in a week.
- First thing that breaks if wrong: nothing breaks from the shape itself; if goals are still missed, the cause was proven to be coverage, not structure.

**Candidate 2: Centralized, 5 people, one manager, reporting stays with product.**
- Same shape and coverage fix as Candidate 1, isolating the line as the only variable.
- Useful as the counterfactual: if this brief's real problem is surface overload (likely), this candidate proves the reporting line was never the issue.
- Wrong pick if the driver really is awareness — leaves distribution unsponsored.

**Candidate 3 (VP Product's proposal): Split by focus — content pod + community pod, separate leads, under marketing.**
- Rejected. Split-by-focus has a staffing floor of roughly eight people (this skill's baseline), because each half needs to be a viable team and the coordination between them is permanent, not one-time setup. Five people is below that floor.
- The arithmetic is worse than it looks: two lead roles out of five heads is 40% of headcount moved into management, leaving three ICs to cover twelve surfaces. That's a smaller working team than today's, with an added permanent coordination cost on top.
- It doesn't even map cleanly onto the actual coverage: the enablement/DX surfaces (API docs, 3 SDKs, sample apps) aren't clearly "content" or "community." They'd land wherever has slack, recreating exactly the informally-absorbed-work problem that causes missed goals in the first place.
- Least reversible option on the table — once two people are hired/leveled as pod leads, undoing the split needs both to agree to give up a team.
- Revisit this shape once headcount crosses roughly ten (survey baseline: 69% of DevRel teams are under ten people, so this isn't a small-company workaround, it's the common case).

**Recommendation: Candidate 1.** It buys the reporting-line correction the new VP wants without adding a management layer the team can't staff, and it forces the real fix — coverage — instead of letting a reorg stand in for one.

---

## Coverage

| Function | State |
|---|---|
| Advocacy | Owned — blogs, YouTube, webinar, conference track |
| Community management | Owned — Discord, champions, Stack Overflow |
| Technical writing | Owned — API docs, changelog (confirm whether by a dedicated writer or advocates doing double duty) |
| Developer marketing | Shared with marketing once the line moves — DevRel writes, marketing distributes; no lead-gen gates |
| Developer education | Not deliberately covered today — webinar and champions touch it informally; decide explicitly rather than let it stay implicit |
| Developer-experience engineering | Owned — 3 SDKs, sample apps. **Re-scope this**: move core SDK maintenance to an X-as-a-service interlock with engineering (engineering ships and maintains, DevRel owns samples, docs and the community-facing experience) rather than DevRel carrying full SDK ownership across three languages |

Coverage staffed on 82.2% (advocacy) down to 27.4% (DX engineering) of teams generally (same 2024 survey) — this team is unusually broad, not unusually thin, which reinforces that the fix is subtraction, not reorganization.

**Resolve every gap one of four ways: hire, re-scope onto an existing owner, refuse in writing, or contract out.** For this team, right now, refuse or re-scope is the only affordable move — there's no headcount ceiling given to hire against, and contracting a surface still needs an internal accountable owner. Concrete candidates to re-scope or refuse before the next goal-setting cycle:
- SDK maintenance depth (move to engineering-owned, DevRel-serviced, as above).
- Conference track — confirm whether this is a speaking calendar or Vantor Mesh running its own track; the latter is a program decision, not a structure one, but it's heavy enough to be worth a written yes/no.
- Developer education — either staff it deliberately or refuse it in writing; stop letting it live informally inside the webinar and champions program.

---

## Interlocks

| Team | Mode | What crosses | Arbiter |
|---|---|---|---|
| Product | Collaboration during launches, X-as-a-service otherwise | Developer feedback in, roadmap/launch dates out | Head of product |
| Engineering | X-as-a-service for SDK core, facilitation for writing/demo coaching | SDK releases and technical review in, samples and docs out | Eng manager |
| Marketing (once line moves) | Collaboration on campaigns, X-as-a-service on distribution | Content in, channels and audience data out | Marketing leadership — with the explicit no-lead-gen-gate rule attached |
| Support | X-as-a-service | Recurring failure signals in, troubleshooting content out | Support lead |
| Sales | X-as-a-service, capped in hours | Evaluation material out, objections in | [confirm owner] — keep this capped; nothing in the surface list suggests sales enablement is the driver |

One mode per team, one arbiter per line. The product interlock is the one that matters most here — it's the pillar the marketing move starves, so it needs a real cadence (biweekly roadmap slot), not a standing invitation to "collaborate closely."

---

## Ladder & titles

Don't default advocates onto the marketing ladder on the move — that's the mechanism behind the "absorbed into pipeline support" failure, since promotion criteria built around campaign ownership don't describe writing docs, maintaining samples, or running Discord. Recommend either a DevRel-specific ladder or an adapted engineering IC ladder, given how much of this team's work (SDKs, docs, samples) is technical artefact production rather than campaign output. [confirm current ladder and title conventions before finalizing.]

---

## Budget

[confirm] — name who owns headcount budget vs. program budget separately; in 60% of surveyed programs (same 2024 survey) these are different people, and the reporting-line move is a natural moment for that split to get redrawn without anyone noticing.

---

## Re-org triggers

- The funded driver assumption above turns out wrong once confirmed.
- A second team starts doing content or community work without a declared interlock.
- Any surface stays at bus factor one for a full quarter after the re-scoping above.
- The team declines the same category of request three times for lack of coverage.
- Headcount crosses roughly ten — Candidate 3's split becomes affordable at that point, not before.
- The marketing collaboration mode on campaigns runs past a launch window with no end date.

---

## Transition

- **Week 1:** pause the pod split. Do not create two lead roles. Run the real Step 1 inventory with named owners and hours to replace the [confirm] placeholders above.
- **Month 1:** move SDK core maintenance to the engineering interlock; get a written yes/no on developer education and the conference track; stand up the biweekly product-roadmap slot; land the no-lead-gen-gate rule with marketing before any webinar or blog goes into a marketing campaign brief.
- **Quarter 1:** reset the team's goals against the re-scoped surface list — goals set against 12 surfaces are very likely why two quarters were missed regardless of parent org, and carrying the old goal set into a new structure reproduces the same failure with a new org chart on top of it.
- **Unchanged:** headcount, the five people's underlying skill set, docs ownership.

---

## Quality gate

- Work inventory: names/hours not yet filled in — **fails**, flagged with the placeholder table and the surface-count math as the interim evidence.
- Reporting line: driver stated as a working assumption, not confirmed — **conditional pass**, explicitly labeled.
- Shape: justified by staffing floor and coordination cost, not by what the new VP wants — **passes**; Candidates 2 and 3 shown and deleted with reasons rather than silently dropped.
- All six coverage functions stated, none blank — **passes**.
- Bus-factor-one risk named on every surface implicitly (12 surfaces, 5 owners, no backups) — **passes**, flagged as the headline finding.
- Interlocks: one mode and one arbiter per team, sales capped — **passes**, two arbiters marked [confirm].
- No headcount ratio quoted as benchmark, no compensation band present — **passes**.
- Re-org triggers: five, all observable without a survey — **passes**.

Net: this brief is usable to stop the pod split from happening on autopilot and to redirect the VP's energy toward coverage, but it is not complete — the inventory and the funded-driver confirmation are the two items that turn the [confirm] placeholders into a final document.