# Recommendation: don't move the page — split it, and shrink the reason a notebook felt necessary

I read `developer-quickstart-guide/SKILL.md` and all four references (`delivery-mechanisms.md`, `quickstart-template.md`, `worked-examples.md`, `verification-protocol.md`). Applying the skill's decision framework, the data-eng team's proposal bundles two unrelated problems into one fix. Untangling them removes the need for the notebook entirely.

**The two problems:**
1. 70% of the page is setup bloat (Python pinning, JDBC driver, Arrow build, CLI install) — this kills the time budget and has nothing to do with the container.
2. The payoff is a chart, and charts don't render on a plain docs page — this is what's actually pulling the team toward a notebook.

Fix problem 1 by deleting prerequisites, not by changing containers. Fix problem 2 by moving the chart out of the success moment instead of building infrastructure to accommodate it.

## Why the notebook fails the container test, specifically

Per `delivery-mechanisms.md`:

> Delete the sandbox and the notebook from the shortlist, rather than leaving them at the bottom, whenever the interview named no owner for the container or a security review the team will not clear. A container nobody maintains fails in front of the reader on their first visit.

"Nobody has volunteered to maintain notebook infrastructure" is exactly that answer to interview question 12. That alone drops the notebook off the list — a rewritten page is worth nothing the day the notebook kernel breaks and nobody notices for three weeks.

The JupyterHub doesn't rescue this, because it doesn't close the gap that matters:

> An in-house sandbox the platform team already maintains for something else moves the sandbox from a standing job to near-free, and straight to the top.

That line is about *infrastructure cost*, not *ownership*, and it's about *reuse for the same trust boundary*. Your JupyterHub is provisioned for internal analysts — authenticated employees, presumably on a trusted network. A getting-started page is read by anonymous prospects evaluating Cobalt for the first time. Routing external, unauthenticated readers into an internal analyst tool means:

- someone has to build auth/tenancy for external users on infrastructure that has never needed it,
- someone has to answer for external code execution landing on internal platform infra,
- and per the same reference, this is one of the three containers that "execute the reader's code, and sometimes their credentials, on a third party's infrastructure" — here it's *your own* infrastructure, which makes the security review harder to skip, not easier.

The JupyterHub reduces build cost for an *internal* notebook. It does nothing for the ownership question, and it may make the compliance question worse. Reuse the instinct, not the literal server: if the team later wants a public notebook, that's new infra with a new owner, informed by how JupyterHub is run, not a redirect onto it.

Container ranking stays: **plain docs page** (default) for this quickstart. Move up a rung only when a cold run proves the friction that rung removes is what's breaking the budget — and the friction here (a giant local toolchain install) is removed by deleting prerequisites, a content fix, not a container fix.

## Reframe the actual defects

| # | Symptom | Failure mode (per skill) | Fix |
|---|---|---|---|
| 1 | ~1,820 words of setup before step 1 | "Environment setup swells the page" | Ship a single pinned container image or install script; delete the prerequisite instead of documenting it |
| 2 | Whatever setup survives still needs documenting | "Where environment setup is large and durable, give it its own page linked from step 1" | Split into a separate **Environment setup** page |
| 3 | Success moment is a bar chart | Chart requires a rendering surface the plain page can't give it → pulls the whole page toward a heavier container | Redefine the success moment as a query result the reader can see in a terminal; move the chart to an optional next step |
| 4 | Reader queries a dataset they didn't create | worked-examples.md, data-platform note: "a demo dataset the reader did not create weakens the proof" | Have the reader materialize a small table from the public dataset themselves (cheap, one extra line, doesn't touch the container decision) |
| 5 | Product class is "Database / data platform" (10 min baseline); current page is 2,600 words, mostly install | Budget blown by an order of magnitude | New budget commitment below, achievable once #1–#3 land |

I can't cold-run this — Cobalt's real CLI, JDBC driver and dataset aren't available to me, and the current page text wasn't provided. Everything below is the redesign and a verification plan for your team to execute; treat the code blocks as illustrative shape, not verified output, exactly the caveat `worked-examples.md` puts on its own invented "Pigeon" example.

## 1. Success moment + time budget

- **Success moment:** the reader runs a query against the hosted NYC taxi dataset and sees real rows come back in their terminal.
- **Budget:** 10 minutes (Database/data-platform baseline), title states it, cold run enforces it.
- The bar chart is real value — it moves to "Next steps" as a two-minute follow-on, not the gate the reader must clear to feel Cobalt works.

## 2. The quickstart page

```markdown
# Query your first Cobalt table in 10 minutes

You will run Cobalt against a public dataset of 1M NYC taxi trips and see
real rows come back.

## Before you start

- Docker: check with `docker --version` (https://docs.docker.com/get-docker/)
- Nothing else. The container below already has the pinned Python runtime,
  JDBC driver and Arrow build Cobalt needs.

## 1. Start Cobalt

    docker run --rm -it -p 8420:8420 cobalt/quickstart:3

You should see:

    Cobalt 3.4.1 ready on :8420
    Attached dataset: nyc_taxi_trips (1,048,575 rows)

Port already in use? Stop whatever's on 8420, or add `-p 8421:8420` and use
that port in step 2.

## 2. Connect and load a working table

    cobalt-cli connect localhost:8420
    cobalt> CREATE TABLE my_trips AS
            SELECT * FROM nyc_taxi_trips
            WHERE pickup_date = '2026-01-15'
            LIMIT 50000;

You should see:

    CREATE TABLE my_trips: 50,000 rows loaded

## 3. Query it

    cobalt> SELECT EXTRACT(HOUR FROM pickup_time) AS hour, COUNT(*) AS trips
            FROM my_trips
            GROUP BY hour
            ORDER BY hour;

You should see:

    hour | trips
    -----+-------
       0 |   412
       1 |   287
       ...
      23 |   891

Empty result? Confirm step 1's dataset attached — rerun the container and
check the startup line for `Attached dataset`.

## What just happened

You loaded a slice of a 1M-row public dataset into your own table and ran
a columnar aggregation over it — the query you just ran scans only the
`hour` and `pickup_time` columns, not the full row.

## Next steps

- [Plot this as a chart in a notebook](…) — same query, rendered as a bar chart
- [API reference](…)
- [Community Slack](…)
```

## 3. Cut list

| Removed from this page | Where it lives now |
|---|---|
| Python version pinning, JDBC driver install, Arrow build instructions | `cobalt/quickstart` Docker image — no longer documented because no longer needed |
| Full manual-install path (for readers who can't/won't use Docker) | New **Environment setup** page, linked once from "Before you start" |
| Bar-chart rendering | New **Plot your results** how-to, linked from Next steps — this is where a notebook is worth revisiting, once someone owns it |
| Any product-history or architecture framing (if present on the current page — flag for the cold run) | Explanation docs |

## 4. Verification plan (someone on your team runs this)

Per `verification-protocol.md`:
1. Clean container, no cached Docker layers, no pre-pulled `cobalt/quickstart` image, no local Python/JDBC/Arrow anything.
2. Fresh machine, timer starts at page load.
3. Run every block verbatim — including the `docker pull` time inside step 1's timer, since the reader pays that cost too.
4. Compare real output to documented output line by line; log any mismatch as a defect.
5. Run it twice: once with an experienced SQL/analytics reader, once with someone who's never used Cobalt — per the skill, the second profile catches what the first one's tribal knowledge routes around.
6. Confirm elapsed time lands at or under 10 minutes on both runs. If the Docker pull alone blows the budget, that's a defect against the image size, not against this page's wording.

If step 1 doesn't hold — e.g., the pinned image is genuinely infeasible to build and maintain — the fallback is *not* "reach for the notebook." It's shrinking the Docker image scope (e.g., ship it without the JDBC path if most quickstart readers only need the CLI) or accepting a slightly longer manual-install budget on the linked setup page, while keeping the core query-and-result flow on the plain page.

## 5. Instrumentation

In the skill's value order:
- **Step-level drop-off**: event per step; watch specifically whether the `docker pull` inside step 1 becomes the new biggest drop, since that's the one part of the old setup burden you didn't delete, just compressed.
- **Support tickets quoting a step number.**
- **Median page-load-to-success time** — this is the number that tells you whether cutting the chart out of the gate actually worked.
- **Completion rate.**
- **Day-7 return of completers** — promote this one once completion looks healthy; it's the only metric that tells you whether "query returns rows" was the right success moment, versus the bar chart people actually wanted to see.

## When to revisit the notebook

Only once two things exist, per the interview: a named owner for the notebook environment (not "the platform team," a person or team that signs up for pager duty on it), and a security sign-off for exposing execution access to anonymous external readers, distinct from the JupyterHub's existing internal-analyst clearance. At that point it's a strong *addition* — linked from "Next steps" as the chart-plotting follow-on already sketched above — not a replacement for the page that gets someone to their first working query.