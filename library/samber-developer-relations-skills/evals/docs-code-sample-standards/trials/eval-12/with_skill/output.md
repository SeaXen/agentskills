## Sample audit: Marlowe Freight docs tree, 2026-10-30

**Status: no census run.** You gave no docs path, and I found no Marlowe docs tree in this checkout. So this report has no counts, no findings and no scores. I won't invent numbers for a corpus I haven't seen. What follows is the audit design for your constraints, ready to run the moment you point it at the tree.

### 1. Inputs I need (they change the tier ranking)

1. Docs path, and which surfaces are in scope (docs site, API reference, README, examples repo).
2. **Q4/Q8:** Does any CI exist outside this air-gapped box? Are there engineering hours to build a harness?
3. **Q9:** When does this need to show a result?
4. **Q10:** One-off cleanup, or a standard enforced every release?
5. Who owns a broken sample today?
6. Which language do readers arrive with most? That decides tier 1.

### 2. Method

- **Inventory before audit** (Nielsen Norman Group): mechanical census on 100% of samples, then judgement on a stratified sample.
- **ROT triage** (redundant, outdated, trivial) as the first cut.
- **Docs as Tests** (Manny Silva) for the verification design.
- **Google Cloud's ranked principles** break rule conflicts: clarity → idiomaticity → consistency → simplicity → portability → maintainability.

### 3. Environment constraints applied

Only Python runs here, and the corpus is Python, Java, Ruby and Go.

| Language | What this box can verify | Status to report |
| --- | --- | --- |
| Python | Syntax check (`python3 -I -m py_compile`), then execution in a clean venv with stdlib only | Compile-only. Run only if the sample has no third-party imports. |
| Java, Ruby, Go | Nothing. No compiler or interpreter. | **Unverified**, never "passing". |
| All | Mechanical lint via `sample-audit.py` (pure stdlib, works offline) | Census complete. |

- Samples needing a package registry can't be installed here. That is a limit of the box, not a finding against the sample.
- The skill says to produce the tier assignments, the lint results and a written verification plan when execution is impossible. It also says to label unexecuted samples *unverified*.
- **Tier deletion:** until a pipeline exists outside this box, Run and Compile-only are unavailable for Java, Ruby and Go. Every sample in those languages is *unverified*. Standing up a CI job per language, on the published artefact, is queue item 1 for them.
- Samples that bill, destroy or call a third party never get Run, whatever CI can do.

### 4. Fixing the 63-P0 noise problem

**Cause:** the scanner treats a flag as a verdict. The skill says to treat every flag as a candidate to confirm, because a rotation page legitimately contains a key-shaped string. Last quarter's report skipped that step. Two pages were not cut out from 63 findings, and every P0 got ignored.

**Rules for this audit:**

1. **Scan everything, report by triage class.** Don't exclude the two pages. A blanket path exclusion would hide a real leak on them.
2. **P0 means harm to the reader who copies it.** A flag reaches P0 only if it passes one of these tests:
   - The string is not on the known-fake list and could be real: a live-format prefix (`sk_live_`, `AKIA…`, `ghp_…`, `xox…`) with plausible entropy, or a private-key header with a real body.
   - An insecure switch sits in a block presented as the recommended path.
3. **Expected findings go to a separate bucket, "declared intentional", not P0.** A flagged sample lands there only if all three hold:
   - It is tier Illustrative, with a visible label on the rendered page.
   - Its key-shaped strings are demonstrably fake: angle-bracket placeholders, vendor documentation sentinels such as `AKIAIOSFODNN7EXAMPLE`, or a repeated filler pattern.
   - An insecure example is introduced as an anti-pattern, with the secure form shown next to it.
4. **Anything declared intentional but unlabelled is a P2.** An unlabelled illustrative sample looks broken.
5. **Group by root cause, not by sample.** If one pattern recurs 40 times, that is one fix-queue item with 40 locations.
6. **Report P0 the moment it is seen.** The credential check lists only P0s that survived triage.
7. **Real-key check:** I can't confirm from here that a key-shaped string is dead. For any survivor of rule 2, the owner rotates it, or confirms from the issuing system that it never existed. That confirmation belongs in the finding.
8. **Standing fix:** add a per-sample marker in the fence info string (for example `tier=illustrative`) plus a reviewed allowlist file naming path, line and reason. A new unlisted hit then stands out. `sample-audit.py` reads only `tier=` today, so the allowlist needs a small wrapper. Changing the scanner itself is your decision.

### 5. Commands to run

```
python3 -I scripts/sample-audit.py <docs-dir> --format summary
python3 -I scripts/sample-audit.py <docs-dir> --format json --ext .md,.mdx > inventory.json
python3 -I scripts/sample-audit.py <docs-dir> --format tsv > census.tsv
```

Then, for Python blocks only:

1. Extract them to a scratch directory.
2. Run `python3 -I -m py_compile` on each.
3. Record pass or fail per `path:line`.

### 6. Stratified rubric pass

- **Size:** state a number you can actually score, for example 40 samples. Quote results as estimates with that base, not as corpus-wide counts.
- **Strata:** language × product area × age. Over-weight the language added last, and include old pages.
- **Dimensions** (0–2 each): correctness, runnability, idiomaticity, error handling, credential handling, copy-paste safety. Record each dimension, not a total.
- **Judgement checks** a regex can't make:
  - Does each symbol still exist in the current API?
  - Is the documented output current?
  - Do the sibling-language samples do the same thing?

### 7. Pass thresholds to report against

- **Measured comparator:** deprecated-API rate below 43%. That figure is Zhou & Walker, FSE 2016, measured on Stack Overflow posts. Using it as a gate is this skill's choice.
- **Skill baselines, not industry standards:**
  - Zero P0 after triage, and 100% of adoption-path samples at tier Run and green.
  - Pass rate ≥90%.
  - ≥80% of the corpus at tier Run or Compile-only and executed by CI.
  - Parity ≥90% across tier-1 languages.
- **Today's expected result:** the ≥80% tested-share gate fails by construction for Java, Ruby and Go, because nothing can run them here. If the team can't meet it, cut samples instead of lowering the bar.

### 8. Fix queue shape

1. **Surviving P0s** (credentials that pass triage, insecure defaults presented as advice): owner, this week. Harm outranks the ratio.
2. **Build CI outside this box**, one job per language, installing the published artefact. This is the first item for Java, Ruby and Go.
3. **Mark the rotation and hardening samples** Illustrative with visible labels, plus the allowlist (rule 8). One fix covers all 63 prior hits.
4. **Adoption-path samples** (quickstart, auth, first call): promote to Run by hand.
5. **P1** (does not work as written), then **P2** (policy violations, parity gaps).

Items 4 and 5 are ordered by (readers affected × severity) ÷ effort, a ratio rather than a severity list. The ratio starves low-traffic samples that need a harness built to fix them, so promote those by hand when they sit on the adoption path.

### 9. Ownership

When a sample goes red in CI on a Friday afternoon, whose queue does it land in? I can't answer that without question 5. Encode the answer as code-owner rules on sample paths plus a blocking check, not a wiki paragraph. Bug and security fixes take priority over new samples.

### 10. Next step

Send me the docs path and answers to questions 2–4. I'll then run the census, triage the P0 pile into real versus declared-intentional, and return the filled report with counts.