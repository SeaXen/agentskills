# mistral-gauge → GitHub Sponsors: tier setup + path to $7,200/mo by March 2027

## Reality check first (skipping this would be malpractice)

190 stars, 4k downloads/mo, ~60 companies. That's real traction for a niche infra library — but run the math on $7,200/mo before committing to it as a "quit my job" number:

- Self-serve GitHub Sponsors from individuals converts at well under 1% of your actual user base, even for well-loved projects. 4k monthly downloads doesn't mean 4k people who'd ever click "sponsor." Realistic individual-tier income in 5 months: **$50–$300/mo**, not thousands.
- To hit $7,200/mo from company tiers alone at $250–$500/mo price points, you'd need **20–30 of your 60 known companies to convert** — a 35–50% conversion rate. Cold, self-serve B2B sponsorship conversion runs closer to 3–8%, even with direct outreach.
- The only realistic lever is **a handful of large, hand-sold support contracts** with the companies that have the most to lose if you stop maintaining this. 4–6 companies at $800–$2,000/mo closes the gap. That's an achievable number of relationships for one person to personally close in 5 months. 25 is not.

So: build the full public tier ladder below (it's good practice and captures the long tail), but treat it as the *visible* layer. The number gets hit — if it gets hit — through direct sales to 5-10 named accounts, not by publishing a Sponsors page and waiting.

Set a checkpoint: **January 15, 2027.** If signed/committed MRR is under ~$4,500 at that point, $7,200 by March isn't happening — negotiate a phased/part-time transition with your employer instead of a hard cutover. Better to know in January than March.

---

## 1. Public tier ladder (paste directly into GitHub Sponsors)

**Individual tiers** — goodwill + long tail, low effort to maintain:

| Tier | Price | What they get |
|---|---|---|
| **Supporter** | $5/mo | Name in `SPONSORS.md`, sponsor badge on your GitHub profile view of you |
| **Backer** | $15/mo | Above + early read of release notes before tagging, name in release changelogs |
| **Patron** | $50/mo | Above + priority triage on your issues (not SLA — just "looked at sooner") |

**Business tiers** — this is where the number comes from. Price these as risk-mitigation/support, not donation:

| Tier | Price | What they get |
|---|---|---|
| **Business — Starter** | $99/mo | Logo in README "Used By" wall, 48h issue-response target, private email channel |
| **Business — Priority** | $349/mo | Above + guaranteed sev1/sev2 response SLA (24h/72h), quarterly 30-min roadmap call, input on prioritization |
| **Business — Dedicated** (Contact for annual) | $999/mo+ | Above + 4 guaranteed hours/month of direct engineering time (integration help, code review, security-patch fast-track), named point of contact |

Don't publish a price above $999 on the page itself — for the real anchor deals ($1,500–$3,000/mo), sell those by hand as a support agreement (see §3), then list them publicly as "Custom / Contact me" so the page doesn't cap what a serious account would pay.

---

## 2. Files to set up

**`.github/FUNDING.yml`** (root of mistral-gauge repo):
```yaml
github: [your-github-username]
```

**Sponsors page goal ladder** (GitHub lets you set one active funding goal with a description — cycle through these as you hit them):
> **$2,500/mo** — I keep mistral-gauge maintained on nights/weekends at current pace, plus faster issue triage.
> **$5,500/mo** — I go to 3 days/week on mistral-gauge: faster releases, better docs, more format support.
> **$7,200/mo** — I go full-time. Full-time means: same-week feature turnaround, formal SLAs for Business sponsors, and a real roadmap instead of "whatever's on fire."

**README sponsor section** (add above the fold, right under the one-liner):
```markdown
## Used in production by

[logo] [logo] [logo]  <!-- ask 5-6 of your 60 known companies if you can list them — see outreach below -->

mistral-gauge parses pressure-sensor logs for production data pipelines. If it's load-bearing
for you, consider a [Business sponsorship](https://github.com/sponsors/your-username) —
it funds continued maintenance and gets you a support SLA.
```

A visible "Used by" wall is the single highest-leverage thing you can add — it's social proof that turns a cold ask into "everyone else already does this."

---

## 3. The part that actually gets you to $7,200: direct outreach to the 60

Publishing tiers and waiting gets you the individual long tail and maybe 1-2 self-serve businesses. The rest has to be sold.

1. **Rank the 60.** Sort by: how business-critical your library likely is to them (production pipeline vs. side script), company size, and any existing signal (they've opened issues, filed PRs, work at a company you can identify from their GitHub org). Pick the top 15.
2. **Reach out personally, not via the Sponsors page.** One email/issue-comment per company, from you, referencing their specific use if you know it.
3. **Template:**

   > Subject: mistral-gauge — going full-time on it, wanted to give you a heads-up
   >
   > Hi [name] — I saw [company] uses mistral-gauge [in X, if known]. I'm setting up formal support tiers because I'm aiming to go full-time on the project by March.
   >
   > If it's running in production for you, a Business sponsorship ($99–$999/mo) gets you a response SLA and direct access to me instead of hoping an issue gets picked up. Happy to jump on a 15-min call if useful, no pressure either way — just wanted you to hear it from me before I announce it publicly.
   >
   > [Sponsors link]

4. **For the 5-10 most valuable ones**, don't stop at the $999 tier — offer a direct support agreement ($1,500–$3,000/mo, invoiced, 1-page agreement covering response times + a few hours of integration help). Some companies' procurement won't do a GitHub Sponsors subscription but will happily sign a support contract with an invoice. This is where the real dollars come from.
5. Budget for **~10% close rate** on cold-to-warm outreach even when well-targeted. 15 outreaches → 1-2 closes per wave. Run 3 waves (Oct, Nov, Dec) across different segments of the 60, not all 15 at once.

---

## 4. Timeline

| By | Target MRR | Action |
|---|---|---|
| Oct 2026 | Tiers live, page published | Ship the ladder above, add "Used by" wall, first outreach wave (top 15) |
| Nov 2026 | $1,500–$2,500 | Second outreach wave, ask early sponsors for warm intros to peers |
| Dec 2026 | $3,000–$4,500 | Third wave, start converting any Starter tiers to Priority/Dedicated |
| **Jan 15, 2027** | **Checkpoint** | If committed MRR < ~$4,500: negotiate part-time transition with employer instead of hard cutover in March |
| Mar 2027 | $7,200 (stretch) or negotiated partial | Go full-time if hit; go part-time/phased if not |

Build the tiers now — they're correct regardless of the outcome. Just don't let "$7,200 by March" be the thing that decides whether you can pay rent; let the January checkpoint decide that.