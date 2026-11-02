# Review: "Ingest pipelines just got simply amazing"

**Verdict: don't send as written.** The headline and body carry two numbers the source doesn't state and several hype words. The item also has four links where the template allows two. A corrected version follows, and it can go out at noon once the blocked lines below are cleared.

## What fails

| # | Problem | Rule | Fix |
|---|---|---|---|
| 1 | "cut costs by 40%": the paragraph you pasted says nothing about cost. | Source fidelity: no number the source doesn't state | Cut |
| 2 | "latency by half": the source says the *batch window* fell from 6 hours to 40 minutes, which is a different measure and a different size of change. | Source fidelity | Use the source's own figures and wording |
| 3 | "40%" may be a misreading of "40 minutes". | Source fidelity | Check the full post for a cost figure. If none exists, it stays out. |
| 4 | "simply amazing" is hype, and "simply" is patronising. | Tone pass | Cut. The headline says what the post claims. |
| 5 | "a great post" and "our friends" are editor endorsement, with no reason given. | Tone pass; item template (answer "why does this reader care?") | Replace with a line about the reader's work |
| 6 | "It's easy to set up, just follow their steps": "easy" and "just" are patronising. Your paragraph doesn't mention steps at all. | Tone pass; source fidelity | Cut |
| 7 | The item has four links: the post, `case-study`, `docs/streams` and `pricing`. The template allows one primary link plus one aside. | Item template | Keep the post and the docs link. Cut the case study and pricing. |
| 8 | "Read more here" is a non-descriptive link, and the headline isn't linked. | Item template | Link the headline |
| 9 | There is no author or organisation credit. | Item template | Add `Author (Selwyn)` |
| 10 | The `|` separator mashes three links into one line. | Item template | Replace with a one-line aside |

## Corrected item (Buttondown markdown)

```markdown
**[Selwyn: nightly batch window down from 6 hours to 40 minutes after moving to Quarrytide streams](https://selwyn.example/blog/etl-to-streams)**
Selwyn's team reports that after moving its nightly job onto Quarrytide streams, the batch window fell from 6 hours to 40 minutes and the on-call team stopped getting 3am pages for stuck jobs. Relevant if a slow nightly job is your main source of pages.
[AUTHOR NAME] (Selwyn) - to try it yourself, start with the [Quarrytide streams docs](https://quarrytide.example/docs/streams)
```

- **Body length:** 45 words, inside the 20–45 range.
- **Figures:** every one comes from your pasted paragraph. Both are attributed to Selwyn ("reports").
- **Source's wording:** the item says "nightly job", as the source does. Your draft's "ETL" appears only in the URL slug, so I left it out.
- **Percentages:** I added no percentage for the 6h→40min drop, because the source doesn't state one.

## Plain-text part

```
Selwyn: nightly batch window down from 6 hours to 40 minutes after moving to Quarrytide streams
https://selwyn.example/blog/etl-to-streams

Selwyn's team reports that after moving its nightly job onto Quarrytide streams, the batch window fell from 6 hours to 40 minutes and the on-call team stopped getting 3am pages for stuck jobs. Relevant if a slow nightly job is your main source of pages.
[AUTHOR NAME] (Selwyn) - to try it yourself, start with the Quarrytide streams docs:
https://quarrytide.example/docs/streams
```

## Pre-send report

| Check | Status |
|---|---|
| One primary link, descriptive link text | pass |
| Tone pass (editor-written prose) | pass after the fixes above |
| Factual claims trace to the source | pass for the pasted paragraph only |
| Author or source line | **blocked**: I need the author's name |
| Full Selwyn post read by a person | **blocked**: I only had the pasted paragraph, and the URLs are placeholders I can't open. Someone should confirm the headline fairly reflects the post. |
| Docs link (aside) read by a person | **blocked**: unread. It also needs to resolve through Buttondown's click-tracking domain in the test send. |
| Test send in Gmail, Apple Mail on a phone and classic Outlook, in light and dark mode | **blocked** on a human test send |
| Archive page matches the send | **blocked** until after sending |

Image and code-block checks don't apply, because this item has no images or code.

## Open questions

1. **Author name** for the credit line.
2. **Is a cost figure in the post or the case study?** If someone can point to the sentence, I'll add it back with attribution. Until then it stays out.
3. **Was the pricing link deliberate?** If you want a Quarrytide pricing or plan mention, it belongs in an own-release item with availability stated, not here.
4. **Is this the lead item?** If it is, I'll write the subject (about 45 characters) and the preview text. If it isn't, nothing changes.

If you can't clear the post and docs reads before noon, send the headline-only version. It's the Selwyn headline and the author credit, with no summary sentence. That keeps every unread claim out of the issue. I'd hold the item to the next issue rather than send the original wording.