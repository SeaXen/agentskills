# Promptwright Bluesky launch-week plan

Launch is Tuesday, called **T**. The plan covers T-5 through T+6. I changed three parts of your plan because each carries a real risk. Section 1 explains why and what replaces them.

## 1. Changes to your plan

| Your plan | Risk | Replacement |
|---|---|---|
| Daily AI-generated tip from the brand account | Bluesky users are openly hostile to AI-generated content. Your product is AI. A tip that reads as generic AI output is the likeliest source of a pile-on. | Keep the daily tip. A named human engineer writes or substantially edits each one. Each tip is grounded in a real PR finding, with a screenshot or diff. AI drafts are fine, and the human is the author. |
| CEO asks all 40 employees to like and repost in the first hour | A simultaneous burst from one org looks like coordinated inauthentic behavior. It can be flagged, and it skews your signal. Silent reposts also hide the affiliation. | Ask, don't instruct. Make it opt-in and stagger it across 24 hours. Employees add a personal line and disclose "I work at Promptwright". Likes and reposts come from people who use the product. |
| Pull every "code review" post from the firehose to build a prospect list and fine-tune on tone | Two separate problems (below). | Split into two paths (section 5). |

The firehose problem has two parts:
- **Fine-tuning:** Bluesky data is technically public. The community strongly objects to AI training on user posts, and the 2024 dataset backlash is the precedent. Quoting or imitating people's tone with a model also puts you in the same story as your product launch. Confirm the current Bluesky terms and developer policy with counsel before any use.
- **Prospect list:** handles and post content are personal data. Under GDPR you need a lawful basis, a privacy notice, and an opt-out. A mass-scraped list is hard to defend and is a bad first impression for a launch.

## 2. Decisions needed before T-5

1. **Confirm "next Tuesday"**: 2026-11-03 or 2026-11-10?
2. **Brand account owner and a named human voice** for the daily tips.
3. **Launch hook:** one claim you can demonstrate, such as a real bug caught on a real open-source PR. The hook is the post.
4. **Disclosure line for employees** (draft in section 4).
5. **Legal sign-off on the engineering data plan** (section 5).

## 3. Day-by-day plan

**T-5 to T-3: prepare**
- Complete the brand profile: handle, display name, bio, pinned post, link in the bio.
- Verify the domain as the handle, e.g. `promptwright.dev`, which gives a trust signal on Bluesky.
- Follow and engage with 30–50 relevant developers, maintainers and review-tooling people. Reply with substance, and don't pitch.
- Write the launch thread: hook post, a 20–30 second demo clip with alt text, a link, and one honest limitation.
- Write the 7 tips (T to T+6). For each, find a real PR finding first, then write it.
- Build the Starter Pack "Code review people". Don't add yourselves only. Include maintainers and tool builders.
- Brief employees (section 4).
- Draft the "AI use" policy line for your bio or pinned post, e.g. "Tips are written by [name]. AI drafts the code review comments in the product, not our posts."

**T-2 to T-1: dry run**
- Do a full rehearsal with the demo clip. Check the alt text, links, and previews.
- Prepare replies for the 5 likely objections: "another AI reviewer", privacy and code access, pricing, accuracy and false positives, and training on my code. Answer the training question with facts, in writing, before launch.
- Soft-seed the launch with 3–5 friendly developers who agreed to try it, so they can post honest takes after launch. Ask for honesty, not praise.

**T (launch day)**
- 9:00 local: pin the launch thread. Tip #1 goes out the same day, or about 3 hours later.
- Hour 1: the founders and the person behind the brand reply to every response personally. This matters more than the repost count.
- Employees engage across the day, staggered. Nobody gets a 10-minute window.
- Track in real time: replies, quote posts, the sentiment of negative replies, and product signups attributed by UTM link.
- Do not delete critical replies. Answer them.

**T+1 to T+5: sustain**
- One tip per day from the named human, built around a real finding.
- Alternate formats: a screenshot of a real finding, a short clip, a "here's what it got wrong" post (honest failures build trust), and a reply thread to a question people asked.
- Daily 30-minute community window: answer replies, thank people who posted real use.
- Retrospective check at T+3: if reply sentiment is negative on the tips, pause the cadence and answer questions instead.

**T+6: close out**
- Publish a short "what we learned from launch week" post with real numbers.
- Review metrics (section 6) and decide what to continue.

## 4. Employee participation

Send this to staff, from the CEO:

> We launch Promptwright on Bluesky on Tuesday. If you use the product and want to share it, please do, in your own words and on your own schedule. Say that you work at Promptwright. Participation is optional, nobody will check, and please don't repost without a line of your own.

Rules:
- Voluntary, with no tracking of who participated.
- Disclosure in every post ("I work at Promptwright").
- Staggered across T, not in the first hour.
- Likes and reposts only for content they actually agree with.

## 5. Engineering data plan

**Path A: listening (allowed, narrow)**
- Use Bluesky search, feeds, and the public API to find people asking about code review pain.
- Reply to them by hand, with something useful. Don't DM cold.
- Keep notes on themes (aggregate), not a database of individuals.

**Path B: tone (no scraping needed)**
- Build the style guide from your own docs, your own posts, and your named author.
- If you want external examples, study 10–20 public posts manually and write rules from them, with no ingestion.

**Path C: fine-tuning**
- Don't train on Bluesky users' posts. Use licensed data, your own data, or synthetic data.
- Get counsel to confirm Bluesky's current terms and any consent signals before deciding.

**If engineering still wants a firehose pipeline,** get a written decision first covering lawful basis, retention, a privacy notice, an opt-out path, and honoring deletions.

## 6. Metrics

| Metric | Why | Target |
|---|---|---|
| Replies to the launch post | Signal of interest beyond likes | Set from your follower baseline |
| Quote posts, positive vs negative | Shows reception, not just reach | Positive majority |
| Link clicks (UTM) | Intent | Track daily |
| Signups attributed | The real outcome | Track per day |
| Follower growth | Weak signal, so don't optimize for it | Track only |
| Inbound questions answered within 2 hours | Quality of engagement | 100% on T |

I deliberately left numeric targets blank. Set them from your current follower count and past product-launch results. I don't have either.

## 7. Risk register

| Risk | Likelihood | Mitigation |
|---|---|---|
| Backlash to AI-generated posts | High if unmitigated | Named human author, grounded tips, clear AI policy line |
| Coordinated-behavior flag | Medium | Opt-in, staggered, disclosed |
| Privacy complaint over scraping | Medium to high if run as originally planned | Replace with section 5 |
| "Does it train on my code?" thread | High | Prepare a clear, factual answer before T |
| Negative reply pile-on | Medium | Reply fast, concede real limits, don't delete |

## 8. Next step

Confirm the Tuesday date and the five decisions in section 2. After that I can draft the launch thread, the seven tips' structure, and the objection replies.