# Grindstone quickstart: activation is a measurement problem, not a copy problem

## Recommendation

Don't rewrite the page yet. The data you already have rules out the diagnosis marketing is assuming.

A stronger hero and an embedded video are top-of-funnel levers — they move how many people *start* the page, not what happens after they finish it. Your numbers say the page is not the leak: 71% of starters reach the final step, cold-run clean, every command and output verified. The leak is somewhere in the 68-point gap between "reached the final step" and "activated 30 days later," and that gap sits entirely outside the page markets wants to touch. Ship the hero/video if it helps top-of-page conversion, but track it as a separate metric — it will not move the 3%, and if it ships alone you'll be back here in a quarter with the same flat number and a spent budget.

What actually needs to happen: instrument the funnel between quickstart-success and activation, find the step where the 68 points disappear, then fix that step. Below is the funnel, the events, and the ranked questions the data has to answer before anyone touches a word of copy.

## Why "flat for a year" is the tell

A number that's been flat for twelve months isn't noise and isn't a copy problem — copy problems move a needle, even a small one, the first time you touch them. Flat-for-a-year means something structural is capping activation regardless of who reaches the end of the tutorial, and the quickstart's own completion rate (71%, unusually high — Tom Johnson's SendGrid benchmark had a live workshop complete at 1-in-20) tells you the cap isn't page comprehension. It's downstream.

## The funnel you're missing

Your current instrumentation apparently stops at "reached the final step." Extend it past the quickstart's own success moment into the product:

| Stage | Event | What it proves |
|---|---|---|
| 1 | `docs_page_loaded` | Reader arrived |
| 2 | `quickstart_step_completed` (×N, per step) | Reader is progressing, not stuck |
| 3 | `quickstart_success_event` (flag evaluation returns a value) | The documented success moment — your 71% |
| 4 | `sdk_installed_in_project` (a package/init call outside the tutorial's own sandbox context) | Reader moved from copy-paste to their own codebase |
| 5 | `flag_wired_into_app_logic` (first evaluation call from a non-tutorial file/service) | Reader did real integration work, not just re-ran the sample |
| 6 | `flag_evaluated_in_deployed_environment` (staging or prod, not the sandbox key) | Reader shipped it |
| 7 | `activated_30d` (your existing definition) | Retained usage |

Stages 4-6 are almost certainly where you have zero visibility today, and almost certainly where the drop happens — the quickstart's own success moment (stage 3) is a curl response or a CLI print, deliberately contrived per the quickstart pattern. For a feature-flag API specifically, that moment proves the API works; it proves nothing about whether the reader went on to wrap real conditional logic around a flag and deploy it. That's a materially bigger lift than the other 5 minutes, and it's a lift the quickstart was never scoped to carry — trying to fix it by making the quickstart's hero section stronger doesn't reach it.

## Drop-off questions to answer, in order

Rank by cost to instrument versus what it localizes — cheapest, most diagnostic first:

1. **Where between stage 3 and stage 7 does the population shrink fastest?** One event per stage (4-6 above) for four weeks tells you which single stage owns most of the 68-point loss. Everything else on this list is a follow-up to whichever stage wins.
2. **Do completers get a production-capable credential, or only a sandbox/test key?** If the quickstart's key can't touch a real environment, stage 6 is structurally blocked for everyone until they go through a separate, unmeasured provisioning step. This is the single most common failure shape for hosted feature-flag/auth-style APIs — a 5-minute code path wrapped in an unstated access path. Check this before anything else on the list; it's a one-query answer against your key-issuance table.
3. **Does activation correlate with reader type (self-serve vs. team-onboarding vs. enterprise-gated)?** If self-serve activates at meaningfully >3% and the blended number is dragged down by an enterprise cohort stuck on provisioning, the fix is an access-path fix, not a docs fix at all.
4. **Do completers return within 7 days, and does that predict 30-day activation?** This is the metric the skill this page follows explicitly promotes above completion rate the moment completion is healthy and activation is flat — because it's the only cheap signal that tells you whether the tutorial's chosen success moment (a flag evaluation in isolation) is the *right* proxy for eventual real usage, or a moment that happens to be easy to demo but doesn't predict retention.
5. **Do support tickets or community questions cluster around "how do I use this outside the sandbox"?** Near-zero cost to pull; if they cluster right after the quickstart's last step, that's corroborating evidence for #2, not a new finding.
6. **Is the documented success moment even the moment product considers "real" usage?** Ask whoever owns the 3% definition what it actually requires (N evaluations, a second session, a specific SDK call). If nobody can state it precisely, that's the actual root cause — you can't fix a gap to an undefined target.

## What to do about video and the hero rewrite

Reframe it, don't kill it. It's answering a different, legitimate question — is enough of the right audience getting to the page and starting it — which is not the one that's currently broken. Concretely:

- Give it its own metric: page-load volume and step-1 start rate, not 30-day activation. If those are also flat, the hero/video has a real job.
- Don't let it touch the tutorial's own steps. A stronger hero is copy above the fold; if it pushes any actionable content down or adds pre-action narrative, it will erode the 71% you currently have, which is your best evidence the page itself isn't the problem.
- An embedded video is a fourth delivery-mechanism decision layered onto a page that already passes its cold-run threshold on words alone — it adds a maintenance surface (a video goes stale exactly like a command does, silently) for a stage of the funnel that isn't where the loss is.
- Timebox it separately from the activation work so the two initiatives don't get credited or blamed for each other's numbers in next quarter's review.

## Next steps and timeline

1. **This week:** ship events for stages 4-6, plus a query answering the credential/gating question (#2 above) — that one's free, it's a lookup against data you already have.
2. **4 weeks:** let the funnel run untouched; four weeks is the default measurement window before committing to a target, per the same baseline-then-relative-improvement rule that applies to every KPI here.
3. **After week 4:** you'll have a named stage owning most of the loss. Bring that back as a scoped follow-up — likely either an access/provisioning fix (if #2 confirms it) or a new post-quickstart artifact (an integration how-to, owned by the developer-journey-map skill, not this one) covering the stage-3-to-stage-6 gap the quickstart was never meant to close.
4. **In parallel, no dependency:** let marketing ship the hero/video against page-load and step-1-start metrics. Report both results separately in the next review — don't let a win on one metric get read as a win on the other.