# Tidewater Devcon: selection plan for Monday

**Short answer: no, you're not covered.** The anonymous mode is a good start, but it does not deliver the blind review you promised, and the travel-grant field makes that gap matter. Fix three things before reviewers open the first proposal:

1. ⚠️ **The platform hides the author field, not what authors wrote.** Titles, abstracts and outlines still carry names, employers, past talks, project names and writing style. Your community is tight, so reviewers will recognise people from content alone.
2. ⚠️ **The grant question must not reach reviewers.** You told submitters that asking won't hurt them. Check that the grant column is hidden in the review view, in exports and in any shared spreadsheet. If the platform can't hide it, strip it before reviewers see anything.
3. ⚠️ **Four reviewers can't also be the anonymizers.** The anonymizer role must not score anything. You need one or two extra people for it, ideally outside the reviewer four.

I've assumed some answers below because you gave a lot of context but not all of it. The assumptions are listed at the end, and I've marked where my numbers are my own design rather than sourced.

## 1. Committee

- **Model:** small consensus committee. Four graders, one non-voting anonymizer role, one synchronous discussion round.
- **Add:** one or two anonymizers from outside the grader four. A trusted helper who won't submit and won't grade is enough.
- **Arbitrator:** name one person now, for any reviewer who won't recuse. This is not a published practice. It's my addition, so label it that way to the committee.
- **Reading load (my arithmetic):** if every proposal gets three reads, 240 × 3 ÷ 4 = 180 reads per grader. If all four read everything, it's 240 each. Confirm everyone can do that by the discussion date. If not, the process has failed before it starts.

## 2. Rubric: letter-grade advocate scale

Write it down before anyone scores. Changing it mid-review re-scores whatever was read first.

| Grade | Meaning |
| --- | --- |
| A | Will actively advocate |
| B | Likes it, won't advocate |
| C | Neutral |
| D | Will advocate against |
| X | Abstain: suspect I know who the speaker is |

- **Aggregation:** a best-worst pair per proposal ("AC"). Never average.
- **Floor:** at least one A to be seriously considered.
- **Comments:** mandatory on every grade. They become the decline feedback later.

## 3. Anonymization: promote to a dedicated anonymizer

Your grant question is a promotion condition for this option. Anonymization is what enforces "asking won't hurt your chances". A tight community that recognises people is a second condition.

**Anonymizer steps:**

1. Rewrite identifying details into placeholders, such as "[Large Tech Firm]" or "[they]".
2. Keep identity where it is the talk's own subject.
3. Assign random IDs, so submission order can't identify anyone.
4. Move grant requests into a separate sheet that no reviewer sees.

**Where identity re-enters:** only after the final accepted list is fixed. Then the anonymizer, and only for accepted speakers, reveals names so logistics can start. Declined submitters are never named to the grader team. Publish this boundary to submitters now.

**Grant decisions:** a person who graded nothing handles them, after selection. This keeps your promise true, and checkable.

**Timing risk:** 240 proposals is a lot of manual rewriting. At an estimated 5 minutes each (my guess), that is about 20 hours of work, so two helpers take roughly 10 hours each. If that can't be done by Monday, move the start date. Starting with leaks is worse than starting two days late. Don't start grading on a half-anonymized pool, because reviewers have then already read the names.

**State the limit out loud, to the committee and in the plan:** no evidence shows anonymized review changes acceptance outcomes by demographic. It's a defensible process promise. It is not a proven equity outcome, so don't claim one.

## 4. Conflict-of-interest brief (send before scoring opens)

- **Abstain (X)** on a proposal where you suspect you know the speaker. In your community this will happen often.
- **Abstain, don't score**, on a colleague, a close collaborator, or an employer or competitor of yours. Review with your event hat on.
- **Disclose in the review text** for lesser conflicts, such as a friendship or the same meetup circle, if you keep reviewing.
- **Recusal fallback:** decide now what happens to a proposal that loses too many graders. Suggested: fewer than 2 valid grades means the arbitrator assigns one additional grader. This is my own design.
- These are honour-system rules. No registry or audit exists anywhere, so say so.
- **Organizers who submit:** disclose before scoring, abstain on your own talk and your employer's, and agree a cap on organizer talks. Sponsor-affiliated speakers go through the same review under a self-set cap.

## 5. Rounds and cut rule (fix before anyone sees a ranking)

These numbers are my design, not sourced figures. Adjust them, but only before scoring.

1. **Round 1:** each proposal gets at least 3 grades, with comments. Assign by random ID, and reassign anything marked X.
2. **Cut:** every proposal with at least one A goes to discussion, and everything else is out.
3. **Safety valve, set now:** if more than about 60 proposals have an A, require AA or AB. If fewer than about 40 do, add the top ABs. Write the tiebreaker down so the line isn't drawn around a favourite.
4. **Discussion round:** one synchronous meeting. Fill 30 slots, then order 5 backups (the documented waitlist size, scaled to your decline risk).

For calibration, 30 of 240 is 12.5%. PyCon US 2025 selected about 15% of 938, and KubeCon EU 2024 about 9%. Turning away most proposals is normal.

## 6. Program-fit pass (on the shortlist only)

Check topic spread, employer spread, local versus out-of-town, and first-time speakers. Also check:

- **Vendor talks:** if the audience forgot the product name tomorrow, would they keep the lesson?
- **Freshness:** check "latest" claims against the event date, not the submission date. Consider holding a few slots open for late invitation.

**Record every trade-off in writing**, including what you swapped and why. Otherwise next year's committee re-argues it blind. Decide before review whether any balance target is a goal or a gate.

## 7. Communication, in this order

1. **Acceptances and waitlist notices together**, each with a confirmation deadline.
2. **Declines** once acceptances are confirmed.
3. **Program announcement.**

Hold to the notification date you published. A missed date costs more trust than any wording recovers.

- **Waitlist:** promise a date, never the odds.
- **Decline wording:** "We received 240 proposals for 30 slots. Selection followed the criteria we published." Add that the pool was reviewed anonymously.
- **Feedback:** if you can afford the editorial time, edit reviewer comments into per-proposal feedback, since mandatory comments make it nearly free to produce. Send nothing a reviewer didn't write.
- **Accepted speakers:** one commercial-demo rule in every acceptance email.
- **Duplicates:** if someone has two accepted talks, let them choose which to give.

## 8. Record for next edition

- Acceptance ratio.
- First-time speaker, employer and local/out-of-town shares against what you promised.
- Number of X abstentions, and number of proposals that lost reviewers to recusal.
- How many declined submitters submit again.

## Assumptions to correct

- The call promised blind review and a notification date, and I haven't seen its exact wording. Check that the plan matches it.
- Your program-announcement date is far enough away for a two-round process.
- You don't need a multi-tier cascade (this is a single-room committee, not a multi-track one).
- No invited or sponsor talks sit in the same pool. If any do, decide their lane before Monday.
- You'll run this yearly, so the rubric and the decision record are worth keeping.

## Questions that would change the plan

1. How many people can act as anonymizers, and by when?
2. Can your platform hide the grant field from the review view and from exports?
3. Do any of the four reviewers, or their employers, have proposals in the pool?
4. Who arbitrates a deadlock?

Tell me the answers and I'll tighten sections 1 to 5.