Web access was denied, so I couldn't verify anything. I wrote the slide from memory and marked what I'm unsure of. **Two of your four claims don't hold up as written. I'd fix them before the slide goes in front of your manager.**

## Slide

**Title: Task-first docs, tested in CI, cut learning time and failures**

- **Task-first beats comprehensive.** Learners using a "minimal manual" finished in about 40% less time and completed more tasks than learners using a conventional manual. Carroll et al., 1987.
- **Readers fail on docs they can't trust.** [Your own figure from our docs data goes here, e.g. support tickets or failed-quickstart rate.]
- **Docs break like code, so test them like code.** Run the steps in CI. If a step fails, the doc fails (docs-as-tests).
- **Our rule: every how-to ends with a verification step, and has a checkpoint before any irreversible step.** This is our house standard.

**Ask: one sprint to put how-to steps under CI.**

**Sources**
- Carroll, J. M., Smith-Kerr, P. L., Ford, J. R., & Mazur-Rimetz, S. A. (1987). The minimal manual. *Human-Computer Interaction*, 3(2), 123–153.
- Silva, M. *Docs as Tests*. docsastests.com. (A practitioner approach, not a study.)

## Problems with your four claims

1. **"Tripled task completion" is probably overstated.**
   - I recall the 40% less learning time. I don't recall a tripling, and I'd guess the paper reports roughly 2.5× on a performance measure. Check the paper before quoting a multiplier.
   - The subjects were novices learning a word processor. That is a weaker match for developer how-to pages.
   - The minimal manual cut reference material but kept error-recovery information. Your manager can use that against "strip the explanations".
2. **"88% rank clarity top issue (ICSE 2020)" doesn't match what I remember. Don't cite it until you find the source.**
   - The closest paper I know is Aghajani et al., *Software Documentation: The Practitioners' Perspective* (ICSE 2020). Its top problems were incorrect, outdated, and incomplete content, not clarity.
   - I don't recognize the 88% figure. Open the paper and find the table. If the number isn't there, drop it.
   - If the paper's real finding is that docs are outdated or wrong, it supports your CI case better than clarity does. That is a strong reason to fix the claim rather than just drop it.
3. **"Every doc is a test suite" is a slogan, not evidence.** It's fine as an idea, but don't put it next to two studies as if it were a third. I've reworded it as a practice and credited the docs-as-tests community without attributing a quote.
4. **Diátaxis doesn't, as far as I recall, prescribe your verification or checkpoint rule, so I removed the citation.**
   - It says how-tos should be goal-focused, assume competence, and follow a logical sequence. Checking results step by step is closer to its tutorial guidance.
   - Diátaxis says to keep explanation out of how-tos by linking to it, not deleting it.
   - So it supports your page structure but not your rule. Call the rule "our house standard", or reread diataxis.fr and quote the exact line.

## Your decision

How do you want to handle the 88% claim? I can rewrite that bullet around the outdated-docs finding once you have the ICSE 2020 paper open, or keep the placeholder for your own data.

I did not read anything under `skill-wip/`.