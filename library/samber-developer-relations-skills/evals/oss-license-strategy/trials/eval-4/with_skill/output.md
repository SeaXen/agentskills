# Harborloom: MIT → BUSL-1.1 for 4.0

Using `oss-license-strategy`. This is a **Step 6** job (relicensing an existing project), run with **Step 1** first — you've already picked the posture (commercial optionality) and the license (BUSL-1.1), so I'm not re-running the full Step 2 brainstorm; I validate the choice in one paragraph and move straight to the change plan. Where a fact isn't in your message (legal entity name, competitor's name, conference date, repo layout), it's a bracketed placeholder — fill it in before anything ships.

## The one finding that has to land before the artifacts

**47 outside contributors, code still in the tree, inbound=outbound only, nothing ever signed.** Per this skill's relicensing playbook: *"Every copyright holder whose code is still present must consent, unless a contributor agreement already granted the right."* You have no such agreement. That's not a formality — it's the actual legal mechanism a fork challenge or a disgruntled contributor would use against you, and it's precisely the scenario Mozilla spent 2001–2006 resolving for Firefox.

Four weeks is enough time to *announce* the change. It is not enough time to get affirmative, defensible consent from 47 people, some of whom you may not have live contact info for. I'm not going to pretend otherwise. Two honest paths:

- **Slip the date** and run consent-gathering properly first (months, per Mozilla's own precedent).
- **Ship on the 4-week date anyway**, scoped and risk-managed: relicense prospectively only, start contributor outreach today in parallel, get counsel to sign off on a stated risk-acceptance policy for non-responders, and keep the door open to rewrite/revert specific contributions that a contributor actively objects to.

Given "before the user conference" reads as a fixed external constraint, I'm building the plan around the second path — but say this to your co-founders as a decision they're making, not a detail I smoothed over. This is exactly the kind of call this skill won't make for you: get an actual lawyer to bless the "silence after a stated deadline = we proceed" default before you rely on it. I can structure the process defensibly; I can't tell you it's risk-free.

## Step 1 — Constraints

- **Dependency licenses**: not yet audited here — I don't have your manifests. Run it before you finalize anything: enumerate every shipped dependency (transitive included), separate build/test-only from shipped, flag anything copyleft. One relief: the Change License in BUSL applies only to *your* codebase, not to your dependencies — they keep their own terms regardless of what you pick.
- **Ownership**: assume the 47 are individual contributors on their own time unless you know specific ones were sponsored by an employer — if so, route those specifically to counsel, don't guess at their employment contracts.
- **Contributor consent**: the load-bearing constraint above. Only contributors whose code is *still present* (verified by `git blame`/`git log --follow` against the current tree, not the full historical list of 47) actually need to sign off — some of the 47 may have had their patches fully superseded since. Run that narrowing first; it may cut the real number meaningfully.
- **Trademark**: not mentioned, so flagging it as its own gate. A relicense provokes forks (see below); a fork can reuse your code under the old MIT terms but cannot call itself "Harborloom" only if the mark is actually cleared and enforceable. Check this now, in parallel — it's cheap and it's the thing that stops "Harborloom Community Edition" from confusing your own sales pipeline.
- **No foundation, no procurement allowlist mentioned** — noted as "none known," not "none exists." If any current customer's procurement process requires OSI-approved-only, BUSL will fail that filter; confirm none of your live deals depend on it before you ship.

## Step 2/3 — Why BUSL-1.1, briefly, since you've already decided

Your actual problem — a managed competitor reselling your engine and winning deals — is a hosted-resale problem, not a "won't publish their modifications" problem. AGPL would only make the competitor publish their source; it would not stop them from operating the competing service or winning the deal. BUSL lets you flatly require a commercial license for that specific use, which is the lever that addresses what you named. That's the right call for this situation, not just the popular one.

## Step 4 — Contribution policy going forward

You're at rung 1 (nothing) today, which is exactly what created this problem, and you're about to have a real reason (commercial optionality) to move up:

- **Add a DCO now**, effective at the 4.0 boundary, for every future contribution — near-zero friction, gives you the provenance trail you don't currently have for any of the 47.
- **Add a narrow CLA for future contributions to the BUSL-covered code only**, with the reason stated in the contributing guide, not hidden:

  > Why we ask: we license commercial use of this project outside the Additional Use Grant, which needs rights our license alone doesn't give us. Signing grants us a license to your contribution — you keep your copyright and can use your own work anywhere else.

- If you keep any client libraries/SDKs/examples on MIT (recommended below), those stay on the DCO only — no CLA needed where you're not asking for relicensing rights.
- This is the fix that stops this exact problem recurring at 5.0.

## Step 6 — The relicense plan

**Who must consent**: every one of the 47 whose code survives in the current tree. Build the list from `git blame` on the 4.0 branch, not from PR history — that's the set the playbook actually requires.

**Outreach mechanism** (start this today, in parallel with drafting):
- One message per contributor (issue comment or the email tied to their commits), asking for one of three answers within a stated deadline: consent to relicense their historical contribution under BUSL-1.1, decline, or no response.
- **Decline or no-response by the deadline → that contribution is rewritten or removed from the 4.0 (BUSL) tree before release**, and stays available forever in the last MIT release for anyone who wants it, including the departing contributor. Don't ship code under BUSL that a contributor actively declined to relicense — that's the one move this skill's playbook treats as indefensible, versus "we tried to reach them and couldn't."
- Get counsel to bless the "no response = treated as decline, code gets swapped out" default in writing before you rely on it operationally.

**Version boundary**: 4.0 and forward only. Every 1.x/2.x/3.x release stays MIT permanently — that's not a policy choice, it's how licensing works; anyone can fork from the last MIT commit today regardless of what you do next. Say this plainly in the announcement rather than let someone else say it first.

**What stays permissive**: if you ship separate client libraries, SDKs, language bindings, or examples/docs as distinct packages, leave those on MIT. That's what keeps integrations working and keeps the ecosystem from feeling like a single closed-off move — and it's what HashiCorp, the closest precedent here, did with its SDKs and APIs. If Harborloom is a single monolithic engine with no separable client surface, say so and this line doesn't apply — confirm your repo layout before the announcement locks it in.

**Prepare for the fork.** Given MIT + copyleft precedent (Elastic → OpenSearch, Redis → Valkey, HashiCorp → OpenTofu), expect one. You won't know who leads it in advance, but decide now: will you accept PRs back from a hostile fork, will you keep contributing fixes to the last-MIT branch, what do you say publicly when it's announced. A vendor caught flat-footed by the predictable response reads as having not thought this through — don't be that.

**4-week execution plan**:

| Week | Dates (from 2026-09-24) | Work |
|---|---|---|
| 1 | 09-24 → 10-01 | Narrow the 47 to actual current-tree contributors. Send consent outreach with a 2-week deadline. Run the dependency audit. Draft LICENSE, CONTRIBUTING changes, announcement. Kick off counsel review — this is the "contested contribution" moment the skill says needs a lawyer, not this document. |
| 2 | 10-01 → 10-08 | Counsel sign-off on the risk-acceptance policy for non-responders. Confirm trademark status. Finalize Additional Use Grant wording. |
| 3 | 10-08 → 10-15 | Consent deadline lands mid-week. Rewrite/remove any declined or unresolved contributions from the 4.0 branch. Cut RC, tag the last-MIT commit clearly. |
| 4 | 10-15 → 10-22 | Ship 4.0, publish LICENSE + CONTRIBUTING, publish the announcement, monitor and respond — expect an HN/Reddit thread given precedent, and expect it to be hostile regardless of how well you handled consent. |

## Step 7 — Artifacts

### `LICENSE` (root, unmodified BUSL-1.1 text, parameters filled in)

```
Business Source License 1.1

Parameters

Licensor:             [Harborloom, Inc. — confirm exact legal entity name]
Licensed Work:        Harborloom 4.0
                       The Licensed Work is (c) 2026 [Harborloom, Inc.]
Additional Use Grant:  You may use, copy, modify, and run the Licensed
                       Work for any purpose, including production use
                       within your own organization or on behalf of
                       your own customers, provided that you do not
                       offer the Licensed Work, or a Competing Offering,
                       to third parties as a hosted or managed service.

                       A "Competing Offering" is a product offered to
                       third parties, including via paid support, that
                       provides substantially the capabilities of
                       Harborloom's paid hosted offering(s), whether the
                       Licensed Work is used alone or embedded within
                       another product or service.

Change Date:           The fourth anniversary of the first publicly
                       available distribution of this version of the
                       Licensed Work.

Change License:        GNU General Public License v2.0, or any later
                       version.

Terms

The Licensor hereby grants you the right to copy, modify, create
derivative works, redistribute, and make non-production use of the
Licensed Work. The Licensor may make an Additional Use Grant, above,
permitting limited production use.

Effective on the Change Date, or the fourth anniversary of the first
publicly available distribution of a specific version of the Licensed
Work under this License, whichever comes first, the Licensor hereby
grants you rights under the terms of the Change License, and the
rights granted in the paragraph above terminate.

If your use of the Licensed Work does not comply with the requirements
currently in effect as described in this License, you must purchase a
commercial license from the Licensor, its affiliated entities, or
authorized resellers, or you must refrain from using the Licensed Work.

All copies of the original and modified Licensed Work, and derivative
works of the Licensed Work, are subject to this License. This License
applies separately for each version of the Licensed Work and the
Change Date may vary for each version of the Licensed Work released by
Licensor.

You must conspicuously display this License on each original or
modified copy of the Licensed Work. If you receive the Licensed Work
in original or modified form from a third party, the terms and
conditions set forth in this License apply to your use of that work.

Any use of the Licensed Work in violation of this License will
automatically terminate your rights under this License for the current
and all other versions of the Licensed Work.

This License does not grant you any right in any trademark or logo of
Licensor or its affiliates (provided that you may use a trademark or
logo of Licensor as expressly required by this License).

TO THE EXTENT PERMITTED BY APPLICABLE LAW, THE LICENSED WORK IS
PROVIDED ON AN "AS IS" BASIS. LICENSOR HEREBY DISCLAIMS ALL WARRANTIES
AND CONDITIONS, EXPRESS OR IMPLIED, INCLUDING (WITHOUT LIMITATION)
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE,
NON-INFRINGEMENT, AND TITLE.

MariaDB hereby grants you permission to use this License's text to
license your works, and to refer to it using the trademark "Business
Source License", as long as you comply with the Covenants of Licensor
below.

Covenants of Licensor

In consideration of the right to use this License's text and the
"Business Source License" name and trademark, Licensor covenants to
MariaDB, and to all other recipients of the licensed work to be
provided by Licensor:

1. To specify as the Change License the GPL Version 2.0 or any later
   version, or a license that is compatible with GPL Version 2.0 or a
   later version, where "compatible" means that software provided
   under the Change License can be included in a program with software
   provided under GPL Version 2.0 or a later version. Licensor may
   specify additional Change Licenses without limitation.

2. To either: (a) specify an additional grant of rights to use that
   does not impose any additional restriction on the right granted in
   this License, as the Additional Use Grant; or (b) insert the text
   "None".

3. To specify a Change Date.

4. Not to modify this License in any other way.

Notice

The Business Source License (this document, or the "License") is not
an Open Source license. However, the Licensed Work will eventually be
made available under an Open Source License, as stated in this
License.

For more information on the use of the Business Source License for
MariaDB, see the Business Source License FAQ at
mariadb.com/bsl-faq-adoption.
```

SPDX identifier: `BUSL-1.1`. Ship a matching `SPDX-License-Identifier: BUSL-1.1` header on every file in the BUSL-covered tree; keep `SPDX-License-Identifier: MIT` on anything you're leaving permissive. Update package/registry metadata license fields and any container image labels to match.

### `CONTRIBUTING.md` addition

```markdown
## Licensing

Harborloom 4.0 and later ship under the Business Source License 1.1.
Releases through 3.x remain under MIT permanently.

New contributions require:
- A DCO sign-off (`git commit -s`) on every commit.
- A one-time Contributor License Agreement, because we sell a
  commercial license of this project outside the terms of the
  Additional Use Grant — that requires rights the BUSL alone doesn't
  give us. You keep your copyright; you can use your own work anywhere
  else.

A missing sign-off fails CI. Fix it with `git commit --amend -s`
(single commit) or `git rebase --signoff <base>` (several).
```

### Consent request to the 47 (template, one per contributor)

```
Subject: Harborloom 4.0 licensing change — action on your past contribution

Hi [name],

Harborloom is moving from MIT to the Business Source License 1.1
starting with version 4.0 ([target date]). Everything through our
last MIT release stays MIT forever — nothing about that changes, and
you can always use or fork that code under those original terms.

Your PR(s) [links] are still present in the 4.0 tree, and MIT alone
doesn't give us the right to carry your code forward under new terms
without your OK. Three options, by [deadline, 2 weeks out]:

1. Reply "I consent" — your contribution moves into 4.0 under BUSL-1.1
   like the rest of the codebase.
2. Reply "I decline" — we'll rewrite or remove that code from the 4.0
   branch before release. It remains available to everyone, including
   you, under MIT in our last 3.x release.
3. No reply by the deadline — we'll treat this the same as declining,
   for the same reason: we'd rather lose a few lines of code than ship
   something you didn't agree to.

Full context on why we're doing this: [link to announcement/draft].

Thanks for the code — it's why this project exists at all.
```

## The blog post

```markdown
# Harborloom 4.0: what's changing, and why

Starting with Harborloom 4.0, on [target date], new releases ship
under the Business Source License 1.1 (BUSL-1.1) instead of MIT.
Every release through [last 3.x version] stays MIT — permanently, no
exceptions, and you can fork from that last commit
([commit hash]) at any time.

## What changes

Under BUSL-1.1, you can still do almost everything you do today for
free: run Harborloom in production, modify it, embed it in your own
product, use it at any scale, for your own organization or on behalf
of your customers.

The one thing the license reserves is this: offering Harborloom
itself — or a product that competes with our own hosted offering — as
a managed or hosted service to third parties requires a commercial
license from us.

Four years after each release, that release automatically converts to
GPL-2.0-or-later. This isn't a permanent lock — it's a delay.

## What doesn't change

- Every release up to and including [last 3.x version] stays MIT,
  forever. Nothing retroactive.
- [Client SDKs / API bindings / examples / docs, if kept permissive]
  stay MIT.
- Self-hosting, embedding, modifying, running Harborloom internally at
  any company size — all still free, no commercial license needed.

## Why

[Competitor] launched a managed Harborloom offering in June 2026 and
has been winning deals against us, using our own code, without
contributing back or paying for it. That's the specific situation
this addresses — not a general worry about "sustainability," a named
competitive fact.

We looked at AGPL first. It would only require [Competitor] to publish
their modifications — it wouldn't stop them from operating the
competing service or change which deals we win. BUSL lets us require
a commercial license for exactly that use, which is the thing that
actually matters to us.

## Who this affects

Anyone who wants to resell Harborloom, or a product that competes with
our hosted offering, as a service to third parties. If that's you,
[talk to us about a commercial license / link].

## Who this doesn't affect

The overwhelming majority of our users: anyone self-hosting for
internal use, anyone embedding Harborloom in their own non-competing
product, every individual developer running it locally or in their
own infrastructure. If you're not selling access to Harborloom itself,
nothing changes for you.

## About existing contributions

47 people outside Harborloom have contributed code that's still in our
tree. We never had a contributor agreement, so we've reached out to
each of them individually to ask permission to carry their code
forward under the new terms. Where we couldn't reach someone or they'd
rather not, we've rewritten or removed that code from 4.0 — it remains
available to everyone under MIT in [last 3.x version].

Going forward, new contributions need a DCO sign-off and a lightweight
CLA — the reason is in our contributing guide, not hidden in fine
print: we now sell a commercial license, which needs rights our
license alone doesn't grant us.

## If you'd rather not move with us

That's a legitimate choice. [Last 3.x version] is MIT, forever, at
commit [hash]. Fork it. We mean that plainly, not as a dare — some of
our own contributors may choose to.

Questions: [contact].
```

## Open items — get these answered before you ship, not after

- Legal entity name for the Licensor field, and jurisdiction, for counsel to finalize the Additional Use Grant / "Competing Offering" wording — that definition is the whole license in practice and deserves an actual lawyer's pass, not mine.
- Confirm repo layout: is there a separable client/SDK surface to leave on MIT, or is this one monolithic tree?
- Trademark status on "Harborloom" — check now.
- Competitor's actual name and whether you're willing to name them publicly (recommended — vague framing gets read as evasion and picked apart within hours, per every documented precedent here).
- Exact conference date, to confirm the 4-week window actually clears it with room for the RC/testing cycle above.

**Revisit this decision if**: the consent-gathering surfaces a contributor who owns a meaningfully large, load-bearing chunk of the codebase and declines (that may force a bigger rewrite than a 4-week window can absorb); a credible fork gains real traction; a target account's procurement explicitly bans non-OSI licenses; or four quarters post-launch the commercial license has produced no revenue against the named competitor, at which point BUSL bought you nothing but the fork.