## Audit: halvard-nyqvist profile README

### Critical issue: it will not render as written

None of the lines after the banner image are separated by a blank line, and none use list markers (`-`). In CommonMark (what GitHub uses), consecutive lines with no blank line between them collapse into a **single paragraph**, joined with spaces. So instead of the clean stacked look the emoji-prefixed lines are clearly meant to produce, the actual rendered output is going to look like this:

> ![banner](banner.png) Software engineer. I love building things and learning new technologies. 🔭 I'm currently working on something exciting 🌱 Learning Rust 📫 Reach me: halvard@nyqvist.dev [my blog](https://blog.nyqvist.dev)

One run-on wall of text, image and all, instead of a scannable list. This is the thing to fix — everything else is polish.

### Content issues

- **"I'm currently working on something exciting"** — this is unfilled template text, not a placeholder that reads as intentional. It signals "copied a template, never finished it" more than it signals mystery/intrigue. Either name the project (even vaguely — "a CLI tool," "something in the observability space") or cut the line entirely. Cutting it looks more finished than leaving it.
- **"Software engineer. I love building things and learning new technologies."** — generic boilerplate that could be any of a few million profiles. It doesn't tell a visitor what you actually work on (language, domain, stack). Combined with the placeholder line above, the profile currently gives zero concrete signal about your actual expertise — that's the pinned repos' job normally, but the bio text is free real estate being wasted.
- **No name in the heading.** "Hey there 👋" is fine stylistically, but pairing it with the handle-derived title only is a missed chance — most profile READMEs put the name right in the H1 for recruiters/collaborators skimming fast.
- **Public personal email.** `halvard@nyqvist.dev` in plain text will get scraped by bots. Common mitigation: obfuscate it, route through a contact form on the blog, or just rely on the blog link / GitHub's own "Contact" sidebar. Flagging this as a choice, not an error — if you're fine with the spam tradeoff, leave it.
- **Inconsistent formatting between lines.** Three lines use an emoji prefix (🔭🌱📫), the blog link doesn't. Once you fix the line-break issue, decide if the blog link gets a 🔗/📝 prefix to match, or if the whole set becomes a plain bullet list instead — either is fine, just be consistent.

### What's fine as-is

- The banner is a good instinct — visual break above the fold works.
- "🌱 Learning Rust" is genuinely useful: specific, current, gives visitors something to talk to you about.
- The overall brevity is appropriate for a personal profile — this doesn't need badges, stats widgets, or a table of projects. Sparse is fine; broken formatting and empty placeholder text are not.

### Minimal fix

```markdown
# Hey there, I'm Halvard 👋

![banner](banner.png)

Software engineer working on [specific thing, or cut this line].

- 🔭 Currently building **[name/description]**
- 🌱 Learning Rust
- 📫 Reach me: halvard@nyqvist.dev
- 📝 [Blog](https://blog.nyqvist.dev)
```

Blank line after the heading, blank line after the image, and the emoji lines turned into an actual list (`- `) so line breaks are guaranteed regardless of renderer quirks.

### On the pins

I didn't pull your live profile (fetching it needed a tool-approval step I didn't want to push through without you present), so I can't grade the specific repos GitHub picked. But the general answer to "is auto-picked good enough to leave alone" is **no, don't leave it on autopilot**. GitHub's default pin selection favors your most-starred or most-recently-active public repos — that's a popularity/recency signal, not a "best represents me" signal. It'll happily surface an old tutorial fork or a dead experiment if it happens to have more stars or a recent commit than your strongest work.

Curate the 6 slots manually for: one flagship/most-polished project, something that demonstrates your current focus (e.g., a Rust repo, tying back to the bio), and anything with a genuinely good README of its own — since a visitor who clicks through is about to judge that repo's README exactly the way this audit just judged your profile's.