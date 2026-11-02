**The line: give away the edges, license the core so it can only loosen, never promise "always open."**

**1. Full open source fails your reversibility test — this isn't a judgment call, it's how licensing works.**
Once you ship code under an OSI license (Apache 2.0, MIT), every copy already distributed is irrevocably licensed. You can change the license for the *next* release, but you cannot claw back rights on what's already out. "Open source it and see" is not an experiment — it's a one-way door on every version that goes out before you change your mind.

- Elastic, MongoDB, HashiCorp, and Redis all learned this the costly way: each shipped fully open, got commoditized by hyperscalers reselling their software as a managed service, then relicensed to claw back commercial rights. Each triggered a community fork (OpenSearch, Valkey, OpenTofu) and a trust hit that outlasted the license change itself.
- The backlash wasn't really about the new license. It was about breaking an explicit "we are open source" promise. Don't make that promise in the first place and there's nothing to walk back.

**2. Don't open source the broker core. License it source-available from day one.**
Use a BUSL-style license (Business Source License 1.1 — CockroachDB, Sentry, early HashiCorp): source visible, free to run for development, self-serve trial, and non-competing production use, with a narrow commercial carve-out blocking "offer this as a hosted service to third parties." You set the Change Date (when it converts to a fully open license) — set it 3-4 years out, or push it every release if you want.

Why this satisfies your CTO's constraint:
- You're pre-launch, no outside contributors yet — you hold 100% of the copyright. This is the only moment where you have full freedom to pick terms. Once you take outside PRs without a CLA, relicensing gets legally messy (this is exactly what slowed MongoDB and Elastic down).
- Every new release can carry its own Additional Use Grant. You're not locked into today's terms forever — you get a real per-release dial, and the direction you control is "loosen if it's working, hold the line if it's not." That's reversible in the direction that matters.
- What you can never take back is source already released under a given grant. So don't over-grant on day one. Start conservative, expand later — expanding is trivial and costless; contracting is what burns trust.

**3. Add a CLA now, even with zero external contributors.**
Costs nothing today. Removes the exact blocker that made past relicensing fights slow and adversarial — you don't want to be tracking down contributor sign-off in year three because you didn't set this up in week one.

**4. Decouple "open source" from "self-serve."** This is likely the actual confusion driving your investors' push.
Platform engineers don't need an OSI license to self-serve, sandbox, and expense. They need: readable source, a binary they can pull without a sales call, and confidence you won't rug-pull them mid-project. Confluent, Redpanda, Temporal, and CockroachDB all run strong bottom-up PLG motions on source-available licenses. "Open source" and "frictionless trial" are separable — sell the board on the second, not necessarily the first.

**5. Give away what isn't your moat, fully and permanently.**
Client libraries, SDKs, connectors, CLI tooling — Apache 2.0 or MIT, no restriction. These drive integration and adoption, carry near-zero competitive value standalone, and you should be comfortable never taking them back. This is where "open source," full stop, is the right and genuinely reversible-because-you'll-never-want-to-reverse-it answer.

**What to tell the board on the 30th:**
Not "open source: yes/no." Say: source-available core (BUSL) with a self-serve-friendly use grant, permissive OSI license on SDKs/clients, CLA in place from commit one, use grant reviewed every major release. That's a decision, it ships in three weeks, it gets you the visibility and self-serve motion your investors want, and there is no version of it your CTO can't unwind without breaking a promise you never made.