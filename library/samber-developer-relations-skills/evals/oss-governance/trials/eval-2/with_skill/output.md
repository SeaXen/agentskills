## Governance review — Halyard: is the "bus factor 4" claim right?

**No.** Recomputed properly per this skill's method (contributor absence factor — the CHAOSS metric formerly called bus factor: smallest number of contributors responsible for 50% of contributions, 12-month window), the number is **3, not 4** — and that's the flattering version. The credential and per-area picture underneath it is worse than any single headcount number can show.

### Step 1 — Recompute with required hygiene

Measurement hygiene (succession-playbook.md) says: exclude bot/automated authors, exclude merge commits or "the person who integrates looks like the person who writes." Both apply here.

1. **Drop `renovate[bot]` (1240).** It's an automated dependency bot, not a contributor. Raw total 3650 → 2410.
2. **Back out Priya's merge-queue commits.** She runs the merge queue, and 610 of her 980 commits are merges, not authorship. Her real authored count is 980 − 610 = **370**. Total after both corrections: 2410 − 610 = **1800**. Half = 900.
3. **Accumulate descending on the corrected numbers:**

| Rank | Contributor | Corrected commits | Cumulative |
|---|---|---|---|
| 1 | Tomas | 430 | 430 |
| 2 | Priya | 370 | 800 |
| 3 | Ines | 350 | **1150** ← crosses 900 |
| 4 | Karl | 310 | — |
| 5 | Wen | 190 | — |
| 6–9 | (four others) | 60/40/30/20 | — |

**Contributor absence factor = 3** (Tomas + Priya + Ines), not 4. If you skip the merge-commit correction and just drop the bot, it's even lower — Priya (980) + Tomas (430) alone cross the 1205 threshold on a 2410 total, giving **2**. Either way the honest number is *below* 4, meaning the board's slide overstates resilience, not understates it. There's no reasonable hygiene pass on this data that produces 4 — the most likely explanation is the deck counted "Priya, Tomas, Ines, Karl" as "four real maintainers" by eyeballing who's above the small tail, which is a headcount impression, not the accumulate-to-50% metric it's being presented as.

### Why the commit number isn't even the binding constraint here

Per the succession playbook: "Code access is rarely the binding constraint — the credentials are," and compute concentration **per governed area as well as project-wide**, because a project-level factor "routinely hides a subsystem owned by exactly one person, and that subsystem is what actually breaks on a departure." Two things in your own description already fail worse than the commit math:

- **Windows backend: absence factor of 1.** Karl is the only person who has touched it in two years. The project-wide "3" is invisible cover for this — if Karl leaves, that subsystem stops getting maintained the same day, regardless of what the other four people are doing elsewhere.
- **Release credentials: one holder, should be two.** Priya alone holds the npm token and the release signing key. The self-set baseline this skill uses (published-findings.md) is explicit: "Contributor absence factor of at least 2, **and at least two holders of every privileged credential** — the smallest value at which no single departure stops releases." You have one holder of both rows. Per the health check in the main skill, this credential check is called out as **"the one threshold worth blocking on"** — more load-bearing than the commit-based number, because a signed release is downstream of that key before anyone notices it's gone.

Also worth naming: Priya running the merge queue and holding the sole publish/signing credentials makes her a chokepoint independent of her raw commit rank. Even though Tomas now edges her out on real authored volume (430 vs 370), nobody but Priya can currently cut and sign a release at all — that's a harder single point of failure than any contributor-count metric captures.

### Bottom line for the board

State it as three separate numbers, not one:

- **Project-wide contributor absence factor: 3** (corrected for the bot and the merge queue) — below what the deck claims, though it clears the ≥2 baseline on its own.
- **Windows-backend absence factor: 1** (Karl) — fails the baseline outright, and it's exactly the kind of subsystem-level concentration a project-wide number hides.
- **Privileged-credential holders (npm token, signing key): 1** (Priya), against a target of 2 — this is the one that actually stops releases on a single departure, and it's the one the "bus factor is 4" framing doesn't measure at all.

### What step 7 says to do next, in order

1. **Don't promote anyone as a reaction to this finding.** "Promoting to fix a concentration number" is a listed failure mode — handing out keys under pressure is exactly the pattern the 2024 xz-utils takeover exploited.
2. **Windows backend first, since it's the more acute single point of failure (factor of 1 vs. a credential row that's inconvenient but not yet broken):** get a second person reviewing Karl's PRs now, on the staged trust ladder (reviewer → maintainer over months of evidence), not a same-day merge grant.
3. **Second key holder for npm + signing, on the staged trust ladder's own rule: never granted in the same act as merge rights, only after a supervised release cycle.** Tomas or Ines are the natural candidates by corrected commit share — but the grant should follow the evidence-over-months path, not be triggered by this audit alone.
4. **Re-quote the board number as three lines, not one**, and mark the credential row as the one to actually track quarter over quarter — it's the number that determines whether the project can ship the week someone leaves, which is what "bus factor" is meant to answer in the first place.