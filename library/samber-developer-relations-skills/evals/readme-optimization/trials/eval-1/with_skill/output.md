Using the **readme-optimization** skill to answer this.

## First: the stat is folklore, not GitHub research

"Repos with detailed READMEs get 50% more contributions" is on this skill's own refuse-list — it circulates widely with no traceable source, and it is not GitHub's research. I won't build the plan on it. What *is* sourced (Prana et al. 2019, 393 GitHub repos):

| README answers | % that have it |
|---|---|
| What the project is | 97.0% |
| How to use it | 88.5% |
| Why pick it over the alternative | **25.7%** |
| What state the project is in | **21.4%** |

The two categories worth chasing are scarce ones: **differentiation** and **status**. Neither is architecture, roadmap, FAQ, or a contributors wall.

## Second: I'd stop you before you write those four sections

Tessarine's README today is 4 sections (title, install, examples, licence). Half of all sampled READMEs sit at 5–12 sections, median 7 — so you have room to grow, but going straight to architecture + roadmap + FAQ + contributors wall on a 40-line page is the skill's named failure mode: *"adding architecture and roadmap sections to a small utility makes it look abandoned, not mature."* A wall of aspirational sections next to three code samples reads as a project overcompensating, not one that's earned the length.

There's also a maintenance cost each one accrues silently:
- **Architecture section** — goes stale the next time you touch internals; belongs in a linked `ARCHITECTURE.md` if it's worth writing at all.
- **Roadmap** — a public promise list nobody updates after month two; issues/milestones already do this job better.
- **FAQ** — usually a symptom, not a fix. If people keep asking the same question, that's a docs gap or an API smell the README should close by being clearer up front, not a growing Q&A appendix.
- **Contributors wall** — fine, but it's a community-health element, and this skill keeps those out of the README file itself (CONTRIBUTING.md, or an all-contributors bot rendering into its own section) so they don't add scroll distance before a reader has decided anything.

None of the four move the 25.7%/21.4% needle. A one-paragraph differentiation statement and an honest status line would, and each is a few sentences.

## What I can score right now, and what I can't

I don't have the Tessarine repo — no read access, can't run `go get`, can't check the parser against documented flags. That blocks two of the five pass/fail checks outright, so treat this as provisional, not a real audit:

```
README audit — samber/tessarine   (audience: TBD — see Q below)
Band A: A1 pass (title + one-line description implied) · A2 UNKNOWN (can't run install) ·
        A3 UNKNOWN (can't verify code samples against source) · A4 FAIL (no status stated) ·
        A5 pass (MIT line present)
Band B: B1 0/2 (no differentiation stated) · B8 2/2 (4 sections, well under the 5–12 median band)
Verdict: incomplete — can't clear Band A without repo access
```

## Before I draft anything, four questions (these gate the rewrite per the skill)

1. Can you paste the repo URL, or give me read access, so I can actually run the install and check the fixed-point/rounding claims against your source instead of writing plausible-sounding financial-math prose I can't verify? For a money library, an invented claim about rounding behavior is the one mistake that actually costs someone real money.
2. Who lands on this page — Go developers evaluating it for their own codebase, or does adoption also route through a company's approval process (licence/security review)? Changes whether Step 8 trust signals (security policy, release cadence) apply at all.
3. Honest status: experimental, actively maintained, or stable/feature-frozen? At 900 stars this probably isn't "experimental," but I won't guess for you.
4. Can you name the one or two libraries someone would use instead of Tessarine, and what you deliberately trade off against them? That's the missing 25.7% content, and it's usually the highest-leverage thing to add.

## My recommended order, once I have that

Effort-vs-value for your actual situation, not the four sections you proposed:

1. **Status line** — one sentence, free, closes A4.
2. **Claim check** — verify the three existing code samples still compile against current API (needs repo access).
3. **Differentiation paragraph** — 3–5 sentences on why fixed-point over `float64` or `big.Float` for money, what you deliberately don't support.
4. **Badge row** — cap at 4, assessment signals only (CI, coverage, latest version, licence); drop anything that's just an intent statement.

That's an afternoon, targets the two categories that are actually scarce, and doesn't leave four half-maintained sections for the next contributor to either update forever or quietly let rot. Send me the repo and I'll run the real audit script and give you verified prose instead of a guess.