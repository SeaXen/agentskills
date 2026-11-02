# Reviewer conflicts: policy and refusal fallback

This follows the `event-talk-selection` skill and its references. I skipped its usual interview because you're short on time. I assume your 7 reviewers include a non-scoring anonymizer, or that you can name one before Thursday.

## The policy

**Abstain from the proposals you have a conflict with. Don't score and disclose.** The rule is to skip the question when the submitter is a close colleague or works for an organisation you compete with. Abstaining also covers the case where you suspect you've identified an anonymised author. Reviewers should act on behalf of the event, not their employer.

| Case | Ruling | Why |
|---|---|---|
| **Marisol** and her desk-neighbour | ❌ Not "score + note". She abstains on his proposal. | He is a close colleague, so skip-the-question applies. A note added after scoring doesn't undo the score. Her score also feeds the best-worst pair, and one "A" is the practical floor for serious consideration. A note in a shared comment can also unblind the discussion. |
| **Reviewer 90% sure of the author** | ✅ Abstain with an **X**. | This is the identity-suspicion rule. 90% is enough, and he doesn't need proof. He should not name the suspected author to other graders, because that unblinds the proposal for them. |
| **Reviewer at a competing company** | ✅ Abstain on the 3 competing submitters' proposals only. Not on the whole pool. | The rule covers organisations you compete with. Recusing from the whole pool would waste a reviewer for no gain. |

How the abstentions work in practice:

1. **Use the anonymizer as the go-between.** Under blind review the competitor-employer reviewer can't tell which proposals are the three. The anonymizer sees the raw names, so the reviewer tells the anonymizer privately. The anonymizer pulls those proposals from that reviewer's queue. Marisol does the same.
2. **Don't make anyone point at a proposal.** If Marisol can't tell which proposal is her colleague's, she gives the anonymizer his name and nothing else.
3. **Ask the style-guesser to report privately.** Tell the anonymizer, not the committee. The anonymizer can then check whether the proposal needs more rewriting.
4. **Reviewers with a lesser conflict may continue if they disclose it.** Same employer, a friendship or a topic bias can be stated in the review text itself. This option comes from PyConDE's model. Marisol's case is too close for it.
5. **Log everything.** Record each abstention and disclosure next to the proposal. If the program later looks self-serving, that record is your defence.

Note that the call may have promised blind review, and these abstentions are not that process breaking. Blind review hides the author field but not writing style. These recusals are the backstop for the gap you've just found.

## The honest limit

Every published recusal rule is honour-system. No registry, escalation path or audit mechanism appears anywhere in the sources. **The refusal procedure below is my own design, not an established practice.** Say so if anyone challenges it.

## Decide before Thursday

1. **Name the arbitrator.** Pick one organizer who isn't conflicted on that proposal. Name a backup in case the arbitrator is the conflicted one.
2. **Set the floor for a proposal that loses reviewers.** With 7 reviewers, one or two recusals still leave 5 or 6 scores. Suggested floor: **at least 3 scores** (my number). It borrows PyConDE's rule that a proposal holding 3 or more reviews stops being actively resurfaced, and that rule is a de-prioritisation threshold, not a standard. If a proposal falls below the floor, an unconflicted organizer or reserve reviewer scores it. The anonymizer cannot score it. Flag it in the discussion round as "fewer graders, less comparable".
3. **Brief everyone in writing before scoring opens.** The rule costs one paragraph and only works before scoring starts.

## If someone refuses to step back

Fix it structurally rather than by persuasion:

1. **Ask once, privately.** The arbitrator explains the rule and why it protects the reviewer too. Give the reviewer the abstain option, and the disclose option only if the conflict is lesser.
2. **Remove the assignment.** The anonymizer pulls the proposal from their queue, so they can't score it. This works only while the proposal is still anonymous to them.
3. **If they have already scored, exclude that score.** Drop it from the aggregate and tell them in writing. Don't let it count with a note attached.
4. **If they keep pushing, tell them it is a condition of reviewing.** The arbitrator can drop them from the committee for those proposals. If it happens repeatedly, drop them from the committee. Write down who decided and why.
5. **Check that the rest of their scores are independent.** If they were willing to bend this rule, you may want to look at their other scores before the cut.

Don't:
- Let the dispute run past scoring.
- Let the conflicted reviewer take part in the discussion on that proposal.
- Retrofit anonymity afterwards. Once reviewers have seen names, it can't be taken back.

## Reviewer brief, ready to paste

> Before scoring opens: abstain (don't score) on any proposal from a close colleague, or from an organisation you compete with. Abstain with an X if you think you've identified an anonymised author, and tell the anonymizer privately, never the group. For lesser conflicts, such as the same employer or a friendship, you may continue only if you state the conflict in your review text. Do not read others' reviews on a proposal you abstained from. If you won't abstain, [arbitrator name] decides, and your score on that proposal will be excluded.

Still open:
- Does your call promise blind review or named review? If named review, the same policy applies and the anonymizer step drops out.
- Who is your anonymizer?