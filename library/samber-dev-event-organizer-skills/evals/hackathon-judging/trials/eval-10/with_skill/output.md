# Sableford Hack: judging and closing-ceremony plan

**Next action today:** send me the six numbers in "Open inputs", then publish the contest path (section 6) to every team. Both are needed before Sunday.

## Verdict on the plan as it stands

| Element | Verdict | Why |
|---|---|---|
| Announce live from your notes | ⚠️ Change | Winners get collected before the ceremony and read from slides. Notes invite improvising at the podium. |
| Project the full scoring sheet with judge names and raw marks | ❌ Drop | It doesn't prevent rigging accusations. It gives teams a leaderboard to audit at a precision the rubric wasn't built for, and it names every judge next to every mark. |
| Top five do live demos while the sponsor judges finish | ❌ Drop | Demo slots and judging draw on the same minutes. The top-five list also tells the room who is in the running before anything is announced. |

## 1. Announcement plan

1. Set a hard deadline for sponsor-track judges, e.g. 60 min before the ceremony. Get each sponsor's winner in writing. Announce sponsor-track winners from that confirmation, so the ceremony isn't where a sponsor changes its mind.
2. Build one slide per prize: track, winner, and the criteria that decided it. Lock the deck before doors open.
3. Announce **rank and criteria only**. Withhold per-judge marks, per-team raw marks, and the numeric weights (unless Sableford already published the weights before submissions closed).
4. Open the ceremony only once every winner is confirmed. If a sponsor track is late, announce it last. Don't fill the gap with demos.
5. Fill stage time with content that doesn't use the judges' minutes: sponsor talks, a keynote, a recap reel, or a short break. Don't preview finalists.
6. Run the drop-test on every sponsor track where the contract puts the sponsor's own rep on the panel. Compute the track rank with and without that judge's scores. If the winner changes, tell the sponsor before the ceremony and decide in advance who makes the call.
7. Check the judge list against the entrant list now. Judges, organizers, volunteers, and sponsors can't compete as hackers.

## 2. Why the scoring sheet stays private

- A uniformly harsh or generous judge shifts every mark they give. Public raw marks make that look like bias, so you'd get more accusations, not fewer.
- Teams would argue about decimals the rubric never promised.
- Judges would be exposed by name. That makes recruiting harder next edition.
- Public marks answer "who scored us low?", which isn't the question. The question is whether the process was fair, and a published process answers it.

**What kills the rigging accusation instead:**

- Say on a slide that the criteria were published in advance, every team was judged on the same rubric, conflicts were recused, and there is a challenge path (section 6).
- Show the tie-break ladder if one was needed.
- Name the judges on a "Meet the jury" slide, without attaching marks to them.

**If you still want full transparency:** it's a legitimate choice, but make it deliberately, not as an anti-rigging reflex. It needs a rubric robust enough to survive audit and a published tie-break ladder alongside. Judges must also have been told beforehand that their marks would be public, and it's too late to tell them now. If you go this way anyway, publish team-level totals only, never judge names.

## 3. Allocation check (blocked on inputs)

I can't confirm the window is feasible yet. The test is `k = floor((J × W) / (N × t))`.

- `k ≥ 1`: every team can get a judge at the format's contact time.
- `k < 1`: the plan is Band 3. That means a pass/fail pre-screen, or a longer window. Never shorten `t` on the day, because that re-scores whichever teams were seen first.
- Full coverage is only possible if `N ≤ W / t`. Adding judges doesn't change that cap.

**Open inputs:**

1. Number of teams that submitted (`N`).
2. Minutes from submission close to ceremony start (`W`).
3. Confirmed judges (`J`), and whether sponsor judges are counted in them.
4. Demo/judging format and contact time per team (`t`).
5. What the published rules promised on criteria, tie-breaks, and disputes.
6. Whether any signed sponsor agreement requires that sponsor's rep to judge its own track.

## 4. Pass threshold: six items in writing before scoring is final

| Item | Status |
|---|---|
| Criteria with weights | Confirm against the published brief |
| Scoring scale | Confirm |
| Allocation map: judge, teams, order, start time | Blocked on inputs 1-4 |
| Conflict rule and recusal fallback | Add: self-declared recusal, replacement judge routed from another panel, swap recorded |
| Tie-break ladder | Add if not published (below) |
| Contest path | Publish now (section 6) |

**Tie-break ladder:**

1. Highest score on the highest-weighted criterion.
2. Most judges who placed the project first among the teams they saw.
3. A named tie-break judge decides, on the record, in one sentence.
4. Co-award, only if the prize is divisible and the rules said so.

No coin flip, no re-scoring, and no organizer override of the judges' combined result.

## 5. Record before the ceremony

Teams that got fewer judges than the map promised, recusals that fired, and challenges received. Pick two or three and write down what each would change next edition.

## 6. Contest path to publish to all teams now

Submissions have already closed, so this is late. Send it to everyone, not just the team that asked, and say it's being added for transparency. If the original rules already contained a dispute process, use that wording instead.

- **Receives challenges:** `[named role, e.g. Head of Judging]`
- **Window:** `[e.g. 48 h after the ceremony, closing before any prize is paid]`
- **What can change:** an arithmetic error, a missed submission, or an eligibility fact
- **What cannot change:** a judge's opinion
- **Answer you'll get:** written, naming the rubric, the weights, and which criterion decided. No per-judge scores.

## Reply to the team

> Subject: Re: What happens if we think the result is wrong
>
> Hi [name],
>
> Thanks for asking before the ceremony rather than after. Here is how it works.
>
> If you believe the result contains an error, send it to [role / address] within [window] of the ceremony. That window closes before any prize is paid. We're sending this process to every team today, so everyone has the same information.
>
> A challenge can change the result if it shows an arithmetic error, a missed or mis-recorded submission, or an eligibility mistake. It can't change a judge's opinion of a project. If a challenge shows an error, we'll correct it before prizes go out.
>
> You'll get a written answer. It will explain how the rubric and its weights were applied and which criterion decided the ranking. We don't share individual judges' scores, so that judges can mark freely and teams aren't compared at a precision the rubric wasn't designed for.
>
> Judges were asked to step out of scoring any team they have a tie to. Ties are checked against the entrant list before results are final.
>
> Best,
> [your name]

**Don't promise in the reply:** re-judging, access to scores, or a specific outcome. Don't add anything about this year's ranking, since none exists yet.

## Do this before Sunday

1. ⏳ Send me the six inputs. I'll compute `k` and the allocation map.
2. Publish the contest path to all teams.
3. Set the sponsor-judge deadline and collect sponsor confirmations.
4. Cut the top-five demos and the live scoring-sheet projection from the run-of-show.
5. Build and lock the winner slides.