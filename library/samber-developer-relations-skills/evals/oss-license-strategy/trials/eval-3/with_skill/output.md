No. CLA and patent grant are two different mechanisms — conflating them is the named failure mode this skill calls out ("Assuming a CLA solves patents").

**Why not**

- Patent grant lives in the **outbound license** — the text governing what the insurer gets when they use quillsort. MIT text is silent on patents. No grant, no denial, just silence.
- CLA governs the **inbound** side — what a contributor grants the project. Even a well-drafted CLA with a patent clause licenses that contributor's patents *to the project*; it does not by itself rewrite the LICENSE file every downstream user reads. The insurer's counsel is checking the artifact they receive (the license), not your contributor paperwork.
- Confirmed patent-grant licenses: Apache-2.0, GPL-3.0, MPL-2.0. Confirmed silent: MIT, BSD. That's from the license text itself, not case law — checkable in minutes.

**What actually answers their question**

Move the outbound license to Apache-2.0 (or dual-license MIT/Apache-2.0). It carries an explicit patent grant plus patent retaliation (a contributor's patent suit against a user kills their own grant). This is the standard, checkable "patent grant in place" answer — the same move FSF recommends once "patents, corporate contributors or a foundation enter the picture."

**The catch: 11 contributors**

Relicensing an existing project needs consent from every copyright holder whose code is still present — hard rule, no shortcut, no CLA retroactively fixes it since none exists yet. Concretely:

1. Check whether each of the 11 contributors' patches are still in the current codebase (some old patches may already be rewritten/removed — check via `git log --follow` per file, or blame).
2. For code still present, ask each contributor for a one-line OK to relicense to Apache-2.0 (GitHub issue comment or email is enough, no legal drafting needed on their side).
3. Old published releases stay MIT forever regardless — that's normal, not a problem, nobody's existing rights change.
4. Anyone unreachable or unwilling: rewrite/remove their specific lines, or accept a mixed-license repo with the per-file boundary written down (Step 7 artifact #2) until that code is naturally replaced.

**Where CLA actually fits — separately**

Justify a CLA only if quillsort needs a right the (now Apache-2.0) license doesn't already grant: dual-licensing plan, a foundation donation, a specific hyperscaler-fork fear. None of those are in what you've described. At 340 stars with drive-by patch contributors, a signature wall costs you PRs at the door for no benefit already covered by the license switch — Fogel's own point, and this skill's own failure pattern ("CLA on a hobby project"). Skip it. If that changes later (real business model shows up), revisit — CLA rung stays available, just not the fix for this specific ask.

**Can't verify for you**

Whether Apache-2.0 alone satisfies *this insurer's specific* internal policy checklist — that's their legal team's call, not something I can assert. Worth asking them directly what their checklist actually requires; some corporate OSS-approval policies check "OSI-approved + patent article present" and stop there, satisfied by Apache-2.0 with zero CLA. Also unconfirmed here: quillsort's own dependency licenses (if any non-stdlib deps exist, check they don't carry copyleft terms that'd block Apache-2.0 as outbound — 5 min check on the lockfile/manifest).

**Next action:** grep the codebase for which of the 11 contributors' patches are still present, then send those people (only those people) a one-line relicense-consent ask.