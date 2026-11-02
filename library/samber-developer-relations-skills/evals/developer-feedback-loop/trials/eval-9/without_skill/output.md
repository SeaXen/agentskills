**Next action (10 min):** open the spreadsheet and check which columns already hold source channel, customer ID or email, and date. Those feed everything below. Then answer the 4 questions at the end.

## Recommendation: don't hand-label 412 rows with 38 labels

Three changes make this fastest. They also make Anika's look-over easier.

1. **Cluster before you label.**
   - 412 requests over 18 months across 3 channels will have many duplicates.
   - Expect roughly 100–150 distinct themes.
   - Put themes in the tracker, one per feature. Link the raw requests under each theme. All 412 stay in, nothing is lost.
   - The count of distinct requesters per theme becomes your demand signal.

2. **Split labels into facts and judgments.**
   - **Facts, from data.** Source channel and tier. Fill them by script from the spreadsheet. No manual work.
   - **Derived.** Product area. A cheap model (haiku) classifies it. You spot-check about 10%.
   - **Judgments.** Priority P0–P3 and effort S/M/L. Do not pre-assign these to all 412.

3. **Set priority and effort only on the planning shortlist.**
   - Priority from the source channel is a trap. A booth note is not lower priority than a Discord post.
   - Derive priority from demand: distinct requesters, enterprise count, fit with the roadmap.
   - Effort belongs to engineers. Ask Anika to size about 20–30 shortlisted themes. That takes about 30 minutes and is the most useful thing she can do in planning prep.

## Schema: 4 facets instead of one flat list of 38

| Facet | Values | Filled by |
|---|---|---|
| Source | discord, support, booth, sales | Script (fact) |
| Tier | free, pro, enterprise, unknown | Script, with `unknown` as a value (booth notes will mostly have it) |
| Area | your product areas (about 20 of the 38) | Model, then spot-check |
| Priority and Effort | P0–P3, S/M/L | Human, shortlist only |

Make these tracker fields, not free-text labels. Fields can be filtered and counted; labels drift.

## 3-week plan

**Week 1: data in (about 4–5 hours of your time)**
1. Fix the schema above. Cut your 38 labels to the product areas, plus the fields. (15 min)
2. Clean the spreadsheet. Normalize channel names and tier values, and flag rows with no requester ID. (45 min)
3. Bulk-import all 412 via CSV or API with source, tier and date set. I can write the script once you name the tracker. (30 min)
4. Run the area classification and the duplicate clustering. Output: a theme proposal with member rows. (about 1 hour, mostly unattended)
5. Review the clusters yourself and merge or split the wrong ones. This is the one step that needs your judgment. (2–3 hours)

**Week 2: shortlist**
1. Rank themes by distinct requesters, with enterprise weighted up. Pick the top 25–30.
2. Send Anika the shortlist. Ask her to size it S/M/L, and tell her it takes 30 minutes. This fits "take a look, nothing formal."
3. Set P0–P3 on the shortlist only.

**Week 3: planning prep**
1. Freeze the tracker.
2. Produce one page: top themes, demand counts, effort, and the tail of unprioritized items.

## Weekly digests to Anika

You are three weeks out, so that is 3 digests at most. Cheaper options:
- **Best:** a saved tracker view she can open any time, plus one short message per week with 3 lines: what changed, what you need from her, what is next.
- If she wants email, I can set up a scheduled job that drafts the digest from the tracker. You review and send it. Setup takes about 20 minutes.

Do not build a full report pipeline for 3 sends.

## Risks to know about

- ⚠️ **Booth and Discord rows probably carry no tier or identity.** Tier `unknown` is honest. Don't guess it.
- ⚠️ **Reading an LLM's area labels without spot-checking will hide errors.** Check at least 40 rows.
- ⚠️ **Nothing leaves the sheet if it contains customer names or emails,** unless the tracker is internal. Tell me before I run any script on it.

## Questions (reply with letters)

1. Which tracker? (Linear, Jira, GitHub Projects, Notion, other)
2. Does the spreadsheet have a requester ID or email column? (yes / no / only for support)
3. Is "weekly digest" Anika's request, or yours? If hers, what does she want in it?
4. Can the spreadsheet content go through a model (haiku) for classification? (yes / no / only after redaction)

Next: answer 1–4, then I write the import script for step 3.