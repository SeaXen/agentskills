## What you're missing

You're polishing step 5 (the ask) when your own numbers are the textbook signature of steps 6 and 7 never having happened — findability and the corporate lane. This is invocation example #2 from the skill almost verbatim: *"Three funded startups ship our library and nobody sponsors us."* → when usage is proven and income is zero, **the ladder is rarely the problem; findability and the absence of a working company tier usually are.**

## The tell is in your own numbers

- 900k downloads/month + 3 named Series-B dependents + 2 engineers filing issues = usage is not in question. You have more third-party proof of dependence than most funded projects ever get.
- $35/month from 4 individuals = the *gratitude* channel is barely working and the *company* channel has never fired once.
- A $2,000 top tier existing on the page proves nothing — a tier is not "open" until a company can actually clear it through procurement. Priced-but-unpayable and no-tier-at-all convert identically: zero.

Copy rewrites only move the gratitude number. They cannot open a channel that was never wired up.

## What's actually broken — check these, in order

**1. Findability (step 6) — the zero-effort channel, check first**
- Does `.github/FUNDING.yml` exist on the default branch, sponsor button enabled in repo settings? Check the org-level fallback too (`{owner}/.github`) — a stale one silently overrides nothing.
- Is `funding` filled in `package.json`? Funder tooling (deps.dev-style resolvers, thanks.dev) reads the manifest, not just the repo.
- Fetch every funding link live. One 404 removes the project from a funder's list entirely — this is a hard filter, not a scoring ding.
- If any of this is missing, you're invisible to the automatic "breadth" money — the kind that gave one company's dependency tree 95%+ coverage at $4–10/dependency with zero outreach. At 900k downloads/month you're a strong breadth candidate and probably collecting none of it.

**2. Payability (step 7) — the silent killer of a $2,000 tier**
- Can you issue a numbered invoice, this week, with bank details? A Sponsors button alone doesn't clear a Series-B company's AP process.
- Do you have an entity, a contractor arrangement, or a fiscal host? Invoiced GitHub Sponsors has a **$5,000/invoice minimum** — smaller company asks need a fiscal host instead, or they can't be processed at all.
- If a $2,000 tier has no invoice path behind it, an approver who *wants* to say yes still can't push it through finance. This is very likely your actual root cause: the page looks finished, the mechanism to accept the money doesn't exist yet.

**3. Is the top tier actually named and priced for a company, or just tall?**
- "Platinum, $2,000" tells nobody it's theirs. "Team" or "Business" does (Porzio's own finding, confirmed by Vue and Sindre Sorhus's ladders: name the tier for the buyer).
- Is it priced against a number an approver can defend — docs traffic, README views — or against generosity? "Logo somewhere" is not a media buy; "logo on docs footer, 18k views/month" is.

**4. Outreach never happened**
- A sponsorship page is not outreach. It converts people who already arrive intending to pay — almost never how a company's procurement process starts.
- The channel that actually lands retainer-sized money — "strategic sponsorship" — is the *only one of the four corporate mechanisms won by pitching*, and it starts with a direct email to a named person (platform lead, staff engineer, head of security) at each of your 3 known dependents, naming their exposure and your service, not a link.
- Your 2 issue-filing engineers aren't just support load — they're your nominators for employee-nominated funds (Indeed-style, $10k/month/cycle at some companies). That path needs: OSI license stated, a funding mechanism present, project not employee-owned. If FUNDING.yml is missing, this path is closed too, silently, and neither of those engineers can act on your behalf even if they wanted to.

## Why "rewrite the copy" is the wrong fix

It's the only part of the problem anyone outside the project can see. Findability and payability are invisible until someone actually checks the manifest, fetches the funding link, or tries to get an invoice out of you — so intuition defaults to "the words must be wrong." Your case is the opposite: the ask is fine, the plumbing behind it was never connected.

## Do this, in order

1. **This week:** ship `.github/FUNDING.yml` + npm `funding` field, verify every link resolves live, confirm the sponsor button is on. Near-zero effort, unlocks the automatic breadth channel immediately.
2. **This week:** get invoice capability real — entity, contractor setup, or a fiscal host — before you send a single outreach email. A pitch that can't be paid is worse than no pitch.
3. **Rename and re-anchor the top tiers** for a company buyer, priced against a real number (docs traffic, README views), not against how generous it sounds.
4. **This month:** write the strong-outreach email (named contact, named dependence, named price, named service — security triage windows, release cadence, upgrade support) to each of the 3 Series-B startups directly. That's the only mechanism that reaches the money the individual ladder never will.
5. **Start tracking sponsor count split individual vs. company**, not just total income. Right now that split is 100/0 — that's the metric that would have caught this months ago, and it's the one "rewrite the copy" was never going to move.