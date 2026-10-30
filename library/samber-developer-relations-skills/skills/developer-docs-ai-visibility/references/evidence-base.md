# Evidence base

Every figure this skill uses, with its label. Labels: **vendor-documented** (the AI or platform vendor's own docs), **independently measured** (research or logs from a party not selling AI-visibility tooling), **practitioner inference** (reasoned, not measured), **vendor-marketing** (a figure from a company selling SEO or AI-visibility tooling), **first-party** (the user's own logs, analytics and panel). Statements by vendor employees outside documentation are labelled informal. Self-set baselines are this skill's own defaults.

## Contents

- [Eligibility and selection](#eligibility-and-selection)
- [Generative engine optimization research](#generative-engine-optimization-research)
- [llms.txt and markdown twins](#llmstxt-and-markdown-twins)
- [Version fixes shipped by docs owners](#version-fixes-shipped-by-docs-owners)
- [Measurement](#measurement)
- [Third-party surfaces](#third-party-surfaces)
- [Self-set baselines](#self-set-baselines)
- [Claims to refuse](#claims-to-refuse)

## Eligibility and selection

- OpenAI and Anthropic run separate agents for search, user fetch and training; Perplexity runs search and user-fetch agents and no training agent; Google crawls with Googlebot and controls Gemini training and Gemini-app grounding through the `Google-Extended` token, which does not affect Search. Vendor-documented.
- No vendor publishes a citation-selection algorithm; Google says AI features need "no additional requirements" beyond indexing and snippet eligibility, and that optimizing for generative AI search "is still SEO". Vendor-documented.
- On one site, AI crawlers fetched 1,241 pages per citation sent over a month (Buytaert, 2026). Independently measured, single site.
- AI Overviews and AI Mode share about 13.7% of cited URLs for the same query (Ahrefs). Vendor-marketing.

## Generative engine optimization research

- Aggarwal et al., "GEO: Generative Engine Optimization" (KDD 2024): methods "capable of boosting source visibility by up to 40%"; citing sources, adding quotations and statistics gave 30-40% relative gains; keyword stuffing little or none. Independently measured - on a benchmark of general web queries, content rewritten by a model, gains measured as relative share within a fixed source set, so one source's gain is another's loss. No developer documentation in scope.
- No published independent replication on live commercial engines reproduces the 40%; later surveys frame it as a benchmark result and report cross-engine divergence. Independently measured.
- Page-feature correlations (answer-first, code blocks, headings, freshness, structured data) as citation drivers: no robust non-vendor study isolates any of them. Figures circulating ("schema-marked pages cited 2.3x more") come from tool vendors without methods. Vendor-marketing.

## llms.txt and markdown twins

- Ahrefs, logs across 137,210 domains: 97% of `llms.txt` files got zero requests in a month; AI retrieval bots made 1.1% of the requests that did arrive. Vendor-marketing.
- Buytaert, hosting-fleet logs: about 0.001% of requests hit `llms.txt`; on his own site every request in a month came from SEO audit tools; markdown twins added about 7% crawler traffic because "Bots fetch both versions". Independently measured.
- Evil Martians, two months of one site's logs: 37 of about 770 `llms.txt` fetches came from named AI assistants; Claude Code requested Markdown 76% of the time, ChatGPT fetched rendered HTML. Independently measured, single site.
- Google Search: "You don't need to create new machine readable files, AI text files, or markup". Vendor-documented. A Google search advocate added that server logs show AI services "don't even check for" llms.txt. Informal.
- Counter-figure: a docs-hosting vendor's CDN analysis of 25 companies found a median of 14 `llms.txt` and 79 `llms-full.txt` visits, mostly from ChatGPT. Vendor-marketing (it sells llms.txt hosting). It shows user-triggered reads, not search citation.

Reading: a convenience for coding agents and paste-into-chat users, not a search-citation lever.

## Version fixes shipped by docs owners

- Sourcegraph: Google indexed old-version hosts despite canonicals ("a hint, not a rule"); fixed with `X-Robots-Tag: noindex` on version hosts. Docs-owner observation.
- Prisma: version labels in title, description, structured data and markdown; canonical only where two versioned URLs are the same document; legacy content pruned from its LLM feeds. Docs-owner change.
- Next.js: a compressed docs index written into the project's agent instruction file, pointing at local doc files matched to the installed version; on Vercel's own Next.js evals it reached 100%, against 79% for skills with explicit instructions and 53% with no docs. Vendor-documented, own eval, not replicated.
- Kubernetes: current plus four previous releases on separate hosts, each old one with a "no longer actively maintained" banner. Vendor-documented.
- Google does not recommend noindex for steering canonical choice within a site; redirects are the strongest consolidation signal. Vendor-documented.
- Third-party mirrors' and forum answers' share of stale answers: not measured anywhere.

## Measurement

- ChatGPT adds `utm_source=chatgpt.com` to referral links for sites allowing its search bot (OpenAI publishers FAQ). Vendor-documented. Periods where it appeared dropped have been reported. Independently observed, unconfirmed by the vendor.
- Same prompt, repeated: fewer than 1 in 100 runs returned the same list of recommended brands, fewer than 1 in 1,000 in the same order, while the leading brands still appeared in most runs (SparkToro and Gumshoe, 2,961 runs). Independently measured, with a vendor co-author. It measured brand lists, not cited sources; source lists have not been measured the same way.
- Repeat-run overlap of 20-33% for local prompts (BrightLocal). Vendor-marketing.
- Bing's webmaster AI report shows citations and grounding queries for Copilot and Bing AI summaries, no clicks. Vendor-documented. Google counts AI Overviews and AI Mode inside Web search totals; a separate generative-AI report has been announced with a partial rollout. Vendor-documented; check availability on the property.
- Commercial trackers' "most cited domains" leaderboards disagree with each other (Reddit first in one, Wikipedia first in two others, YouTube first for one engine in another). Vendor-marketing; no independent accuracy audit exists.
- ChatGPT referring about 10% of new signups at one developer platform. Vendor self-report on social media, not audited.

## Third-party surfaces

- Reddit, YouTube, Wikipedia and LinkedIn top most citation leaderboards; GitHub appears in ChatGPT's top 20 in one audit; Q&A sites rank lower. Vendor-marketing and agency data: the direction agrees across sources, the magnitudes do not.

## Self-set baselines

- 20-40 prompts per panel; five or more runs per prompt, assistant and mode.
- Re-run horizon of four to eight weeks for retrieval levers; next model release for recall levers.
- Targets in SKILL.md Step 5.

Replace each with the team's own numbers once two panels exist.

## Claims to refuse

| Claim | Why it fails |
|---|---|
| "Add statistics and quotes for +40% AI visibility" | benchmark result on general web content, unreplicated live, relative share in a fixed set |
| "FAQ schema raises AI citations" | no study isolates it; Google limits FAQ rich results to a few authoritative site types and needs no special markup for AI features |
| "llms.txt gets you cited by ChatGPT" | logs show AI search crawlers almost never request it |
| "Answers must be 40-60 words" | figures range from 25 to 170 words across sources, none measured on docs |
| "Content older than N months loses citations" | correlations from tool vendors; date bumps without content change are a Google warning sign |
| "Blocking GPTBot hides you from ChatGPT" | training and search bots are separate at OpenAI; at Google the reverse trap exists, since `Google-Extended` also gates Gemini grounding |
| "Our AI rank is #3 for 'best database'" | positions do not repeat across runs |
