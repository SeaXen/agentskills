# Orbitkit: writer program vs. sponsored post, and Priya's Medium imports

## Do this first

1. **This week:** ask Priya for a 20-minute handoff call. Her access is the time-critical item (Part 2).
2. **This month:** don't pick one spend. Keep the four-writer program as the default and test the sponsored post only if the publication gives you hard numbers (Part 1).

---

## Part 1: Which gives better ROI?

### The cost is the same

Four articles at $300 is $1,200, the same as the one sponsored post. The question is whether four independent pieces beat one placement in a bigger room.

I can't compute ROI without your numbers. Here is how to decide.

### Metric

For an SDK, views aren't the outcome. Count **activated developers**: people who installed the package and evaluated a first flag. If you can't see activation, use npm installs plus signups from tracked links.

- **ROI per option** = activated developers attributed ÷ dollars spent.
- **Attribution rule, written before launch:** every piece gets its own UTM link, plus a landing path nobody else uses (for example `/start?src=writer-anna`). Count anyone who clicks and activates within 30 days.
- **Window:** 60 days. Articles keep earning after week one, but a sponsored post mostly doesn't.

### How the two compare

| | 4 writers ($1,200) | 1 sponsored post ($1,200) |
|---|---|---|
| Audience per piece | Small, the writer's followers, plus search | Large, the publication's readers and email list |
| Trust | Higher: reads as a peer's experience | Lower: labeled sponsored, and readers discount it |
| Shelf life | Longer: search keeps sending traffic | Short: a spike, then a tail |
| Variance | Spread over four bets, but quality varies by writer | One bet, and you can't redo it |
| Control | Low: it's on their account | Low to medium: the publication edits it |
| Fit for an SDK | Good if the piece shows real code and a real use case | Good only if the audience is JS developers who ship flags |

### My read

- **Default to the writers.** At equal cost you get four chances and more search surface, and peer posts convert better for developer tools than ads do. This is a judgment from how developers react to sponsored content, not a measured benchmark.
- **The sponsored post can win on reach.** A big JavaScript publication gives you an audience you can't reach otherwise. It only pays off if the audience is large and active.
- **Before you decide, ask the publication for:**
  1. The email list size and the typical views of their last 3 sponsored posts.
  2. Whether they publish clicks and read-through for past sponsors.
  3. Any makegood if the post underdelivers.
  4. Who writes it: you, or their staff.
- **Rule of thumb:** if they won't share past sponsored-post performance, treat the post as unproven and don't buy it this month.

### Make the writer program stronger

- **Brief each writer** with a use case, not "write about Orbitkit." Examples: migrating from a homegrown flag system, or flags in a Next.js app.
- **Review for accuracy** before publishing. Wrong code in a paid post hurts you.
- **Require disclosure** of the payment in each article. This is an FTC requirement and Medium's expectation.
- **Check paywalling.** If a writer is in Medium's Partner Program and paywalls the post, non-members can't read it. Ask for a free-access link or an unlocked post.
- **Pay on acceptance, not on views,** so quality is rewarded, not clicks.
- **Own a copy.** Ask for permission to republish on your docs or blog with a canonical link. Otherwise the asset belongs to the writer's account.

### Decision rule

After 60 days, compare cost per activated developer for the writers against the sponsored post. Put the result on the record before you spend more.

---

## Part 2: Priya's 12 imported posts

### The risk

The stories sit on Priya's personal account, and the publication depends on them. Loss paths:

1. **Her login is her work email.** Medium sign-in is often tied to an email address. When IT deletes her company mailbox, she may lose access, and so can you.
2. **She is the owner or an editor of the publication.** If she is the only admin, you can't manage it after she leaves.
3. **She removes or deletes the stories** (or the account) later, and the "backbone" of the publication disappears.
4. **Bylines and rights.** The stories carry her name, and the Medium account is hers, not the company's.

I'm not certain of every Medium detail (publication roles, account ownership transfer). Check these in Medium's publication settings and help pages before acting.

### Steps

1. **Check the publication's roles this week.** Who is the owner and who are editors? Make sure at least two company-controlled accounts hold the admin and editor roles. Do this before she leaves.
2. **Ask Priya to change her Medium login email** to a personal one before her company mailbox goes away. Do it as a request, because it's her account.
3. **Verify the canonical links.** Medium's import tool normally sets the canonical to the original blog URL. Confirm all 12 point at your site. If they do, SEO credit goes to your blog regardless of where the Medium copy lives.
4. **Decide the future of each story with Priya, in writing:**
   - **Option A (simplest): she leaves them published** and keeps them in the publication, or at least on her profile. She gets a portfolio. You get stable URLs. Ask for an email commitment not to delete.
   - **Option B (clean ownership): re-import the 12 posts from the company blog under a company-owned Medium account** (canonicals point to your blog), add them to the publication, then ask Priya to remove hers from the publication. Keep her originals published, because Medium has no redirects and deleting breaks inbound links.
5. **Check the employment agreement** on who owns work she wrote on company time. Don't lead with this. Use it only if she refuses a reasonable handoff.
6. **Check for Partner Program earnings.** If she paywalled any of the 12, she is earning from your content. Raise it openly rather than discovering it later.
7. **Update the bylines.** Decide whether the publication should say "Orbitkit Engineering" and credit her as a former engineer, and tell her so she agrees.

### Longer term

The same lesson as Part 1: you don't own content on someone else's account. Give the publication a company-owned owner account (a shared mailbox such as `eng-blog@`) and keep your blog as the canonical home.

---

## Questions that would sharpen this

- What did the publication say about audience size and past sponsored results?
- Can you see activation, or only npm downloads?
- Is Priya the publication's owner, or just a writer in it?
- Did she paywall any of the 12?