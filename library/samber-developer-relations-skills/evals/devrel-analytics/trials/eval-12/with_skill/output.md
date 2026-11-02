## Short answer: no, not as-is. All three have a real problem, and the fixes are different for each.

### 1. "58% talk-to-signup conversion" — ❌ don't publish this number

Two independent defects, not one:

- **Wrong units.** 11 is a count of *people*; 19 is a count of *talks*. A talk-to-signup rate needs signups ÷ people reached (attendees, badge scans, business cards — whatever the actual audience was), not signups ÷ talks delivered. Dividing people by events produces a number that looks like a percentage but doesn't mean "58% of people we talked to signed up" — it means nothing measurable. If a real per-person rate is wanted, the denominator has to be re-derived from however many people were actually met, not from talk count.
- **Below the small-N floor.** Even with the right denominator, 19 and 11 both sit well under this skill's ~30-event floor for reporting a rate at all. Below that, publish the raw list — names/orgs and dates — not a percentage. Small-N percentages swing on one data point and this skill explicitly lists "a percentage computed on fewer than ~30 events" as a claim to refuse.

There's a third, softer issue: "people we met later opened an account" is almost certainly recall, not a traced journey. Talks are an off-web surface with zero automatic collection — nothing links a handshake at a booth to a signup unless a vanity URL, QR code, or a self-reported "how did you hear about us" field was in place at the time. Unless one of those existed, this 11 is anecdotal, not `journey_linked` or even `self_reported` evidence, and the "record nothing when the merge is ambiguous" rule says it shouldn't be presented as attributed fact.

Calling it "our strongest number" is exactly the framing that should trigger extra scrutiny, not less — a metric picked because it's flattering is the first one Goodhart's law comes for.

**What to do instead:** report "19 talks given; 11 named people we can point to who later signed up" as a dated list, unlabeled as a rate. Going forward, plant a vanity URL or QR code per talk and add a stable self-reported source option ("met you at a conference/talk") at signup — then next quarter's number is real instead of remembered.

### 2. Public top-20 answerer leaderboard — ❌ blocked by the privacy gate as scoped

This skill's privacy gate says it plainly: "Publish no per-member leaderboard without consent." The community-health skill repeats it as a named failure mode ("Publishing person-level data. Leaderboards and per-member activity tables create privacy exposure and change behaviour in ways you did not intend"). Handles + answer counts, ranked and public, is exactly that shape — community activity is person-level data by default, and answering a question in a support channel isn't consent to being ranked publicly by name.

There's a second problem sitting underneath the first: raw answer-count is an incentivized volume metric with no quality counter-metric. Rank people on count alone and you'll get fast, thin, first-to-reply answers competing for rank instead of correct ones — the same dynamic that makes "closed issues" produce premature closes.

**What to do instead, pick one:**
- Get explicit opt-in per person before naming them on any public board, and pair the count with a quality signal (e.g., accepted-answer rate, or a "thanks/helpful" react count) so it doesn't reward speed over correctness.
- Or drop the "public, named" part entirely: aggregate ("42 members answered 300+ questions this month") with no names, or recognize top answerers privately (DM, role badge, internal shoutout) instead of a public ranked list.
Also exclude staff/mod accounts from the count before anything ships — otherwise the board just measures the support team.

### 3. Four blog posts/month per advocate — ⚠️ not this skill's call, and the shape is risky

Setting a target is explicitly out of scope here — this skill refuses target-setting requests by design and routes them to `devrel-metrics`, the same way it would refuse "set us a target for docs conversion rate." Two things worth flagging before that conversation happens:

- **Per-person quotas are a named anti-pattern**, not just here: "Per-person metric targets turn colleagues into competitors and pull the work toward whatever is counted." A fixed post-count per head measures the team instead of the program.
- **It's an incentivized volume metric with no counter-metric attached.** The one worked example in the sourced material for exactly this metric (blog-post publish rate, DevRel Foundation Metrics Index) pairs it with organic reads/entries per post for this reason — a flat "4 posts" quota with nothing else will get you 4 thin posts.
- Is "4" derived from this program's own trailing baseline, or is it a round number picked because it sounds reasonable? If there's no baseline yet, the correct move is to mark it "baselining," publish the last three months' actual per-advocate rate, and set a direction/range for the first two cycles — not a fixed point target on day one.

**What to do instead:** take this to a `devrel-metrics` pass — define it as a program-level (not per-head) publish-rate metric, baseline it against the last three months, pair it with a quality counter-metric, and decide who actually owns the threshold and what happens when someone misses it.

---

**Net:** kill the 58% headline, replace with the dated raw list; don't ship the leaderboard without consent or a quality pairing; don't hand out an individual quota without a baseline and a counter-metric. None of these are "close enough" — each one would get flagged the first time someone checks the math or the source.