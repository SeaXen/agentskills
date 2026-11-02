# DevRel Org Chart — 12-Month Plan (6 → 10, Marketing → Product)

**One assumption, stated up front:** you didn't give me the current 6 people's titles, so I'm assuming a typical 1→6 DevRel build-out: **Head of DevRel (you) + 2 Developer Advocates + 1 Technical Writer + 1 Community/Social Coordinator + 1 DevRel Program Manager**. Swap labels to match reality — nothing below changes shape if I'm off by one title.

---

## 1. Org chart — today (Month 0)

```
CMO
└── Head of DevRel (you)
    ├── Developer Advocate A
    ├── Developer Advocate B
    ├── Technical Writer
    ├── Community/Social Coordinator
    └── DevRel Program Manager
```

## 2. Org chart — Month 12 target

```
CPO / VP Product  ← reporting line moves here
└── Head of DevRel (you)                       [solid line: Product | dotted line: CMO]
    ├── Developer Advocate A (existing)
    ├── Developer Advocate B (existing)
    ├── Technical Writer (existing)
    ├── DevRel Program Manager (existing)
    ├── Community Manager (new, Q1)             [dotted line: CMO — content distribution/brand]
    ├── Developer Advocate C (new, Q2)
    ├── Developer Advocate D (new, Q3)
    └── Developer Educator (new, Q4)
```

Flat structure, no new management layer. 9 direct reports is the top end of workable for a Head of DevRel who's still hands-on — don't add a Community Lead / Content Lead role now. That's an 11-12 headcount problem, triggered when one of these ICs starts managing someone else (e.g., a contributor-program coordinator), not a 10-headcount one.

## 3. The Marketing → Product move: do it, but keep a dotted line

Your instinct is right, and it matches where the function actually is: at 6→10 people, DevRel's real leverage is contributor programs, docs, CLI feedback loops, and roadmap input — all product-adjacent, not campaign-adjacent. Keeping it under Marketing past this point means CLI feature requests and community bug reports keep routing through a function that has no authority over the roadmap.

The risk in a full move: you lose Marketing's distribution infrastructure — content calendar coordination, brand voice, UTM/analytics stack, paid amplification. Teams that move 100% out of Marketing tend to get under-resourced by both sides within 2 quarters.

**Fix:** solid line to Product/CPO, dotted line to CMO — specifically for the Community Manager (owns content distribution) and for quarterly brand/voice alignment. Cheap to set up, cheap to unwind if it's not needed.

**Do this alongside the reorg, not after it:** rewrite DevRel's OKRs to match the new reporting line before the move lands. Product will judge you on contributor activity, API/CLI adoption, docs time-to-first-call — not pipeline and content reach. If you don't redefine the scorecard, you'll spend two quarters being measured by the wrong numbers.

## 4. Hiring sequence: your instinct, with one flag

Community manager → 2 advocates → developer educator holds up, for one reason you may already have covered: a contributor program needs a community foundation first — moderation, good-first-issue curation, a champions pipeline to pull contributors from. Community Manager first is correct.

**The one place I'd push back:** developer educator last means docs stay thin for 9-12 months while Community + 2 Advocates scale the outward-facing motion. Poor documentation is the single most common killer of contributor programs specifically — "setup too complex" and "can't find good first issues" are the top two reasons outside contributors bounce before their first PR. If your existing Technical Writer already owns solid quickstarts and a CONTRIBUTING.md-equivalent, current sequence is fine — the educator's Q4 scope becomes curriculum/certification-style content, not foundational docs. If docs are thin today, swap the educator to Q2/Q3, ahead of the second advocate. You know which is true; I don't.

### Quarter-by-quarter

| Quarter | Hire | Scope |
|---|---|---|
| Q1 (M1-3) | Community Manager | Owns Discord/Slack/forum, moderation, engagement rhythm. Starts informal champion identification from usage + community signals — no new hires needed for this, runs on existing data. |
| Q2 (M4-6) | Developer Advocate C | Weight toward awareness/content — talks, blog, socials. Covers top-of-funnel while existing advocates focus on integration support. |
| Q3 (M6-9) | Developer Advocate D | Weight toward integration/production — sample apps, complex-integration support, technical office hours. Splits the developer-journey coverage cleanly between the two new advocates. |
| Q4 (M9-12) | Developer Educator | Docs hierarchy overhaul (quickstart → guides → reference), CONTRIBUTING.md finalized. Gates the public launch of the contributor program. |

---

## 5. Leverage programs

### Program 1: Champions (start now, Q1 — no hire required)

Prep work for the contributor program, and immediate value on its own — feedback loop, support deflection.

- Invite-only, 5-10 people to start. Identify via usage (top 10%), community help-answering, and unprompted content/mentions.
- Benefits that hold up: early feature access, private channel with the team, conference ticket sponsorship, real swag. Skip commission-based referrals and titles without benefits — both kill credibility fast.
- Owner: Community Manager, once hired. Runs on your existing team until then.
- This is your contributor-program farm system: most first contributors come from the champions list, not cold GitHub traffic.

### Program 2: Contributor program for the CLI (prep Q1, public launch Q4)

Your headline ask — worth sequencing deliberately, not launching in month 1.

**Why Q4 and not now:** the program lives or dies on two things you won't have until then — curated good-first-issues and a fast review SLA. Launching before the docs foundation exists reproduces the two most common contributor-program failure modes: newcomers can't get a dev environment running, and PRs sit unreviewed for weeks. Both are silent killers — no one complains publicly, they just don't come back.

**Structure:**
- `CONTRIBUTING.md`: one-command dev setup, clearly labeled `good-first-issue` / `help-wanted`, committed 48h first-response time on PRs.
- Recognition ladder: first PR merged → welcome + CONTRIBUTORS listing; 3+ PRs → contributor swag; 10+ PRs → "Core Contributor" label + direct Slack access; sustained contribution → maintainer invite, conference sponsorship.
- Ownership split: Developer Educator (onboarding docs), one Advocate (PR triage, coordinating review with Eng), Community Manager (recognition, Discord role).
- **The one dependency outside your control:** Engineering has to actually commit to the 48h review SLA. This is worth getting in writing from Eng leadership before you announce the program publicly — a DevRel-side commitment with no matching Eng-side commitment is the single most common reason these programs stall after a strong launch week.

### Program 3: Content bounty program (launch Q3)

Multiplies your two new advocates' reach without more headcount — pay community members directly for tutorials/integrations.

- $200-500 for a blog post, $300-750 for a video tutorial, $500-2000 for a published/maintained integration.
- Must disclose sponsorship, creator keeps editorial control and ownership — both non-negotiable, both are what keeps this from reading as advertorial.
- Secondary function: another sourcing channel for champions and future contributors — someone who'll write a paid tutorial about your CLI is a warm lead for a PR later.

Referral/ambassador programs: hold off. They're a good Year 2 move once the champions list has real depth (10-20+ people) to draw ambassadors from — launching one now just splits a small, high-touch group across two programs with unclear differentiation.