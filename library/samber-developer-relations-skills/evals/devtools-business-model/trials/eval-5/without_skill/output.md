**Next action: freeze the blog post today. Don't ship BUSL-1.1 or the "open source" wording until the audit in Section 4 below runs.**

# Halyard: License Strategy Memo

**To:** Founders, Board
**Re:** The BUSL-1.1 proposal, and what actually defends the business

---

## 1. Kill the phrase "our new open source license" before anything else

BUSL-1.1 is **source-available, not open source**. OSI has never approved it and will not: the Additional Use Grant discriminates by field of endeavor, which fails OSD #6. Publishing a post that calls it "open source" is not spin, it is a factual error, and it is the single most reliably punished move in this genre — MongoDB/SSPL (2018, withdrawn from OSI review in 2019, dropped by Debian and Fedora), Elastic/SSPL (2021), HashiCorp/BUSL (2023), Redis/RSALv2+SSPL (2024). Every one of them got the same thread, usually within six hours.

Say this instead, verbatim in the post: **"Halyard's next release moves from Apache-2.0 to the Business Source License 1.1, a source-available license. BUSL is not an OSI-approved open source license, and we are not going to call it one."** Owning that sentence costs you the headline and buys you the comment section.

It also matters legally. Marketing a non-OSI license as "open source" invites unfair-competition and false-advertising complaints, and it directly undermines your own trademark posture (below), where you need to look like the disciplined party. It further breaks downstream promises: procurement checklists, distro packaging, Homebrew, and corporate license allowlists gate on OSI status, not on your blog post.

⚠️ **Check first: is Halyard in a foundation?** CNCF, ASF, and LF projects require an OSI-approved license. If Halyard carries any conformance mark or foundation affiliation, this plan is not modifiable — it is off the table until you exit, and exiting is the loudest possible signal to a forker.

## 2. What BUSL actually buys you: less than the board thinks

- **Zero retroactive effect.** Every commit ever published under Apache-2.0 stays Apache-2.0 forever. Managed Halyard is already built on that code. The relicense does not touch the competing service that exists today, does not force a rename, and does not create a single dollar of leverage in the two contested accounts.
- **It only constrains future releases.** Value accrues only to the extent your roadmap contains things the provider needs. If the wire protocol is stable and they can sit on the last Apache-2.0 tag for 18 months, BUSL is a tax on your own community and free of charge to them.
- **Non-production use is always permitted** by BUSL's base grant. Your restriction lives entirely in the Additional Use Grant.

**Draft the Additional Use Grant narrowly and enumerate the carve-ins.** HashiCorp's "competitive offering" language was vague enough to scare integrators, resellers, and platform teams who were never the target — that ambiguity was a primary accelerant for OpenTofu. Recommended shape: permit all production use *except* offering Halyard, or a service whose primary value is Halyard's functionality, to third parties as a hosted or managed service. Publish an FAQ that explicitly permits: internal production at any scale, embedding Halyard inside your own non-queue product, consulting/support/migration services, CI and testing, and OEM in appliances. Counsel will resist the FAQ. Publish it anyway — enterprise procurement cannot approve an ambiguous grant.

**Change Date: 2 years, not 4.** HashiCorp took the full four (the common convention) and got maximum distrust for it. A rolling two-year window means any given version is genuinely open source within two years — a defensible answer to "so it's proprietary now." **Change License: MPL-2.0.** BUSL-1.1's parameter rules require the Change License to be GPLv2-or-later or GPL-compatible; MPL-2.0 satisfies that cleanly and was HashiCorp's choice. FSF treats Apache-2.0 as GPLv2-incompatible, so if the board wants "it reverts to Apache-2.0" as the trust story, get that blessed by counsel rather than assumed. Do not edit BUSL's body text — only the parameters — or you lose the SPDX identifier `BUSL-1.1` and the familiarity that comes with it.

## 3. Forking risk: high. Assume it happens.

The pattern is unbroken. SSPL produced OpenSearch (AWS-led, 2021; moved to the Linux Foundation in 2024). Terraform's BUSL move produced OpenTofu within days, under the Linux Foundation within weeks, plus OpenBao from Vault. Redis's license changes produced Valkey under LF, backed by AWS, Google, Oracle, Ericsson and Snap. Note the endings: **Elastic re-added AGPLv3 in 2024 and Redis re-added AGPLv3 in 2025** — both conceded, years late, after the fork had already taken the community.

Your situation is worse than the median, not better. A provider that has already shipped the service has sunk cost to defend and an urgent need to give those two accounts a license story. Fork probability, estimate: **70-80% within 90 days of your announcement**, conditional on your roadmap containing anything they want.

What raises the odds: a broad outside-contributor base (a fork inherits legitimacy); other vendors embedding Halyard who now need a non-BUSL path; a vague Additional Use Grant; a 4-year Change Date.
What lowers them: a contributor base that is ~100% your employees (a fork then has to staff from zero); you controlling the trademark and a conformance test suite; a first-party managed service already in market; a shorter, clearly-scoped grant.

Note the non-fork failure mode too: they may simply freeze on the last Apache-2.0 release and diverge. That fragments the protocol without giving you any of the reputational sympathy a hostile fork would.

## 4. The contributor gate — real, but not the one you were told

Correct the record: **Apache-2.0 inbound does let you ship future releases under BUSL.** Section 4 expressly permits different license terms "for any such Derivative Works as a whole," provided you meet Apache-2.0's conditions. You do not need a CLA to relicense the combined work.

What you cannot do is revoke the Apache-2.0 grant on contributed code. It stays permissive, in place, extractable, and its notices must be retained in your BUSL tree — which is itself a map for a forker.

Audit to run **this week**, before anything ships:
1. Any inbound code that is *not* Apache-2.0 — copyleft, unlicensed pasted patches, vendored deps, provenance-unclear blocks. This is the only category that can actually block you.
2. NOTICE/LICENSE/header compliance across the tree. Notice failures turn a clean relicense into a public compliance embarrassment.
3. Top 20 outside contributors by lines landed. Adopt **a CLA (Apache ICLA-style) plus DCO for all future contributions** before the announcement, not after.
4. Personally contact the top outside contributors under embargo. Relicensing volunteer work without a heads-up triggers a fork more often than the license terms themselves.

## 5. Trademark: your fastest and most underused lever

Apache-2.0 §6 grants no trademark rights. The copyright license the provider relies on says nothing about their right to call the product "Managed Halyard." Nominative use lets them say "compatible with Halyard"; using HALYARD as the brand of a competing service is a different, likely-confusion question.

The precedent is exact and it worked: Elastic sued AWS over "Amazon Elasticsearch Service" in 2019; the 2022 settlement had AWS rename to Amazon OpenSearch Service. A rename is plausibly forceable in months — versus a relicense that changes nothing for years.

This week: confirm trademark registrations (classes 9 and 42, US + EU + provider's home jurisdiction); file gaps; have outside counsel send a letter. Publish a trademark policy at the same time that grants generous community use (talks, blogs, compatibility claims, unmodified redistribution) and reserves service-branding — generosity to the community is what makes the letter to the provider read as principled, not protectionist.

## 6. BUSL does nothing for the two accounts. Here's what does.

Different clock, different team, starting Monday.

- **CEO-to-CEO/CTO-to-CTO outreach in both accounts this week.** Not through the champion who already flagged it — above them.
- **Contract leverage now:** multi-year renewal at a real discount in exchange for term extension; a roadmap-input seat; migration-assistance credits. Renegotiate before the provider's proposal lands, not after.
- **Ship a first-party managed Halyard.** This is the actual answer to "someone else monetizes our hosted experience," and it's the only thing BUSL's Additional Use Grant can meaningfully protect going forward. BUSL without a managed offering protects an empty room. Put a GA date on the calendar this quarter.
- **The "why us, not the hyperscaler" pitch needs:** core maintainers on your support rotation who fix the bug in the release, not a fork three versions behind; day-zero version parity and upgrade paths; no cross-cloud lock-in; roadmap influence in writing; total cost modeled against the provider's egress and instance markup. Argue latency-to-fix, portability, and price — not purity.

## 7. Sequencing

**This week:** contributor/provenance audit + notice sweep. Trademark referral, letter drafted, registration gaps filed. Executive outreach into both accounts, renewal terms drafted. Confirm foundation/conformance constraints. **Freeze the blog post.**

**This month:** CLA + DCO live on the repo. Additional Use Grant drafted with counsel, carve-in FAQ written. Managed-offering scope, pricing, GA date committed. Embargoed briefings to top contributors, top 10 customers, embedding vendors, two friendly analysts/press. Pre-write the fork response.

**This quarter:** Managed offering in private preview in the two contested accounts. License change ships **with** the managed offering, one narrative. Trademark resolution or escalation.

## 8. Blog post outline

- Lead with the business fact, not philosophy: "Two weeks ago a cloud provider launched a managed service built on Halyard. We are changing how we license future releases so the company that builds Halyard can keep building it." No "evolving industry landscape."
- State the license honestly (§1 wording), Change Date and Change License in the first screen.
- A table: what stays the same (every existing release is Apache-2.0 forever; self-hosting at any scale; embedding; forks of old code) vs. what changes (offering Halyard as a managed service to third parties, future releases only).
- Say explicitly what this does *not* do: doesn't affect the provider's existing service, doesn't remove anything from anyone's hands, doesn't stop anyone hosting the Apache-2.0 code. Say it yourselves — if a commenter says it first, you look like you were hiding it.
- Contributors section: what you audited, who you contacted, the new CLA, what contributors get in return.
- Preempt the thread with a Q&A: "Is Halyard still open source?" — No, future releases are source-available, here's the Change Date. "Will you relicense again?" — commit to a written policy. "Can I still run it in production?" — yes, examples. "What if you get acquired?" — answer it.
- Don't claim OSI status, don't use "open core" loosely, don't name-and-shame the provider, don't promise the relicense protects customers from hosting competition.

## 9. Bottom line

**Don't ship the board's plan as stated** — not the wording, not this timeline.

1. **This week, unconditionally:** contributor/provenance audit, CLA, trademark letter over the "Managed Halyard" name. Trademark is faster, cheaper, has a winning precedent, and is the only lever that touches the service that already exists.
2. **Account defense on a separate track starting Monday**, run by the founders, not legal.
3. **Commit to a first-party managed Halyard this quarter.** Without it, no license change protects revenue you actually have.
4. **Then relicense, in ~8-10 weeks, in this shape:** keep the core on an OSI-approved license — **AGPLv3 with a commercial exception** — and put BUSL-1.1 (2-year Change Date, MPL-2.0 Change License) only on the managed-service control plane and enterprise tier. AGPL lets you keep saying "open source" truthfully, and most hyperscalers' own internal policies keep them away from AGPL code paths even though compliance is achievable. It's where Grafana started, and where Elastic and Redis both eventually retreated to after their forks had already won. Get there first instead of last.

If the board insists on BUSL across the whole core: 2-year Change Date, enumerated carve-ins, CLA in place, contributors contacted under embargo, trademark letter already sent, managed offering dated — and the post never uses the words "open source license." Shipping it next week, with today's wording and none of the groundwork, is how you get a Linux Foundation fork by November and lose both accounts anyway.