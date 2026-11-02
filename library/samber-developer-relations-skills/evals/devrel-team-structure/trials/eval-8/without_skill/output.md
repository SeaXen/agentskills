# DevRel structure proposal: Larkfield Identity

## Recommendation

**Consolidate all 11 people into one DevRel team under you. Don't split it by focus, and don't embed anyone in product squads.** Organize it by the self-serve signup journey, not by the three groups it comes from.

I haven't seen your inventory, your reporting line, or what the five engineers actually do. Everything below rests on the assumptions listed at the end. Confirm them before you present.

## Why

- **Eleven people with three managers is the problem.** The survey reports 43.6% of teams have more than one group doing DevRel work (DevRel Agency, *State of Developer Relations 2024*, 310 respondents). Splitting the work across those groups produces the usual failure mode. Marketing and engineering each optimize their own metric, and docs belongs to nobody.
- **Self-serve signups are won in the docs and the first 15 minutes of use.** That is quickstart, SDK samples, and error messages. Talks and posts only bring people to that point. Today, two contractors own the surface that matters most.
- **Eleven is just over the ten-person line.** That line is a baseline from the skill I used, not a published finding. Hub-and-spoke is technically affordable at 11, but its cost is a management layer and a standing coordination forum. A split-by-focus team needs about 8 people per half, so you can't afford it.
- **Embedding fails its own test here.** It pays off only when product input is the funded driver. Yours is signups.

## Three candidates

| | A. One team (recommended) | B. Hub-and-spoke | C. Keep three groups, add interlocks |
|---|---|---|---|
| Shape | One manager line, four functional pods | Hub of 3, spokes in marketing and platform | Status quo plus a steering group |
| Easy | One metric, one calendar, one place to say no | Local closeness to product | No political cost |
| Hard | Marketing and platform each give up headcount | Hub becomes an approval bottleneck | Nobody owns signups end to end |
| Coordination | Low | A standing forum and approval flow | High, permanent |
| Undo cost | Moderate | A quarter to unwind | None |
| First failure | Platform engineers pulled back into roadmap work | Hub approves instead of enabling | Docs falls between groups again |
| Wrong pick if | Exec team won't move headcount | You grow past about 15 | Signups stop being the funded driver |

**Pick B instead if** headcount transfers are politically impossible but you can still get a single accountable leader.

## Proposed pods (illustrative until the inventory exists)

| Pod | Owns | Likely staffing |
|---|---|---|
| Activation | Docs, quickstart, samples, changelog, time-to-first-call | 2 contractors plus 2 engineers |
| Developer experience engineering | SDKs, API ergonomics, sample apps, friction fixes | 3 engineers |
| Advocacy and content | Tutorials, talks, blog, video | 3 from product marketing |
| Community | Forum or Discord, support presence, champions | 1 from product marketing |

- **Convert at least one contractor seat to a full-time owner**, or name an internal owner of the docs site. A surface run only by contractors disappears when the contract ends.
- **Give every surface an owner and a backup.** No surface should depend on one person.
- **Plan to 70% of declared capacity.** That is about 7.7 effective people out of 11. It is a baseline you can adjust. It leaves room for support load, launches, and travel.
- **Say what you refuse.** Examples are no event calendar beyond N conferences, and no per-product advocates. A written refusal list is worth more to the exec team than a longer scope.

## Reporting line

Use this shape and fill it in:

> DevRel reports to **[function]**, because the funded driver is self-serve signups and **[leader]** owns that number. This line will starve **[pillar]**. **[named team]** covers that gap, reviewed at **[date]**.

- **If you report to marketing:** you get awareness budget and attribution. You risk losing product input and the engineers' craft. Counter with a standing monthly review with platform engineering on the top 10 developer friction items.
- **If you report to product or engineering:** you get roadmap influence and credibility. You risk starving community and content. Counter by keeping one dedicated content owner.
- **Don't report to sales or the CEO.** Sales buys fast attribution at the cost of community trust. The CEO line has no succession path.

## Interlocks (one mode each)

| Team | Mode | What crosses | Arbiter |
|---|---|---|---|
| Product | Collaboration for launches only | Roadmap, release readiness | You and the head of product |
| Platform engineering | X-as-a-service | API changes, deprecations, SDK review | Head of platform |
| Product marketing | X-as-a-service | Positioning, launch assets | You and the head of PMM |
| Support | X-as-a-service | Top ticket themes to docs | Head of support |

## Metric: define it before the meeting

- **Don't report raw signups.** Report activated signups, meaning a first successful API call within 7 days.
- Add time to first call and docs-to-signup conversion as leading indicators.
- Expect the exec team to ask why signups are the funded driver. Have the activation definition and a baseline ready.
- This is also the defense against the "downloads as users" trap.

## Transition

- **Week 1:** announce the single leader, freeze new commitments, and run the surface inventory (owner, manager, hours per week, what breaks if it stops).
- **Month 1:** move reporting lines and name pod leads. Convert or extend the contractors.
- **Quarter 1:** first activation baseline, first refusals documented, and a review of whether platform engineers are being pulled back to roadmap work.

## Re-org triggers

Reopen the structure if any of these happens:

- The funded driver changes.
- Headcount passes about 15.
- A surface sits at one owner with no backup for a quarter.
- A second team starts doing DevRel work without a declared interlock.
- The team declines the same type of request three times for lack of coverage.

## Decisions to take from the exec team

1. Approve a single accountable leader for DevRel (you).
2. Approve headcount transfers from product marketing (4) and platform engineering (5).
3. Approve converting at least one docs contractor seat to full-time.
4. Agree that activated signups is the success metric.
5. Agree on the reporting line and the date it gets reviewed.

## What I assumed, and what could change this

- **I don't know your reporting line.** The line section is a template for that reason.
- **I assumed the five platform engineers do developer-facing work** such as SDKs and API support. If they mostly do internal platform work, the DX pod shrinks and you may only be able to claim dotted-line time.
- **I assumed the four marketing people split across advocacy, content, and community.** If some are brand or campaign people, they stay in marketing and you may be below 11.
- **I assumed transfers are negotiable.** If they aren't, fall back to candidate B.
- **The pod staffing is a guess.** The surface inventory in week 1 should replace it. Don't present names to the exec team until you've done it.
- **Ratios and compensation:** I deliberately gave no advocate-to-developer ratio or pay bands. Neither has a defensible source.

If you tell me your reporting line and what the five engineers actually do, I can tighten the pods and the reporting-line paragraph.