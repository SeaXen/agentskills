## The reframe first

"Post every day" is the wrong success metric. What actually moves a staff-eng or DevRel hire is: **written technical depth, teaching ability, and visible community presence** — evidenced by a body of work, not a streak. Daily posting is a *habit that produces the raw material*; it is not itself the deliverable. Build the plan around one flagship piece a week, fed by daily notes, not around 30 polished essays. That's the difference between a month that compounds and a month that burns you out by day 12.

Growth here = real value (the linter, the depth of what you write about it) × discoverability (GitHub + distribution) × first-use experience (README, docs). If any of those is zero, the daily posting doesn't matter.

---

## Week 0 — foundation (do this before the first public post)

**GitHub, since it's your landing page and hiring managers will click through:**
- Rewrite the README: one-liner, why-this-linter-over-tflint/checkov, GIF or terminal recording of it catching a real bug, quick start in under 5 lines, badges (CI, crates.io version, license, stars).
- Add 8-10 GitHub topics: `rust`, `terraform`, `linter`, `hcl`, `static-analysis`, `infrastructure-as-code`, `cli`, `devops`.
- Add `CONTRIBUTING.md` and tag 5 real `good first issue`s — you want other engineers visibly collaborating with you, that's a stronger staff/DevRel signal than solo output.
- Set up a profile README (`github.com/<you>/<you>`) linking the project, your blog, and what you're currently learning.

**Platform decisions (make once, don't relitigate weekly):**
- Owned: a blog (even a static one, or dev.to/Hashnode as owned-enough since they syndicate + index for search).
- Rented/borrowed for reach: pick **one** primary social — LinkedIn if staff-eng/DevRel hiring managers are the audience, X if it's the Rust/infra OSS crowd. Cross-post to the other but don't create native content for both daily; that's how "daily" dies in week two.

**Positioning:** write one paragraph, for yourself, answering "what do I want a hiring manager to conclude after reading 10 of my posts?" (e.g., "this person can explain a hard systems problem clearly and ships things people use"). Every piece gets checked against that.

---

## Content pillars (pick 3-4, don't spread thinner)

| Pillar | Why it matters for the goal |
|---|---|
| **Parser/linter internals** (HCL parsing, AST design, rule engine architecture) | This is your staff-level signal — architecture reasoning, tradeoffs, not just "I learned X today." |
| **Rust, learned in public** | Searchable (tutorials rank), and shows you can go deep on a language outside your day job. |
| **Terraform/IaC ecosystem** | Searchable, product-aligned, draws the actual user base of your linter into your orbit. |
| **The build-in-public meta-narrative** (why you're doing this, what you're optimizing for, what failed) | This is the DevRel signal specifically — hiring managers for DevRel want to see you can narrate a journey and build an audience, not just write code. |

60/30/10 split across the month: ~60% searchable (parser deep-dives, Rust how-tos, Terraform content), ~30% shareable (opinions, "why I made this tradeoff," the meta-narrative), ~10% experimental (try a format you haven't — a short demo video, a diagram thread).

---

## The cadence that survives a month

- **Daily (5-15 min):** a build-log post on your primary platform. One lesson, one snippet, one screenshot, one decision you made and why. This is the "every single day" commitment — keep it genuinely small so it's sustainable.
- **Weekly (1 flagship):** a real long-form piece on the blog/dev.to — pulled together *from* that week's daily notes, not written from scratch. Cross-post to dev.to/Hashnode (SEO), summarize as a thread/post on your social platform, drop in 1-2 relevant communities if it's genuinely useful there (r/rust, r/Terraform, r/devops — read each sub's self-promo rules first).
- **Distribution discipline:** write the flagship with pull-quotes and subheads that double as standalone social posts. One good piece, reformatted everywhere, beats four mediocre platform-native posts.

---

## First month, week by week

**Week 1 — Foundation + first daily reps**
- Mon-Tue: README overhaul, GitHub topics, profile README, positioning paragraph.
- Wed: First daily build-log post — announce the project + what you're building in public and why (the meta-narrative, sets context for everything after).
- Thu-Fri: Daily build-logs on whatever you actually hit (a parsing bug, a Rust borrow-checker fight, a design decision).
- Weekend: Draft flagship #1 — a technical deep-dive, e.g. "How \<linter\> parses HCL into an AST" or "Why I chose \<parsing approach\> and what I'd do differently." Pick something with real technical meat, not a recap.

**Week 2 — Ship the first flagship, start engaging outward**
- Mon: Publish flagship #1 on blog, cross-post to dev.to, summarize on social.
- Daily build-logs continue.
- Engage in 1-2 relevant communities: answer a question in r/rust or r/Terraform, comment thoughtfully on 2-3 adjacent build-in-public posts (borrowed audience, not spam).
- Tag 3 more `good first issue`s; respond to any inbound issue/PR within 48h — visible responsiveness is part of the DevRel signal.

**Week 3 — Community + second flagship**
- Submit the project to `awesome-rust` and one Terraform/IaC-specific list (check star/activity gate first).
- Daily build-logs continue.
- Draft + publish flagship #2 — go shareable this time: an opinion piece or "what I got wrong" post (e.g., a design decision you reversed). Vulnerability/honesty content earns disproportionate shares.
- If you hit a genuine milestone (a real bug caught, a benchmark, a contributor's first PR merged), that's HN/Reddit-worthy — otherwise don't force a launch-style post this early.

**Week 4 — Review, adjust, compound**
- Daily build-logs continue.
- Flagship #3 — pick whichever pillar got the most engagement in weeks 1-3, double down.
- Review: GitHub traffic/referrers, which flagship got the most reads/shares, which daily posts got replies vs silence. Kill formats that flopped, keep what worked.
- Write a short "one month of building in public" retrospective — this is itself a strong meta-narrative piece and closes the loop for anyone who followed since week 1.

---

## What to watch (not vanity metrics)

- Stars are a lagging indicator — track GitHub traffic/referrers and clone counts instead (Insights → Traffic).
- Track replies/comments on daily posts, not just likes — that's the actual "is this landing" signal.
- Track who's engaging: if staff engineers/DevRel folks at companies you'd want are the ones responding, that's more valuable than raw volume.

## Traps that kill this by week 3

- Treating "daily" as "daily polished essay" — you'll quit. Daily = build-log, weekly = flagship.
- Posting to every platform natively — pick one primary, cross-post the rest.
- Chasing stars over substance — a hiring manager reads 3-5 of your posts, not your star count.
- Going silent on issues/PRs once the posting habit starts — responsiveness is part of the story, not separate from it.