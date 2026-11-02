# The gap: DCO ≠ relicensing rights

🔴 **Engineering's framing is wrong, and it's wrong in a way that will surface exactly when a bank's legal team does vendor due diligence.**

"Dual licensing" (AGPL + commercial) only works if Sablewright holds — for 100% of the shipped code — rights broad enough to license it under terms other than AGPL. A DCO sign-off doesn't grant that.

The DCO (`Signed-off-by:` trailer) certifies the contributor *has the right to submit their patch under the project's stated license* (here, AGPL-3.0). It grants Sablewright nothing beyond what AGPL-3.0 already grants every other licensee on earth. It is a provenance attestation, not a copyright license grant.

Consequence: for each of the 22 outside contributors, unless something beyond the DCO exists, Sablewright can only distribute their code under AGPL-3.0 — the same license they contributed it under. Selling a bank a commercial license that covers those contributors' lines is Sablewright purporting to grant rights it doesn't hold. That's not a theoretical risk: bank procurement/legal teams routinely request a chain-of-title / IP-ownership rep as part of vendor security review, specifically because financial institutions get burned by exactly this pattern.

This is the textbook reason dual-licensed projects use a **CLA**, not a DCO. Qt is the standard example: GPL/LGPL + commercial, and The Qt Company requires every contributor to sign a CLA precisely so it can grant a second, proprietary license over community contributions. A DCO-only project (e.g. the Linux kernel) deliberately *cannot* do this — that's a feature there, a blocker here.

# What to set up

## 1. Audit, before anything else

- Enumerate every merged PR from the 22 outside contributors: files touched, lines changed, which subsystems.
- Pull the exact DCO text your bot enforces — confirm it's stock DCO 1.1 wording, not a custom variant that happens to include a broader grant (check `CONTRIBUTING.md` history for this).
- Flag which of the 22 contributed as employees of another company (check commit email domains, LinkedIn, `Signed-off-by` names vs. affiliations) — their employer may hold the actual copyright, meaning the individual can't grant relicensing rights alone even if they want to.
- Get outside IP/licensing counsel to confirm the gap and put a number on exposure. Banks will have their own counsel review this; get there first.

## 2. Close the gap on the existing 22

No single move fixes this — expect to combine these:

- **Retroactive consent.** Go back to each contributor with a relicensing agreement (a CLA addendum covering *past* contributions specifically — a new CLA signed today does not retroactively cover old PRs unless it says so and they sign it). Prioritize by lines-of-code / how central their files are to what you're selling.
- **Rewrite.** For contributions you can't get consent on (unreachable, refuses, wants payment you won't pay), reimplement that code internally so Sablewright/an employee owns it outright. Track exactly which files this touches.
- **Architectural isolation.** If external contributions cluster in separable modules/plugins, scope the commercial SKU to exclude them — those pieces stay AGPL-only, forever, and that's fine as long as they're not load-bearing for what banks are buying.
- **Accept AGPL-only for the rest.** Some code may just stay encumbered. Document it so it's a conscious scoping decision, not a landmine someone finds in Q2.

With 22 contributors this is tractable in weeks, not years — that's small enough to run as a direct outreach campaign, not a legal odyssey.

## 3. Fix the contribution pipeline going forward

- Add a **CLA** (individual + corporate) alongside — not instead of — the DCO. Keep DCO for lightweight authorship attestation; the CLA is what actually grants Sablewright a license broad enough to relicense, including under future commercial terms.
- CLA must include an explicit copyright grant (perpetual, worldwide, irrevocable, sublicensable) sufficient to relicense contributions under any license, plus a **patent grant** — AGPLv3 carries its own implicit patent peace clause for AGPL licensees, but a Sablewright-issued proprietary license to a bank is a separate grant that doesn't automatically inherit that patent coverage from the original contributor.
- Require a **Corporate CLA** for anyone contributing as part of their job — the individual CLA doesn't bind their employer's copyright.
- Gate merges on CLA the same way the DCO bot gates today (CLA Assistant, EasyCLA, or equivalent) — same enforcement pattern, one more required check.
- Update `CONTRIBUTING.md` and the PR template to state plainly: contributions are licensed to Sablewright under the CLA; the project ships under AGPL-3.0; Sablewright separately sells commercial licenses.

## 4. Build the artifact banks will actually ask for

- Maintain a contributor rights ledger: contributor → PRs/files touched → agreement status (DCO only / CLA signed / rewritten / isolated) → date.
- This becomes the chain-of-title summary handed to a bank's legal/procurement team during vendor review. Not having it ready is itself a red flag to a regulated buyer — having it ready and clean is a sales asset, not just a defensive document.

# What to tell the CEO and engineering

"AGPL + commercial license = dual licensing" is correct **only if** Sablewright owns or controls the rights to everything being sold. Right now it doesn't, because DCO was never designed to grant relicensing rights — it was designed for the opposite case (projects that never intend to leave copyleft).

This doesn't blow up the Q1 plan. It's a parallel workstream that needs to start now: rights audit, CLA rollout, and contributor outreach all take real calendar time, and 22 people is a small, closeable list if you start immediately rather than after the first bank contract is on the table.