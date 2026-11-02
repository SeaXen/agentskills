# Berlin Infra Days show: guest pipeline after the 34-speaker pool ran out

I applied the `tech-podcast-youtube-channel` skill and its three references. I did not run the interview, so the answers below rest on labelled assumptions. Items marked *(skill construction)* are the skill's own design choices, not sourced practice. Per the skill, I present this section by section, and nothing should go out under the show's name until you approve each section.

## Verdict

- ❌ **Vaultwright's quarterly VP slot** is not a guest-sourcing option. The skill deletes "a guest slot given because a sponsor paid for it, published as an editorial booking". "No money changes hands" doesn't change that, because the slot is still given because of the sponsorship.
- ❌ **The public pitch-us form** stays off for now. Opening a public call needs two conditions: the pool is exhausted, and a named vetting owner holds a written bar. The first is met. The second isn't, because nobody reviews anything today.
- ✅ **Fix the missing review step first.** It is the one gap that blocks every way of getting past the pool: the pitch form, community nominations and cold outreach.
- Booking "whoever replies first" is the skill's negative example: "Availability is not fit and enthusiasm is not a bar."

## Assumptions to confirm

Each answer below would move a rung.

| # | Assumption | If wrong |
|---|---|---|
| Q1 | A recurring show is already decided in your portfolio. At 40 episodes it effectively is. | If it was never decided, route to `event-portfolio-strategy` first. |
| Q3 | A person has recurring quiet-month hours, but nobody else on the team reviews. | If nobody is named, drop both original-content rungs. The posture becomes archive-only or no channel, by decision. |
| Q5 | The 34 are the people you have permission to contact for the show. Other past speakers may exist without that permission. | Re-asking them for show permission is the cheapest way to widen the pool. |
| Q6 | No vetting owner, no written bar, and unknown release custody. | A named owner and bar unlock the open pitch. |
| Q8 | The show should outlive the current team. | If not, cold outbound is out. |
| Q10 | Unknown. Is there a community space that already surfaces guest names? | If yes, community nomination becomes a rung. |

## 1. Existence posture and quiet-month owner

- Keep the original-content posture only if Q3 names one person who has agreed to the rhythm.
- If the guest supply dries up before the pipeline below is staffed, fall back by decision. Don't let it lapse.
  - Use the cheapest format on the effort ladder, such as an unedited stream or a reused edition recording.
  - Or go archive-only.
- A guest-starved show with no owner is the lapse the skill warns about.
- **Rejected rungs, recorded so nobody re-argues them:**
  - a stated cadence nobody agreed to hold
  - the heavy-cadence channel, since no in-house editor or funded owner is known

## 2. Cadence commitment

Write one sentence the owner agreed to. Don't invent an interval. Derive it from the owner's honest quiet-month hours. *(skill construction)*

> "We publish [what] on [rhythm the owner agreed to], hosted by [name]. If a cycle slips, we say so in the feed."

Publish only that sentence. Don't announce a bigger rhythm to absorb new guest supply.

## 3. Guest pipeline

### Menu 2 ranking for your situation

| Rung | Status | Condition |
|---|---|---|
| Speaker pool only | Exhausted | Re-check Q5. Ask lapsed or unreachable speakers for show permission. Include confirmed-upcoming 2026/27 speakers if allowed. |
| Pool plus community nomination | **Next rung** | Needs Q10: a community space that already surfaces candidates. Nominations are input, not bookings. |
| Open pitch (the form) | **Blocked** | Needs a named vetting owner with a written bar. Both halves must hold. |
| Cold outbound | Not now | Needs compounding intent (Q8), hours that return nothing for several cycles (Q9), and a vetting owner (Q6). Reuse the craft in `event-speaker-sourcing` and `event-speaker-cold-outreach`. |
| Sponsor-given slot | **Deleted** | See § 3a. |

### The pipeline

Every guest goes through the same steps, whatever the source: pool, nomination, pitch form or sponsor suggestion.

1. **Intake.** Sources are the pool list, nominations, the form once it is unlocked, and sponsor suggestions. Each entry records who suggested them and why.
2. **Triage by the named vetting owner against a written bar.** Record who checked what. Reuse the intake discipline from `event-cfp-design` rather than building a second one.
3. **Conduct check.** The event's code of conduct binds the show. Route this to `event-code-of-conduct` and don't restate a softer policy.
4. **Decision logged:** accept, decline or hold, with a reason.
5. **Booking**, only after acceptance.
6. **Episode release before recording.** See § 4.
7. **Record, publish, update the pipeline log.**

**Booker and reviewer should be different people, or the reviewer should at least get a veto.** *(skill construction)* Today the booker is the only gate.

### The written bar

Use these four questions. They are the skill's own construction. *(skill construction)*

1. Does the guest have something specific to say on a topic your audience recognises?
2. Is there anything in the public record you would be answering for after publishing?
3. Has anyone on the team worked with them, and what did they say?
4. Does the guest understand the recording will be published, and how?

Reject any bar that lists attributes like "engaging, well-known, technical". Nobody has ever failed that.

### The pitch form, when it unlocks

It needs all three of these, or it is an inbox, not a pipeline:

- a published bar
- a named reviewer
- a stated answer window

Derive the window from the reviewer's real capacity. The skill gives no number.

### 3a. Vaultwright

The skill gives three routes. Recommended: option 2.

1. **Decline as an editorial slot.** Say so plainly and offer the sponsor-side route below.
2. **Treat the VP of Engineering as a normal candidate.**
   - He enters the same pipeline and meets the same bar.
   - There is no guaranteed quarterly slot and no commitment.
   - It is only a booking if the bar says yes.
3. **Make it a sponsored segment.** That is a sponsorship decision, made via `event-sponsor-value-proposition` and disclosed as sponsored. It is never a sourcing rung here.

Reasons:

- A standing quarterly slot turns the show into sponsor inventory.
- It also erodes the one thing the show gives the audience, which is editorial independence.

Disclosure wording is review-triggered. Route it to your own counsel.

## 4. Release instrument

- Use a separate episode-specific release, signed by every participant (including hosts and any third voice), before recording.
- A stage consent never covers an episode. "They signed last year" fails.
- A named custodian holds the records. Wording goes to counsel, and I name no jurisdiction or retention period.
- If you do live or unedited streams, the release must cover live publication.
- **Audit now.** You are 40 episodes in with no review step, so verify that every published episode has a release on file. If some don't, that is a live obligation. Handle it with counsel, not by guessing.

## 5. Feed relationship

| Path | Status |
|---|---|
| conference → channel: recordings arrive as episodes or cuts | EXISTS |
| conference → channel: confirmed speakers are the booking pool | EXISTS, but exhausted |
| channel → conference: a past guest is a warm first contact for the next call for speakers | EXISTS |
| channel → conference: show notes link to the ticket page | ASPIRATIONAL. Don't claim it fills seats. |
| channel → swap: episodes as inventory for a swap | EXISTS |
| channel → speakers: a watched channel attracts speakers | ASPIRATIONAL. Test it with one optional question to speakers: "did our published videos play a part in your decision?" |
| pitch form → pipeline | ASPIRATIONAL until the reviewer exists |
| Vaultwright → show | **None**, by decision |

## 6. Handover

Write it now, not when someone leaves. It is one page, dated, and covers:

- the platform account, with a second named holder, so it isn't personally owned
- control of the feed
- admin roles
- where the back-catalogue masters live
- the release custodian and the retention decision, restated
- the guest contact list, and the pitch inbox once it exists
- what the show has promised publicly
- a re-check date

## 7. Gates and measures

The three gates are mandatory, with zero exceptions:

- **Release coverage:** every published episode has a release on file with a named holder.
- **Named quiet-month owner:** the public cadence is the one that person agreed to.
- **Handover readiness:** the handover document exists, is dated, and names living holders.

Self-set measures, declared before the cycle starts:

- Cadence kept (binary per cycle). A repeated miss is a demotion signal, not a discipline problem.
- Pipeline depth, reported as a count of guests agreed ahead of the next publish date.
- Back-catalogue reachability.
- Speaker-loop answers, as a count.
- Quiet-month publishing, binary per gap.

The skill sets no numeric thresholds, because none are sourced.

## What you do first

1. Name the vetting owner and write the four-question bar. This unlocks everything else.
2. Audit release coverage across the 40 episodes.
3. Ask lapsed speakers for show permission, and check Q10 for a community space.
4. Reply to Vaultwright using route 2: he goes through the normal bar, with no standing slot.
5. Open the pitch form only after steps 1 and 3 are done.

Tell me your answers to Q3, Q5, Q6 and Q10 and I'll re-rank the menus against them.