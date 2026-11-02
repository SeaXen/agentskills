# Solvi Sessions: goal check and reporting plan

## Verdict

**The goal setup is not right yet.** It has three problems:

1. **The deck omits the reason half the money is there.** Product is funding inference-caching feedback. "Goodwill and 700 attendees" doesn't mention it.
2. **Neither stated goal is an outcome.** "Goodwill" has no measure. "700 attendees" counts an output, and it's ambiguous: 700 registered, or 700 who showed up?
3. **The two goals pull against each other.** Product's goal is deep feedback from a few relevant people. Marketing's goal is breadth. A free half-day summit built for 700 is a poor format for feature feedback, and a summit that feels like a feedback harvest undermines goodwill.

The yearly plan raises the stakes: year 1 sets the baseline that year 2 will be judged against.

## Fix: one primary goal per funder, one shared guardrail

| | Marketing (50%) | Product (50%) |
|---|---|---|
| **Primary goal** | Goodwill among the right audience: ML engineers who run or evaluate model serving | Usable feedback on inference caching from people with real serving workloads |
| **Leading measure** | Attended (not registered) target-persona attendees | Qualified feedback conversations held |
| **Outcome measure** | Post-event "would recommend" and "would attend next year" scores, plus 30/90-day follow-on actions | Number of roadmap decisions the feedback changed, plus beta or design-partner signups |

**Shared guardrail:** the event must not read as a product pitch. Track it with a survey item such as "Sessions were useful regardless of whether I use Solvi."

## Changes to make before the event

1. **Define 700.** Pick registrations or attendance. Free events usually see a large drop between sign-up and show-up, so set the attendance target from your own past events or a comparable event. I'd drop the headline number and target "N attended, of whom X% fit the persona."
2. **Put caching feedback in the format, not in the keynote.** Options: a hands-on lab, small roundtables, or office hours with the caching engineers. Reserve seats for production-serving users.
3. **Capture workload data at registration.** Ask role, serving scale, and whether caching matters to them. Without it, Product can't tell whose feedback it is.
4. **Collect consent for follow-up** at registration, so feedback calls and beta invites are allowed.
5. **Agree the targets and the "success" bar in writing now**, before results exist. This includes what Product counts as a successful feedback yield.
6. **Tag everything for year 2.** Use the same survey questions, the same funnel definitions, and a UTM or source on every registration path.

## What to report afterwards

Build both reports from the same dataset. Don't send the same headline number to both teams.

### To Marketing

- **Funnel:** registered → attended → stayed past the midpoint, with the share who fit the persona.
- **Goodwill:** the survey scores (recommend, return next year, guardrail question), with response rate and sample size.
- **Follow-on behavior at 30 and 90 days:** community joins, docs or GitHub activity, newsletter signups. Report these as observed behavior, not as attributed pipeline unless you tracked it.
- **Efficiency:** cost per attended persona-fit attendee, with the Marketing share of spend.
- **Year-2 baseline table:** every metric above, with its definition.

### To Product

- **Yield:** how many people gave caching feedback, by workload type and scale, and how many conversations were deep versus a quick survey answer.
- **Themes:** ranked by frequency and severity, with consented quotes.
- **Decisions:** what the feedback confirms, contradicts, or changes in the roadmap.
- **Commitment signals:** beta signups, design-partner conversations booked, and people who actually tried it. Behavior counts for more than praise.
- **Limits of the data:** attendees are self-selected and friendly. Praise at a free community event is weak evidence of demand. Say so explicitly.
- **Product share of spend** against the yield.

### To both, in one shared page

- Actual spend against budget, split 50/50.
- Each team's targets against results, stated before the event.
- Honest misses, with the cause if known.
- The year-2 recommendation: keep the format, change the format, or change the split.

**Next step:** take the goal table and the six pre-event changes to a 30-minute alignment with both owners. Get sign-off on the targets before registration opens.