**Recommendation: BUSL, not AGPL — but relicensing alone won't fix the problem you actually have.**

**Why BUSL fits the threat and AGPL doesn't**

- Your harm is a hyperscaler running a *managed service* built on your code, undercutting your commercial offering. That's exactly what BUSL's "Additional Use Grant" is built to block: free use for everything except offering a competing hosted/managed product. HashiCorp, MongoDB (SSPL), Elastic, CockroachDB, Confluent all moved this direction for this exact reason.
- AGPL's network clause is weaker than your GC thinks here. It triggers on distributing a *modified version* or offering one as a network service. Sophisticated cloud vendors route around this by keeping their control plane as a separate process that calls your engine over an API — arguably not a "combined work," so no disclosure obligation. AWS did precisely this with MongoDB: rather than fork AGPL'd Mongo code, they built DocumentDB as a clean-room reimplementation. AGPL didn't stop competition — it just changed its shape. It's a real deterrent against literal code copying, but not a reliable one against a hyperscaler "obviously your codebase with new plumbing."
- AGPL also cuts the other way on your current wound: it's notorious for scaring enterprise legal/procurement, which is the exact population you're already losing (two stalling renewals). Swapping to a license enterprises actively avoid, while you're bleeding enterprise revenue, compounds the problem it's meant to solve.

**What relicensing cannot touch**

- The fork that already shipped is under Apache-2.0 forever. BUSL (or AGPL) only governs code you release *after* the switch. The cloud provider keeps full rights to everything up to that commit and can keep maintaining their fork indefinitely.
- If brand/naming confusion is part of "very obviously our codebase," that's a trademark question, not a copyright-license question. Handle separately.

**Before the board can actually lock in BUSL at next release, confirm three things**

1. **Copyright chain.** Four years, ~19k stars, almost certainly external contributors. Check whether you have a CLA or DCO that assigns/licenses rights broadly enough to relicense their contributions. If not, you can only BUSL *new* code going forward — old code stays Apache-2.0, contributor by contributor, unless you get retroactive consent or rewrite affected sections. This is the single most common blocker teams skip and regret (Redis hit this in 2024).
2. **Fork risk math.** Established Apache projects that go BUSL reliably spawn a foundation-backed fork within weeks (Terraform → OpenTofu, Elasticsearch → OpenSearch, Redis → Valkey). Tracing lives in the CNCF/OpenTelemetry orbit, which is exceptionally fork-friendly — including for the same cloud provider that just forked you. Model whether a credible fork leaves you worse off than status quo before committing.
3. **Draft the Additional Use Grant and Change Date narrowly.** Restrict only "offering this as a competing hosted/managed service"; leave internal use, embedding, and self-hosting free. Set Change Date at 3–4 years (Apache/MPL reversion) to keep "eventually open source" credibility and blunt community backlash. Copy CockroachDB's or Sentry's language as a starting point, not SSPL's — SSPL was rejected by OSI and drew more heat than it was worth.

**Middle option worth putting in front of the board:** open-core instead of whole-project relicensing — keep the 19k-star core Apache-2.0 (preserves community trust, avoids fork trigger), and ship the genuinely differentiated enterprise layer (multi-tenant control plane, RBAC/SSO, fleet management) under BUSL or fully proprietary. This targets your renewal problem directly without reopening the fork-risk fight on the whole project.

**Bottom line:** tell the board BUSL, correct the GC's AGPL assumption on the record (get outside OSS-licensing counsel to confirm — this is a live area of case law, not settled), and don't let "we relicensed" get reported as "we fixed the AWS/GCP/Azure problem." It stops the *next* fork. It does not claw back the one you already have.