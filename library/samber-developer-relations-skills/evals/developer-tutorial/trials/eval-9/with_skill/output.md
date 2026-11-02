# Ardenmoor Documentation Style Guide — Tutorials

Numbered standards for anyone authoring or reviewing a tutorial. Each rule states its source in the citation line. Three of these are baselines Ardenmoor is choosing to adopt, not published industry rules — marked ℹ️. One has no citable source at all — marked ⚠️, with a recommendation instead of a citation.

1. **A tutorial runs 15–60 minutes end to end.** Under 15 minutes, write it as a quickstart instead; over 60, split it into an ordered pair at a checkpoint.
   - Source: The Good Docs Project, tutorial template guide — "Ideally, your tutorial should take 15 to 60 minutes to complete."

2. **A tutorial has at most seven primary steps.** A ladder that needs more rungs is two tutorials, not one long one.
   - Source: The Good Docs Project, same guide — "Avoid writing procedures that are more than seven primary steps long."

3. **A primary step has at most four substeps.** A step needing a fifth substep has crossed into a second concept; split it.
   - Source: The Good Docs Project, same guide — "Aim for no more than four substeps in any primary step."

4. **ℹ️ Place a checkpoint every 3–5 steps.** Each checkpoint is a command, its exact output, and a way back (a branch, tag, or reset command) — never a bare "it should work now."
   - Source: Ardenmoor internal standard, not an industry figure. No organization publishes "every 3–5 steps" at this granularity. For comparison: Diátaxis argues for a checkpoint at *every* step; Google Codelabs caps total codelab length (5–10 steps) rather than checkpoint interval; freeCodeCamp's two-minute rule checkpoints nearly every step. Ardenmoor's spacing is chosen because it divides the seven-step ceiling (Standard 2) evenly — cite it internally, not to outside teams as a published bar.

5. **Fade worked examples across three stages: full code, then a diff with the insertion point named, then a requirement plus expected output.** Never ship a tutorial that copy-pastes as much at the last step as at the first.
   - Source: the underlying effect — competence-appropriate scaffolding removal — is Renkl & Atkinson's guidance-fading research in cognitive load theory. The three-stage shape (full/diff/requirement) is an Ardenmoor convention, not their documented design: their own experiments fade continuously (one blank added at a time) rather than in three fixed stages. Cite the effect as sourced; cite the three-stage split as Ardenmoor's own, chosen for authorability.

6. **⚠️ No industry-sourced completion-rate floor exists — do not cite one.** There is no published, tutorial-specific completion benchmark anywhere in the literature reviewed for this standard (Diátaxis, the Good Docs Project, Kirkpatrick). Figures like "55%" circulating in developer-marketing material are self-reported vendor numbers about signup funnels, not tutorials, and don't transfer.
   - Recommendation: if Ardenmoor wants a 55% floor, adopt it explicitly as *Ardenmoor's own target*, and measure every subsequent tutorial against its own prior version — not against an external bar. Attributing 55% to an outside source will not survive a review challenge, because no such source exists.

7. **ℹ️ Run each checkpoint's companion branch in CI weekly, in addition to on every commit.** Fail the docs build on a broken checkpoint; an advisory-only job gets muted within a month.
   - Source: Ardenmoor internal standard. The practice of running companion-repo checkpoints in CI is general good practice for docs that carry runnable code; the specific weekly cadence is not published by any named framework — it's chosen to catch product drift between releases, independent of docs edits. Match the cadence to Ardenmoor's actual release train rather than defending "weekly" as a fixed rule.

---

**For reviewers:** Standards 1–3 are direct quotes from a named external template and can be defended as such without further discussion. Standards 4, 5, and 7 are Ardenmoor decisions informed by named research or practice, and should be presented in review as *our* convention, with the rationale above, not as an outside mandate. Standard 6 needs a decision from whoever owns this guide before it ships with a number attached — as written it has no defensible citation, and shipping it silently invites exactly the re-litigation this document is meant to prevent.