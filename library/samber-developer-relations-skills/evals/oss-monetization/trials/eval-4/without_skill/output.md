# Brasswick Pro: boundary and pricing

**Verdict:** the plan needs four changes. Move percentage rollouts back to free, drop the daily ping, price per editor seat, and merge the audit-log PR. I haven't seen the PR, so my merge advice depends on a review of the code (see 4).

## 1. Boundary

Gate what an organisation needs, not what a developer needs. SSO, governance and compliance features are bought by someone who isn't the person running the server.

| Feature | Tier | Reason |
|---|---|---|
| Flags, environments, segments, basic targeting | Free | This is the product. |
| **Percentage rollouts** (simple, sticky, per flag) | **Free** | Your draft puts this in Pro, which I'd reverse. Gradual rollout is the core reason people pick a flag server, so gating it cripples the free tier and invites a fork. |
| Rules engine (advanced) | Pro | Gate the advanced layer instead: multi-condition rules, scheduled rollouts, approval workflows, automated progressive delivery. Teams with many flags and many editors value these. |
| Basic audit log | Free | See 4. |
| Audit log (advanced) | Pro | Configurable retention, export, SIEM streaming, tamper evidence, filtering API. |
| SSO (SAML/OIDC) | Pro | The standard paid feature, and what your two inbound customers asked for. |
| SCIM and group-to-role mapping | Pro | |
| Per-environment rate limiting | Weak Pro candidate | It protects the server from misconfigured SDKs, so gating it makes the free server look fragile. Keep a global limit free. Make per-environment quotas and per-key limits Pro, framed as multi-team governance. |
| Basic RBAC, API keys, Prometheus metrics | Free | |

Three rules protect trust:

- **Never move a shipped free feature to Pro.** Anything free today stays free. This is the usual way open-core projects lose their community.
- **Put Pro code in a separate directory (`ee/`) under a commercial or source-available license.** Core stays MIT. Check that all contributors agreed to MIT-compatible terms, and add a DCO or CLA before accepting contributions to Pro paths.
- **Publish the boundary in the repo** as a short `PRICING.md` or docs page, so nobody has to guess.

## 2. Banner and daily ping

**Drop the daily ping.** It would hurt you in three ways:

- **Trust:** an MIT, self-hosted server that phones home reads as a betrayal. The bank and the logistics company are the buyers you most want, and they usually run air-gapped or egress-restricted networks. They will block the ping or reject the software.
- **Legal:** it also creates GDPR and security-review friction for those customers.
- **Redundancy:** you don't need it to check a license.

**Do this instead:**

- Ship Pro keys as **signed licenses** (Ed25519, with expiry, seat count and instance ID). The server verifies them **offline**.
- Offer an **optional**, documented, opt-in anonymous version check if you want usage data. Make it off by default, list the exact fields sent, and send nothing identifying.

**Banner:** keep it small and tied to a trigger.

- Show it only to admins. Make it dismissible, and never block or degrade the server.
- Trigger it when someone opens the SSO or audit settings, not on a raw count of "more than 5 users". User count is a weak signal, and a five-user team may be your best advocate.
- Count locally. Don't report the number anywhere.

## 3. Pricing

I have no willingness-to-pay data, so treat the numbers below as a proposal to validate, not a finding.

**$19 per developer per month has three problems:**

- **Too low for the buyers who want SSO.** Banks and logistics firms pay enterprise rates and expect a contract, an invoice and support.
- **Hard to audit.** An offline server can't verify "developers". Many people touch a flag tool (product managers, ops, QA), and arguing about who counts is a bad sales conversation.
- **Likely under comparable commercial flag products.** Check the current public prices of LaunchDarkly, Unleash, Flagsmith and GrowthBook before you publish. I can't verify their numbers from here.

**Proposed structure:**

| Tier | Price | Notes |
|---|---|---|
| Community | Free, MIT | Everything in the free column above. |
| Pro | **$29 per editor seat per month, billed annually, 10-seat minimum** (about $3,500 a year) | An editor is anyone who can change flags. Viewers and SDK evaluations are free and unlimited, so seats are countable and match the value. Includes SSO, advanced audit, advanced rules engine, and email support. |
| Enterprise | Quote, annual contract | Air-gapped license files, SCIM, support SLA, security-review documentation, invoice and PO billing. This is for the bank and the logistics company. |

**Validate before you publish:**

1. Quote the two companies that asked for SSO. Ask what they pay for SSO elsewhere.
2. Ask 4 to 6 of the other named production users what they would pay, and for what.
3. If most say $29 is easy, raise it. If most hesitate, try $19 with the editor-seat model.

The editor-seat model matters more than the exact number.

## 4. The audit-log PR: merge it, after review

**Merge it if the code is sound.** A basic, free audit log that records who changed what and when is table stakes. Withholding it costs goodwill and gains little. Your Pro value sits in retention, export, streaming, tamper evidence and SSO identity, not in basic recording.

Before merging, check:

- **Extension point:** the design must let Pro replace or extend the storage and export layer without a rewrite or migration.
- **Content:** it must not log secrets or evaluation context data.
- **Retention:** it needs sensible default limits, such as a size cap or a fixed number of days, so the free log can't grow forever.
- **Tests and docs:** both must be present.
- **Maintainers:** the other two maintainers should agree, because this sets the free/Pro line in public.

Thank the contributor and tell them the boundary: basic log is free, advanced audit features are Pro. That avoids a surprise later.

## 5. Next steps

1. Decide the boundary table with your two co-maintainers.
2. Review and merge the audit-log PR.
3. Add the license split and DCO or CLA.
4. Build offline license verification. Skip the ping.
5. Run the pricing calls with the two SSO requesters and a few others.
6. Publish `PRICING.md` with the "nothing free becomes Pro" promise.