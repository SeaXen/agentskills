# Pinewick devtools weekly: sponsor block and footer

I kept Lumora's "same font and layout" request and dropped two things:

- **The "Sponsored" tag stays.** Unlabeled paid copy styled as editorial is deceptive under FTC endorsement guidance and EU/French rules (the French LCEN requires ads to be identifiable). Your readers would also notice. A small label above the item still gives Lumora the native look. If they push back, "Presented by Lumora" is a softer wording that still discloses the paid placement.
- **"#1 fastest in the world" is cut.** It's an unsubstantiated superlative, and your newsletter carries the legal exposure for it. Ask Lumora for a benchmark link, and if they send one, use the second version below.

## Sponsor block

Use the same component as your editorial items: same heading size, body font, and link style. Add only the label line.

**Version A (safe, no claim needing proof):**

```markdown
<sub>SPONSORED · LUMORA</sub>

### Lumora: observability you can start on free

Lumora is an observability platform for metrics, logs, and traces. The free tier takes a few minutes to set up.

[Sign up free](SIGNUP_URL) · [Read the docs](DOCS_URL) · [See pricing](PRICING_URL)
```

**Version B (if Lumora sends a public, dated benchmark):**

```markdown
<sub>SPONSORED · LUMORA</sub>

### Lumora: fast observability, free to start

Lumora is an observability platform for metrics, logs, and traces. In [BENCHMARK_NAME, DATE](BENCHMARK_URL), it ranked fastest at [SPECIFIC_METRIC]. Start on the free tier.

[Sign up free](SIGNUP_URL) · [Read the docs](DOCS_URL) · [See pricing](PRICING_URL)
```

**Before sending:**
- Replace the three URLs and send Lumora the final copy for sign-off.
- I dropped "don't miss out!" because it's pressure copy that doesn't match your editorial voice. Put it back if Lumora insists.
- The "free tier takes a few minutes" line is my paraphrase of "Start free today". Check it with Lumora, or cut it to "Start free today."

## Bottom of the issue

Five equal asks compete with each other, and click-through usually drops when everything is a call to action. I ranked them by deadline and value, with one primary ask and the rest in a single row:

```markdown
---

**Join us live: Nov 14 webinar**
[TOPIC / one line on what attendees learn]. [Register →](WEBINAR_URL)

**Try Driftwood early**
The Driftwood beta is open. [Sign up for the beta →](DRIFTWOOD_URL)

[Star us on GitHub](GITHUB_URL) · [Join the Discord](DISCORD_URL) · [Follow on Bluesky](BLUESKY_URL)
```

Why this order:
1. **Webinar** comes first because it has a date. Registration is time-sensitive, and this is the only issue before Nov 14 that can reach everyone.
2. **Driftwood beta** is a product conversion, so it gets its own line.
3. **GitHub, Discord, and Bluesky** are low-effort, always-available asks. A single row keeps them from cluttering the page.

If your boss wants all five at equal weight, swap the last row for five separate lines. I'd advise against it.

**To confirm with you or your boss:**
- The webinar topic and time, so the line says something real.
- Whether the footer sits above or below the sponsor block. I'd put the sponsor block mid-issue, not directly above the footer, so it doesn't compete with your own asks.
- Your template format. This is Markdown. If you send from HTML or a tool like Beehiiv, Substack, or Buttondown, tell me and I'll convert it.