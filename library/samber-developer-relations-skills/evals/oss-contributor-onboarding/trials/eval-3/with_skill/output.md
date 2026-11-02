## Fernbank good-first-issue queue: what to do

**Short answer: reject your friend's fix. Labelling more issues and stacking `help wanted` on top makes this worse, not better, because it doesn't touch the actual defect — the queue is failing on completeness and claim hygiene, not on size.**

### Why "label more + add help wanted" is the wrong move

A `good first issue` label is a promise of mentoring, not a difficulty rating — that's Kubernetes' own definition of the convention, and it's the one that stuck industry-wide. GitHub also surfaces that label algorithmically to strangers browsing the whole platform, with no published criteria of its own. That means the label is already pulling in outside attention on its own; what sits behind it decides whether that attention turns into a contributor or a bad first impression that doesn't come back.

Look at what's actually behind your 19:

- **"Add retry backoff config" / "Improve docs for the supervisor"** are titles, not issues. No observed/expected behaviour, no file location, no verification command, no named mentor. A newcomer's real question when scanning a list isn't "is this easy?" — it's "can I already do this?" (this is the one finding from a controlled newcomer study the skill leans on: participants picked issues by whether the required skill/domain was legible, not by an assigned difficulty label). A one-line title answers nothing, so a stranger scrolls past it. That's a documentation/discoverability failure in Steinmacher's newcomer-barrier taxonomy, not a supply problem.
- **This is the textbook failure mode the skill calls out by name: labelling old bugs as beginner-friendly.** "Small for someone who knows the codebase" is not small for a stranger. If an issue has no location, no verification command, and no mentor, it isn't a first issue regardless of the label on it — you already have 17 unclaimed proofs of that sitting at zero activity for seven months.
- **Adding more of the same vague issues recruits more strangers into the identical dead end.** More labelled surface with the same missing four fields doesn't create more "can I do this?" clarity — it creates more people who look, can't tell, and leave. Volume was never the constraint here; the two blocking checks this queue is actually failing are "first issues are complete" and "claiming is defined."
- **Adding `help wanted` on the same 19 blurs a distinction you need, rather than fixing anything.** `help wanted` is the broader "we'd take a patch," with no mentoring commitment attached — it's a legitimately different promise than `good first issue`, not a bigger megaphone for the same one. Stacking both labels on the same unfinished issue body tells a newcomer two contradictory things about how much help they'll get, and fixes zero of the missing fields.

### What's actually broken, in order of damage

1. **Two dead claims are silently occupying "unclaimed" slots.** A commenter claimed one in January and went quiet — eight months, no expiry, no reap. You have no published claiming convention or stale-claim rule, so the queue *looks* like it has 19 live opportunities when at least 2 are ghosts and the rest have sat untouched long enough to suggest the same underlying defect applies to all of them. This is exactly the "claiming is defined" check, and it's failing outright.
2. **The other 17 fail the completeness bar.** None of the one-liners you describe carry the seven parts a real first issue needs: observed behaviour, expected behaviour, file + test location, required skills, a suggested approach (or an explicit "design not settled, discuss first"), the exact verification command, and a named mentor. That's not a nitpick — it's the single biggest reason a technically-competent stranger reads the title and leaves without commenting, which produces exactly the symptom you're describing: zero touches, seven months running.
3. **You don't yet know if the standing floor is even the right size.** The self-set baseline this kind of queue should hold to is "at least three *valid, complete, unclaimed* issues at any time" — not nineteen vague ones. Nineteen half-written issues are worse than five well-written ones: they cost you nothing to display and everything to a stranger's trust once they open two of them and find the same thin body twice.

### The actual fix for the queue

1. **Publish a claiming convention and a stale-claim expiry now, and apply it retroactively.**
   - Convention: claim by commenting on the issue; a maintainer assigns within a stated window (pick a number your three maintainers can actually hold, weekly release cadence suggests you have the throughput — say so explicitly rather than guessing).
   - Expiry: no update from the claimant in 14 days → a maintainer posts a check-in offering three honest outs (finish it, let a maintainer land the last bit and keep them as author, or release it back to the pool), not a bot auto-close. Send that to your January claimant this week — don't let an eight-month-silent claim keep blocking a slot any longer.

2. **Triage all 19 individually — don't relabel them in bulk.** For each one, do exactly one of:
   - **Rewrite it to the seven-part shape** (behaviour, location, skills, approach-or-"discuss first", verify command, named mentor) and keep `good first issue`, only if a maintainer will actually mentor it.
   - **Re-tag as `help wanted` instead** (drop `good first issue`) if it's real, acceptable work but nobody has bandwidth to mentor a newcomer through it. This is the correct, narrower use of your friend's idea: split the pool by mentoring commitment, don't merge the two labels onto the same items.
   - **Close it** if seven months of drift mean it no longer reflects the current codebase — a "retry backoff config" ask against a job-queue library may have been overtaken by whatever shipped in the meantime; a stale issue nobody can currently verify against is worse than no issue.
   - **Keep "Improve docs for the supervisor" as a non-code entry point** — reserved doc/test-only issues are the widest door into a project and the first thing an all-code queue loses. Rewrite it with the same seven parts (location = which doc file, verify = does it render/build, mentor = named), don't discard it just because it's not code.

3. **Name a mentor per issue, rotated across your three maintainers**, and size what's left in the queue to what three people can actually stand behind — a shorter list of issues someone is actually watching beats nineteen that nobody is.

4. **Re-check after the pass**: does the queue now hold at least three complete, currently-valid, unclaimed issues? If not, you've over-pruned relative to your mentoring capacity, and the fix is more maintainer time or fewer promises, not more labels.

### What I don't have and would change the plan

I don't have read/run access to the Fernbank repo, so I can't confirm the things a full audit would check before you publish anything — whether a `CONTRIBUTING` file exists and states this convention, what your actual median time-to-first-response is on the rare PR that does land, or whether the cold clone-to-passing-tests path even works today. If setup is *also* broken, fixing the queue's wording won't move the needle — a stranger who claims a well-written issue and then can't get the test suite running cold is a different, higher-priority leak (documentation describing a broken setup is worse than no documentation at all). Worth a quick honest answer before you invest in rewriting all 19: when did anyone last run your own setup instructions from a genuinely clean machine?

### Track after you ship this

Second-contribution rate and new-external-contributor count are too noisy to read at your volume — with 19 stale issues you likely have zero external PRs this quarter, so don't expect a trend line yet. What you *can* watch immediately: does the retroactive claim-expiry actually reap the two dead claims within your stated window, and does the rewritten queue hold its floor of three valid unclaimed issues a month from now without you refilling it manually. Those are the two signals that tell you whether the fix took, before you wait for an external PR to prove it.