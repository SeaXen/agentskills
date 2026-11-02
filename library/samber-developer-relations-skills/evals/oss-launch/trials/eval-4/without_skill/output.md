# Pellet Launch Week — Day-by-Day Map

**Format:** Mon–Fri, one release + one blog post + one demo per day, escalating arc, Friday = biggest reveal + roadmap. Every day publishes to a single landing page (`pellet.dev/launch-week` or similar) that acts as the owned-channel hub — this is the thing you point Twitter/HN/Reddit at, not individual posts.

**Order logic:** foundation → visual → technical depth → proof → vision. Each day should stand alone for someone who only sees that one post, but the five together tell "this is a real, finished tool, built by one person, that other real people already use."

---

## Monday — The Generator (reintroduction)

**Why first:** most of your audience has never heard of Pellet even after 14 months solo. Day 1 doubles as "hello, this exists," not just "here's a technical deep dive."

**Content:**
- Blog post: why Pellet exists, what it's for (technical docs specifically — not "yet another SSG"), the core build pipeline, a build-speed number vs. 1-2 named competitors (Docusaurus, VitePress, Hugo — pick what you actually beat).
- Demo: 60-90s terminal recording, `pellet build` on a real-sized docs project, showing the time.
- Launch-week landing page goes live same morning with all 5 day slots visible (greyed out for Tue–Fri) — this is your countdown mechanic.

## Tuesday — Theme System (the "wow, look at this" day)

**Why second:** most shareable day — screenshots and before/after GIFs travel on social far better than API docs. Put it early to catch momentum while people are still checking the hub daily.

**Content:**
- Blog post: 2-3 themes shown side by side, how theming works (CSS vars? component overrides?), one worked example of a user re-skinning docs in <10 min.
- Demo: GIF/video flipping between themes live.
- If you have even one real external user who themed their docs with Pellet — feature them here. Borrowed credibility beats another feature list.

## Wednesday — Plugin API (mid-week depth)

**Why third:** by Wednesday the audience is self-selected toward people who actually care about the tool, not just the screenshots. This is the day for the technical crowd — good placement for a Hacker News submission, since HN rewards substance over polish.

**Content:**
- Blog post: plugin API surface, one non-trivial example plugin (search integration, versioning, i18n — whatever's real), design decisions/tradeoffs.
- Demo: short code walkthrough, not a GIF — this audience wants to read code.
- Ship one small first-party plugin alongside the post if you have one ready; "here's the API + here's proof it's usable" lands better than API docs alone.

## Thursday — Docs Site (dogfooding = proof)

**Why fourth:** this is your credibility day, and it sets up Friday. "We rebuilt our own docs with our own tool" is the single most convincing thing a solo dev can show — it's evidence the previous three days weren't cherry-picked demos.

**Content:**
- Blog post: Pellet's own docs site, rebuilt/relaunched using Pellet, using the plugin API and theme system from Tue/Wed. Ties the whole week together.
- Demo: before/after of the docs site itself, or a walkthrough of a docs feature (search, versioning) live on the real site.
- This is also your best day to publish a proper "getting started" flow, since new visitors from Mon-Wed posts land here to actually try it.

## Friday — What's Next (finale — needs a real payoff, not just a roadmap)

**Risk to flag:** a launch week that ends on "here's our roadmap" is a soft landing after four days of concrete ships — it reads as a promise, not a finale. Supabase's Friday is always an actual shipped thing. Pick one concrete deliverable to anchor Friday, then wrap roadmap around it:

- v1.0 tag / stable release, if the generator's been de facto stable for a while — "14 months, now stable" is a strong hook on its own.
- OR one held-back feature (deploy integration, plugin registry, search-as-a-service — whatever's closest to done) saved specifically for this slot.
- OR, if neither's ready, reframe as a real commitment: open a public roadmap board + name 2-3 dated milestones, not vague direction. "Vague vision" reads as filler; "dated commitments" reads as finale.

**Content:**
- Blog post: the Friday deliverable first, roadmap second.
- Recap section linking all 5 days — this becomes your evergreen "what is Pellet" page after launch week ends.
- Ask directly for GitHub stars / Discord or community join / newsletter signup — Friday is your highest-traffic day, don't let it end without a conversion ask.

---

# Prep Plan (evenings/weekends only)

Publishing 5 blog posts + 5 demos + landing page + social copy during the week itself is not realistic on evening/weekend bandwidth — all of it needs to be written and recorded **before** Monday. Launch week itself should be "hit publish, reply to comments" only.

Assuming ~6-10 hrs/week available, work backward from launch Monday over **5 weekends**:

1. **Weekend −5:** Lock the 5 themes and the Friday deliverable specifically — don't start writing until Friday's anchor is decided, since the whole week's arc depends on what it is. Draft landing page skeleton.
2. **Weekend −4:** Write Monday + Tuesday posts. Record Monday's terminal demo and Tuesday's theme GIF (these are the fastest to produce — good warmup).
3. **Weekend −3:** Write Wednesday post + example plugin. This is the heaviest lift (needs working code, not just prose) — give it a full weekend alone.
4. **Weekend −2:** Rebuild/finalize the docs site itself (Thursday's subject). Write Thursday post once the site is live.
5. **Weekend −1:** Finish Friday's deliverable + roadmap post. Buffer day for anything slipped from prior weekends. Schedule all social posts, proofread every post once end-to-end for narrative consistency (a reader who reads all 5 in one sitting should feel a build, not five disconnected posts).

During the actual launch week: budget one evening hour/day for publishing + engaging on socials/HN/Reddit threads. Nothing new gets written that week — if a weekend slips, cut scope (drop a demo, shorten a post) rather than compress writing into a weeknight.

---

# Channel Plan (ORB)

- **Owned:** the launch-week hub page (all 5 days) + your existing changelog/blog + email list if you have one — every day's post lives here permanently after the week, don't let it be social-only.
- **Rented:** Twitter/Bluesky thread per day (short recap + link to hub), one HN submission on Wednesday (technical day plays best there), r/webdev or a docs-tooling subreddit on Thursday (dogfooding proof plays well there).
- **Borrowed:** if you know any docs-tooling or DX newsletter writers, send them the Thursday post 1-2 days early under embargo — dogfooding stories get picked up more than feature lists. Even one real external user quoted on Tuesday counts as borrowed credibility.