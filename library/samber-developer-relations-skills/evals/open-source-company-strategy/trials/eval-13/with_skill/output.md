## Wharfline — open-core tier boundary decision

### Verdict

Reject the 25-user cap. Adopt a published persona-based rule (buyer-tiered open core), not "case-by-case with written criteria" as stated — that's still the least durable of the three known shapes unless the criteria collapse to one stable axis. And fix the "open source" label on the enterprise repo now, as a separate action, regardless of which tiering shape wins.

### Why the 25-user cap fails

1. **It's exactly the move GitLab's own published stewardship model rules out by name.** Their promise list includes "no artificial limits — repository count, user count, data size, throughput — on the open edition." A hard user cap is that category, not a variant of it.
2. **It fails the value-capture gate.** Name what a 24-person team loses by staying under 25 that a 26-person team gains by paying — nothing does. Headcount isn't a mechanism; it's a proxy nobody has to respect. Teams game it by spinning up a second org, staying at 24, or forking before you ever collect. "Matches where our money comes from" describes current revenue, not a reason a competent team can't just route around the wall.
3. **It fails the differentiating-asset gate.** Team size isn't a differentiator, it's incidental. You're not taxing a capability customers pay for — SSO, audit logs, multi-cluster orchestration, compliance reporting — you're taxing growth itself, which punishes your best adoption signal (a self-hosted deployment growing past 25 users is your funnel working, not a moment to wall it off).
4. **It's a narrowing move on a product that's been open core since 2021 with no such limit.** Nothing about a cap looks like "taking a feature away," but it retroactively constrains everyone already running Wharfline past 25 seats. That's read as a reversal, at fork speed — HashiCorp's and Redis's relicensing produced community forks within days, and Docker's 2017 rename drew severe backlash while changing no license and withdrawing no code at all. The lesson holds even for a "clean, enforceable" cap: the community prices what was taken, not how defensible the mechanism looked to the team that shipped it.
5. **Even on pure durability, it's the wrong shape.** Of the three named boundary shapes (buyer-tiered, scale-tiered, feature-by-feature), a user cap is scale-tiered, and scale-tiering explicitly "prices out exactly the large community deployments that generate contributors" — the deployments a self-hosted CI product depends on for visibility and word of mouth.

### Why "case-by-case, write down the criteria" is right in spirit and wrong as written

Writing criteria down beats not writing them down. But "case by case" is, by name, the least durable shape available: it re-litigates the line every roadmap cycle, which is the exact fight you're trying to end. Writing criteria down doesn't fix that unless the criteria reduce to one stable test that doesn't move with each feature's perceived value — "how valuable is this feature" has no stable answer quarter to quarter; "whose problem is this feature" does.

### The actual rule to adopt

**Buyer-tiered, on GitLab's persona test: who is the buyer for this specific feature, not how good it is.**

- Individual-contributor features — the engineer configuring pipelines, writing jobs, debugging builds — stay in the open edition, unconditionally, no seat or scale ceiling.
- Features whose buyer is a platform lead, security/compliance, or procurement — SSO/SAML, cross-team RBAC, audit logging, fleet/multi-cluster orchestration, compliance reporting, uptime SLA tooling — go in the commercial edition.

This test is stable because "whose problem is this" doesn't change as the roadmap grows; "how valuable is this" does, which is what's driving the quarterly fight today. It also gives you a mechanical answer for every future roadmap item instead of a fresh negotiation: ask who asked for it, tier it, move on.

### Publish non-reversal commitments now, not just the rule

A rule with no public commitment gets renegotiated the first time a paid feature underperforms. Publish, at minimum:

- Never move an already-open feature into the paid tier.
- Never add artificial limits — user count, repo count, job count, size, throughput — to the open edition. This is the line that permanently forecloses reviving the 25-user cap under a different name next year.
- Ship tests for open features alongside the features.
- Announce any boundary change before it lands, with the reasoning and the version it takes effect in.

### Decision rights

Name two separate roles, not one committee:

- **Business call — "should this feature be paid?"** Owned by whoever owns the roadmap (head of product, or the CEO if it's a large tiering move — GitLab names its CEO as final decider on exactly this class of decision). Applies the persona test above.
- **Compliance call — "does this violate a published commitment?"** Owned by whoever owns licensing/legal, reviewing every proposed paid feature against the non-reversal list before it ships. This is what stops "case by case" from quietly drifting back once the fight resumes next quarter.

### Fix the "open source" label — independent of the above

The enterprise repo is under a source-available license. Calling it "open source" on the marketing site is open-washing, and "everyone does this" is not a defense — it's a description of a pattern that has already drawn public correction against Elastic, HashiCorp, and others for the same move, and the OSI reserves "open source" for OSD-compliant licenses specifically because source-available terms (field-of-use restrictions, no-compete clauses) don't qualify. The audience the label is meant to reassure — engineers checking license terms before adopting — is also the audience most likely to notice and call it out, publicly.

Fix: call the enterprise repo "source-available" everywhere on the site. Reserve "open source" for the actual OSI-licensed core. This costs a find-and-replace, not a licensing change, and removes a live credibility liability that's unrelated to which tiering shape you pick.

### Re-evaluation trigger

Annual planning cycle, or earlier if: a competitor ships a managed/hosted version of Wharfline against you, a large customer or a procurement review flags the source-available "open source" claim, or a fork appears. Re-run the persona test at that point — don't let it silently decay back into feature-by-feature the next time a roadmap fight gets heated.