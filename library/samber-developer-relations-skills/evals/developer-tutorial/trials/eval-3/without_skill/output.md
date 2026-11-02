Quick take: the fix might be treating a symptom. Before adding a "copy full solution" button, check whether "too hard" means *insufficient hints* or *too big a concept jump* — those need different fixes.

**Two things to reconsider:**

- **Full-file dump at steps 1-2 vs. 6-8 aren't the same move.** Steps 1-2 are almost certainly boilerplate/setup — low learning value, so giving the whole file costs nothing pedagogically. Steps 6-8 are presumably where the actual rate-limiter logic lives (the part worth teaching). Dumping the complete file there removes the struggle at exactly the point it's supposed to happen. Precedent from steps 1-2 doesn't transfer.

- **Pseudocode → full solution is a two-rung ladder with a big gap in the middle.** A reader who doesn't parse the pseudocode has nowhere to go but "click solution, copy-paste" — which becomes the path of least resistance at your hardest steps, not a safety net for it. Copy-paste rate on steps 6-8 will likely spike and *look* like the fix worked (feedback stops) while nobody actually learns the hard part.

**Cheap way to close the gap without a third full hint tier:** add a one-sentence conceptual nudge above the pseudocode — "you need a sliding window / token bucket here, because X" — not code, just naming the concept. Costs a sentence, not authoring time, and stops readers from either flailing or jumping straight to copy-paste.

**Also worth doing before writing any hints:** reread the step-5→6 transition. "Too hard starting at step 6" often means two new concepts got introduced in one step with no checkpoint in between (see progressive-complexity / checkpoint-every-3-5-steps pattern) — that's a step-splitting fix, not a hints-authoring fix, and it's free relative to writing new content per step.

**If you ship the button anyway:** gate it behind progressive disclosure (reveal pseudocode first, second click reveals solution) instead of a flat sibling button next to pseudocode — keeps the default action the least-revealing one. And instrument clicks per step once live; that's the only way to tell if 6-8 actually needed the rescue or if one step was the real bottleneck.