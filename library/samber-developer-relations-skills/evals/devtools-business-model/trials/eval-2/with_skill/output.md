## Verdict: no, the boundary doesn't hold as drawn. 3 of the 5 items fail the paid-boundary test — pull them before you announce.

Applying step 3's five gates plus the "never on the paid side" list ([references/model-fit-scorecard.md](.)) to each item:

| Feature | Org-only? | Defensible w/o hostility? | Observable trigger? | Cost-to-serve OK? | Licence-compatible? | Hits a "never" rule? | **Verdict** |
|---|---|---|---|---|---|---|---|
| SAML/SSO login | yes | yes | yes (SSO config attempt) | yes (self-hosted) | check | **yes — sso.tax** | **PULL** |
| RBAC | yes | caution | needs a signal | yes | check | no | **KEEP (scoped)** |
| Audit logging | yes | caution | yes (audit/compliance ask) | yes | check | no, if scoped right | **KEEP (scoped)** |
| Kubernetes operator | debatable | **no** | n/a | yes | **likely no** | **yes — community-contributed** | **PULL** |
| Bulk CSV export | yes | n/a | n/a | yes | check | **yes — data export** | **PULL** |

### Why each PULL fails

**SAML/SSO login — fails the sso.tax rule outright, independent of whether it clears the org-only test.** The skill's own "never" list names this exactly: "SSO is a core security requirement for any company with more than five employees," and charging for it is the practice the actively-maintained `robchahin/sso-wall-of-shame` catalogue exists to shame. Yes, a solo self-hoster doesn't need SAML — but org-only-ness doesn't rescue this one, because the objection isn't "individuals also want it," it's "this is basic security hygiene, not a feature." Note the tension: the open-core archetype reference literally lists "SSO/SAML" as a typical paid-boundary component — that's a description of how the market used to draw this line, not this skill's recommendation. The explicit step-3 rule overrides it.

**Kubernetes operator — the worst item on the list, for two independent reasons.** First, it's a "community contributed" feature by name — "selling contributors their own work back invites the hostile fork," the most cited fork trigger in this market. Second, and more serious: if that operator already merged and shipped in an MIT-licensed release (which "written by a contributor at a bank" strongly implies — past tense, presumably already in the repo), Nuvexa may not even have the *legal* right to make it proprietary. Published MIT code stays MIT forever unless the contributor signed a CLA assigning or broadly licensing those rights back. **Before anything else, check: is there a CLA on file for that contributor, and does it grant relicensing rights — not just a right to redistribute?** If not, anyone can package that exact operator as a free "community edition" from day one, and Nuvexa ends up publicly claiming ownership of something it can't enforce — reputationally worse than never gating it at all.

**Bulk CSV export of flag history — direct hit on "data export and portability."** This is the customers' own operational history. Gating export reads as "pay us to get your own data back," and the skill is explicit this specific move is "punished harder here than in any other B2B segment." Keep all export, including bulk/full-history CSV, free and unlimited.

### Why RBAC and audit logging hold — with a scoping condition

Both are the canonical open-core boundary (the archetype reference names them together as the standard shape: "SSO/SAML, RBAC, audit logging... compliance reporting"). Minus SSO, these are legitimate. But narrow them:

- **RBAC**: gate the boundary at *custom roles and fine-grained permission policies* (per-environment/per-flag scoping, approval workflows), not at "any role differentiation at all." A bare Admin/Editor/Viewer split is close enough to basic access control that gating it entirely risks the same objection as SSO. Fine-grained policy management is the part an org needs and a solo dev doesn't.
- **Audit logging**: split it. Security-event logs — logins, permission changes, SSO config changes, anything a security team needs to detect a breach — stay free; this is the same "security fundamentals" territory as SSO (see the 2023 Microsoft/CISA episode, where paywalling basic cloud logging behind an E5 tier became a public incident after it delayed breach detection). The Enterprise item should be narrowly *compliance-grade retention and export of flag-change history* — who toggled which flag, when, immutable, exportable for a SOC 2 auditor. That's the accepted line, and it matches the skill's own named trigger: "an audit request."

### Two things to confirm before you announce anything

1. **Was any of these five features already released in a past MIT version?** "Published releases stay licensed forever" — if RBAC, audit logging, or CSV export already shipped in the open repo, pulling them into Enterprise now isn't a paid-boundary question, it's "closing a previously open core," the single most irreversible, trust-destroying move on the reversibility ladder, and it's read by the community as intent to close even when you say nothing. Check the changelog/release history for all five items, not just the operator, before finalizing.
2. **How will you see the crossing on self-hosted instances?** Every surviving gate needs an observable trigger — a second team, an audit request, a volume threshold. Self-hosted deployments don't emit that by default. If there's no opt-in telemetry or registry signal today, pipeline generation (not closing) will be the bottleneck, exactly as the open-core archetype warns.

### Net effect

Stripping SSO, the K8s operator, and CSV export leaves a two-item boundary (scoped RBAC + scoped audit/compliance export). That's thin — worth naming rather than discovering after the announcement. If revenue needs more than that, add from legitimate, unclaimed org-only territory instead of re-litigating the three you just pulled: multi-tenant/multi-cluster management, packaged compliance evidence (SOC 2 report bundles), guaranteed support SLAs or LTS backports (stacks cleanly as a secondary per the skill's stacking rules), or a genuinely *new* Kubernetes capability built fresh on top of the existing free operator (e.g., managed multi-cluster rollout policies) rather than reclassifying what a contributor already gave away.