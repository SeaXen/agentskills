# GreenGrid plan sanity check

**Verdict:** ⚠️ Two problems need fixing before the board sees this. The 8%/4% target is borrowed, and the 12 problems don't cover 160 people.

## 1. The 8% invalid / 4% disqualification target

**Drop it as a target.** The brief-design skill says not to borrow a disqualification, invalid-submission or dispute rate from another event. Rates aren't comparable across formats, sizes and audiences. It also notes that no platform or survey publishes an aggregate DQ or dispute rate. Last year's 8% and 4% are one event's numbers, and your board is treating them as a benchmark.

Three more problems:

- **The denominator is undefined.** 160 is registrants, not teams or submissions. With 1-4 person teams you probably have 40-60 teams. At 50 teams, "under 4%" means at most 1 DQ, and "under 8%" means at most 3 invalid. One ruling moves the rate by 2 points, so the metric is mostly noise.
- **It rewards the wrong behaviour.** A ceiling on DQs pushes organizers to not disqualify, or to relabel DQs as "invalid." Clear published rules exist so you can point to them when you do have to disqualify someone.
- **It measures the outcome, not the cause.** Disputes come from ambiguous sentences in the brief, and the plan can control those.

**Replace it with gates you can verify before publication** (these are self-set, not industry standards, and the brief should say so):

1. **Structural gate.** All seven items exist in writing with zero blanks before publication. Iterate until the count is seven.
   - Hacking window as start and end wall-clock times.
   - Eligibility statement.
   - Team-size rule.
   - Per-track problem statement with its minimum viable submission.
   - Submission checklist matching the demo format.
   - Named evaluation categories.
   - Deadline with late policy.
2. **Ambiguity gate.** For every rule, write the reading a team arguing the opposite would use. Any rule with a second plausible reading isn't written yet.
3. **Signals to record.** Track clarification questions asked, submissions rejected as invalid and why, and tracks with no entries.

If the board insists on a number, report last year's 8%/4% as context only. Set the GreenGrid thresholds after this edition from your own logged counts, with the denominator stated (teams that submitted).

## 2. 12 engineers vs 160 participants

The civic-tech capacity rule is one expert-plus-workable-project pairing per four non-expert participants. It counts participants, not teams.

- 160 participants need about 37-40 pairings.
- You have 12, which is roughly 1 per 13 people. That covers about 48 people.
- The other ~110 are the "struggling to find something relevant to work on" group the ratio is meant to prevent.

Pick one:

- **Cap or stage registration** to about 48, or
- **Recruit about 25 more problem owners**, or
- **Split each of the 12 problems into 2-3 buildable sub-challenges** that engineers are willing to mentor.

Don't convert this into a tracks-per-team ratio. Twelve challenge tracks would also overshoot the one sourced ceiling, which scales track count to judging capacity (MLH: aim for 3 absent sponsor tracks, never 20 or more). Group the 12 problems into a few thematic challenge tracks instead.

## 3. Narrow-theme demand test

"Grid resilience" is a narrow vertical. You already have 160 registrations, so demand looks fine. The skill still wants a documented checkpoint:

- Checkpoint date, self-set count, and a pre-agreed wider theme.
- Confirm what each problem-owning engineer or employer keeps if the theme widens.

Nothing goes in the board plan until you've confirmed that the 160 count is final. If registration is still open and isn't capped, the count can still move.

## 4. Real utility problems: exposure to check before publishing

- **Data confidentiality.** Real problems from utility work may involve critical-infrastructure or internal data. The standard "code must be public and stay public" rule may be impossible to honour. Decide this before copying the sentence, and state the replacement visibility rule if you drop it.
- **Employer approval.** Do the 12 engineers have clearance to share their problems?
- **IP.** I write no IP clause. Route ownership questions to counsel via `event-sponsor-agreement`. Don't publish "participants keep their work" as a fact.
- **Fallback if a problem owner drops out.** Publish a rule for it. Written in advance it's a rule, and improvised mid-event it's a favour.
- **Prompts rewritten from the engineers' own words.** They'll describe benefits and context, not buildable constraints. Each of the 12 needs a structured statement with five parts:
  1. Context.
  2. The challenge as a question.
  3. Checkable constraints.
  4. Resources, including what is *not* provided.
  5. A minimum viable submission, so the quarter a team reaches is still demoable.

## 5. Open items I need before the brief can be drafted

I did not draft the brief. The skill needs these answers first, one at a time:

1. Hacking window in hours, and in person or digital?
2. Which demo/judging structure is already chosen?
3. Do participants bring problems, or do the 12 engineers supply them? (Likely both.)
4. Do any sponsors fund prizes, and does any agreement promise a named challenge track?
5. Does anything need sponsor API keys, accounts or datasets? Has someone built against it end to end?
6. Who may enter, and what team-size rule has `hackathon-team-formation` set?
7. Any beginner or student carve-out?
8. Do prizes carry cash value? Are minors expected? Is personal data collected at submission? Minors and personal data each force a review before publication, whatever the efficiency ranking says.
9. Publication date, one-off or recurring, and is counsel available?
10. Has anyone tested demand for the narrow theme? (Covered by § 3 above.)

**Next step:** answer 1, 2 and 8 first. They decide which rule set is allowed at all.