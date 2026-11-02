# OtterForge Conf, edition 5: routing

**Next action:** run `samber/dev-event-organizer-skills@event-feedback` this week. It decides the survey question, and the feedback window closes fastest.

## Assumptions

- **Event finished.** You said it wrapped, so the session is in the "it has finished" block. The short-list below contains only after-and-between skills.
- **Edition 5.** That opens the `recurring` gate and gives `event-continuous-improvement` prior editions to read.
- **In-person, all talks recorded.** That opens the `in-room` gate.
- **Date.** I took "last Saturday" as 2026-10-10. Correct me if it was the 3rd.
- **Open questions.** Funding model, landing date and effort ceiling are unknown. They are the four questions at the end.
- **No context file written.** This repo is not the OtterForge project, so I did not write `event-context.md` here. The content is at the bottom.

## Route

**`samber/dev-event-organizer-skills@event-feedback`**

Its scope is what participants are asked, through which channel, when, and what goes back to them. It also covers how to fix a response rate nobody answered.

## 1. Sequence now that it's over, and the survey

The sequence is **`event-feedback` → `event-debrief` → `event-content-repurposing` → `event-continuous-improvement` → `event-growth-strategy`**.

On skipping the survey, the decision belongs to `event-feedback`, so take it there. My read is that "people are tired of forms" argues for a shorter, in-channel instrument, not no instrument:

- Edition 5 is the first edition with several prior ones to compare against. A gap in the participant series weakens the later trend read and the growth decision.
- The skill's own scope includes surveying through the channel that gets real response rates. A long emailed form is the thing people are tired of.
- Your tiredness is itself a finding to bring to that session, with your past response-rate data.

## 2. Dead YouTube channel, and the developer-content push

These are two different things, and they go to two different places.

**a. The dead channel and the recorded talks → this collection.**
- `tech-podcast-youtube-channel` covers whether to sustain a standing channel at all. It also covers the cadence commitment, a named owner in the quiet months, and a wind-down or handover. Reviving it, shutting it down and restructuring it all fall inside that scope.
- `event-content-repurposing` covers what to do with this edition's recordings: formats, release cadence, and the rights gate on slides and photos. It explicitly excludes the standing channel, and the channel skill excludes clip-cutting. Run content repurposing first, because its inventory is what the channel decision feeds on.

**b. A real developer-content and documentation push around the open-source tooling → recommend `samber/developer-relations-skills`.**
- No skill in this collection covers developer content, documentation or open-source strategy.
- This is a recommendation, not a dependency. This collection stays usable on its own.
- Candidates there include `developer-docs-structure-audit`, `docs-seo`, `engineering-blog-post` and `open-source-company-strategy`. I have not read their scopes, so verify before you commit.

One seam to settle early: **decide whether the YouTube channel is meant to carry that developer content**. If yes, the channel decision and the DevRel plan must agree. Make the channel decision first, because it is cheaper.

## 3. Hackathon segment against the headline sponsor's API

**Not a platform question.** The routing reference says a sponsor's API becoming a hackathon challenge belongs to `hackathon-brief-design`, and that skill's own description names it. Do not hand it to a platform collection.

Only one thing would change that. If you needed to build your own sandbox, SDK or test mode for teams, that is a platform question, and `samber/developer-platform-skills` would then be the recommendation. A sponsor's already-public API does not trigger it.

Nothing in the hackathon lane is reachable yet. Edition 6's format is not fixed, because "a hackathon segment" is a wish rather than a decision. So `event-format-selection` comes first, and every `hackathon` row stays suspended until it returns.

## Short-list, ordered by value per unit of effort

Re-rank, stated aloud:
- **Finished event:** deleted the existence check, the spine, fill-the-room, the sponsorship sale and on-the-day work. Deleted, not demoted.
- **Edition 5:** restored the cross-edition entries.
- **Unknowns:** landing date and effort ceiling would move more, but I don't have them.

1. **`event-feedback`**
   - *Attacks:* participant memory and goodwill decay by the day. This is the only input the other skills cannot reconstruct later.
   - *Costs:* one design session, plus a short instrument and a reply to respondents.
2. **`event-debrief`**
   - *Attacks:* the team's own memory of what fired against the risk register and run of show fades fast.
   - *Costs:* one blameless retro session, then a dated lessons log with owners.
3. **`event-content-repurposing`**
   - *Attacks:* 1,400 attendees' worth of recorded talks lose momentum after the event, and this is the inventory the next campaign and the channel both need.
   - *Costs:* a rights check on slides and photos, plus a publishing cadence you must keep.
4. **`tech-podcast-youtube-channel`**
   - *Attacks:* the dead standing channel, with an explicit keep-or-close verdict.
   - *Costs:* low to decide, but a standing owner and cadence if you keep it. This is where your effort ceiling matters most.
5. **`event-community-building`**
   - *Attacks:* the audience between editions, and the community's appetite for more.
   - *Costs:* ongoing moderation and programming. It is cheap per session, but you owe it continuity.

## Chain

Dependency order, not efficiency order:
1. `event-feedback` hands `event-debrief` the participant verdicts to reconcile against the team's own view.
2. `event-debrief` hands `event-content-repurposing` the lessons and the list of what was captured.
3. `event-content-repurposing` hands `tech-podcast-youtube-channel` an inventory and a release cadence, so the channel decision rests on real material.
4. `event-continuous-improvement` reads the debrief logs across editions and hands `event-growth-strategy` the trends.

## Not now

- **`event-continuous-improvement`**
  - *Unblocked when:* this edition's debrief has landed and at least one prior edition's debrief log exists.
  - *Question for you:* do prior debrief logs exist?
- **`event-growth-strategy`**
  - *Unblocked when:* the trend read has returned.
- **`event-format-selection`**
  - *Unblocked when:* you are ready to decide edition 6's shape. Its question is whether a hackathon segment joins the conference, and with what track structure.
  - *Why it's here:* it is the gate for everything hackathon-related.
- **`hackathon-brief-design`**
  - *Unblocked when:* `event-format-selection` returns "hackathon segment fixed".
  - *Then it covers:* the sponsor-API challenge framing.
  - *Then the rest of the lane:* team-formation, mentoring, judging and cash-prize follow in order.
- **`event-sponsor-value-proposition` and `event-sponsor-fulfillment`**
  - *Unblocked when:* the headline sponsor's renewal conversation opens, and the hackathon is a candidate package.
  - *Question for you:* when does their budget window close?
  - *Why it's here:* that deadline would promote the sponsorship work.

## Gap

None of your three asks falls outside the collection except the developer-content and documentation push. For that, install `samber/developer-relations-skills`.

## Routines (dry-run only, nothing created)

Each routine below needs your approval before anything is created.

```
Routine: kickoff re-invocation
Trigger: once per session start on this project
Runs: samber/dev-event-organizer-skills@dev-event-kickoff
Output channel: a dated line in the session log of event-context.md
Cost: near zero per firing
First fire: next session
Stops: when edition 6's doors-open date passes
```

```
Routine: post-edition trend read
Trigger: the day the edition 5 debrief lands (date to be set)
Runs: samber/dev-event-organizer-skills@event-continuous-improvement
Output channel: a dated section in event-context.md, plus a message to the organizers
Cost: one reading per firing
Stops: after the growth decision is recorded
```

I installed the two cheapest. The ticket-pace and work-back routines belong to edition 6 and wait for its dates. Nothing carries over from an earlier edition.

## Context artifact: save as `event-context.md`

```markdown
# Event context

_Last updated: 2026-10-12_

## Identity
- Event: OtterForge Conf
- Edition: 5 (finished, Saturday 2026-10-10, assumed)
- Funding model: not stated

## Format (the gate source)
- Shape: conference. Track count: not stated.
- Delivery mode: in-person. All talks recorded.
- Edition 6: a hackathon segment is wanted, not fixed. Format not fixed.

## State
- In flight: post-edition work not yet started.
- Decided: nothing recorded.
- Open: survey instrument; YouTube channel keep or close; developer-content push; hackathon segment.
- Constraints: landing date, one-off versus standing and effort ceiling not yet asked.

## Session log
- 2026-10-12 - "what now after edition 5, channel, hackathon" → `event-feedback`
  → recorded the three asks and the unfixed edition-6 format.
```

I did not write memory either. When you do, keep attendee and speaker data, accommodation requests, conduct reports, negotiated sponsor rates and contract terms still under negotiation out of it.

## Four questions to finish the kickoff

Please answer these, ideally as picks:
1. **Who funds and organizes OtterForge?** Volunteer community, company, foundation, or mixed? This sets the sponsorship weighting.
2. **Is there a date the next result must land by?** Examples: a sponsor budget window, the edition 6 CFP, or doors open.
3. **What is your effort ceiling?** One-off hours only, a week of work, a standing few hours weekly, or staff or budget?
4. **How many tracks did edition 5 run, and does an expo floor or press surface exist?** This confirms the `conference` gate.