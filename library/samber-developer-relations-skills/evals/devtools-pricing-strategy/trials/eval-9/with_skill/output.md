## Sanity check: Vaultstream roadmap (secrets-sync CLI, 6 eng, free tier live, $180k enterprise deal pending)

**Bottom line: the sequencing is backwards, and the entry tier decision actively kills your only channel that doesn't need a human.** One piece is defensible — promoting the enterprise rung — but the plan overshoots it into building enterprise *only*, for two quarters, with everything else pushed to "some time after."

### What's right

Pulling enterprise features forward is a legitimate move, not a default violation. The skill's own rule: *"Promote [enterprise] the moment named deals stall on audit logs, an SLA or an identity requirement — a stalled deal is evidence the ratio cannot see."* You have exactly that evidence: one deal, $180k/yr, named blockers (audit logs, SCIM). That's real, not a hypothetical enterprise buyer.

### What's wrong

**1. You're building the whole enterprise rung when the deal only needs a slice of it.**
Audit logs + SCIM unblock the $180k deal. SSO, granular RBAC, and SOC 2 are the *rest of the rung*, not what's blocking this specific account. Bundling all of it into "phase 1" turns a scoped unlock into a standing compliance program before you know a second enterprise account exists.

**2. Deferring self-serve is the one thing this skill says never to do first.**
Build order (efficiency, step 3): `self-serve paid > free surface > team > enterprise`. Reason stated directly: *"it is the only one that returns revenue without a human in the loop."* Your plan puts it last, undated ("some time after"). For two quarters, the only revenue source you're building toward is one deal — nothing compounds, nothing self-serves, and the team rung you're building second has no self-serve customers yet to need roles or shared billing for.

**3. "Contact us" at the entry tier is an exit, not a funnel.**
Direct quote: *"Publish prices as far up the ladder as the business can bear. In a bottom-up motion, 'contact sales' at the entry rung is not a lead form, it is an exit."* You already have a free tier — a working bottom-up signal — and you're about to gate the paid step above it behind a sales conversation. That doesn't "qualify every lead," it removes the tier most CLI users would actually convert through on a card, unassisted. The developer free-to-paid median is ~5% (sourced: Lenny's Newsletter survey, developer products), and that number assumes a self-serve step exists to convert *into*. Gate it behind contact-us and you're not qualifying leads, you're discarding the conversion event itself.

**4. Gate placement: SSO doesn't belong in the enterprise bundle by default.**
Reference table: basic SSO with a common provider sits at **team**, not enterprise — only custom IdP/SCIM/directory sync/session policy belong at enterprise. SSO is also the most-cited paywall backlash case in this market (sso.tax's bar: a 10% surcharge is acceptable, an identity tier is not). If "SSO" in your plan means basic SSO, ship it cheap at team; keep the enterprise-specific identity work (which for you, concretely, is SCIM — already named as a blocker) scoped to the deal.

**5. Resourcing math nobody's written down.**
SOC 2 + SSO + RBAC + audit logs, built by a 6-engineer team, is a multi-quarter standing job (the skill's own magnitude: *"enterprise rung is a standing job of security reviews, questionnaires, custom terms and SLA credits"*). That's effectively your whole engineering org for two quarters, for one $180k account. The field-sales viability threshold (sourced: Christoph Janz) is roughly six figures ARR per account — $180k clears that, so a human-mediated sale is economically sound *for this account*. But committing your entire build capacity to the full enterprise surface on the strength of one deal is a bet that more six-figure accounts are coming. Is the pipeline behind this deal real, or is it the only one? That answer should gate whether you build the *full* SOC 2 program now or defer it until a second or third enterprise prospect confirms the pattern.

### Recommended resequencing

1. **Now, scoped:** ship audit logs + SCIM as a negotiated unlock for the $180k deal specifically — not the full enterprise rung. Treat it as closing one account, not launching a tier.
2. **In parallel, quarter 1:** build self-serve paid. It shares most of its engineering with the free tier's metering (same axis, same meter per step 3), it's the cheapest rung to build, and it's the only one earning without sales cycles while the enterprise deal closes.
3. **Quarter 2:** team rung — roles, shared billing, basic SSO. This now has self-serve customers to graduate from.
4. **After, evidence-gated:** finish the rest of the enterprise rung (full RBAC, SOC 2 as a certified program, negotiated SLAs) once a second or third enterprise deal confirms the segment, not on the strength of one.
5. **Entry tier:** publish a real self-serve price. Qualify leads on product usage signals (seats, repos connected, secrets synced — whatever your value metric ends up being) instead of a contact form. Save "contact us" for the enterprise rung only, where it belongs.

### Open question this plan skips

You haven't named a value metric anywhere in this — seats, secrets synced, environments, something else. For a CLI that likely gets invoked by CI as much as by humans, seats may not hold (step 2's collapse trigger: *"flat seat count against rising usage"*). Worth nailing down before self-serve pricing goes live, since it decides what the self-serve rung is even charging for.