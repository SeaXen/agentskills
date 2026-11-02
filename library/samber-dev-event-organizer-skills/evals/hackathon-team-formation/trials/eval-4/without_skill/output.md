# Team assignment plan for Tallgrass Hack

**Recommendation:** Add the question now, but make assignments **tentative teams announced about 48 hours before**, not the night before. Allow swaps at kickoff. Last-minute hard assignments fail because of no-shows and unanswered forms.

## 1. Why not hard-assign the night before

- ⚠️ **No-shows.** Free events often lose 30–50% of signups. Teams built from signups will have holes by morning.
- ⚠️ **Unanswered questions.** Free-text responses won't come from everyone. Some of your 160 solos will never answer.
- ⚠️ **No time to react.** An assignment sent the night before leaves no room to fix a mismatch or let people meet first.
- ℹ️ **Ownership.** Forced teams care less than teams that chose each other. An opt-out and a swap window fix most of this.

## 2. Form changes (do today)

Use structured fields, not just free text. Structured fields are what you can match on.

1. **Team status** (required): "I have a team", "I'm solo, match me", or "solo, but I'd rather find people myself".
2. **Team name or code** (if they have a team): so you can group the 80 already-teamed people.
3. **Roles** (pick up to 2): backend, frontend, design/UX, data/ML, hardware, product/pitch.
4. **Experience level** (1–3).
5. **Theme interest** (multi-select from 3–5 themes).
6. **Idea status**: "I have an idea", "I want to join an idea", or "open".
7. **Free text, optional**: "What do you want to build?"
8. **Full-event availability**: yes or no.
9. **Consent line:** "We use your answers only to form teams and delete them after the event." Required for GDPR.

📌 Your 240 existing signups are already registered, so **send them a short follow-up form today**, with a deadline 3 days before the event. New signups answer in the main form.

## 3. Matching rules

**Team size:** target 4, allow 3–5. 160 solos make about 40 teams of 4.

**Hard constraints:**
- Every team has at least one person who can build, such as backend, frontend, or data.
- Every team has at least 2 distinct role areas.
- Beginners (level 1) are spread out. No team is all beginners.
- Pre-formed teams stay together. Top up a team of 2–3 with solos only if they opted in ("open to extra members").

**Soft score:**
- Same theme interest: highest weight.
- Complementary roles.
- Idea owners are seeds. Assign "want to join an idea" people to a seed that matches their theme and fills a missing role.

**Method:** a short script or spreadsheet is enough. Pick seeds, assign greedily by score, then review the result by hand. 240 people is small enough for a person to check every team in about an hour.

💡 Free text is hard to match on directly. Classify it into role and theme tags first. A Typesafe/Jev call fits here, since it's a judgment on natural language.

## 4. Handling the gaps

- **Unanswered solos:** put them in an **unmatched pool**. Leave 1 open slot in about a third of teams as floaters for them and for no-show fill.
- **Broken pre-formed teams:** a team that loses members at check-in becomes solos. Run a **floater desk** at check-in.
- **Overbooking:** don't over-assign. Teams of 4 that lose one member are still viable teams of 3.

## 5. Timeline

| When | Action |
|---|---|
| Today (D−10) | Add the question. Email the 240 existing signups the follow-up form. |
| D−10 to D−3 | Send a reminder at D−6 to non-responders. |
| D−3 | Lock answers. Registration has closed. |
| D−3 to D−2 | Run matching and review by hand. |
| D−2 | Email each person their tentative team, with a team chat channel (Discord/Slack), a one-line intro of each teammate, and an **opt-out or swap link**. |
| D−1 (night before) | Reconcile swap requests and confirmations only. No new matching. |
| Check-in | Mark no-shows. Merge broken teams. Send the unmatched pool to the floater desk. |
| Kickoff | Run a 30–45 minute **swap window**: 60-second idea pitches, then people may switch teams. |

## 6. Open points

- **Team size cap:** does the venue or judging limit teams to 4 or 5?
- **Themes or tracks:** if you have none, theme interest drops out and idea status becomes the main signal.
- **Expected no-show rate:** if you have data from past events, use it to size the floater slots.