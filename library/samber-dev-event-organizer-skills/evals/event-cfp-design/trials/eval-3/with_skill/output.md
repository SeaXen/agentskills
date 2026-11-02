# Brightloop Conf CFP: submission form and call (draft for validation)

I read the `event-cfp-design` skill and both of its references. Its interview wasn't possible here, so the open inputs are listed at the end. Four of your requests conflict with the skill, so I changed them. The reasons come first, then the form.

## What changed from your draft

| Your request | Decision | Why |
|---|---|---|
| One big unlimited text box | **Replaced** with split fields and a word cap | The skill names this a failure mode ("One text box for everything"). Reviewers can't score topic and speaker fit separately, and no anonymization is possible. Your draft is also the skill's own negative example. |
| Accept lightning talks | **Dropped** | The structure is fixed at 30-min talks and half-day workshops. The call must offer exactly the formats the structure has, because a lightning submission is one nobody can schedule. If you want them, reopen the structure through `event-format-selection` first. |
| 1-10 audience self-rating | **Replaced** with 3 tiers | Three tiers are enough, and a finer scale invites false precision. The tiers are the PyCon US ones. |
| Unlimited proposals per person | **Capped at 3** | The cap keeps review load proportional to the pool and discourages shotgun submissions. PyCon US uses the same cap. Volume isn't your bottleneck, since turning away most submissions is the normal state of a healthy CFP. The fix for volume is review capacity, not more intake. |

## 1. Timeline

The event date wasn't given, so these anchors are relative to it. E is the event date.

| Milestone | Anchor |
|---|---|
| CFP opens | E − 18 weeks |
| CFP closes | E − 9 weeks |
| Review | E − 9 to E − 7 weeks |
| Notifications and program announcement | E − 7 weeks |

- **Floor check:** the source floor is a call open at least a month, closing 6-8+ weeks before the event, with at least 2 weeks of review. Speakers need 4-6 weeks to arrange travel or time off.
- **If E is under about 10 weeks away:** the skill deletes the open CFP and the program goes invited, through `event-speaker-sourcing`.
- **Workshops:** half-day workshops need more prep, so notify them in the same window rather than later.

## 2. The form

Each type is its own submission type. Fields marked * are required.

**Common to both types**
- Title* (one line)
- Abstract* (max 100 words: the pitch, not the outline)
- Why you? (optional, max 100 words: why you're the right person for this topic)
- Audience level*: Just starting out / Some experience / Advanced experience
- Speaker bio* (2-3 sentences)
- Links to prior talks (optional)
- Email*
- Speaker name*

**Type A: 30-minute talk**
- No extra fields.

**Type B: half-day workshop** (shown only when selected)
- Outline* (a structured outline separate from the abstract)
- Prerequisites for attendees*
- Maximum attendee capacity*
- Hands-on setup requirements*

**Consent checkboxes:** code of conduct, recording permission, photo release. Collecting these now avoids chasing them after acceptance.

**Optional:** a photo, required only on acceptance.

**Cap, as stated in the form:** "Up to 3 proposals per person, across both types."

**Identity-bearing fields:** the name, bio, links and photo are kept separate so they can be hidden if you ever run a blind first phase.

## 3. Published review criteria

Draft text for the call:

> - **No pay-to-play.** No speaker spots can be bought by sponsors. Not ever.
> - **New content preferred.** Material already presented or published online is considered, but less attractive.
> - **Local and out-of-town balance.** We aim for a good balance between Manchester-area and visiting speakers.
> - **New speakers favored.** Brightloop is a supportive place for new voices.
> - **Bold subjects encouraged.** We don't want to hear the same things over and over.
> - **Concepts over products.** Elevate tool-specific talks to the conceptual level.

- **Dropped criterion:** the sourced sixth criterion routes tool pitches to open space. Your structure has no open-space block, so I replaced it with "Concepts over products" rather than promise a redirect that doesn't exist.
- **Honesty check:** publish only criteria you will actually apply. Name recognition and topic mix will shape selection, so don't claim otherwise.

## 4. Anonymization posture

I recommend **named review**, with the published criteria carrying the fairness work. That is the skill's default for a small committee tuning program balance.

- **State this in the call:** "Proposals are reviewed with speaker names visible."
- **Alternative:** mandatory blind review is stronger on equity but needs two-phase review and speaker instructions to scrub identifying details from free text. Choose it if diversity is a stated goal and the committee has capacity.
- **Avoid opt-in anonymous:** a pool that mixes named and anonymous submissions isn't reviewed on one footing.

## 5. Speaker benefits

Draft text for the call:

> All speakers receive a free Brightloop Conf ticket.

- **Nothing else goes in the call** until the budget confirms it. Travel and honorarium language published early runs into the taxes, visas and conflict-of-interest issues the DevOpsDays guide warns about.
- **If you add travel grants later:**
  - Frame them as enabling attendance, not rewarding quality.
  - Cap them at one per accepted proposal.
  - Ask speakers who can afford to attend to skip the request.
- **Honorarium calibration points** (not a market rate): !!Con pays a flat $256 and ffconf pays £500. Set your own figure against your budget and tax review.

## 6. First-time speakers and promotion

**First-time support**
- Use the published criteria plus the split form as calibration if this is your first CFP.
- If past editions exist, publish accepted proposals as worked examples.
- Keep the "favor new speakers" line either way.
- Skip mentorship unless you have a volunteer mentor pool and a long window.

**Promotion**
- Sustain promotion across the whole open window, not only at open.
- Sequence each announcement like Write the Docs: post it on the blog, share the link on social, then send the email 1-2 hours later.
- Under-represented people in tech are much less likely to respond to an open call.
  - If diversity is a goal, reach out directly to community groups.
  - `jlengstorf/awesome-speaker-diversity` has a list and an email template.
  - Add the Manchester-area frontend and tech groups you already know.
- No published data ranks promotion channels by where submissions came from, so I haven't invented a ranking.

## 7. Handoff and measurement

**Handoff**
- Submissions go to `event-talk-selection`.
- Invited speakers run in parallel via `event-speaker-sourcing`.
- The accepted program goes to `event-schedule-design`.

**Measurement:** pick 2-3 and write down the revision each would trigger next edition.
- Submissions-to-slot ratio. PyCon US 2025 was about 6.5:1, and on a first CFP even 2-3:1 is a strong signal.
- First-time-submitter share.
- Share of submissions the criteria already exclude.
- When in the window submissions arrive. A dead middle points to a promotion failure, not a window-length problem.

## Inputs I assumed or couldn't confirm

1. **Event date.** The timeline needs it. Please confirm it is more than 10 weeks away.
2. **Ownership.** I assumed a community conference. A vendor conference would couple the timeline to a launch calendar.
3. **First CFP or repeat.** I assumed first. A repeat could add worked examples and revisit anonymization.
4. **Budget.** I stated only the free ticket. Tell me if travel or an honorarium is confirmed.
5. **Diversity goal and committee size.** These decide named versus blind review.

Per the skill, nothing should go public until you've validated each section. The timeline, form and criteria are the ones to check first.