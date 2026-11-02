# Tracewell starter notebook and forum post

I changed three things from your brief. Each one protects the post from removal or from backfiring on you.

1. **Disclose the affiliation.** The post opens with "I work on Tracewell". An undisclosed vendor plug in a 2,000-team forum gets flagged fast.
2. **Drop "gives you an edge".** You have no evidence for it, and a promotional claim can get the post removed. The post claims only what the tool does: it makes prompts and outputs inspectable for error analysis.
3. **Check the competition rules first.** Two things could break the plan:
   - Code competitions usually require internet off in the submission run. The logging can't run live there.
   - Sending competition-derived prompts to a third-party service may be restricted by the data-use rules.

   Read the Rules tab before posting. The notebook below buffers locally to handle the first point. I haven't seen this competition's rules, so I can't say whether the second applies.

I also didn't invent Tracewell SDK calls. Anything marked `TODO` needs your real API.

## Notebook outline

**Title:** `Starter: LLM answer ranking baseline + prompt logging with Tracewell`

| # | Cell | Content |
|---|------|---------|
| 1 | Setup | `os.environ['TRACEWELL_API_KEY'] = 'tw-xxxx'  # replace with yours` (your line, unchanged) |
| 2 | Key hygiene | Prefer Kaggle Secrets: `UserSecretsClient().get_secret("TRACEWELL_API_KEY")`. Fall back to cell 1 if the secret is missing. Markdown warning: never paste a real key into a notebook you publish. |
| 3 | Imports and config | `pip install tracewell` (TODO: real package name), seed, paths, constants |
| 4 | Data load | Load train and test. Print shapes and 3 sample rows. |
| 5 | Offline-safe logger | Wrapper `log_prompt(prompt, response, meta)`. If internet is available, send to Tracewell. If not, append to `/kaggle/working/prompt_log.jsonl`. Include a comment on why: submission runs are usually offline. |
| 6 | Baseline ranker | Simple, honest baseline (TF-IDF or small embedding similarity, then a pairwise or listwise scorer). Every LLM call goes through `log_prompt`. |
| 7 | Local validation | CV metric matching the competition metric. Report the score with its variance. |
| 8 | Error analysis | Pull the worst-ranked examples from the log. Show prompt, model output, and gold ranking side by side. This is the part Tracewell is for. |
| 9 | Flush buffered logs | Optional cell for an internet-enabled session: bulk-upload `prompt_log.jsonl`. |
| 10 | Submission | Write `submission.csv` with no network calls. |
| 11 | Notes | Trial is 14 days, then paid. Hosted only. Affiliation disclosure. Link to the rules check. |

Keep cell 11 in the notebook itself, not just the forum post. Notebook readers often never see the thread.

## Forum post

**Title:** Starter notebook with prompt logging for error analysis (disclosure: I work on Tracewell)

> Hi all,
>
> Disclosure up front: I work on Tracewell, an LLM observability service. This is a commercial product, hosted only. It needs an API key, with a 14-day free trial and paid plans after that.
>
> I published a starter notebook in the Code tab. It has a simple ranking baseline and a logger that records every prompt and response. The goal is to make error analysis faster: you can pull up the worst-ranked examples and read exactly what the model saw and said.
>
> Things to know before you try it:
>
> - **Offline runs.** Submission notebooks usually run with internet off. The notebook buffers logs to a local JSONL file, and you can upload them later from an internet-enabled session.
> - **Rules.** Check the competition's data-use rules before sending any prompt derived from competition data to an external service. If the rules don't allow it, keep the logs local. The notebook works fine that way.
> - **Keys.** Use Kaggle Secrets for your API key. Don't paste a real key into a notebook you make public.
> - **No leaderboard claims.** I haven't measured a score gain from logging. It helps you find failure modes, and what you do with them is up to you.
>
> The notebook runs without a Tracewell account if you use local logging only. Happy to answer questions here, and feedback on the notebook is welcome.

## Before you publish

1. Read the Rules tab for external-service and data-sharing limits.
2. Confirm the real Tracewell package name and calls, then replace the `TODO`s.
3. Run the notebook once in a fresh Kaggle session with internet off, to confirm the fallback path works.
4. Check the public notebook for any real `tw-` key before you press Publish.

I can write the full cell code once you give me the Tracewell SDK call signatures.