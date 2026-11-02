**Fix: kill sequential group debrief. Force silent scores first, calibrate after.**

Root cause of Brightwell mess: two named failures.

1. Hiring manager spoke first → anchored two people, flipped their read.
2. Group format → nobody wants sole "no" → holdout pressure kills honest signal.

This is not DevRel-specific. General finding: structured, independently-scored, mechanically-combined interviews beat holistic group debriefs. Debrief job = calibrate interpretation of scores already submitted. Never originate a score live in the room.

## New protocol

1. **Before debrief:** each of 4 interviewers submits scores async — form or doc, not verbal. Deadline: end of interview day, before anyone talks to anyone else.
2. **Score format per competency** (from scorecard, pre-set weights):
   - Numeric score (1-5)
   - One evidence note ("said X when asked Y") — no evidence note, score does not count.
3. **Nobody sees others' scores until all 4 submitted.** Blocks anchoring by default — no first-speaker effect possible.
4. **Compute weighted total mechanically** before the meeting even starts. This is the draft decision, not final — debrief can override only with new evidence, never gut feel.
5. **Debrief agenda, 30 min, time-boxed:**
   - Show all 4 scorecards side by side, anonymized order (not by seniority) or reverse-seniority speaks first — never hiring manager first.
   - Discuss only competencies with >1.5 point spread between interviewers. Skip competencies everyone agreed on — no re-litigating.
   - Each disagreement: interviewer with lower/higher score states evidence, 2 min cap, no persuasion speech.
   - Hiring manager speaks last, on disagreements only, evidence-based — never opens the meeting.
6. **Decision = the weighted mechanical total**, adjusted only if the debrief surfaces a factual correction (wrong evidence note, missed answer) — not "I feel differently after discussion."

## Why this stops both failures

- Anchoring: impossible once scores are locked before anyone speaks.
- Holdout pressure: nobody defends a live position in front of the room — they defend a score already on paper, submitted before group dynamics existed.

## Quality check before running it live

- [ ] Every interviewer scored independently, evidence note attached, before debrief — no exceptions for "just chat first."
- [ ] Scorecard weights set before the loop starts, not decided in the debrief.
- [ ] Hiring manager never speaks first in debrief.
- [ ] Final call traceable to the mechanical weighted score, not a room vote.

Next: pick your next DevRel debrief and run the async-scoring form before the room meets — 15 min to set up, catches the same failure before it repeats.