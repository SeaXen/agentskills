# Brightloop Conf CFP: Submission Form (final)

## Changes from your draft

| Your request | Decision | Why |
|---|---|---|
| One unlimited text field | ❌ Replaced with structured fields, each with a character limit | A single free-text box gets you uneven proposals that are hard to compare. Reviewers can't score what they can't find. |
| Lightning talks | ❌ Not offered | Your program has only 30-minute talks and half-day workshops. A lightning slot would have no place in the schedule, so every acceptance would be a rejection or a program change. If you want them, add the slots to the program first, then add the format option. |
| 1-10 audience self-rating | ❌ Replaced with 3 named levels | Speakers can't calibrate a 1-10 scale. Most pick 6 or 7, so it tells you nothing. Named levels with a one-line definition work better. |
| Unlimited proposals | ⚠️ Capped at 3 per speaker | Unlimited submissions add review load and mostly add duplicates. Three keeps volume healthy and gives each speaker a clear "pick your best" prompt. |

## Form

**Intro text (top of form)**
> Brightloop Conf is a 400-person frontend conference in Manchester. We accept **30-minute talks** and **half-day workshops**. You can submit up to **3 proposals**; use one form per proposal. Speaker details are collected once per submission, so reuse them. Reviewers see all fields.

### Section 1: Speaker

| # | Field | Type | Required | Limit |
|---|---|---|---|---|
| 1 | Full name | Short text | Yes | 100 chars |
| 2 | Email | Email | Yes | Validated format |
| 3 | Speaker bio | Long text | Yes | 600 chars. Help text: "Third person. Used on the website if accepted." |
| 4 | Company / affiliation | Short text | No | 100 chars |
| 5 | Links (website, GitHub, social, past talk video) | Short text | No | 3 URLs |
| 6 | Speaking experience | Single select | Yes | First time / A few meetups or small events / Regular conference speaker |

### Section 2: Proposal

| # | Field | Type | Required | Limit |
|---|---|---|---|---|
| 7 | Format | Single select | Yes | **30-minute talk** / **Half-day workshop (3-4 hours)** |
| 8 | Title | Short text | Yes | 80 chars |
| 9 | Abstract (public) | Long text | Yes | 800 chars. Help text: "What the audience will learn. This text appears in the program if accepted." |
| 10 | Details for reviewers (private) | Long text | Yes | 1,500 chars. Help text: "Outline, key points, demo plans, why you're the right person. Not published." |
| 11 | Audience level | Single select | Yes | See below |
| 12 | Topic area | Single select | Yes | Frameworks & rendering / Performance / Accessibility / Design systems & CSS / Tooling & build / Testing / AI in frontend / Other |
| 13 | Key takeaways | Long text | Yes | 3 bullets, 300 chars total |

**Audience level (field 11)**
- **Beginner**: assumes basic HTML/CSS/JS knowledge only.
- **Intermediate**: assumes you ship frontend code professionally.
- **Advanced**: assumes deep experience with the topic.

**Workshop-only fields (shown only if field 7 = workshop)**

| # | Field | Type | Required | Limit |
|---|---|---|---|---|
| 14 | Max participants and prerequisites (laptop, installs) | Long text | Yes | 400 chars |
| 15 | Hour-by-hour plan | Long text | Yes | 800 chars |

### Section 3: Logistics and consent

| # | Field | Type | Required |
|---|---|---|---|
| 16 | Has this talk been given before? (where, when) | Short text | No |
| 17 | Travel or accessibility needs we should know about | Long text (300 chars) | No |
| 18 | I agree to the code of conduct | Checkbox | Yes |
| 19 | I agree that Brightloop Conf may record and publish my session if accepted | Checkbox | Yes |
| 20 | I agree to the privacy notice (data used only for CFP review and speaker communication) | Checkbox | Yes |

## Rules to configure

- **Submission cap:** 3 per email address. Show a clear error on the fourth: "You've reached the limit of 3 proposals."
- **Confirmation email:** send on submit with a copy of the answers and the notification date.
- **Editing:** allow edits until the CFP closes, via a link in the confirmation email.
- **Reviewer view:** show fields 8-13 (plus 14-15 for workshops) first. Consider hiding name, bio, and links for a first scoring pass.
- **Deadlines:** the form needs an open date, close date, and notification date. I didn't have yours, so I left them out of the intro text. Add them under the intro.

## Open questions for you

1. Do you want lightning talks as a real format? If yes, the program needs slots for them first.
2. Is 3 proposals the right cap, or would you prefer 2 or 5?
3. Do you want speaker travel or fee info on the form? A line like "We cover X" prevents mismatched expectations, so I'd add it if there's a policy.