## Short answer

License: MIT is fine — that's not actually the hard part.

Clearance: **not yet.** You have three separate risk factors stacking, and a Slack "sure, go ahead" doesn't clear any of them. This needs actual resolution before you publish, not just before this month ends.

*(I'm not a lawyer — treat this as engineering-brain risk triage, not legal advice. Given what's at stake, get 15 minutes with actual employment counsel before you push publish.)*

## Why it's not clear

**1. Work-laptop / work-hours time is the biggest problem.**
Most invention-assignment carve-out statutes (CA Labor Code §2870, and similar laws in WA, IL, MN, DE, KS, NC, UT) only protect an invention if it was made *entirely* on your own time, with your own equipment, AND unrelated to the employer's business or actual work assigned to you. "Mostly weekends, but a decent chunk on the work laptop during work hours" fails the "entirely" test outright, even in a state with a favorable statute. If you're not in one of those states, there's no statutory floor at all — your contract's literal text governs.

**2. It's not a side project unrelated to the employer's business — it's already running their business.**
40 internal production jobs depend on it. That's the opposite of "a hobby project with no connection to my job." Any invention-assignment clause that covers work "related to the company's business" or "resulting from work performed for the company" plausibly reaches this, even though Calderbrook is a logistics company, not a software company — internal tooling that runs their operations is still "related to the business."

**3. A manager's Slack DM is not a release of IP rights.**
Two separate problems here:
- Scope is ambiguous — "sure, go ahead" likely meant "keep building/using this," not "you personally own this and can publish it under MIT to the public."
- Authority is doubtful — most managers can't unilaterally waive company IP. That's usually legal/HR's call, sometimes requiring signing authority above a line manager.

It's useful as evidence of good faith. It is not a shield if this ever gets contested.

**4. Separate from ownership: confidentiality.**
Even if you fully owned the copyright tomorrow, the current codebase likely has Calderbrook-specific details baked in — job names, internal hostnames/endpoints, scheduling patterns that reveal how their operations work. That needs scrubbing regardless of how the ownership question resolves.

## What to actually do, in order

1. **Get the actual clause read properly.** Paste the paragraph to an employment lawyer rather than trying to parse it yourself — this is exactly the kind of ambiguous legal language that reads differently to a non-lawyer than to someone who knows the local case law. Cheap relative to 8 months of work.
2. **Convert the DM into a written, specific approval — or better, sidestep ownership entirely.** Two workable asks to HR/legal, not just your manager:
   - "Can the company confirm in writing it has no ownership claim over sleetline and I'm free to publish it under MIT on my personal GitHub?"
   - Or, often easier to get a yes on: **let Calderbrook open-source it under its own name**, with you credited as author. Sidesteps the whole ownership fight, and companies say yes to this more often than to "let the employee take it and walk."
3. **Scrub before publishing, either way.** Strip job names, internal hosts/endpoints, any business-logic specifics tied to Calderbrook's operations, and check for the trivial stuff (credentials, internal URLs in comments/config/test fixtures).
4. **Don't let "this month" be the deadline that decides this.** A rushed publish now, walked back after legal flags it, is a much worse outcome than a publish that slips six weeks.

## On the license itself

MIT is the right choice once you're clear — permissive, minimal friction, standard for a CLI-style infra tool, good for adoption. No reason here to reach for Apache 2.0 (patent grant) or a copyleft license (GPL/AGPL) unless you specifically want to block someone wrapping it as a SaaS — doesn't sound like your goal. Keep MIT as the plan; it was never the blocking question.