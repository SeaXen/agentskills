**Verdict: no. LGPL-3.0 wrong pick for this artifact. Don't file paperwork yet.**

## Why LGPL-3.0 fails here

LGPL trigger: distribution of linked work. Obligation: recipient must be able to relink modified library into it. Two facts in your setup break that promise:

1. **Static linking.** Reference: "static linking pulls relink obligations onto the application." Whole firmware inherits the relink duty, not just pulsecore.
2. **Signed firmware, nothing else boots.** LGPLv3 incorporates GPLv3 §6 anti-tivoization: for a "User Product," you must give Installation Information — enough for recipient to install and run a *modified* library on the actual device. A locked bootloader that only executes vendor-signed images is the exact case that clause exists to kill. Naming it: this is Tivoization, named after TiVo's own hardware lockdown, the reason GPLv3/LGPLv3 added the clause at all.

One open legal question inside that: GPLv3 defines "User Product" as something normally used for personal, family, or household purposes. Hospital appliance, sold B2B, probably fails that test — so the anti-tivoization duty might not formally attach. That's a real question, not settled here — route it to counsel, don't assume it either way.

But even without anti-tivoization, LGPL's base relink duty still assumes the modified library can eventually *run*. On a device where nothing unsigned boots, ever, that promise is either hollow or broken. Fixing it by dropping to **LGPL-2.1** (no anti-tivoization clause) doesn't solve the goal — it just lets you comply on paper while the customer's fix can never actually run on real hardware. That's the textbook Tivoization loophole. Don't reach for it; it reads badly if noticed and buys you nothing real.

## Plain GPL-3.0 also wrong

Static-linking a library under plain GPL pulls the *whole* combined work under GPL (FSF's own reading — this is the entire reason LGPL exists as a separate license). Ship GPL-3.0 pulsecore statically linked, and each appliance maker's whole proprietary firmware must go GPL too if distributed. That kills adoption from your existing paying customers outright.

## The gap nobody's license fixes

No copyleft flavor — MPL, LGPL, GPL, AGPL — creates a duty to send fixes **back to you**. Every one of them only obligates the appliance maker to make modified source available to *their* recipients (the hospital). You are not automatically a recipient. "Fixes come back to us" is not a licensing outcome — it's a **contract** outcome. Only a contract term (support agreement, commercial license condition) can require upstream submission to Thornerly specifically. Keep that separate from the license decision.

## Two honest postures (step 2 — no recommendation locked yet)

| Posture | License | What happens | Cost |
|---|---|---|---|
| **A — Open commons** | MPL-2.0 | File-level copyleft. Explicitly permits static linking into proprietary firmware — no relink/install promise, so zero Tivoization conflict on the locked device. Modified pulsecore files must be published to recipients on distribution. Real but request-based reciprocity. | Retires your per-unit fee — MPL already lets appliance makers link for free. Revenue has to move to support/certification/services. |
| **B — Copyleft leverage + dual license** | GPL-3.0 (public track) + commercial license (paid track) | Static linking under plain GPL forces the whole firmware open — genuinely inconvenient for every appliance maker, so nearly all of them buy the commercial track instead. Commercial contract carries a mandatory "submit your modifications upstream" clause. | Needs a CLA (below) to keep dual-licensing contributed fixes. Needs drafted commercial contract. AGPL-3.0 buys nothing extra here — no network/SaaS angle in embedded firmware, skip it. |

Row A matches your literal sentence ("open it up") most cleanly and has zero technical conflict with the locked device. Row B preserves the per-unit-fee-shaped revenue and gives you an actual enforceable fixes-back clause instead of hoping for one. Your message says "right now… we license it per unit" without saying you're dropping that revenue — confirm which one you actually want before picking. That single answer decides A vs B.

## Contribution policy — needed either way

Add a **CLA** (not just DCO) the moment appliance makers start contributing fixes back. Reason: relicensing/dual-licensing contributed code needs a right your outbound license alone doesn't grant. Today pulsecore is fully Thornerly-owned, so no CLA gap yet — but the first external patch you merge creates one. State the reason in the CLA text per contributing-guide wording: "we offer a commercial license to customers who can't accept [GPL-3.0/MPL-2.0], which needs rights the open license alone doesn't give us."

## Before paperwork starts — close these

1. **Dependency audit.** Enumerate everything pulsecore statically links or vendors, transitive included. A single copyleft dependency already shipping in the artifact can eliminate options before preference matters.
2. **Ownership check.** Confirm no contractor code or unclear-provenance code sits in the tree without an assignment already in hand.
3. **Revenue question.** Keep per-unit fee in some form, or retire it? Decides posture A vs B.
4. **User Product / anti-tivoization question.** Whether hospital-sold appliances count as GPLv3 "User Products" — get counsel's read, don't self-decide.
5. **Regulatory check.** Locked/signed boot is likely an FDA/IEC 62304-driven requirement, not just a business choice. Have counsel confirm the chosen license's obligations don't collide with your customers' device certification.

## Artifacts once decided

`LICENSE` at root (unmodified text), SPDX headers, contributing-guide section with the sign-off/CLA mechanic and its automated check, package metadata license field, `NOTICE` file if the pick requires attribution propagation.

Not legal advice — the User Product classification and the FDA/locked-boot interaction both need a lawyer before anything ships. Everything above is what the license text and documented precedent (TiVo/Tivoization, MPL's own stated design intent) say, not a prediction of what a court or auditor would rule.

**Next: answer the revenue question (keep per-unit fee or not) — that's the one fact that picks A or B.**