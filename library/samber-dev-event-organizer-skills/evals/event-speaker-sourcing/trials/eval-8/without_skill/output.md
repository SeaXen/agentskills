**Do this first (10 min):** stop binning the old spreadsheet. Add an `edition` column and keep one append-only table across years. Your three metrics don't fix the real gap, which is that you have no history to compare against.

## What your three metrics miss

Your plan:

- **Combined social reach:** it measures speaker fame, not sourcing quality. It only goes up, it double-counts overlapping audiences, and it can't say whether the people showed up or were good. Cut it, or keep it as a label only.
- **Invitations sent:** this is effort. It tells you what you did, not what you got.
- **Average response time:** the mean is skewed by outliers, and non-responders drop out of it. The speakers who ghost you are the data you most need. Use the median, and count non-response as its own number.

The biggest hole: **none of the three would have warned you about the keynote cancellation.** You measure getting speakers, not keeping them.

## Proposed sheet (7 metrics)

1. **Funnel by channel.** Track invited → replied → accepted → confirmed → delivered. Tag each speaker with a channel: personal referral, past speaker, open CFP, cold outreach. This replaces "invitations sent". It tells you which channel to spend time on next year. *(Primary.)*
2. **Delivery rate.** Confirmed speakers who actually spoke, divided by confirmed. Add cancellation lead time in days for every dropout. Your keynote is the data point at 6 days. *(Pair with metric 1, so a volume push can't hide flakiness.)*
3. **Confirmation depth.** A "yes" is not one level. Record the stage: verbal, written, travel booked, slides received. Set dated checkpoints, for example T-90, T-30 and T-14 days. A speaker stuck at "verbal" at T-30 is your early warning.
4. **Bench coverage.** The share of slots with a named backup, with the keynote first. Add replacement time, meaning how many days it takes to fill a vacated slot. A cancelled keynote only sinks the day if you have no reserve.
5. **Median days from invite to confirmed.** Track it next to the non-response rate. Both are cheap and need no extra tooling.
6. **Decline reasons.** Code every decline: date, fee, travel, topic, no reply. This costs one column and is the most useful sourcing data you will collect.
7. **Outcome per speaker.** Choose one:
   - session rating from attendees, or
   - registrations that came from a speaker-tagged link.
   
   Add a one-line "how did you hear about us" question on the ticket form. This is what tests whether reach predicts anything. Correlate reach against rating and delivery rate on your own data. If reach doesn't predict them, drop it with evidence. Big-name speakers may even cancel more often. That is a hypothesis to test, not a fact.

Optional, for long-term health:

- **Speaker mix:** new vs returning, region, topic coverage.
- **Would-return score:** a one-question speaker survey after the event.
- **Cost per confirmed speaker:** fees, travel and your own hours.

## Rules to write down now

- **Attribution rule, before the period starts.** "Came because of speaker X" is self-reported unless a tagged link proves it. Say which you use.
- **Small N.** Under about 30 speakers, report raw lists with dates, not percentages. One edition is one data point, so read it as a list, not a rate.
- **Thresholds:** none yet. You have no baseline. Mark every metric "baselining" this year and set ranges after edition 3, using your own numbers. Don't borrow another conference's figures.
- **Every metric gets an action.** Example: if confirmation depth is "verbal" at T-30, escalate and activate the backup. A metric with no action gets cut.
- **Kill rule.** Remove any metric that changed no decision in two cycles.

## Data retention (you're in France)

Binning the old sheet may have been a GDPR reflex. Keep the history without keeping the personal data:

- Keep: speaker ID, channel, dates, stage reached, decline code, outcome.
- Delete: names, emails, handles after a set retention period.

This keeps the baseline and drops the personal details.

## Gaps I can't fill

- Editions 1 and 2 are probably gone. Rebuild what you can from email and the old sheet, and mark those rows low-confidence.
- Edition 3 is the first real baseline. Edition 4 is the first one you can compare against.

## Next action

Create the table with columns `edition, speaker_id, channel, invited_on, replied_on, stage, confirmed_on, delivered, cancel_days_before, decline_code, backup_named`. Backfill the keynote's row first. Reply with how many speaker slots you have and who owns the sheet, and I'll set the checkpoint dates for the 5 months left.