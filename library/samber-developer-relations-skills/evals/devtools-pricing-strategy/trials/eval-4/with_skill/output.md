Using devtools-pricing-strategy (step 3 gate rules + references/packaging-ladder-and-gates.md, pricing-evidence-base.md, pricing-change-cases.md) to sanity-check the three proposed gates.

## Verdict

| Gate | Verdict |
|---|---|
| SSO → enterprise-only | ❌ Fails the skill's rule directly |
| Data export / CSV → paid | ❌ Fails the never-paywall list, likely retroactive |
| Security patches delayed 30 days for community edition | ❌ Fails the never-paywall list, worst of the three |

None of the three survive as proposed. All three are named explicitly in this skill as the specific moves this market punishes hardest.

---

## 1. SSO enterprise-only

Rule (packaging-ladder-and-gates.md): *"basic SSO with a common provider → free or team... security fundamentals; gating them is the most criticised move in this market."* Keep only enterprise identity work — custom IdPs, SCIM, directory sync, session policy — at the top.

- sso.tax's own inclusion bar: "if your SSO support is a 10% price hike, you're not on this list." Sourced, but it's one maintainer's threshold, not a verified safe harbor — treat as directional, not a guarantee.
- CISA Secure by Design pledge (200+ signatories, sourced, voluntary — not binding) names SSO at no extra cost as a goal.
- Weatherline going from $240/mo Team straight to "starts at $28k" Enterprise for basic SAML/OIDC is a textbook 3x-plus identity tax, not a 10% surcharge.

The fact that it's "the single biggest reason anyone upgrades" is the tell, not the justification. It means buyers who need nothing but identity — no audit logs, no SCIM, no dedicated infra — are being forced through a $28k negotiated deal just to get SSO. That's friction against the ladder's own logic: self-serve/team rungs exist so an org doesn't need a human in the sale. Finance is reading a symptom of mispriced gating as proof the gate works.

**Fix:** move basic SSO (common IdPs — Google, Okta, Azure AD via SAML/OIDC) to the Team rung ($240/mo). Keep at Enterprise only: custom IdPs, SCIM provisioning, directory sync, session policy, audit-log-tied identity controls. This still monetizes identity — just at a rung a buyer can self-serve into instead of walking away or escalating to a sales cycle that isn't scoped for a $28k ask. Net effect is likely more revenue, not less: cheap-conversion Team deals plus the SSO-driven upsell pressure now points at $240/mo, not a stalled sales call.

## 2. Data export / raw CSV behind paid tier

Both references are explicit: never-paywall list includes *"Data export and portability"*; gate table says *"Usage visibility and data export → free → withholding either reads as a trap and blocks migration in both directions."*

- The stated reason — "free users burn a lot of egress" — is a cost justification, not a value justification. pricing-change-cases.md flags this exact pattern in its worked negative example: *"The justification is the vendor's cost, not the customer's value. Cost justifications invite the customer to compute your margin, and developers will."*
- Netlify's $104K bandwidth bill (sourced, dated case) is the canonical egress-cost failure, and the fix that held wasn't "gate the feature," it was caps + alerts + a stated runaway-usage policy.
- Open question I can't resolve from what you've told me: is CSV export already live and free today, or unshipped? If it's already shipped free and you pull it, that's the retroactive-gating pattern from the same doc's negative example verbatim — an existing capability taken back reads as extraction and is the move that produces forks/front-page threads, not a defensible new paid feature.

**Fix:** don't gate export itself — gate the thing actually driving egress. Keep manual, UI-driven CSV export of your own usage/data free, uncapped in count but bounded in size/rate (this satisfies "usage visibility and data export → free" and the free-limit checklist's "limits sit on the same axis as the paid metric"). Put the actual cost driver behind paid: API-based bulk export, scheduled/automated export, historical backfill beyond a window, data-warehouse sync. That's a new capability, not a repossessed one, so it doesn't trip the retroactive-gating problem.

## 3. 30-day security-patch embargo for community edition

Gate table: *"Security patches → every rung, always → withholding them turns users into adversaries and attracts CVE coverage."* Never-paywall list: *"Security fundamentals and security patches for the free edition."* This is the clearest, least-arguable violation of the three — it's on both lists verbatim, and it's not a trust/PR risk like the other two, it's an operational security risk: a public 30-day window where community-edition installs run a known-vulnerable version is a disclosed-but-unpatched state, which is exactly what invites CVE pile-on and turns your own free users into the attack surface everyone points at.

There's no "fix the gate placement" version of this one — unlike SSO or export, there's no adjacent capability to redirect the paywall onto. Security patches for the free edition aren't a monetization lever in this skill's model at all.

**Fix:** ship security patches simultaneously to every edition, always. If finance wants a paid-customer-first lever here, it doesn't exist in a defensible form — redirect that instinct at priority support response times or a dedicated security contact for paying tiers (both legitimate, both already in the standard rung contents), not at the patch itself.

---

## What to tell finance

The frame "SSO is our biggest upgrade driver" and "security patches are a paid perk" both describe the same mistake: using security fundamentals as the wedge instead of building one. This skill's ladder rule is gate on what an *organization* needs that a solo developer doesn't — audit logs, SCIM, residency, SLA credits, dedicated support. SSO, patches, and your own usage data fail that test; every org needs them, so gating them just taxes a requirement instead of selling risk removal. The revenue finance wants from SSO is real — take it at Team, not by holding a security fundamental hostage at Enterprise.

None of this touches your two published price points ($240/mo Team, "starts at $28k" Enterprise) — this is a gate-placement fix, not a repricing exercise.