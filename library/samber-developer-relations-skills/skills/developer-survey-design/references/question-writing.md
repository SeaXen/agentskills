# Question writing

Good and bad pairs, scale templates and the demographic block for a developer survey.

## Contents

- Good and bad pairs
- Scale templates
- Option lists
- Demographic and sensitive block
- Open text

## Good and bad pairs

```
// ✗ Bad - agree/disagree invites acquiescence; "intuitive" is the team's word
"Our API is intuitive." Strongly agree … Strongly disagree
// ✓ Good - item-specific scale, the respondent's task
"How easy or hard was it to make your first successful API call?" Very easy / Easy / Neither / Hard / Very hard / Haven't tried

// ✗ Bad - two ideas, one answer
"How fast and reliable is the query planner?"
// ✓ Good - one idea each
"How often do query plans surprise you in production?" Never / Rarely / Sometimes / Often / Don't know
"How satisfied are you with query performance for your main workload?" Very satisfied … Very dissatisfied

// ✗ Bad - leading stem, praise built in
"How much do you love the new migration tool?"
// ✓ Good - behaviour first, attitude second
"Have you used the migration tool since it shipped?" Yes / No / Didn't know it existed
(if yes) "How well did it handle your last migration?" Completely / Mostly / Partly / Not at all

// ✗ Bad - recall window too long, vague quantifier
"How often do you read the docs?" Rarely / Sometimes / Often
// ✓ Good - concrete window, countable options
"In the last 3 months, how many times did you open the docs?" 0 / 1-2 / 3-10 / More than 10

// ✗ Bad - wishlist question, everyone says yes
"Would you like more tutorials?"
// ✓ Good - forces a trade-off the roadmap owner needs
"If we could improve only one, which would help you most?" Getting started / Reference / Migration guides / Troubleshooting / Other (please specify)

// ✗ Bad - telemetry already knows this better
"Which version are you running?" (when version is reported by opt-out telemetry)
// ✓ Good - ask what telemetry cannot see
"What stops you from upgrading to the latest major version?" (multi-select, randomised)
```

## Scale templates

Keep one direction for every scale in the survey, positive first or negative first, never both.

- Ease: Very easy / Easy / Neither easy nor hard / Hard / Very hard
- Satisfaction: Very satisfied / Satisfied / Neither / Dissatisfied / Very dissatisfied
- Frequency (concrete window): Never / Once / A few times / Weekly / Daily
- Importance for a trade-off: ask a single choice or a top-3 pick instead of rating every item "important"
- Recommendability: use the 0-10 item only if the community health sheet already tracks it, word-for-word; never invent a variant

Add "Don't know" or "Not applicable" as a separate option outside the scale, and decide once how the report treats it.

## Option lists

- Exhaustive and exclusive. Numeric ranges never overlap (1-5, 6-20, not 1-5, 5-20).
- "Other (please specify)" on every nominal list; code its answers into next year's options.
- Randomise order for unordered lists (tools, languages, blockers). Keep fixed order for scales and ranges.
- Cap a multi-select at what fits one screen on a phone; route long lists behind a screener.
- Use the community's names for tools and concepts, not internal codenames.

## Demographic and sensitive block

Place last, optional, broad bands:

- Years of professional experience: Less than 1 / 1-2 / 3-5 / 6-10 / 11-20 / More than 20 / Prefer not to say
- Role: list from the decision table only; "Other"
- Organisation size: 1 / 2-10 / 11-100 / 101-1,000 / 1,001-10,000 / More than 10,000 / Not employed / Prefer not to say
- Region: continent or broad region, never city

Sensitive items (gender identity, ethnicity, disability, sexual orientation) only when a decision in the table needs them, typically outreach measurement. Put them behind a separate explicit consent:

```
The next three questions are about your identity. They help us see whether the
community reaches everyone. They are optional, reported only as totals for groups
of 10 or more, and never published at the individual level.
[ ] I agree to answer these questions          (unticked; skipping jumps past the block)
```

Every sensitive item offers "Prefer not to say" and self-describe text.

## Open text

- One open box per decision that needs the respondent's words, not one per section.
- Ask for a specific instance: "Describe the last time X got in your way" beats "Any feedback?".
- Warn respondents not to include names or company details, then still check every quote before publication.
