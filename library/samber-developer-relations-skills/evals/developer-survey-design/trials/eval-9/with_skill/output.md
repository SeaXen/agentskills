**Verdict: no, not as written.** Change two things on slide 3: "backend developers" becomes "respondents", and the margin of error comes out. The ±1.8% is the worse problem. I checked your methodology summary against the skill's claim ladder and its list of claims to refuse. I haven't seen the report itself.

## Slide 3 text to use

> In Nimbusline's 2026 State of Serverless survey, 58% of backend-role respondents (n=3,104) said they run WebAssembly workloads in production.

Put this in the footnote or speaker notes:

> Open-link survey promoted through Nimbusline's newsletter, Discord and conference talks. Not weighted. Question: "Do you run WebAssembly workloads in production today?" Percentages describe respondents, not all backend developers.

## Why the original fails

1. **"58% of backend developers" is a rung-4 claim.** The skill says rung 4 ("of developers" or "of the ecosystem") is not available from an opt-in survey.
   - The sample is people Nimbusline's channels reach: newsletter readers, Discord members and conference attendees.
   - Those people are mostly engaged and serverless-interested, so they are far more likely than the average backend developer to run Wasm.
   - The most this survey supports is rung 1: "X% of respondents", with n and exact wording.
2. **"±1.8%" must go.**
   - n=3,104 gives about ±1.8% only under the random-sample formula.
   - AAPOR says margin of sampling error does not apply to opt-in online surveys.
   - Skill rule: never print a margin of error on an opt-in sample. The number implies a precision the design cannot deliver.
   - Buyers who know surveys will spot it, and it undermines the rest of the slide.
3. **"now" implies a trend.**
   - "Now run" suggests growth, but the methodology you sent shows no prior-year comparison.
   - Trend claims need an unchanged question and a similar source mix.
   - Drop "now" unless Nimbusline publishes a comparable earlier edition.
4. **Unweighted, no calibration sample.**
   - Nothing in the methodology you sent corrects for who answered, so the report cannot measure how far its respondents drift from backend developers in general.
   - That is why the claim stays at rung 1.

## What to check before the slide ships

These are open points, not confirmed defects. Ask Nimbusline, or look in the full report:

1. **Is n=3,104 the backend-only base, or all respondents?** If it is all respondents, the 58% has a smaller base. The slide must state the right n.
2. **Can respondents pick several roles?** "Selected 'backend' as a role" suggests yes. If so, the group overlaps with full-stack, platform and others.
3. **What counts as a "Wasm workload"?** The question doesn't define it. Respondents may include edge runtimes or browser use. Check whether the report defines it, and whether "Don't know" was shown or dropped.
4. **Who funded and ran it?** Nimbusline sells serverless. Disclose that if the deck doesn't already make it obvious.
5. **Funnel and cleaning.** Check for starts, completes, bots and speeders removed. The methodology you pasted shows none of them.

## What the number can and can't support

- **Supports:** "Production Wasm use is common among Nimbusline's serverless-engaged community."
- **Does not support:** "Wasm is mainstream among backend developers", or any market-size or adoption claim.

If an enterprise buyer asks "58% of what?", the rewritten slide has a clean answer. The original does not.

## Next action

1. Paste the rewritten text above onto slide 3 (about 5 minutes).
2. Email Nimbusline with items 1 and 3 from the checklist. Ask for the questionnaire PDF at the same time.
3. If they confirm n is the backend-only base, you're done. If it isn't, send me the report's actual numbers and I'll fix the n on the slide.