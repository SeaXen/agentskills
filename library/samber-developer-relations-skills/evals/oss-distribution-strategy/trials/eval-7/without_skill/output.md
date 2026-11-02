Web search isn't available in this session, so I'm building this from what's durable and well-established rather than pulling live URLs — I'll flag the one or two spots where you should do a 5-minute sanity check before submitting anything.

Here's the plan.

---

## First, the honest math

3 hours/month = 9 hours/quarter = 36 hours/year, forever, solo. That budget cannot fund: a self-published newsletter, multiple maintained framework-adapter packages, *and* a quarterly cycle of list submissions, on top of the actual coding you're already doing to keep slatevane alive. Something in your original wishlist has to give, and I'd rather tell you which one than quietly ship you a plan you can't sustain past month four.

The thing that has to give is **"integrations" meaning published adapter packages.** A `@slatevane/react-hook-form` or `@slatevane/formik-bridge` package is not a one-time cost — it's a second (and third) repo with its own issue queue, its own semver, and its own breaking-change exposure every time React or Vue ships a major version. For a solo maintainer at 3h/month, that's the single most common way an OSS side project quietly turns into a second job. So:

- **"Integration" in this plan means a documentation guide + a working example, not a published package.** "Using slatevane with React Hook Form," "slatevane + Next.js Server Actions," etc. — code lives in a CodeSandbox/StackBlitz link you embed, not in a repo you maintain. Zero ongoing maintenance surface beyond "does the example still run" once a year.
- If slatevane's core already *requires* framework-specific bindings to be usable at all (i.e., it's not framework-agnostic and a "React integration" is really "the only way to use this from React"), that's a different, much bigger conversation — tell me and we redo this from scratch, because that's product work, not distribution work.

Same edit to "newsletter push": at 900 weekly downloads and 3h/month, you don't run a newsletter — you don't have the list, and building one is its own multi-year project. **"Newsletter push" means pitching your quarterly release into newsletters other people already run** (JavaScript Weekly, TypeScript Weekly, Frontend Focus, Bytes, Console). That's a 15-minute email per quarter, not infrastructure.

With those two substitutions, the rest of your ask is genuinely fundable in 3h/month. Here's the system.

---

## The repeating engine (do this every quarter, forever)

One quarter = one release-shaped content cycle. Budget: ~9 hours. Same recipe every time so it never requires fresh strategic thought — that's what makes it survive year five, not just year one.

| Step | Time | What it actually is |
|---|---|---|
| 1. Write the quarterly note | 1.5h | Not a blog post from scratch — curate your own CHANGELOG/commits from the last 3 months into 300-500 words: what shipped, why, one code snippet. This is the single artifact everything else points to. |
| 2. Pitch it to 3-4 newsletters | 30 min | Reuse a template (below). Send the same week the quarterly note goes live. |
| 3. Post in 2 community spaces | 1h | One relevant subreddit (e.g. r/typescript or r/reactjs, whichever fits that quarter's angle) + one Discord/Slack `#showcase`-type channel. Not both every time if it feels repetitive to the same audience — rotate. |
| 4. Rotate one integration guide | 3h | Write or refresh one framework usage guide. Q1 React, Q2 Vue, Q3 Svelte, Q4 = catch-up/refresh whichever got stale, no new one. Four frameworks total is the ceiling — resist adding a fifth. |
| 5. Touch one curated list | 1h | Rotate through your 3-4 target lists (below), one per quarter — check it's still accurate, or submit if not yet listed. By month 12 all 3-4 are covered; from year two on this step is pure maintenance. |
| 6. Issue/PR triage sweep | 1h | Close stale issues, thank anyone who filed a good bug report or PR, merge what's mergeable. This is distribution too — a repo that looks abandoned kills every other tactic above. |
| 7. Buffer | 1h | Absorbs the quarter something breaks, a list rejects your PR and you need to rework it, or a newsletter reply asks a follow-up question. |

**Total: 9h.** No month-to-month variation to design — you're not inventing new tactics each quarter, you're running the same seven-step loop with different rotation inputs (which framework, which list, which community). That's what makes "forever" realistic: decision fatigue is the actual thing that kills solo-maintainer marketing, not lack of tactics.

---

## Year one is different: front-load setup

The loop above assumes your GitHub/npm surface is already in shape and you have a shortlist of targets. Neither is true yet, so spend Q1's 9 hours on setup instead of the steady-state loop, then start the loop in Q2.

**Q1 setup budget (9h):**
- README pass — one-liner, why-this-over-Formik/RHF/etc., 5-line quick start, badges (npm version, downloads, bundle size via bundlephobia) — 1.5h
- `package.json` keywords + GitHub topics tuned for how someone searches ("form validation typescript," "type-safe forms," "form state management") — 30 min
- Build the actual shortlist: confirm your 3-4 target lists and 3-4 target newsletters still exist and accept submissions (5 min each, just visit the site — don't skip this, submission processes change) — 1h
- First integration guide (pick whichever framework has the most existing slatevane users, check your GitHub issues/discussions for hints) — 3h
- First quarterly note + first newsletter pitch — 2h
- Buffer — 1h

From Q2 onward, you're in the steady-state loop.

---

## The 3-4 curated lists — concrete shortlist

Rather than a scattershot directory crawl (low value per the general research on this — most "software directories" don't send qualified traffic), target lists a TypeScript/form-library user actually browses:

1. **A GitHub awesome-list for your primary framework** — `awesome-react-components` (has a dedicated Forms section) or the equivalent for whichever framework you integrate first. High credibility, community-vetted, and the PR itself is a small piece of visibility (reviewers and watchers see it).
2. **`awesome-typescript`** — independent of framework, matches slatevane's core identity as a TypeScript-first library.
3. **bestofjs.org** (or the current equivalent ranked-directory site for the JS/TS ecosystem) — these sites rank by real signals (stars, downloads, commit activity) rather than pure curation, so once you're listed it's low-maintenance: your existing growth does the work.
4. **A forms-specific or niche list if one exists in your framework's ecosystem** (e.g. a "state management" or "forms" section inside a broader `awesome-<framework>` list) — search for this once in Q1 setup rather than assuming it exists.

Before submitting to any of these, do the 5-minute check: open the repo, confirm it had a commit or merged PR in the last 6 months, and read its `CONTRIBUTING.md` for exact PR format. An abandoned list is wasted effort; a list with strict formatting rules that you ignore gets your PR closed unread.

---

## The newsletter pitch — reusable template

Send this the same day your quarterly note goes live. Personalize the subject only.

```
Subject: slatevane [vX.Y] — [one-line hook, e.g. "type-safe form state with zero re-renders on validation"]

Hi [curator name if known],

slatevane is a TypeScript form-state library (~900 weekly npm downloads).
Just shipped [the one genuinely interesting thing this quarter — a feature,
a size reduction, a new integration guide]. Thought it might be a fit for
[newsletter name].

Repo: [link]
Release notes: [link to the quarterly note]

Thanks either way — appreciate what you put out every week.
```

Targets: JavaScript Weekly, TypeScript Weekly, Frontend Focus, Bytes.dev — all have long-running "submit a link" processes (usually a simple form or a submission email on their site). Confirm the current submission mechanism for each once during Q1 setup, since these details drift; don't rely on this plan's memory of them a year from now.

Expect a low hit rate — these curators reject far more than they accept, and a 900-download library isn't going to land every quarter. That's fine: the cost is 30 minutes, and even one hit a year is worth the whole year's postage. Don't take a rejection (silence, really — they don't reply) as a signal to stop; it's a lottery ticket, not a review.

---

## What this plan deliberately does NOT include, and why

- **No Discord/community server of your own.** Running a community is a full role, not a task — at 900 downloads and 3h/month you don't have the traffic to sustain one, and an empty Discord is worse for credibility than no Discord.
- **No conference talks / CFPs.** High-effort, multi-month lead time, doesn't fit a fixed 9h/quarter loop without blowing the budget some quarter.
- **No paid promotion, no Product Hunt re-launch cycle.** PH is a one-time launch asset you've presumably already spent; re-launching reads as spammy and won't get algorithmic favor twice.
- **No adapter packages**, per the reasoning above — this is the load-bearing cut that makes everything else sustainable.
- **No monthly cadence.** A monthly newsletter pitch with nothing new to say trains curators to ignore you. Quarterly matches your actual output cadence for a solo-maintained library.

---

## Minimal metrics (don't build a dashboard)

Once a quarter, during the buffer slot, glance at three numbers — npm weekly downloads (npmjs.com package page, no tool needed), GitHub stars trend, and whether last quarter's newsletter pitches got picked up. That's it. Anything more elaborate than that is itself a time sink competing with the 9 hours you're trying to protect.