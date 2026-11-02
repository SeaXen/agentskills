**Verdict: mixed. 2 of 4 changes back desirable-difficulty research. 2 sabotage it.**

Desirable difficulty (Bjork) only raises retention when three things hold: learner has enough schema to attempt task, feedback loop exists to correct wrong guesses, difficulty sits in the target skill (germane load) not around it (extraneous load). Bootcamp grads have thinner schema and lower self-efficacy than senior devs — expertise-reversal effect (Kalyuga) means minimal-guidance moves that help experts actively hurt novices. Score each change against those 3 conditions:

**1. Remove expected-output blocks — hurts as written.**
Prediction-before-checking is real retrieval practice. But deleting the output block deletes the feedback half of the loop. Learner predicts wrong, nothing corrects it, wrong model ships silently. Fix: keep output, collapse it (`<details>`/spoiler). Ask one concrete predict question first ("what does this log, and why?"), then reveal.

**2. Off-by-one bug in step 3 — sound idea, unsafe as written.**
Debugging faulty examples has real research backing (erroneous-worked-examples effect). Risk: a silent bug reads as "tutorial is broken," not "intentional," and bootcamp grads default to blaming themselves or abandoning, not debugging. Fix: label it — "🐛 something's off here, tests will fail with X, find it before moving on." Give a visible symptom, a hint after a few minutes stuck, fix in a collapsed reveal. Place it only after they've learned to read the relevant error output — not before.

**3. Unpin Node version — hurts, not desirable difficulty at all.**
This is pure extraneous load (Sweller). Env/toolchain trouble has zero relation to job-queue concepts, and its difficulty is random — depends on OS, existing installs, nvm state — not on anything the tutorial teaches. It's also the tutorial skill's own checklist item ("Verify Installation," exact version + check command) for a reason: unrelated setup failures are the #1 way learners drop off before reaching real content, and a learner who quits retains nothing. Fix: keep the pin. If environment-reasoning is a skill you want to teach, make it its own scoped exercise, not ambient noise in a queue tutorial.

**4. Vague goal in step 5 — workable, only with a feedback path.**
Interpreting an ambiguous requirement is a real transfer skill, legit to practice late in a tutorial once schema is built. But bare vagueness with no way to self-check leaves bootcamp grads unsure they even succeeded — that uncertainty compounds with a population that already under-trusts itself. Fix: give explicit acceptance criteria (what must be true) instead of a spec, then reveal one valid solution + rationale afterward so they can compare.

**Net effect if shipped as-is:** #1 and #3 raise drop-off without raising learning — worst possible retention outcome, since a quitter retains zero. #2 and #4 can genuinely help, only with the reveal/signpost scaffolding added.

**Also:** "will this raise retention" is a testable claim, not an assumption to ship on. Check with a delayed task (have them extend the queue a week later) or a completion-rate delta, before and after — otherwise this stays a guess.

Next: rewrite step 3's bug as a labeled challenge with visible symptom + hint, and re-pin the Node version — those two edits alone fix the changes most likely to tank completion.