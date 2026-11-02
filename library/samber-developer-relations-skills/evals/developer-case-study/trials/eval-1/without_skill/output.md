# Kestrel Freight cuts p95 dispatch latency from 8.4 minutes to 95 seconds by retiring cron

**Snapshot**
- **Company:** Kestrel Freight — dispatch operations
- **Team:** Dispatch engineering, led by Dana Okafor (Staff Engineer, Dispatch)
- **Change:** Replaced a cron-scheduled dispatch pipeline with [Workflow Engine Name]
- **Result:** p95 dispatch latency dropped from 8.4 minutes to 95 seconds
- **Measurement window:** four weeks before cutover vs. four weeks after
- **Live in production:** nine weeks

## The problem: a dispatch pipeline held together by cron

Kestrel Freight's dispatch pipeline decided which driver got which load and how fast that decision reached the driver's app. It ran on a set of cron jobs.

Cron jobs don't know about each other. When one step ran late — a delayed data pull, a slow downstream API — nothing downstream knew to wait, retry, or back off. Jobs stacked up, overlapped, or silently skipped a cycle. Dispatchers found out something was wrong when a load sat unassigned, not when the job failed.

That failure mode shows up directly in dispatch latency: the time between a load becoming available and a driver getting the assignment. On Kestrel Freight's own account, this was the number that mattered most to the team, and to drivers waiting on their next job.

## The change: dispatch as a managed workflow

Kestrel Freight moved the dispatch pipeline off cron and onto [Workflow Engine Name]. The steps stayed largely the same — pull loads, match drivers, push assignments — but they now run as a single tracked workflow instead of independent scheduled scripts. Retries, backoff, and step-to-step handoff are handled by the engine instead of by ad hoc scripting around each job.

The team cut over nine weeks ago and has run the new pipeline in production since.

## The result: p95 latency down 89%

Kestrel Freight tracks dispatch latency on a Grafana board. Comparing the four weeks before cutover to the four weeks after:

- **p95 dispatch latency: 8.4 minutes → 95 seconds**

That's the metric the team watches most closely, because it reflects the slow end of the distribution — the loads that used to sit the longest before a driver got the assignment.

Dana Okafor, Staff Engineer on the dispatch team, also described a drop in on-call load since the cutover — by her estimate, roughly half. Kestrel Freight hasn't instrumented on-call volume, so this is Dana's read from living with the system day to day, not a measured figure. She attributed it to the same root cause as the latency drop: failures that used to require someone to notice a stuck cron job and intervene now retry and surface on their own.

> [Insert a direct quote from Dana here — pull it from the call recording rather than paraphrasing it as a quote. Nothing in the brief for this post included exact wording, so nothing here is presented as verbatim.]

## Why it worked

The latency improvement traces back to one change: failures in the pipeline stopped being invisible. Under cron, a stuck step meant a stuck load, discovered late. Under the workflow engine, a stuck step retries or fails loudly, and dispatch never queues behind a job nobody was watching.

---

**Before this goes on the blog, three things to close out:**

1. **Verbatim quote.** The draft above deliberately doesn't invent quoted dialogue for Dana — attributing invented words to a real, named engineer at a customer company is a real problem if it runs on the public blog. Pull an actual line from the recording and drop it in.
2. **Customer sign-off.** Standard practice before publishing any case study naming a customer, an employee, and specific performance numbers: confirm Kestrel Freight (and Dana specifically, since she's quoted by name) has approved this text, the numbers, and the use of the Grafana screenshot.
3. **Product name.** I've left `[Workflow Engine Name]` as a placeholder since the brief didn't name the product this post is promoting.

The on-call figure is written as Dana's own estimate, not a company metric, since it's explicitly untracked — worth keeping that framing rather than tightening it into a bare "50% reduction" stat next to the measured latency number, which would misrepresent it as equally rigorous.