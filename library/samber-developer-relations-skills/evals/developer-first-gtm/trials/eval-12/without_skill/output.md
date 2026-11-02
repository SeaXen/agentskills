## The problem with "a developer is a developer"

It's true at the wrong layer. The person typing `tilcrest migrate` is a developer in both segments — same skill, same CLI, same need to see a safe migration plan before running it. That's the product layer, and it should absolutely be unified.

But the entity deciding whether Tilcrest gets used is not the same in both segments. An indie dev or a two-person shop decides alone, with a credit card, in minutes. A platform team inside an insurer or bank cannot decide alone — SSO, audit logs, and an MSA aren't feature preferences, they're gates a security/procurement function puts up before *any* individual, however senior, is allowed to point the tool at a real database. That's a go-to-market and legal-approval difference, not a developer-skill difference. Collapsing it into "one flow" will do one of two things: annoy indie users with enterprise friction (a sales-call gate before they can try the CLI), or strand enterprise engineers in a self-checkout flow that can't produce what their compliance team actually needs (SOC 2 docs, a signed MSA, an SSO config).

Design one product experience. Design two commercial paths. Here's how to do both without it feeling like two products.

## Onboarding design

**Shared spine (everyone goes through this — this is the part where "a developer is a developer" is correct):**

1. Signup: email or GitHub OAuth. One extra question, framed as personalization, not gatekeeping: *"How are you evaluating Tilcrest?"* — "Just me / a small team" vs. "For my org (we'll likely need SSO, audit logs, or a vendor agreement)." This is the fork point, but nothing forks yet on-screen.
2. First 5 minutes, same for both: `tilcrest init` against a **sandbox schema you provide**, not a real DB. Output: a real, reviewable migration plan with rollback. This is the aha moment — a safe diff they didn't have to trust blindly.
3. Sandbox-first isn't a compromise for the enterprise segment, it's a requirement. A bank engineer usually cannot legally point an unapproved third-party CLI at a live schema before procurement clears it — so if the aha moment requires a real DB connection, enterprise users get zero time-to-value until a contract exists, which is backwards. Indie users, who have full autonomy, will happily connect a real DB immediately after — let them, but don't make it step 1 for anyone.

**Fork, from step 3 onward:**

*Self-serve track* (indie devs, small consultancies):
- Checklist (toolkit pattern, 3–7 items, ordered by value): connect a real DB → run first real migration → invite a teammate → wire into CI. Progress bar, visible completion %, dismissable.
- Free tier caps something real (migrations/environments), and the upgrade prompt shows up at the moment they hit that cap — usage-triggered, not immediate. This is a paid-trial or freemium activation model: low friction, credit card deferred until value is proven.
- Drip emails at 24h/72h if the checklist stalls, days 3/7/14 for feature discovery. No human touch — the whole point of this motion is that it never needs one.
- Activation metric: first real (non-sandbox) migration run. Target: paid conversion within days, self-checkout, zero sales involvement.

*Enterprise track* (platform teams at regulated companies):
- After the same sandbox aha-moment, surface — in-app, not a buried contact form — "Need SSO, audit logs, or an MSA? Talk to us," and route it to a named person within 24 hours. This is the "onboarding call" component from the toolkit, and it's the thing that's actually missing today if it's routing through the same self-serve flow.
- Critically: don't gate further technical evaluation behind that call. Let the engineer keep using the sandbox (and, once their org allows it, a real DB) freely while sales runs in parallel. The champion building internal conviction and the security review are two different clocks — don't make one wait on the other.
- Activation isn't "paid" here. It's milestone-based: champion identified → security questionnaire requested → MSA in legal review → SSO configured. Track those, not usage frequency.
- Timeline is quarters, not days. Don't measure this path against the self-serve checklist's clock.

**Handling the fork honestly:** self-selection will be wrong sometimes — an engineer at a bank might pick "just me" because they're doing a shadow evaluation before their org even knows. Watch for behavioral signals that override it: work email domain, inviting a large team, hitting SSO/audit-log docs, connecting from a company you already know is regulated. When those contradict the self-selected answer, don't block anything — just have a human check in ("noticed you're evaluating from [Company] — flagging in case you need SSO or an MSA down the line"). Enterprise deals often start exactly this way.

## What to report to the board

Kill the single blended free-to-paid number as the headline metric. Here's why it's actively misleading, not just imprecise: a self-serve trial converts to $108/year in 1–14 days; an enterprise trial "converts" to a five- or six-figure contract in 60–180+ days, if it's even the same engineer who started the trial. Blend those into one percentage and the number is dominated by whichever motion had more trial *volume* that quarter — not by which motion is healthier. A great quarter for enterprise (more regulated-company signups, each converting on its own much longer clock) will make the blended number *drop*, and the board will read that as a growth problem when it's actually a mix shift. That's not a hypothetical — it's the default failure mode of blending a fast, cheap, high-volume motion with a slow, expensive, low-volume one into a single rate.

Report instead:

1. **Two conversion lines, not one:**
   - Self-serve: trial → paid within N days (%), time-to-activation, 30/90-day retention.
   - Enterprise: trial → qualified opportunity (champion + security review started) (%), average deal cycle length, and separately, closed-won rate on qualified opportunities. Don't force this into a "conversion rate" comparable to self-serve's — it isn't the same unit of time or the same definition of "won."

2. **One topline number if the board wants a single line to track quarter over quarter: Net New ARR, split by motion.** Dollars weight the two motions correctly by construction — a closed enterprise deal is worth what it's worth, a self-serve sub is worth what it's worth, and neither drowns the other out the way a headcount-based blended percentage does.

3. **Mix shift, reported alongside, one line:** "X% of trials this quarter were enterprise-track vs. self-serve." This is what explains movement in the other numbers and stops the growth team from being credited or blamed for a macro shift in who's showing up, rather than how well either funnel is performing.

4. Tell the head of growth directly: the product instinct — one CLI, one aha moment, one docs set — is right, and worth defending against pressure to fork the product. The instrumentation instinct — one number, one flow, one funnel — is the part that doesn't survive contact with how these two segments actually buy. Splitting the metric isn't a hedge or extra reporting overhead; it's the only way the board can tell whether self-serve or enterprise is the one actually working this quarter, since right now a blended number can't answer that question even in principle.