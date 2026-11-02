# OpsCurrent year-2 CFP design brief

This brief follows the `event-cfp-design` skill. I couldn't run its interview, so the open questions and assumptions are listed at the end.

## Verdict on your three plans

| Plan | Verdict | Why |
|---|---|---|
| Narrow the topic list to cut submissions | ❌ Don't | 310 for 38 slots is about 8.2:1, which is normal. It isn't a scoping failure. |
| Keep the rubric internal | ❌ Don't | It causes the problem you want to fix and doesn't stop arguments. |
| Guaranteed slot for the platinum sponsor | ❌ Don't | It breaks the one hard line in community-conference practice. There are other ways to protect the renewal. |

### 1. Narrowing the call

- **Your ratio is healthy.** PyCon US 2025 accepted 15% of 938 proposals, about 6.5:1. swyx puts established conference pools at 200 to 1,200 applicants, so 8 to 30x oversubscription is normal. The skill lists "reading oversubscription as failure" as a failure mode. The fix for volume is review capacity, not a narrower call.
- **Narrowing won't remove vendor pitches.** A vendor can fit any topic list. The cost of narrowing falls on good independent speakers. In year 2 the real danger is undersubscription of quality talks, and that is the stop signal.
- **Vendor pitches are an off-policy share problem.** Fix it with published criteria and a redirect, covered in the criteria section below.
- **Optional light framing.** You can add a short "what we're looking for" theme note. Don't make it a hard topic cut.

### 2. Keeping the rubric internal

- Unstated criteria is the skill's first failure mode: "rejections read as arbitrary, and next year's submission pipeline pays for it."
- Publishing the rubric is what stops pitches. Criterion 6 says tool and product talks go to open space, so vendors get a clear signal before they submit.
- Rejected speakers can argue with an unpublished rubric just as easily. A published rubric gives you a defensible answer: "we applied the criteria in the call."
- You can keep these internal: individual reviewer scores, reviewer notes, and the exact weights.
- Publish only criteria you will really apply. The skill's honesty check applies: name recognition and topic mix do shape selection.

### 3. The platinum guaranteed slot

- The community-pole rule is "no speaker spots can be bought by sponsors: not ever - period." The skill treats this as the one non-negotiable criterion.
- A guaranteed slot also contradicts your own call if you publish that criterion. Speakers who find out will assume every slot was for sale.
- This is your decision. If you grant the slot, say so openly in the call, label it as a sponsored session, and drop the "no bought spots" line. That costs trust, and you can't undo it.
- Renewal-smoothing alternatives that keep the line intact:
  1. The sponsor submits through the same CFP under the same criteria. Staff can submit like anyone else.
  2. A clearly labeled sponsor session outside the speaker program, such as a demo room or booth stage. It is not a talk slot.
  3. Product and tool talks go to the open-space block, which suits platinum. This only works if your structure has an open-space block (see open questions).
  4. A sponsor-visible review of your ticket sales, attendee fit, and CFP quality numbers (see measurement).

## Timeline

The event date is unknown, so these are relative to it:

- **Open:** as soon as possible, for at least 1 month. The standard window is about 2 months.
- **Close:** 8 or more weeks before the event, and never inside 6 weeks. Speakers need 4 to 6 weeks to arrange travel.
- **Review:** at least 2 weeks inside the gap between close and program announcement.
- **Notify:** state the date in the call.
- **Floor-compressed** (a hard date): about 4 weeks open, close at 6 to 8 weeks out, 2 weeks of review. Under about 10 weeks to the event, drop the open CFP and go invited via `event-speaker-sourcing`.
- **Year 2 is a compounding asset.** If you have room, a longer window helps. It only works if someone sustains promotion across the whole window.

## Submission form

Use the standard rung, one submission type per offered format:

1. Title (one line).
2. Abstract, max 100 words.
3. "Why you?" (optional).
4. Format, limited to the formats your structure offers.
5. Audience level: Just starting out / Some experience / Advanced experience.
6. Bio.
7. Prior-talk links (optional).
8. **Cap: three proposals per person.** This is the PyCon US figure. State it in the call.

**Employer and product disclosure field (my addition, not sourced).** Ask for the speaker's employer, and ask "does this talk center a product your employer sells?" This is cheap triage for the pitch problem. It lets reviewers route a talk to open space before scoring it.

## Published review criteria (draft text)

Adapted from the DevOpsDays six-point template:

1. No sponsor can buy a speaker spot. Sponsors may submit like anyone else.
2. New content is favored over already-published material.
3. We aim for a balance of local and out-of-town speakers.
4. New speakers are actively favored.
5. Bold subjects are encouraged.
6. Product- and tool-specific talks belong in open space, not the main program. Elevate the talk to the concept.

Criterion 1 holds only if you decline the guaranteed slot. Criterion 6 holds only if your structure has an open-space block.

## Anonymization posture

- **Default for a small volunteer committee:** named review, with published criteria carrying the fairness work. This is the field default.
- **Mandatory blind** fits if equity is a stated goal and you have capacity for two-phase review. In that case:
  - Hide author information in the first phase.
  - Instruct speakers to keep identifying details out of titles and free text.
  - Publish exactly when identity enters review.
- **Avoid opt-in anonymous.** A pool that mixes named and anonymous submissions isn't reviewed on one footing.

## Speaker benefits

- State the floor: every speaker gets a free event ticket.
- Add travel or an honorarium only if the budget has confirmed it. Direct payment raises tax, visa, and conflict-of-interest issues.
- If you run travel grants, use PyCon US's shape:
  - Grants enable attendance and don't reward quality.
  - One grant per accepted proposal.
  - Speakers who can afford to attend are asked to self-select out.
- Don't publish anything unconfirmed.

## First-time-speaker support

- Publish last year's accepted proposals, with permission, as worked examples.
- Add the "favor new speakers" criterion.
- Add proposal mentorship only if you have a volunteer mentor pool and a window long enough to pair mentors before close.

## Promotion

- No organizer has published a channel-by-channel breakdown of where submissions come from, so this part rests on a few sourced practices.
- Sustain promotion across the whole open window, not only at open.
- Sequence announcements as Write the Docs does:
  1. Write the announcement.
  2. Post it to the blog.
  3. Tweet a link to the post.
  4. Wait 1 to 2 hours, then send the mass email, so the community can catch errors first.
- If diversity is a goal, reach out actively. DevOpsDays warns that "under-represented people in tech are much less likely to respond to your CFP."
- Sourced mechanisms: the `jlengstorf/awesome-speaker-diversity` list with its template email, and PyCon 2010's categorized distribution list.

## How you'll know this year went better

Pick 2 or 3 measures and write the thresholds down before the CFP opens. Raw submission count is the wrong target, and your plan to cut it would have made this year look "better" without improving anything.

| Measure | Last year | Suggested threshold (you set it) | Revision if missed |
|---|---|---|---|
| **Off-policy share**: submissions the criteria already exclude, mostly vendor pitches | Unknown. "A big chunk" isn't a number. | Tag last year's 310 now to get the baseline. Set a target well below it. | If the share stays high, the criteria aren't landing. Move the criteria higher in the call and tighten the product-disclosure field. |
| **First-time-submitter share** | Unknown, tag it too | Beat last year's share. For scale, DjangoCon Europe 2024 had 51 first-timers among 138 submitters. | Add mentorship or worked examples. |
| **Submission timing**: when submissions arrive in the window | Unknown | No dead middle | If the middle is dead, promotion failed, not the window length. Rework the promotion plan. |
| **Submissions-to-slot ratio** (context only) | 8.2:1 | Stay at or above about 6:1 | If it drops below your floor of quality talks, the call is too narrow or reach is too thin. |

Also record qualitative signals: complaints about unexplained rejections, and whether the platinum sponsor renews without the guaranteed slot.

The measures to start with are the first two. Last year's data gives you the baseline for both.

## Handoff

- Submissions go to `event-talk-selection` for the rating grid, committee, and notifications.
- The invited-speaker channel runs in parallel via `event-speaker-sourcing`.
- The accepted program lands in `event-schedule-design`.
- Present the call section by section for validation before it goes public. Don't edit it quietly after launch.

## Open questions

These would change the design, and the skill asks them one at a time. Please answer them in your reply:

1. **Event date, and weeks until the program must be announced.** This sets the timeline rung.
2. **Does your structure have an open-space block?** Criterion 6 and the sponsor alternatives depend on it.
3. **Committee size and organizer hours.** This decides blind vs named review and whether mentorship is realistic.
4. **Budget.** What can you honestly promise speakers beyond the free ticket?
5. **Is speaker diversity a stated goal?** If yes, is there capacity for active outreach?
6. **What assets exist?** For example: last year's accepted proposals to publish, a mentor pool, or a CFP tool you already pay for.
7. **Which formats did last year offer?** The call must offer exactly the formats your structure has.

I can record the thresholds and revision triggers in memory once you confirm them.