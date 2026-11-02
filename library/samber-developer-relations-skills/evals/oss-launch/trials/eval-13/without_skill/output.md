## One-liner

**Original:** "Basalt: the revolutionary, blazing-fast data platform that reimagines how modern teams move data."

Problems: "revolutionary," "blazing-fast," and "reimagines" are unverifiable adjectives — they carry no information and are exactly the words a skeptical technical reader (or HN) discounts on sight. It also never says what Basalt actually *is*, and "modern teams" isn't an audience.

**Rewrite:**

> Basalt is an open-source ETL runtime for building and running data pipelines — self-host it free, or let us run it for you.

Why this is stronger: it states the category (ETL runtime), the open-source status up front (this *is* your credibility, especially against Airflow), and the actual business model (OSS + managed) in one honest sentence — no claim in it needs a citation.

If you have one concrete, defensible differentiator (a specific architectural choice, not "fast"), swap it in:

> Basalt is an open-source ETL runtime built for [specific thing — e.g. "single-binary deploys, no scheduler/webserver/metadata-DB stack to babysit"]. Self-host it free, or let us run it for you.

Don't reach for "fast" in the headline until the benchmark below is public and reproducible (see last section).

## Comparison table

**Original:**

| | Basalt | Airflow |
|---|---|---|
| Fast | yes | no |
| Modern | yes | no |
| Easy to use | yes | no |
| Scalable | yes | no |

This will get you torn apart. Every row is a subjective adjective, not a fact, and going 4-for-4 in your own favor reads as dishonest before anyone even checks the claims. "Scalable: no" for Airflow is the one line a hostile commenter will screenshot first — Airflow runs at real scale at plenty of large companies, so that cell alone can discredit the whole table, and by extension the launch.

Replace subjective adjectives with facts a reader can verify themselves:

| | Basalt | Airflow |
|---|---|---|
| Pipeline definition | [e.g. YAML/SQL, no DAG code required] | Python DAGs |
| Deployment footprint | [e.g. single binary] | Scheduler + webserver + workers + metadata DB |
| Managed option from the maintainers | Yes | No (third-party only) |
| License | [your license] | Apache 2.0 |

Every cell here should be something a reader could go check and find true. If you can't state a row as a checkable fact, cut the row — don't reach for an adjective to fill it.

## HN first comment

**Original:** "Hey HN! We're incredibly excited to finally share Basalt with the community after 18 months of hard work. It's a game-changer for data teams and makes pipelines 10x faster. We'd love your feedback and support!"

Problems:
- Exclamation points and "incredibly excited" / "game-changer" — pure hype, no content, exactly what HN polices hardest.
- "Makes pipelines 10x faster" is asserted with no source — and it doesn't even match the 6x number you mentioned to me. Inconsistent numbers across channels is the single fastest way to get a benchmark claim (and the whole launch) disbelieved.
- "We'd love your feedback and support" — "support" reads adjacent to asking for upvotes, which is against HN's guidelines and something dang's mods watch for.

**Rewrite** (fill the brackets with real specifics — don't invent a backstory):

> Hi HN, [name] here — one of the people building Basalt, an open-source ETL runtime.
>
> We built it after running into [specific, real pain point with existing tools]. Basalt is [1–2 concrete sentences on what's actually different architecturally — not adjectives].
>
> It's fully open source ([license]); we also run a managed version for teams that don't want to operate it themselves.
>
> We benchmarked it against Airflow on [describe the workload] and saw a 6x improvement — methodology and reproduction steps here: [link]. Self-reported vendor benchmarks deserve skepticism, so happy to hear where this doesn't hold up.
>
> Happy to answer questions about the architecture, the benchmark, or anything else.

This follows the standard Show HN/Launch HN shape: backstory, technical substance, an honest hedge on your own benchmark, and an open invitation to question you — which is what actually earns goodwill in that thread, not enthusiasm.

## Should you lead with "6x faster than Airflow"?

No — don't lead with it, and don't let "10x" and "6x" both exist in public copy; pick the one real number.

Reasons:
- It's a single internal workload, self-reported, with no published methodology. HN's first instinct on any performance claim is "what hardware, what dataset, what Airflow config, is this reproducible" — an unpublished number turns your top comment thread into a methodology interrogation instead of a product discussion.
- Airflow is an orchestrator; if Basalt is positioned as a runtime, the comparison may not even be apples-to-apples, and someone will say so.
- The inconsistency between "10x" (HN draft) and "6x" (benchmark) is itself a red flag — it looks fabricated even if both numbers are real, just measured differently.

What to do instead: publish the benchmark as its own page with full methodology (hardware, dataset, exact Airflow version/config, code to reproduce it), and *reference* it — don't assert the number as a headline claim. Lead the launch with the honest, checkable value prop (open source, self-hostable, managed option), and let the performance story be something people discover by clicking through, not something they have to take on faith from a one-liner.