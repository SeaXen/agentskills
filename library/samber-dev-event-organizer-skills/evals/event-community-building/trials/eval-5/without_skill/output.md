# KernelDays points system: review

**Verdict:** the goal is right (keep the forum alive between editions). Three parts of the design need to change before launch: the rank-by-volume scoring, the public top-3 photos, and the "points lead to organizer" ladder.

## 🔴 Fix before launch

1. **Don't score volume.**
   - Points for posting reward noise. A systems-programming crowd will game it quickly, or script it. LLM-written filler is now cheap too.
   - Score outcomes instead:
     - accepted or upvoted answers, counted from *distinct* users
     - a first reply to a newcomer's thread
     - a thread that gets resolved
   - Cap points per day, and give none for self-reactions or reactions from alt accounts.
   - Let moderators revoke points.

2. **Don't publish top-3 photos by default.**
   - Names and photos are personal data under GDPR, and Finland is in the EU. You need explicit, opt-in, withdrawable consent per person, per edition.
   - Featuring people publicly also exposes them to harassment and unwanted recruiter contact. Some strong contributors are pseudonymous on purpose.
   - Offer handle only, handle plus avatar, or full name and photo. Let the winner choose.
   - Photos also pressure people to post more, and they skew who shows up (people with time, people already visible).

3. **Vet the volunteer's prototype bot before it touches real data.**
   - Check its permissions, how it stores tokens and secrets, who can run it, and where the points database lives. Check retention and whether it can be deleted.
   - Name an owner and a backup person, because volunteers disappear.
   - Prove the scoring logic with tests, since it will decide who gets public recognition.

4. **Treat "Community Champion" as an endorsement.**
   - The title carries your brand. Tie it to conduct as well as points: no code-of-conduct strikes in the period, and a moderator veto.
   - Publish the criteria. Opaque rules turn disputes into drama.

## 🟠 Design changes

- **Monthly leaderboard:** the reset punishes anyone who was busy for a month. It also hands the top spots to whoever has the most free time.
  - Option A: no ranking. Use badges and a "contributors this month" list, in alphabetical order.
  - Option B: a ranked board, but only the top 10 are visible, opt-in, and counted on a rolling 90 days.
- **Badges:** make them typed, not tiered by count. Examples: *Answered*, *Reviewed a CFP draft*, *Welcomed a newcomer*, *Shared a post-mortem*, *Wrote a talk recap*. People see which behaviors you value.
- **Levels:** keep levels few, three or four. Unlock privileges that matter to this audience, such as early access to CFP feedback, a speaker Q&A, or a ticket discount code. Don't unlock cosmetic titles alone.
- **Seasons:** align them to the conference cycle. For example, run a "pre-CFP", a "pre-event" and a "post-event" season, each with its own badge set. That keeps the forum moving across the year.

## 🟠 The organizer ladder

Points do not measure organizing ability. Posting a lot and running a venue, sponsor, or schedule are different skills. A top-ranked poster can burn out as a volunteer, and a quiet person with strong logistics skills never ranks.

Use points as one signal and add explicit steps:

1. Reaching level N triggers a personal invite from a human organizer. It does not grant access automatically.
2. Offer small, bounded tasks first: moderate one subforum for a month, review CFP submissions, or run a speaker Q&A thread.
3. Shadow an organizer for one edition cycle.
4. Then offer a named role with a clear time commitment.

Also publish the roles and time cost up front, so "volunteer" doesn't read as "free labor". Ask outgoing volunteers what burned them out.

## ℹ️ Tell me before you build

- What exactly is dying: replies, new threads, or returning members? Pick one metric before you pick mechanics.
- How big is the forum? Under about 200 monthly actives, a leaderboard looks empty and a few people win every month.
- Who moderates, and who handles score disputes?
- Is there a code of conduct and an enforcement history to tie the title to?

## ✅ Suggested rollout

1. **Weeks 1-2:** a bot security review, plus a consent form and a scoring spec on one page.
2. **Weeks 3-4:** shadow mode. The bot scores quietly and nothing is shown. Read the results and see who would have "won".
3. **Weeks 5-12:** a pilot with badges and an opt-in board, no photos.
4. **Week 13:** compare against your metric. Add Champion titles and homepage features only if quality held up.

Without that comparison, the points system is a guess.