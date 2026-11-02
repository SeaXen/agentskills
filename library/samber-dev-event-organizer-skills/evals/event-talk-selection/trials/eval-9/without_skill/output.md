# Riverbend Summit: setting up selection with quotas

## Short answer

Don't add the weighted "diversity" column. Score quality only, then pick the program in a separate, logged step that enforces the board's two quotas.

## Why the 20% column fails

- **It doesn't match the board's ask.** The board set floors on the final program (≥19 first-time, ≥10 end-user). A 20% weight is a bonus on each talk, and it can't guarantee either floor.
- **It's too strong and too vague.** Scores for the top 150 talks sit in a narrow band. A 20% component will reorder that whole band, so a 3.9 talk can outrank a 4.5 talk. Nobody can say why 20% and not 5% or 40%.
- **It asks reviewers to judge things they can't judge.** "First-time" and "end-user company" are facts. Collect them on the submission form and verify them. Don't let reviewers guess.
- **It recreates the January argument.** The swap becomes invisible, buried in a sum.

## The setup

### Step 1: Freeze the rules before opening submissions to reviewers

Get board sign-off on a one-page rules doc. Settle these definitions:

| Item | Proposed default | Why it matters |
|---|---|---|
| Target numbers | 19 of 38 first-time, 10 of 38 end-user (9.5 rounded up) | "At least" means floors. |
| Floor or goal? | Hard floor, unless the board says otherwise | Ask the board. |
| First-time speaker | Never given a talk at any public conference or meetup | A narrower definition ("never at Riverbend") changes the pool a lot. |
| End-user company | Employer's main revenue isn't selling software, cloud, consulting, or training in this domain | Consultancies, vendors, and cloud providers don't count. |
| Overlap | One talk can count toward both quotas | Otherwise you need 29 slots of quotas. |
| Panels | The quota is met if a clear majority of panelists qualify. For panels, I'd count only moderators plus panelists, with no partial credit. | Pick one rule and apply it to everyone. |
| Per-track | Quotas apply to the whole program. Each track needs ≥3 first-time and ≥2 end-user talks as a soft check. | Prevents one track becoming all vendors. |

### Step 2: Run a feasibility check on the data

Count first-time and end-user submissions among the 420 before anything else. If end-user talks are only 8% of submissions (about 34), the 10-slot floor needs near-total acceptance of them. You'd want to tell the board that before scoring starts.

### Step 3: Add intake fields and keep them away from reviewers

- First-time: yes/no, plus a one-line prior-speaking history for verification.
- Employer, with a coordinator-assigned category: end-user / vendor / consultancy / academic / other.
- Don't collect gender or other demographics unless you have a separate, voluntary, consented process. If the event or any speaker is in the EU, GDPR applies.
- Optional: blind speaker names and employers during scoring. This helps first-timers on its own.

### Step 4: Reviewers score quality only

Use 3–4 criteria on a 1–5 scale, for example relevance to the track, depth, originality, and clarity of the proposal. Use at least 3 reviewers per talk. That is about 1,260 reviews, or roughly 60 each with 20 reviewers. Normalize per reviewer to remove harsh and generous graders, and run a calibration round on 10 shared talks first.

### Step 5: Selection, as a separate logged step

1. Rank all talks by normalized score.
2. Define the **eligible band**, for example the top 2.5× slots (about 95 talks), or every talk above a fixed score threshold. Set it in Step 1, before seeing results.
3. Take the top 38 by score.
4. If a quota is short, swap in the **highest-scored qualifying talk** from the band for the **lowest-scored non-qualifying selected talk**. Repeat until the floors are met.
5. If the floors can't be met inside the band, **escalate to the board**. Don't quietly widen the band.
6. Tie-breaks, in order: track balance, then topic duplication, then a coin flip with a recorded seed.
7. Report the cost of the quotas: the score of the lowest accepted talk versus the highest rejected talk.

### Step 6: The decision log (the January fix)

Keep one row per talk touched by anything other than raw rank. This includes every swap, with **both** sides named.

| Field | Example |
|---|---|
| Talk ID, track | T2-147 |
| Raw rank, normalized score | 52, 3.91 |
| Attributes | first-time, end-user |
| Action | Accepted over T1-031 (rank 31, 4.20) |
| Reason code | QUOTA_FIRST_TIME |
| Proposed by, approved by, date | name, name, date |

Reason codes: `QUALITY`, `QUOTA_FIRST_TIME`, `QUOTA_END_USER`, `TRACK_BALANCE`, `TOPIC_DUPLICATE`, `SPEAKER_CAP`, `PANEL_RULE`. The rule is that no talk below a rejected, higher-scored talk gets in without a row naming both. Share the log with the committee and the board at sign-off, and keep it. Anyone can re-run the algorithm and get the same program.

## The two panels

Handle both with a rule, not a one-off judgment.

**Four speakers, one consultancy**
- This isn't a diversity problem. It's a panel-format problem: one employer means one viewpoint.
- Rule for all panels: ≥2 distinct employers and an independent moderator.
- It counts as zero toward the end-user floor, because a consultancy isn't an end user.
- Don't reject it outright. Send it back with a deadline: "Add an end-user practitioner and a second organization, or resubmit as a single talk." Score it after the revision.

**Three men**
- The board gave no gender target, and you'd be introducing a criterion after seeing a submission.
- Two options:
  - Don't gate on it. Treat the panel on its merits.
  - Add a rule for every panel, such as "panels must show viewpoint diversity, and the organizers will work with submitters to broaden". The committee, or the board if it's a policy change, decides this before scoring. It then applies to all panels.
- Whichever you pick, log it with a reason code.

## Decisions to confirm with the board

1. Are the two quotas hard floors, and do they apply to talks or to speakers?
2. Exact definitions of "first-time" and "end-user".
3. Panel counting rule, and whether you adopt the panel composition rule above.
4. The size of the eligible band, and who decides when quotas can't be met inside it.

## Timeline

1. Rules doc drafted and signed off by the board.
2. Intake fields added, and the feasibility count done.
3. Panel eligibility check, with revisions requested.
4. Calibration round.
5. Scoring.
6. Selection run, with the log written as you go.
7. Committee review of the swap list.
8. Sign-off, with the log archived.

I can draft the one-page rules doc or the log spreadsheet template next. Which do you want first?