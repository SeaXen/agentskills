Two issues with the plan collide with rules this same skill file states directly — worth fixing before you write anything.

## 1. "Too hard" isn't a diagnosis yet

Reader feedback saying step 6+ is "too hard" is exactly the shape of input the verification protocol exists to replace. Compare it to the skill's own bad-audit example: *"the signature verification part is complex and could use more explanation"* — a guess from reading, not falsifiable, and it pushes toward explanation, which is the one thing Diátaxis says blocks learning.

"Too hard" could mean four different things, each with a different fix:

| If it's actually... | Fix |
|---|---|
| Defect (code doesn't run as documented past step 6) | Fix the code/output block |
| Hidden prerequisite (something assumed but never taught — e.g. concurrency primitives a rate limiter needs) | Move it to "Before you begin" |
| Concept gap (step 6+ introduces two new ideas at once) | Split the step |
| Friction (ambiguous file/insertion point) | Rewrite the sentence |

Handing over the full file for all three steps "fixes" all four uniformly by deleting the requirement to think — which is the cheapest possible response and the one least likely to be right. Before touching the steps: watch 1-2 mid-level Python devs run steps 6-8 cold, log each stumble as one of the four kinds above. Fifteen minutes of that tells you whether it's one broken step (fix that step) or a genuine ladder problem (fix the ladder) — those are different edits.

## 2. Full solution at 6, 7, 8 is the tutorial's named anti-pattern

Straight from this skill's worked examples, labeled "Negative example - no fading": *"Step 8 written like step 2, a full file to paste. It is faster to write, faster to complete, and teaches nothing: the learner never once produced the pattern."* That's your plan, verbatim.

It also fails the pass threshold's criterion 5 — the learner performing the objective once more, unaided — because by step 8 they've never once produced the pattern themselves. The failure-modes table has a row for exactly this: "Learner still copy-pastes at the last step" → "Fade earlier: switch to diff blocks, then to requirements."

Steps 1-2 as full files is correct (early stage, worked-example effect for novices). Steps 6-8 should be the *least* copy-paste, not the most — they're the late stage where the reader should be producing code, with help available only when stuck.

## 3. Your two hint types are the two worst by value-per-hour

The skill ranks the four rungs by teaching value per authoring hour: **blanked solution > pointer > full solution > pseudocode**. You picked pseudocode and full solution — the bottom two.

- Full solution "is free to paste, and teaches the least."
- Pseudocode "is prose you rewrite on every API change to say what the blanked block already says" — worst ongoing cost, plus it drifts from the real code every time the Kestrelo API changes.

Swap in **blanked solution** (your existing full-solution code, minus 2-3 interesting lines) and a **pointer** (a link to the relevant reference section) instead. Both are cheaper than what you planned:

- Blanked solution costs you nothing extra to author — you're already writing the full solution for the "copy full solution" button; just delete the load-bearing lines.
- Pointer is a link, effectively free.

Escalate in this order when a reader is stuck on step 6/7/8: pointer → blanked solution → full solution, with full solution as the last click, not the headline button. That also stops the per-step full-solution button from duplicating the complete final artifact you already give in "What you built" at the end.

## 4. One more candidate root cause

The tutorial has 8 steps; the Good Docs Project's sourced ceiling is seven primary steps. That the pain starts right at step 6 — near where an 8-step tutorial runs past the recommended max — is worth checking as a structural cause, not just a content one: is step 6+ cramming two concept-ladder rungs (e.g. core concept and robustness) into one step because there wasn't room otherwise? If your cold-run diagnostic shows a concept gap rather than isolated friction, consider splitting at a checkpoint into two shorter tutorials instead of propping up the last three steps with bigger hints.

## Recommended order of operations

1. Run the cold-run diagnostic on steps 6-8 with 2 mid-level Python devs (matches your declared audience) before deciding anything. Log by kind.
2. Fix whatever the diagnostic actually finds per step — they may not all need the same treatment.
3. For whatever residual difficulty remains after fixing real defects/gaps, add graded reveals (pointer → blanked solution → full solution) under 6-8, not a blanket full-file dump.
4. Drop pseudocode unless one specific step is genuinely algorithm-shaped (e.g. token-bucket refill math) where a blanked code block can't carry the idea — author it only there, not across all three steps by default.