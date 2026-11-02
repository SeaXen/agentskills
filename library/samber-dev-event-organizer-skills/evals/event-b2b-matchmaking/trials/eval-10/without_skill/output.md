# Red flags for Friday's ScaleWorks Expo auto-scheduling launch

I haven't seen the model, the data or the form text. This is a review of the plan as you described it. Nothing here is legal advice.

## Verdict

⚠️ Don't ship it as described. Ship a softer version Friday: auto-propose, then let people confirm. You keep most of the two weeks saved and drop the irreversible parts.

## 🔴 Blockers (fix or cut before Friday)

**1. Enrichment goes beyond what people opted into**
- The opt-in form covered what attendees typed. The company-database data came from somewhere else.
- Under GDPR, you likely owe attendees a notice for data obtained from a third party (Art. 14). It must say what you added, where it came from, and that it feeds profiling for matching. The notice is due within one month, and before first use if you use it to communicate with them.
- Check whether the data is person-level or company-level. Person-level is the bigger problem.
- Check the company database's license. Many forbid this use or redistribution to third parties (the vendors).
- Check whether the join was a fuzzy match on company name. Wrong matches mean wrong firmographics on real people.
- **Fastest safe fix:** retrain or run the model without the enriched features for Friday. Add them back after a notice and an opt-out are in place.

**2. Auto-scheduling ignores capacity**
- Top-3 per attendee gives 500 × 3 = 1,500 meetings across 40 vendor teams. That averages about 37 meetings per team.
- Scores are not spread evenly, so popular vendors will get far more. Their grids will be overbooked or silently truncated.
- Attendees will then show up to meetings that can't happen, or that the vendor never agreed to.
- **Fix:** replace independent top-3 with a capacity-constrained assignment. Cap each vendor's slots, and fill by global score. Run it as a simulation on the real data and check the load per vendor before sending anything.

**3. Meetings land in grids with no consent from either side**
- Attendees opted into the Expo. It's unclear that they opted into having meetings imposed on them.
- Vendors get the attendee's name and profile the moment a meeting is placed. That is data sharing, and you should confirm the form covered it.
- The enriched fields must not flow to vendors unless the notice covers it.
- **Fix:** "Proposed" status with one-click accept or decline. Notify only after the batch is reviewed.

## 🟠 Serious, but can be mitigated in days

**4. No ground truth for "fit"**
- If this is the first event, no outcome data exists (meeting held, follow-up, deal). The model must have been trained on a proxy or on labels someone made up.
- Ask what the label is. If the answer is "tag overlap" or a hand-built score, the 14-feature GBM adds opacity but no validated signal.
- **Cheap check:** hand-review about 30 random attendees and their top-3. Have two people judge "would I take this meeting?" independently. If under about 70% say yes, don't auto-place anything.

**5. Firmographics can skew who gets good matches**
- Company size and funding are strong proxies. Big-company attendees and well-funded vendors rise, and small startups sink.
- Missing enrichment (small or private companies) is a systematic gap. A GBM will treat missing as signal.
- Check feature importance and the score distribution by company-size bucket before launch.

**6. You can't explain a match**
- Attendees will ask "why this vendor?". With a GBM, you need per-match reasons (for example the top 2–3 features, or the shared tags).
- Plain-language reasons in the invite also build the trust that makes people accept.

**7. Free-text "role in their own words"**
- Check how it becomes features: keyword rules, embeddings, or a lookup. Junk and edge cases (empty, non-English, very long) must not crash or distort the score.

## 🟡 Operational gaps to close

- **Irreversibility:** once invites go out, you can't recall them. Do a dry run and a staged send first (about 25 attendees, then everyone).
- **Kill switch:** you need a way to pause the scheduler and wipe proposed meetings.
- **Cancellations and no-shows:** is there rebalancing or re-suggestion? Without it, empty slots pile up.
- **Conflicts:** talks or sessions in the same slot, availability that has gone stale since the form, and time zones.
- **Support load:** decline and reschedule must be self-serve, or the two weeks you saved come back as email.
- **Vendor fairness:** vendors paid and may expect equal exposure. Check the cap and distribution for each vendor, and decide whether you can explain the outcome.

## ✅ What's fine

- Using opted-in profile data to rank fit. That is the purpose people agreed to.
- Automating the first draft of the schedule. The only problem is skipping confirmation.

## Minimum plan before Friday (about 2 working days)

1. Drop the enriched features from the launch model. Retrain and compare. (~half a day)
2. Run the capacity-constrained assignment on real data and check load per vendor. (~half a day)
3. Hand-review 30 matches. (~1 hour)
4. Switch to "proposed" meetings with accept and decline. Send only to a pilot batch first. (~1 day)
5. Check the form text and privacy notice against what vendors will see. (~1 hour)
6. Write a short notice about the enrichment now. Re-enable it after that notice and an opt-out are live.

## Questions that would change my answer

1. What is the model trained on, and what is the label?
2. What exactly did the opt-in form say about sharing profiles with vendors and about automated matching?
3. Is the appended data person-level or company-level, and what does its license say?
4. Are the attendees in the EU (or covered by similar rules)?
5. How many slots does each vendor team really have?