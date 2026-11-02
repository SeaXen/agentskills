I attempted to pull fresh citations (OpenSSF/FINOS/regulatory sources) but web search wasn't granted in this session, so what follows draws on stable, well-documented facts (regulations, tool mechanics) rather than fabricated stats. I've flagged the two or three numbers you should re-verify before the meeting.

---

# The case for hardening girder's supply chain: a business memo for your VP

## The one-line ask

Two engineer-weeks to add cosign signing, SLSA provenance, a per-release SBOM, and take the OpenSSF Scorecard from 4.2 to 7+ — framed as **defending the existing 180k/month against a regulatory-driven churn risk, and removing an automated elimination gate on new adoption**, not as a marketing campaign.

## Reframe "grows adoption" before you walk in

Don't promise a download-count lift. Nobody can causally attribute a % of Maven Central pulls to a Scorecard score, and a VP of Engineering will smell an unfalsifiable claim immediately — it costs you credibility on everything else in the pitch. What you *can* argue, concretely:

1. **This defends the 180k you already have.** Banks and insurers don't choose to stop using a library — their AppSec/TPRM function forces the migration when the library fails a compliance bar they didn't set. That's a downside risk to existing revenue-adjacent usage, not a growth opportunity you're speculating about.
2. **This removes a binary elimination gate on new adoption.** At a bank, a library doesn't lose a "which is better" technical bake-off — it gets dropped from the shortlist before anyone evaluates the API, because an automated OSS-intake tool or a manual security questionnaire flagged it first. Girder never gets a chance to compete on merit.
3. **This compresses the security-review cycle**, which is the actual bottleneck between "an engineer at Bank X wants to `import` girder" and "it ships to prod." Faster yes = more conversions from evaluation to production use, which is where download growth would actually show up if it shows up at all.

That's the pitch: risk mitigation on the base, plus unblocking a funnel stage that today silently kills adoption you never hear about.

## Why this is already happening to your users, not hypothetical

- **EO 14028** (US, 2021) requires SBOMs for any software sold to the federal government — this set the NTIA minimum-elements SBOM format (CycloneDX/SPDX) as the de facto standard every downstream vendor questionnaire now copies, including bank and insurer procurement templates that were never federal to begin with.
- **DORA** (EU Digital Operational Resilience Act, in force since Jan 17, 2025) requires EU financial entities to maintain a register of ICT third-party dependencies and manage supply-chain risk for anything supporting a critical function. A bank's compliance team now has a regulatory mandate to know exactly what's in girder and whether it's verifiably what it claims to be.
- **EU Cyber Resilience Act (CRA)** phases in reporting obligations and requires manufacturers of "products with digital elements" to produce an SBOM (Annex I). Even where CRA exempts individual OSS maintainers directly, it obligates the *commercial software* your bank/insurer users ship — which means their compliance teams push the SBOM requirement down onto every dependency, girder included.
- **FINOS** (the Fintech Open Source Foundation, founded by banks including Morgan Stanley, with Goldman Sachs/Citi/others as members) exists specifically because large financial institutions standardize how they vet OSS before internal approval — it's a credible signal that this isn't one bank's idiosyncratic policy, it's an industry-wide pattern among exactly your user base.

None of this requires girder to do anything — it's already reshaping what your bank and insurer users are required to ask their vendors, including OSS ones. The two engineer-weeks is the difference between girder answering those questions with a link, or with an email thread that takes three weeks and might not resolve in your favor.

## The mechanism that actually touches downloads

Modern SCA/dependency-risk tools (Snyk, JFrog Xray, Black Duck, Endor Labs, Socket, Sonatype's own Nexus IQ/OSS Index, GitHub's supply-chain features) increasingly ingest OpenSSF Scorecard results, SLSA provenance, and signature verification as inputs to automated risk scoring — this is how a growing share of enterprises now gate *which* OSS versions get pulled into a build at all, not just which get manually reviewed. A library that scores well shows up green; one that doesn't triggers a manual review queue that most engineers just route around by picking an alternative. This is the concrete, mechanistic link between the score and adoption — not "higher score feels more trustworthy," but "higher score is a literal pass condition in tools your users already run."

## Mapping the 2 weeks to the actual Scorecard math

Scorecard is a weighted average across ~18 checks (0–10 each, critical/high/medium/low weighted). Before committing the plan, have someone run `scorecard --repo=github.com/<org>/girder` (or pull the cached result from `deps.dev`) to see girder's actual per-check breakdown — I don't have live access to your repo, so don't let me guess which checks are dragging you to 4.2. That said, the checks this scope should move, roughly in order of leverage:

| Check | Weight | What moves it |
|---|---|---|
| Signed-Releases | High | cosign + SLSA provenance directly — likely your single biggest jump, since unsigned releases probably score near 0 today |
| Token-Permissions | High | least-privilege CI tokens — config-only, cheap |
| Dangerous-Workflow | Critical | fix script-injection risk in CI YAML — config-only, cheap |
| Pinned-Dependencies | Medium/High | pin CI actions/deps by hash — largely automatable |
| Branch-Protection | High | repo setting, zero engineering cost — do this before the sprint even starts |
| Security-Policy | Medium | add `SECURITY.md` — trivial |
| SAST | Medium | add CodeQL (or equivalent) to CI — cheap |
| CII-Best-Practices badge | Low | self-certification form, near-zero cost |
| Vulnerabilities / Maintained / Code-Review | High | likely already fine for an actively maintained, active-PR project — verify, don't assume |

Several of the highest-weighted checks are configuration work, not deep engineering — that's *why* 4.2→7+ is credible in two weeks, and worth saying explicitly, because it shows the ask is tightly scoped rather than padded.

**Caveat on SBOM specifically**: Scorecard does not currently score SBOM presence as a dedicated check (worth confirming against the live check list at scorecard.dev before you finalize scope, in case that's changed). SBOM's payoff is separate from the Scorecard number — it's what lets a bank's compliance team populate their DORA ICT asset register or answer a CRA-driven vendor questionnaire without emailing you. Present it as a second, independent lever, not as another Scorecard point.

## What to measure instead of raw downloads

Raw Maven Central downloads will be too noisy and too lagging to prove anything in the timeframe your VP will want an answer. Propose tracking, before and after:

- The Scorecard number itself (objective, cheap to check weekly).
- Count of inbound "do you sign releases / do you have an SBOM / can you fill out this security questionnaire" issues or emails — this is your friction proxy, and a drop here is a direct, attributable win.
- Time-to-resolution on those threads, if you can measure it.
- New GitHub orgs/repos from known finance-sector domains appearing as dependents (GitHub's "Used by" / dependency graph) after the change ships.
- Whether any specific stalled enterprise adoption (if you know of one) unblocks.

Tell her upfront this is the measurement plan — it signals you're not going to come back in a quarter with a cherry-picked download graph and call it proof.

## Objections to pre-empt

- **"Prove it grows downloads."** It won't be provable in the direct sense — walk her to the reframe above before she asks.
- **"Why do we need to lead vs. just meet the bar eventually?"** Because DORA is already in force and CRA obligations start phasing in from 2026–2027 — your bank/insurer users' own compliance deadlines are closer than they look, and being ahead of the requirement is what turns this into a sales asset in their next vendor review instead of a scramble.
- **"Two weeks feels arbitrary."** Point to the check table — most of the score jump is configuration, not novel engineering, which is exactly why it's cheap.

**One thing to verify before you present this**: Sonatype's own supply-chain reports and the exact current CRA compliance dates shift year to year — pull the current numbers/deadlines fresh rather than quoting mine from memory, since I couldn't verify them live this session.