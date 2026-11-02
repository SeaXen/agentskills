## Claims that didn't match their sources

Four of your claims overreach what the sources support. I changed the slide, not the sources.

| You wrote | What the source supports | On the slide |
| --- | --- | --- |
| "tripled task completion" | Experiment 1 found 2.7× as many subtasks (n=19). Experiment 2 found +58% (n=32). | Direction only on the slide, figures in the footnote. |
| "88% rank clarity as the top docs issue" | In Survey-I (78 respondents), 88% rated clarity as important. That is a perceived-importance rating, not a ranking, and not a measured outcome. | "Rated important". |
| The minimal manual supports stripping how-to explanations | It tested a novice training manual for a word processor. It supports brevity and action-first writing, not a how-to-specific rule. | Framed as "task-first". |
| Diátaxis for the verification and checkpoint rule | Diátaxis doesn't say this. The ordering of verification before the irreversible step, and the warning before a destructive step, come from Cloudflare's how-to standard. Closing every page on a verification step and a separate checkpoint before the point of no return is our own rule. | Cloudflare cited for the order, ours labelled as ours. Diátaxis cited for "user at work". |

The 1987 study's authors report "40% less learning time". That is the study's direction, so I kept it in the footnote with its sample size.

The eng manager can also attack the framing of "stripping explanations". Diátaxis moves explanation to its own pages and links to it, so the slide says "move", not "strip".

## Slide

**Task-first how-tos, tested like code**

- **Readers at work need the task, not the lecture.** Diátaxis: a tutorial serves the user "at study", a how-to guide serves the user "at work". Explanations move to linked pages and stay available.¹
- **Short, task-first material beat the full manual.** A task-oriented manual under a quarter the length cut novices' learning time and raised the subtasks they completed.²
- **Clarity and correct code are what practitioners say they need.** 88% of surveyed practitioners rated clarity important, and 59% rated erroneous code examples important.³
- **Docs that nobody runs go stale.** "Each doc is a test suite, each procedure a test case, each step an assertion", run against the product.⁴

**Our rule:** every how-to carries a checkpoint before any irreversible step and closes on a verification step. CI runs the steps against the released product.⁵

**Ask:** one sprint to wire how-to steps into docs CI.

### Footnotes

1. Diátaxis, diataxis.fr. The "at study / at work" line comes from its distinction between tutorials and how-to guides.
2. Carroll, Smith-Kerker, Ford & Mazur-Rimetz, "The Minimal Manual", *Human-Computer Interaction*, 1987. Novices learned a word processor. Experiment 1 (n=19): about 40% less learning time and 2.7× the subtasks completed. Experiment 2 (n=32): 58% more subtasks. These are small lab studies, so cite the direction and not the magnitude.
3. Aghajani et al., practitioner surveys, ICSE 2020. Survey-I had 78 respondents (146 across both surveys). The figures are perceived importance, not measured outcomes.
4. Manny Silva, docsastests.com. This is an advocacy position, not evidence.
5. Verification before the irreversible closing step, and a warning before a destructive step: Cloudflare how-to standard. Testing instructions start to finish and re-testing after every notable release: Good Docs Project. Closing every page on a verification step and a separate checkpoint: our team's rule.

I took the Carroll volume details and the Aghajani title from memory, and the skill's own list doesn't include them. Check the Carroll volume and page numbers (I believe 3(2), 123–153) and the Aghajani title before you print them.

## What this slide doesn't prove

- **The CI sprint rests on bullets 3 and 4 only.** The 1987 study says nothing about CI. The 59% figure on erroneous code examples is your best support for it, and it is a stated importance, not a measured one.
- **The skill's estimate for wiring is lower than a sprint.** It puts executable steps in CI at half a day to set up and near-zero after. That is an estimate, not a measurement. If you already have a docs-test job, the real cost may be lower still. Check this before the manager does.
- **I don't know your ask.** "One sprint" comes from your message. Add scope if you have it, for example how many how-tos CI would cover.