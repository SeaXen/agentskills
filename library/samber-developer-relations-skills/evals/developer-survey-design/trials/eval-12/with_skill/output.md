# Ashgrove SDK survey: what's missing before Monday

**Two parts of your plan break the skill's rules. Fix them before Monday.**

1. **Don't tweak questions during week 1.** Any wording change after full launch splits the data into two groups you can't compare.
2. **Don't pool the 40 Discord responses as-is.** Two questions changed after they answered, so they came from a different instrument.

I assumed "three weeks out" means Fri 13 Nov. I couldn't check your questionnaire, decisions or audience. Questions 1-4 gate the design, so my answers to them are open (last section).

## Re-ranking block (the skill requires this)

- Answer 4 (results in 3 weeks): calibration sample **demoted** to "next edition", because the date is under 4 weeks away.
- Answer 4: cognitive interviews **demoted** to "next edition", for the same reason.
- Answer 4: expert review and soft launch **kept**, and they become the pilot.
- Answer 5 (newsletter and Discord only, as far as I know): rung 2 of the claim ladder is **deleted**. Everything you publish is rung 1, "X% of respondents".

## Fix 1: freeze the wording, then pilot properly

Your plan skips the freeze. The skill's pilot rule (Step 6) is to freeze wording before the full launch.

**Plan instead of "send to everyone, tweak later":**

1. **Fri-Sun, about 2 h:** one person outside the team reads every question against the question-writing rules. They also complete the survey on a phone and with a screen reader. Grids and long multi-selects fail first there.
2. **Mon, soft launch:** send to about 5-10% of the newsletter, a random slice, through its own tagged link. Check three things:
   - **Median time**, against the length you'll state in the invitation. Budget the longest routed path, not the average.
   - **Breakoff point:** the question where people quit.
   - **Empty or "Other" answers:** a spike marks a confusing question.
3. **Tue, freeze.** Fix confusing questions and lock the wording. Log every change.
4. **Wed, send to the rest of the newsletter.** Tag these responses as the main wave.

This costs you two days of the field window and removes the need to tweak later.

**If a question still turns out to be broken in week 2:**

- Either drop it from the report, or
- report the before and after versions separately, labelled "not comparable".

Never merge them.

**Feedback from readers:** point it at one inbox or thread and log it for next edition. Don't act on it live.

## Fix 2: the 40 Discord responses

**Default: tag them `pilot` and keep them out of the headline numbers.** The skill keeps pilot responses only if no wording changed afterwards, and two questions did.

They are still useful:

- They show which questions confused people. That was their job.
- The Discord comments that led to the two changes are cognitive-interview material. Log them.

**Option, my judgement and not a skill rule.** You may pool the answers to questions that are word-for-word unchanged, if all of these hold:

- Question order and routing didn't change either, since position affects answers.
- The privacy notice and age gate were the same as Monday's (see item 3 below).
- You report them as a separate Discord-pilot source in the source mix.
- The methodology states the pilot and the two changed questions.

The two changed questions get no pilot data, whichever option you choose.

**Duplicates:** some of the 40 are probably on the newsletter. Tell them in Discord, "if you answered Thursday, you don't need to retake it." Without identifiers you can't dedupe them, so state the risk in the methodology.

## Checklist before Monday

Numbered by when to do it. Items 1 and 2 block everything else.

1. **Answer the four gating questions** (last section). Without them there is no decision table.
2. **Build the decision table.**
   - One row per question: the decision it informs, the owner, and the answer that would change the decision.
   - Cut any question with no row.
   - Cut any question your telemetry answers (SDK version, OS, language version, region).
   - Mark publication questions `publish`.
   - Book a readout meeting with each decision owner for the week results land.
   - Estimated time: 1-2 h.
3. **Privacy basics.** Skip this and a launch Monday becomes a launch blocker if you have EU or UK respondents.
   - **First page:** a privacy notice (who runs it, why, legal basis, processor, retention, what you publish) and an age gate (16+, or 18 if you ask sensitive items), before question 1.
   - **Contact details:** follow-up interviews or any incentive need a separate form and separate unticked consent. Never put email in the response table.
   - **Newsletter email:** the invitation must carry no promotion. A survey that feeds sales is marketing, and marketing-email rules apply.
   - **IP logging:** switch it off in the survey tool.
   - **Thursday's version:** check it had the same notice. If not, that is one more reason to keep the 40 out.
4. **Length.** State a median completion time in the invitation, from the soft-launch median. Price per screen or grid row, and about a minute per open-text box.
5. **Open-text hours.** Time yourself coding 50 answers, extrapolate to your expected completes, and cap the boxes at the hours available.
6. **Source tags.** Give Discord, the newsletter slice and any other channel distinct links or a hidden field, so you can publish the source mix.
7. **Cleaning rules, written now.** Qualifiers, speeders (below about a third of the median for the routed path), straight-lined grids, duplicates and bots. Record the count each rule removes.
8. **Incentive: none by default.** Promise respondents the results first, posted to every channel before any press release. If you do offer a public prize, switch on the fraud checks first: a trap option nobody can have used, and an attention check.
9. **Language.** A single-language survey under-samples everyone less comfortable in it. Translate, or name that gap in the bias sentence.
10. **Who has seen the questionnaire?** If a sponsor or partner saw or changed it, the methodology names them.

## Timeline to the Fri 13 Nov deadline

| Date | Step |
|---|---|
| Fri 23 - Sun 25 Oct | Decision table, expert review, privacy pack, cleaning rules |
| Mon 26 Oct | Soft launch to a random 5-10% of the newsletter |
| Tue 27 Oct | Review median time, breakoff and empties. **Freeze wording.** |
| Wed 28 Oct | Send to the rest of the newsletter; post in Discord |
| Mon 2 Nov | One reminder, optional |
| Fri 6 Nov | Close the survey. A field window of about 9 days leaves analysis time. |
| Fri 6 - Wed 11 Nov | Clean, analyse, hand-code open text |
| Thu 12 Nov | Readouts with decision owners |
| Fri 13 Nov | Results land |

If the deadline is earlier than 13 Nov, shorten the close date, not the soft launch.

## What you can claim in the results

Everything is rung 1. Use this wording:

> "62% of the 1,240 respondents use X. Respondents came mostly from our newsletter and Discord."

Don't write "62% of developers". Don't print a margin of error. An open link has no valid one. Don't report a response rate either, because an open link has no denominator. Report the funnel instead: views where known, starts, completes, kept.

Your methodology must include a plain sentence naming who the sample over-represents, which is likely engaged Ashgrove users.

Every chart carries:

- the exact wording
- who was asked and n
- "multiple answers allowed" where true
- how "Don't know" was handled
- "not weighted"

Trend claims need unchanged wording and a similar source mix. This is your first edition, so there is nothing to compare to yet.

## Open questions I need answered

These are the skill's gating questions. Your answers decide the decision table and the claim rules.

1. Which decisions will the results feed, and who owns each (roadmap, docs, community, marketing)?
2. Will results be published outside the team, or will anyone quote headline percentages in a report, press release or sales deck?
3. Who is the population: Ashgrove SDK users, community members, the wider ecosystem, or prospects?
4. Is this a one-off, or the first edition of a yearly series? If yearly, we freeze a core module of questions now.

Also useful: are your respondents or organisation in the EU or UK, is a partner co-running the survey, and which survey tool are you using?

Paste the questionnaire and I'll build the decision table next.