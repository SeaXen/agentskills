# Launch plan — Pellet (5-day launch week)

## Assumptions I filled in without asking

You asked for the five days directly, so I inferred the rest instead of interviewing you turn by turn. Correct anything wrong here before you lock a date — these drive the whole plan:

- **Audience**: both — individual devs picking a docs tool for themselves, and teams evaluating it for a product's docs site. That's why company-adoption assets (comparison table, maintenance/funding honesty) show up below, not just a quickstart.
- **Replaces**: Docusaurus, MkDocs+Material, Hugo, Sphinx, mdBook, VitePress/Starlight, Nextra, GitBook. This is a **crowded category** — more on that under Risks.
- **No company, no fixed external date** (no conference, no funding announcement) — this is a self-imposed launch week.
- **Solo maintainer, evenings + weekends only** — this is the constraint that shapes everything below, more than the five themes do.
- **Timezone**: Europe (Paris), unconfirmed. The posting-hour recommendations assume this — shift them if wrong.

## Verdict: go with reduced scope, pending two gates

I can't run these for you sight-unseen, so treat them as open until you confirm:

- **Step 1 (name/license clearance)** — "Pellet" is a plain English word; if you haven't done a trademark/existing-project search plus secured the GitHub org, domain and package-registry name, do that before anything below gets a date. Rename-after-visible is the one mistake on this list you can't undo.
- **Step 2 (readiness gate)** — run the cold-run protocol yourself: fresh directory, README only, no source-diving. If a stranger can't get from clone to visible output inside the time your README claims, that's the top HN comment on Monday, not a launch.

Everything else below assumes both pass.

## Shape check: does this clear the caravan bar?

The skill's threshold is three conditions, not two: 3+ announceable items, a conference-or-fixed-date, and someone to own each day.

- Items: you have five (core, plugin API, themes, docs site, roadmap) — clears easily.
- Fixed date: **you don't have one.** No conference, no external deadline. This is the weak leg of the stool. Fix it by tying Friday to something real — cut an actual v1.0 tag that week, or pick the date and treat it as fixed once announced — rather than running the week on vibes alone.
- Owner per day: solo is fine here — "named owner" doesn't mean a different person, it means someone is actually staffing that day. You, every day, is a valid answer as long as you don't also have a day with nobody watching.

Verdict: proceed, but the missing external date is a real gap, not a formality — note it in your own head as the thing most likely to make you skip Wednesday when you're tired.

## The five days

| Day | Theme | Why this order |
|---|---|---|
| **Mon** | The generator itself | Anchor day — answers "what is it, do I have this problem, why not Docusaurus/MkDocs/Hugo" |
| **Tue** | Plugin API | "How it extends" — technical depth for the power users the anchor thread attracts |
| **Wed** | Theme system | Visual/demo day — screenshots and GIFs carry this one, not prose |
| **Thu** | Docs site (dogfooded) | Proof day — "we built our own docs with it," strongest signal for company adopters |
| **Fri** | What's next | Finale — roadmap, governance honesty, week recap, the durable write-up |

This sequence (intro → extend → customize → prove it → where it's going) is the same arc Supabase and Cloudflare's Innovation Weeks run for a reason: each day answers the question the previous one raised.

### Monday — the anchor, and the only day that gets a Show HN

This is the one channel-mechanics decision that overrides everything else: **one Show HN for the whole week, not five.** HN's duplicate detection and per-domain weighting are invisible from outside — five submissions from one project in one week reads as spam even if every post is genuinely different content, and the penalty is silent. Don't repeat this on Product Hunt either; pick it for one day only (Monday or Wednesday, not both — a visual theme-gallery post is actually a better PH fit than the core-generator post if you want to use it there instead).

- **Anchor channel**: Hacker News (Show HN), assuming Pellet isn't tied to one specific language ecosystem — if it is (a Rust-only tool, a Go-only tool), swap to that ecosystem's subreddit/forum instead per the channel table.
- **The one-liner** needs the real differentiator filled in, not a placeholder: `Pellet is a static site generator for technical docs that <the specific thing Docusaurus/MkDocs/Hugo don't do>`. If you can't finish that sentence with something concrete and checkable, that's the actual blocker for Monday — worth more of your remaining prep time than anything else on this page.
- **Comparison table**: name real alternatives, lose at least one row honestly (install size, build speed, plugin count, whatever you actually lose on). A table where you win every row gets read as marketing and discredits the rest of the post.
- **Run of show** (see timing note below): post, first comment within a minute (who you are, why it exists, what's interesting under the hood, what it doesn't do yet), stay in the thread 3-4 hours.

### Tuesday — Plugin API

- **Content**: a working example plugin, the architecture decision behind the API shape, what plugin authors can't do yet.
- **Channels**: your own blog post + your own social thread + one secondary community picked for fit (not a generic dev forum — wherever people who'd actually write a Pellet plugin already hang out). Don't paste the Monday blurb here; rewrite the context for this audience.
- If someone in the still-open HN thread asks "can it be extended?", answering with a link to this post is fine — starting a second HN submission for it is not.

### Wednesday — Theme system

- **Content**: this is the demo day — a theme gallery, a GIF of switching themes live, a short "build your own theme" walkthrough. Prose carries this one the least of all five days.
- **Channels**: own blog + social (image-led) + one secondary community with visual/frontend overlap. This is also the natural slot for Product Hunt if you're using it at all, instead of Monday.

### Thursday — Docs site (dogfooding)

- **Content**: publish Pellet's own docs site as the artifact, and be honest about what broke while building it. This is the day that does the most work for the company-adoption reader — "production track record" is the row on the comparison table that a lone maintainer struggles to fill, and this is how you fill it.
- **Channels**: own blog + social + a community actually populated by technical writers, not just developers (this audience cares about docs tooling specifically and is under-served by the other four days).

### Friday — What's next (finale)

- **Content**: the roadmap, and — deliberately — the governance question nobody likes stating out loud: you're a solo maintainer, so say what that means (response time you can actually hold, what happens if you go quiet, any funding/sponsorship situation). Readers forgive a stated limitation; they don't forgive discovering one later. This is also where the durable long-form write-up belongs — normally that asset loses every scheduling round because it costs a week you don't have, but Friday is built to carry it, so use it here instead of skipping it.
- **Channels**: long-form post + social recap thread linking all five days + this is when newsletters and curated lists you submitted earlier in the week actually publish. A second HN post is optional and risky (see duplicate-detection note above) — only do it if Friday's content is genuinely a new artifact, and otherwise save the "mail the mods" second-chance-pool option for if Monday underperformed, not as a standing Friday plan.

## Fitting this into evenings and weekends

This is the actual hard constraint, more than the content plan:

- **Two weekends before launch week**: this is where all five posts get written, the cold-run protocol gets run, comparison tables and screenshots get built, and the readiness gate gets cleared. None of that belongs in the launch week itself.
- **Weeknight posting window**: derived, not folklore — Paris evening (roughly 18:00-21:00 CEST) overlaps US East Coast late morning through early afternoon and US West Coast morning, which is inside a US reader's working day, not outside it. This is a real overlap you can compute for your own timezone, not a canonical "best time to post HN" — the skill is explicit that those hardcoded claims are invented.
- **The daytime gap**: you'll be offline for the hours between your evening post window and the next evening, which is exactly when a US morning reader might ask a valid technical question and get silence for 12+ hours. Mitigate with a short lunch-break check-in each day rather than trying to be present all day — a 10-minute reply beats a 12-hour gap.
- **Weekend after launch week**: second wave — newsletters that missed the cycle, any secondary community you deliberately skipped during the week, first triage pass on issues the launch surfaced, cut a release if fixes came out of it.

## What to cut first if the week gets too heavy

Delete, don't demote — a deprioritized task just reappears as Thursday-night scope creep:

1. Cut the daily secondary-community post before anything else. Two well-placed posts (Wednesday to a visual/frontend community, Thursday to a docs-writing community) beat five generic ones squeezed in after a full day.
2. Cut newsletters to a single batch submission early in the week, not five.
3. Never run Product Hunt on more than one day — it isn't built for a multi-day cadence, and it's the first thing you can drop entirely without losing much (the channel table ranks it secondary for a dev tool anyway).
4. If Tuesday or Wednesday visibly dies, don't force the same intensity through Thursday — the finale on Friday is the day that most needs your energy, since it's the one carrying the durable asset.

## Risks specific to this plan

- **The crowded category is the real risk, not the schedule.** A sharp, specific "why not Docusaurus/MkDocs/Hugo" answer matters more than any hour-of-day decision on this page. If that answer is still vague, fix it before picking a date.
- **No fixed external date** weakens the caravan justification the skill sets as a threshold — tie Friday to something real (an actual version tag) rather than running purely on a self-imposed calendar.
- **Five consecutive launch days, solo, evenings-only, is a real burnout setup** — Tidelift's maintainer surveys put burnout at 46-58% even outside launch weeks. Decide now, not on Wednesday night, what "I'm skipping the secondary post tonight" looks like so it's a plan, not a failure.
- **Silent unstaffed daytime hours** on a launch thread read as absence to a reader who doesn't know your day job exists. The lunch check-in is the cheapest fix.

## Measurement

Capture the baseline Sunday evening before Monday: stars, unique clones, registry downloads for the prior full week, docs sessions, current referrer mix. Store it outside the traffic panel — it's a short rolling window and won't survive to compare against later.

Read Day 1 as attention, Day 7 as trial, Day 30 as adoption — and specifically watch what Tuesday-Thursday's referrer traffic looks like against Monday's. That comparison is the one that tells you, next time, whether five days actually outperformed a single well-run spike for a solo maintainer, or whether the extra four days mostly cost you evenings for a rounding error in reach.