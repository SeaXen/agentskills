# Build-in-public charter — Terraform linter (and the Rust/parser-design learning alongside it)

Two things are bundled in your ask, and they pull in different directions, so I split them before building the plan.

**What you actually described is two practices, not one.** "Post daily about the linter" is *build in public* — content anchored to a project, aimed at an audience that might adopt, contribute, or sponsor it. "Post daily about whatever I'm learning — Rust, parser design, whatever I hit that week" is *learning in public* (Shawn Wang's term) — a career practice about your own skill and reputation, not the project's. Your goal (staff role or DevRel job) is a personal-credibility outcome, so learning-in-public is actually the dominant practice here, with the linter serving as your proof of work rather than the other way around. That changes what "daily" should mean — see Cadence below.

**Assumptions I'm making, since I can't interview you turn-by-turn here — correct any of these and the plan below shifts:**
- Solo maintainer, no co-founders, no revenue on the linter. Nothing to clear with anyone else.
- You have a day job (backend engineer) alongside this — so "daily" has to fit around full-time work, not be the work.
- The Rust/parser-design track is exploratory learning, not yet a committed rewrite of the linter.
- Primary outcome: hiring/credibility signal for yourself. Secondary: more contributors/users on the linter, since that's evidence you can point to.
- Horizon: roughly a year, open-ended archive rather than a single launch moment.

---

## The charter

```
Goal            Primary: staff-role or DevRel-job credibility signal for yourself.
                Secondary: contributors and adoption on the linter, as evidence.
Context         Solo maintainer. No revenue, no co-founder, no investor claim on
                any number. Your day job is the one boundary that isn't yours alone
                — see Boundaries.
Audience        Two, and they read the same posts differently:
                (1) backend/infra developers who might use or contribute to the
                    linter — amplification and technical peer credibility.
                (2) staff engineers, eng managers, and DevRel hiring managers —
                    the actual conversion target. For the DevRel branch specifically,
                    the writing itself is a work sample: DevRel is a communication
                    job, so a good devlog is an audition tape, not just evidence.
Rung            Rungs 1-3: shipping log, decisions, failures. This is what buys
                contributor trust and hiring credibility — metrics rarely do.
                Rung 4 (stars, downloads, contributors, issue response time),
                quarterly only, as light supporting evidence for job conversations.
                Rung 5 excluded: no revenue exists to disclose.
Stop condition  Rung-4 numbers stop if they start reading as bragging, or once a
                job lands and the audience shifts from "evaluating me" to
                "coworkers/employer" — re-charter at that point, don't just fade.
                No stop condition needed for rung 5 — it was never opened.
Boundaries      Hard blocks: unpatched vulnerabilities (coordinated disclosure
                only), any third-party data/names without consent, your employer's
                proprietary code/systems/incidents — never, even as an anonymized
                analogy.
                Grey zones, decided now: don't announce the Rust work as a
                committed rewrite until it ships — label it "personal exploration,"
                explicitly separate from the linter's roadmap, so current users
                don't read it as "the Go version is being replaced" (Osborne
                effect). No dated roadmap, direction only. Mention your employer
                only if it complies with their own social-media policy — check
                that once, in week 0, not post-by-post.
Cadence         Private daily notes (raw, ~10 min, never published as-is) feeding
                a weekly public log (shipped / learned / stuck / next) plus a
                substantial post every 2-3 weeks tied to an actual linter release
                or a real decision/failure. See Month 1 below for the ramp-up.
                No literal daily public posting — reasoning below.
Surfaces        Anchor: a devlog section on your own site or the repo (own the
                archive — set this up in week 0 if it doesn't exist).
                Amplifiers: X (short-form, the build-in-public/indie audience),
                LinkedIn (rewritten, not cross-posted — this is where staff/DevRel
                hiring managers actually look), dev.to or Hashnode for the
                Rust/parser-design pieces (SEO reach), r/Terraform / r/devops /
                r/rust for occasional milestone or technical posts, Hacker News
                "Show HN" reserved for genuinely significant releases only.
Support plan    README states maintenance scope and expected response time.
                Feature requests route to GitHub Discussions, never DMs. Watch
                issue volume vs. contributor count — if issues grow faster than
                contributors after a post lands, pause posting and fix the README
                or docs gap instead of writing more.
Measurement     Ignore stars and followers as pass/fail signals — track them only
                paired with a movement signal (contributors, downloads).
                What actually counts: first-time contributors per quarter, and —
                since the real goal is personal — any recruiter/hiring-manager
                message, interview, speaking or podcast invite that references a
                specific post. Reviewed quarterly, not weekly; this compounds too
                slowly to read week to week.
Pause rule      Two consecutive missed weekly logs → drop publicly to release-spine
                only ("shipping a release, that's the post") and say so in one
                sentence. Never let it go quiet without a note — silence reads as
                the project dying, which is the opposite of the signal you want a
                hiring manager to see.
```

---

## Why not literal daily posting

Run the capacity math before committing to it, not after burning out on it:

```
per post   = drafting + code snippet/screenshot + review + boundary check
           ≈ 20-30 min even for something short
per week   = 7 posts × 25 min           = ~3 hours drafting alone
reply load = 7 posts × threads × reply time   — usually bigger than drafting
```

That's before you've written a line of Rust or touched the linter. Daily public posting on top of a full-time job is exactly the "all posts, no shipping" failure mode — the content about the work crowds out the work, and a hiring manager evaluating a staff-engineer candidate is looking for depth, not volume. A weekly log made from real daily notes gives you the daily habit (which is genuinely valuable for retention and for having raw material) without carrying the publishing and reply cost seven times over. Reduce frequency before reducing depth — one real decision post beats seven "today I learned" tweets.

---

## Month 1, week by week

**Week 0 — before anything goes public**
- Write the charter above for real: fill in your own answers, don't just accept mine.
- Set up the anchor surface if you don't have one — a devlog page, or expand the repo's CHANGELOG into something linkable.
- Add a one-paragraph maintenance-scope statement to the linter's README; point feature requests at Discussions.
- Pick a zero-friction private note format (a markdown file, a notes app — doesn't matter, it just needs to survive a bad week).
- Confirm your employer's social-media policy once, so you're not re-checking it under deadline later.

**Week 1 — establish the shipping log**
- Private notes daily, ~10 min, no pressure on quality.
- One public post: a real "state of the project" update — not "200 stars, thank you!" but the strong-example shape: a couple of real numbers (weekly downloads, contributor count, response time) plus what they actually mean. Bare-milestone posts teach nobody anything and read as marketing.
- Amplify once on X, once on LinkedIn — rewritten per platform, not the same text pasted twice.

**Week 2 — first decision post**
- Turn the week's notes into one decision-format post about something you've already built in the linter — the HCL parsing approach, a scope-cut, whatever real choice exists. Name the alternatives you didn't pick and why, not just the outcome. This is rung 2, and it's the highest-credibility-per-word content you have before any Rust work exists publicly.

**Week 3 — introduce the Rust/parser-design thread, carefully**
- First post on the Rust exploration, explicitly framed as personal learning, explicitly separate from the linter's roadmap. State plainly that the Go linter isn't going anywhere yet — don't let readers infer a rewrite that isn't committed.
- Weekly log post from the week's private notes (shipped / learned / stuck / next).

**Week 4 — first failure post, and a review**
- Use a real friction point from the month — a wrong bet, a bug, something reverted — even small. A feed of only wins gets discounted wholesale, including the true parts.
- Run the four-question pre-publish check retroactively against everything you posted this month, as a habit-forming exercise: does it expose an unfixed security issue; does it use someone else's data without consent; does it commit to a date you don't control; would it be a problem quoted alone by a hostile reader.
- Check the month against the charter: did cadence hold, did any named signal move (a contributor, a message, an invite), did any boundary get close to a breach. Set month 2's cadence off what this month actually cost you, not off the plan.

---

## Two things worth deciding before you write the first post

1. **Read Plausible's positioning before you decide how loud to be about numbers** (`plausible.io/about`) — fully public code, milestone-only disclosure, no live dashboard. That's closer to your actual situation than Buffer's everything-public model, and it's proof the practice doesn't require a metrics feed to work.
2. **Run drafts through a humanizer pass before publishing.** A devlog that reads like a press release defeats the purpose — the whole value of this, for a DevRel application especially, is that it sounds like you.