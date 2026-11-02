Couldn't fetch your live repo list (network calls need approval I don't have here), so this plan gives you a rubric to apply to your own six pins rather than naming them directly — slot your real repos in where indicated.

---

# Two-Weekend GitHub Rebuild — Priya Nandakumar

## Read this first: calibrate the investment

The "78% of recruiters check GitHub before the phone screen" line is unsourced marketing copy from a recruiting blog — treat it as directional, not a number to plan around. What's actually true, from how these three companies hire senior backend engineers:

- **Datadog, Stripe, Cloudflare all screen primarily off your resume + recruiter phone screen.** GitHub is a secondary confirmation signal an interviewer skims for 60–90 seconds before your onsite loop, not a gate before the first call.
- At your level (6 YOE), what they're checking for is **evidence you can do the job** — clean production-grade code, real system-design judgment, things that survived contact with scale or failure. They are *not* checking for a polished personal brand.
- Gamified profile elements (visitor counters, streak badges, snake animations, LeetCode widgets) read as junior/performative at your seniority and can quietly work against you with exactly this audience — infra engineers who'll silently judge you for decorating instead of shipping.

So: two full weekends is more time than the GitHub piece alone justifies. Budget it as **1.5 weekends on GitHub, 0.5 weekend held back for resume/LinkedIn alignment and one mock system-design interview** — higher-leverage for these three companies specifically. Below is the plan either way; cut it down if you'd rather reclaim that time.

---

## What a Datadog/Stripe/Cloudflare interviewer actually looks for

In order, in the 90 seconds they'll spend:

1. **Do the pinned repos show systems/infra depth?** — concurrency, networking, storage, observability, API design, distributed systems — not CRUD tutorials or bootcamp clones.
2. **Is there evidence of production discipline?** — tests, CI badge that's green, a real README with a design rationale, not just "how to install."
3. **Is the commit history real work, not a green-square farm?** — meaningful commit messages, PRs, issues — evidence of how you work, not just that you work.
4. **Does the profile README read like a senior engineer, in 15 seconds?** — no filler, one sentence of who you are, 2–3 things worth clicking into.

Everything below is built around those four checks.

---

## Weekend 1 (Sep 26–27) — Audit, triage, fix the foundation

### Saturday — Audit (3–4 hrs)

**Block 1 (60 min): Cold-read your own profile**
Open `github.com/priya-nandakumar` in an incognito window. Time yourself: 90 seconds, pretend you're a Stripe recruiter. Write down, unfiltered:
- What's the first impression — student side project energy or production engineer energy?
- Which of the 6 pins would you *not* want an interviewer clicking into?
- Is there anything stale, broken, or embarrassing (a placeholder README, a repo named `test123`, a dead link)?

**Block 2 (90 min): Score every candidate repo**
List every repo you own (not just current pins) and score each 1–5 on:

| Criterion | What it means |
|---|---|
| Relevance | Backend/infra/systems — the thing Datadog/Stripe/Cloudflare actually hire for |
| Depth | Non-trivial problem, not a tutorial-follow-along |
| Production signal | Tests, CI, error handling, structured logging |
| Documentation | README explains *why*, not just *how to run it* |
| Freshness | Touched in last 12–18 months, or timelessly correct |

Anything scoring under 12/25 is not pin-worthy this cycle — deprioritize, don't waste time polishing it.

**Block 3 (90 min): Pick your six pins deliberately**
Don't pin your six most-starred or most-recent — pin for **narrative coverage**. A strong senior-backend set for these three companies looks like:

1. **One systems-depth project** — something with concurrency, a custom data structure, a protocol implementation, a small database/cache engine, a load balancer, anything that shows you reason about performance and correctness under constraints.
2. **One "this runs in production" project** — real tests, CI green badge, structured logging, a design-decisions section in the README (trade-offs you made and why).
3. **One API/service-design project** — clean API contracts, versioning thought-through, error semantics — this maps directly to Stripe's bread and butter.
4. **One observability/reliability-flavored project** — metrics, tracing, health checks, graceful degradation — maps directly to Datadog.
5. **One open-source contribution** (a real merged PR to a project you don't own, ideally something infra-adjacent — a driver, a client library, an operator). If you don't have one yet, this becomes a stretch goal for Weekend 2, not Weekend 1.
6. **One that shows range or personality** — something slightly unusual (a CLI tool, a small compiler/interpreter, a home-lab/networking project) that gives an interviewer something to ask about in the "tell me about a project you enjoyed" question — this is the one place a bit of personality earns its keep.

If you don't have 6 that clear the bar, better to pin 4 strong ones than pad to 6 with weak ones.

### Sunday — Start the heavy lifting (4 hrs)

Work top-down through your 6 picks. For each repo that needs it:

- [ ] Add/fix the CI badge — a red or missing badge is worse than no badge
- [ ] Add or fill out tests if coverage is thin — doesn't need to be complete, needs to be *real*
- [ ] Rewrite the README opening: one-sentence problem statement, then a "Design notes" or "Why" section (this is the single highest-leverage edit for this audience — it's what separates "I copied a tutorial" from "I made engineering decisions")
- [ ] Add a short architecture diagram or decision log if the project has any real complexity (even ASCII or a simple Mermaid diagram beats nothing)
- [ ] Remove/archive anything embarrassing you found in the Saturday audit

By end of Sunday: 6 candidate pins identified, top 2–3 repos fully polished. Don't touch the profile README yet — that's Weekend 2, once you know exactly what you're linking to.

---

## Weekend 2 (Oct 3–4) — Finish repos, build the profile README, QA

### Saturday — Finish repo polish + projects section (4 hrs)

- [ ] Finish polishing the remaining 3–4 pinned repos using the same checklist as Weekend 1 Sunday
- [ ] If you're missing the open-source-contribution pin, spend an hour finding one realistic small PR to open now — a typo/doc fix doesn't count for this purpose, but a real bug fix or small feature to a project you already use does. It won't merge by Oct, that's fine — a well-written *open* PR still demonstrates the habit.
- [ ] Write the **Projects section** for your profile README — 3-5 lines per project max:

```markdown
## Projects

**[project-name](link)** — one-sentence problem + your role.
Built X to solve Y. Handles Z at [scale/constraint that matters]. [Tech stack].

**[project-name](link)** — one-sentence problem + your role.
...
```

Resist the urge to list all 6 pins again here in prose — the pins already show visually on your profile. Use this section for the 2–3 that need a sentence of context the pin card can't show (why it matters, what scale, what you'd do differently).

### Sunday — Profile README + final QA (3 hrs)

**Block 1 (90 min): Write the profile README**

Senior-backend-at-infra-companies register — no gamification, no emoji soup, no stats-widget wall. Something closer to:

```markdown
# Priya Nandakumar

Backend engineer, 6 years — distributed systems, API design, reliability.
Currently: [what you actually work on / are interested in, one line].

## Projects
[the section from Saturday]

## Recent focus
- [Skill/domain 1 — e.g., "observability tooling," "high-throughput APIs"]
- [Skill/domain 2]
- [Open source: link to the contribution from Weekend 1]

## Elsewhere
[LinkedIn] · [blog if you have one] · [email]
```

That's it. No visitor counter, no streak badge, no trophy case, no typing animation. At 6 YOE targeting Datadog/Stripe/Cloudflare, restraint reads as senior; decoration reads as compensating.

**Block 2 (45 min): Repo settings pass**
For each of the 6 pinned repos:
- [ ] Description field filled (shows under the pin — don't leave it blank)
- [ ] Topics added (5–10, e.g. `golang`, `distributed-systems`, `grpc`, `observability`)
- [ ] License file present
- [ ] Default branch is `main`, no leftover `master`

**Block 3 (45 min): Final cold-read + QA**
- [ ] Re-run the 90-second cold-read from Weekend 1 — did the first impression actually change?
- [ ] Check mobile rendering of the profile README
- [ ] Click every link in every README — dead links are an instant credibility hit
- [ ] Ask one trusted engineer friend (ideally one who's interviewed at a similar company) for the 90-second read — you're too close to it to see it fresh anymore

---

## What to explicitly skip

Given your target companies, don't spend time on:
- Stats cards, streak counters, trophy widgets, visitor badges — noise for this audience
- LeetCode/WakaTime integrations — irrelevant signal for backend infra roles
- Snake animation / typing SVG — costs time, reads as junior here
- Chasing more stars/forks on existing repos — not enough runway before applications to matter, and it's not what's being evaluated anyway

## If you have the 0.5 weekend to spare

Redirect it to: (1) a 45-minute resume pass making sure the same 2–3 projects you just polished are the ones your resume bullets reference — GitHub and resume should tell the same story, and (2) one mock system-design interview, since that's the actual gate at all three companies and higher-leverage than a 7th hour of README polish.