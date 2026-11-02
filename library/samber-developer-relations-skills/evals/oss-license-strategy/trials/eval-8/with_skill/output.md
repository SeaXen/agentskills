## Sablewright: setting up dual licensing on top of AGPL-3.0

**⚠️ Correct the premise first.** Engineering is right that AGPL-plus-commercial-license is a well-worn model (MySQL, MongoDB, Sleepycat, Ghost — all did this). They're wrong that you already have it. Dual licensing only works when the vendor **holds or has been granted all the rights** to relicense the code under different terms. A DCO doesn't grant that. It's Karl Fogel's rung 2 — a contributor's `Signed-off-by` trailer only certifies "I wrote this, or have the right to submit it under the project's existing license" (AGPL). It gives you no right to also offer that same code under a proprietary commercial license. That right isn't implied, it's a separate grant, and today nobody has given it to you.

Concretely: of your 22 outside contributors, none of them ever agreed you could sell their code under different terms than AGPL. Right now, if a bank's legal team does the diligence that comes with a commercial software purchase — and banks' legal teams do this — they will ask for your chain of title. You cannot currently produce one. That's not a compliance nicety to clean up eventually; it's the thing that kills or delays the Q1 deals your CEO already promised the board.

### What's actually missing

1. **The right to dual-license 22 people's code.** DCO ≠ CLA. You need a CLA (or an equivalent retroactive grant) to do what you're planning.
2. **A commercial license document** that is legally distinct from AGPL and actually says what banks are buying.
3. **A process to close the gap on already-merged code**, separate from fixing it going forward — these are two different jobs with two different timelines.

### The two-track plan

**Track 1 — Future contributions: replace DCO with a CLA**

- Adopt an Individual CLA (ICLA) plus a Corporate CLA (CCLA) — don't draft one from scratch; adapt a proven template (Apache Software Foundation's ICLA/CCLA, or the Linux Foundation's EasyCLA text). Using a known, litigated template is what keeps this out of a multi-week bespoke legal review.
- Don't stack CLA on top of DCO. Mixing rungs doubles friction for no added right — the CLA already gives you everything the DCO did (provenance) plus what you actually need (relicensing rights). Retire the DCO bot once the CLA is in place; keep the DCO's historical commits as-is, they don't need to be re-signed.
- Enforce with an automated gate on every PR (EasyCLA or CLA Assistant), same principle as your current DCO bot: a policy enforced by memory isn't a policy.
- State the real reason in CONTRIBUTING.md, don't hide it behind "legal safety":
  > Why we ask: we sell a commercial license of this server to organizations (e.g. regulated financial institutions) that cannot accept AGPL's network-disclosure terms. That requires rights AGPL alone does not give us. Signing grants us a license to your contribution; you keep your copyright and can use your own work anywhere else. Contributing on behalf of an employer? They sign a CCLA once and maintain an approved-contributor list.
  
  An unexplained CLA reads as a rights grab and costs you drive-by contributions. A stated, checkable reason usually gets signed without argument.

**Track 2 — The 22 existing contributors: a scoped consent campaign, not a full relicense**

You are not changing the outbound license (AGPL-3.0 stays exactly as-is for the community edition), so this is smaller than Fogel's or Mozilla's full-relicense playbook — but the underlying discipline is the same:

- **Scope it precisely first.** Don't assume all 22 need chasing. Run `git log`/`git blame` against the files that actually ship in the commercially-sold artifact to find whose code is *still present*. Some early contributions may have been rewritten or removed since; that shrinks the list.
- **Get each remaining contributor to sign a CLA retroactively covering their existing contributions** — same document as Track 1, explicitly worded to cover past commits, not just future ones.
- **Map the unreachable ones now.** For anyone you can't reach or who refuses: either rewrite that specific code before it's sold commercially, or accept the gap and disclose it — don't paper over it. This list is the thing you don't want a bank's outside counsel discovering before you do.
- **Log the campaign as you go**: name, commit(s) covered, date signed, method of contact. This is exactly the artifact a buyer's diligence process will ask you to produce.

### The commercial license itself

- It needs to be drafted (or reviewed) by counsel — this is not a template-swap like the CLA. It has to specify what a bank actually gets released from (the AGPL §13 network-source-disclosure obligation, primarily), term, support terms, and how it interacts with future AGPL releases they might pull in.
- Decide the version boundary now: does the commercial license cover the current codebase only, or does it auto-extend to future AGPL releases? This has to be explicit in the contract, and it determines whether Track 2's consent campaign is a one-time event or a recurring one every time an outside PR merges without Track 1's CLA gate already catching it.

### What needs a lawyer — name it, don't guess

- Drafting the commercial license terms sold to banks.
- Confirming the CLA text's enforceability in whatever jurisdictions your CCLA signatories sit in.
- Whether your specific retroactive-consent wording actually covers "past and future contributions" the way you intend — get this checked, not assumed, since it's the whole basis of the commercial deals.
- Anything a specific bank's procurement counsel pushes back on in redlines.

Nothing above about *what these instruments do* is legal advice; how they apply to Sablewright's actual contracts and jurisdictions is exactly the boundary where you stop reasoning about it yourselves.

### Artifacts to ship, in order

1. CLA text (ICLA + CCLA), adapted from an existing template — not drafted from scratch.
2. Automated CLA-check bot wired into CI, replacing the DCO check.
3. CONTRIBUTING.md updated with the CLA section and the stated reason.
4. Consent-campaign tracking log (contributor, commits covered, status) — start this immediately, it's your longest lead-time item.
5. Commercial license document (counsel-drafted).
6. LICENSE file: unchanged, AGPL-3.0 stays exactly as it is — you are not relicensing the open project.

### Timeline reality check

Q1 is tight for Track 2, not Track 1. Standing up a CLA bot and updated CONTRIBUTING.md is days of work. Reaching 22 people, some of whom may have gone quiet, gotten new employers, or be unreachable, and getting signed retroactive grants back is weeks, realistically — and every account that's supposed to close in Q1 should have its "does the code they're buying have clean consent" question answered explicitly before signature, not assumed. If the campaign isn't done by the time the first bank deal is ready to close, tell sales and counsel that now, not after the contract's signed — that's a materially different risk than "engineering says we're fine."

### Revisit triggers

Reopen this if: a contributor refuses to sign and their code can't be cleanly rewritten before a specific deal closes; a foundation or acquirer later asks for a full IP audit; or the commercial-license revenue doesn't materialize and the CLA friction turns out to have cost you drive-by AGPL contributors for nothing.