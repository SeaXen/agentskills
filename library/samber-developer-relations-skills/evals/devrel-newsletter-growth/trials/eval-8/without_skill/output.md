**Likely cause:** the signup box promises something the newsletter doesn't deliver. This is a strong hypothesis, not yet confirmed. Don't go weekly yet.

## What the data says

- People who leave after 1–3 issues are expectation mismatches. They signed up for "weekly Go performance tips" and got a monthly product update. They leave on the first or second issue.
- Long-time subscribers aren't leaving much. If they were, the cause would be fatigue or content decay.
- Going weekly with product updates sends four times as much of the wrong content to people who wanted Go tips. That should raise unsubscribes and spam complaints.

## One gap in the story

The mismatch is about a year old, but unsubscribes only doubled over six months. So something else probably changed too. Candidates:

- **More signups.** The docs box got more traffic or a better placement. Raw unsubscribe counts then rise even if the rate stays flat.
- **A content or format change** in the newsletter.
- **Deliverability or complaints.** Spam-complaint rate above about 0.3% hurts delivery at Gmail and Yahoo.

Check these before you commit to the story.

## Do this

1. **Pull unsubscribe rate, not count (about 30 min).** Compute per send, split by subscriber tenure (1–3 issues vs 4+) and by signup month. Compare the rate with signups per month.
   - If the rate is flat and signups doubled, the problem is smaller than it looks. The mismatch is still real.
   - If new-cohort rate is high and old-cohort rate is flat, the mismatch is confirmed.
2. **Check complaints and unsubscribe reasons (about 15 min).** Look at the spam-complaint rate in your email provider. Read any free-text unsubscribe reasons.
3. **Fix the signup box today (about 5 min).** Change it to say "Monthly product updates from the Fernhollow team". This stops new people from joining under a false promise.
4. **Decide which promise you keep.**
   - **Option A (recommended): keep it monthly and honest.** Add one Go performance tip or deep-dive per issue. This honors the original promise and keeps monthly product updates. Cost: about half a day per issue.
   - **Option B: make the Go tips real.** Run two lists, "Go perf tips (weekly)" and "Product updates (monthly)", and let people choose at signup. Cost: engineers must write weekly. Only do this if they will, and if it's useful, because a weekly list that decays is worse than none.
5. **Send existing subscribers a one-time preference email (about 1 hour).** Ask whether they want tips, product updates, or both. Don't re-permission the whole list; a few unsubscribes here is better than silent churn.
6. **Test weekly with data, not argument (4–6 weeks).** After the copy matches the content, send weekly to a random 10–20% group and keep the rest on monthly. Compare unsubscribe rate, opens, clicks, and docs or product visits. If weekly wins on engagement and the unsubscribe rate stays level, roll it out.

## What to tell the CEO

- "Top of mind" works only for people who want what you send. Right now new subscribers get something different from what they signed up for.
- More frequency multiplies the mismatch.
- Here is the plan: fix the promise this week, then test weekly on a holdout. If weekly wins, you ship it with evidence.

**Next:** run step 1. It takes about 30 minutes. Paste the unsubscribe rate by tenure and signup month if you want me to read it with you.