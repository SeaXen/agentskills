**Yes, there are two problems. I'd push back on the plan before the forum opens.**

**1. The site is invisible to Google for six months.**
- Login-required content isn't indexed, so the whole forum disappears from search. [Discourse] [Google]
- Marketing's payoff is ranking threads, and ranking comes from threads that are already public and answered.
- On the day you flip, you start with zero indexed content, not six months of accumulated content.
- Login-required is also friction for askers. Answers are what make a forum valuable, and a login wall makes both asking and finding them harder.

**2. Flipping to public later breaks what members agreed to.**
- People who posted behind a login wall posted for a closed audience.
- Making those threads public afterwards breaches that expectation. [practitioner]
- One forum ended up starting new public categories instead, so the old threads never became public.
- That would mean most of your six months of content could never be ranked anyway.

**Better plan.** Treat counsel's worry ("until we see what people post") as a moderation risk and cover it with targeted controls:

1. **Launch public.** Keep anything a customer contract covers in a restricted category from day one. Decide public versus private per category before launch.
2. **Spam and abuse controls.**
   - Turn on AI spam detection.
   - Add watched words.
   - Block disposable email domains.
   - During a wave, queue only TL0 posts.
   - Use the TL0 limits: 3 topics and 10 replies on day one, 2 links, 0 attachments.
   - Links below TL3 carry nofollow, so spam gets no SEO value. [Discourse]
3. **If counsel still wants a closed phase, make it short and explicit.**
   - Run a restricted founding-member phase of about 2-6 weeks, not six months.
   - Tell founders in the invite that their posts go public on launch day. Seed 5-10 real, answered questions in the two weeks before launch.
   - Everything after launch is public from the first post.
4. **Ask counsel what the actual risk is.** Is it liability for user content, personal data, customer confidentiality, or brand safety? Each one has a narrower fix than closing the whole site:
   - Terms of service and posting guidelines.
   - A takedown and flag process.
   - Restricted categories.
   - A moderation ladder. For that, see `samber/developer-relations-skills@developer-community-moderation`.

**Two caveats.**
- Don't sell marketing a fixed traffic figure. Forum search traffic swings with core updates, so sell answered questions first and search as upside. [practitioner]
- I haven't seen your admin settings. I haven't checked what your hosted plan allows for AI spam detection, Solved or SSO. Check the live values before committing to any of the above.

**Questions that would sharpen this:**
- What exactly is counsel worried about?
- Who will answer questions daily, and for how many hours a week?
- Is any content contractually private?

If you want, I can turn this into a one-page note for counsel and marketing.