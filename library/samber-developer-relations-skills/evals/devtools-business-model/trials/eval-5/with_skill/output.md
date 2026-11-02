# Halyard: relicensing decision and the announcement, corrected

## Read this first: the blog post as described cannot ship

BUSL-1.1 is not an open-source licence, and the gap is checkable in under a minute by anyone who reads it. The Open Source Definition's clause 6 forbids restricting a field of use; BUSL exists specifically to restrict one field of use (competing production hosting). The OSI board rejected the same move by MongoDB (SSPL) in January 2021 in these words: *"the hallmark of a fauxpen source license is that those who made the switch claim that their product continues to remain 'open' under the new license, but the new license actually has taken away user rights."* Redis's own CEO, after the BSD→RSALv2/SSPL move, wrote that the change achieved its anti-hyperscaler goal but "hurt our relationship with the Redis community" — and had to concede in public that the licence wasn't OSI-approved.

If the post says "new open source licence," three things happen in the same week: someone quotes the OSI definition at you, the correction gets more distribution than the announcement, and it fails automated OSI-approved-only checks in the procurement pipelines of exactly the enterprise accounts you're trying to keep. Call it what it is: **source-available**, or **delayed open source** (BUSL converts to an OSI-approved licence at a fixed Change Date — that's the honest and defensible framing). This is a wording fix, not a softer version of the announcement; the content underneath doesn't change.

## Constraints, stated before anything else gets decided

1. **The licence already shipped.** Every Halyard release published under Apache-2.0 stays Apache-2.0 forever. Nothing you do to the next release touches what's already out — including whatever version the cloud provider's "Managed Halyard" is built on. This is the only genuinely irreversible lever in this whole decision, and it's already been pulled, in the other direction, by the first release.
2. **Where it runs.** A distributed queue is server software that customers can self-host or a vendor can run for them — the cloud provider just proved the second half of that by shipping a managed version. That's what makes hosted/source-available levers relevant at all; if Halyard could only ever be self-hosted, none of this would apply.
3. **Who signs.** Two of your biggest accounts already have a hyperscaler sales team in the room. That's an enterprise procurement motion, not a self-serve one — which means whatever you do next has to survive a security/legal review, not just look good in a blog post.

## What relicensing the next release actually buys you against this specific threat

Be precise about the mechanism, because the board's urgency implies this fixes the two accounts in progress. It doesn't, not directly:

- BUSL only binds **future releases**. The cloud provider's current "Managed Halyard" is presumably built on an already-published Apache-2.0 version, which they can keep running, patching, and reselling forever, license-compliant, with zero exposure to whatever you ship next.
- The two accounts currently being worked by the hyperscaler's sales team are being sold *today's* Apache-2.0-licensed product. A licence change on your next release doesn't retract that, doesn't slow that sales cycle, and doesn't appear anywhere in the compliance review those deals are going through this month.
- What it does do: it stops the threat from **compounding**. Every future feature, performance improvement, and bug fix you ship after the Change Date parameters kick in requires a commercial licence for competing hosted use — so the gap between "what the hyperscaler can resell" and "what Halyard actually is" starts widening from this release forward, instead of staying at zero.

So: this is a defensive move with a lag, not a rescue for the two accounts on fire right now. Say that to the board directly — approving it under the belief it stops this quarter's account losses sets up a predictable "why didn't this work" conversation in Q1.

## Sequencing: don't let the slow, irreversible lever be the only move

The reversible and the irreversible responses run in parallel, not in sequence, and they're not interchangeable:

- **Reversible, and the only thing that can actually affect the two accounts in progress**: compete for them now, this quarter, with what the licence change can't touch — a first-party managed Halyard offering (or, faster, a support/SLA/escalation-path contract sold directly to those two accounts), priced and pitched before the hyperscaler's renewal cycle closes. This needs no licence change, no consent-gathering, no waiting — it's a sales and packaging motion you can start this week.
- **Effectively irreversible, and worth exactly one shot**: the licence change. Every documented precedent (Elasticsearch→SSPL, Redis→RSALv2/SSPL, HashiCorp→BUSL) produced a fork within weeks, led by the same class of actor you're worried about. Run it deliberately — consent map, parameters, announcement — not on the two-week clock the board is currently on. A rushed version of an unwalkable decision is the worst combination available here.

## Name the model the licence is supposed to protect

A restrictive licence is not a business model by itself — it's a wall around one, and right now nobody has said what's behind the wall. Pick one before the announcement goes out, because the Additional Use Grant you write depends entirely on the answer:

- **Hosted Halyard Cloud** — you sell the operated service; BUSL's Additional Use Grant explicitly permits self-hosting and internal production use, and only withholds the right to resell Halyard as a competing hosted service. This is the standard shape and it's the one that keeps your current self-hosting users completely unaffected.
- **Commercial licence sold to cloud providers** — closer to dual licensing: the hyperscaler (or any managed-service reseller) pays you for the right to do exactly what they're doing now. Slower to close, but it turns the competitor into a customer instead of just a target for a licence fight.
- **Support/LTS on top of either** — sell the two threatened accounts a contract, independent of which of the above you pick.

The board's framing ("ship BUSL, announce it") skips this. Don't let the announcement go out before this is decided — the Additional Use Grant is the paragraph that determines whether existing large self-hosters get caught in the restriction by accident, and that mistake is the fastest way to turn your own users into the fork's first contributors.

## The relicensing plan, if the board proceeds

1. **Consent map.** Enumerate every contributor whose code is still present in the tree. No CLA on file means no unilateral relicense of their contributions — this is why every documented case (HashiCorp included) applied the new licence to **future releases only**, leaving prior releases and any code you can't get consent for on Apache-2.0 permanently. Budget this in weeks if Halyard has an active external contributor base, not days — Mozilla's Firefox relicensing took from 2001 to 2006 for a fully retroactive case; you don't need that scope here, but don't assume this step is free.
2. **Version boundary.** Next major release (e.g. Halyard vN+1) onward is BUSL-1.1. Everything published up to and including vN stays Apache-2.0 forever, and anyone — including the cloud provider — may fork from that last commit. Plan for that fork, don't be surprised by it.
3. **What stays permissive.** Client SDKs, the wire protocol/API spec, docs, and examples stay Apache-2.0. This is what HashiCorp did (SDKs and APIs stayed MPL) and it's what keeps the client ecosystem — every language binding, every integration — intact instead of fracturing on day one.
4. **BUSL parameters, decided now, not left as boilerplate:**
   - **Change Date**: pick a concrete date ≤4 years out (e.g., 3 years from the vN+1 release date).
   - **Change License**: GPL-2.0-or-later (the standard, and the one every adopter's legal team already knows how to read).
   - **Additional Use Grant**: the load-bearing clause — permit unrestricted self-hosting and internal production use at any scale; restrict only *offering Halyard as a competing hosted/managed service to third parties*. Draft this against the model you picked above, not against "whatever sounds safe."
5. **Expect the fork, name who leads it.** The cloud provider already runs a working managed product off the current Apache-2.0 tree — they are the single most likely party to fork the last permissive commit and keep it alive, alone or via a neutral foundation, exactly as AWS did with OpenSearch and Valkey, and as the Linux Foundation did with OpenTofu. Decide your response before it happens: what differentiates the BUSL line (features, performance, the support contract from the two accounts) from a frozen fork, so the fork isn't simply "free Halyard, forever."
6. **Trademark, separately.** The licence doesn't stop anyone from continuing "Halyard" under its old terms and calling it Halyard. If you haven't already, clear and assert the trademark now — two months' lead time is typical — and check whether the hyperscaler's product name ("Managed Halyard") itself needs a conversation independent of the licence question.

## The announcement, corrected

```markdown
# Halyard licensing change

**What changes** — Apache-2.0 → Business Source License 1.1, effective from Halyard vN+1.
This is a source-available licence, not an open-source licence: it converts automatically
to GPL-2.0-or-later on <Change Date, ≤4 years from vN+1's release>.

**What does not change** — every release up to and including vN stays Apache-2.0, permanently,
and remains forkable by anyone. Client SDKs, the wire protocol, and documentation stay
Apache-2.0 going forward as well.

**Who this affects** — anyone offering Halyard as a hosted, managed service to third parties
without a commercial agreement with us, starting with vN+1.

**Who this does not affect** — every self-hosting user, at any scale, in production, today or
after this change. Running Halyard inside your own infrastructure, or embedding it in your own
product for your own use, is unrestricted under the Additional Use Grant.

**Why** — [named competitor]'s managed offering, launched [date], reuses our API, our work, and
our support burden without a commercial relationship with us. This protects our ability to
build a sustainable [hosted Halyard Cloud / commercial licensing / support] business around the
project we maintain.

**Contributors** — existing contributions remain under their original Apache-2.0 terms.
Contributions to vN+1 and later are made under BUSL-1.1's terms; [state CLA status here].

**Alternatives** — vN, the last Apache-2.0 release, remains available and forkable; here is its
last commit: <link>.
```

Do not swap "source-available licence" for "open source licence" anywhere in this document, including the title, the tags, or the tweet announcing it. The moment it's inconsistent in one place, that's the sentence that gets screenshotted.

## Risks and revisit triggers

- **The fork happens anyway, led by the hyperscaler.** Signal: a competing distribution announced within weeks of the vN+1 release, following the Elasticsearch/Redis/HashiCorp pattern exactly. Response is prepared in the plan above, not improvised.
- **The two accounts leave before the countermeasure lands.** Signal: procurement decision date earlier than your managed-offering or support-contract readiness date — this is why the reversible motion has to start now, independent of the licence timeline.
- **A self-hoster gets caught by an over-broad Additional Use Grant.** Signal: any support ticket or public complaint from an existing large user asking whether their current deployment now needs a commercial licence — this means the grant was drafted against the wrong model in step above and needs republishing, fast, with an apology, not a clarification.
- **The "open source" label ships anyway and gets corrected in public.** Signal: any reply, HN comment, or press mention citing the OSI definition or the SSPL precedent within 48 hours — treat this as certain if the vocabulary fix above isn't made, not as a risk to monitor.