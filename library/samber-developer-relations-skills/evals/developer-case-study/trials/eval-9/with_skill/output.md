**Verdict: not yet.** Quote is fabricated, not transcribed. Draft leans on unsupported superlatives. No instrument or window on any number. Two spine sections (alternatives, limitations) are missing entirely.

## Evidence ledger

| Claim | Class | Instrument | Window | Who re-derives |
|---|---|---|---|---|
| Deploy cadence: Tuesdays-only → ~9x/week | Reported | none cited yet — check if deck pulls from CI/CD deploy logs | not stated | Director of Platform Engineering |
| Rollback ping stopped (Friday) | Directional — qualitative, no count | none | not stated | same |
| "Deployments rose sharply" | Unsupported — draft's own paraphrase, drop it, real number above replaces it | — | — | — |
| "Incidents fell" | Unsupported — not in the director's quote at all, no source given | — | — | need separate confirmation or cut |
| "Seamless / game-changing / effortless / transformative" | Not a claim — superlative, gate 7 fails outright | — | — | — |

Pull the deck's actual instrument and window for the two real numbers before anything ships.

## The draft (what's usable now, gaps marked)

**1. Headline outcome**
Stonebridge Bank went from one deploy day a week to about nine deploys a week — and their Director of Platform Engineering stopped getting paged for Friday rollbacks.

**2. Adopter and system** — [NEEDS: what Stonebridge's platform team runs, scale, stack. One line, no "founded in..." boilerplate.]

**3. Before-state and cost** — [NEEDS: why Tuesdays-only existed, what it cost them in engineer time or blocked releases. "Deploying seamlessly" tells the reader nothing they can recognize in their own system.]

**4. Why this technology** — MISSING. Need what else Stonebridge evaluated and what tipped it. Without this, section 4's whole point — a decision a reader can reuse — doesn't exist.

**5. What they built** — [NEEDS: named components, sequencing, any bank-specific constraint (change windows, approval gates) that shaped the rollout.]

**6. Results**
> "We went from deploying Tuesdays only to about nine times a week, and I stopped getting the Friday rollback ping."
> — [Name], Director of Platform Engineering, Stonebridge Bank

That's the actual quote. Verbatim, it already carries a before/after — stronger than the paraphrase it replaced. Needs the instrument/window from the deck attached next to it.

**7. Cost and unsolved** — MISSING. Ask: migration effort in engineer-weeks, dual-running period, what broke, what stayed on the old path, who shouldn't copy this. Vendor-only studies skip this section; it's the cheapest differentiation available.

**8. What's next**
The team plans further rollout across the org. *(Fine as-is, but confirm it's the director's own framing, not house copy.)*

## Approval package — confirm before drafting further

1. **Director's real name and title** — quote is currently unattributable without it.
2. **Sign-off on using his actual words** above, replacing the paraphrase — low-risk ask, it's what he said.
3. **Company name + logo** — Stonebridge is a bank: check the contract's publicity clause first, then get comms sign-off separately. Don't assume a logo clause covers the quote or the metrics.
4. **Security/legal review** — regulated industry, near-certain requirement, not yet mentioned as engaged. Open this now, not after drafting.
5. **Instrument + window for the deck numbers.**

Default if you propose one: "publish anonymized (rung 2 — named bank, unnamed engineer) if sign-off isn't back by <date>."

## Gate report

| # | Check | Status | Fix applied |
|---|---|---|---|
| 1 | Every claim classified | Fail | none yet — ledger above starts it |
| 2 | Number has instrument + window | Fail | none yet — needs deck sourcing |
| 3 | ≥1 limitation published | Fail | section doesn't exist |
| 4 | Alternatives section present | Fail | section doesn't exist |
| 5 | Every quote verbatim | Fixed | swapped fabricated quote for the real transcript line |
| 6 | Approval evidence on file | Fail | nothing on file yet |
| 7 | Zero unsupported superlatives | Fixed | cut "seamless / game-changing / effortless / transformative" |

5 of 7 still fail. Not shippable as "clean up the prose" — it needs sections 4 and 7 built, the numbers sourced, and approval opened.

## Derivatives

Not applicable — nothing's approved yet.

**Next:** get the director's name/title and confirm he's fine with his real quote replacing the paraphrase.