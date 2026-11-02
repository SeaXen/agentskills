## Recommendation: BUSL-1.1 on the core, not AGPL — and not as a fix for what already happened

Switch the tracing core to **Business Source License 1.1** at the next release, converting to **GPL-2.0-or-later** after a **4-year Change Date**, with a broad **Additional Use Grant** that keeps almost everything you have today free. Leave client SDKs/instrumentation libraries on Apache-2.0. This is not legal advice — it's the licensing-strategy read; two spots below need your counsel's sign-off, flagged explicitly.

### First, correct the premise the board and GC are both working from

Neither AGPL then nor AGPL now "prevents" what already happened, and that has to be said out loud before anyone picks a license off the back of it:

- **The clone is already forked from a published Apache-2.0 tree.** Every release you've ever shipped stays Apache-2.0 forever — that's not a loophole to close, it's what "open source" means. Nothing you license today reaches backward into a fork that already exists.
- **Even prospectively, AGPL obliges disclosure, not prohibition.** A hyperscaler with the engineering resources to build a control plane on your codebase has the resources to comply with AGPL's network clause — publish the modified source — and keep running the exact same managed service. AGPL redirects competition into a compliance cost; it does not remove the competitor. Treating it as a shield is a documented failure mode, not a hypothetical one.
- **Whether their "control plane bolted on" would even count as a modified/combined work under AGPL's network clause is a real question — and it's the one thing nobody should assert without counsel.** If the control plane talks to your code only over an API boundary rather than linking/combining with it, AGPL's source-disclosure trigger may not reach it at all. That's the first of the two items to route to your GC directly, not settle here.
- If AGPL had been in place, it also cuts against you on the buy side: it's one of the few licenses with a **named, written enterprise ban** (Google's own published policy: "AGPL MUST NOT be used at Google," extending to laptops). Given your self-serve revenue is already down 11% QoQ, adding a license some engineering orgs are forbidden from touching is a real adoption cost, not a free move.

So: AGPL wouldn't have stopped this, and adopting it now mainly buys you a disclosure right against the *next* clone, at the cost of your OSI badge's easiest-to-defend cousin and a written enterprise ban some of your own self-serve funnel may be subject to.

### Why BUSL over AGPL, specifically for your situation

The actual harm is narrow and nameable: *a specific hyperscaler reselling your code as a managed service, with zero reciprocity, while your own commercial motion (self-serve + enterprise renewals) absorbs the damage.* BUSL's Additional Use Grant is a field-of-use carve-out built for exactly that shape of problem — it doesn't ask "did they publish their modifications," it asks "are they offering a competing hosted/managed service," which is both the actual thing you're trying to stop and a much easier line for your sales and legal teams to explain to procurement than AGPL's murkier network-clause question above.

This is also not a novel move — it's the HashiCorp shape almost exactly: MPL-2.0 → BUSL-1.1 in August 2023, triggered by a hyperscaler-adjacent competitive threat, future releases only, SDKs/APIs left untouched. Recommended parameters for your case:

- **Change Date: 4 years** (the maximum BUSL allows) from each release under the new terms. Given the threat is live now, don't shorten this for goodwill — a 2-year window converts to fully open right when a managed clone would be entrenching.
- **Change License: GPL-2.0-or-later.** This is the license the code becomes automatically once the Change Date passes for each release; it needs no compatibility check against your current Apache-2.0 corpus because nothing is being combined, the code is just changing what it is.
- **Additional Use Grant — make this the load-bearing part:** grant free production use for everything *except* "offering the software, or a service substantially derived from it, as a hosted or managed distributed tracing service to third parties." Self-hosted deployments, internal use, and embedding stay completely free. This is what protects the self-serve line you're already worried about — a BUSL adoption with no use grant would hit your own declining self-serve revenue harder than the competitor did.

### What needs settling before the Change Date is more than a number on a slide

1. **Contributor consent.** Four years and ~19k stars means outside contributors almost certainly hold copyright on code still in the tree. If there's no CLA today, the relicense can only bind *future releases* — anything of theirs already merged stays under Apache-2.0 regardless of what you announce, and you need a map of who's reachable versus whose code has to be rewritten or removed to close the gap. This is the second item for counsel: confirming what, if anything, your existing contributor agreements already grant you.
2. **Dependency audit.** Nobody's checked whether anything shipped in the core carries a copyleft license that forecloses this before preference even enters. Do this from the lockfile, not from memory, before the date is locked.
3. **Repository boundary.** Apply BUSL to the collector/backend core only — leave instrumentation SDKs, client libraries, and any wire-format/protocol spec on Apache-2.0. Those are your adoption funnel and the reason customers can integrate without a legal review; commoditizing them for free is what keeps the top of the funnel open while the part that's actually being resold gets the restriction. Write the boundary down in a root `LICENSING.md` — a single root `LICENSE` file would otherwise silently claim the whole tree.

### Expect a fork, and don't let it be a surprise

Every documented case of this move produced one, within days to a few weeks: Elasticsearch → AWS's OpenSearch, Redis → the AWS/Google-backed Valkey, HashiCorp → the Linux Foundation's OpenTofu (140+ companies signed on within weeks of the announcement). You're at higher risk than the average case, not lower — the hyperscaler in question has already demonstrated working familiarity with your codebase, which is exactly the profile of an actor who could stand a fork up fast, possibly under a foundation banner for legitimacy. Name who would plausibly lead it, decide your response before the announcement goes out, and don't frame the change as "protecting the community" — that reads as evasion and gets taken apart publicly within hours. Frame it as what it is: a named competitor, reselling your work with no reciprocity, while two enterprise renewals stall.

### What this move does not fix

A license change alone doesn't rescue the two stalling renewals — that's a value-capture and competitive-positioning question, not a licensing one, and it's worth a pass with `devtools-business-model` to make sure sales has an actual answer ("you get our roadmap, support and SLA; a hosted clone doesn't") rather than just a licensing footnote. BUSL closes the *future* version of the problem; it does not retroactively touch the service that already launched six weeks ago, and no license would have.

### Artifacts for the release

- `LICENSE` at repo root replaced with unmodified BUSL 1.1 text (parameters filled in); `sdk/LICENSE` (or per-package) stays Apache-2.0; root `LICENSING.md` explaining the split.
- `SPDX-License-Identifier` headers updated per directory to match the boundary.
- Package/registry metadata and any container image labels updated for the core; left alone for SDK packages.
- Contributing guide updated with the version boundary (old releases stay Apache-2.0 forever) and, if you don't already run one, a CLA introduced for new contributions to the core going forward — publish the actual reason (you need rights AGPL/BUSL alone don't grant for a future commercial motion), not "for legal safety."
- Announcement drafted before the decision is finalized, stating the change plainly: what changes, what doesn't (SDKs, past releases, docs), who's affected (managed-service resale) with a concrete example, who isn't (everyone self-hosting or embedding), why (name the provider or don't name a reason at all — vague "sustainability" framing gets picked apart), and where the last Apache-2.0 commit is for anyone who wants to fork it.

**Revisit if:** a foundation entry changes the rules, a fork gains real traction and needs a response, the stalling renewals resolve without the license change mattering, or 12 months pass with no measurable change in managed-service resale activity.