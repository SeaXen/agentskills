Diataxis drifting back in 18 months with no writer and no docs CI isn't a discipline failure — it's what happens when a structure depends on everyone remembering a taxonomy instead of something enforcing it. The reorg fixed the symptom (bad placement) but not the cause (nothing stops bad placement from recurring). Do these five things differently.

## 1. Make placement machine-checkable, not memory-checkable

Add a doc lint step to CI (a five-minute script, not a docs platform):

- **Require frontmatter** declaring the Diataxis quadrant (`type: tutorial|how-to|reference|explanation`) on every page.
- **Enforce folder-matches-type**: fail CI if `type: how-to` lives outside `/how-to/`. This alone kills "procedures filed under concepts" — the four reference pages under tutorials would never have merged.
- **Flag near-duplicates**: a simple title/heading similarity check (even TF-IDF cosine on headings) catches a second routing-profiles doc at PR time, before it ships, not 18 months later.
- **Flag staleness**: if code in a directory changes and no doc under the matching path changed in the same PR window, surface it as a warning. Doesn't need to be smart — visibility is the point.

This is the actual gap versus round one: you had a taxonomy, not a gate. A taxonomy without a gate degrades at the rate of your least-careful commit.

## 2. Put the decision rule in the contributing guide, not in people's heads

The concepts/how-to boundary is the one CI can't fully judge — that's a judgment call, and it's also exactly where you drifted. Give it a one-line test next to the folder names, not an essay:

- Tells you what to type, in order, to get a result → **how-to**.
- Explains why the system behaves this way → **explanation**.
- Teaches a beginner by doing → **tutorial**.
- Describes the thing (API, config, field) → **reference**.

Six engineers won't re-read the Diataxis site each time. They will read four lines next to the folder they're about to commit into, if it's on the page they're already looking at.

## 3. Assign a rotating steward, not a writer you don't have budget for

You don't need a technical writer to stop entropy — you need one accountable person at a time. Rotate a "docs steward" monthly among the six engineers:

- 30 minutes: run the lint output, merge/redirect any flagged duplicates, spot-check quadrant placement on anything touched that month.
- Rotation prevents "everyone's job = nobody's job," which is what actually killed the first reorg — big-bang cleanup, then diffuse ownership, then nobody's specifically on the hook when a PR misfiles something.

## 4. Fix the two named symptoms now, with a trap for the next one

- Merge the two routing-profiles docs into one canonical page. Leave a stub/redirect at the deleted location — people duplicate because they find the wrong page before the right one, not out of carelessness. A dead link that redirects prevents the next fork.
- Move the four reference pages out of tutorials this pass, but also add them to the near-duplicate/misplacement lint so a fifth one can't land the same way silently.

## 5. Schedule the audit you didn't schedule last time

18 months of silent drift means nobody looked until it was bad enough to notice unprompted. Put a lightweight structural audit on the calendar — quarterly, 30 minutes, same steward role — independent of the CI gate, because CI catches mechanical drift (wrong folder, duplicate title) but not slow semantic drift (a how-to that's grown three paragraphs of rationale and quietly become half-explanation). A human pass every quarter catches that before it's an 18-month backlog again.

**The core difference from last time:** the 2025 effort was a sort. This one needs to be a sort plus a gate, because six unsupervised engineers writing docs as a side effect of shipping code will always regress toward whatever's easiest to reach for at commit time — and "easiest" was never going to be Diataxis unless something made the wrong choice visibly wrong before merge.