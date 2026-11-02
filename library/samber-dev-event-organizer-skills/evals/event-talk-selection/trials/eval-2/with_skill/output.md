# Kestrel Summit selection plan: 310 proposals, 28 slots

## Recommendation

**Run this edition as a named review, as the call promised. Do not switch to anonymous review on Monday, and do not announce it as the diversity measure.** Three reasons:

1. **The call promised named review.** The skill's rule is to delete anonymization from the menu when the call published named review. Submitters wrote their proposals knowing reviewers would see their names and bios. Changing the rules at the moment reading starts breaks that promise. Only the start date makes the change technically possible: the skill says retrofitting after reviewers have seen names anonymizes nothing, and here nobody has read yet.
2. **It cannot be done properly by Monday.** Real anonymization of 310 proposals needs a dedicated anonymizer: one or two people who never score, who rewrite identifying details into placeholders and assign random IDs. Tool-level hiding only removes the author field. It leaves bios and "at my company…" text in the abstract. Half-done blind review is what the skill calls anonymization theater.
3. **There's no evidence it fixes the imbalance.** No published evidence shows anonymized review changes acceptance outcomes by demographic. It's defensible as a process commitment, not as a proven equity result. Last year's 24 of 26 is more likely an outreach problem. The skill's evidence file says under-represented people are much less likely to respond to a CFP. Review can't fix a pool that never arrived. It can only trade at the shortlist stage.

Announcing it as a diversity measure would also be a claim you can't back up. If next year's numbers don't move, the announcement becomes the criticism.

## What to tell the two board members

- Anonymization is a good idea, but for next edition, in the call design. The call can then promise it, and it gets a proper anonymizer role and time to run.
- This edition, the levers that exist are: a stated balance pass at the shortlist, a written record of the trades made, and outreach for next year.
- If the board still overrules, that's their decision. Conditions:
  - Notify every submitter before Monday that review is now anonymous, and say what changed.
  - Staff a real anonymizer.
  - Delay the start if needed.
  - Present it as a process change, not a proven outcome.

## 1. Committee model and roles

The ratio is about 11:1 (9% acceptance). That's in the KubeCon EU 2024 range (9%), so a high decline count is normal.

I haven't had answers to the effort questions (reviewers, hours, tracks). My default is a **distributed reviewer pool with a closing committee meeting**. It's the only documented model with a real reviewers-per-proposal figure.

- **Reviewers:** each proposal gets at least 3 reviews, about 930 reviews in total. With 8 reviewers that's about 116 each, so check it against your real hours. Once a proposal holds 3 reviews, stop actively surfacing it.
- **Committee:** meets after the review window closes, decides from scores and comments, and is not a second scoring tier.
- **Arbiter:** one named person breaks deadlocks and rules on recusal disputes.
- **Fallback if fewer than about 6 people can really read:** shrink the pool by an explicit first-pass rule, such as an eligibility screen against the published criteria. That is your own design. Label it as such.

Solo curation is off the menu, since you published open criteria.

## 2. Rubric, written before anyone scores

Use the 0–3 scale with a mandatory written comment on every review:

| Score | Meaning |
| --- | --- |
| 0 | No, strong: would argue against accepting |
| 1 | No, indifferent |
| 2 | Yes, indifferent |
| 3 | Yes, strong: would argue strongly in favor |

Guiding questions: is the topic current and relevant, how detailed is the submission, what problem does it address, what are the takeaways. Positive signals are practical methodology, open-source tooling, and ethics discussion. Negative signals are product-selling talks and talks already given at very similar events.

Add the published criteria from your call as scoring questions. Don't add new ones mid-review.

## 3. Anonymization: named review, with the boundary written down

- **Execution depth:** named review, as published. Reviewers see names and bios.
- **Where identity enters:** from the start, for everyone, per the call. There's no blind phase.
- **What carries fairness instead:** the published criteria, mandatory comments, and the conflict-of-interest rules below.
- **Bias guard on bios:** add one line to the reviewer brief. Score the proposal on the rubric, and use the speaker field only for the "speaker fit" question. Say plainly that this is a norm, not a control.

## 4. Conflict-of-interest brief

Send this before scoring opens.

- Abstain on colleagues you work closely with, or on organizations you're associated with or compete against. Review wearing the event's hat.
- Abstain if you're the author or helped write it. Don't read the other reviews on it.
- For a lesser conflict (same employer, a friendship, a topic bias), disclose it in the review text.
- Organizers who submit disclose it, abstain on their own talk and their employer's, and stay under a written per-edition cap. The same goes for sponsor-affiliated speakers.
- **Arbitration:** the named arbiter rules on refusals. A proposal that loses so many reviewers to recusal that its scores are no longer comparable goes to the committee for a discussion-only decision. Both are your own design, because no published registry or escalation procedure exists.

## 5. Rounds and cut rule

State the cut before seeing any ranking. Proposed (adjust, then freeze):

1. **Round 1:** every proposal gets 3 or more reviews. Rank by mean score, and treat any proposal with a 0 as needing discussion.
2. **Cut:** the top 30% (about 93 proposals) advance. This mirrors the cascade's published first-stage percentage, but it's your own threshold here.
3. **Round 2:** the committee meets on the shortlist only and reads comments, not just scores.
4. **Fill the slots:** 28 slots, then an ordered waitlist of about 5 to 8. Five is the one documented size, so say you're extrapolating if you go higher.

## 6. Program-fit pass: where balance is actually addressed

This pass is the only place this edition can respond to last year's criticism. It's allowed only through criteria the call published.

- **Check the published criteria first.** If the call listed new speakers, local versus out-of-town spread, or topic spread, those are legitimate inputs. If gender or under-representation balance was never published, adding it now is a post-hoc criterion. Decide with the board whether to add it, and tell submitters. Don't use it quietly.
- **Decide before review whether any target is a goal or a gate.** An example is "at least X% of speakers who don't identify as men". The one documented quantified targets (50% new speakers, 25% end-user companies) weren't rubric line items.
- **Write down every trade:** which higher-scored talk lost to which lower-scored one, and why. Next edition's committee will otherwise re-litigate it blind.
- **Also run:** the lesson-transfer test for vendor talks, the topic-freshness check against the event date, and the depth gradient if the room is mixed.

## 7. Waitlist and notification sequence

1. Acceptances and waitlist notices go out together, with a confirmation deadline on acceptances.
2. Declines go out once acceptances are confirmed.
3. The program announcement comes after that.

Honor the notification date the call published. Don't give waitlisted speakers odds, only the date they'll know by.

**Acceptance:**
> Your proposal **"{title}"** has been accepted for Kestrel Summit, {date}. Please confirm by **{deadline}**, or we'll offer the slot to another speaker. What you get: {perks as the call stated}. What we need next: {bio, headshot, slide deadline, travel}. No commercial demo or sales pitch: the audience should leave with the lesson, not the product.

**Waitlist:**
> Your proposal **"{title}"** is on our waitlist for Kestrel Summit. It made our final shortlist and would be programmed if a slot opens, which sometimes happens and sometimes doesn't. You'll hear from us either way by **{date}**. Please don't hold travel on our behalf.

**Decline (default, with criteria recap):**
> Thank you for submitting **"{title}"**. We're not able to include it this year. We received 310 proposals for 28 slots, so we declined many talks we'd have liked to program. Selection followed the criteria we published with the call: {criteria in one line}. We'd like to see you submit again next year.

Per-proposal feedback is optional. Your rubric already mandates comments, so only editing is missing. Strip reviewer names and say the feedback explains this decision, not a general assessment of the speaker.

## 8. Metrics to record

- **Acceptance ratio:** 28 of 310, about 9%.
- **Balance outcome vs stated goals:** women and non-men share of submitters versus accepted, plus first-timers, employer spread, and local versus out-of-town. Compare the submitter share to the accepted share. If they match, the problem is the pool, not review.
- **Reviewer coverage:** proposals per reviewer and how many lost reviewers to recusal.
- **Declined-submitter return rate** next edition.

Write down now what each result would change. For example, a submitter pool that's already skewed means you invest in outreach, not in review mechanics.

## What this edition can credibly announce

- A written rubric, mandatory comments, a recusal brief, and a recorded balance pass.
- Outreach commitments for next call.
- Next edition's call will promise anonymized review, with a dedicated anonymizer, published before the call opens.
- Don't say it "fixes" or "will fix" the gender imbalance. Say what you did and report the numbers afterward.

## Questions I still need answered

These change sizing, not the recommendation:

1. How many people will really read, and for how many hours?
2. Single-track or multi-track?
3. What is the program-announcement date?
4. Exactly which criteria did the published call list?
5. Does the call mention gender balance or first-time speakers?
6. Do organizers or sponsors' staff submit?
7. Are there invited talks in the same program?
8. Does the form carry travel-grant requests? That would raise the case for an anonymizer next year.