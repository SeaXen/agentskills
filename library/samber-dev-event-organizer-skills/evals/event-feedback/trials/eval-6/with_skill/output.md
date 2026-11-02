# DataStack Summit, 2nd edition: board update

I did not compute a blended 10-point score. `event-feedback` bars it: satisfaction, return intent and operations answer three different questions, so averaging them gives a number nobody can explain. The board would also read it as a verdict, and the demand verdict belongs to `event-market-fit`, which weighs what attendees did, not what they said.

Your 8.2/10 example is simply 4.1/5 doubled, which is satisfaction alone. Blending in the other two figures moves it with the weights you pick:

| Blend (on a /10 scale) | Result |
|---|---|
| Equal weights: 8.2, 5.8 (58%), 7.2 (3.6/5×2) | 7.1 |
| Satisfaction counted double | 7.4 |
| Return intent counted double | 6.8 |

Any weighting is arbitrary, and the lowest component (return intent) is the one a blend buries.

## Response rates, which set how far to trust each number

| Role | Population | Responses | Rate | Reading |
|---|---|---|---|---|
| Attendees | 700 emailed (of 850) | 210 | **30%** | Top of the 10–30% emailed band, so the collection worked. |
| Attendees, whole event | 850 | 210 | 24.7% | The 150 attendees who were never emailed are unheard. |
| Sponsors | 6 | 2 | 33% | Meaningless as a percentage. Treat by name. |

- Respondents are self-selected. All attendee figures describe the 210 who answered, not the 850 who came.
- The band comes from Explori, a credible source (10–20% typical, 20–30% for a well-designed survey).

## Findings, one number each

| Measure | Result | Benchmark | Status |
|---|---|---|---|
| Overall satisfaction | **4.1/5** | CNCF reports 4.2/5 across its own events, which is context only | ✅ Solid |
| Likely or very likely to return | **58%** | PCMA/Sparks early-warning line is ≥67% | 🟠 **9 points under the line** |
| Operations rating | **3.6/5** | None | 🟠 Lowest score, so the first fix target |

- Return intent is a stated intention, not behavior. Hand it to `event-market-fit` as a qualitative input, never as a demand verdict.
- Free-text themes were not provided, so I can't say why operations scored 3.6. Send me the open answers and I'll group them into counted themes.

## Sponsors: not for the appendix

- Two of six answered, and one of those two ticked **"will not sponsor again."**
- The skill says to treat that answer as a trigger for an immediate phone call. It must not sit in an appendix table.
- 🆘 Action: call that sponsor this week, and hand their verdict to `event-sponsor-fulfillment` now.
- The four sponsors who didn't answer are unknown. Say that plainly. Don't write "50% positive."
- The appendix can hold the sponsor survey detail. The headline sits on the main slide as one line.

## Slide draft

**Title: DataStack Summit 2nd edition: attendees liked it, but fewer say they'll return and operations lagged**

| Measure | Result | Read |
|---|---|---|
| Overall satisfaction | 4.1 / 5 | Strong |
| Likely to return | 58% | Below the 67% warning line |
| Operations | 3.6 / 5 | Weakest area |

**Footer, on the slide itself:** 210 responses from 700 emailed (30%); 850 attended. Self-selected respondents.

**Sponsors (one line, main slide):** 6 surveyed, 2 answered; 1 will not sponsor again. Call scheduled before [date]. Full sponsor detail in the appendix.

**Next steps (3 bullets):**
1. Call the sponsor who declined; report back at the next board meeting.
2. Theme the free text on operations and return intent (counts, redacted quotes).
3. Send the respondents a you-said-we-changed note, because that is what lifts next year's response rate.

**Speaker note:** No composite score is shown on purpose. Satisfaction, return intent and operations answer different questions, and an average would hide the 58%.

## Hand-offs
- **`event-debrief`:** the whole findings summary.
- **`event-market-fit`:** satisfaction and return intent as a qualitative signal only.
- **`event-sponsor-fulfillment`:** the "will not sponsor again" verdict, immediately.
- **`event-continuous-improvement`:** return intent below 67%. This goes through the debrief log, not directly.

## Not answerable from this data
- Why return intent is 58%.
- What the 490 non-respondents think.
- Anything about the four silent sponsors.

The thresholds above are published evidence. The "no blended score" rule and the immediate sponsor call are this skill's own judgment.