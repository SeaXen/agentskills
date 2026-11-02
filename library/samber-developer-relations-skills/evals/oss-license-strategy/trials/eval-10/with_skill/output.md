# Sleetline: license and clearance

Two separate questions here, and they don't have the same kind of answer. The license question is mechanical and I can just answer it. The "am I clear" question is a legal-ownership question about a specific contract clause I have never seen, in a jurisdiction I don't know, and won't attempt to resolve — that one needs a real answer from a person, not a plausible-sounding one from me. Here's why, and what to actually do this month.

## The license: MIT is the right call, and it's the easy part

For a small standalone tool (a cron replacement, not a library other packages link against, not something you're hosting as a service for others), where the goal is adoption and nobody has floated a business model:

- **MIT.** Shortest, most recognized permissive license, zero friction, no counsel needed, leaves every option open later because as sole author you can still relicense unilaterally *while it's still just you*. This matches the FSF's own logic for small programs (they'd say Apache-2.0; MIT is this skill's softer default for brevity/recognition — flagging that as a default, not a rule).
- Apache-2.0 would only earn its extra length if you expect patent exposure or corporate co-contributors soon. A cron replacement doesn't scream "patent risk" — MIT is fine.
- Contribution policy once it's public: start with **nothing formal**, add a **DCO** (`git commit -s`, a bot that checks for the trailer) the moment a stranger's first PR shows up. It costs you nothing and gives you a provenance trail if this ever grows. No CLA — you have no business model and no foreseeable relicense, so a CLA at this size is just a wall that scares off drive-by contributors for a right you don't need.
- Before you publish: audit whatever `sleetline` depends on (`go.mod`/lockfile) for a copyleft dependency that ships in the binary. One GPL dependency would override MIT as your outbound choice entirely. I haven't seen the repo, so this is a five-minute check you need to run, not something I can assume clean.
- Scrub the repo of anything Calderbrook-specific before pushing — internal hostnames, job names that reveal business logic, credentials, config referencing their infra. That's independent of the license; MIT says nothing about confidentiality.

That part, you can execute this week regardless of anything else below.

## "Am I clear to do it": this is the part that isn't mine to answer

The facts you've given are exactly the profile that turns into a dispute later, not because any one fact is damning, but because they cut in different directions:

- **Weekends, your own machine** — the strongest fact in your favor.
- **A "decent chunk" during work hours, on your work laptop** — the strongest fact against you. Many invention-assignment clauses key off *time and equipment*, not just subject matter, and some jurisdictions' statutory carve-outs for personal inventions (where they exist) specifically require the work to be done *without* using employer equipment. You used employer equipment for part of it, which is exactly the fact those carve-outs are written to exclude.
- **It replaces a business function and 40 of your employer's production jobs run on it** — this cuts against "personal side project" framing regardless of how it was built. A tool your employer already depends on operationally is not a neutral fact.
- **Your manager said "sure, go ahead" in a Slack DM** — this is not a release. A manager's informal okay to *build* something is not the same as an authorized person releasing the *company's* IP rights to the public under MIT. Most companies route IP releases through legal or an OSS-approval process precisely because a line manager usually doesn't have signing authority over what the company owns. If Calderbrook ever wanted this tool back under wraps — a new manager, an acquisition, a competitor forking it — "my manager said go ahead in a DM" is a thin thing to stand on.
- **You can't parse the inventions clause yourself** — that's the tell. This is the one input in the whole decision that genuinely requires someone qualified to read your actual contract, in your actual jurisdiction, against your actual facts. I'm not going to guess what it says or how a court would read it — that's precisely the kind of claim this process is built to refuse, because a wrong guess here doesn't cost you a bad license choice, it costs you a public repo you may have to pull down, or worse.

What "clear" actually looks like, and it's gettable inside your month:

1. **Get it in writing, from someone who can actually bind the company** — not a re-ask of your manager, but a short note (email is fine) to your manager *and* whoever handles this at Calderbrook (legal, HR, an OSS-approval process if one exists) stating plainly: "I built sleetline, partly on personal time and partly on company time/equipment; I want to publish it on GitHub under MIT this month; can you confirm the company has no IP claim, or grant a release." A DM saying "sure go ahead" answers "can I build this," not "does the company waive its claim on it."
2. **Have your actual inventions clause read by someone qualified** — an employment lawyer, ideally one who knows your jurisdiction, or your own counsel if you have access to one. This is a genuinely cheap, fast thing to get answered (often a single paid consultation) compared to what it costs to find out the hard way after 40 people have forked it.
3. Do both in parallel — they don't block each other, and either one clearing you is enough to hit your "this month" target.

The MIT decision and the artifact work (LICENSE file, SPDX headers, DCO check, CONTRIBUTING.md) are ready to go the moment step 1 or 2 above comes back clean. Don't publish before that — a public release is the one step here you can't undo by relicensing later; every fork already out there keeps its terms forever even if you change your mind next week.

**Bottom line:** MIT, yes. Public this month, not yet — get the release in writing or the clause read first; that's a this-week problem, not a should-block-you-for-long one.