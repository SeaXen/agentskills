## Recommendation: reject the user-cap, adopt a written feature-category rubric (not raw case-by-case)

Neither proposal as stated is quite right. Proposal 1 (25-user cap) trades a real quarterly argument for a worse long-term problem. Proposal 2 (case-by-case) is the right instinct but "write down the criteria" is too vague to actually stop the fighting — it needs to be a fixed rubric, applied mechanically, not a looser version of the same debate.

### Why the user cap is the wrong axis

- **It doesn't track your actual value driver.** For a CI product, value scales with governance needs (SSO, audit, RBAC), scale/reliability needs (HA, performance at production scale), and support needs — not headcount. A 40-person team running simple pipelines has none of those needs; a 6-person team in a regulated industry needs all of them immediately. Gating on seats prices the wrong thing.
- **It punishes your best free users, not your best prospects.** A hard "free up to N users" ceiling is the textbook anti-pattern: your most successful open-source adopters — the ones evangelizing you internally — are the first ones to slam into the wall, at the exact moment they'd otherwise become your best word-of-mouth. It reads as "we changed our mind once you proved the product works," which is a specific, well-documented trigger for community backlash (see how HashiCorp's and Elastic's licensing moves were received, even though those were license changes rather than a user cap).
- **It's expensive and risky to enforce.** A real cap needs the self-hosted binary to count active users and phone home or refuse above threshold. That's license-enforcement code shipped inside your "open" edition — which itself undermines the open-source trust you're relying on for adoption, and it's an ongoing engineering/support burden (edge cases: bot accounts, service accounts, CI-triggered users, multi-org counting disputes).
- **Feature-module gating doesn't need any of that.** GitLab, Sourcegraph, Mattermost, Grafana — the whole open-core cohort — gate by *what the feature is*, not by counting who's logged in. Enterprise features simply aren't in the OSS build. No runtime enforcement, no phone-home, no counting disputes.

### The rubric to adopt instead

Fix a small, stable set of categories, once, and apply them mechanically to every roadmap item going forward:

| Category | Goes commercial when it... | Examples |
|---|---|---|
| Governance & compliance | Exists to satisfy an auditor, regulator, or security team | SSO/SAML, fine-grained RBAC, audit logs, compliance exports |
| Scale & reliability | Exists to keep production stable at scale | HA/multi-region, advanced caching, priority performance work |
| Cross-team management | Exists to administer many teams/projects as one org | Org-wide policy, usage/cost analytics across teams |
| Support & commitment | Exists to guarantee a response, not just a capability | SLAs, dedicated support, professional services, custom contracts |

Anything that doesn't clearly land in one of those four stays open, full stop — no re-litigating. New feature proposals get slotted at design time, not fought over at planning time. Add one governance rule: an exception (something that seems like a bucket-4 item but you want to give away, or vice versa) needs sign-off from one named owner, not a roadmap-meeting vote. That's what actually kills the quarterly fight — it moves the disagreement from "everyone argues every feature" to "rare, deliberate, owned exceptions."

You can still use team size informally in messaging ("comfortable for small and mid-size teams") — just don't make it the enforced technical boundary. The correlation between "large team" and "needs governance/scale features" is real; let it stay a correlation, not the mechanism.

## Separately: stop calling the enterprise repo "open source"

Fix this regardless of what you decide above — it's a bigger risk than the tier-placement fight.

- "Open source" has a specific meaning (OSI-approved license: free use, modification, and redistribution, including commercial and competing use). A source-available license — visible code with usage restrictions — doesn't meet that bar, no matter how open the diff feels.
- "Everyone does this" isn't accurate for the companies that got burned by it. MongoDB (SSPL), Elastic, and HashiCorp (BSL) all *stopped* calling those repos "open source" specifically because the mislabeling — after building years of goodwill as genuinely open — triggered public backlash, community forks (OpenTofu, OpenBao, Valkey), and OSI/Fedora/Debian delisting. The lesson from those cases is "be precise about this," not "everyone gets away with it."
- It creates real downstream risk: a customer or integrator who takes "open source" at face value may reasonably assume rights your actual license doesn't grant (redistribution, competing hosted offering). That's a license dispute waiting to happen, not just a branding nitpick.
- It's also the single fastest way to torch the trust your open-core motion depends on. Your adoption funnel runs on developers believing your OSS claims are honest; get caught soft-pedaling one license as another and every other claim on the site gets re-scrutinized.

Action: audit the site and docs, replace "open source" with "source-available" (or name the license directly) everywhere it refers to the enterprise repo, and add a one-line FAQ answer ("Is Enterprise open source? No — it's source-available under [license]; here's what that means"). Keep "open source" exclusively for the repo actually under an OSI license.