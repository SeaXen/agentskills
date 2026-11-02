**Verdict: not good to go.** Four of your five decisions fail the `developer-how-to-guide` ship gate, and the fifth is a claim that will fail when someone checks it. Each one has a fix that still meets Friday.

## What to change

| # | Your plan | Problem | Fix |
|---|---|---|---|
| 1 | Priyanka runs it herself | The author fills gaps from memory, so her run can't clear the gate. Only a cold run by someone who hasn't seen the draft counts. | Priyanka runs it once to capture real output. A second person at the competence floor then runs it cold. |
| 2 | Run on her production account, on her real domain | The gate bans production and the author's own machine. Swapping a certificate on a live domain can break HTTPS for real visitors. It also puts her real private key through a draft procedure. | Use a throwaway subdomain on a Marrowgate test tenant. If nothing else exists, use the lowest-blast-radius real resource and record it in `tested_with`. Say on the page what that run did not cover. |
| 3 | Keep the Windows upload variant, tagged "untested" | An "untested" tag isn't an allowed state. The gate requires every documented variant to be run at least once. | Drop the Windows steps. Leave one line on the page: "Windows upload isn't covered here." List Windows in the hand-over with the team that must test it, and publish later once someone has a Windows machine. |
| 4 | Ship two `UNVERIFIED` blocks with a note | A page carrying any marker does not ship. The renewal command changed last sprint, so these are the blocks most likely to be wrong. A note doesn't verify a command. | Run the renewal command on the test domain this week and paste back the real output. If that can't happen before Friday, cut renewal. It's a separate goal with a different verification, so it can be its own follow-up page ("Renew your custom TLS certificate"). Ship the rest. |
| 5 | Style guide says the seven-point gate is the industry standard, citing the Good Docs Project | The seven-point threshold is the skill's own baseline, not a published standard. The Good Docs Project backs only three things: "test your how-to instructions from start to finish", "re-test instructions after every notable product release", and the 8-10 step cap. A false citation gets the whole style guide discounted. | Reword it. Suggested text: "Our ship gate is a house standard. Its principle comes from the Good Docs Project: test instructions from start to finish, and re-test after every notable release." |

## Verification plan

Hand this run list to Priyanka and the second runner.

```
Environment:   Marrowgate test tenant with one deployed site, a throwaway
               subdomain you control, and a certificate plus private key
               issued for that subdomain. Not production, not her real domain.
Runner:        A second person who holds the role the prerequisites name and
               hasn't seen the draft. Priyanka may dry-run first, but only to
               capture output.
Capture:       The two UNVERIFIED renewal blocks, by step number. Paste back the
               exact command, flags and output from a real run on the test
               domain. Also capture the upload output and the independent check
               (for example, the certificate served on the domain).
Variants:      macOS and Linux upload: run both, or drop the one nobody can run.
               Windows upload: drop. Out-of-scope line only.
Re-run:        Every step marked "safe to re-run", repeated on the finished
               state. Upload first, since a re-upload is the likely idempotency trap.
Roll back:     Exercise the section before and after the certificate swap.
               Confirm the previous certificate can be restored, and say so on
               the page if it can't.
Fill:          owner (a team, not Priyanka), tested_with (API version or run
               date), last_verified, any UNVERIFIED-LINK targets.
Product gaps:  Anything the page can't verify because Marrowgate has no
               independent read path. Report it to the product team.
```

Three things on the page need extra care for this feature:

- **Private key:** the page must never have the reader paste it into a command line or an exported variable. Use a file path or stdin.
- **Safeguard before the swap:** keep the old certificate active until the new one is verified. Add before you remove.
- **Propagation:** state the expected delay and give a poll command with a timeout. Verify through a check independent of the upload call's own response.

## Friday plan

1. **Today:** Priyanka dry-runs the whole page on the test tenant, including both renewal blocks, and pastes back the real output. She removes the markers only where the output is real.
2. **Next:** the second runner does a cold run of the recommended path plus the macOS and Linux variants.
3. **Fix and re-run** only the affected steps.
4. **Ship** if all seven criteria hold.

Fallback if the cold run slips: ship the upload-and-verify page without renewal and without Windows, each with a one-line out-of-scope note. Follow-up pages: renewal, then Windows. Don't ship markers, an "untested" tag or a production-only run.

## Open questions

I couldn't ask these interactively, so I assumed answers. Correct any that are wrong.

1. **Which Friday?** Today is Friday 2026-10-30. I assumed the deadline is next Friday, 2026-11-06. If it's today, use the fallback.
2. **Who can be the second runner?** I assumed someone in support or another engineer exists. If nobody can, you ship a draft with `owner: UNVERIFIED` and the hand-over names the missing runner as the blocker.
3. **Does Marrowgate have a test tenant or test mode for certificates?** I assumed a throwaway subdomain works. If not, tell me and I'll rework the environment line.
4. **Does a certificate swap cause downtime or a billing change?** I assumed a brief propagation delay and no cost. If it does either, the page needs a change-window line and a stronger warning.