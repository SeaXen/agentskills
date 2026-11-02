# tidepool v1.0 launch: dev.to post, paid pinning, contributor listing

## Two things to know first

**1. dev.to doesn't sell homepage pinning.** Featured placement is editorial: the DEV team picks posts, and I know of no paid way to get it. I couldn't verify this live in this session, so confirm it with `support@dev.to` before you plan around it. Anyone offering to sell you a "featured" slot is probably a reseller or a scam, so don't pay them.

What money can buy on dev.to is sponsorship or ad inventory through their partnerships team. It's labeled as sponsored, it doesn't count as a pinned post, and it likely costs more than your budget allows.

**2. I'm unsure about two tags.** `#contributorswanted` may not be an established tag. A new tag works, but it has no audience, so it won't bring in readers. Keep `#opensource` and `#news`, and swap the last tag for one of these:
- `#productivity`, which you already have.
- `#cli`, `#devtools`, or your language tag (for example `#go` or `#rust`). I'd add one of these if you drop `#contributorswanted`.

dev.to allows 4 tags per post. If you keep `#contributorswanted`, say "contributors wanted" in the title or the first paragraph so people can find it.

## What to do with the budget

Pinning is out. Here is where a few thousand dollars does help:

| Spend | Est. cost | Why |
|---|---|---|
| Good-first-issue prep (10–15 labeled, scoped issues) | Time only | This is the main driver of contributions. |
| Short demo GIF or terminal recording | $0–$300 | It's the most-shared asset in a CLI post. |
| Cover image | $0–$200 | Posts with covers get more clicks. |
| Sponsor a newsletter slot in your language's community (Go Weekly, Console.dev, and similar) | $500–$1,500 | Targeted reach. Confirm current rates. |
| Hold the rest in reserve | The remainder | Use it after launch week for what worked, or for a contributor bounty or swag. |

For contributors, a pinned post matters less than a contributor-ready repo. Before Tuesday, check that you have a `CONTRIBUTING.md`, labeled `good first issue` and `help wanted` issues, and a working dev setup.

## The post

**Title:** tidepool v1.0 is open source, and we're looking for contributors

**Tags:** `opensource, news, productivity, contributorswanted` (see the tag note above)

**Cover image:** terminal screenshot or demo GIF

---

Today we're open-sourcing **tidepool**, our CLI for `<one-line description of what it does>`, and releasing v1.0.

### Why we built it

`<2–3 sentences: the problem you hit, in concrete terms. Name the workflow that was painful, not a generic "productivity" claim.>`

### What it does

```bash
# install
<install command>

# the 10-second demo
<the most impressive single command>
```

`<GIF or output of that command>`

- **`<Feature 1>`**: `<one line, what the user gets>`
- **`<Feature 2>`**: `<one line>`
- **`<Feature 3>`**: `<one line>`

### What v1.0 means

`<State your stability promise: for example, whether you follow semver and what you consider the public interface (flags, config format, output).>`

### Why open source

`<1–2 honest sentences: your reason, license name, and who maintains it.>`

### We want contributors

We've labeled issues you can pick up this week:

- [`good first issue`](`<link>`): small, scoped, with pointers to the right files
- [`help wanted`](`<link>`): larger pieces where we'd love another maintainer's eyes
- [`CONTRIBUTING.md`](`<link>`): setup in `<N>` minutes, how we review, and how fast we respond (`<your real target>`)

We also want to hear what's missing or broken. Open an issue, or tell us in the comments below.

### Links

- Repo: `<github.com/...>`
- Docs: `<link>`
- Install: `<command>`

If tidepool is useful to you, a star helps others find it. Questions, feedback and criticism are all welcome below.

---

Fill the `<...>` placeholders with real details. I don't know what tidepool does, so I didn't invent features or numbers.

## Contributor listing

I'm assuming you mean a dev.to Listing (a "collaborators wanted" type of post) or a similar contributor call. If you meant something else, tell me which platform. Reuse this text:

**Title:** Contributors wanted: tidepool, an open-source CLI for `<what it does>`

**Body:**
> tidepool v1.0 just went open source (`<license>`). We're looking for contributors for `<language>`, docs, and testing on `<OS/platforms>`. We've labeled `<N>` good first issues and review PRs within `<your real target>`. Repo: `<link>`. Read `CONTRIBUTING.md` first.

**Tags:** `opensource`, plus your language tag.

dev.to Listings may cost credits. I'm not sure the feature is still active, so check the Listings page in your account before Tuesday.

## Timeline

| When | Action |
|---|---|
| Fri 30 Oct – Mon 2 Nov | Prepare issues and `CONTRIBUTING.md`. Record the demo GIF. Save the post as a **draft** on dev.to. Email `support@dev.to` about featuring. |
| **Tue 3 Nov** | Cut the v1.0 tag and publish the post. Publish the listing once the post is live. Post the link to your own channels. |
| Tue – Fri | Answer every comment within a few hours. DEV staff do sometimes feature posts with strong early engagement, so replies help. |
| Following week | Review what drove traffic, then decide how to spend the reserve. |

## Questions that would sharpen this

1. What does tidepool do, and what language is it written in? That fills the placeholders and picks the right tag.
2. Which license are you using?
3. Do you want me to look up current dev.to ad and sponsorship rates? I can't confirm them from memory.