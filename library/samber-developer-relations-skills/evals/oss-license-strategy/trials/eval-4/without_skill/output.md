# Before the license text and post — three facts that should shape both

**You almost certainly have the legal right to do this without going back to the 47 contributors.** MIT is a permissive license with an explicit sublicensing grant. Under the "inbound=outbound" convention every MIT project runs on, a contributor who sent you a PR licensed *their* contribution to the project under MIT — and MIT lets you redistribute derivative/combined works under different terms, as long as you keep their original copyright and permission notice attached to their code. That's the mechanism that let HashiCorp, Elastic, and others do this without a CLA. It is not the mechanism copyleft relicensing needs — you're fine here specifically because you started MIT.

**But you cannot undo what's already MIT.** Every commit through your last MIT-licensed release stays MIT forever, for everyone who already has it. Anyone — including the competitor — can fork that last commit and keep going under the original terms. This has happened every single time a company has pulled this move: Terraform → OpenTofu, Elasticsearch → OpenSearch, Redis → Valkey. Assume it happens to you too. It's not a legal risk, it's close to a certainty, and the plan below treats it as one.

**The reputational risk outranks the legal risk.** Ambushing 47 people who wrote you free code, via a blog post, is the part that actually burns trust — not the license change itself. Email them before you publish, this week, not as a courtesy but before legal review finishes drafting the Additional Use Grant. Don't put names in the public post without asking first; offer an opt-in contributors' thank-you list instead.

Have actual counsel review the Additional Use Grant scope below before it ships — that clause is where BUSL announcements get contested, and I'm not able to give you that sign-off.

---

## The license: `LICENSE` for Harborloom 4.0 and later

Replace the MIT `LICENSE` file with this, starting at the 4.0 tag only. Every 3.x and earlier tag/branch keeps its existing MIT `LICENSE` file, untouched, permanently.

```
Business Source License 1.1

Licensor:             [LEGAL ENTITY NAME, e.g. Harborloom, Inc.]
Licensed Work:        Harborloom 4.0
                       The Licensed Work is (c) 2026 [LEGAL ENTITY NAME]
Additional Use Grant:  You may use, copy, modify, and create derivative
                       works of the Licensed Work for any purpose,
                       including production use within your own
                       organization or on behalf of your own end
                       customers, PROVIDED THAT you do not, and do not
                       enable a third party to, offer the Licensed Work
                       or a Derivative Work to third parties as a
                       hosted, managed, or "as-a-service" product whose
                       primary value to its users is providing access
                       to the functionality of the Licensed Work —
                       whether offered for a fee or for free, and
                       whether or not modified, rebranded, or combined
                       with other software.

                       Embedding the Licensed Work as a component of a
                       materially different product or service, where
                       running the Licensed Work is not the primary
                       thing you are selling or offering, is not
                       restricted by this grant.

Change Date:           [4.0 RELEASE DATE + 4 years, e.g. 2030-10-22]

Change License:        Apache License, Version 2.0

For information about alternative licensing arrangements for the
Licensed Work, please contact [licensing@harborloom.dev].

Notice

The Business Source License (this document, or the "License") is not
an Open Source license. However, the Licensed Work will eventually be
made available under an Open Source License, as stated in this
License.

License text copyright (c) 2017 MariaDB Corporation Ab, All Rights
Reserved. "Business Source License" is a trademark of MariaDB
Corporation Ab.

-----------------------------------------------------------------------

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
authorized resellers, or you must refrain from using the Licensed
Work.

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
   this License, as the Additional Use Grant, or (b) insert the text
   "None".

3. To specify a Change Date.

4. Not to modify this License in any other way.
```

**Two spots for you to decide, not me:**

1. *Apache 2.0 as the Change License technically isn't GPLv2-compatible*, so strictly it breaks Covenant #1 above. In practice this doesn't stop anyone — Sentry and CockroachDB both ship BUSL with Apache 2.0 as the change license and nobody has enforced the covenant against them — but flag it to counsel rather than assume it's fine.
2. *Consider a small-company carve-out* in the Additional Use Grant (e.g., "organizations with fewer than 25 employees and under $1M ARR may offer a hosted Harborloom service"). This is what lets you say "we're not going after solo devs and small shops, we're going after funded competitors" — worth deciding before publish, because the post below is much easier to write if that line exists.

---

## The blog post

**Title: A license change for Harborloom 4.0**

Harborloom has been MIT-licensed since the first commit. Forty-seven people outside our own team have sent us code that's still running in production today, for free, with no contract asking them to. That's the project we set out to build, and it's the reason Harborloom exists at all.

With version 4.0, we're changing the license going forward. New code, starting at 4.0, ships under the Business Source License 1.1 (BUSL), not MIT. Every version up to and including 3.x stays exactly as it is — MIT, forever, no exceptions, no retroactive change. If you're running 3.x today, nothing about your rights to that code changes tomorrow, next year, or ever.

**Why we're doing this**

Since June, a managed version of Harborloom — built on our code, maintained by a team that has contributed approximately none of it back — has been winning deals against us. Prospects run a bake-off, find our own software running under someone else's logo with a support contract attached, and buy that instead of talking to us. We built this project. We pay the people who maintain it, review the PRs, write the docs, and answer the issues. A well-funded, hosted-only imitation is what BUSL is built to stop, and it's the reason MongoDB, Elastic, HashiCorp, Sentry, CockroachDB, and a growing list of others made the same call before us.

**What doesn't change**

- Reading the source. Forking it. Modifying it. All still true, starting the day 4.0 ships.
- Running Harborloom in production, for yourself or for your own customers, self-hosted or on your own infrastructure. Still free, no license purchase required.
- Contributing. We still want your PRs, and we still review and merge them.
- Every release through 3.x. MIT, permanently, no strings retroactively attached.

**What does change**

If you want to offer Harborloom itself, or a derivative of it, to third parties as a hosted or managed product — competing directly with what we sell — that now requires a commercial agreement with us. That's the entire scope of the restriction. It's not aimed at people running Harborloom to power their own product; it's aimed at reselling Harborloom-as-a-service without a relationship with us.

**And BUSL isn't "closed source"**

Four years after each release, that version automatically converts to Apache 2.0 — a fully open license, no action required on our part or yours. We don't have to remember to open it up later; the license itself guarantees it. Source stays visible the entire time, before and after conversion. What changes is who's allowed to resell it as a service in the interim, not who's allowed to read or run it.

**To the 47 of you who sent us code**

We're reaching out individually before this post goes up, because you deserve to hear it from us directly, not read it here first. Your contributions are staying exactly where they are, under the license you sent them under, with your name attached. If you'd like to be named publicly as a contributor to the project, tell us and we'll add you to a page for it — we won't do that without asking.

Going forward, new contributions will go through a Developer Certificate of Origin (sign-off on each commit, no paperwork, no lawyers) so provenance stays unambiguous for everyone, including us. This isn't retroactive and it isn't a hoop — it's a one-line `git commit -s`.

**We know how this reads**

We expect some of you to be unhappy about this, and some of you to fork the last MIT release and keep going without us. That's allowed, it's expected, and it's the honest tradeoff of the license we started with. We'd rather say that plainly than pretend everyone will be fine with it. What we're optimizing for is a version of Harborloom that still has a team behind it in five years — and right now, that requires closing the specific gap a hosted competitor is exploiting, not the whole front door.

We'll be at [user conference] in [month]. Come find us if you want to talk about this in person — we'd rather have that conversation face to face than in a comment thread.

**FAQ**

*Do I need to do anything to my existing Harborloom install?* No. Nothing changes for 3.x. Upgrading to 4.0 doesn't retroactively change your rights to versions you're already running.

*Can I still fork 4.0?* Yes — BUSL is source-available, not source-restricted. You can copy, modify, and redistribute it. The one thing you can't do is run it as a hosted service for third parties without a commercial agreement with us.

*What if I'm a small team offering Harborloom hosting to a handful of customers?* [Fill in once the carve-out threshold above is decided — either "you're covered under our Additional Use Grant, no action needed" or "reach out, we'll work something out."]

*Is this permanent?* No. Each release converts to Apache 2.0 automatically four years after it ships. 4.0 converts on [date].

*Why not just add a CLA and stay MIT?* A CLA controls future contributions; it doesn't stop someone from re-hosting code that's already MIT-licensed. It wouldn't have solved the problem we actually have.

---

## The four weeks, compressed

- **Week 1 (now):** Legal reviews the BUSL parameters above, especially the Additional Use Grant scope and the small-company carve-out decision. In parallel, email all 47 contributors individually — this has to happen before anything public, so start it in parallel with legal, not after.
- **Week 2:** Finalize license text and carve-out. Update every `LICENSE` file, source header, and packaging manifest for the 4.0 branch only. Stand up a DCO check on new PRs. Draft the docs FAQ page. Brief your support/community team on likely questions so they're not caught flat-footed.
- **Week 3:** Send the finalized post to anyone under embargo you want to pre-brief (analysts, key customers, close contributors). Lock the conference talking points. Confirm the change-date math against the actual 4.0 ship date.
- **Week 4:** Publish the post the same day 4.0 ships. Staff Discord/GitHub Discussions/issues that day and the next — this generates volume fast. Expect a fork announcement within days; have a one-paragraph, non-defensive response ready rather than writing one under pressure.