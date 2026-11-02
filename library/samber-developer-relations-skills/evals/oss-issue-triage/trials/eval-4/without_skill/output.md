## Reframe the target before building anything

You asked for an "AI-generation" classifier, but that's the wrong prediction target. You have no ground-truth labels for "was this written by an LLM" — you have ground truth for "was this report valid," which is what you actually care about. Three reasons not to build a pure AI-text detector as your gate:

1. **AI-text detectors are unreliable on adversarial input.** Published detectors run 5–20% false-positive rate on human-written text, and any spammer who gets auto-rejected once will just ask their LLM to "rewrite this to sound more human" — a one-line prompt defeats most stylistic detectors.
2. **Legitimate researchers increasingly use LLMs to write up real findings** — non-native English speakers especially. A gate on "AI-ness" disproportionately rejects genuine reports from that group, which is a fairness and reputational problem, not just an accuracy one.
3. **It doesn't target the actual failure mode.** The reports draining your 90 minutes aren't costly because they're AI-written — they're costly because they're *unreproducible or fabricated* (invented function names, PoCs that don't actually crash anything). That's a mechanically checkable fact, not a stylistic one, and it's far cheaper and more reliable to check directly.

## Recommended architecture: deterministic gate first, ML second, human sampling always

1. **Submission friction (no ML).** Require a mandatory structured field: exact `tinderbox` commit/tag, build command, and a concrete input file that triggers the bug, plus the actual crash output. Most templated LLM-slop reports either skip this or fill it with plausible-looking nonsense — this alone kills a large share of junk before anyone reads prose.
2. **Deterministic reproducibility gate (highest ROI, build this first).** Automate: pull the stated commit, build with ASAN/UBSAN, feed the submitted input, check for an actual crash/sanitizer report. Separately, grep the stated repo for every file/function/line the report cites — hallucinated citations are a strong tell. This runs in seconds, costs zero reviewer time, and targets ground truth directly instead of a proxy.
3. **ML triage score, trained on valid/invalid labels — used to prioritize, not to hard-auto-reject.** Only the reports that already pass step 2 reach this stage, so the pool is smaller and less imbalanced.
4. **Human spot-check on anything auto-filtered.** Never let steps 1–3 fully remove human eyes from 100% of rejections — sample a fixed percentage (see below) for a 5-minute skim.

## How to train the step-3 model

- **Label:** accepted/valid vs rejected, pulled from your own historical triage decisions — not "AI-generated," which you can't reliably label anyway.
- **Features**, mixed structured + text, not just raw text:
  - Did it pass the step-2 reproducibility gate (binary — this alone will dominate the model).
  - Fraction of cited file/function/line references that resolve in the actual codebase.
  - Presence of a working diff/patch vs. prose-only "suggested fix."
  - Submitter history: prior accepted reports, account age, prior rejected-report count.
  - Boilerplate/template similarity to your corpus of known-junk reports (embedding similarity, cheap and effective — LLM slop reports cluster tightly).
  - Generic CWE/impact language mismatched to the actual code path (e.g., claims "remote code execution" in a library with no network-facing entry point).
- **Model:** gradient-boosted trees (LightGBM/XGBoost) on the engineered features above, or logistic regression if your labeled volume is small (you likely have well under a few hundred positive examples/year). Skip fine-tuning an LLM — you don't have the data volume to justify it, and it adds an opaque, harder-to-audit decision layer to a process that may face legal/PR scrutiny.
- **Validation:** stratified k-fold given the ~1:15 imbalance. Report precision-recall, not ROC-AUC — ROC looks good on imbalanced data even when the model is mediocre. Optimize for **recall on the valid class**, not accuracy.

## Threshold: don't auto-reject on a blind accuracy-optimal cutoff

Do the base-rate math before picking a number. At a 1:15 real:junk ratio, even a good classifier misfires expensively:

- 1,000 reports → ~67 real, ~933 junk.
- A detector with 90% recall on junk and a 5% false-positive rate on real reports (optimistic, for either an AI-detector or your trained model) still auto-rejects **~3–4 genuine vulnerability reports per 1,000 submissions with zero human review** — in a memory-unsafe C image parser, exactly the bug class that becomes a CVE.

Concrete recommendation:

1. **Run the model in shadow mode for 3–6 months first.** Score every incoming report, log the score, keep triaging manually. Then backtest: what recall would each threshold have given on your actual historical valid reports?
2. **Pick the threshold that gives ~99%+ recall on known-valid reports in backtesting**, not the threshold that maximizes overall accuracy or junk-reduction. Expect this to only filter 30–60% of junk, not 90%+ — that's the correct trade, because a missed real memory-corruption bug is far more expensive than an extra hour of triage.
3. **Never route auto-rejected reports to a silent bin.** Auto-file them as "low-priority" and have one reviewer spot-check a fixed sample (e.g., 15–20%) weekly, both to catch missed valids and to detect model drift as spam tactics evolve.
4. **Don't publish the mechanics.** Stating "we auto-reject AI-generated reports below score X" on your bounty page hands spammers a target to tune against. Keep the gate internal; publish only the reproducibility requirement from step 1, which is legitimate and doesn't leak your detection logic.

## Expected effect on your actual bottleneck

Your 90-minutes-per-junk-report cost comes from two humans reading prose and trying to reproduce a claim. Step 2 (deterministic ASAN/fact gate) removes that reproduction work entirely for anything that doesn't produce a real crash or cites nonexistent code — for an image-parsing C library, this is likely the majority of your LLM-slop volume, and it costs you compute seconds, not reviewer time. Build and ship that gate first; only invest in the ML scoring layer once you've measured how much volume step 2 leaves behind.