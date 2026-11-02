# Is AGPL the right move for Kettleworth Data — licensing decision record

Not legal advice — this is a distribution and business-model analysis. Two items below need your lawyer before Friday, flagged where they come up.

## Direct answer

**AGPL-3.0 is the right license family for the problem you named — closing the "run it as a managed service, publish nothing" loophole. A straight MIT→AGPL swap is not the right move.** The version worth taking to the board is: AGPL-3.0 going forward, paired with a CLA and a commercial dual-license track, executed as a future-releases-only change — plus two checks you need answered *before* Friday, because either one could change the recommendation.

The two checks:

1. **Does your bank, your retailer, or the account in procurement have a blanket AGPL ban** — a category-level rejection regardless of how you use it, the way Google's published policy works ("code licensed under the GNU Affero General Public License (AGPL) MUST NOT be used at Google," down to laptop installs, per `opensource.google/documentation/reference/using/agpl-policy`)? No industry-wide figure exists for how common this is — name-check the actual policies of your three accounts, don't assume.
2. **Does your bank's or retailer's specific self-hosted deployment architecture trigger AGPL's network-source disclosure duty for *them*, not just for a hyperscaler** — e.g. many internal users hitting the server over their internal network? Whether that counts as "interacting through a computer network" under AGPL §13 is a real, contested reading, not something this analysis (or any non-lawyer) should assert. Put this in front of counsel who can look at the actual deployment topology.

If either comes back badly, you're proposing to relicense in a way that spooks the two paying accounts you're trying to protect revenue from, not just the hyperscalers.

## Constraints (run this before the board meeting, not after)

- **Dependencies.** Not enumerated here — you need to run this yourself: list every shipped dependency (including transitive), from lockfiles/manifests, and flag any copyleft-incompatible one. A single incompatible dependency in the shipped artifact can veto AGPL outright, discovered the hard way at the first release if skipped now.
- **Contributor consent.** MIT since 2023 with ~4,000 installs implies real external contribution. Unless you already run a CLA (nothing you said suggests one), **every outside contributor whose code is still present must consent to the relicense.** Count them, and figure out who's reachable. Mozilla's Firefox relicense (2001–2006) is the calibration for how long a full-consent campaign takes when it isn't trivial — plan in months, not the days before Friday.
- **Ownership.** If any of the code was written on a hyperscaler's or another employer's time by a past contributor, that's a separate, real complication — route it to counsel rather than reasoning it out yourselves.
- **External rules.** Bank and retailer procurement often filters on OSI approval specifically. AGPL-3.0 is OSI-approved; that's a point in its favor over the source-available alternatives below.

## Postures considered (never just one option)

**A — Stay MIT, monetize by hosting/support/enterprise features.** Zero consent problem, zero fork risk, board gets nothing to point to. Doesn't touch the actual complaint: MIT already lets a hyperscaler ship a managed offering, legally, today. No license stops a well-resourced competitor willing to comply — copyleft redirects competition into compliance work, it doesn't prevent it.

**B — AGPL-3.0, straight relicense.** Closes the resale-without-reciprocity loophole for future releases. This is the FSF's own named default for server software, and it passes the one test that justifies pulling this lever at all: a plausible, *named* competitor (your two hyperscalers) actually attempting the thing AGPL targets. But AGPL alone bets that a hyperscaler will comply (publish their modifications) rather than route around you. The documented precedent says otherwise:

  | Project | Change | What actually happened |
  |---|---|---|
  | Elasticsearch | Apache-2.0 → SSPL/Elastic License (2021) | AWS forked it as OpenSearch |
  | Redis | BSD → RSALv2/SSPLv1 (2024) | AWS and Google backed the Valkey fork |
  | HashiCorp Terraform | MPL-2.0 → BUSL-1.1 (2023) | Linux Foundation shipped the OpenTofu fork within weeks |

  Every one of these was a permissive-to-restrictive move made *specifically* to blunt hyperscaler competition, and every one produced a hyperscaler- or foundation-backed fork of the last open commit, not compliance. With two hyperscalers already building look-alike managed products, they have both the motive and the engineering capacity to do exactly this to your last MIT release — which stays forkable forever no matter what you decide, since published releases keep their original terms permanently.

**C — Source-available (BUSL/FSL/Elastic-License-2.0 style) with an Additional Use Grant covering self-hosted production use.** Surgically targets "don't resell this as a competing hosted service" while explicitly carving out free use for exactly the profile your paying accounts have (self-hosted, not reselling). Softer on your existing customers than AGPL's blanket-ban exposure. But it's not OSI-approved — you cannot call it open source, it may fail your bank's procurement filter outright, and it still provokes the same fork dynamic (moving toward restriction always does) while buying less goodwill than AGPL for the same effect.

**Recommendation: B, but only with the dual-licensing structure below** — A leaves the actual problem untouched; C trades an OSI-approved, well-understood license for a category your bank's procurement may not even recognize, for a narrower benefit.

## License and contribution policy

- **AGPL-3.0** for the server, new releases from a defined version boundary onward. It's OSI-approved (survives procurement filters that source-available options don't) and carries GPL-3.0's patent grant, which MIT doesn't.
- **CLA, introduced at that same version boundary, new contributions only** — existing history grandfathered. State the real reason in the contributing guide: *"we sell a commercial license of this code to customers who can't accept AGPL, which requires rights AGPL alone doesn't give us."* An unexplained CLA reads as a rights grab; a stated one reads as a business decision most contributors accept.
- If you have any officially maintained client libraries/drivers, leave them MIT. Every precedent case's surviving goodwill ran through the permissive pieces left untouched.

## Business model — name it, don't gesture at it

This is sales-led B2B with paying accounts already in hand: **dual licensing** (AGPL for everyone, commercial license for accounts that can't or won't accept AGPL) is the standard structure here — it's what turns "this account's legal team rejected AGPL" from a lost deal into the reason they buy the commercial license instead. Open core is a weaker fit (you'd be arguing about which features move, not defending the core product). Name the two hyperscalers internally in the business case you bring the board — "protect our competitive position" gets shredded in public the way vague sustainability framing did for Redis and HashiCorp; a named, concrete threat is what survives scrutiny.

## Relicensing plan (this is a change, not a fresh pick)

1. Map every outside contributor whose code remains; get consent, plan to rewrite or drop the rest.
2. Fix the version boundary — AGPL binds future releases only. State this explicitly to the board: **the last MIT release is forkable by anyone, forever, starting the day you announce this** — including by either hyperscaler. That's the predictable cost of this move, not a failure mode you can engineer around.
3. Decide what stays MIT (client SDKs, examples, docs) and say so.
4. Prepare your answer for "someone forks the last MIT commit" before you announce, not after — name who'd plausibly lead it and what your response is.
5. Write the announcement now, honestly: what changes, what doesn't, who's affected (with a concrete example), who isn't, why — named, not "sustainability" — and where the last MIT commit lives for anyone who wants to fork it.

## Artifacts once the decision is made

- `LICENSE` (AGPL-3.0, unmodified text) for the server; keep any permissive component's LICENSE separate with a written boundary.
- `SPDX-License-Identifier` headers matching the boundary.
- Collective copyright notice ("Copyright The Kettleworth Authors") rather than a name list.
- Package/registry metadata and container labels updated.
- CONTRIBUTING.md with the DCO/CLA wording and an automated check on every PR — a policy enforced by memory isn't enforced.

## What to actually tell the board Friday

AGPL is defensible and well-precedented for what you're worried about, and the named-competitor test passes — this isn't a restriction with no target. But sell it as what it is: a multi-month consent and rollout project, not a Friday flip; a move that will likely produce a fork rather than compliance from at least one of the two hyperscalers; and a change that needs your bank's and retailer's own policies checked *before* the vote, because the same license line that stops a hyperscaler can just as easily stop your own signed customer's renewal.