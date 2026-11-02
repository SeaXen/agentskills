# Sanity check: Tessellate Hack judging plan

**Verdict: ⚠️ don't run it as planned.** Three of the four parts need to change. The averaging idea can stay, but only if one number checks out.

## What breaks

1. ❌ **One overall mark out of 100 per judge.**
   - Your brief names four categories: Impact, Craft, Originality, Storytelling. A bare number scores none of them, so teams built to criteria nobody applied.
   - The skill deletes the single overall score as soon as more than one track awards a prize. You have three prizes across two tracks.
   - A bare number can't say why a team won. That makes challenges hard to answer, and it leaves the tie-break with nothing to use.
   - A 0-100 scale is also too fine for a judge standing between two tables. Use 1-5 integers per criterion.

2. ❌ **Eyeballing the sponsor prizes from the same numbers.**
   - A payments-company prize and an observability-company prize each need a criterion the four categories don't contain: how well the project uses that sponsor's technology.
   - The same scores can't pick those winners. A general score blends in everything else, so it can't tell which project used the sponsor's product best.
   - Run separate weighted totals over the same sheet:
     - The sponsor criterion gets real weight in its own track.
     - It gets 0% in the general track, so a vendor's API calls don't buy a grand prize.
   - Tell each sponsor now that a project can win their track and place nowhere overall. That is the design working.
   - Announce sponsor winners from each sponsor's own written confirmation, collected before the ceremony.

3. ❌ **No conflict rule.**
   - "No formal process" is deleted from the skill's menu once any sponsor funds a prize.
   - Default to self-declared recusal: judges don't score a team they're close to, and they tell the judging lead so another judge can be routed in.
   - Name the fallback in advance for a team that loses too many judges.
   - Check the judge list against the entrant list before scoring starts.

4. ⚠️ **Plain average of the top three.** This is only valid if every judge sees every team.
   - Full coverage requires `N ≤ W / t`, where N is teams, W is judging-window minutes, and t is minutes per team.
   - The judge count doesn't appear in that formula, so adding judges can't extend full coverage.
   - Reference points for W = 120 minutes: 12 teams at 10 min/team, 24 teams at 5 min/team.
   - If the cap holds, a raw average is fine. A harsh judge shifts every team equally and the order doesn't change.
   - If the cap fails, judges see slices and a harsh judge shifts only their slice. Then you need per-judge normalization, and the number of judges per team is `k = floor(J × W / (N × t))`.
   - If `k < 1`, you need a published pass/fail pre-screen or a format change. Never shorten t on the day.

## Replacement plan

1. **Rubric: keep your four categories, in the brief's exact words.**
   - Score each 1-5.
   - Give each an integer weight, summing to 100.
   - My starting point to debate: Impact 30, Craft 30, Originality 20, Storytelling 20.
   - Put the heaviest weight on what a judge can observe in the slot. Craft is the most observable; "Impact" is the hardest to see in four minutes.
   - The numeric weights can stay private. Publishing the category names and a knockout list already satisfies disclosure.

2. **Tracks: three totals from one sheet.**

   | Prize | Computed from |
   | --- | --- |
   | General (1st, 2nd, 3rd) | Four categories only, weighted |
   | Payments sponsor | Four categories, reduced, plus a sponsor-technology criterion (about 30% in the skill's worked example) |
   | Observability sponsor | Same shape, with that sponsor's criterion |

   Decide whether one project can take both a general and a sponsor prize. I'd say yes, but state it in the rules.

3. **Combination rule: tied to your allocation band.** Raw average under full coverage, per-judge normalization under a sampled panel.

4. **Tie-break ladder: publish before submissions close.**
   - Highest score on the highest-weighted criterion.
   - Most judges who ranked the project first among the teams they saw.
   - A named tie-break judge decides, on the record, in one sentence.
   - Co-award only if the prize is divisible and the rules said so in advance.
   - No coin flips, and no re-scoring after the demos.
   - Your brief is already out, so publish this as a rules addendum while submissions are still open.

5. **Sponsor representatives judging their own track.**
   - If a signed agreement requires this, confine them to their track and pair them with at least one neutral judge.
   - Run a drop-test: compute the track rank with and without their scores.
   - If the winner changes, tell the sponsor before the ceremony.
   - Disclose the composition in the published rules before submissions close.
   - If nothing is signed yet, the drafting belongs to `event-sponsor-agreement`.

6. **Contest path.** Publish four things before submissions close:
   - A named person who receives challenges.
   - A short window that closes before prizes are paid.
   - What can change: arithmetic, eligibility, or a missed submission, but not a judge's opinion.
   - An answer that cites the rubric and the deciding criterion, not per-judge scores.

7. **Knockout rules (separate from the rubric).** Write them for how this event's own theme invites gaming, and publish them with the category names. I can't write them without knowing the theme or the brief's deliverable rules.

8. **Announcement.**
   - Announce from prepared slides, with the winner list collected before the ceremony.
   - Publish ranks and criteria only. Keep raw scores private.

## What I need from you

I can't confirm the allocation band without these. Please answer them in order.

1. Which demo/judging structure did you pick (expo table, stage pitch, video only), and how many minutes per team does it assume?
2. How many teams do you expect to submit, and how many minutes run between submission close and the ceremony start?
3. How many judges are confirmed, and can they all be in one room at once?
4. Does any signed sponsor agreement require that sponsor's rep to judge their own track? What criteria did you publish for the sponsor challenges?
5. Do teams get per-team feedback after the event?
6. Did the published rules already promise anything about ties or disputes?
7. Who can break a tie on the record, and is this a one-off or a recurring event?

## Do before judging opens

Six items must exist in writing with no blanks: weighted criteria, scale, the judge-to-team map, the conflict rule with its fallback, the tie-break ladder, and the contest path. Once scoring starts, changing any rule invalidates what's already scored.

**Not verified:** I haven't run any numbers, because I don't have N, W, J or t. The 12-team and 24-team caps come from the skill's reference table. The 30/30/20/20 weights are my own starting suggestion, not a standard.