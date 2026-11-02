# Atlas Forge: mentor-side design

**Next action: open the Kelvara sponsor-agreement conversation first.** It is the longest lead-time item. Everything else on this page depends on its outcome.

I read the skill and both references. I have not run the one-question-at-a-time interview, so the plan below rests on stated assumptions (section 8). Each assumption names the rung it would move.

## 0. What your constraint does to the design

- Kelvara as the sole allowed backend is the deepest sponsor-integration depth the skill recognizes: **the sponsor's technology as sole substrate**.
- The published rules have already promised every team a working Kelvara platform. Mentor coverage is how that promise gets kept.
- Kelvara has offered money only, so the promise is currently **unstaffed**. This is the failure mode "a sponsor track promised in the brief and unstaffed on the floor" ⚠️.
- Two consequences follow from the skill's rules:
  - **"No mentor programme" is deleted** as an option.
  - **On-call from organizers is not enough.** Unless your organizing team has built on Kelvara, the expertise isn't in the building.
- Two rooms push the request mechanic toward routing and a staffed presence. Both rungs are promoted by the skill's multi-room trigger.

## 1. Coverage depth per track

Size against coverage units, not headcount. I give no mentor-to-participant ratio. The skill refuses to invent one, and the only published ratio (Tauberer's) covers project supply at themed events, not mentor staffing.

**Rung: expertise-matched roster.** Promotion condition met: Kelvara is required for every track, which is deeper than "required for one track".

| Coverage unit | Commitment level | Why |
|---|---|---|
| Kelvara realtime platform | **Guaranteed**: a Kelvara-tagged person present for stated hours | Sole substrate. The brief's fallback sentence assumes the platform gets support. |
| Track 1 | Available (see note) | Reachable through the request mechanic |
| Track 2 | Available (see note) | Same |
| Track 3 | Available (see note) | Same |
| Track 4 | Available (see note) | Same |
| General stack (git, deployment, dominant language) | Available | Every team touches it |

Note on the tracks: raise a track to **guaranteed** for the hours it is actively worked if the event is themed, with organizer-supplied problems (Q3).

"Guaranteed" needs a decision with two rooms: **in which room?**

- Default I recommend: a Kelvara-tagged mentor in each room during guaranteed hours. A guarantee that means "somewhere in the building" fails the way "find one" fails.
- Cheaper alternative: one Kelvara desk both rooms can reach, with the walk published in the request mechanic.
- The choice depends on the effort ceiling (Q8) and on what Kelvara agrees to.

Handing the guarantee to the shift plan: give `event-volunteers` the constraint, "this tag, present, these hours, in these rooms". It does the sizing, buffers, confirmation and backfill. The number of people comes out of that arithmetic, not from me.

## 2. Recruitment channels and lead times

**Rung: mixed pool with a written engagement rule.** Promotion condition met: the brief names a sponsor technology, and no community mentor can be assumed to know Kelvara.

- Reject sponsor staff only. Its trust value is the worst of the four rungs, and every participant would read a Kelvara badge as a sales conversation. They have no choice of backend, so the badge reads as even more of a sales conversation.
- Also reject a mixed pool without the rule. It is the default when nobody writes the paragraph.

| Channel | Role here | Lead time |
|---|---|---|
| **Kelvara technical staff** | Guaranteed Kelvara coverage. A sponsorship deliverable, not a volunteer sign-up. | Weeks. Start now. |
| Community and alumni (user groups, past participants, partner companies, library maintainers) | Track-domain and general-stack coverage | Days, from a warm list |
| People outside Kelvara who have built on Kelvara | Second source of Kelvara coverage, tagged "has built with it" | Days to weeks |
| Returning mentors | Cheapest, only if someone kept the list (Q7, Q10) | Days |

**The Kelvara ask, framed as a deliverable.** Their exclusivity rule is in the published rules. Staffing the platform they mandated is the counterpart obligation, not a favor. Terms go in `event-sponsor-agreement`, not in a briefing email:

- Named people, or a named count, and the Kelvara products they cover.
- Hours committed, matched to the hours teams work with the platform. A track-by-hour table from the run of show helps here.
- The engagement rule (section 5), written in as a term.
- A named escalation contact for platform problems the on-floor staff cannot solve.
- An outage plan: what teams are told, and who tells them, if the platform degrades. With a sole backend, every team is blocked at once.
- Treat a missing Kelvara mentor as a **fulfilment failure** handled with the sponsor, never as a volunteer no-show.

**If Kelvara declines to staff.** Don't quietly fall back.

1. Tell the sponsor contact that the published rule and the staffing are linked.
2. Recruit Kelvara-experienced people from outside Kelvara.
3. Rewrite the brief's support sentence to say what support exists.

The brief must not promise support the event cannot deliver.

## 3. Expertise tags

- One tag per challenge track, in the brief's own words. Tags must map to the track names teams entered.
- **Kelvara**, by product name, kept separate from the language it is written in or its SDK language.
- One general-stack tag.
- Two depth levels per tag: **has built with it** or **has read the docs**. Ask at sign-up and don't infer from job titles.
- Keep the list short enough for a coordinator to recall at 3 am.

## 4. Expertise constraint handed to the shift plan

- Stagger by when each track needs each skill, as the brief sequences them. Early-stage mentors go first, technical mentors once teams have a direction.
- Take the slot from each mentor at sign-up. A slot is the commitment, and presence beyond it is a courtesy.
- Give each assigned mentor a checkable visit cadence for their slice of teams. This is a number the event sets for itself. Stop scheduled visits ahead of the final stretch.
- **Overnight (decide and publish).** 36 hours certainly runs through a night, which is the hour with the most blocked teams. Choose one of three and publish it:
  - **Kelvara-tagged person present all night.** The faithful reading of "guaranteed".
  - **Thin cover, with a named on-call Kelvara contact.**
  - **Published as unstaffed.** Use this only if Kelvara won't cover nights. Say so in the brief, because the sole-substrate promise is weakest here.

## 5. Request mechanic (as participants will read it)

**Rungs: request channel with organizer routing, plus identifiable mentors, plus a staffed mentor area.** Office hours are a supplement only.

- **Channel with routing.** Promoted three ways: multiple rooms, a sponsor track whose questions must reach one named person, and an overnight window. Mentors know where to find requests, and organizers connect teams to mentors.
- **Routing must not be one person.** At least two people work it, with a published fallback so there is no 3 am single point of failure. This is the standing job the low-effort-ceiling answer would demote.
- **Identifiable mentors.** A marker and a named role in the channels. Use a Kelvara tag or marker so teams can find platform experts by sight.
- **Staffed mentor area** in each room, or one reachable desk if the effort ceiling forces it.
- **Office hours** answer questions that can wait. They are never the sole route, because the window runs through the night.

Publish where the brief is published, before the window opens, and repeat it at the opening. State four things:

1. How to recognize a mentor.
2. How to ask.
3. What to expect, including that asking early is normal.
4. What happens when nobody covers it.

For the uncovered-skill escalation route, publish this order before the window:

1. Roster second level ("has read the docs"), said plainly.
2. Kelvara's escalation contact.
3. Ask the other team's participants (a request, not an assignment).
4. Tell the team plainly that no help exists, early enough to pivot. A pivot at hour 4 is possible, and one at hour 30 is not.

Interruption discipline, because push coverage in two rooms drifts:

- Per-visit time cap with a visible timer.
- A team-controlled do-not-disturb signal.
- A published list of what each present mentor knows.
- A shared view of blocked teams and who visited whom. Watch for a loud team being visited repeatedly while another goes untouched.

## 6. Mentor briefing

**Rung: boundary plus scenario walkthrough.** Promotion conditions met: Kelvara staff will mentor on their own employer's platform, and most volunteers are likely new to mentoring. "None" is deleted if any prize carries cash value (Q6). A title sponsor suggests it does, so confirm.

Contents (all rungs):

- Where to be, when, and what a slot means.
- How requests arrive, in the exact form participants use.
- Who to escalate to for non-technical issues.
- A pointer into `event-code-of-conduct`'s script. Don't paraphrase it.

**Help-versus-build boundary (edit into your voice):**

> Mentors explain, diagnose, unblock and demonstrate. Mentors do not write code that ships in a submission. If a mentor needs to show something in code, it is written outside the team's repository - a scratch file, a message, a whiteboard - and the team types the version that lands. If a mentor has already committed to a team's repository, the team declares it in the submission.

Platform-specific risk: because Kelvara is mandatory, the pull to "just fix their Kelvara config" is strongest here. Scenario-walk it:

- **Positive:** the mentor reads the platform error with the team, names the failure class, asks what changed, points at the config. The team fixes it and can debug the next one.
- **Negative:** the mentor says "let me drive", fixes it, pushes. The commit is authored by someone who may be in the room at prizes.

**Engagement rule, for every Kelvara-supplied mentor** (mirror it into the agreement):

> While mentoring, you are helping the team in front of you with the problem they brought. Not a sales conversation, not a recruiting conversation, not a demo. If a participant asks about your company, your product's pricing, or working for you, answer briefly and point them at your booth or your team's channel. Wearing a mentor marker means a participant cannot easily decline the conversation, which is exactly why it is not the place to have it.

- Teams cannot choose another backend, so this rule matters more here than at an optional-sponsor event.
- Also include power-dynamics guidance: ask before touching anything, leave the project unevaluated, and say out loud what you don't know.
- Mentor conduct policy and enforcement belong to `event-code-of-conduct`, so don't draft a second pipeline.

## 7. Contact log decision

**Keep a mentor-team contact log by default**, recording which mentor spent meaningful time with which team. A title sponsor commonly asks for a jury seat, and Kelvara staff are likely mentors.

- Rule, stated declaratively: a mentor who materially helped a team recuses from judging that team.
- The mechanics belong to `hackathon-judging`. Hand over the log before the judge pool is fixed.
- Confirm in Q5 whether any mentor is also a judge. If none is, the log is cheap insurance but not required.

## 8. Assumptions to confirm (each names the rung it would move)

| # | Assumed | If different |
|---|---|---|
| Q1 | In person. Window runs through the night. | A digital or hybrid event reinforces routing. A window that doesn't run overnight lets office hours return as a primary route. |
| Q2 | All four tracks required on Kelvara (sole substrate). | Confirmed by what you told me. |
| Q3 | Themed or open is unknown. | Themed raises track coverage from "available" to "guaranteed" in peak hours. |
| Q4 | No sponsor staffing committed or signed. | A signed commitment moves the Kelvara channel from "negotiate" to "deliver". |
| Q5 | Mentor-judge overlap unknown. | See section 7. |
| Q6 | Prizes carry cash value. | If not, the "none" briefing rung is back on the menu, but I'd still not use it. |
| Q7 | First edition or recurring is unknown. | Recurring promotes the reusable walkthrough even more strongly. |
| Q8 | Effort ceiling unknown. | A low ceiling demotes the routed request channel, which is a standing job. The fallback is a staffed area per room plus markers. |
| Q9 | Roster close date unknown. | A close date promotes the community and alumni channels. The Kelvara negotiation and the tagging pass finish last. |
| Q10 | Existing assets unknown (returning mentors, an organizing team that knows Kelvara). | An organizer team that has built on Kelvara can partly cover on-call. It cannot cover overnight and routing while running the event. |

## 9. Pass threshold before the window opens

**All five must exist in writing with zero blanks.** This is a self-set threshold, so compare it only against your own earlier editions.

1. Expertise tags mapped onto the four tracks, plus Kelvara and the general stack.
2. A coverage commitment per unit, including which room and which overnight option.
3. The request mechanic as teams will read it.
4. The mentor briefing including the boundary sentence and the engagement rule.
5. The escalation route for an uncovered skill, with a named Kelvara contact.

Signals to record live (pick two or three, each with a revision it would trigger):

- Longest-waiting requests and their track.
- Hours when no Kelvara-tagged mentor was present.
- Requests that found nobody.
- The contact log, if any mentor judges.

Close out by recording which units ran short and at which hours. Hand the mentor list to whoever recruits next edition.

## 10. Order of work

1. Start the Kelvara deliverable negotiation in `event-sponsor-agreement`. It runs for weeks.
2. Answer Q3, Q5, Q6 and Q9.
3. Decide the per-room guarantee and the overnight option.
4. Open the community and alumni channels in parallel with step 1.
5. Tag mentors as they confirm.
6. Hand the expertise constraint to `event-volunteers`.
7. Publish the request mechanic with the brief.
8. Hold the mentor briefing before the window opens.

Per the skill, validate this section by section before the window opens: coverage depth, channels, tags, mechanic, then briefing. A mechanic changed mid-event is one half the field never learns.