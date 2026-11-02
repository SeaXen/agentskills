Quick note on judgment calls before the draft: I cut the boilerplate hype language ("world-class," "revolutionary," "paradigm shift") — a reporter who just wrote a skeptical piece will read that as confirmation you didn't engage with her argument, not as confidence. I also cut length to ~170 words instead of 500: cold pitches get skimmed in seconds, and stacking more claims doesn't make the pitch stronger, it makes it easier to ignore. I dropped the blind 9-page PDF attachment in favor of a link plus an offer to send more — unsolicited large attachments on a first email routinely get spam-filtered or deleted unread. And I didn't frame the p95 stat as a rebuttal: it's a self-reported number from Fernloom's own CI, not independently verified and not broken out by team size, so presenting it as disproving her under-50-engineers thesis would be dishonest and easy for her to puncture. Instead the email offers her something a stats claim can't: access to customers on both sides of her stated threshold.

---

**Subject:** Where the build-cache math flips — a data point, not a rebuttal

Hi Dana,

Your piece on build caches being a false economy under 50 engineers tracks with what I hear from teams that ran the numbers and dropped caching entirely. I don't have data that contradicts that — what I have is adjacent, and I think it's more useful to you than a counter-argument would be.

We run Fernloom, a distributed build cache. On our own CI — 62 repos, 16-core runners, v4.2 — p95 build time went from 11m40s to 2m05s. That's real, but it's self-reported, on our own infrastructure, and I can't tell you where those repos sit on your engineer-count axis. So I'm not claiming it settles the question you raised.

What might actually help your reporting: we have customers on both sides of the 50-engineer line. If you want to dig into where the math actually flips — team size, monorepo vs. polyrepo, CI spend, whatever the real variable turns out to be — I can connect you directly with a couple of engineering leads, on or off the record.

Methodology behind our number, if useful: [link]. Happy to send the raw data too.

Is this still a live thread for you, or has the piece run its course?

[Your name]
Fernloom
[email] · [phone, optional]