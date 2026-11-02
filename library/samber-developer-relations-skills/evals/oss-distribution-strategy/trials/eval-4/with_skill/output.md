⚠️ Before the deliverable: the literal ask — "prove this grows downloads" — isn't supportable, and I'm not going to fabricate a download-lift case. The skill I followed (`oss-distribution-strategy`) is explicit on exactly this question: *"Will an OpenSSF Scorecard above 7 grow our downloads? No evidence supports that. Sell it internally as procurement enablement."* Sigstore's own adoption numbers have no control group, independent Feb-2026 sampling found only 76 of 1,059 npm packages carrying provenance despite native tooling support, and the Scorecard research literature (Zahan et al., ICSE-SEIP 2023) measures vulnerability reduction, never downloads. Pitching signing/SBOM/Scorecard as a growth initiative sets up the next security budget ask to fail when the download graph doesn't move — for reasons that have nothing to do with whether the work was worth doing.

The good news: you don't need the downloads argument. Girder's adopter base — banks and insurers — is exactly the segment where this work has a real, evidence-backed mechanism. Below is the case, built to be pasted into a doc or slide for your VP.

---

# The case for cosign, SLSA, SBOM and Scorecard 7+ on girder

## Don't pitch this as growth. Pitch it as unblocking the growth you already have.

Girder does 180k monthly downloads on Maven Central with a user base concentrated in banks and insurers. That combination means the binding constraint on adoption in your actual segment isn't discovery — those users already found you — it's **procurement**. In regulated-industry engineering orgs, an artifact proxy, dependency-review tool, or security review board can block an install outright, independent of whether the developer who wants to use girder is convinced. That's a different failure mode than "nobody's heard of us," and it doesn't show up in a download graph until it's too late — it shows up as a security questionnaire that never gets answered, an evaluation that goes quiet, or an existing account that fails to expand usage because a second team's compliance review stalled.

**The mechanism, not vibes:** Larios Vargas et al. (ESEC/FSE 2020, 115 practitioners) found the top-rated "highly influential" factors in dependency selection are maturity/stability (62%), license clarity (45%), and active maintenance (44%) — three of the four things this work makes verifiable without anyone having to ask. That study is about what practitioners *say* they weigh, not proof of a causal adoption effect — cite it as evidence of stated evaluator priorities, not as a download forecast. In a bank or insurer, "highly influential" usually isn't even the individual developer's call — it's a review board's, which is the whole reason legibility (can an approver verify license, versioning, security contact and release rhythm without asking anyone) matters more here than in a typical OSS adoption path.

## The regulatory clock is real and it's pointed at your actual users

This isn't a hypothetical compliance angle — it's dated, and it lands on the companies you already listed as your adopters. The EU Cyber Resilience Act's reporting obligations start **September 2026**; SBOM technical documentation becomes enforceable **December 2027**. Those obligations bind manufacturers — and banks and insurers embedding girder in products they ship are manufacturers under CRA. OpenSSF's own framing (Christopher Robinson) predicts this lands on upstream maintainers as a wave of fix-request and SBOM-request pressure from exactly these downstream companies, not as direct legal liability. You should expect that pressure to hit girder's issue tracker starting soon whether or not you fund this now — the two-week ask is about being ready for it in a controlled sprint instead of an unplanned scramble that costs more later and looks reactive to the accounts you most want to keep.

## What "success" actually looks like — and what it doesn't

Track these, not raw Maven Central downloads:

- **Stalled evaluations that resume.** If you can get even an informal read from field/sales/support on which named accounts have gone quiet mid-evaluation or mid-security-questionnaire, that's your real before/after signal. Baseline it now, before starting the work.
- **Security-questionnaire and procurement-gate turnaround time**, for the accounts where you have visibility into it.
- **Scorecard score above 7 with green attestations** — this is a self-set procurement bar this skill (and the wider industry practice it's drawn from) adopts for enterprise review, not a published standard and not an adoption forecast. Say that explicitly if your VP asks where "7" comes from — it's a defensible posture, not a magic number.
- **Growth in named companies on a "used by" page**, if you don't already have one. This is the actual distribution lever hiding inside this ask: Geoffrey Moore's *Crossing the Chasm* mechanism is that pragmatic buyers want peer references from their own segment, and none exist until someone visibly goes first. One named bank or insurer on that page is worth more to the next pragmatic buyer than a thousand anonymous Maven Central pulls — and it's a natural byproduct of doing this work well (ask a design-partner account if they'll be named once they clear their own review using it).

What this will *not* move in any attributable way: the 180k/month number itself. That figure is dominated by CI pulls, transitive resolution, and mirrors — none of which a security posture changes. Don't let the VP conversation anchor on it; if you do, you'll be asked in six months why the number didn't move, and that conversation is worse than the one you're having now.

## The two weeks, mapped to what actually earns the "7"

- **Cosign keyless signing (Sigstore)** on release artifacts — closes the "can an approver verify artifact provenance" gap.
- **SLSA provenance attestation** in the release pipeline.
- **SBOM per release** (SPDX or CycloneDX, generated in CI, not hand-maintained) — this is the one piece with a hard external deadline attached (CRA, Dec 2027), so it's the least discretionary line item.
- **Scorecard remediation** — pull the actual 18-check breakdown and fix what's cheapest first (branch protection, pinned dependencies, dependency-update automation, SAST are usually the fastest points from a 4.2 baseline).
- **`SECURITY.md` with a real disclosure path and SLA** — cheap, and it's the piece that converts unplanned fix-request pressure into a process you control instead of one that controls you.

Cost shape to set expectations correctly: this is a concentrated one-time setup, but signing keys, SBOM generation and the Scorecard score all need low-but-nonzero recurring maintenance after the two weeks — minutes to a couple hours per release, not zero. A lapsed signing pipeline is worse than never having one (it fails downstream builds), so budget a named owner for the recurring piece before you start, not after.

## The line to use with your VP

*"This won't move our download count — nothing in the published research links signing or SBOMs to adoption volume, and I'm not going to claim it will. What it does is remove the procurement blocker that's the actual constraint on growth in our segment: banks and insurers are the buyers most likely to have a review board that can silently kill a deal we never hear about. Two engineer-weeks now, against a dated regulatory deadline (EU CRA, SBOM enforcement Dec 2027) that's going to generate fix-request pressure from these same accounts regardless of what we decide. I'd rather spend it as a planned sprint than an emergency response to our first blocked renewal."*