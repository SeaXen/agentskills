## Recommendation: don't relocate the page whole — split it, and don't reuse the analyst JupyterHub

**Bottom line:** the notebook idea is right for the *symptom* (1,800 words of setup) but wrong as literally scoped ("move the whole page"). Two problems hide inside that plan:

1. ⚠️ **Audience mismatch.** A getting-started page is an acquisition surface — external evaluators hit it cold, often from search. The platform team's JupyterHub serves *internal analysts*, which almost certainly means SSO-gated. Point the quickstart at it and you've replaced "install Python + JDBC + Arrow + CLI" with "get a Cobalt employee to grant you a login" — worse funnel, not better.
2. ⚠️ **The maintenance gap doesn't close, it moves.** Nobody owns notebook infra today. Docs pages are static and cheap to leave stale. A live kernel is not: it needs a pinned base image (Python + JDBC driver + Arrow build + CLI baked in), rebuilds on every Cobalt release, dataset hosting/refresh, and — critically — if it's public-facing, abuse/cost controls for anonymous users running arbitrary code. That's a bigger ongoing commitment than what data-eng is trying to escape, not a smaller one.

### What to do instead

**Split the page into two, don't merge it into one notebook.**

| Path | Audience | Content |
|---|---|---|
| **Try it live** (primary, above the fold) | Anyone evaluating Cobalt | Pre-baked, zero-install notebook. Query the taxi dataset, get the bar chart, in under 2 minutes. |
| **Install locally** (secondary, own page) | People building a real integration | The existing setup steps, kept — trimmed, not deleted. |

This follows the standard quickstart pattern: get to the payoff fast, push the deep-dive to a linked page instead of gating it in front of everyone. Right now 70% of the page is prerequisite for the 30% that's the actual demo — invert that ratio for the front door, and keep the full path one click away for people who need it.

### Fix the infra question before picking a host

✅ **Don't put this on the internal JupyterHub.** Ask platform team for a *separate*, unauthenticated-or-self-serve, rate-limited, ephemeral instance — different security posture (anonymous internet traffic executing code) and different cost profile (per-session teardown, no persistent storage) from what they run for analysts today. Treat it as a new infra request, not a reuse of existing capacity.

✅ **Prefer a third-party hosted option over self-hosting**, given nobody's volunteered to own this: mybinder.org or a Colab badge pointed at a `requirements.txt` + `Dockerfile` checked into the Cobalt repo. Zero servers to run; the "infra" becomes a config file that lives next to the code and gets CI-tested like everything else. Trade-off: cold starts can take 30–60s and you lose branding control — acceptable for a getting-started page, not for a marketed "playground" product.

✅ **Make data-eng own the image, since they're the ones asking for this.** "You want the notebook, you own the `Dockerfile`/`requirements.txt` that keeps Python/JDBC/Arrow/CLI versions in sync with each Cobalt release" — concrete, bounded, and it's the same maintenance surface as today's setup instructions, just executable instead of prose.

### New page shape (target: under 600 words, first result in under 5 minutes)

```
# Getting Started with Cobalt

Query 1M+ taxi trips and chart them by hour — no install required.

[▶ Open in notebook — takes ~30 seconds to start]

## What you'll see
[chart preview / GIF]

## What just happened
3 sentences: connected via JDBC, ran a columnar aggregation, plotted with <lib>.

## Want to run this locally instead?
→ [Local setup guide] (the current 1,800-word section, moved, trimmed to a
  prerequisites table + copy-paste commands per the existing tutorial format —
  not rewritten from scratch)

## Next steps
- [Core concepts]
- [Connect your own data]
```

### Open decisions to settle before building this

- Who signs up to own the notebook image long-term — data-eng, or does this die the moment the requester moves teams? Get a name, not a team.
- Does "hosted notebook" need to also serve internal analysts, or is that a separate, already-solved need on the existing Hub? If separate, don't let the two requirements merge into one system — that's how the audience mismatch above happens again.
- Is the taxi dataset already public and stable enough to embed in a Binder image, or does it need its own lightweight hosting (small parquet subset, not the full dataset) to keep cold-start time down?