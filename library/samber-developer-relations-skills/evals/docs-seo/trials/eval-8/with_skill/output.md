# Carrowmore docs: untangling the AI-bot block

## Verdict

Two blocking layers — a hand-built `robots.txt` with ~20 `Disallow` lines and a CDN "block AI bots" toggle nobody on the docs team enabled — are each doing three unrelated jobs under one switch: stopping *search-style discovery* (what gets an assistant to cite you), *user-directed fetch* (what happens when someone pastes your URL into a chat), and *model training* (the only one legal actually asked for). Fix is not "unblock the bots" or "keep the block" — it's split the one rule into three, keep training blocked, restore the other two. This is a robots.txt/CDN-config fix, not a content or ranking fix, and it ships in under a day once someone has edit access to both.

## Coverage note

No live crawl was run against `docs.carrowmore.com` — this response works from the situation as described, not from a fetched `robots.txt` or CDN dashboard. Before touching anything, pull the actual file and the actual CDN rule set; the category table below is a starting map to sort the real ~20 agent names into, not a substitute for reading them. Vendors rename and add crawlers — verify each agent's category against that vendor's own current crawler documentation, never from the name alone.

## Root cause: one rule, three different things

| Category | What it controls | What breaks if blocked |
|---|---|---|
| Search-style discovery | whether an assistant's own retrieval/index can surface and quote your docs in a normal answer | "ask any assistant about our API" returns nothing — a competitor with open access wins the citation by default |
| User-directed fetch | whether an assistant can fetch a page a user explicitly pasted or named | a prospect who pastes your docs URL and asks a follow-up gets a fetch failure |
| Model training | whether your content may be used to train a future model | no visibility cost at all — pure licensing/policy decision |

Legal only has standing to demand the third row. Infra's blanket `Disallow` list and the CDN's default toggle both collapsed all three into one switch, which is exactly the failure mode that produced marketing's complaint: the docs went dark for the row that actually mattered to her, as collateral damage from the row legal cared about.

## Fix list

| # | Defect | Scope | Fix | Owner | Effort |
|---|---|---|---|---|---|
| 1 | ~20 `Disallow` lines in `robots.txt` block every named AI agent indiscriminately | all AI-crawler traffic to `docs.carrowmore.com` | re-sort the list into the three categories below; keep `Disallow` only on training-only agents; remove it from search/discovery and user-fetch agents | docs infra | 1–2h once the categorization is confirmed |
| 2 | CDN "block AI bots" toggle enabled account/zone-wide, undocumented, origin unknown | possibly wider than just `docs.` — check whether it also hit the marketing site and blog | disable the blanket toggle; replace with a rule scoped to named training-only agents, or per-agent rules matching the robots.txt split | infra/platform | 1h to locate and flip; longer if the CDN only offers an all-or-nothing switch and a per-agent rule has to be built by hand |
| 3 | No one verified actual HTTP response per agent, only dashboard/file state | all ~20 agents | `curl -A "<agent-string>" -sI https://docs.carrowmore.com/<page>` per agent, check status code — robots.txt is honor-system, the CDN is the actual enforcement layer, and a fixed robots.txt can still be silently overridden by an untouched CDN rule | infra | 30 min |
| 4 | No standing decision recorded — this will happen again at the next infra review | org-wide | write down the three-category policy (below) somewhere infra and legal both read before touching crawler rules again | docs owner + legal | 30 min |

Order matters: fix #2 before celebrating #1. A CDN edge block is real enforcement (it drops the request); a `robots.txt` line is a request compliant crawlers choose to honor. If the CDN toggle is still on, cleaning up `robots.txt` alone won't bring the docs back.

## Working categorization (verify names against current vendor docs before applying)

**Training-only — safe to keep blocked, zero visibility cost:**
- `GPTBot` (OpenAI)
- `Google-Extended` (Google — does not affect Google Search indexing, that's `Googlebot`, separate agent)
- `Applebot-Extended` (Apple — does not affect Siri/Spotlight, that's `Applebot`)
- `Bytespider` (ByteDance)
- `CCBot` (Common Crawl — widely reused as training data by others; blocking it doesn't stop any single assistant's live citation ability)

**Search-style discovery / citation — this is the row marketing is missing, unblock it:**
- `OAI-SearchBot` (ChatGPT's search feature)
- `PerplexityBot`
- `Claude-SearchBot` (Anthropic — check current split vs. `ClaudeBot`)
- `Applebot`, `Googlebot`, `Bingbot` — if any of these got swept into the "AI" list by mistake, that's not a policy call, it's an SEO-blocking defect, fix immediately regardless of the training question

**User-directed fetch — unblock it, this is the "someone pasted our URL" path:**
- `ChatGPT-User`
- `Claude-User`
- `Perplexity-User`
- `Meta-ExternalFetcher`

**Ambiguous / single-purpose crawlers that may not split cleanly:**
- `ClaudeBot`, `Meta-ExternalAgent`, `Amazonbot` — some vendors run one crawler across more than one purpose with no training-only alternative. Where that's confirmed true for a given vendor, that's a real trade-off, not a fixable misconfiguration: put it in front of legal explicitly ("blocking this vendor's training also removes citation from their assistant, there is no narrower control") and let them decide per vendor, instead of defaulting to block-everything because it's the easiest line to keep.

## What legal signs off on

> Carrowmore blocks AI systems from using our documentation to train models. We do not block AI systems from retrieving or citing our documentation when answering a user's question, because that is a different control with no bearing on training use, and blocking it only hides our own docs from the people asking about us.

That sentence is defensible, specific, and gets marketing her citations back without asking legal to give up anything they actually wanted.

## Out of scope / pending, don't promise these

- No submission mechanism exists to force any assistant vendor to re-crawl or re-cite faster — once access is restored, re-indexing happens on their schedule, same as it would with a search engine. Don't commit marketing to a date.
- Restoring access is necessary but not sufficient for winning the citation back from the competitor — that's an active-citation problem (content structure, being the better answer), not an access problem. Once this is fixed, that's a separate track (`ai-seo` / `optimize-for-ai`), not part of this fix.
- Publishing `llms.txt` or another machine-readable surface is a separate publishing decision with no ranking or citation effect on its own — don't bundle it into this fix or present it as the thing that brings citations back.