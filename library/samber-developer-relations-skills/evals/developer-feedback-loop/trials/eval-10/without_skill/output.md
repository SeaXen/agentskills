I built both, with one change to your plan: the top five are labeled **"Most requested"**, not **"Coming soon"**. A public "coming soon" is a delivery promise made on product's behalf. Without a sign-off, you'd be committing the company in public to get around the head of product. The risks:

- Customers plan around the label, and sales will quote it.
- If product says no, you've created a public broken promise and a fight over who caused it.
- It can look like you forced a roadmap decision through the customer-facing side.

The labels below still make the pressure visible. Each item has a status that moves to "Coming soon" as soon as one named owner says yes, and that takes one reply.

## 1. Roadmap page (single file, drop-in)

Replace the `[…]` placeholders. Fill the vote counts from your tracker's export, not from memory.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Wrenfield Roadmap: what you asked for</title>
<meta name="description" content="The most requested Wrenfield features, ranked by community votes, with an honest status for each.">
<style>
  :root { --fg:#14181f; --muted:#5b6472; --line:#e3e6eb; --bg:#fff;
          --req:#8a5a00; --reqbg:#fff4d6; --plan:#0b5d3b; --planbg:#d9f4e6;
          --prog:#0b4a8f; --progbg:#dcebfd; --ship:#3b3f46; --shipbg:#eceef1; }
  * { box-sizing:border-box }
  body { margin:0; font:16px/1.55 system-ui,sans-serif; color:var(--fg); background:var(--bg) }
  main { max-width:760px; margin:0 auto; padding:48px 20px 80px }
  h1 { font-size:2rem; margin:0 0 8px }
  .lede { color:var(--muted); margin:0 0 32px }
  .legend { display:flex; flex-wrap:wrap; gap:8px 16px; font-size:.85rem; color:var(--muted); margin-bottom:24px }
  .card { border:1px solid var(--line); border-radius:12px; padding:20px; margin-bottom:14px; display:grid; grid-template-columns:72px 1fr; gap:16px }
  .votes { text-align:center; border-right:1px solid var(--line); padding-right:12px }
  .votes b { display:block; font-size:1.4rem }
  .votes span { font-size:.75rem; color:var(--muted) }
  h2 { font-size:1.1rem; margin:0 0 6px }
  .card p { margin:0 0 10px; color:var(--muted) }
  .badge { display:inline-block; font-size:.75rem; font-weight:600; padding:2px 10px; border-radius:99px }
  .requested { background:var(--reqbg); color:var(--req) }
  .planned   { background:var(--planbg); color:var(--plan) }
  .progress  { background:var(--progbg); color:var(--prog) }
  .shipped   { background:var(--shipbg); color:var(--ship) }
  .meta { font-size:.8rem; color:var(--muted); margin-left:8px }
  footer { margin-top:32px; font-size:.85rem; color:var(--muted) }
  a { color:#0b4a8f }
</style>
</head>
<body>
<main>
  <h1>What you asked for</h1>
  <p class="lede">The five most requested features from our community, ranked by votes. Votes show demand. They are not a delivery commitment. Each item shows its real status, and we update this page when a status changes.</p>

  <div class="legend">
    <span><span class="badge requested">Most requested</span> collecting votes, no decision yet</span>
    <span><span class="badge planned">Planned</span> owner assigned</span>
    <span><span class="badge progress">In progress</span> being built</span>
    <span><span class="badge shipped">Shipped</span></span>
  </div>

  <!-- Repeat per item. Votes: unique accounts only. Flip the badge to "planned" only after a named owner agrees. -->
  <article class="card">
    <div class="votes"><b>[480]</b><span>votes</span></div>
    <div>
      <h2>[Feature X]</h2>
      <p>[One sentence on the problem users describe, in their words.]</p>
      <span class="badge requested">Most requested</span>
      <span class="meta">Last reviewed [YYYY-MM-DD] · <a href="[request-thread-url]">Discuss</a></span>
    </div>
  </article>

  <article class="card">
    <div class="votes"><b>[###]</b><span>votes</span></div>
    <div>
      <h2>[Feature 2]</h2>
      <p>[Problem statement.]</p>
      <span class="badge requested">Most requested</span>
      <span class="meta">Last reviewed [YYYY-MM-DD] · <a href="[url]">Discuss</a></span>
    </div>
  </article>

  <!-- Features 3 to 5 follow the same pattern. -->

  <footer>
    Votes come from [source, e.g. the community forum], counted as unique accounts, as of [date].
    Missing something? <a href="[submit-url]">Submit a request</a>.
  </footer>
</main>
</body>
</html>
```

**Rules that keep the page defensible:**

1. Count unique accounts. Strip duplicates, bots, and employees.
2. Put the vote source and as-of date in the footer.
3. Show a "last reviewed" date on every card, so a stale page doesn't turn into a broken promise.
4. Write no dates and no quarters until an owner commits to them.

## 2. All-hands slide

**Title:** `Our top request: [Feature X]`

**Body (four lines):**

- **480 unique accounts** voted for [Feature X] on [source], since [date]
- It's #1 of the top five. Together, the five drew [N] votes.
- Voters include [N] paying customers, representing [$ARR or % of accounts].
- **Ask:** a 30-minute review of the top five with product, by [date].

**Visual:** a horizontal bar chart of the five vote counts, with Feature X highlighted. Don't use a pie chart.

**Speaker notes (about 60 seconds):**

> "Last week we published the community's top requests. Feature X leads with 480 votes. Here's who those voters are: [N] customers, [segment]. I'm not asking us to commit today. I'm asking product for 30 minutes to look at the top five and tell us yes, no, or not yet, with a reason. Whatever the answer is, we'll put it on the public page, so the community sees a decision instead of silence."

**Pre-empt the three questions you'll get:**

| Question | Prepare |
|---|---|
| "Is 480 a lot?" | Compare it with total active accounts, and with the votes on the #6 to #10 items. |
| "Do voters pay us?" | Join voter emails to the CRM and give an ARR figure. |
| "Is it feasible?" | Ask one engineer for a rough size (S/M/L) beforehand. |

## Before Thursday

1. **Join the 480 votes to account data.** Customer-weighted demand carries more weight with a head of product than a raw count. If most votes are free-tier, say so and don't claim otherwise.
2. **Tell the head of product before the all-hands.** A two-line heads-up ("public page goes live, I'll show the data Thursday, I'm asking for a 30-minute review") keeps this a proposal and not an ambush. If you ambush them in front of the company, they'll fight the data and not engage with it.
3. **Get the PMs on side.** You said they already talk to customers. Ask them to confirm or correct the problem statements on the cards. Their review adds credibility, and it routes around the "no standing review" objection without a formal process.
4. **Check the community's own rules.** Make sure publishing vote counts and feature names doesn't expose anything confidential, such as unreleased work or customer names.

**Decision for you:** if product signs off on any item before launch, flip it to **Planned**, with the owner's name internally. That's the only route to a public "coming soon", and it makes your all-hands pitch stronger, because you'd be presenting a decision.