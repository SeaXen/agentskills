I did not publish-ready this one. It is a draft with marked gaps, because the condensed postmortem has no investigation material and I won't invent any.

I did not run `scan-draft.sh`: the shell calls were refused here. Run `scripts/scan-draft.sh` over the draft before it goes out.

**Mode and pattern:** draft mode, Bug Hunt. The "this week" deadline favours it, and the raw material is already written down. One strike: the pattern's credibility section is "the dead ends you took", and your note has none. Those slots are marked `[FILL]` below.

## Redaction (what I removed and why)

| In the internal note | In the public draft | Reason |
| --- | --- | --- |
| `mreynolds` | removed | Blameless framing. The conditions matter, not who typed the commit. |
| `PROJ-8812`, `#4471`, `go/falcon-postmortem-aug3` | removed | Internal ticket, change and wiki identifiers. |
| "Falcon" | "the routing tier" | Internal codename. |
| "including two enterprise accounts" | removed | Reveals customer detail. Say if you want it back. |

I kept two impact figures: 118 customers and 1.2M failed requests. Both need your explicit yes, since you haven't decided to publish them.

## Claim ledger

| Claim | Class | Action |
| --- | --- | --- |
| 34% of writes dropped | Measured | Reviewer confirms the source (dashboard or logs). |
| 51 minutes | Measured | Confirm the start. Does it begin at the 14:02 deploy or at first impact? |
| 118 customers | Measured | Confirm the counting method. |
| 1.2M failed requests | **Estimate** | The note says "estimated". The draft labels it so, and the method is a `[FILL]`. |
| Reload path re-read the wrong key | Shown | Needs a config or code excerpt with a pinned version. |
| "Easy to write, hard to see in review" | Opinion | Worded as the author's judgement. |

## The draft

> **A config reload that read the wrong key: 51 minutes of dropped writes**
>
> *Published [DATE]. Written by [ENGINEER NAME(S)]. Technical review: [REVIEWER].*
>
> On August 3, starting at 14:02 [TIMEZONE], our write path dropped 34% of writes for 51 minutes. 118 customers were affected, and we estimate 1.2 million requests failed. The cause was a config reload path that re-read the wrong key.
>
> We run a routing tier in front of our storage layer, and every write passes through it. This post covers what happened, what we do not yet know, and what we are changing. We are publishing it because customers asked. I also think this class of bug is easy to write and hard to see in review: a reload path that disagrees with the startup path.
>
> ## What customers saw
>
> [FILL: the error text or status code clients received. Say whether failed writes were rejected visibly or acknowledged and lost. Your note says "dropped" in one place and "failed requests" in another, so this must be unambiguous. It is the first thing an affected customer needs.]
>
> ## Timeline
>
> | Time ([TIMEZONE]) | Event |
> | --- | --- |
> | 14:02 | A configuration change was deployed to the routing tier. |
> | [FILL] | First alert or first customer report |
> | [FILL] | Root cause identified |
> | [FILL] | Rollback or fix applied |
> | [FILL] | Recovery confirmed (14:53 only if the 51 minutes start at the deploy) |
>
> ## What we assumed first
>
> [FILL: the first hypothesis and why it was reasonable. Include each dead end, with the command, graph or log that ruled it out. If the first hypothesis was right, say so. Do not invent a detour.]
>
> ## Root cause
>
> The routing tier can reload its configuration while running. The reload path read a different key than the startup path reads for the same setting. [FILL: which setting, what each key held, and why 34% of writes failed rather than all of them. Add a short config or code excerpt with the version pinned.]
>
> No single person's mistake explains this. A change passed review and [FILL: which checks] and reached production because [FILL: the specific gap, for example no test exercised a reload after startup].
>
> ## Fix
>
> [FILL: what was rolled back or changed, with the diff or config.]
>
> ## What we are changing
>
> [FILL: each action, described without a person's name, with a date or "done". List only what is committed.]
>
> ## What this post does not tell you
>
> - The 1.2 million figure estimates failed requests. It is not a count of lost writes. [FILL: how it was estimated, and how many failed writes clients retried successfully.]
> - [FILL: anything still unverified, for example other deploy paths that share this reload code.]
>
> If you were affected and need your own request logs for the window, contact [SUPPORT CHANNEL].

## Credibility gate

| # | Check | Status |
| --- | --- | --- |
| 1 | Claims classified | ✅ Pass (ledger above). |
| 2 | No unsourced numbers | ⚠️ Pass once the 1.2M estimation method is filled. |
| 3 | Benchmark disclosure | ✅ Not applicable. |
| 4 | One honest, actionable limitation | ⚠️ Partial. The estimate caveat is there, and the "does not tell you" section must be completed. |
| 5 | No unsupported superlatives | ✅ None in the draft. |
| 6 | Snippets pinned and dated | ❌ Fails. There is no snippet yet. The root-cause excerpt is required. |

The post does not clear the gate until the `[FILL]` slots are done.

## Handoff: what needs a human

1. **Dead ends and the investigation.** This is the post's value, and your note has none. Without it the piece is a status page entry, not a Bug Hunt.
2. **The "dropped" vs "failed" question.** Customers will read it as data loss unless you say otherwise.
3. **Timezone and year.** Also whether 14:02 is the start of impact.
4. **Why 34% and not 100%.** A reader will ask immediately.
5. **Actions and dates.** Publish only the ones that are committed.
6. **Security and customer-confidentiality read.** The skill requires it for incident posts. Add legal if the 118-customer figure is contractually sensitive.
7. **Two reviews.** An engineer who worked on the incident checks accuracy. Someone outside the team checks that it reads without insider vocabulary.
8. **Humanizer pass** on the finished prose. Keep the title, times, figures and any code exactly as written.
9. **Commercial disclosure.** Not needed for a pure postmortem, so I added none.

## Questions I need answered (the interview I could not run)

1. Ship the 118-customer and 1.2M figures, or ship percentage and duration only?
2. Is the audience customers affected by the outage, or a general engineering readership?
3. Can you add the detection and recovery story, even in rough notes?

Once you send the investigation notes, I'll fill the slots and re-run the gate.