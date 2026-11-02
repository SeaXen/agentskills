## Bottom line

No license switch — not AGPL-3.0, not SSPL, not a BUSL/FSL source-available term — stops this. The problem you're describing (Austin consultancy, "Novaquill Enterprise," prospects confused about affiliation) is a **trademark/passing-off problem wearing a licensing costume.** Relicensing is the wrong instrument, and pulling it would cost you real adoption for zero effect on the actual harm. Here's why, and what to do instead.

## Why a license change can't touch this fork

Two facts eliminate the option before any brainstorming about *which* license:

1. **License changes bind future releases only.** Every version of Novaquill already published under Apache-2.0 stays Apache-2.0 forever — that's not a policy choice, it's how a granted license works. The consultancy's fork was built from code you already handed out under terms that let them use, modify, rebrand, and resell support against it in perpetuity. Relicensing tomorrow's release to AGPL-3.0 does not reach backward and revoke what they already have. They can keep shipping and supporting that exact snapshot indefinitely, untouched by anything you do going forward.

2. **Even prospectively, copyleft doesn't prohibit what they're doing — it just adds compliance conditions.** AGPL's whole mechanism is: if you run a modified version as a network service, you must publish your modifications' source. It does not prevent forking, does not prevent renaming, does not prevent selling support contracts. A consultancy willing to comply (publish their diffs) keeps operating exactly as before, just with a source-disclosure obligation neither of you would ever check. Copyleft "redirects competition into compliance work; it does not prevent it" — and a support-contract reseller is close to the easiest case to comply with, since there's often little proprietary modification to disclose in the first place.

So the strongest license you could move to still produces the same outcome you have today for the fork already in the market — plus it now costs you: relicensing needs the consent of every contributor whose code is still present (6,000 stars implies a real outside contributor base, not just you), and moving *toward* restriction is the documented trigger for a community fork of your own (Elastic → OpenSearch, Redis → Valkey, Terraform → OpenTofu all followed exactly this move). You'd be spending your own community's goodwill to accomplish nothing against the party you're actually trying to stop.

## What actually stops it: trademark, not copyright

The thing the consultancy did that's causing damage isn't "forked and modified your code" — Apache-2.0 explicitly permits that. It's **naming their build "Novaquill Enterprise"** and putting up a landing page that reads, to your own prospects, as if it's you. That's a trademark/brand-confusion question, governed by a completely different body of law than the one your OSS license operates under, and Apache-2.0 already anticipated it:

> Apache-2.0 §6 (Trademarks): the license "does not grant permission to use the trade names, trademarks, service marks, or product names of the Licensor, except as required for reasonable and customary use in describing the origin of the Work and reproducing the content of the NOTICE file."

The code grant and the name grant are separate under the license you already ship. Forking the sidecar is licensed; calling their commercial product "Novaquill Enterprise" is not — that was never inside what Apache-2.0 gave them, license v2 or otherwise.

Two facts specific to your situation are worth documenting now, because they're the kind of evidence that matters in exactly this type of case (I'm naming what's checkable, not predicting an outcome — this is squarely a "get counsel" situation, not one I'll adjudicate):
- **Two of your own prospects independently asked whether you're the same company** — that's actual confusion, not hypothetical likelihood of confusion, and it's the strongest single fact pattern this kind of claim can have.
- Precedent worth knowing about, not relying on unassisted: in the 2025 Synadia/NATS dispute, William Morgan's framing was that Apache-2.0 "lets anyone ship a relicensed version, but the one thing you can't do is call that relicensed thing the original project name." Separately, *Planetary Motion v. Techsplosion* (261 F.3d 1188) established that giving software away for free is still "use in commerce" for trademark purposes — so "it's open source, so trademark doesn't apply" isn't a defense either side gets to lean on.

## Recommended next steps

1. **Talk to a trademark/IP attorney this week** — this is a live dispute with an identified party, which is exactly the line this skill won't cross unassisted. Bring: your Apache-2.0 NOTICE file, whether "Novaquill" is a registered mark or common-law only, the consultancy's landing page and use of the name, and the two prospect interactions as documented confusion evidence.
2. **Check your trademark status now, in parallel** — registered vs. common-law changes what's available (registered gets you into USPTO opposition/UDRP-style tooling; common-law still supports a passing-off/unfair-competition claim, just with a higher evidentiary bar).
3. **A cease-and-desist over the name**, not the code, is very likely your counsel's opening move — it can ask them to keep the fork (that's licensed and fine) while dropping "Novaquill" from their product name and landing page.
4. **Leave the Apache-2.0 license alone.** It isn't the tool for this job, and changing it now would spend trust you don't need to spend.

## If a real relicense reason exists separately, that's a different conversation

If, independent of this dispute, you're also worried about a well-resourced cloud provider reselling Novaquill as a managed service — that's the actual scenario AGPL/BUSL/SSPL address, and it's worth its own sizing (named competitor, business model, contributor consent map). But say so explicitly if that's live; don't let this consultancy incident be the reason you pull that lever, because it's the one problem that lever can't solve.