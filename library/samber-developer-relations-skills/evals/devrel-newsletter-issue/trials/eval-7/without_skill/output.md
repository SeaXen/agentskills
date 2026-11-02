Don't send as is. Three claims go beyond the Selwyn paragraph. Fixing them takes about 5 minutes.

## Problems, most severe first

1. ❌ **"Cut costs by 40%"** appears nowhere in the paragraph you quoted. Find it in the post and keep it only if it's there. If it's not, delete it.
2. ❌ **"Latency by half"** doesn't match the source. The source says the nightly batch window dropped from 6 hours to 40 minutes, about 89% shorter. That's a different metric, and "half" undersells it. Use their exact numbers.
3. ❌ **"Easy to set up, just follow their steps"** has no support in the paragraph. It promises a how-to, but the post may only be a retrospective. Verify the post has steps, or cut the line.
4. ⚠️ **Headline "simply amazing"** is hype, and "simply" implies ease, which is unproven. Lead with the real result instead.
5. ⚠️ **Four links in one item.** Pricing is unrelated to the story and reads as a sales push in a community roundup. The case-study link is unverified, so check it or drop it. Keep the post and the docs.
6. ⚠️ **"Read more here"** is a non-descriptive link label. The `|` also renders as literal text in Buttondown markdown.
7. ℹ️ **One customer's result.** Add a short note that it comes from their workload.
8. ℹ️ **"Our friends at Selwyn"** is fine if Selwyn is a partner or customer. If there's a commercial tie, say so.

## Replacement item

```markdown
**How Selwyn cut a 6-hour nightly batch to 40 minutes**

Selwyn moved their nightly ETL job onto Quarrytide streams. In their words: "we reduced our nightly batch window from 6 hours to 40 minutes, and the on-call team stopped getting 3am pages for stuck jobs." These are results from their own workload, so yours will vary.

[Read Selwyn's write-up](https://selwyn.example/blog/etl-to-streams) · [Quarrytide streams docs](https://quarrytide.example/docs/streams)
```

## Before noon

1. Open the Selwyn post. Look for the 40% cost figure and a step-by-step section. I didn't open it, so I can't confirm either.
2. If the cost figure is there, add this sentence after the quote: "They also report a 40% cost reduction."
3. If the post has steps, add "They walk through the migration steps" before the links.
4. Click both links in Buttondown's preview.

Next: check the Selwyn post for the cost figure and the steps. Paste what you find if you want me to adjust the copy.