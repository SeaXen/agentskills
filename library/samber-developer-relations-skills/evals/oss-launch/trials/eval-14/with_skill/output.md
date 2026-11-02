Read the oss-launch skill and its Step 5 (channel-playbook.md) and Step 7 (measurement-plan.md) references, which is exactly where this question routes per the skill's own invocation table. Here's the answer.

---

## Short answer: no honest number exists, and your plan works against the mechanic

**How many stars/day to hit the front page:** I can't give you one, and any number you find online is folklore. GitHub has never published the Trending selection formula. The skill's own reference is explicit on this: "treat any reverse-engineered version as folklore and never promise a trending placement." Every "you need X stars/day" figure circulating in blog posts traces back to someone's single anecdote or a launch-consultancy's marketing copy, not to GitHub. Adopting one as a target just means you get judged against fiction later.

**What's actually documented about the algorithm:** GitHub Trending ranks repositories by stars *gained inside a rolling window* — today / this week / this month — not cumulative stars, and it's filtered by language. That's it. That's the entire public surface. Everything else (weighting by unique starrers vs. bots, contributor diversity, velocity-relative-to-history) is reverse-engineered guesswork with no confirmation from GitHub.

One real, usable fact: **your realistic target is the Rust language Trending page, not the global one.** The global page pools every language; the Rust page is a much smaller sample, so the star-velocity needed to clear it is meaningfully lower. That's the honest target to aim for, not a specific daily count.

## The bigger problem: your 14-day drip plan is the documented anti-pattern

This is the part worth stopping on. Trending samples a *window* — day, week, month. It rewards a slope inside one of those windows, not a total accumulated over fourteen days. The skill states this directly: "the same effort compressed into one day produces the slope these surfaces reward, while a week of drip produces none." Spreading Reddit → Tuesday tweet → Wednesday Lobsters → ... across two weeks means you never produce a concentrated spike inside *any* single day or week window — you produce fourteen small, independent blips, each too small to register, and none of them compound into the others because by the time Wednesday's Lobsters post lands, Monday's Reddit thread has already decayed.

There's a second mechanism working against you, separate from Trending: discussion platforms themselves rank on *early engagement density*. A Reddit post, a Lobsters post, and a tweet fired on different days each start from zero momentum and die alone. The skill's rule is "pick one anchor channel and treat everything else as amplification pointing back to it" — because "four simultaneous primary posts produce four dead threads." Your plan isn't simultaneous, it's sequential, but it has the same root flaw: every channel is being treated as its own primary launch instead of one channel carrying the story and the rest linking back to that one thread.

Two weeks of steady posting also isn't justified by what you have. A multi-day "caravan" sequence (Supabase Launch Week-style) only earns its cost past a specific bar: **at least three separate announceable items, a fixed date like a conference, and a named owner per day.** A single crate release doesn't clear that bar — you'd be running caravan-level effort for spike-level content, which the skill ranks as worse than doing nothing: "a caravan dilutes into several ignored posts" below that threshold.

## What to do instead

**Collapse this into one spike, fired inside a single day, with amplification in the hours after — not new channels on new days:**

1. **T-0h:** Repository, crates.io listing, README, and any linked docs must all be in a state a stranger can follow unaided — this is the actual precondition the skill gates on before any date is set (a broken install command becomes the top comment, permanently).
2. **T+0, one anchor:** Pick one. For a Rust crate doing zero-copy protobuf decoding, you have two reasonable anchor candidates, not five:
   - **r/rust** — you're ecosystem-bound, and this is where Rust developers already evaluate new crates.
   - **Hacker News or Lobsters** — zero-copy protobuf decoding is general infra/dev-tooling with appeal past just Rust users, which is the profile that channel-playbook.md routes to a general aggregator instead.
   Pick based on where you already have real account history — a first-ever post that's a self-link reads as spam regardless of quality.
3. **T+0, immediately:** Your own top-level comment on that thread — who you are, why it exists, what's interesting under the hood (the zero-copy technique is your real differentiation — lead with it), what it doesn't do yet.
4. **T+30–90min:** Your own Twitter/social post, linking to the *discussion*, not duplicating the announcement.
5. **T+2–6h, same day:** Secondary communities — Lobsters (if not your anchor), a relevant Discord/Zulip, This Week in Rust submission — staggered, with the context rewritten for each. Never paste the same blurb twice; it reads as a bot and gets removed on sight.
6. **Same week:** Newsletter/curated-list submissions (This Week in Rust digest, etc.) — these publish on their own schedule regardless of what day you submit.

That's the whole spike: one day of concentrated firing, not fourteen days of drip. If you have a real second story — the zero-copy design decisions, benchmark methodology, why this differs from prost/protobuf — that's legitimate week-two content as a long-form write-up, not a repeat of the same launch announcement on a new platform.

## One hard boundary your plan needs to respect

Don't read "steady stream of stars" as license to ask anyone to star, upvote, or comment, or to coordinate it across accounts. Hacker News explicitly penalizes the submission, the account, and sometimes the whole domain for vote solicitation; Product Hunt discounts inauthentic engagement by design. Sharing the launch and asking people to "go look" is fine — asking them to star it is not, and both platforms detect coordinated patterns even when you don't get caught in the moment.

## Before you fire anything

Snapshot your baseline *tonight*, not after: current stars (11), crates.io downloads for the last full week, any existing referrer data. Traffic panels only keep a short rolling window, so an uncaptured baseline is unrecoverable — you won't be able to tell a real spike from noise without it. Then judge success at three points, not one: Day 1 (did the anchor thread get engagement, not just stars), Day 7 (did crates.io downloads move against last week), Day 30 (did downloads stay up, or was it a one-day curiosity spike). Stars are the loudest and least meaningful number in that set — treat a stars spike with no download movement as the announcement traveling without the project traveling with it.