**Next action (10 min):** Pull the last 9 issues from your email tool. Export per-issue sends, opens, clicks, unsubscribes, bounces. Do this before you tell the CMO yes or no.

## Verdict

Don't flip to weekly yet. Run a diagnosis, then a gated 6-issue weekly pilot with a lighter format. Weekly with the current inputs fails on two counts:

1. **Supply.** Last quarter gave about 7 original items (4 releases, 2 posts, 1 webinar) across 13 weeks. Weekly needs 13 issues. About 6 slots have nothing to say.
2. **Single point of failure.** Tomasz is the only writer, and nobody else has touched the issue. One sick week or one launch crunch kills the cadence.

Higher frequency also usually lowers per-issue open rate. It won't fix a slide that already exists. Find the cause first.

## Phase 0: diagnose the slide (Oct 26 – Nov 6, about 4h total)

Opens are a weak signal. Apple Mail Privacy Protection inflates them, so the 38% in January may have been partly fake. Check these, in order:

1. **Deliverability.** Look for spam placement, rising bounces, and SPF, DKIM and DMARC alignment. Check Gmail and Yahoo bulk-sender compliance, including one-click unsubscribe. Takes 30 min. This is the most common silent cause of a steady slide.
2. **List hygiene.** Of the 6,200, how many have clicked in the last 90 days? If 40% haven't, the open rate is diluted by dead addresses. Sunset or re-permission them.
3. **Content fit.** Compare click rate per issue against topic. Which issues did the readers who clicked actually engage with?
4. **Subject line and send time.** Compare the best and worst 3 issues.
5. **Baselines to record now:** click rate, click-to-open rate, unsubscribe rate per issue, reply count, newsletter-attributed docs visits and signups (add UTMs if missing).

Output: one paragraph on the likely cause, and a number to beat. Use click rate as the primary metric. Stop treating 38% opens as the target.

## Phase 1: format that fits 3 hours

One fixed template, so each issue is assembly, not invention:

| Block | Content | Time |
|---|---|---|
| Lead | One original item or one release | 60 min |
| Tip | One practical API-observability tip, reused from docs or support tickets | 30 min |
| Links | 3 curated external links, one line of opinion each | 30 min |
| CTA | One action, UTM-tagged | 5 min |
| Subject, QA, schedule | Plus a 15-min second-person review | 40 min |
| Metrics check | Next day | 15 min |

Total: about 3h of Tomasz's time. It only fits if the second reviewer exists.

**Monthly rotation of the lead slot:**

- **Week 1:** release or changelog digest.
- **Week 2:** tutorial or tip from docs.
- **Week 3:** blog post or webinar recap and recording.
- **Week 4:** customer or community story, or a roundup.

**Supply gap.** The original pipeline gives about 2.3 items a month for 4 lead slots. Close the 1.7-item gap with:

- 1 short post a month from engineering, written by Tomasz from a 20-minute interview.
- Support tickets as the source of tips.
- Webinar clips cut into 2 or 3 issues.

Without these, the pilot fills with filler and the click rate drops.

## Phase 2: weekly pilot (Nov 10 – Dec 15)

| Step | Date | Action |
|---|---|---|
| 1 | Nov 2–6 | Write 3 issues ahead. Hold them as a buffer. |
| 2 | Nov 2–6 | Name a second reviewer. Confirm Tomasz really has 3h every week, not 3h a month. |
| 3 | Nov 10 | Send pilot issue 1. Send on the same weekday and time each week. |
| 4 | Nov 10 – Dec 15 | Send 6 weekly issues. Refill the buffer to 2 issues ahead. |
| 5 | Dec 16 | Hold the gate review. |
| 6 | Dec 22 – Jan 5 | Skip sends over the holidays. Resume in January if the gate passes. |

Don't launch weekly on the old list without hygiene done first. The first weekly sends will damage sender reputation if dead addresses are still on it.

## Gate (Dec 16)

The thresholds below are proposals. Set them from your Phase 0 baselines.

- **Go weekly** if all hold: click rate per issue is at or above the baseline, unsubscribe per issue is under 2x baseline, and the buffer never dropped below 1 issue.
- **Fall back to biweekly** if clicks hold but the buffer ran dry or Tomasz exceeded 4h per issue. Biweekly is 2 issues a month with the same template.
- **Return to monthly, plus a short mid-month digest** if unsubscribes exceed 2x baseline or click rate fell more than 20% relative.

Write these rules down now and send them to the CMO, so the result isn't argued after the fact.

## What to tell the CMO

"Top of mind" isn't measured by opens. Report these instead:

- Unique clickers per month. This is engaged reach, and weekly should raise it.
- Newsletter-attributed docs visits and signups.
- Replies and forwards.

## Risks

| Risk | Mitigation |
|---|---|
| Tomasz burns out | Second reviewer, 2-issue buffer, fixed template, 3h cap |
| Filler content lowers clicks | Supply gap plan above. Skip a week rather than send weak content. |
| Reputation damage from frequency | Hygiene first, one-click unsubscribe, watch bounce and complaint rates |
| Weekly becomes permanent by default | Gate review with pre-agreed thresholds |

## Open questions (answer these three)

1. Is Tomasz's 3h available every week, or is that a monthly figure he'd stretch?
2. Who can be the second reviewer, and can engineering give 20 minutes a month?
3. Does your email tool show click data per subscriber? Phase 0 needs it.

**Next:** do the 10-minute export, then answer question 1.