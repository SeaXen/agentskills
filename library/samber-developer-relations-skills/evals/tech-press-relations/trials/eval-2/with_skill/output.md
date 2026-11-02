Verdict first: qualifies as a story (evidence + shift, 2 of 5 tests solid), but only as **"the number"** angle — proprietary data drop, not a product news. Never call it a launch. Two blockers before send, both in the copy below as `[PLACEHOLDER]`: real figures once you run the query, and consent/anonymization sign-off (data already anonymised — confirm a human actually reviewed it, don't assume).

Copy is normal press-release prose (external artefact, not caveman-compressed). Fill placeholders, get legal/privacy sign-off on the dataset claim, then it's sendable.

---

**FOR IMMEDIATE RELEASE**

**[CITY, COUNTRY] — [MONTH DAY, YEAR]**

## [X]% of Breaking API Changes Ship Without a Version Bump, According to New Analysis of 3,400 Engineering Teams

### Sablefish's six-month study of anonymised schema-diff data finds most teams have no reliable signal that a "safe" API update just broke a downstream consumer

Sablefish, maker of the open-source CLI for diffing API schemas, today published an analysis of six months of anonymised usage data from 3,400 engineering teams. The finding: **[X]%** of changes that Sablefish classified as breaking — removed fields, changed types, tightened required parameters, altered status codes — were released without any accompanying version-number change, semantic or otherwise.

"A version bump is supposed to be the warning label," said [NAME], [TITLE] at Sablefish. "[QUOTE — one sentence, in this person's own words, making a claim or naming a consequence. Example shape: 'What surprised us wasn't that people break their APIs — it's that most of them don't know they did until a client files a ticket.' Replace with something the named spokesperson will actually stand behind.]"

**What the data shows**

- Across [N] schema comparisons run between [MONTH YEAR] and [MONTH YEAR], **[X]%** of changes matching Sablefish's breaking-change ruleset (see methodology) shipped under an unchanged or non-major version identifier.
- The gap was widest in [SEGMENT, e.g. "internal/private APIs versus public-facing ones" or "teams under N engineers"] — **[X]%** there, versus **[X]%** for [comparison segment].
- Teams using automated schema-diffing in CI caught the change before release at a **[X]%** higher rate than teams running diffs manually or not at all. [Cut this bullet if the dataset can't actually support the causal framing — correlation only, say so if that's what it is.]

**Methodology**

Sablefish's CLI runs a structural diff between two versions of an API schema (OpenAPI, GraphQL SDL, or protobuf) and classifies changes against a fixed breaking-change ruleset [link to ruleset]. Between [START DATE] and [END DATE], with opt-in telemetry and team consent, Sablefish logged anonymised, aggregated counts of breaking-change classifications and the version-string delta observed at release time, across 3,400 teams. No schema content, field names, endpoint paths, or organisation-identifying data were retained — only the classification label and whether the version identifier changed. Full methodology, the anonymisation process, and an aggregated version of the dataset are available at [LINK].

**Limitations**

This dataset reflects only teams already using Sablefish, which may skew toward organisations already paying attention to API compatibility — meaning the true rate across the industry could be higher, not lower. "Breaking" is defined by Sablefish's ruleset, not by a universal standard; teams may disagree with individual classifications. The data shows correlation between diffing practices and version discipline, not causation. [Add or correct any limitation the actual analysis surfaces once it's run — do not ship this list unless someone checked it against the real data.]

**About Sablefish**

Sablefish is a command-line tool for diffing API schemas — OpenAPI, GraphQL, and protobuf — to catch breaking changes before they reach production. [One more factual sentence: founding year, license, install count, or GitHub stars if disclosable. Skip anything unverified.]

**Data and assets**

Aggregated dataset, methodology writeup, and the ruleset used for classification: [LINK]
Sablefish CLI, docs, and source: [LINK]

**Press contact**

[NAME]
[EMAIL]
[Response-time commitment — state only if you'll actually honour it]

###

---

Next: run the query for `[X]%`, get one person to sign off in writing that the anonymisation was reviewed (not assumed), then swap in real names/quotes. Want the media-map (who to send this to) or the pitch email next?