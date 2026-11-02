# Vantage Retail 30-hour hack: prompt specificity and a draft prompt

## Recommendation

Use the **structured statement**, not starter repos with acceptance tests. The five parts are context, the challenge as a question, constraints, resources provided, and a minimum viable submission (MVS).

- ⚠️ **Why your co-organizer's option is the wrong rung:** the fully specified challenge needs about a week or longer, or a sponsor whose integration tests already exist. A 30-hour hack has neither. Below a weekend, it also turns the event from a build into a graded exercise.
- ⚠️ **Cost:** a starter repo, dataset and acceptance tests for each prompt is days of organizer engineering per prompt. With several prompts, that likely lands before the publication date.
- ⚠️ **Fairness:** acceptance tests measure fit to your spec, not quality. They reward whoever reads the test harness fastest. They also punish a team with a better reading of the problem.
- ⚠️ **The 25% rule:** teams typically deliver about a quarter of their own pre-hack estimate of their scope. That is the team's own plan, not your prompt. Hidden tests make a quarter-finished team score zero. An MVS makes that quarter demoable.

**What gets your co-organizer the objectivity they want, at lower cost:**

1. **Checkable constraints.** Write them so a judge can verify each one by looking at the demo.
2. **A stated MVS per prompt.** Every team knows the floor, and judges compare like with like.
3. **Shared resources, not shared tests.** Give every team the same fixture data and the same mentor hours. The data is the part that costs teams the most time.
4. **Named evaluation categories and a published exclusion list.** Judges score what the brief names.

Weights, scale and judge allocation belong to `hackathon-judging`. I print none here.

**One exception worth considering:** if one prompt has a single numeric target, ship a small scoring script for that prompt alone, as an optional self-check. Don't use it as the judge. The ISRO "lookup under 100 ms" statement shows a number can live in a checkable constraint with no test suite behind it.

## Draft prompt (one challenge track)

I assumed one track per prompt. Placeholders in `[brackets]` need your input. Don't publish with any left.

> **Smarter stores track: finding the gap before the customer does**
>
> *Context.* A store associate walks the floor and notices an empty shelf slot only after a customer asks for the item. By then the sale is usually lost. Stock systems show the item as "in store", because it sits in the back room or on a pallet, so nobody is alerted. Associates have a handheld device and about [N] minutes per aisle round.
>
> *The challenge.* How can a store detect a shelf gap, and get the right item from the back room to the shelf, before a customer notices it is missing?
>
> *Constraints.*
> - It must work from data a store already has: [POS sales, stock counts, planogram].
> - It must not require new in-store hardware.
> - Its output must reach an associate in one action, not a dashboard they must check.
> - It must run offline or degrade gracefully if the store network drops.
> - It must not use real customer or employee personal data.
>
> *Resources provided.*
> - A synthetic or anonymised [8-week] sales and stock extract for [2] stores: [location, owner, format].
> - A sample planogram for [one aisle].
> - Mentors: [names or roles, which hours].
> - *Not provided:* camera or shelf-sensor data, and any live production system.
>
> *Minimum viable submission.* One scenario, running end to end: input data goes in, and a specific "restock this slot now" signal comes out for one associate. A single working flow counts. A design with no running code does not.
>
> *If a provided data source or internal service is down* through no fault of your team, you will be judged on design and integration plan, not on a working call.

**Why this shape:**
- A team can decide in one reading whether it wants the problem.
- The MVS sets the floor.
- Every constraint is checkable by a judge.
- The missing resource (sensor data) is named, so teams don't plan around it.

## Before I draft the rest

I need these answers before the full brief. They change the rungs above:

1. **Demo and judging structure:** is it expo tables, a stage pitch, video-only, or a hybrid? This is a fixed input from `event-format-selection`. It sets the submission checklist.
2. **Who brings the problem:** do teams pitch their own ideas, or does the organizer supply the prompts? If teams pitch their own, an open theme could be correct and the brief would publish the pitch mechanic instead.
3. **Number of prompts and tracks:** how many do you want? Roughly how many teams are 60 engineers, and what are the team-size limits from `hackathon-team-formation`?
4. **Data:** can you get a synthetic or anonymised store extract before publication? Without it the data constraint above can't be met, and the MVS has to shrink.
5. **Prizes:** are there any, and does an internal sponsor fund one? A funded prize deletes the open-theme rung and needs a named track.
6. **Rules and publication:** which rules apply internally (IP, data handling, public-code requirement, who is barred), and when must the brief be published? Public-code does not transfer to an internal event without a decision. If any data is personal or any participant is a minor, route it to your data-protection owner first.

I'd draft the remaining prompts as variations of this skeleton after answers 1–3.